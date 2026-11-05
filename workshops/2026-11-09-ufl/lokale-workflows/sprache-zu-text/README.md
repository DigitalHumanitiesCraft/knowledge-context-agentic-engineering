# Sprache zu Text lokal

Dieser Ordner zeigt für den Workshop Uni for Life (9. und 10.11.2026), wie sich eine Besprechung mit einem offenen Modell auf dem eigenen Rechner transkribieren lässt. Die Aufnahme verlässt den Rechner nicht. Anschließend fasst ein lokales LLM (Large Language Model) über Ollama das Transkript in Stichpunkte und offene Aufgaben zusammen.

## Aufruf

Transkription mit der für die Demo empfohlenen Einstellung, in einer Zeile:

```
python transkribiere.py besprechung.wav --models large-v3-turbo --devices cpu --vad --no-context --glossar "Northwind Traders, Chai, Côte de Blaye, Agentic Engineering, Excel"
```

Danach `python pruefe.py` für den Prüfbericht und `python zusammenfassen.py transkripte/large-v3-turbo_cpu_glossar_vad_nocontext.txt` für die Zusammenfassung. Mit `--devices cuda` läuft die Transkription auf einer NVIDIA-GPU.

## Dateien

- `referenzskript.txt` enthält das fiktive Gespräch zweier Personen aus dem Vertriebsteam von Northwind Traders, Sprecherin A und Sprecher B. Es ist die Referenz für die Prüfung.
- `erzeuge_audio.py` synthetisiert das Skript mit piper-tts zu `besprechung.wav` (61,9 s, 16 kHz mono, rund 2 MB).
- `transkribiere.py` transkribiert mit faster-whisper, misst Laden und Transkription getrennt vom Download, schreibt `transkripte/<lauf>.txt` mit Zeitmarken und hängt jeden Lauf samt Transkripttext an `messwerte.json` an. Mit `--out <Ordner>` landen beide in einem anderen Ordner.
- `pruefe.py` berechnet die Wortfehlerrate (WER, Anteil falscher, fehlender und zusätzlicher Wörter) mit jiwer, prüft Zahl, Produktnamen und Fachbegriff und schreibt `pruefbericht.md` mit allen Abweichungen je Lauf.
- `zusammenfassen.py` schickt ein Transkript an das lokale Ollama (`http://127.0.0.1:11434/api/chat`), schreibt `zusammenfassung_<lauf>.md` mit Modell und Laufzeit im Kopf und gibt nur deren Pfad aus. `--out <Ordner>` legt sie in einen anderen Ordner.

## Installation und Modelle

Stand 5.11.2026, Python 3.11 aus dem Microsoft Store, alle Pakete per pip in den User-Site.

- `piper-tts` 1.8.0 und `faster-whisper` 1.2.1, letzteres mit `ctranslate2` 4.8.5 und `av` 18.1.0. `jiwer` 4.0.0 war bereits installiert.
- Für die GPU zusätzlich `nvidia-cublas-cu12` 12.9.2.10, `nvidia-cudnn-cu12` 9.28.0.42 und `nvidia-cuda-nvrtc-cu12` 12.9.86, zusammen rund 2 GB. CTranslate2 bringt unter Windows kein cuBLAS mit und meldete ohne diese Pakete `cublas64_12.dll is not found`. `transkribiere.py` legt die DLL-Ordner der Pakete vor dem Laden in den Suchpfad und sucht sie im User-Site wie in den site-packages einer virtuellen Umgebung. Ein CUDA-Toolkit ist nicht nötig.
- Whisper-Modelle liegen im Hugging-Face-Cache `%USERPROFILE%\.cache\huggingface\hub`: `Systran/faster-whisper-small` (486 MB, Download 42 s), `Systran/faster-whisper-medium` (1,5 GB, 125 s), `mobiuslabsgmbh/faster-whisper-large-v3-turbo` (1,6 GB, 131 s). Für `large-v3-turbo` verweist faster-whisper auf das Repository von mobiuslabsgmbh, Systran bietet diese Größe nicht an. Ein Funktionstest hat zusätzlich `Systran/faster-whisper-tiny` (75 MB) geladen.
- Piper-Stimmen aus `rhasspy/piper-voices`: `de_DE-kerstin-low` für A und `de_DE-thorsten-medium` für B, je rund 61 MB, dazu `de_DE-mls-medium` (74 MB) aus einem Stimmvergleich. Python sieht sie unter `%LOCALAPPDATA%\piper-voices`. Weil die Store-Version von Python AppData virtualisiert, liegen sie physisch unter `%LOCALAPPDATA%\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Local\piper-voices`.

## Ergebnisse vom 5.11.2026

Gemessen auf AMD Ryzen 7 7800X3D (8 Kerne) und NVIDIA RTX 4080 mit 16 GB. CPU läuft mit int8, GPU mit float16, Sprache ist fest auf Deutsch gesetzt, Beam-Breite 5. Die Zeiten sind der schnellere von zwei Durchgängen, Echtzeitfaktor ist Transkriptionszeit geteilt durch Audiolänge. Während der Messung belegte ein anderer Prozess über Ollama 10 bis 15 GB der GPU, die GPU-Zeiten schwanken deshalb. Vollständige Werte stehen in `pruefbericht.md` und `messwerte.json`.

