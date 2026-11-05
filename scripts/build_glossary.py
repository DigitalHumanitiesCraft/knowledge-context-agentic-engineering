# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Build the public glossary pages from the canonical glossary.

Regime: single-file script with inline metadata and no first-party imports.

Data flow: `knowledge/terms.md` is the one maintained source of every term.
Each public entry carries, at its end, the fields `*Short.*` (one English
sentence), `*Begriff.*` (the German term) and `*Kurz.*` (one German sentence),
and optionally `*Blog.*` (a link to the explaining blog section). The module
comes from the section the entry stands in. The page chrome (head, header,
footer) is taken from `docs/index.html` and `docs/index.de.html`, so the
glossary never diverges from the landing pages. Output is
`docs/glossary.html` and `docs/glossary.de.html`; `knowledge/` itself is never
published.

Usage: `uv run scripts/build_glossary.py` from the repository root, or
`python scripts/build_glossary.py`. `--check` builds in memory and exits 1 if
the committed pages differ, so a stale page cannot go unnoticed.

Design decisions:
- Each entry is parsed on its own; a malformed entry is collected with its
  line number and reported, and the pages are written only when every entry
  is complete (skip-and-log-and-collect, exit 0 only on complete success).
- Search runs on a precomputed normalised field (umlaut folding, diacritics
  stripped, case folded), so the enhancement script needs no search library
  and the page stays complete without JavaScript.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / "knowledge" / "terms.md"
VIDEOS = ROOT / "data" / "videos.json"
DOCS = ROOT / "docs"
BASE = "https://dhcraft.org/knowledge-context-agentic-engineering/"

# A field value runs to the next italic label of any kind, so no internal
# note can slip into a published sentence.
LABEL = re.compile(r"\*([A-Z][^*]*?)\.\*")
FIELD = re.compile(r"\*(Short|Begriff|Kurz|Blog)\.\*\s+(.+?)(?=\s+\*[A-Z][^*]*?\.\*|$)")
PUBLIC = ("Short", "Begriff", "Kurz", "Blog")
ENTRY = re.compile(r"^- \*\*(?P<term>.+?)\.\*\* ")
SECTION = re.compile(r"^## (?:(?P<num>[1-5]) )?(?P<title>.+)$")
FOLD = str.maketrans(
    {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "ae", "Ö": "oe", "Ü": "ue"}
)

TEXT = {
    "en": {
        "file": "glossary.html",
        "other": "glossary.de.html",
        "index": "index.html",
        "title": "Glossary",
        "description": "One-sentence definitions of the terms used in the five modules of Knowledge, Context and Agentic Engineering for Knowledge Work, in English and German.",
        "intro": "One-sentence definitions of the terms the five modules use, with their German counterparts.",
        "back": "Back to the teaching materials",
        "search": "Search terms",
        "module": "Module",
        "all": "All modules",
        "general": "General and cross-cutting",
        "count": "{n} terms",
        "one": "1 term",
        "none": "No term matches this search.",
        "more": "Read more",
        "jump": "Modules",
        "locale": "en_GB",
    },
    "de": {
        "file": "glossary.de.html",
        "other": "glossary.html",
        "index": "index.de.html",
        "title": "Glossar",
        "description": "Ein-Satz-Definitionen der Begriffe aus den fünf Modulen von Knowledge, Context and Agentic Engineering for Knowledge Work, auf Deutsch und Englisch.",
        "intro": "Ein-Satz-Definitionen der Begriffe, die die fünf Module verwenden, mit ihren englischen Entsprechungen.",
        "back": "Zurück zu den Lehrmaterialien",
        "search": "Begriffe durchsuchen",
        "module": "Modul",
        "all": "Alle Module",
        "general": "Übergreifend",
        "count": "{n} Begriffe",
        "one": "1 Begriff",
        "none": "Kein Begriff passt zu dieser Suche.",
        "more": "Mehr lesen",
        "jump": "Module",
        "locale": "de_DE",
    },
}


@dataclass(frozen=True)
class Term:
    """One public glossary entry as parsed from terms.md."""

    term_en: str
    term_de: str
    short_en: str
    short_de: str
    module: str
    blog: str | None
    line: int

    @property
    def anchor(self) -> str:
        return "term-" + re.sub(r"[^a-z0-9]+", "-", normalise(self.term_en)).strip("-")


def normalise(text: str, fold: bool = True) -> str:
    """Fold umlauts (or, with fold=False, only strip them), strip diacritics and case."""
    decomposed = unicodedata.normalize("NFD", text.translate(FOLD) if fold else text)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).casefold()


