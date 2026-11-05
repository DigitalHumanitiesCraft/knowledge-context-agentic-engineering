# /// script
# requires-python = ">=3.11"
# dependencies = ["openpyxl"]
# ///
"""Redact an incoming customer mail and its staff spreadsheet locally before a cloud agent sees them.

Workshop demo for Uni for Life 2026 (session on agentic engineering and governance). Single-file
script regime: stdlib plus openpyxl, no project manifest.

Data flow, three stages:

1. Deterministic script. Recipient display names from the An/Cc header lines (and their other
   occurrences in the text), e-mail addresses, phone numbers with extensions and postal addresses
   are replaced by placeholders. The spreadsheet is rewritten with an allowlist of columns, so a
   column nobody classified is dropped rather than passed on.
2. Local LLM via Ollama. The model only *finds* the remaining spans (third-party names, sentences
   on personal circumstances) and returns them as JSON. The script replaces them verbatim. The
   model never rewrites the mail, so it cannot silently change retained text, and a span it
   invents that does not occur in the mail is rejected and listed.
3. Deterministic check. Known strings that must not survive and content that must survive
   (pruefliste.json, specific to the test mail), plus generic checks that need no list: a regex
   re-scan, the staff names read from the spreadsheet, and a cell comparison of the cleaned
   spreadsheet. The result is a release template (freigabe.md) for a human.

Usage:
    python redact_mail.py
    python redact_mail.py --model qwen3.5:9b --model ministral-3:8b --runs 2
    python redact_mail.py --mail eigene.txt [--xlsx anhang.xlsx] [--checklist liste.json] --out DIR

Without --mail the script runs on the test mail with its spreadsheet and checklist. A variant
under testmails/ gets the spreadsheet by default and its checklist via --checklist. An own mail
gets neither by default, so the test fixtures never stand in for its own attachment or list.

Outputs go to ./ausgabe. With several models or runs, the primary outputs come from the first
run of the first model, and messungen.json records every run. Exit code 0 means that no known
string leaked, no generic check found anything and no content that must stay was lost.

Trust boundary: the release template and messungen.json hold the removed original strings and
the raw model answers, so they stay local and never go to the cloud agent. The console prints
only the model, run times, counts, a checksum prefix and the output folder, because a cloud
agent that started the run reads the console.
"""

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook, load_workbook

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1] / "data"
# 127.0.0.1 instead of localhost: on Windows the IPv6 attempt first costs about two seconds per call.
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

# Allowlist instead of a blocklist: a column added to the export later is dropped by default.
# Names are dropped too, because orders reference staff by EmployeeID, which suffices for analysis.
KEEP_COLUMNS = frozenset({"EmployeeID", "Title", "HireDate", "ReportsTo"})

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
EXTENSION = re.compile(
    r"(?i)\b(Durchwahl|Durchw\.|DW|Klappe|Nebenstelle|ext\.|extension)([ \t]*:?[ \t]*)(\d{1,6})\b"
)
# Dots are not separators, otherwise dates such as 08.11.2026 would count as phone numbers.
PHONE = re.compile(
    r"(?<!\w)(?:\+\d{1,3}[ /-]?)?(?:\(\d{1,5}\)[ /-]?)?\d{2,5}(?:[ /-]\d{2,8}){1,4}(?!\w)"
)
YEAR = re.compile(r"(?:19|20)\d\d")
US_STREET = re.compile(
    r"^[ \t]*\d{1,6}[ \t]+(?:[NSEW]\.?[ \t]+)?(?:[A-Z][\w.'-]*[ \t]+)*?"
    r"(?:Way|Rd|Road|St|Street|Ave|Avenue|Blvd|Boulevard|Ln|Lane|Dr|Drive|Ct|Court|Pl|Place|Hill|Hwy)\.?"
    r"(?:[ \t]+(?:Apt|Suite|Ste)\.?[ \t]*\w+)?[ \t]*$",
    re.MULTILINE,
)
US_CITY = re.compile(
    r"^[ \t]*[A-Z][A-Za-z .'-]*,[ \t]*[A-Z]{2}[ \t]+\d{5}(?:-\d{4})?(?:,[ \t]*[A-Za-z .]+)?[ \t]*$",
    re.MULTILINE,
)
DE_STREET = re.compile(
    r"\b[A-ZÄÖÜ][\w.-]*(?:straße|strasse|str\.|gasse|weg|platz|allee|ring|ufer|damm|kai|zeile)"
    r"[ \t]+\d{1,4}[a-z]?(?:/\d+)*(?:,[ \t]*(?:[A-Z]{1,2}-)?\d{4,5}[ \t]+[A-ZÄÖÜ][\w-]+)?"
)
DE_CITY = re.compile(
    r"^[ \t]*(?:[A-Z]{1,2}-)?\d{4,5}[ \t]+[A-ZÄÖÜ][\w .-]*$", re.MULTILINE
)
RECIPIENT_HEADER = re.compile(
    r"^(An|Cc|Bcc|Kopie|To)[ \t]*:(.*)$", re.MULTILINE | re.IGNORECASE
)
SENDER_HEADER = re.compile(
    r"^(?:Von|From)[ \t]*:[ \t]*(.*?)[ \t]*<", re.MULTILINE | re.IGNORECASE
)

