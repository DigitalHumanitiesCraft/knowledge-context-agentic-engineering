"""Checks for the deterministic stage 1 of redact_mail.py, without Ollama.

The real test mail is the main fixture. The inline lines cover formats the test mail lacks
(Austrian phone numbers and addresses) and the false positives the phone pattern must avoid
(dates, year ranges); they are synthetic because no such mail exists in data/.

Run: python -m unittest test_redact_mail.py
"""

import unittest

import redact_mail as rm


class Stage1(unittest.TestCase):
    def test_real_mail(self) -> None:
        text, sender, _ = rm.stage1_mail(
            (rm.DATA / "kundenanfrage.txt").read_text(encoding="utf-8")
        )
        self.assertEqual(sender, "Andrew Fuller")
        for s in ("@", "555-9482", "3457", "Capital Way", "Tacoma", "Steven Buchanan"):
            self.assertNotIn(s, text)
        for s in ("Andrew Fuller", "1996 bis 1998", "9. November 2026, 08:12"):
            self.assertIn(s, text)

    def test_formats(self) -> None:
        text, _, _ = rm.stage1_mail(
            "Tel. +43 316 380-1234 oder 0316/380-1234, ext. 42\nUniversitätsplatz 3, 8010 Graz\nA-8010 Graz\n"
        )
        self.assertEqual(
            text,
            "Tel. [TELEFON] oder [TELEFON], ext. [TELEFON]\n[ADRESSE]\n[ADRESSE]\n",
        )

    def test_no_false_phone(self) -> None:
        line = (
            "Am 08.11.2026 um 10:30, Jahre 1996-1998 und 1996 1997 1998, Auftrag 10248."
        )
        self.assertEqual(rm.stage1_mail(line)[0], line)


class OwnData(unittest.TestCase):
    """The trust boundary for a person's own mail, checked without Ollama."""

    def test_console_shows_counts_only(self) -> None:
        res = rm.RunResult("qwen3.5:9b", 1, "[NAME] kommt.")
        res.checks = {
            "durchgelassen": ["Steven Buchanan", "E-Mail-Muster: a.b@example.org"],
            "verloren": ["Auftrag 10248"],
        }
        line = rm._summary_line(res)
        for s in ("Steven Buchanan", "a.b@example.org", "Auftrag 10248"):
            self.assertNotIn(s, line)
        self.assertIn("durchgelassen 2, verloren 1", line)

    def test_own_mail_gets_no_test_fixtures(self) -> None:
        own = rm.HERE / "eigene.txt"
        self.assertEqual(rm._inputs(own, None, None), (own, None, None))
        mail, xlsx, checklist = rm._inputs(None, None, None)
        self.assertEqual(mail.name, "kundenanfrage.txt")
        self.assertEqual(xlsx.name, "mitarbeitende.xlsx")
        self.assertEqual(checklist.name, "pruefliste.json")

    def test_test_variant_keeps_staff_list(self) -> None:
        variant = rm.HERE / "testmails" / "kundenanfrage_variante.txt"
        self.assertEqual(
            rm._inputs(variant, None, None),
            (variant, rm.DATA / "mitarbeitende.xlsx", None),
        )
        own_xlsx = rm.HERE / "eigene.xlsx"
        self.assertEqual(rm._inputs(variant, own_xlsx, None)[1], own_xlsx)

    def test_check_without_workbook(self) -> None:
        original = (rm.DATA / "kundenanfrage.txt").read_text(encoding="utf-8")
        after1, sender, _ = rm.stage1_mail(original)
        checks = rm.stage3_check(original, after1, after1, {}, None, None, sender)
        self.assertEqual(checks["verboten"], {})
        self.assertNotIn("Namen aus der Mitarbeiterliste", checks["allgemein"])
        self.assertEqual(checks["allgemein"]["E-Mail-Muster"], [])


if __name__ == "__main__":
    unittest.main()
