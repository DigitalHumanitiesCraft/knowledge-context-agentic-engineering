"""Regression checks for the glossary parser at the internal/public boundary.

Run with `python -m unittest discover -s scripts` from the repository root.
"""

import unittest

from build_glossary import _parse, normalise, related, search_field

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
