"""Check converted text against the ground truth in make_test_pdf.py.

Usage: python check_output.py

Compares the Docling Markdown with two naive extractions (pypdf and, if
available, pdftotext) and writes output/check-report.txt. All checks are
string comparisons against the generator's constants, so the report is
reproducible and does not depend on a model judging the output.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import make_test_pdf as gt

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "output"
NAIVE = OUTPUT / "naive"

# Ground truth per page, used for OCR word recall on the image-only page.
PAGE1_TEXTS = [
    gt.HEADER,
    gt.TITLE,
    gt.SUBTITLE,
    gt.H_SCOPE,
    gt.SCOPE_TEXT,
    gt.SCOPE_TEXT_2,
    gt.H_PRINCIPLES,
    *gt.PRINCIPLES,
    gt.H_TABLE,
    gt.TABLE_INTRO,
    *[c for row in gt.TABLE for c in row],
    gt.TABLE_OUTRO,
    gt.FOOTNOTE,
]


def norm(text: str) -> str:
    # Collapse whitespace and undo Markdown escaping and emphasis so that only
    # the wording is compared.
    text = text.replace("\\_", "_").replace("**", "")
    return re.sub(r"\s+", " ", text).strip()


def words(text: str) -> list[str]:
    return re.findall(r"[\wÄÖÜäöüß-]+", text.lower())


def naive_extract(pdf: Path) -> dict[str, str]:
    from pypdf import PdfReader

    out = {"pypdf": "\n".join(p.extract_text() or "" for p in PdfReader(pdf).pages)}
    if shutil.which("pdftotext"):
        for label, args in (("pdftotext", []), ("pdftotext-layout", ["-layout"])):
            res = subprocess.run(
                ["pdftotext", *args, "-enc", "UTF-8", str(pdf), "-"],
                capture_output=True,
                check=True,
            )
            out[label] = res.stdout.decode("utf-8")
    NAIVE.mkdir(parents=True, exist_ok=True)
    for label, text in out.items():
        (NAIVE / f"{pdf.stem}.{label}.txt").write_text(text, encoding="utf-8")
    return out


def check_full(name: str, raw: str, is_markdown: bool) -> list[str]:
    text = norm(raw)
    lines = raw.splitlines()
    report = [f"## {name}"]

    def found(s: str) -> bool:
        return norm(s) in text

    heading_lines = [
        norm(re.sub(r"^#+\s*", "", ln)) for ln in lines if ln.lstrip().startswith("#")
    ]
    heads_text = sum(found(h) for h in gt.HEADINGS)
    heads_md = sum(norm(h) in heading_lines for h in gt.HEADINGS)
    report.append(f"Überschriften als Text: {heads_text}/{len(gt.HEADINGS)}")
    if is_markdown:
        report.append(
            f"Überschriften als Markdown-Überschrift: {heads_md}/{len(gt.HEADINGS)}"
        )
        missing = [h for h in gt.HEADINGS if norm(h) not in heading_lines]
        if missing:
            report.append(f"  nicht als Überschrift: {missing}")

    items_text = sum(found(i) for i in gt.PRINCIPLES)
    item_re = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(.*)$")
    list_lines = [norm(m.group(1)) for ln in lines if (m := item_re.match(ln))]
    items_md = sum(norm(i) in list_lines for i in gt.PRINCIPLES)
    report.append(f"Listenpunkte als Text: {items_text}/{len(gt.PRINCIPLES)}")
    if is_markdown:
        report.append(
            f"Listenpunkte als Markdown-Liste: {items_md}/{len(gt.PRINCIPLES)}"
        )

    cells = [c for row in gt.TABLE for c in row]
    cells_text = sum(found(c) for c in cells)
    report.append(f"Tabellenzellen als Text: {cells_text}/{len(cells)}")
    if is_markdown:
        table_rows = [
            [norm(c) for c in ln.strip().strip("|").split("|")]
            for ln in lines
            if ln.strip().startswith("|")
        ]
        rows_ok = sum(
            row in table_rows for row in [[norm(c) for c in r] for r in gt.TABLE]
        )
        report.append(
            f"Tabellenzeilen exakt als Markdown-Tabellenzeile: {rows_ok}/{len(gt.TABLE)}"
        )

    report.append(f"Fußnotentext vorhanden: {found(gt.FOOTNOTE)}")
    paras = [
        gt.SUBTITLE,
        gt.SCOPE_TEXT,
        gt.SCOPE_TEXT_2,
        gt.TABLE_INTRO,
        gt.TABLE_OUTRO,
        *gt.PROCESS,
        gt.VIOLATIONS_TEXT,
    ]
    paras_ok = sum(found(p) for p in paras)
    report.append(f"Absätze wortgleich und zusammenhängend: {paras_ok}/{len(paras)}")
    broken = [p[:40] for p in paras if not found(p)]
    if broken:
        report.append(f"  nicht zusammenhängend: {broken}")

    header_hits = text.count(norm(gt.HEADER))
    footer_hits = len(re.findall(rf"{gt.FOOTER_PREFIX} \d+ von \d+", text))
    report.append(
        f"Kopfzeile im Text: {header_hits}x, Fußzeile mit Seitenzahl im Text: {footer_hits}x"
    )

    leads = [p.split(". ", 1)[0] + "." for p in gt.PROCESS]
    positions = [text.find(norm(lead)) for lead in leads]
    in_order = all(p >= 0 for p in positions) and positions == sorted(positions)
    report.append(
        f"Lesereihenfolge zweispaltiger Teil korrekt: {in_order} (Positionen {positions})"
    )
    # Order within the columns is not enough: the following section must also
    # come after the last column paragraph, otherwise the right column ends up
    # under the wrong heading.
    next_pos = text.find(norm(gt.H_VIOLATIONS))
    after = next_pos > max(positions)
    report.append(
        f"Abschnitt 5 steht nach dem zweispaltigen Teil: {after} (Position {next_pos})"
    )
    return report


def check_scan(name: str, raw: str) -> list[str]:
    expected = words(" ".join(PAGE1_TEXTS))
    got = set(words(raw))
    hit = sum(w in got for w in expected)
    cells = [c for row in gt.TABLE for c in row]
    return [
        f"## {name}",
        f"Zeichen im Ergebnis: {len(raw.strip())}",
        f"Wortrecall gegenüber Seite 1: {hit}/{len(expected)} ({hit / len(expected):.0%})",
        f"Überschriften wortgleich: {sum(norm(h) in norm(raw) for h in gt.HEADINGS[:4])}/4",
        f"Listenpunkte wortgleich: {sum(norm(i) in norm(raw) for i in gt.PRINCIPLES)}/{len(gt.PRINCIPLES)}",
        f"Tabellenzellen wortgleich: {sum(norm(c) in norm(raw) for c in cells)}/{len(cells)}",
        f"Markdown-Tabelle vorhanden: {any(ln.strip().startswith('|') for ln in raw.splitlines())}",
        f"Fußnotentext wortgleich: {norm(gt.FOOTNOTE) in norm(raw)}",
    ]


def main() -> int:
    md = OUTPUT / f"{gt.PDF.stem}.md"
    md_scan = OUTPUT / f"{gt.SCAN_PDF.stem}.md"
    if not md.is_file():
        print("run convert.py first", file=sys.stderr)
        return 1
    report = ["# Prüfbericht PDF zu Markdown", ""]
    report += [
        *check_full(f"Docling: {md.name}", md.read_text(encoding="utf-8"), True),
        "",
    ]
    for label, text in naive_extract(gt.PDF).items():
        report += [*check_full(f"naiv {label}: {gt.PDF.name}", text, False), ""]
    if md_scan.is_file():
        report += [
            *check_scan(
                f"Docling: {md_scan.name}", md_scan.read_text(encoding="utf-8")
            ),
            "",
        ]
    # The scan PDF is a versioned fixture; a clone that lacks it still gets the text-PDF checks.
    if gt.SCAN_PDF.is_file():
        for label, text in naive_extract(gt.SCAN_PDF).items():
            report += [*check_scan(f"naiv {label}: {gt.SCAN_PDF.name}", text), ""]
    else:
        print(
            f"{gt.SCAN_PDF.name} not found in input/, naive scan checks skipped; "
            "make_test_pdf.py regenerates it (needs Word on Windows and PyMuPDF)",
            file=sys.stderr,
        )
    out = "\n".join(report)
    (OUTPUT / "check-report.txt").write_text(out, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