SYSTEM_PROMPT = """Du prüfst eine E-Mail, bevor sie an einen externen Dienst weitergegeben wird. Telefonnummern, E-Mail-Adressen und Postadressen sind bereits durch Platzhalter in eckigen Klammern ersetzt. Deine Aufgabe ist, die verbleibenden Stellen zu finden, die etwas über einzelne Personen verraten.

Antworte nur mit JSON der Form {"personen": [...], "umstaende": [...]}.

personen: jeder Name einer Person außer dem Absender, genau so geschrieben wie im Text.

umstaende: jeder vollständige Satz, der
- persönliche Umstände einer Person nennt, etwa Gesundheit, Krankheit, Schwangerschaft, Elternzeit, Pension, Ruhestand, Urlaub, Familie, Kündigung oder Leistung, oder
- auf private Daten hinweist, etwa Geburtsdaten, Privatadressen, private Telefonnummern oder Gehälter.
Kopiere jeden Satz Zeichen für Zeichen aus dem Text, vom ersten Wort bis zum Satzzeichen am Ende.

Nimm nicht auf: den Absender, Firmennamen, Ortsnamen, Produkte, Berufsbezeichnungen und Platzhalter in eckigen Klammern. Wenn nichts zutrifft, gib leere Listen zurück."""

SPAN_SCHEMA = {
    "type": "object",
    "properties": {
        "personen": {"type": "array", "items": {"type": "string"}},
        "umstaende": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["personen", "umstaende"],
}


@dataclass
class Redaction:
    stage: str
    category: str
    original: str
    placeholder: str


@dataclass
class RunResult:
    model: str
    run: int
    text: str
    redactions: list[Redaction] = field(default_factory=list)
    rejected: list[str] = field(default_factory=list)
    seconds_llm: float = 0.0
    ollama: dict = field(default_factory=dict)
    checks: dict = field(default_factory=dict)


def _sub(
    pattern: re.Pattern,
    text: str,
    category: str,
    placeholder: str,
    log: list[Redaction],
    stage: str = "1 Skript",
) -> str:
    def repl(m: re.Match) -> str:
        log.append(Redaction(stage, category, m.group(0).strip(), placeholder))
        return placeholder

    return pattern.sub(repl, text)


def _sender_name(text: str) -> str:
    m = SENDER_HEADER.search(text)
    return m.group(1).strip().strip('"') if m else ""


def _recipient_names(text: str, sender: str) -> list[str]:
    names = []
    for m in RECIPIENT_HEADER.finditer(text):
        for part in m.group(2).split(","):
            nm = re.match(r"\s*\"?([^\"<>]+?)\"?\s*<[^>]*@[^>]*>", part)
            if nm and nm.group(1).strip() != sender:
                names.append(nm.group(1).strip())
    return names


def _redact_phone(text: str, log: list[Redaction]) -> str:
    def repl(m: re.Match) -> str:
        digits = re.sub(r"\D", "", m.group(0))
        groups = re.findall(r"\d+", m.group(0))
        # Year lists and ranges ("1996-1998") look like numbers with separators but are no phones.
        if not 7 <= len(digits) <= 15 or all(YEAR.fullmatch(g) for g in groups):
            return m.group(0)
        log.append(Redaction("1 Skript", "Telefon", m.group(0), "[TELEFON]"))
        return "[TELEFON]"

    return PHONE.sub(repl, text)


def stage1_mail(text: str) -> tuple[str, str, list[Redaction]]:
    """Return the deterministically redacted mail, the sender name and the redaction log."""
    log: list[Redaction] = []
    sender = _sender_name(text)
    # Header names first, while the addresses that mark them are still intact.
    for name in _recipient_names(text, sender):
        text = _sub(
            re.compile(re.escape(name)), text, "Name (Kopfzeile)", "[NAME]", log
        )
    text = _sub(EMAIL, text, "E-Mail", "[E-MAIL]", log)

    def ext_repl(m: re.Match) -> str:
        log.append(
            Redaction("1 Skript", "Telefon (Durchwahl)", m.group(0), "[TELEFON]")
        )
        return f"{m.group(1)}{m.group(2)}[TELEFON]"

    text = EXTENSION.sub(ext_repl, text)
    text = _redact_phone(text, log)
    for pattern in (US_STREET, US_CITY, DE_STREET, DE_CITY):
        text = _sub(pattern, text, "Postadresse", "[ADRESSE]", log)
    return text, sender, log


def stage1_workbook(src: Path, dst: Path) -> dict:
    """Write a copy of the workbook that holds only allowlisted columns, and report what was dropped."""
    wb = load_workbook(src, data_only=True)
    out = Workbook()
    out.remove(out.active)
    report: dict = {
        "datei": src.name,
        "blaetter": [],
        "entfernte_werte": set(),
        "namen": [],
    }
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        header = [str(h) if h is not None else "" for h in rows[0]]
        keep_idx = [i for i, h in enumerate(header) if h in KEEP_COLUMNS]
        drop_idx = [i for i in range(len(header)) if i not in keep_idx]
        new = out.create_sheet(ws.title)
        for row in rows:
            new.append([row[i] for i in keep_idx])
        for row in new.iter_rows(min_row=2):
            for cell in row:
                if isinstance(cell.value, datetime):
                    cell.number_format = "yyyy-mm-dd"
        for row in rows[1:]:
            for i in drop_idx:
                if row[i] is not None:
                    report["entfernte_werte"].add(str(row[i]))
        if "FirstName" in header and "LastName" in header:
            fi, li = header.index("FirstName"), header.index("LastName")
            report["namen"] += [
                (str(r[fi]), str(r[li])) for r in rows[1:] if r[fi] and r[li]
            ]
        report["blaetter"].append(
            {
                "blatt": ws.title,
                "zeilen": len(rows) - 1,
                "behalten": [header[i] for i in keep_idx],
                "entfernt": [header[i] for i in drop_idx],
                "fehlende_erlaubte": sorted(KEEP_COLUMNS - set(header)),
            }
        )
    # A fresh workbook carries no document properties, comments or styles from the source.
    out.save(dst)
    return report


def _ollama_chat(model: str, user: str) -> tuple[str, dict]:
    body = json.dumps(
        {
            "model": model,
            "stream": False,
            "think": False,
            "format": SPAN_SCHEMA,
            "options": {"temperature": 0},
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
        }
    ).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=body, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = json.loads(r.read())
    except (urllib.error.URLError, TimeoutError) as e:
        raise SystemExit(
            f"Stufe 2: Ollama unter {OLLAMA_URL} nicht erreichbar oder Modell {model} fehlt ({e})."
        ) from e
    meta = {
        k: data.get(k)
        for k in (
            "total_duration",
            "load_duration",
            "prompt_eval_count",
            "eval_count",
            "eval_duration",
        )
    }
    return data["message"]["content"], meta


def _parse_spans(raw: str) -> dict | None:
    """Distrust the model output: strip fences, cut to the outer braces, accept only lists of strings."""
    raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.MULTILINE)
    start, end = raw.find("{"), raw.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        data = json.loads(raw[start : end + 1])
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    return {
        key: [s.strip() for s in data.get(key, []) if isinstance(s, str) and s.strip()]
        for key in ("personen", "umstaende")
    }


