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
        "side": "Glossary navigation",
        "order": "Order",
        "by_module": "By module",
        "by_letter": "Alphabetical",
        "letters": "Alphabet",
        "details": "German definition",
        "details_related": "German definition and related terms",
        "related": "Related terms",
        "permalink": "Link to this term",
        "for": "for",
        "skip": "Skip to the entries",
        "shortcut": "Ctrl+K or / focuses the search",
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
        "side": "Navigation im Glossar",
        "order": "Ordnung",
        "by_module": "Nach Modul",
        "by_letter": "Alphabetisch",
        "letters": "Alphabet",
        "details": "Englische Definition",
        "details_related": "Englische Definition und verwandte Begriffe",
        "related": "Verwandte Begriffe",
        "permalink": "Link zu diesem Begriff",
        "for": "zu",
        "skip": "Zu den Einträgen springen",
        "shortcut": "Strg+K oder / springt in die Suche",
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


def search_field(term: Term) -> str:
    """Folded words plus the stripped variant of each word that differs, once each."""
    text = " ".join((term.term_en, term.term_de, term.short_en, term.short_de))
    words = normalise(text).split() + normalise(text, fold=False).split()
    return " ".join(dict.fromkeys(words))


def _headwords(term: Term) -> list[str]:
    """Normalised headword parts a sentence can mention, e.g. both halves of "X and Y"."""
    parts = []
    for name in (term.term_en, term.term_de):
        # Greedy, so a nested qualifier such as "(Art. 3(3))" goes as a whole.
        name = re.sub(r"\s*\(.*\)", "", name)
        # No split on "as" or "als": in "Openness as a Multidimensional
        # Property" the second half is a description, not a name of its own.
        pieces = re.split(r"\s+(?:and|und)\s+", name)
        parts.append(name)
        # A single word cut out of a compound name ("Deterministic" from
        # "Deterministic and Probabilistic Tasks") is an ordinary adjective far
        # more often than a mention; it counts only as the stem its partner
        # extends, as in "Token and Tokenization".
        if len(pieces) > 1:
            parts += [p for p in pieces if " " in p]
            first, second = pieces[0], pieces[1]
            if " " not in first and second.lower().startswith(first.lower()):
                parts.append(first)
    # Very short headwords such as "Tag" match ordinary words in the other language.
    return list(dict.fromkeys(p for p in map(normalise, parts) if len(p) >= 4))


# An abbreviation in parentheses, two or more capitals with optional digits:
# MCP, A2A, GPAI, MOC. "(Art. 3(3))" and "(Research)" are qualifiers.
ABBREVIATION = re.compile(r"\((?=(?:[0-9]*[A-Z]){2})([A-Z0-9]+)\)")


def _abbreviations(term: Term) -> list[str]:
    """Abbreviations the term names in parentheses, in their written case."""
    found = ABBREVIATION.findall(f"{term.term_en} {term.term_de}")
    return list(dict.fromkeys(found))


RELATED_MAX = 6

# Headword matches that name a homonym rather than the entry, as
# (entry anchor, related anchor). Each one is checked on every build, so a
# renamed entry or a rewritten sentence that no longer matches is reported
# instead of leaving a dead exclusion behind.
RELATED_EXCLUDE = frozenset(
    {
        # "schema validation" is itself a deterministic check, which module 05
        # sets apart from scholarly or domain validation.
        ("term-deterministic-check", "term-validation-scholarly-or-domain-validation"),
        # "their internal memory" means the agents' own state, not notes an
        # agent writes for later sessions.
        ("term-agent2agent-protocol-a2a", "term-agent-memory-auto-memory"),
        # "individual memory" is a person's recollection.
        ("term-write-back", "term-agent-memory-auto-memory"),
        # "a provider" and "ein Anbieter" are the vendor in the ordinary
        # sense, not the role the AI Act defines in Art. 3(3).
        ("term-assistant-character", "term-provider-art-3-3"),
        ("term-critical-cyber-capability", "term-provider-art-3-3"),
    }
)


