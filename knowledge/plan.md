---
title: Plan
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Plan
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/plan
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-plan
status: active
created: 2026-08-20
updated: 2026-11-18
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [project.md, specification.md, journal.md]
---

# Plan

This plan carries accepted future work and its entry and exit conditions. The Research Director Log supplies every human contribution by stable `RD-###` identifier; completed provenance remains in `journal.md` and Git.

## Current milestone

Close the six delivered workshop instances and obtain the author's visual acceptance of the published pages (RD-017). The single page of 4 November 2026 and the glossary pages of 5 November are published. On 2026-11-10 both landing pages, both glossary pages, the stylesheet and the script on the live site were byte-identical with `docs/` at `c8d4a66`, and the removed covers, downloads and registers answered with 404. The current public contract lives in `specification.md`. On 2026-11-18 the same six files were identical with `docs/` at `ee2bbce`.

## Active sequence

- RD-016: the author sets the six tags of the taught states. One commit then removes the five earlier folders and their register entries and rewrites the source references that point into them. The Uni for Life folder follows once the author's report stands in its delivery notes. Its three local workflows live in `local-workflows/` since 2026-11-12, and the decks link them there once the session working on the decks has changed the links.
- Continue the separate terminology and teaching-content review of the Full Slide Deck and Full Lecture Notes. It includes the document-type and checking vocabulary, where `terms.md` and the UFL deck keep Declarative, Process and Action Documents and the UFL lecture notes follow the Promptotyping paper 1.0, and the UFL source anchors in `terms.md`, many of which still name section titles and hands-on numbers from before the lecture notes were realigned on 2026-11-05.
- Fill the `*Blog.*` fields of `terms.md` once the planned glossary blog post exists, then rebuild the glossary pages.
- Maintain workshop source material for actual teaching assignments without recreating individual event pages or Learning Routes.
- Obtain the author's acceptance of the prepared Verification, Validation and Acceptance section linked from INDEX.md (RD-025), which follows the terminology decision of 2026-11-05 since its reconciliation on 2026-11-10. After acceptance, integrate the wording into section 7.7 of the German notes with the caption of figure 12, into the English notes and the slide text, and prepare the corresponding native slides. Other sections continue through their own source checks and acceptance.
- Transfer the section on always-on and proactive agents, added to the slide text and both lecture notes on 2026-11-10, into the Google versions of the deck and the notes once the author has read it.
- Bring `slides/full-slide-deck.md` in line with the Google deck. On 2026-11-12 another session changed the deck on the author's instruction, removing its speaker notes and draft markers, shortening four slides with new figures, and preparing an import of slides from the Uni for Life deck, so the export of 2026-08-20 no longer describes it. A new export follows once the import is done, and the editorial slide on always-on agents is then checked against the deck and the author's own section on Personal AI Agents.

## Completed milestones

- **v0.2:** shared interface baseline, KUG Web Module, Learning Routes and completed five-module Video Library; release commit `0e285e7`, tag `v0.2`.
- **v0.3:** Module 00, five bilingual subject hubs, Claude Code, Codex and Pi introductions and Curated Skills; release commit `aa41933`, tag `v0.3`. This topology is preserved historically and superseded in the active tree by the Research Director decision of 2026-08-26.

## Maintenance contract

- Update register data and affected public pages in the same work step.
- Recheck product commands and claims against their primary sources before publication.
- Preserve each taught state with its registered git tag before removing it from the public upcoming-instance tree.
- Record substantive transitions in `journal.md`; keep technical evidence in the Operations result and Git.
