---
id: research-2026-08-25-preparation-copy
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/index.html
  - docs/index.de.html
  - knowledge/specification.md
---

# Copy correction: describe Preparation by participant purpose

## Research Director evaluation

The landing-page Preparation copy currently lists browser access, local tools and an AI harness too early. At this point the interface must explain why the tutorial exists: it prepares participants to take part in a workshop. The detailed path remains inside the guide itself.

## Required bilingual copy

Replace the German hero sentence with:

> Im [Vorbereitungstutorial] erfährst du, wie du alles für die Teilnahme an einem Workshop einrichtest.

Replace the English hero sentence with:

> The [preparation tutorial] shows you how to set up everything you need to take part in a workshop.

Keep the existing language-matched link targets on the bracketed phrases.

For consistency, remove the tool inventory from the compact Preparation section near the end of each landing page as well. Use:

German:

> Der Vorbereitungsleitfaden führt dich Schritt für Schritt durch alles, was du für die Teilnahme an einem Workshop vorbereiten musst. Jeder Schritt endet mit einer überprüfbaren Kontrolle.

English:

> The preparation guide takes you step by step through everything you need to prepare for a workshop. Each step ends with a check you can verify.

Preserve the existing guide links and section structure.

## Verification criteria

1. Both landing-page hero paragraphs describe the participant purpose and contain no browser, local-tool or AI-harness inventory.
2. Both compact Preparation sections use the purpose-oriented copy above.
3. All four links still resolve to the language-matched Preparation page.
4. `html-validate` and `git diff --check` pass after integration.

This evaluation is already resolved by the supplied wording and does not remain as an open Research Director Log entry.
