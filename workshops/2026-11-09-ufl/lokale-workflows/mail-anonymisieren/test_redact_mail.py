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


if __name__ == "__main__":
    unittest.main()