def _find_span(text: str, span: str) -> re.Pattern | None:
    exact = re.compile(re.escape(span))
    if exact.search(text):
        return exact
    # The model may reflow whitespace across a line break or "correct" the case of a misspelled
    # name; rejecting such a span would let the original pass, so both are tolerated.
    loose = re.compile(
        r"\s+".join(re.escape(tok) for tok in span.split()), re.IGNORECASE
    )
    return loose if loose.search(text) else None


def stage2_llm(text: str, sender: str, model: str, run: int) -> RunResult:
    user = f"Absender: {sender}\n\nE-Mail:\n{text}"
    t0 = time.perf_counter()
    raw, meta = _ollama_chat(model, user)
    spans = _parse_spans(raw)
    if spans is None:
        # One retry for invalid JSON; anything else is a hard failure of this run.
        raw, meta = _ollama_chat(model, user)
        spans = _parse_spans(raw)
    seconds = time.perf_counter() - t0
    result = RunResult(
        model, run, text, seconds_llm=seconds, ollama=meta | {"roh": raw}
    )
    if spans is None:
        result.rejected.append(
            "Antwort war zweimal kein gültiges JSON, Stufe 2 ohne Wirkung."
        )
        return result
    items = [(s, "Umstand", "[PERSÖNLICH]") for s in spans["umstaende"]] + [
        (s, "Name", "[NAME]") for s in spans["personen"]
    ]
    # Longest first, so a name inside an already removed sentence is not reported twice.
    for span, category, placeholder in sorted(items, key=lambda x: -len(x[0])):
        if sender and span in sender:
            result.rejected.append(f"Absender nicht entfernt: {span!r}")
            continue
        if re.fullmatch(r"\[[A-ZÄÖÜ -]+\]", span) or "\n\n" in span:
            result.rejected.append(
                f"Platzhalter oder mehr als ein Absatz, verworfen: {span[:80]!r}"
            )
            continue
        pattern = _find_span(result.text, span)
        if pattern is None:
            # A name inside a sentence removed just before is covered, not invented.
            if _find_span(text, span) is None:
                result.rejected.append(f"Nicht wörtlich im Text, verworfen: {span!r}")
            continue
        result.text = _sub(
            pattern,
            result.text,
            category,
            placeholder,
            result.redactions,
            stage="2 LLM",
        )
    return result


