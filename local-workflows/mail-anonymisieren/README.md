# Mail anonymisieren

Eine eingehende Kundenmail mit Excel-Anhang wird auf dem eigenen Rechner bereinigt, bevor ein Cloud-Agent sie zu sehen bekommt. Ein Skript entfernt, was sich an seiner Form erkennen lässt, ein lokales Large Language Model (LLM) findet im Freitext die Stellen über Personen, und eine zweite, wieder deterministische Prüfung legt das Ergebnis einem Menschen zur Freigabe vor. Grundlage ist die synthetische Testmail `../../data/kundenanfrage.txt` mit dem Anhang `../../data/mitarbeitende.xlsx` (Northwind-Daten, fiktiv).

## Aufruf

```
python redact_mail.py
```

Voraussetzungen sind Python ab 3.11 mit `openpyxl` und ein lokal laufendes Ollama mit dem Modell `qwen3.5:9b`. Es wird kein Cloud-Dienst aufgerufen. Ein Modellvergleich mit Wiederholungen läuft mit `python redact_mail.py --model qwen3.5:9b --model ministral-3:8b --runs 3`, eine andere Mail mit `--mail` und `--out`, optional mit `--xlsx` für den Anhang und `--checklist` für eine eigene Prüfliste. Tabelle und Prüfliste der Testmail gelten nur, wenn `--mail` fehlt. Die Abwandlungen unter `testmails/` bekommen die Tabelle ebenfalls ohne Schalter und ihre Prüfliste mit `--checklist`, etwa `python redact_mail.py --mail testmails/kundenanfrage_variante.txt --checklist testmails/pruefliste_variante.json --out <Ordner>`. Der Exit-Code ist 0, wenn keine bekannte Stelle durchgerutscht ist, die allgemeinen Prüfungen nichts gefunden haben und kein zu erhaltender Inhalt verloren ging, sonst 1. Die Konsole nennt je Lauf Modell, Laufzeiten, die Anzahl durchgelassener und verlorener Stellen und eine Prüfsumme der bereinigten Mail, am Ende den Ausgabeordner. Die Stellen selbst stehen in der Freigabevorlage.

## Stufen

1. Skript. Es ersetzt Anzeigenamen aus den Kopfzeilen An und Cc samt ihren weiteren Vorkommen, E-Mail-Adressen, Telefonnummern mit Durchwahl und Postadressen in US- und deutsch-österreichischer Schreibweise durch Platzhalter. Aus der Tabelle übernimmt es nur die Spalten einer Positivliste (`EmployeeID`, `Title`, `HireDate`, `ReportsTo`), jede andere Spalte fällt weg, auch eine, die ein späterer Export neu hinzufügt. Die Spaltennamen liest es aus der Datei und schreibt eine neue Arbeitsmappe ohne Formatierung, Kommentare und Dokumenteigenschaften der Quelle.
2. Lokales LLM. Das LLM schreibt die Mail nicht um. Es liefert als JSON die Namen Dritter und die vollständigen Sätze über persönliche Umstände oder private Daten, und das Skript ersetzt genau diese Stellen. Eine Stelle, die so nicht in der Mail steht, wird verworfen und in der Freigabevorlage aufgeführt. Abweichende Leerzeichen und Großschreibung toleriert der Abgleich, weil das Modell falsch geschriebene Namen sonst korrigiert und die Stelle dadurch durchrutscht.
3. Prüfung. Sie meldet für jede Zeichenkette der Prüfliste, ob das Skript, das LLM oder keine Stufe sie entfernt hat, und für jeden Inhalt, der bleiben muss, ob er erhalten ist. Unabhängig von der Prüfliste sucht sie erneut nach E-Mail- und Telefonmustern und, sobald eine Tabelle bearbeitet wird (bei der Testmail und ihren Varianten immer, bei einer eigenen Mail mit `--xlsx`), nach Vor- und Nachnamen aus der Mitarbeiterliste und nach entfernten Tabellenwerten in der bereinigten Kopie. Nicht bearbeitete Anhänge der Mail werden ausdrücklich genannt.

## Ausgaben

Im Ordner `ausgabe/` liegen die bereinigte Mail `kundenanfrage_bereinigt.txt`, die bereinigte Tabelle `mitarbeitende_bereinigt.xlsx`, die Freigabevorlage `freigabe.md` und `messungen.json` mit Laufzeiten, Modellantworten und Prüfsummen jedes Laufs. Die Freigabevorlage enthält die entfernten Originalstellen, damit der Mensch sie beurteilen kann, und bleibt deshalb lokal. Weiter geht allein die bereinigte Mail mit der bereinigten Tabelle.

Im Ordner `testmails/` liegen drei Abwandlungen der Testmail mit eigener Prüfliste. `variante` nennt Ruhestand, Krankschreibung, Kinder, Vornamen und eine österreichische Privatadresse, `schwer` Unfall, Therapie, Gehalt, eine Assistentin ohne Listeneintrag und ein Geburtsdatum im Text, `luecken` mittelbar identifizierende Angaben, einen falsch geschriebenen Namen und eine Adresse in ungewohnter Reihenfolge.

