# Prüfbericht Sprache zu Text

Erzeugt von `pruefe.py` aus `messwerte.json` und `referenzskript.txt`.
Wortfehlerrate (WER) nach Kleinschreibung, Entfernen der Satzzeichen und Bindestrich als Leerzeichen.
Audiolänge 61.89 s. Zeiten in Sekunden, Echtzeitfaktor = Transkriptionszeit / Audiolänge.

Transkription: schnellster Durchgang, in Klammern alle Durchgänge. Laden ohne Download.

| Lauf | Transkription s | Echtzeitfaktor | Laden s | WER | Zahl 28 | Produkt Chai | Produkt Côte de Blaye | Fachbegriff Agentic Engineering |
|---|---|---|---|---|---|---|---|---|
| small_cpu | 8.06 (10.82, 8.06) | 0.13 | 1.13 | 13.7% | nein | nein | nein | ja |
| small_cuda | 2.23 (2.96, 2.23) | 0.036 | 0.69 | 8.9% | ja | ja | nein | ja |
| medium_cpu | 22.56 (23.0, 22.56) | 0.365 | 2.77 | 8.3% | ja | nein | nein | ja |
| medium_cuda | 3.23 (3.23, 4.32) | 0.052 | 1.55 | 8.3% | ja | nein | nein | ja |
| large-v3-turbo_cpu | 17.67 (18.08, 17.67) | 0.286 | 2.88 | 8.3% | ja | nein | nein | ja |
| large-v3-turbo_cuda | 5.5 (5.5, 6.16) | 0.089 | 1.84 | 50.6% | ja | nein | nein | ja |
| small_cpu_t4 | 7.34 (7.34, 8.19) | 0.119 | 0.67 | 13.7% | nein | nein | nein | ja |
| large-v3-turbo_cpu_t4 | 17.69 (17.69, 19.39) | 0.286 | 2.53 | 8.3% | ja | nein | nein | ja |
| large-v3-turbo_cpu_glossar | 22.9 (25.52, 22.9) | 0.37 | 2.06 | 8.9% | ja | ja | ja | ja |
| large-v3-turbo_cuda_glossar | 1.22 (1.43, 1.22) | 0.02 | 1.73 | 5.4% | ja | ja | ja | ja |
| small_cpu_glossar | 7.67 (7.97, 7.67) | 0.124 | 0.79 | 7.7% | ja | ja | nein | ja |
| small_cuda_glossar | 1.81 (1.83, 1.81) | 0.029 | 0.74 | 7.7% | ja | ja | nein | ja |
| large-v3-turbo_cpu_vad | 17.72 (17.72, 17.77) | 0.286 | 2.28 | 8.3% | ja | nein | nein | ja |
| large-v3-turbo_cuda_vad | 5.3 (5.3, 6.39) | 0.086 | 1.53 | 9.5% | ja | nein | nein | ja |
| large-v3-turbo_cpu_glossar_vad | 23.01 (23.68, 23.01) | 0.372 | 2.37 | 8.9% | ja | ja | ja | ja |
| large-v3-turbo_cuda_glossar_vad | 1.27 (1.46, 1.27) | 0.021 | 1.65 | 5.4% | ja | ja | ja | ja |
| small_cpu_glossar_vad | 7.63 (7.63, 7.77) | 0.123 | 0.78 | 7.7% | ja | ja | nein | ja |
| small_cuda_glossar_vad | 1.89 (1.96, 1.89) | 0.031 | 0.75 | 7.7% | ja | ja | nein | ja |
| large-v3-turbo_cpu_glossar_vad_nocontext | 17.17 (17.26, 17.17) | 0.277 | 2.11 | 5.4% | ja | ja | ja | ja |
| large-v3-turbo_cuda_glossar_vad_nocontext | 1.21 (1.44, 1.21) | 0.02 | 1.65 | 5.4% | ja | ja | ja | ja |
| large-v3-turbo_cpu_vad_nocontext | 17.22 (17.58, 17.22) | 0.278 | 2.05 | 8.3% | ja | nein | nein | ja |
| large-v3-turbo_cuda_vad_nocontext | 1.15 (1.33, 1.15) | 0.019 | 1.46 | 7.7% | ja | nein | nein | ja |

