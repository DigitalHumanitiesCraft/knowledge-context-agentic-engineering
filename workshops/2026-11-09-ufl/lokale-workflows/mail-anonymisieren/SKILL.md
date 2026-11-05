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
- was fehlt und installiert werden müsste,
- welche Grenzen der Abschnitt Grenzen in `README.md` nennt, mindestens dass bei einer echten Mail nur die allgemeinen Prüfungen laufen.

Dann wartest du auf die Freigabe.

## Einrichten

1. Prüfe Betriebssystem, Python-Version (ab 3.11), Arbeitsspeicher, Grafikkarte und freien Plattenplatz.
2. Lies in der offiziellen Dokumentation von Ollama (https://ollama.com) nach, wie es auf diesem Betriebssystem installiert wird. Installiere nur nach Freigabe.
3. Lade das Modell mit `ollama pull qwen3.5:9b`. Reicht der Speicher nicht, nenne die Messungen der README zu `ministral-3:8b` und `qwen3.5:4b`, das kleinere Modell ließ in zwei Testmails Sätze durch.
4. Installiere `openpyxl` mit pip.

## Ausführen und prüfen

1. `python test_redact_mail.py` prüft die Muster ohne LLM.
2. `python redact_mail.py` bereinigt die Testmail. Exitcode 0 heißt, dass keine Stelle der Prüfliste durchgerutscht ist.
3. Zeig dem Menschen `ausgabe/freigabe.md`. Sie enthält die entfernten Originalstellen und bleibt deshalb lokal.
4. Eine eigene Mail läuft mit `--mail`, `--xlsx`, `--checklist` und `--out`. Ohne eigene Prüfliste findet, was weder Muster noch Mitarbeiterliste kennen, nur der Mensch beim Lesen.