## Messung vom 5. November 2026

Gemessen auf einer RTX 4080 mit Ollama 0.17.1, `temperature` 0, `think` aus, Prompt-Hash `195ba841c5b6`. Die Laufzeit ist die Wanduhrzeit der Stufe 2, gemessen im Skript. Der erste Lauf eines Modells enthält das Laden in den Grafikspeicher, das Ollama mit 3,0 bis 5,6 Sekunden angab. Stufe 1 brauchte 10 bis 110 Millisekunden. Ein vollständiger Aufruf von `python redact_mail.py` dauerte mit Laden des Modells 6,7 Sekunden, bei bereits geladenem Modell 1,6 bis 2,6 Sekunden.

| Testmail | Modell | Lauf 1 | weitere Läufe | durchgelassen | verloren |
| --- | --- | --- | --- | --- | --- |
| kundenanfrage | qwen3.5:9b | 6,4 s | 1,3 s, 1,2 s | nichts | nichts |
| kundenanfrage | ministral-3:8b | 5,4 s | 1,2 s, 1,2 s | nichts | nichts |
| kundenanfrage | qwen3.5:4b | 4,0 s | 0,8 s, 0,8 s | Hinweis auf Geburtsdaten und Privatadressen | nichts |
| variante | qwen3.5:9b | 6,8 s | 2,5 s | nichts | nichts |
| variante | ministral-3:8b | 6,4 s | 2,0 s | nichts | nichts |
| variante | qwen3.5:4b | 3,9 s | 0,9 s | Hinweis auf Geburtstage | nichts |
| schwer | qwen3.5:9b | 7,0 s | 1,7 s | nichts | nichts |
| schwer | ministral-3:8b | 5,8 s | 2,0 s | nichts | nichts |
| schwer | qwen3.5:4b | 6,4 s | 1,7 s | nichts | nichts |
| luecken | qwen3.5:9b | 7,2 s | 1,5 s | nichts | nichts |
| luecken | ministral-3:8b | 5,0 s | 1,2 s | Satz über die einzige Frau im Londoner Team | nichts |
| luecken | qwen3.5:4b | 3,9 s | 0,5 s | dieser Satz, Herkunft und Ernährung, die Adresse | nichts |

Jeder Lauf lieferte innerhalb eines Modells eine byte-gleiche bereinigte Mail. Bei der Testmail kamen qwen3.5:9b und ministral-3:8b zum selben Ergebnis. In der Testmail entfernte das Skript Telefonnummer, Durchwahl, alle E-Mail-Adressen, die Postadresse und den Cc-Namen, das LLM die beiden Namen im Text, Pension, Elternzeit und den Satz zu Geburtsdaten und Privatadressen.

Zum Vergleich lief der Prompt des Vortests, der das LLM die ganze Mail umschreiben lässt, auf derselben Ausgabe der Stufe 1. Beide Modelle entfernten in je zwei Läufen die Namen, ließen aber Pension, Elternzeit und den Geburtsdaten-Satz stehen und brauchten 7,6 bis 13,9 Sekunden. Daraus lässt sich ableiten, dass der Gewinn gegenüber dem Vortest aus dem Wechsel vom Umschreiben zum Benennen ganzer Sätze kommt.

## Grenzen

- Die Prüfliste gilt nur für die Testmail. Bei einer echten Mail laufen allein die allgemeinen Prüfungen, und was weder Muster noch Mitarbeiterliste kennen, findet nur der Mensch beim Lesen. Bestanden heißt, dass keine bekannte Stelle durchgerutscht ist.
- Sätze über persönliche Umstände fallen ganz weg, mit ihnen auch Sachangaben. In der Testmail geht verloren, dass eine Person online teilnehmen möchte.
- Absendername, Funktion und Firma bleiben absichtlich stehen, der Absender ist damit erkennbar.
- Die Tabelle ist pseudonymisiert. Über `Title`, `HireDate` und `ReportsTo` lassen sich Einzelne wiedererkennen, etwa der Vice President oder die einzige Person mit dem Titel Inside Sales Coordinator.
- Bearbeitet wird nur `mitarbeitende.xlsx`. `kunden.xlsx` enthält Namen, Telefon- und Faxnummern von Ansprechpersonen, `bestellungen.xlsx` Lieferadressen. Die Freigabevorlage nennt diese Anhänge als nicht bearbeitet.
- Die Muster für Adressen erkennen Straßen nur an einer Endung wie Way, Blvd., straße oder gasse mit Hausnummer. „Moss Bay Blvd. 722“ und „Am Graben 5“ entgehen ihnen, britische Postleitzahlen im Fließtext ebenso. Umgekehrt ersetzen sie „Arbeitsplatz 2“ als Adresse. Telefonnummern mit Punkten als Trenner werden nicht erkannt, damit Datumsangaben unberührt bleiben.
- Der Prompt ist deutsch und auf Personen in einem Team zugeschnitten. Mittelbare Angaben ohne Schlüsselwort ließ ministral-3:8b stehen. Die Stabilität bei `temperature` 0 gilt für diese Maschine und diese Ollama-Version.
