# PDF zu Markdown mit Docling

Ein Agent liest Markdown zuverlässiger als PDF oder docx, weil Überschriften, Listen und Tabellen im Markdown als Struktur im Text stehen. Docling wandelt Dokumente lokal in Markdown um, die Dokumente verlassen dabei den Rechner nicht. Dieser Ordner enthält ein fiktives Testdokument mit typischen Schwierigkeiten, die Umwandlung und eine deterministische Prüfung der Ausgabe gegen den bekannten Inhalt.

## Aufruf

```
python convert.py input/northwind-ki-regeln.pdf
```

Ohne Argument wandelt `convert.py` alle PDFs in `input/` um und schreibt `output/<name>.md`, mit `--out <Ordner>` in einen anderen Ordner. `python check_output.py` vergleicht danach Docling mit naiver Textextraktion und schreibt `output/check-report.txt`. `python make_test_pdf.py` erzeugt das Testmaterial neu und braucht dafür Microsoft Word unter Windows. Alle drei Fassungen des Testdokuments sind versioniert, ein frischer Klon braucht den Generator deshalb nicht.

## Dateien

- `make_test_pdf.py` erzeugt die Richtlinie „Interne Regeln zum Einsatz von KI im Vertrieb“ der fiktiven Firma Northwind Traders als docx (python-docx), ergänzt in Word die Fußnote, exportiert über Word das PDF und rastert Seite 1 zu einem Bild-PDF ohne Textschicht (PyMuPDF, 150 dpi, Graustufen). Der Inhalt steht als Konstanten im Skript und dient der Prüfung als Referenz.
- `input/` enthält `northwind-ki-regeln.docx`, `northwind-ki-regeln.pdf` (zwei Seiten mit Kopfzeile, Fußzeile „Seite N von M“, nummerierter Liste, Tabelle, Fußnote und zweispaltigem Abschnitt) und `northwind-ki-regeln-scan.pdf`.
- `convert.py` ruft Docling mit Standardeinstellungen auf und misst Importzeit, Pipeline-Aufbau und Umwandlung getrennt.
- `check_output.py` prüft per Stringvergleich Überschriften, Listenpunkte, Tabellenzellen und -zeilen, Fußnote, Absatzzusammenhang, Kopf- und Fußzeilen, Lesereihenfolge im zweispaltigen Teil und bei der Bildseite den Wortrecall.
- `output/` enthält die Markdown-Dateien, `naive/` die Ausgaben von pypdf und pdftotext, `check-report.txt` den Prüfbericht.

## Gemessene Ergebnisse vom 5. November 2026

Umgebung: Docling 2.60.0 (docling-core 2.50.0, docling-ibm-models 3.10.2), Python 3.11, torch 2.11.0 nur CPU, OCR-Engine RapidOCR 3.4.2 mit onnxruntime, Desktop-Rechner mit AMD Ryzen 7 7800X3D und 31 GB RAM. Parallel lief auf derselben Maschine ein LLM über Ollama auf der GPU.

Laufzeiten in Sekunden, gemessen von `convert.py`:

| Lauf | Import | Pipeline-Aufbau | Bild-PDF, 1 Seite | Text-PDF, 2 Seiten | Prozess gesamt |
|---|---|---|---|---|---|
| erster Lauf, Modelle im Cache | 8,4 | 4,5 | 7,5 | 2,3 | 23,8 |
| zweiter Lauf | 7,6 | 2,9 | 5,6 | 2,1 | 19,3 |
| offline aus vorab geladenem Modellordner | 8,1 | 1,9 | 7,7 | 2,5 | 21,3 |
| docx direkt | 8,7 | 2,6 | – | 0,2 (docx) | – |

Das Bild-PDF wird zuerst verarbeitet und trägt deshalb auch Aufwärmzeit. Der Modell-Download von Hugging Face (`docling-tools models download layout tableformer`) umfasst `ds4sd/docling-layout-heron` mit 163,8 MB und `ds4sd/docling-models` mit 341,6 MB (Tableformer accurate und fast), zusammen 505,4 MB, und dauerte auf dieser Leitung 9,9 Sekunden. Die OCR-Modelle von RapidOCR (55,5 MB, onnx- und torch-Varianten) lädt `docling-tools models download rapidocr` von modelscope.cn. Der erste Versuch brach mit einem Verbindungsabbruch ab, der zweite brauchte 468 Sekunden. Im normalen Lauf nutzt Docling die Modelle, die bereits im Paketordner von rapidocr liegen.