def _mentions(terms: list[Term]) -> dict[str, list[Term]]:
    """Every other term whose headword or abbreviation the entry's sentences name."""
    patterns = {
        t.anchor: [
            re.compile(rf"(?<![a-z0-9]){re.escape(h)}(?:s|es|n|en|e)?(?![a-z0-9])")
            for h in _headwords(t)
        ]
        for t in terms
    }
    # Abbreviations are matched in their written case on the raw sentences, so
    # "MOC" cannot match inside an ordinary word; "MCP's", "MCPs" and
    # "GPAI-Modell" count, "GPAIX" does not.
    capitals = {
        t.anchor: [
            re.compile(rf"(?<![A-Za-z0-9]){re.escape(a)}s?(?![A-Za-z0-9])")
            for a in _abbreviations(t)
        ]
        for t in terms
    }
    folded = {t.anchor: normalise(f"{t.short_en} {t.short_de}") for t in terms}
    raw = {t.anchor: f"{t.short_en} {t.short_de}" for t in terms}
    return {
        t.anchor: [
            o
            for o in terms
            if o.anchor != t.anchor
            and (
                any(p.search(folded[t.anchor]) for p in patterns[o.anchor])
                or any(p.search(raw[t.anchor]) for p in capitals[o.anchor])
            )
        ]
        for t in terms
    }


def related(
    terms: list[Term], exclude: frozenset[tuple[str, str]] = RELATED_EXCLUDE
) -> dict[str, list[Term]]:
    """Terms whose headword the entry's own public sentences mention.

    Relations are derived only from the public sentences, so the internal
    definitions in terms.md never shape what the page shows. Reverse links
    were left out: a passing mention elsewhere ("for knowledge work" in the
    Docling sentence) made Docling look related to Knowledge Work.
    """
    return {
        anchor: [o for o in found if (anchor, o.anchor) not in exclude][:RELATED_MAX]
        for anchor, found in _mentions(terms).items()
    }


def stale_exclusions(
    terms: list[Term], exclude: frozenset[tuple[str, str]] = RELATED_EXCLUDE
) -> list[str]:
    """Exclusions that no longer remove a match, because a name or sentence changed."""
    found = {a: {o.anchor for o in near} for a, near in _mentions(terms).items()}
    return [
        f"RELATED_EXCLUDE {source} -> {target} matches nothing; update or remove it"
        for source, target in sorted(exclude)
        if target not in found.get(source, set())
    ]


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


MODULES = ("01", "02", "03", "04", "05", "00")


def _letter(name: str) -> str:
    first = normalise(name, fold=False)[:1].upper()
    return first if "A" <= first <= "Z" else "#"


