"""Convert PDF (or DOCX) files to Markdown with Docling, entirely on this machine.

Usage: python convert.py [FILE ...]   (default: every PDF in ./input)

Writes output/<name>.md (output/<name>.docx.md for DOCX) and prints wall-clock timings, split into import,
pipeline setup and per-file conversion, because the first two dominate a
live demo and are paid once per process.
"""

import logging
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "output"


def main(argv: list[str]) -> int:
    files = [Path(a) for a in argv] or sorted((HERE / "input").glob("*.pdf"))
    missing = [f for f in files if not f.is_file()]
    if missing:
        print(f"not found: {', '.join(map(str, missing))}", file=sys.stderr)
        return 1

    # INFO shows which models and OCR engine Docling actually loads.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    t0 = time.perf_counter()
    from docling.document_converter import DocumentConverter

    t1 = time.perf_counter()
    converter = DocumentConverter()
    # Pipelines are built lazily; initialize_pipeline makes setup time visible
    # separately instead of hiding it in the first conversion.
    from docling.datamodel.base_models import InputFormat

    converter.initialize_pipeline(InputFormat.PDF)
    t2 = time.perf_counter()
    print(f"TIME import_s={t1 - t0:.1f} setup_s={t2 - t1:.1f}")

    OUTPUT.mkdir(exist_ok=True)
    for path in files:
        start = time.perf_counter()
        result = converter.convert(path)
        markdown = result.document.export_to_markdown()
        elapsed = time.perf_counter() - start
        # Non-PDF sources keep their extension so a DOCX and the PDF made from
        # it do not overwrite each other's Markdown.
        name = f"{path.stem}.md" if path.suffix.lower() == ".pdf" else f"{path.name}.md"
        target = OUTPUT / name
        target.write_text(markdown, encoding="utf-8")
        pages = len(result.document.pages)
        print(f"TIME file={path.name} pages={pages} convert_s={elapsed:.1f} -> {target.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