def stage3_check(
    original: str,
    after1: str,
    final: str,
    checklist: dict,
    workbook: dict | None,
    wb_out: Path | None,
    sender: str,
) -> dict:
    def status_forbidden(s: str) -> str:
        if s not in original:
            return "nicht in der Mail"
        if s not in after1:
            return "entfernt durch Skript"
        return "entfernt durch LLM" if s not in final else "DURCHGELASSEN"

    forbidden = {
        s: status_forbidden(s) for s in checklist.get("darf_nicht_ueberleben", [])
    }
    keep = {}
    for s in checklist.get("muss_erhalten_bleiben", []):
        if s not in original:
            keep[s] = "nicht in der Mail"
        elif s not in after1:
            keep[s] = "VERLOREN durch Skript"
        else:
            keep[s] = "erhalten" if s in final else "VERLOREN durch LLM"

    generic = {}
    generic["E-Mail-Muster"] = EMAIL.findall(final)
    generic["Telefon-Muster"] = [
        m.group(0)
        for m in PHONE.finditer(final)
        if len(re.sub(r"\D", "", m.group(0))) >= 7
    ]
    if workbook is not None and wb_out is not None:
        # The staff list is a name list the check gets for free; first names count, since mails use them.
        sender_parts = set(sender.split())
        names = []
        for first, last in workbook["namen"]:
            if f"{first} {last}" == sender:
                continue
            for needle in (f"{first} {last}", first, last):
                if needle not in sender_parts and re.search(
                    rf"\b{re.escape(needle)}\b", final
                ):
                    names.append(needle)
        generic["Namen aus der Mitarbeiterliste"] = sorted(set(names))

        out_values = set()
        for ws in load_workbook(wb_out, data_only=True).worksheets:
            for row in ws.iter_rows(values_only=True):
                out_values |= {str(v) for v in row if v is not None}
        generic["Entfernte Tabellenwerte in der bereinigten Kopie"] = sorted(
            workbook["entfernte_werte"] & out_values
        )

    leaked = [s for s, st in forbidden.items() if st == "DURCHGELASSEN"] + [
        f"{k}: {v}" for k, vs in generic.items() for v in vs
    ]
    lost = [s for s, st in keep.items() if st.startswith("VERLOREN")]
    return {
        "verboten": forbidden,
        "erhalten": keep,
        "allgemein": generic,
        "durchgelassen": leaked,
        "verloren": lost,
    }


