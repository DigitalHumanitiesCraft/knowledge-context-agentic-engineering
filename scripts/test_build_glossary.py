"""Regression checks for the glossary parser at the internal/public boundary.

Run with `python -m unittest discover -s scripts` from the repository root.
"""

import unittest

from build_glossary import (
    RELATED_EXCLUDE,
    TERMS,
    _headwords,
    _parse,
    normalise,
    related,
    search_field,
    stale_exclusions,
)

HEAD = ["## 2 Prompt Engineering", ""]
BASE = "- **Term.** German Begriff. Body. *Source.* Deck. *Literature.* None."
PUBLIC = " *Short.* One. *Begriff.* Begriff. *Kurz.* Eins."


class ParseTests(unittest.TestCase):
    def parse(self, line: str, head: list[str] = HEAD):
        return _parse([*head, line])

    def test_complete_entry(self) -> None:
        terms, errors = self.parse(BASE + PUBLIC)
        self.assertEqual(errors, [])
        self.assertEqual((terms[0].short_de, terms[0].module), ("Eins.", "02"))

    def test_internal_label_after_public_fields_is_refused(self) -> None:
        terms, errors = self.parse(BASE + PUBLIC + " *Editorial decision.* Hidden.")
        self.assertEqual(terms, [])
        self.assertIn("internal label", errors[0])

    def test_duplicate_field_is_refused(self) -> None:
        _, errors = self.parse(BASE + PUBLIC + " *Kurz.* Zwei.")
        self.assertIn("Kurz given twice", errors[0])

    def test_blog_link_is_trimmed_and_must_be_https(self) -> None:
        terms, _ = self.parse(BASE + PUBLIC + " *Blog.* https://dhcraft.org/x.")
        self.assertEqual(terms[0].blog, "https://dhcraft.org/x")
        _, errors = self.parse(BASE + PUBLIC + " *Blog.* javascript:alert(1)")
        self.assertIn("https://", errors[0])

    def test_entry_outside_a_module_is_reported(self) -> None:
        _, errors = self.parse(BASE + PUBLIC, head=["## Unknown", ""])
        self.assertIn("outside a module", errors[0])

    def test_missing_fields_are_reported(self) -> None:
        _, errors = self.parse(BASE)
        self.assertIn("missing Short, Begriff, Kurz", errors[0])

    def test_related_terms_come_from_the_entrys_own_sentences(self) -> None:
        head = ["## 3 Knowledge and Context Engineering", ""]
        lines = [
            *head,
            "- **Token and Tokenization.** B. *Short.* Units. *Begriff.* Token. *Kurz.* Einheiten.",
            "- **Context Window.** B. *Short.* Limit in tokens. *Begriff.* Kontextfenster. *Kurz.* Grenze.",
            "- **Deterministic and Probabilistic Tasks.** B. *Short.* Split. *Begriff.* Aufteilung. *Kurz.* Teilung.",
            "- **Validation.** B. *Short.* Resists deterministic testing. *Begriff.* Validierung. *Kurz.* Prüfung.",
        ]
        terms, errors = _parse(lines)
        self.assertEqual(errors, [])
        found = related(terms)
        links = {t.term_en: [o.term_en for o in found[t.anchor]] for t in terms}
        # "tokens" mentions the stem of "Token and Tokenization".
        self.assertEqual(links["Context Window"], ["Token and Tokenization"])
        # A lone adjective cut out of a compound name is no mention.
        self.assertEqual(links["Validation"], [])
        # Relations run one way, from the entry that names the other.
        self.assertEqual(links["Token and Tokenization"], [])

    def test_parenthesised_abbreviation_is_a_headword(self) -> None:
        head = ["## 4 Agentic Engineering", ""]
        lines = [
            *head,
            "- **Model Context Protocol (MCP).** B. *Short.* An open standard. "
            "*Begriff.* Model Context Protocol (MCP). *Kurz.* Ein Standard.",
            "- **Agent2Agent Protocol (A2A).** B. *Short.* Complementing MCP's "
            "agent-to-tool standard. *Begriff.* Agent2Agent (A2A). *Kurz.* Ergänzung.",
            "- **Map of Content (MOC).** B. *Short.* Unlike an MCPX server, XA2A "
            "or mcp in lower case. *Begriff.* Map of Content (MOC). *Kurz.* Einstieg.",
        ]
        terms, errors = _parse(lines)
        self.assertEqual(errors, [])
        found = related(terms, exclude=frozenset())
        links = {t.term_en: [o.term_en for o in found[t.anchor]] for t in terms}
        self.assertEqual(
            links["Agent2Agent Protocol (A2A)"], ["Model Context Protocol (MCP)"]
        )
        # Abbreviations match in their written case and as whole words only.
        self.assertEqual(links["Map of Content (MOC)"], [])

    def test_as_does_not_split_a_headword(self) -> None:
        terms, _ = self.parse(
            "- **Openness as a Multidimensional Property.** B. *Short.* One. "
            "*Begriff.* mehrdimensionale Offenheit. *Kurz.* Eins."
        )
        self.assertEqual(
            _headwords(terms[0]),
            ["openness as a multidimensional property", "mehrdimensionale offenheit"],
        )

    def test_excluded_homonym_is_dropped_and_a_stale_exclusion_reported(self) -> None:
        head = ["## 5 Critical Perspectives and Governance", ""]
        lines = [
            *head,
            "- **Validation (Scholarly or Domain Validation).** B. *Short.* Adequacy. "
            "*Begriff.* Validierung. *Kurz.* Angemessenheit.",
            "- **Deterministic Check.** B. *Short.* Such as schema validation. "
            "*Begriff.* Deterministische Prüfung. *Kurz.* Etwa Schemavalidierung.",
        ]
        terms, _ = _parse(lines)
        pair = (
            "term-deterministic-check",
            "term-validation-scholarly-or-domain-validation",
        )
        self.assertEqual(len(related(terms, exclude=frozenset())[pair[0]]), 1)
        self.assertEqual(related(terms, exclude=frozenset({pair}))[pair[0]], [])
        self.assertEqual(stale_exclusions(terms, exclude=frozenset({pair})), [])
        renamed = frozenset({("term-deterministic-checks", pair[1])})
        self.assertIn("matches nothing", stale_exclusions(terms, exclude=renamed)[0])

    def test_homonym_exclusions_hold_on_the_real_glossary(self) -> None:
        # Every listed exclusion still matches terms.md and removes its relation.
        terms, errors = _parse(TERMS.read_text(encoding="utf-8").splitlines())
        self.assertEqual(errors, [])
        self.assertEqual(stale_exclusions(terms), [])
        found = related(terms)
        for source, target in RELATED_EXCLUDE:
            self.assertNotIn(target, [o.anchor for o in found[source]])

    def test_search_field_lists_each_word_once(self) -> None:
        terms, _ = self.parse(
            BASE + " *Short.* Über über. *Begriff.* Begriff. *Kurz.* Eins."
        )
        words = search_field(terms[0]).split()
        self.assertEqual(len(words), len(set(words)))
        self.assertIn("ueber", words)
        self.assertIn("uber", words)

    def test_normalise_folds_or_strips_umlauts(self) -> None:
        self.assertEqual(normalise("Überdestillation"), "ueberdestillation")
        self.assertEqual(normalise("Überdestillation", fold=False), "uberdestillation")


if __name__ == "__main__":
    unittest.main()