def _field_problems(line: str) -> list[str]:
    """Public fields come last, once each, with no internal label among them."""
    labels = LABEL.findall(line)
    first = next((i for i, label in enumerate(labels) if label in PUBLIC), None)
    if first is None:
        return []
    problems = [
        f"internal label {label} after the public fields"
        for label in labels[first:]
        if label not in PUBLIC
    ]
    problems += [f"{label} given twice" for label in PUBLIC if labels.count(label) > 1]
    return problems


def _parse(lines: list[str]) -> tuple[list[Term], list[str]]:
    terms: list[Term] = []
    errors: list[str] = []
    module: str | None = None
    for number, line in enumerate(lines, start=1):
        section = SECTION.match(line)
        if section:
            title = section.group("title").strip()
            if title == "References":
                break
            if section.group("num"):
                module = f"0{section.group('num')}"
            else:
                module = "00" if title.startswith("General") else None
            continue
        entry = ENTRY.match(line)
        if not entry:
            continue
        where = f"terms.md:{number} {entry.group('term')}"
        if module is None:
            errors.append(f"{where}: entry outside a module section")
            continue
        problems = _field_problems(line)
        found = FIELD.findall(line)
        fields = dict(found)
        missing = [name for name in ("Short", "Begriff", "Kurz") if name not in fields]
        if missing:
            problems.append(f"missing {', '.join(missing)}")
        blog = fields.get("Blog", "").strip().rstrip(".") or None
        if blog and not blog.startswith("https://"):
            problems.append("Blog must be an https:// URL")
        if problems:
            errors.append(f"{where}: {'; '.join(problems)}")
            continue
        terms.append(
            Term(
                term_en=entry.group("term"),
                term_de=fields["Begriff"].rstrip("."),
                short_en=fields["Short"].strip(),
                short_de=fields["Kurz"].strip(),
                module=module,
                blog=blog,
                line=number,
            )
        )
    anchors = [t.anchor for t in terms]
    errors += [
        f"duplicate anchor {a}"
        for a in sorted({a for a in anchors if anchors.count(a) > 1})
    ]
    return terms, errors


def _chrome(lang: str) -> tuple[str, str]:
    """Head and header from the landing page, footer after its main element."""
    page = (DOCS / TEXT[lang]["index"]).read_text(encoding="utf-8")
    top = page[: page.index('<main id="main-content" tabindex="-1">')]
    bottom = page[page.index("</main>") + len("</main>") :]
    return top, bottom


def _head(top: str, lang: str) -> tuple[str, list[str]]:
    t = TEXT[lang]
    url = BASE + t["file"]
    site = "Knowledge, Context and Agentic Engineering"
    rules = (
        (r"<title>.*?</title>", f"<title>{t['title']}: {site}</title>"),
        (r'(<meta name="description" content=")[^"]*', rf"\g<1>{t['description']}"),
        (
            r'(<meta property="og:description" content=")[^"]*',
            rf"\g<1>{t['description']}",
        ),
        (r'(<meta property="og:title" content=")[^"]*', rf"\g<1>{t['title']}: {site}"),
        (r'(<link rel="canonical" href=")[^"]*', rf"\g<1>{url}"),
        (r'(<meta property="og:url" content=")[^"]*', rf"\g<1>{url}"),
        (r'(hreflang="en" href=")[^"]*', rf"\g<1>{BASE}glossary.html"),
        (r'(hreflang="de" href=")[^"]*', rf"\g<1>{BASE}glossary.de.html"),
        (r'(hreflang="x-default" href=")[^"]*', rf"\g<1>{BASE}glossary.html"),
        # The language control switches between the two glossary pages.
        (r'<a href="index\.html" lang="en"', '<a href="glossary.html" lang="en"'),
        (
            r'<a href="index\.de\.html" lang="de"',
            '<a href="glossary.de.html" lang="de"',
        ),
    )
    errors = []
    for pattern, replacement in rules:
        top, hits = re.subn(pattern, replacement, top, count=1)
        if not hits:
            errors.append(f"{t['index']}: no match for {pattern}")
    return top, errors


