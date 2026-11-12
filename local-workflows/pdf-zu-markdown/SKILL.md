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
- was fehlt und installiert werden müsste, mit Größen. PyTorch, das Docling mitinstalliert, belegt unter Windows in der CPU-Variante rund 0,5 GB, die Modelle zu Layout und Tabellen laut README rund 505 MB, dazu kommen die OCR-Modelle. Unter Linux installiert pip vermutlich eine PyTorch-Variante mit CUDA-Bibliotheken von mehreren GB, gemessen ist das nicht,
- welche Grenzen der Abschnitt Grenzen in `README.md` nennt, mindestens dass die Standard-OCR deutsche Scans schlecht liest,
- dass der Mensch ein vertrauliches Dokument selbst in seinem Terminal umwandelt, wie es der Abschnitt Eigene Daten beschreibt.

Dann wartest du auf die Freigabe.

## Einrichten

1. Prüfe Betriebssystem, Python-Version, Prozessor, Arbeitsspeicher und freien Plattenplatz.
2. Lies die Installation in der Docling-Dokumentation (https://docling-project.github.io/docling/) nach und installiere `docling` und für die Prüfung `pypdf` mit pip, nur nach Freigabe.
3. Lade die Modelle vorab mit `docling-tools models download layout tableformer rapidocr -o modelle`. Danach läuft die Umwandlung mit den Umgebungsvariablen `DOCLING_ARTIFACTS_PATH=<Pfad zu modelle>` und `HF_HUB_OFFLINE=1` ohne Netz.
   - Findet die Shell `docling-tools` nicht, liegt der Skriptordner von pip nicht im `PATH`, etwa bei einer Installation mit `--user` unter Windows. Dann ruft `python -m docling.cli.tools models download layout tableformer rapidocr -o modelle` dasselbe Programm auf.
   - Kündige den Download der RapidOCR-Modelle vorher an. Sie kommen von modelscope.cn, im Test brach der erste Versuch ab und der zweite dauerte fast acht Minuten. Im normalen Lauf ohne `DOCLING_ARTIFACTS_PATH` nutzt Docling laut README die Modelle, die das Paket rapidocr mitbringt.
4. Sollen deutsche Scans gelesen werden, recherchiere eine OCR-Engine mit deutschem Sprachmodell und nenne die Optionen, bevor du eine einrichtest. Die README nennt Kandidaten, getestet ist keiner.

## Ausführen und prüfen

1. `python convert.py` wandelt alle PDFs in `input/` um und schreibt `output/<name>.md`. Die Konsole zeigt Zeiten, Seitenzahlen und Dateinamen, dazu INFO-Meldungen von Docling mit Dateinamen und lokalen Pfaden, aber keinen Text aus dem Dokument.
2. `python check_output.py` schreibt `output/check-report.txt`. Erkläre dem Menschen, was vollständig ankam und was verloren ging, etwa die verschobene Überschrift im Spaltensatz und den Wortrecall beim Scan. Das Testdokument ist fiktiv, du darfst Bericht und Markdown deshalb selbst lesen.
3. Eigene Dokumente wandelt `convert.py` um, wenn ihr Pfad als Argument übergeben wird. Für sie gibt es keine Referenz, ihre Prüfung ist das Lesen des Markdowns. Wer es liest und wer den Aufruf ausführt, regelt der folgende Abschnitt Eigene Daten.

## Eigene Daten

Ob ein eigenes Dokument vertraulich ist, entscheidet der Mensch. Ein Dokument, das ohnehin an dich gehen darf, wandelt ihr wie das Testdokument um, und du liest das Markdown. Bei einem vertraulichen Dokument führt der Mensch die Pipeline aus, und du arbeitest nur mit Befehlszeilen und Pfaden. Alles, was du liest oder in der Konsole siehst, geht als Kontext an den Anbieter des Cloud-Agenten.

- Der Mensch führt den Aufruf selbst in seinem eigenen Terminal aus. Du nennst ihm die Befehlszeile und wartest auf seine Rückmeldung. Sie lautet `python convert.py <Dokument> --out <Ordner>`.
- `--out` zeigt auf einen Ordner außerhalb dieses Repositorys, damit das Markdown weder in `output/` noch in `git status` erscheint.
- Du liest weder das Dokument noch das Markdown. Nenne dem Menschen den Pfad der Ausgabe, er öffnet die Datei selbst. Die Konsolenausgabe enthält keinen Text aus dem Dokument. Sie nennt aber Zeiten, Seitenzahl und den Namen des Dokuments, in den Zeilen mit `TIME` ebenso wie in den INFO-Meldungen von Docling, dazu lokale Pfade, etwa zu den OCR-Modellen. Ist schon der Dateiname vertraulich, benennt der Mensch die Datei vor dem Lauf um. Erst dann darf er dir die Konsolenausgabe weitergeben.
- Das Markdown eines vertraulichen Dokuments ist für den Menschen oder ein lokales LLM bestimmt. Was davon an dich geht, entscheidet er nach dem Lesen und übergibt es dir selbst.
