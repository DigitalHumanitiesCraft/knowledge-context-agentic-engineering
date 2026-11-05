"""Synthesise the reference dialogue locally with piper-tts, one voice per speaker.

Usage: python erzeuge_audio.py
Reads referenzskript.txt (lines "A: ..." / "B: ..."), writes besprechung.wav (16 kHz mono).
"""

import os
import subprocess
import tempfile
import wave
from pathlib import Path

from piper import PiperVoice

HERE = Path(__file__).resolve().parent
VOICE_DIR = Path(os.environ["LOCALAPPDATA"]) / "piper-voices" / "de" / "de_DE"
VOICES = {
    "A": VOICE_DIR / "kerstin" / "low" / "de_DE-kerstin-low.onnx",
    "B": VOICE_DIR / "thorsten" / "medium" / "de_DE-thorsten-medium.onnx",
}
# The German espeak phonemiser reads English and French terms as German
# ("Chai" as "Schai", "Agentic" as "Agentiek"), so the audio would not contain
# what the reference says. These raw IPA blocks fix the pronunciation in the TTS
# input only; referenzskript.txt keeps the normal spelling.
PRONUNCIATION = {
    "Agentic Engineering": "[[ ədʒˈɛntɪk ˌɛndʒɪnˈiːɹɪŋ ]]",
    "Côte de Blaye": "[[ kˈoːt də blˈaj ]]",
    "Chai": "[[ tʃˈaɪ ]]",
    "Excel-Listen": "[[ ˈɛksɛl ]] Listen",
    "Cloud": "[[ klˈaʊt ]]",
}
PAUSE_S = 0.5
# 16 kHz mono is what Whisper resamples to anyway, and keeps the file small.
TARGET_RATE = 16000


def parse_script(path: Path) -> list[tuple[str, str]]:
    turns = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        speaker, text = line.split(":", 1)
        turns.append((speaker.strip(), text.strip()))
    return turns


def main() -> None:
    turns = parse_script(HERE / "referenzskript.txt")
    voices = {k: PiperVoice.load(v) for k, v in VOICES.items()}
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, (speaker, text) in enumerate(turns):
            voice = voices[speaker]
            for word, ipa in PRONUNCIATION.items():
                text = text.replace(word, ipa)
            part = Path(tmp) / f"{i:02d}.wav"
            with wave.open(str(part), "wb") as wf:
                voice.synthesize_wav(text, wf)
                # Silence after each turn so the dialogue does not run together.
                n = int(PAUSE_S * voice.config.sample_rate)
                wf.writeframes(b"\x00\x00" * n)
            parts.append(part)
        # The two voices have different sample rates, so ffmpeg resamples each
        # segment before concatenating.
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for p in parts:
            cmd += ["-i", str(p)]
        chains = "".join(f"[{i}:a]aresample={TARGET_RATE}[a{i}];" for i in range(len(parts)))
        joins = "".join(f"[a{i}]" for i in range(len(parts)))
        cmd += [
            "-filter_complex",
            f"{chains}{joins}concat=n={len(parts)}:v=0:a=1[out]",
            "-map", "[out]", "-ac", "1", "-ar", str(TARGET_RATE),
            str(HERE / "besprechung.wav"),
        ]
        subprocess.run(cmd, check=True)
    with wave.open(str(HERE / "besprechung.wav"), "rb") as wf:
        dur = wf.getnframes() / wf.getframerate()
    print(f"besprechung.wav: {dur:.1f} s, {len(turns)} turns")


if __name__ == "__main__":
    main()