def _main(terms: list[Term], lang: str, modules: dict) -> str:
    t = TEXT[lang]
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    groups = []
    jump = []
    for module in ("01", "02", "03", "04", "05", "00"):
        members = sorted(
            (x for x in terms if x.module == module),
            key=lambda x: normalise(x.term_en if lang == "en" else x.term_de),
        )
        if not members:
            continue
        title = t["general"] if module == "00" else modules[module][lang]
        number = (
            ""
            if module == "00"
            else f'<span class="glossary-group__number">{module}</span> '
        )
        icon = (
            ""
            if module == "00"
            else '<span class="module-icon" aria-hidden="true"></span>'
        )
        cls = "" if module == "00" else f" m{int(module)}"
        jump.append(f'<li><a href="#glossary-{module}">{number}{esc(title)}</a></li>')
        rows = []
        for x in members:
            primary, alt, alt_lang, short = (
                (x.term_en, x.term_de, "de", x.short_en)
                if lang == "en"
                else (x.term_de, x.term_en, "en", x.short_de)
            )
            alt_html = (
                ""
                if alt == primary
                else f' <span class="glossary-entry__alt" lang="{alt_lang}">{esc(alt)}</span>'
            )
            more = (
                f' <a class="glossary-entry__more" href="{html.escape(x.blog)}">{t["more"]}</a>'
                if x.blog
                else ""
            )
            # Both spellings are indexed, so "ueber" and "uber" find "über".
            text = " ".join((x.term_en, x.term_de, x.short_en, x.short_de))
            variants = dict.fromkeys((normalise(text), normalise(text, fold=False)))
            search = html.escape(" ".join(variants))
            rows.append(
                f'        <div class="glossary-entry" id="{x.anchor}" data-module="{module}" data-search="{search}">\n'
                f"          <dt><dfn>{esc(primary)}</dfn>{alt_html}</dt>\n"
                f"          <dd>{esc(short)}{more}</dd>\n"
                f"        </div>"
            )
        groups.append(
            f'    <section class="glossary-group{cls}" id="glossary-{module}" aria-labelledby="glossary-{module}-title">\n'
            f'      <h2 class="glossary-group__title" id="glossary-{module}-title">{icon}{number}{esc(title)}</h2>\n'
            f'      <dl class="glossary-list">\n'
            + "\n".join(rows)
            + "\n      </dl>\n    </section>"
        )
    options = "".join(
        f'<option value="{m}">{"" if m == "00" else m + " "}{esc(t["general"] if m == "00" else modules[m][lang])}</option>'
        for m in ("01", "02", "03", "04", "05", "00")
    )
    return f'''<main id="main-content" tabindex="-1">

<section class="hero">
  <div class="wrap">
    <h1>{t["title"]}</h1>
    <p class="intro">{t["intro"]} <a href="{t["index"]}">{t["back"]}</a>.</p>
  </div>
</section>

<section class="glossary">
  <div class="wrap">
    <nav class="glossary-jump" aria-label="{t["jump"]}"><ul>{"".join(jump)}</ul></nav>
    <form class="glossary-tools" role="search" hidden>
      <label class="glossary-tools__field"><span>{t["search"]}</span><input type="search" name="q" autocomplete="off"></label>
      <label class="glossary-tools__field"><span>{t["module"]}</span><select name="module"><option value="">{t["all"]}</option>{options}</select></label>
      <p class="glossary-tools__count" aria-live="polite" data-template="{t["count"]}" data-one="{t["one"]}" data-none="{t["none"]}"></p>
    </form>
{chr(10).join(groups)}
  </div>
</section>
</main>'''


def build() -> tuple[dict[Path, str], list[str]]:
    terms, errors = _parse(TERMS.read_text(encoding="utf-8").splitlines())
    if errors:
        return {}, errors
    modules = json.loads(VIDEOS.read_text(encoding="utf-8"))["modules"]
    pages, errors = {}, []
    for lang, t in TEXT.items():
        top, bottom = _chrome(lang)
        head, problems = _head(top, lang)
        errors += problems
        pages[DOCS / t["file"]] = head + _main(terms, lang, modules) + bottom
    if errors:
        return {}, errors
    return pages, [f"{len(terms)} terms"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the committed pages are out of date",
    )
    args = parser.parse_args()
    pages, messages = build()
    if not pages:
        print("glossary not built:", file=sys.stderr)
        print("\n".join(messages), file=sys.stderr)
        return 1
    stale = [
        p
        for p, text in pages.items()
        if not p.exists() or p.read_text(encoding="utf-8") != text
    ]
    if args.check:
        for p in stale:
            print(f"stale: {p.relative_to(ROOT)}", file=sys.stderr)
        return 1 if stale else 0
    for p, text in pages.items():
        p.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {len(pages)} pages, {messages[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
