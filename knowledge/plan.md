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
updated: 2026-11-05
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [project.md, specification.md, journal.md]
---

# Plan

This plan carries accepted future work and its entry and exit conditions. The Research Director Log supplies every human contribution by stable `RD-###` identifier; completed provenance remains in `journal.md` and Git.

## Current milestone

Publish the redesigned single page of 4 November 2026 together with the generated glossary pages of 5 November and check the live state. The current public contract lives in `specification.md`, an introduction, four material cards, the glossary card and the modules with their videos on each landing page, and two glossary pages, with no external resource. The local commits are not pushed, and on 2026-11-05 the live site still served the stylesheet version `20261015-1` and answered the German glossary URL with 404. Publication and the visual acceptance RD-017 remain author decisions.

## Active sequence

- After the author's push, check the live pages for the stylesheet and script version `20261105-2`, the absence of external requests, both glossary pages, the glossary link on the materials slide of the UFL deck, and 404 responses for the removed covers, downloads and title-slide image.
- Teach the Uni for Life instance on 9 and 10 November 2026, then fill the delivery notes in its profile, have the author set the tag `2026-11-09-ufl` (RD-016) and only then remove the folder and its register entry.
- Continue the separate terminology and teaching-content review of the Full Slide Deck and Full Lecture Notes. It includes the document-type and checking vocabulary, where `terms.md` and the UFL deck keep Declarative, Process and Action Documents and the UFL lecture notes follow the Promptotyping paper 1.0, and the UFL source anchors in `terms.md`, many of which still name section titles and hands-on numbers from before the lecture notes were realigned on 2026-11-05.
- Fill the `*Blog.*` fields of `terms.md` once the planned glossary blog post exists, then rebuild the glossary pages.
- Maintain workshop source material for actual teaching assignments without recreating individual event pages or Learning Routes.
- Obtain bounded author feedback on the prepared Verification, Validation and Acceptance section linked from INDEX.md (RD-025). After acceptance, integrate the identified wording into the German notes and prepare the corresponding native slides. Other sections continue through their own source checks and acceptance.
- RD-024: the Full Slidedeck still gives anyone with the link edit access (checked 2026-11-05); the author lowers it to reader access.

## Completed milestones

- **v0.2:** shared interface baseline, KUG Web Module, Learning Routes and completed five-module Video Library; release commit `0e285e7`, tag `v0.2`.
- **v0.3:** Module 00, five bilingual subject hubs, Claude Code, Codex and Pi introductions and Curated Skills; release commit `aa41933`, tag `v0.3`. This topology is preserved historically and superseded in the active tree by the Research Director decision of 2026-08-26.

## Maintenance contract

- Update register data and affected public pages in the same work step.
- Recheck product commands and claims against their primary sources before publication.
- Preserve each taught state with its registered git tag before removing it from the public upcoming-instance tree.
- Record substantive transitions in `journal.md`; keep technical evidence in the Operations result and Git.
