---
name: mail-anonymisieren
description: Richtet auf dem eigenen Rechner eine Pipeline ein, die eine Mail mit Excel-Anhang bereinigt, bevor ein Cloud-Agent sie sieht, und führt sie mit fiktiven Testdaten aus. Verwenden, wenn Mails oder Tabellen mit Personendaten lokal anonymisiert werden sollen.
---

# Mails anonymisieren

Dieser Ordner ist zugleich Skill und Arbeitsordner. Die Pipeline hat drei Stufen in einem Skript. Code ersetzt, was sich an seiner Form erkennen lässt, ein lokales Large Language Model (LLM) benennt im Freitext die Stellen über Personen, und derselbe Code prüft das Ergebnis erneut. Ein Mensch gibt frei, erst dann geht die bereinigte Mail weiter. Die Einzelheiten und Messwerte stehen in `README.md`.

## Zuerst informieren

Bevor du etwas installierst oder ausführst, erklärst du dem Menschen in wenigen Sätzen:

- was die Pipeline tut und dass keine Daten an einen Cloud-Dienst gehen,
- welche Dateien dieser Ordner enthält: `redact_mail.py` mit allen drei Stufen, `test_redact_mail.py`, `pruefliste.json` für die Testmail, `testmails/` mit drei Abwandlungen und `ausgabe/` für die Ergebnisse,
- dass die Testmail und `mitarbeitende.xlsx` unter `../../data/` liegen, die Pipeline also im geklonten Repository `DigitalHumanitiesCraft/knowledge-context-agentic-engineering` läuft,
- was fehlt und installiert werden müsste, mit Größe des Modells (`qwen3.5:9b` belegt rund 6,6 GB auf der Platte und lädt beim Lauf in Grafik- oder Arbeitsspeicher),
- welche Grenzen der Abschnitt Grenzen in `README.md` nennt, mindestens dass bei einer echten Mail nur die allgemeinen Prüfungen laufen,
- dass der Mensch eine eigene Mail selbst in seinem Terminal bereinigt, wie es der Abschnitt Eigene Daten beschreibt.

Dann wartest du auf die Freigabe.

## Einrichten

1. Prüfe Betriebssystem, Python-Version (ab 3.11), Arbeitsspeicher, Grafikkarte und freien Plattenplatz.
2. Lies in der offiziellen Dokumentation von Ollama (https://ollama.com) nach, wie es auf diesem Betriebssystem installiert wird. Installiere nur nach Freigabe.
3. Lade das Modell mit `ollama pull qwen3.5:9b`. Reicht der Speicher nicht, nenne die Messungen der README. `ministral-3:8b` ist mit rund 6,0 GB kaum kleiner und ließ in einer der vier Testmails einen Satz durch, `qwen3.5:4b` (rund 3,4 GB) in drei der vier.
4. Installiere `openpyxl` mit pip.

## Ausführen und prüfen

1. `python test_redact_mail.py` prüft die Muster und die Konsolenausgabe ohne LLM.
2. `python redact_mail.py` bereinigt die Testmail. Exitcode 0 heißt, dass keine Stelle der Prüfliste durchgerutscht ist, die allgemeinen Prüfungen nichts gefunden haben und kein Inhalt verloren ging, der erhalten bleiben muss. Exitcode 1 meldet einen dieser Befunde oder einen Abbruch, etwa weil Ollama nicht läuft. Die Konsole nennt je Lauf Modell, Laufzeiten, die Anzahl durchgelassener und verlorener Stellen und eine Prüfsumme der bereinigten Mail, am Ende den Ausgabeordner, aber keine Stelle selbst.
3. Nenne dem Menschen den Pfad `ausgabe/freigabe.md`, er öffnet die Datei selbst. Sie enthält die entfernten Originalstellen und bleibt deshalb lokal. Bei der fiktiven Testmail darfst du sie mit ihm durchgehen.
4. Eine eigene Mail bereinigt der Mensch selbst, wie es der folgende Abschnitt beschreibt.

## Eigene Daten

Bei einer eigenen Mail führt der Mensch die Pipeline aus, und du arbeitest nur mit Befehlszeilen und Pfaden. Alles, was du liest oder in der Konsole siehst, geht als Kontext an den Anbieter des Cloud-Agenten, und genau das soll die Pipeline verhindern.

- Der Mensch führt den Aufruf selbst in seinem eigenen Terminal aus. Du nennst ihm die Befehlszeile und wartest auf seine Rückmeldung. Sie lautet `python redact_mail.py --mail <Mail> --xlsx <Anhang> --checklist <Prüfliste> --out <Ordner>`.
- `--out` zeigt auf einen Ordner außerhalb dieses Repositorys. Ohne den Schalter überschreibt der Lauf die versionierten Ergebnisse der Testmail in `ausgabe/`, und schon ein `git diff` brächte dir die Originalstellen.
- `--xlsx` und `--checklist` sind optional. Ohne `--xlsx` bearbeitet das Skript keine Tabelle und nennt angehängte Dateien in der Freigabevorlage als nicht bearbeitet. Eine eigene Prüfliste empfiehlst du trotzdem. Der Mensch legt sie nach dem Muster von `pruefliste.json` mit den Namen und Angaben an, die er in der Mail kennt. Ohne sie laufen nur die allgemeinen Prüfungen.
- Du liest weder die Mail und ihren Anhang noch `freigabe.md` oder `messungen.json`. Beide Dateien enthalten die entfernten Originalstellen und die Antwort des lokalen LLM.
- Nenne dem Menschen den Pfad der Freigabevorlage, er öffnet die Datei selbst. Die Konsolenausgabe und den Exitcode darf er dir weitergeben. Sie nennen Modell, Laufzeiten, Anzahlen, eine Prüfsumme und den Ausgabeordner, aber keinen Inhalt der Mail.
- Die bereinigte Mail und die bereinigte Tabelle liest du erst, wenn der Mensch sie freigegeben hat und dir übergibt.