| Lauf | Gerät | Transkription | Echtzeitfaktor | WER | 28 | Chai | Côte de Blaye | Agentic Engineering |
|---|---|---|---|---|---|---|---|---|
| small | CPU | 8,1 s | 0,13 | 13,7 % | nein | nein | nein | ja |
| small | GPU | 2,2 s | 0,04 | 8,9 % | ja | ja | nein | ja |
| medium | CPU | 22,6 s | 0,37 | 8,3 % | ja | nein | nein | ja |
| medium | GPU | 3,2 s | 0,05 | 8,3 % | ja | nein | nein | ja |
| large-v3-turbo | CPU | 17,7 s | 0,29 | 8,3 % | ja | nein | nein | ja |
| large-v3-turbo | GPU | 5,5 s | 0,09 | 50,6 % | ja | nein | nein | ja |
| large-v3-turbo mit Glossar, VAD, ohne Kontext | CPU | 17,2 s | 0,28 | 5,4 % | ja | ja | ja | ja |
| large-v3-turbo mit Glossar, VAD, ohne Kontext | GPU | 1,2 s | 0,02 | 5,4 % | ja | ja | ja | ja |
| small mit Glossar, VAD | CPU | 7,6 s | 0,12 | 7,7 % | ja | ja | nein | ja |

Das Laden eines Modells aus dem Cache dauerte 0,7 bis 2,9 s. Der Lauf large-v3-turbo auf der GPU ohne weitere Optionen wiederholte am Ende „Passt. Bis Montag.“ bis zur Zeitmarke 84,8 s, obwohl die Aufnahme nach 61,9 s endet. Diese bekannte Wiederholungsschleife von Whisper erklärt die hohe WER. Die Silero-Sprachaktivitätserkennung (`--vad`) allein verkürzte sie auf höchstens zwei Wiederholungen, erst zusammen mit `--no-context` (kein Übertrag des Vorgängertexts in das nächste 30-Sekunden-Fenster) trat sie in keinem Lauf mehr auf. Ein Lauf mit vier CPU-Threads lieferte dieselben Zeiten wie die Voreinstellung, was vermutlich darauf hinweist, dass CTranslate2 ohne Angabe ebenfalls vier Threads nutzt.

Das Glossar wird als `initial_prompt` übergeben und brachte Chai und Côte de Blaye in die richtige Schreibung. Da es genau die geprüften Namen enthält, zeigt dieser Lauf, dass eine vorab bekannte Namensliste wirkt. Ohne Glossar schrieb jedes Modell den Weinnamen als „Koteblei“ oder „Coteblei“, was der gesprochenen Lautung entspricht. In Kombination mit `--no-context` wirkt der Prompt laut Quellcode von faster-whisper nur im ersten 30-Sekunden-Fenster. Für längere Aufnahmen wäre der Parameter `hotwords` zu prüfen, der in jedem Fenster gilt.

Fehler, die in allen Läufen auftreten, stammen dem Muster nach aus der synthetischen Stimme. Die tiefe Qualitätsstufe von kerstin-low macht aus „Guten Morgen“ „Dr. Norwin“, aus „Gut.“ „Pfff“ oder „Für“ und verschluckt „Prima“. Weitere Abweichungen betreffen Formatierung oder ähnlich klingende Wörter, so steht „neun“ als „9“, „Marge“ als „Marke“ und „kleiner“ als „kleine“.

Die Zusammenfassung mit `qwen3.5:9b` dauerte 5,2 s, davon 2,6 s für 233 erzeugte Tokens. Das Modell war bereits geladen, weil ein anderer Prozess es nutzte. Die Stichpunkte geben Zahl, Produkte, Fachbegriff und die Datenschutzvorgabe richtig wieder. Bei den Aufgaben ergänzte das LLM für die Einladung eine Frist „bis Montag“, die so nicht im Gespräch steht, weil dort nur der Termin am Montag genannt wird.

## Grenzen

- Synthetische TTS-Sprache ist sauberer als eine echte Aufnahme mit Raumhall, Überlappungen, Dialekt und Störgeräuschen. Die Werte sind daher eine Obergrenze für die erreichbare Qualität.
- Whisper unterscheidet keine Sprecher. Das Transkript ist ein fortlaufender Text, eine Sprechertrennung bräuchte ein zusätzliches Werkzeug wie pyannote.
- Der deutsche espeak-Phonemisierer von piper spricht englische und französische Wörter deutsch aus, etwa „Chai“ als „Schai“ und „Agentic“ als „Agentiek“. In einem ersten Durchgang erkannte deshalb kein Modell „Côte de Blaye“ oder „Agentic Engineering“. `erzeuge_audio.py` setzt für diese Begriffe IPA-Lautschrift ein, das Referenzskript behält die normale Schreibung.
- Piper erzeugt mit Zufallsrauschen, jede neue Synthese klingt leicht anders. Die Messwerte gelten für die abgelegte `besprechung.wav`.
- Die Zeiten stammen von einem Desktop-Prozessor. Auf einem Laptop ohne GPU ist vermutlich mit der ein- bis zweieinhalbfachen Dauer zu rechnen, gemessen wurde das nicht.
- WER rechnet „9“ gegen „neun“ als Fehler. Die gezielte Prüfung akzeptiert für die Zahl Ziffern und Wort.
