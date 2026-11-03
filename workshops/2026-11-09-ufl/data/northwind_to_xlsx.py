"""Convert Microsoft's Northwind install script (instnwnd.sql) into workshop Excel files."""

import re
import sys
from pathlib import Path

import pandas as pd

STMT = re.compile(
    r'INSERT\s+(?:INTO\s+)?"(?P<table>[^"]+)"\s*(?:\((?P<cols>[^)]*)\))?\s*VALUES\s*\(',
    re.S,
)
# The script inserts order lines without a column list; this is the table's column order.
IMPLICIT_COLS = {
    "Order Details": ["OrderID", "ProductID", "UnitPrice", "Quantity", "Discount"],
    "Customers": ["CustomerID", "CompanyName", "ContactName", "ContactTitle", "Address", "City",
                  "Region", "PostalCode", "Country", "Phone", "Fax"],
}


def parse_values(text: str, pos: int) -> tuple[list, int]:
    """Parse a T-SQL VALUES tuple starting after '(' and return values and end position."""
    values, i = [], pos
    while True:
        while text[i] in " \t\r\n":
            i += 1
        if text.startswith("N'", i) or text[i] == "'":
            i += 2 if text[i] == "N" else 1
            buf = []
            while True:
                if text[i] == "'" and text[i + 1] == "'":
                    buf.append("'")
                    i += 2
                elif text[i] == "'":
                    i += 1
                    break
                else:
                    buf.append(text[i])
                    i += 1
            values.append("".join(buf))
        else:
            m = re.compile(r"[^,)]+").match(text, i)
            token = m.group().strip()
            i = m.end()
            if token.upper() == "NULL":
                values.append(None)
            elif token.startswith("0x"):
                values.append(None)  # binary photo data is not needed for the workshop
            else:
                try:
                    values.append(int(token))
                except ValueError:
                    values.append(float(token))
        while text[i] in " \t\r\n":
            i += 1
        if text[i] == ",":
            i += 1
            continue
        if text[i] == ")":
            return values, i + 1
        raise ValueError(f"unexpected character {text[i]!r} at {i}")


def load_tables(sql: str) -> dict[str, pd.DataFrame]:
    rows: dict[str, list] = {}
    cols: dict[str, list[str]] = {}
    for m in STMT.finditer(sql):
        table = m["table"]
        names = [c.strip().strip('"') for c in m["cols"].split(",")] if m["cols"] else IMPLICIT_COLS[table]
        vals, _ = parse_values(sql, m.end())
        if len(vals) != len(names):
            raise ValueError(f"{table}: {len(vals)} values for {len(names)} columns")
        cols[table] = names
        rows.setdefault(table, []).append(vals)
    return {t: pd.DataFrame(r, columns=cols[t]) for t, r in rows.items()}


def main(src: Path, out: Path) -> None:
    t = load_tables(src.read_text(encoding="utf-8", errors="replace"))
    for name in ("Orders",):
        for c in ("OrderDate", "RequiredDate", "ShippedDate"):
            t[name][c] = pd.to_datetime(t[name][c], format="%m/%d/%Y")
    emp = t["Employees"].drop(columns=["Photo", "PhotoPath"])
    for c in ("BirthDate", "HireDate"):
        emp[c] = pd.to_datetime(emp[c], format="%m/%d/%Y")
    books = {
        "bestellungen.xlsx": {"Orders": t["Orders"], "Order Details": t["Order Details"]},
        "produkte.xlsx": {"Products": t["Products"], "Categories": t["Categories"].drop(columns=["Picture"], errors="ignore"), "Suppliers": t["Suppliers"]},
        "kunden.xlsx": {"Customers": t["Customers"], "Shippers": t["Shippers"]},
        "mitarbeitende.xlsx": {"Employees": emp},
    }
    out.mkdir(parents=True, exist_ok=True)
    for fname, sheets in books.items():
        with pd.ExcelWriter(out / fname) as xw:
            for sheet, df in sheets.items():
                df.to_excel(xw, sheet_name=sheet, index=False)
        print(fname, {s: df.shape for s, df in sheets.items()})


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