Für den Workshop empfiehlt sich, die Modelle vorab in einen Ordner zu laden und offline zu arbeiten:

```
docling-tools models download layout tableformer rapidocr -o modelle
```

Danach läuft `convert.py` mit den Umgebungsvariablen `DOCLING_ARTIFACTS_PATH=<Pfad zu modelle>` und `HF_HUB_OFFLINE=1` ohne Netzverbindung. Das ist die Zeile „offline“ in der Tabelle. Liegt der Skriptordner von pip nicht im `PATH`, etwa nach `pip install --user` unter Windows, startet `python -m docling.cli.tools` dasselbe Programm wie `docling-tools`.

Prüfbericht für das Text-PDF:

- Docling erkennt alle Überschriften als Markdown-Überschriften, alle Listenpunkte als nummerierte Liste und alle Tabellenzeilen zellgenau als Markdown-Tabelle. Kopf- und Fußzeilen fehlen im Markdown, die Fußnote steht als eigener Absatz am Ende von Seite 1.
- Im zweispaltigen Teil stehen die sechs Absätze in richtiger Reihenfolge, Abschnitt 5 aber zwischen der linken und der rechten Spalte. Die Absätze der rechten Spalte erscheinen damit unter der falschen Überschrift.
- Der Trennstrich in „KI-Werkzeuge“ geht verloren, und das Fußnotenzeichen klebt als Zahl am Wort („generative KIWerkzeuge 1 einsetzen“). Fett gesetzte Leitwörter und die Hierarchie zwischen Titel und Abschnittsüberschriften gehen verloren, alle Überschriften stehen auf Ebene `##`.
- pypdf liefert allen Text, auch die Spalten in richtiger Reihenfolge, wiederholt aber Kopfzeile und Seitenzahl auf jeder Seite im Fließtext und kennt keine Struktur. Tabellenzellen über zwei Zeilen zerfallen in Einzelzeilen.
- pdftotext liest im zweispaltigen Teil absatzweise im Wechsel zwischen den Spalten, mit `-layout` zeilenweise über beide Spalten hinweg, und zerreißt mehrzeilige Tabellenzellen.

Prüfbericht für das Bild-PDF:

- pypdf und pdftotext liefern null Zeichen.
- Docling liest die Seite per OCR, erkennt Überschriften, Liste und eine Tabelle mit allen fünf Zeilen. Der Wortrecall gegenüber dem Original liegt bei 69 Prozent. Umlaute fehlen meist („gultig“, „durfen“, „AuBendienst“), Leerzeichen fallen weg („JedesKl-ErgebniswirdvorderWeitergabe“), „KI“ wird zu „Kl“, und ein Satzteil im zweiten Absatz fehlt vollständig. Die Standardmodelle von RapidOCR sind auf Chinesisch und Englisch trainiert.

Die docx-Datei wandelt Docling ohne Layoutanalyse in 0,2 Sekunden um. Reihenfolge, Fettdruck und Tabelle stimmen, die Nummerierung der Liste und die Fußnote fehlen. Die Liste ist im Testdokument über eine Formatvorlage nummeriert, in Word von Hand angelegte Listen können sich anders verhalten.

## Grenzen

- Das Testdokument ist sauber gesetzt und kurz. Echte Scans mit Schräglage, Flecken oder Handschrift sind schwieriger als die gerasterte Seite.
- Gemessen wurde auf einem schnellen Desktop-Prozessor. Ein Laptop ohne GPU braucht vermutlich ein Mehrfaches der Zeiten, gemessen ist das nicht.
- Für deutsche Scans ist die Standard-OCR ungeeignet. Bessere Ergebnisse versprechen ein lateinisches RapidOCR-Erkennungsmodell, EasyOCR oder Tesseract mit deutschem Sprachpaket, getestet wurde keine dieser Varianten.
- Die Prüfung vergleicht Strings mit dem bekannten Inhalt. Sie erkennt fehlende und zerrissene Textteile, bewertet aber keine inhaltliche Lesbarkeit.
