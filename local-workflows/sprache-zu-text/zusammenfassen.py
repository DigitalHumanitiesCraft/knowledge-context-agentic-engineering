"""Summarise a transcript with a local Ollama model into key points and open tasks.

Usage: python zusammenfassen.py transkripte/large-v3-turbo_cuda.txt [--model qwen3.5:9b] [--out DIR]
Writes zusammenfassung_<transcript>.md with model and wall-clock time in its header and prints
only the output path. The summary of an own recording is content a cloud agent must not see,
and an agent that started the run reads the console.
"""

import argparse
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Local endpoint only; the transcript must not leave the machine. 127.0.0.1 instead of
# localhost: on Windows the IPv6 attempt first costs about two seconds per call.
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

PROMPT = (
    "Hier ist das automatisch erstellte Transkript einer Besprechung. "
    "Das Transkript unterscheidet keine Sprecher und kann Erkennungsfehler enthalten.\n\n"
    "Erstelle auf Deutsch:\n"
    "1. Stichpunkte: die wichtigsten Inhalte, höchstens sechs.\n"
    "2. Offene Aufgaben: wer was bis wann erledigt, soweit das Transkript es sagt. "
    "Wenn eine Person nicht erkennbar ist, schreibe 'nicht genannt'.\n"
    "Erfinde nichts, was nicht im Transkript steht.\n\nTranskript:\n"
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript", type=Path)
    ap.add_argument("--model", default="qwen3.5:9b")
    ap.add_argument(
        "--out",
        type=Path,
        default=HERE,
        help="folder for the summary; for own recordings outside the repository",
    )
    args = ap.parse_args()

    raw = args.transcript.read_text(encoding="utf-8")
    # Drop the timestamps so the model sees plain prose.
    text = " ".join(
        re.sub(r"^\[[^\]]*\]\s*", "", line) for line in raw.splitlines() if line.strip()
    )
    body = {
        "model": args.model,
        "messages": [{"role": "user", "content": PROMPT + text}],
        "stream": False,
        "think": False,
        "options": {"temperature": 0},
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError) as e:
        raise SystemExit(
            f"Ollama unter {OLLAMA_URL} nicht erreichbar oder Modell {args.model} fehlt ({e})."
        ) from e
    wall_s = time.perf_counter() - t0

    answer = result["message"]["content"].strip()
    args.out.mkdir(parents=True, exist_ok=True)
    out = args.out / f"zusammenfassung_{args.transcript.stem}.md"
    meta = (
        f"Modell {args.model}, Quelle `{args.transcript.name}`, Laufzeit {wall_s:.1f} s "
        f"(Ollama: load {result.get('load_duration', 0) / 1e9:.1f} s, "
        f"eval {result.get('eval_count', 0)} Tokens in {result.get('eval_duration', 0) / 1e9:.1f} s)"
    )
    out.write_text(f"# Zusammenfassung\n\n{meta}\n\n{answer}\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
