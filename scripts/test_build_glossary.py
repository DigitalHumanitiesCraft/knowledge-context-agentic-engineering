"""Regression checks for the glossary parser at the internal/public boundary.

Run with `python -m unittest discover -s scripts` from the repository root.
"""

import unittest

from build_glossary import _parse, normalise

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

    def test_normalise_folds_or_strips_umlauts(self) -> None:
        self.assertEqual(normalise("Überdestillation"), "ueberdestillation")
        self.assertEqual(normalise("Überdestillation", fold=False), "uberdestillation")


if __name__ == "__main__":
    unittest.main()
