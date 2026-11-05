"""Score every run in messwerte.json against referenzskript.txt and write pruefbericht.md.

Usage: python pruefe.py
WER uses jiwer on lowercased text with punctuation removed; the targeted checks
look for the number, the product names and the technical term.
"""

import json
import re
import unicodedata
from pathlib import Path

import jiwer

HERE = Path(__file__).resolve().parent

# Accepted spellings per checked item. Digits and words both count for the number,
# because Whisper's choice between them is a formatting decision, not a recognition error.
CHECKS = {
    "Zahl 28": ["28", "achtundzwanzig"],
    "Produkt Chai": ["chai"],
    "Produkt Côte de Blaye": ["côte de blaye", "cote de blaye"],
    "Fachbegriff Agentic Engineering": ["agentic engineering"],
}


def reference_text() -> str:
    lines = (HERE / "referenzskript.txt").read_text(encoding="utf-8").splitlines()
    return " ".join(line.split(":", 1)[1].strip() for line in lines if line.strip())


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFC", text).lower()
    text = text.replace("-", " ")
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def word_diff(ref: str, hyp: str) -> list[str]:
    out = jiwer.process_words(ref, hyp)
    r, h = ref.split(), hyp.split()
    diffs = []
    for chunk in out.alignments[0]:
        if chunk.type == "equal":
            continue
        a = " ".join(r[chunk.ref_start_idx : chunk.ref_end_idx]) or "(leer)"
        b = " ".join(h[chunk.hyp_start_idx : chunk.hyp_end_idx]) or "(leer)"
        diffs.append(f"{a} -> {b}")
    return diffs


def main() -> None:
    ref = normalise(reference_text())
    records = json.loads((HERE / "messwerte.json").read_text(encoding="utf-8"))
    rows, details = [], []
    for rec in records:
        hyp = normalise(rec["text"])
        wer = jiwer.wer(ref, hyp)
        hits = {
            name: any(re.search(rf"\b{re.escape(v)}\b", hyp) for v in variants)
            for name, variants in CHECKS.items()
        }
        rec["wer"] = round(wer, 4)
        rec["checks"] = hits
        marks = " | ".join("ja" if ok else "nein" for ok in hits.values())
        runs = ", ".join(
            str(t) for t in rec.get("transcribe_runs_s", [rec["transcribe_s"]])
        )
        rows.append(
            f"| {rec['tag']} | {rec['transcribe_s']} ({runs}) | {rec['rtf']} | {rec['load_s']} | "
            f"{wer:.1%} | {marks} |"
        )
        details.append(f"### {rec['tag']}\n")
        details += [f"- {d}" for d in word_diff(ref, hyp)] or ["- keine Abweichung"]
        details.append("")

    header = " | ".join(CHECKS)
    report = [
        "# Prüfbericht Sprache zu Text",
        "",
        "Erzeugt von `pruefe.py` aus `messwerte.json` und `referenzskript.txt`.",
        "Wortfehlerrate (WER) nach Kleinschreibung, Entfernen der Satzzeichen und Bindestrich als Leerzeichen.",
        f"Audiolänge {records[0]['audio_s']} s. Zeiten in Sekunden, Echtzeitfaktor = Transkriptionszeit / Audiolänge.",
        "",
        "Transkription: schnellster Durchgang, in Klammern alle Durchgänge. Laden ohne Download.",
        "",
        f"| Lauf | Transkription s | Echtzeitfaktor | Laden s | WER | {header} |",
        "|---|---|---|---|---|" + "---|" * len(CHECKS),
        *rows,
        "",
        "## Abweichungen je Lauf (Referenz -> Transkript)",
        "",
        *details,
    ]
    (HERE / "pruefbericht.md").write_text("\n".join(report), encoding="utf-8")
    (HERE / "messwerte.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("\n".join(rows))


if __name__ == "__main__":
    main()