## Abweichungen je Lauf (Referenz -> Transkript)

### small_cpu

- guten morgen lass -> dutte norwen lasst
- den -> dem
- (leer) -> dazu
- dazukommt -> kommt
- dritten quartal -> 3 krathal
- (leer) -> 8 und
- 28 -> 20
- gut -> pff
- chai -> tschey
- côte -> koteblei
- de blaye -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> gerne
- neun -> 9

### small_cuda

- (leer) -> do
- guten morgen lass -> the norwen lasst
- den -> dem
- gut -> pff
- côte -> koteblei
- de blaye -> (leer)
- (leer) -> geil
- also -> so
- prima -> wieder
- kümmere -> kümmer
- neun -> 9
- passt -> hast

### medium_cpu

- guten morgen -> dr norwin
- (leer) -> dazu
- dazukommt -> kommt
- gut -> pfff
- chai -> tschei
- côte -> coteblei
- de blaye -> (leer)
- kleiner -> kleine
- also wie -> guy sowie
- prima -> (leer)
- neun -> 9

### medium_cuda

- guten morgen -> dr norwin
- (leer) -> dazu
- dazukommt -> kommt
- gut -> für
- chai -> tschei
- côte -> koteblei
- de blaye -> (leer)
- kleiner -> kleine
- also wie -> guy sowie
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cpu

- guten morgen -> dr norwin
- gut -> pfiff
- chai danach -> tscheider nach
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cuda

- guten morgen -> dr norwin
- gut -> für
- chai -> schei
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9
- (leer) -> passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag passt bis montag

### small_cpu_t4

- guten morgen lass -> dutte norwen lasst
- den -> dem
- (leer) -> dazu
- dazukommt -> kommt
- dritten quartal -> 3 krathal
- (leer) -> 8 und
- 28 -> 20
- gut -> pff
- chai -> tschey
- côte -> koteblei
- de blaye -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> gerne
- neun -> 9

### large-v3-turbo_cpu_t4

- guten morgen -> dr norwin
- gut -> pfiff
- chai danach -> tscheider nach
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cpu_glossar

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9
- (leer) -> passt bis montag passt bis montag

### large-v3-turbo_cuda_glossar

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### small_cpu_glossar

- guten morgen -> (leer)
- den -> dem
- quartal -> krathal
- gut -> pff
- de -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> friedo
- neun -> 9

### small_cuda_glossar

- guten morgen -> (leer)
- dritten quartal -> 3 krathal
- gut -> pff
- de -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> wieder
- neun -> 9

### large-v3-turbo_cpu_vad

- guten morgen -> dr norwin
- gut -> pfiff
- chai danach -> tscheider nach
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cuda_vad

- guten morgen -> dr norwin
- gut -> für
- chai -> schei
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9
- (leer) -> passt bis montag

### large-v3-turbo_cpu_glossar_vad

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9
- (leer) -> passt bis montag passt bis montag

### large-v3-turbo_cuda_glossar_vad

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### small_cpu_glossar_vad

- guten morgen -> (leer)
- den -> dem
- quartal -> krathal
- gut -> pff
- de -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> friedo
- neun -> 9

### small_cuda_glossar_vad

- guten morgen -> (leer)
- dritten quartal -> 3 krathal
- gut -> pff
- de -> (leer)
- kleiner -> kleine
- (leer) -> geil
- also -> so
- (leer) -> kunden
- kundendaten -> daten
- prima -> wieder
- neun -> 9

### large-v3-turbo_cpu_glossar_vad_nocontext

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cuda_glossar_vad_nocontext

- guten morgen -> dr norwin
- gut -> für
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cpu_vad_nocontext

- guten morgen -> dr norwin
- gut -> pfiff
- chai danach -> tscheider nach
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9

### large-v3-turbo_cuda_vad_nocontext

- guten morgen -> dr norwin
- gut -> für
- chai -> schei
- côte -> koteblei
- de blaye -> (leer)
- marge -> marke
- kleiner -> kleine
- (leer) -> geil
- also -> so
- prima -> (leer)
- neun -> 9