def _main(terms: list[Term], lang: str, modules: dict) -> str:
    t = TEXT[lang]
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    attr = lambda s: html.escape(s, quote=True)  # noqa: E731
    links = related(terms)
    name = lambda x: x.term_en if lang == "en" else x.term_de  # noqa: E731
    title_of = lambda m: t["general"] if m == "00" else modules[m][lang]  # noqa: E731
    number_of = lambda m: (  # noqa: E731
        "" if m == "00" else f'<span class="glossary-group__number">{m}</span> '
    )
    counts = {m: sum(1 for x in terms if x.module == m) for m in MODULES}
    groups, jump, chips = [], [], []
    for module in MODULES:
        members = sorted(
            (x for x in terms if x.module == module), key=lambda x: normalise(name(x))
        )
        if not members:
            continue
        title = title_of(module)
        number = number_of(module)
        icon = (
            ""
            if module == "00"
            else '<span class="module-icon" aria-hidden="true"></span>'
        )
        cls = "" if module == "00" else f" m{int(module)}"
        jump.append(
            f'<li><a href="#glossary-{module}">{number}{esc(title)}</a> '
            f'<span class="glossary-count">{counts[module]}</span></li>'
        )
        chips.append(
            f'<label class="glossary-chip{cls}"><input type="radio" name="module" value="{module}">'
            f'<span class="glossary-chip__label">{icon}{number}{esc(title)}</span>'
            f'<span class="glossary-count">{counts[module]}</span></label>'
        )
        rows = []
        for x in members:
            primary, alt, alt_lang, short, other = (
                (x.term_en, x.term_de, "de", x.short_en, x.short_de)
                if lang == "en"
                else (x.term_de, x.term_en, "en", x.short_de, x.short_en)
            )
            alt_html = (
                ""
                if alt == primary
                else f' <span class="glossary-entry__alt" lang="{alt_lang}">{esc(alt)}</span>'
            )
            more = (
                f' <a class="glossary-entry__more" href="{attr(x.blog)}">{t["more"]}</a>'
                if x.blog
                else ""
            )
            near = links[x.anchor]
            related_html = (
                f'\n              <p class="glossary-entry__related"><span>{t["related"]}:</span> '
                + ", ".join(f'<a href="#{o.anchor}">{esc(name(o))}</a>' for o in near)
                + "</p>"
                if near
                else ""
            )
            # Shown only in the alphabetical order, where no group heading
            # names the module, so it carries its own accessible text.
            tag = (
                ""
                if module == "00"
                else f'<span class="glossary-entry__module"><span class="visually-hidden">{t["module"]} </span>{module}</span>'
            )
            rows.append(
                f'        <div class="glossary-entry{cls}" id="{x.anchor}" data-module="{module}"'
                f' data-letter="{_letter(primary)}" data-search="{attr(search_field(x))}">\n'
                f"          <dt>{tag}<dfn>{esc(primary)}</dfn>{alt_html}</dt>\n"
                f"          <dd>\n"
                f'            <p class="glossary-entry__def">{esc(short)}{more}</p>\n'
                f'            <details class="glossary-entry__details">\n'
                # The hidden term tells the disclosures apart in a list of controls.
                f"              <summary>{t['details_related'] if near else t['details']}"
                f'<span class="visually-hidden"> {t["for"]} {esc(primary)}</span></summary>\n'
                f'              <p class="glossary-entry__other" lang="{alt_lang}">{esc(other)}</p>'
                f"{related_html}\n"
                f'              <p class="glossary-entry__permalink"><a href="#{x.anchor}">{t["permalink"]}</a></p>\n'
                f"            </details>\n"
                f"          </dd>\n"
                f"        </div>"
            )
        groups.append(
            f'    <section class="glossary-group{cls}" id="glossary-{module}" aria-labelledby="glossary-{module}-title">\n'
            f'      <h2 class="glossary-group__title" id="glossary-{module}-title">{icon}{number}{esc(title)}</h2>\n'
            f'      <dl class="glossary-list">\n'
            + "\n".join(rows)
            + "\n      </dl>\n    </section>"
        )
    present = {_letter(name(x)) for x in terms}
    letters = "".join(
        f'<a href="#letter-{c}" data-letter="{c}">{c}</a>'
        if c in present
        else f'<span aria-hidden="true">{c}</span>'
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    all_chip = (
        f'<label class="glossary-chip"><input type="radio" name="module" value="" checked>'
        f'<span class="glossary-chip__label">{t["all"]}</span>'
        f'<span class="glossary-count">{len(terms)}</span></label>'
    )
    return f'''<main id="main-content" tabindex="-1">

<section class="hero">
  <div class="wrap">
    <h1>{t["title"]}</h1>
    <p class="intro">{t["intro"]} <a href="{t["index"]}">{t["back"]}</a>.</p>
  </div>
</section>

<section class="glossary">
  <div class="wrap glossary-layout">
    <aside class="glossary-side" aria-label="{t["side"]}">
      <nav class="glossary-jump" aria-label="{t["jump"]}"><ul>{"".join(jump)}</ul></nav>
      <form class="glossary-tools" role="search" hidden>
        <label class="glossary-tools__field"><span>{t["search"]}</span><input type="search" name="q" autocomplete="off" aria-keyshortcuts="Control+K /" aria-describedby="glossary-shortcut"></label>
        <p class="glossary-tools__hint" id="glossary-shortcut">{t["shortcut"]}</p>
        <p class="glossary-tools__count" aria-live="polite" data-template="{t["count"]}" data-one="{t["one"]}" data-none="{t["none"]}"></p>
        <fieldset class="glossary-filter">
          <legend>{t["module"]}</legend>
          {all_chip}{"".join(chips)}
        </fieldset>
        <fieldset class="glossary-filter glossary-filter--order">
          <legend>{t["order"]}</legend>
          <label class="glossary-chip"><input type="radio" name="order" value="module" checked><span class="glossary-chip__label">{t["by_module"]}</span></label><label class="glossary-chip"><input type="radio" name="order" value="letter"><span class="glossary-chip__label">{t["by_letter"]}</span></label>
        </fieldset>
        <a class="glossary-skip" href="#glossary-entries">{t["skip"]}</a>
        <nav class="glossary-letters" aria-label="{t["letters"]}">{letters}</nav>
      </form>
    </aside>
    <div class="glossary-main" id="glossary-entries" tabindex="-1">
{chr(10).join(groups)}
    </div>
  </div>
</section>
</main>'''


def build() -> tuple[dict[Path, str], list[str]]:
    terms, errors = _parse(TERMS.read_text(encoding="utf-8").splitlines())
    if not errors:
        errors = stale_exclusions(terms)
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
