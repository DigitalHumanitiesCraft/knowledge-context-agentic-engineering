"""Transcribe a German recording locally with faster-whisper and time each run.

Usage: python transkribiere.py besprechung.wav --models small large-v3-turbo --devices cpu cuda
Writes transkripte/<model>_<device>[_tN].txt and appends one record per run to messwerte.json.
"""

import argparse
import glob
import json
import os
import platform
import site
import time
import wave
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent


def enable_pip_cuda() -> None:
    # CTranslate2 on Windows needs cuBLAS and cuDNN DLLs; the nvidia-*-cu12 pip
    # wheels ship them but do not put them on the DLL search path.
    for d in glob.glob(os.path.join(site.getusersitepackages(), "nvidia", "*", "bin")):
        os.add_dll_directory(d)
        os.environ["PATH"] = d + os.pathsep + os.environ["PATH"]


def audio_seconds(path: Path) -> float:
    with wave.open(str(path), "rb") as wf:
        return wf.getnframes() / wf.getframerate()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", type=Path)
    ap.add_argument("--models", nargs="+", default=["small", "large-v3-turbo"])
    ap.add_argument("--devices", nargs="+", default=["cpu"], choices=["cpu", "cuda"])
    ap.add_argument("--cpu-threads", type=int, default=0, help="0 = CTranslate2 default")
    ap.add_argument(
        "--glossar",
        help="comma-separated names and terms passed as initial_prompt, to bias spelling of proper nouns",
    )
    ap.add_argument("--runs", type=int, default=1, help="transcribe N times, report the fastest")
    ap.add_argument(
        "--vad",
        action="store_true",
        help="skip non-speech with the Silero VAD; guards against Whisper repeating the last sentence",
    )
    ap.add_argument(
        "--no-context",
        action="store_true",
        help="do not feed the previous window's text into the next; the other guard against repetition loops",
    )
    args = ap.parse_args()

    if "cuda" in args.devices:
        enable_pip_cuda()
    from faster_whisper import WhisperModel, download_model

    duration = audio_seconds(args.audio)
    out_dir = HERE / "transkripte"
    out_dir.mkdir(exist_ok=True)
    log_path = HERE / "messwerte.json"
    records = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else []

    for model_name in args.models:
        # Download is timed separately so the transcription time reflects only inference.
        t0 = time.perf_counter()
        model_dir = download_model(model_name)
        download_s = time.perf_counter() - t0
        size_mb = sum(f.stat().st_size for f in Path(model_dir).rglob("*") if f.is_file()) / 1e6

        for device in args.devices:
            compute_type = "int8" if device == "cpu" else "float16"
            threads = args.cpu_threads if device == "cpu" else 0
            t0 = time.perf_counter()
            model = WhisperModel(model_dir, device=device, compute_type=compute_type, cpu_threads=threads)
            load_s = time.perf_counter() - t0

            # The first run on a device includes one-off warm-up (CUDA context,
            # kernel selection), so the fastest of several runs is reported too.
            run_times = []
            for _ in range(args.runs):
                t0 = time.perf_counter()
                segments, info = model.transcribe(
                    str(args.audio),
                    language="de",
                    beam_size=5,
                    initial_prompt=args.glossar,
                    vad_filter=args.vad,
                    condition_on_previous_text=not args.no_context,
                )
                # transcribe() is lazy; decoding happens while the generator is consumed.
                segments = list(segments)
                run_times.append(time.perf_counter() - t0)
            transcribe_s = min(run_times)

            text = " ".join(s.text.strip() for s in segments)
            tag = f"{model_name}_{device}" + (f"_t{threads}" if device == "cpu" and threads else "")
            tag += "_glossar" if args.glossar else ""
            tag += "_vad" if args.vad else ""
            tag += "_nocontext" if args.no_context else ""
            lines = [f"[{s.start:6.1f} - {s.end:6.1f}] {s.text.strip()}" for s in segments]
            (out_dir / f"{tag}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

            rec = {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "tag": tag,
                "model": model_name,
                "model_dir": str(model_dir),
                "model_size_mb": round(size_mb, 1),
                "download_or_cache_check_s": round(download_s, 2),
                "device": device,
                "compute_type": compute_type,
                "cpu_threads": threads,
                "glossar": args.glossar,
                "vad_filter": args.vad,
                "condition_on_previous_text": not args.no_context,
                "cpu": platform.processor(),
                "audio_s": round(duration, 2),
                "load_s": round(load_s, 2),
                "transcribe_s": round(transcribe_s, 2),
                "transcribe_runs_s": [round(t, 2) for t in run_times],
                "rtf": round(transcribe_s / duration, 3),
                "text": text,
            }
            records.append(rec)
            log_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"{tag}: load {load_s:.1f} s, transcribe {transcribe_s:.1f} s, RTF {rec['rtf']}")
            del model


if __name__ == "__main__":
    main()
