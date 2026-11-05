---
name: pdf-zu-markdown
description: Richtet Docling auf dem eigenen Rechner ein, wandelt PDF, DOCX und Scans offline in Markdown um und prüft das Ergebnis gegen ein bekanntes Testdokument. Verwenden, wenn Dokumente für einen Agenten als Markdown aufbereitet werden sollen, ohne den Rechner zu verlassen.
---

# PDF zu Markdown

Dieser Ordner ist zugleich Skill und Arbeitsordner. `convert.py` übergibt Dokumente an Docling, das Layout, Lesereihenfolge, Tabellen und bei Scans den Text erkennt und Markdown schreibt. `check_output.py` vergleicht das Ergebnis mit dem bekannten Inhalt des Testdokuments und mit einfacher Textextraktion. Die Einzelheiten und Messwerte stehen in `README.md`.

## Zuerst informieren

Bevor du etwas installierst oder ausführst, erklärst du dem Menschen in wenigen Sätzen:

- was die Pipeline tut und dass die Dokumente den Rechner nicht verlassen,
- welche Dateien dieser Ordner enthält: `convert.py`, `check_output.py`, `make_test_pdf.py` (erzeugt das Testmaterial neu und braucht Word unter Windows), `input/` mit dem fiktiven Testdokument als docx, PDF und Scan, `output/` für die Ergebnisse,
- was fehlt und installiert werden müsste, mit Größe der Modelle (die README nennt rund 505 MB für Layout und Tabellen, dazu die OCR-Modelle),
- welche Grenzen der Abschnitt Grenzen in `README.md` nennt, mindestens dass die Standard-OCR deutsche Scans schlecht liest.

Dann wartest du auf die Freigabe.

## Einrichten

1. Prüfe Betriebssystem, Python-Version, Prozessor, Arbeitsspeicher und freien Plattenplatz.
2. Lies die Installation in der Docling-Dokumentation (https://docling-project.github.io/docling/) nach und installiere `docling` und für die Prüfung `pypdf` mit pip, nur nach Freigabe.
3. Lade die Modelle vorab mit `docling-tools models download layout tableformer rapidocr -o modelle`. Danach läuft die Umwandlung mit den Umgebungsvariablen `DOCLING_ARTIFACTS_PATH=<Pfad zu modelle>` und `HF_HUB_OFFLINE=1` ohne Netz.
4. Sollen deutsche Scans gelesen werden, recherchiere eine OCR-Engine mit deutschem Sprachmodell und nenne die Optionen, bevor du eine einrichtest. Die README nennt Kandidaten, getestet ist keiner.

## Ausführen und prüfen

1. `python convert.py` wandelt alle PDFs in `input/` um und schreibt `output/<name>.md`.
2. `python check_output.py` schreibt `output/check-report.txt`. Erkläre dem Menschen, was vollständig ankam und was verloren ging, etwa die verschobene Überschrift im Spaltensatz und den Wortrecall beim Scan.
3. Eigene Dokumente übergibst du als Pfad an `convert.py`. Für sie gibt es keine Referenz, ihre Prüfung ist das Lesen des Markdowns.
