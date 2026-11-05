# Freigabevorlage für kundenanfrage.txt

Nur lokal verwenden. Diese Datei enthält die entfernten Originalstellen. An den Cloud-Agenten geht allein die bereinigte Mail und die bereinigte Tabelle.

- Erstellt: 2026-11-05T15:38:38
- Modell Stufe 2: qwen3.5:9b (Ollama, lokal, temperature 0), Prompt-Hash 195ba841c5b6
- Laufzeit: Stufe 1 16 ms, Stufe 2 1.8 s
- Automatische Prüfung: bestanden

## Prüfergebnis

- Durchgelassen: nichts
- Verloren: nichts

Bestanden heißt nur, dass keine der bekannten Stellen durchgerutscht ist. Was weder Prüfliste noch Muster kennen, findet allein der Mensch beim Lesen.

### Prüfliste dieser Mail

- 555-9482: entfernt durch Skript
- 3457: entfernt durch Skript
- 908 W. Capital Way: entfernt durch Skript
- Tacoma: entfernt durch Skript
- 98401: entfernt durch Skript
- andrew.fuller@: entfernt durch Skript
- steven.buchanan@: entfernt durch Skript
- office@dhcraft.org: entfernt durch Skript
- Steven Buchanan: entfernt durch Skript
- Margaret Peacock: entfernt durch LLM
- Michael Suyama: entfernt durch LLM
- Pension: entfernt durch LLM
- Elternzeit: entfernt durch LLM
- Geburtsdaten: entfernt durch LLM
- Privatadressen: entfernt durch LLM
- Northwind Traders: erhalten
- eintägigen Workshop: erhalten
- Produkte und Länder: erhalten
- Umsatz: erhalten
- 1996 bis 1998: erhalten
- zweite Januarhälfte 2027: erhalten
- Andrew Fuller: erhalten

### Allgemeine Prüfungen

- E-Mail-Muster: keine Treffer
- Telefon-Muster: keine Treffer
- Namen aus der Mitarbeiterliste: keine Treffer
- Entfernte Tabellenwerte in der bereinigten Kopie: keine Treffer

## Entfernte Stellen

- Stufe 1 Skript, Name (Kopfzeile): 'Steven Buchanan' ersetzt durch [NAME]
- Stufe 1 Skript, E-Mail: 'andrew.fuller@northwind-traders.example' ersetzt durch [E-MAIL]
- Stufe 1 Skript, E-Mail: 'office@dhcraft.org' ersetzt durch [E-MAIL]
- Stufe 1 Skript, E-Mail: 'steven.buchanan@northwind-traders.example' ersetzt durch [E-MAIL]
- Stufe 1 Skript, Telefon (Durchwahl): 'Durchwahl 3457' ersetzt durch [TELEFON]
- Stufe 1 Skript, Telefon: '(206) 555-9482' ersetzt durch [TELEFON]
- Stufe 1 Skript, Postadresse: '908 W. Capital Way' ersetzt durch [ADRESSE]
- Stufe 1 Skript, Postadresse: 'Tacoma, WA 98401, USA' ersetzt durch [ADRESSE]
- Stufe 2 LLM, Umstand: 'Die Geburtsdaten und Privatadressen stehen in der Liste, falls Sie Teilnahmebestätigungen ausstellen.' ersetzt durch [PERSÖNLICH]
- Stufe 2 LLM, Umstand: 'Michael Suyama ist bis Jahresende in Elternzeit, möchte aber online dazukommen.' ersetzt durch [PERSÖNLICH]
- Stufe 2 LLM, Umstand: 'Margaret Peacock geht im Frühjahr in Pension und wird nicht teilnehmen.' ersetzt durch [PERSÖNLICH]

## Anhänge

- mitarbeitende.xlsx, Blatt Employees (9 Zeilen): behalten EmployeeID, Title, HireDate, ReportsTo; entfernt LastName, FirstName, TitleOfCourtesy, BirthDate, Address, City, Region, PostalCode, Country, HomePhone, Extension, Notes
- bestellungen.xlsx: NICHT bearbeitet, vor der Weitergabe selbst prüfen oder weglassen
- produkte.xlsx: NICHT bearbeitet, vor der Weitergabe selbst prüfen oder weglassen
- kunden.xlsx: NICHT bearbeitet, vor der Weitergabe selbst prüfen oder weglassen

## Bereinigte Mail

```text
Von: Andrew Fuller <[E-MAIL]>
An: [E-MAIL]
Cc: [NAME] <[E-MAIL]>
Datum: Montag, 9. November 2026, 08:12
Betreff: Anfrage Workshop Agentic Engineering und Governance für unser Vertriebsteam
Anhänge: bestellungen.xlsx, produkte.xlsx, kunden.xlsx, mitarbeitende.xlsx

Sehr geehrte Damen und Herren,

ich leite den Vertrieb bei Northwind Traders, einem Großhandel für Feinkost und Getränke mit Standorten in Seattle und London. Ein Kollege hat Ihre Weiterbildung bei Uni for Life besucht und Sie mir empfohlen.

Wir möchten für unser Vertriebsteam einen Workshop zu Agentic Engineering und Governance. Unsere Leute arbeiten fast ausschließlich mit Excel-Listen, und mehrere haben inzwischen auf eigene Faust angefangen, Kundendaten in irgendwelche Chatbots zu kopieren. Ich hätte gerne zweierlei. Erstens sollen die Kolleginnen und Kollegen lernen, wie man mit AI Agents unsere Verkaufsdaten sinnvoll auswertet. Zweitens brauchen wir klare Regeln, was erlaubt ist und was nicht, bevor uns die Rechtsabteilung das Thema ganz verbietet.

Konkret wünschen wir uns:

- einen eintägigen Workshop für unser Team, vor Ort in London oder online
- Folien, die wir danach intern weitergeben dürfen, gerne in unserem Firmendesign
- eine kleine Webseite oder Übersicht für die Teilnehmenden, auf der die wichtigsten Begriffe und Regeln nachzulesen sind
- einen ersten Vorschlag für interne Regeln zum Einsatz von KI im Vertrieb

Damit Sie sehen, womit wir arbeiten, habe ich Ihnen unsere Exporte aus dem alten Warenwirtschaftssystem angehängt: Bestellungen, Produkte, Kunden und die Mitarbeiterliste des Vertriebs. Die Daten reichen von 1996 bis 1998, neuere Exporte schickt Ihnen meine Assistentin nach. Mich würde besonders interessieren, welche Produkte und Länder bei uns am meisten Umsatz bringen und ob Sie an den Daten zeigen können, was ein Agent damit anfangen kann.

Zum Team: Es sind neun Personen. [PERSÖNLICH] [PERSÖNLICH] [PERSÖNLICH]

Zeitlich wäre uns die zweite Januarhälfte 2027 am liebsten. Können Sie mir bis Ende nächster Woche ein Angebot mit einem groben Ablauf schicken? Für Rückfragen erreichen Sie mich am besten direkt unter [TELEFON], Durchwahl [TELEFON].

Mit freundlichen Grüßen

Andrew Fuller
Vice President, Sales
Northwind Traders
[ADRESSE]
[ADRESSE]
```

## Freigabe

- [ ] Bereinigte Mail vollständig gelesen
- [ ] Keine weiteren Angaben zu Personen gefunden
- [ ] Nicht bearbeitete Anhänge geprüft oder entfernt

Freigegeben durch: ______________________  Datum: ____________