def _unprocessed_attachments(text: str, processed: set[str]) -> list[str]:
    m = re.search(
        r"^(?:Anhänge|Anhang|Attachments)[ \t]*:(.*)$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    if not m:
        return []
    return [
        a.strip()
        for a in m.group(1).split(",")
        if a.strip() and a.strip() not in processed
    ]


def _release_template(
    res: RunResult,
    stage1_log: list[Redaction],
    wb_report: dict | None,
    unprocessed: list[str],
    seconds1: float,
    mail_name: str,
) -> str:
    c = res.checks
    ok = not c["durchgelassen"] and not c["verloren"]
    lines = [
        f"# Freigabevorlage für {mail_name}",
        "",
        "Nur lokal verwenden. Diese Datei enthält die entfernten Originalstellen. An den Cloud-Agenten geht allein die bereinigte Mail und die bereinigte Tabelle.",
        "",
        f"- Erstellt: {datetime.now().isoformat(timespec='seconds')}",
        f"- Modell Stufe 2: {res.model} (Ollama, lokal, temperature 0), Prompt-Hash {hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest()[:12]}",
        f"- Laufzeit: Stufe 1 {seconds1 * 1000:.0f} ms, Stufe 2 {res.seconds_llm:.1f} s",
        f"- Automatische Prüfung: {'bestanden' if ok else 'NICHT bestanden'}",
        "",
        "## Prüfergebnis",
        "",
        f"- Durchgelassen: {', '.join(c['durchgelassen']) or 'nichts'}",
        f"- Verloren: {', '.join(c['verloren']) or 'nichts'}",
        "",
        "Bestanden heißt nur, dass keine der bekannten Stellen durchgerutscht ist. Was weder Prüfliste noch Muster kennen, findet allein der Mensch beim Lesen.",
        "",
        "### Prüfliste dieser Mail",
        "",
    ]
    lines += [f"- {s}: {st}" for s, st in c["verboten"].items()]
    lines += [f"- {s}: {st}" for s, st in c["erhalten"].items()]
    if not c["verboten"] and not c["erhalten"]:
        lines.append(
            "- Keine Prüfliste übergeben, es liefen nur die allgemeinen Prüfungen."
        )
    lines += ["", "### Allgemeine Prüfungen", ""]
    lines += [
        f"- {k}: {', '.join(v) if v else 'keine Treffer'}"
        for k, v in c["allgemein"].items()
    ]
    lines += ["", "## Entfernte Stellen", ""]
    lines += [
        f"- Stufe {r.stage}, {r.category}: {r.original!r} ersetzt durch {r.placeholder}"
        for r in stage1_log + res.redactions
    ]
    if res.rejected:
        lines += ["", "## Vorschläge des Modells, nicht übernommen", ""]
        lines += [f"- {r}" for r in res.rejected]
    lines += ["", "## Anhänge", ""]
    for sheet in wb_report["blaetter"] if wb_report else []:
        lines.append(
            f"- {wb_report['datei']}, Blatt {sheet['blatt']} ({sheet['zeilen']} Zeilen): behalten {', '.join(sheet['behalten'])}; entfernt {', '.join(sheet['entfernt'])}"
        )
    for name in unprocessed:
        lines.append(
            f"- {name}: NICHT bearbeitet, vor der Weitergabe selbst prüfen oder weglassen"
        )
    lines += ["", "## Bereinigte Mail", "", "```text", res.text.rstrip(), "```", ""]
    lines += [
        "## Freigabe",
        "",
        "- [ ] Bereinigte Mail vollständig gelesen",
        "- [ ] Keine weiteren Angaben zu Personen gefunden",
        "- [ ] Nicht bearbeitete Anhänge geprüft oder entfernt",
        "",
        "Freigegeben durch: ______________________  Datum: ____________",
        "",
    ]
    return "\n".join(lines)


def _summary_line(res: RunResult) -> str:
    """One console line per run, with counts only.

    The console is what a cloud agent sees when it started the run, and the leaked or lost
    strings are exactly the content that must not reach it. They stay in freigabe.md.
    """
    load_s = (res.ollama.get("load_duration") or 0) / 1e9
    return (
        f"{res.model} Lauf {res.run}: Stufe 2 {res.seconds_llm:.1f} s (Ladezeit {load_s:.1f} s), "
        f"durchgelassen {len(res.checks['durchgelassen'])}, verloren {len(res.checks['verloren'])}, "
        f"sha256 {hashlib.sha256(res.text.encode()).hexdigest()[:12]}"
    )


def _inputs(
    mail: Path | None, xlsx: Path | None, checklist: Path | None
) -> tuple[Path, Path | None, Path | None]:
    """Fill in the test fixtures for the test data only.

    An own mail without --xlsx or --checklist runs without them; otherwise the staff list and
    the checklist of the test mail would silently stand in for its own and report on them.
    The variants under testmails/ attach the same staff list, so it stays their default; each
    has its own checklist, which is passed explicitly.
    """
    if mail is None:
        return (
            DATA / "kundenanfrage.txt",
            xlsx or DATA / "mitarbeitende.xlsx",
            checklist or HERE / "pruefliste.json",
        )
    if mail.resolve().is_relative_to(HERE / "testmails"):
        return mail, xlsx or DATA / "mitarbeitende.xlsx", checklist
    return mail, xlsx, checklist


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Mail und Mitarbeiterliste lokal bereinigen, prüfen und zur Freigabe vorlegen."
    )
    ap.add_argument(
        "--mail",
        type=Path,
        help="eigene Mail (Standard: Testmail mit Tabelle und Prüfliste)",
    )
    ap.add_argument("--xlsx", type=Path, help="Excel-Anhang der Mail, optional")
    ap.add_argument("--checklist", type=Path, help="Prüfliste als JSON, optional")
    ap.add_argument(
        "--model",
        action="append",
        help="Ollama-Modell, mehrfach möglich (Standard qwen3.5:9b)",
    )
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--out", type=Path, default=HERE / "ausgabe")
    args = ap.parse_args()
    models = args.model or ["qwen3.5:9b"]
    mail, xlsx, checklist_path = _inputs(args.mail, args.xlsx, args.checklist)
    for p in (mail, xlsx, checklist_path):
        if p is not None and not p.is_file():
            raise SystemExit(f"Eingabe fehlt: {p}")
    checklist = (
        json.loads(checklist_path.read_text(encoding="utf-8")) if checklist_path else {}
    )
    out = args.out
    out.mkdir(parents=True, exist_ok=True)

    original = mail.read_text(encoding="utf-8")
    t0 = time.perf_counter()
    after1, sender, log1 = stage1_mail(original)
    wb_out = out / f"{xlsx.stem}_bereinigt.xlsx" if xlsx else None
    wb_report = stage1_workbook(xlsx, wb_out) if xlsx and wb_out else None
    seconds1 = time.perf_counter() - t0
    unprocessed = _unprocessed_attachments(original, {xlsx.name} if xlsx else set())

    results: list[RunResult] = []
    for model in models:
        for run in range(1, args.runs + 1):
            res = stage2_llm(after1, sender, model, run)
            res.checks = stage3_check(
                original, after1, res.text, checklist, wb_report, wb_out, sender
            )
            results.append(res)
            print(_summary_line(res))

    primary = results[0]
    (out / f"{mail.stem}_bereinigt.txt").write_text(primary.text, encoding="utf-8")
    (out / "freigabe.md").write_text(
        _release_template(primary, log1, wb_report, unprocessed, seconds1, mail.name),
        encoding="utf-8",
    )
    measurements = {
        "datum": datetime.now().isoformat(timespec="seconds"),
        "prompt_hash": hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest()[:12],
        "stufe1_ms": round(seconds1 * 1000, 1),
        "laeufe": [
            {
                "modell": r.model,
                "lauf": r.run,
                "stufe2_s": round(r.seconds_llm, 2),
                "ollama": {k: v for k, v in r.ollama.items() if k != "roh"},
                "modellantwort": r.ollama.get("roh"),
                "durchgelassen": r.checks["durchgelassen"],
                "verloren": r.checks["verloren"],
                "verworfen": r.rejected,
                "sha256": hashlib.sha256(r.text.encode()).hexdigest(),
            }
            for r in results
        ],
    }
    (out / "messungen.json").write_text(
        json.dumps(measurements, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Stufe 1: {seconds1 * 1000:.0f} ms. Ausgaben in {out}")
    return (
        0
        if all(
            not r.checks["durchgelassen"] and not r.checks["verloren"] for r in results
        )
        else 1
    )


if __name__ == "__main__":
    sys.exit(main())
