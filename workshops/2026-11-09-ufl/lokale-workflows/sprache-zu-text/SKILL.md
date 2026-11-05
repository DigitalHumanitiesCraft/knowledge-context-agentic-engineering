---
name: sprache-zu-text
description: Richtet auf dem eigenen Rechner eine Transkription mit faster-whisper und eine Zusammenfassung über Ollama ein und prüft sie an einer synthetischen Testaufnahme. Verwenden, wenn Besprechungen lokal transkribiert und zusammengefasst werden sollen.
---

# Sprache zu Text

Dieser Ordner ist zugleich Skill und Arbeitsordner. `transkribiere.py` transkribiert eine Aufnahme mit faster-whisper, `pruefe.py` misst an der Testaufnahme Wortfehler und die Schreibung von Namen gegen ein Referenzskript, und `zusammenfassen.py` lässt ein lokales Large Language Model (LLM) über Ollama Stichpunkte und offene Aufgaben schreiben. Ein Mensch prüft die Zusammenfassung am Transkript. Die Einzelheiten und Messwerte stehen in `README.md`.

## Zuerst informieren

Bevor du etwas installierst oder ausführst, erklärst du dem Menschen in wenigen Sätzen:

- was die Pipeline tut und dass die Aufnahme den Rechner nicht verlässt,
- welche Dateien dieser Ordner enthält: `besprechung.wav` (synthetisches Gespräch, eine Minute), `referenzskript.txt`, `erzeuge_audio.py` (nur zum Neuerzeugen der Aufnahme, braucht piper-tts), die drei Skripte und `transkripte/`,
- was fehlt und installiert werden müsste, mit Größen (das Modell large-v3-turbo hat rund 1,6 GB, für eine NVIDIA-Grafikkarte kommen laut README rund 2 GB CUDA-Bibliotheken dazu, `qwen3.5:9b` für die Zusammenfassung belegt rund 6,6 GB),
- welche Grenzen der Abschnitt Grenzen in `README.md` nennt, mindestens dass synthetische Stimmen sauberer sind als echte Aufnahmen und Whisper keine Sprecher trennt,
- dass der Mensch eine eigene Aufnahme selbst in seinem Terminal transkribiert, wie es der Abschnitt Eigene Daten beschreibt.

Dann wartest du auf die Freigabe.

## Einrichten

1. Prüfe Betriebssystem, Python-Version, Arbeitsspeicher, freien Plattenplatz und ob eine NVIDIA-Grafikkarte vorhanden ist.
2. Lies in der Dokumentation von faster-whisper (https://github.com/SYSTRAN/faster-whisper) nach, welche Pakete auf der CPU und auf der GPU unter diesem Betriebssystem nötig sind. Installiere `faster-whisper` und `jiwer` mit pip, nur nach Freigabe.
3. Für die Zusammenfassung brauchst du Ollama (https://ollama.com) mit `ollama pull qwen3.5:9b`.

## Ausführen und prüfen

1. Transkribiere mit der Einstellung der README, in einer Zeile:
   `python transkribiere.py besprechung.wav --models large-v3-turbo --devices cpu --vad --no-context --glossar "Northwind Traders, Chai, Côte de Blaye, Agentic Engineering, Excel"`.
   Mit `--devices cuda` läuft es auf der Grafikkarte.
2. `python pruefe.py` schreibt `pruefbericht.md` mit Wortfehlerrate und Namen je Lauf.
3. `python zusammenfassen.py transkripte/large-v3-turbo_cpu_glossar_vad_nocontext.txt` schreibt die Zusammenfassung und gibt nur ihren Pfad aus. Nenne dem Menschen die Pfade von Zusammenfassung und Transkript, er öffnet beide selbst und vergleicht sie. Im Test ergänzte das LLM eine Frist, die im Gespräch nicht vorkommt. Bei der synthetischen Testaufnahme darfst du beide Dateien mit ihm durchgehen.
4. Eine eigene Aufnahme transkribiert der Mensch selbst, wie es der folgende Abschnitt beschreibt.

## Eigene Daten

Bei einer eigenen Aufnahme führt der Mensch die Pipeline aus, und du arbeitest nur mit Befehlszeilen und Pfaden. Alles, was du liest oder in der Konsole siehst, geht als Kontext an den Anbieter des Cloud-Agenten, und eine Besprechung soll den Rechner gerade nicht verlassen.

- Der Mensch führt beide Aufrufe selbst in seinem eigenen Terminal aus. Du nennst ihm die Befehlszeilen und wartest auf seine Rückmeldung. Sie lauten `python transkribiere.py <Aufnahme> --models large-v3-turbo --devices cpu --vad --no-context --glossar "<Eigennamen>" --out <Ordner>` und `python zusammenfassen.py <Ordner>/transkripte/<Lauf>.txt --out <Ordner>`.
- `--out` zeigt auf einen Ordner außerhalb dieses Repositorys. Ohne den Schalter hängt der Lauf das vollständige Transkript an die versionierte `messwerte.json` an, und schon ein `git diff` brächte es dir.
- `--glossar` nimmt die Eigennamen auf, die in der Besprechung vorkommen. Ein Referenzskript gibt es nicht, die Prüfung ist das Lesen durch den Menschen.
- Du liest weder die Aufnahme noch das Transkript, `messwerte.json` oder die Zusammenfassung. Nenne dem Menschen die Pfade, er öffnet die Dateien selbst. Die Konsolenausgabe darf er dir weitergeben, sie nennt nur Laufbezeichnung, Zeiten und den Ausgabepfad.
- Was aus Transkript oder Zusammenfassung weitergeht, entscheidet der Mensch nach dem Lesen und übergibt es dir selbst.
