---
title: Project Charter
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Projekt-Wissensdokument
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/project
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-project
status: draft
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
knowledge-sources:
  - https://dhcraft.org/Promptotyping/
  - https://github.com/chpollin/zbz-ocr-tei
  - https://github.com/DigitalHumanitiesCraft/brand-assets
related: [specification.md, governance.md, plan.md]
---

# Project Charter

This repo is the canonical home of the master corpus for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*, and it carries the platform that presents the corpus and its workshop derivations. The project covers the teaching material itself, the master script, the master slide texts, the workshop profiles and the platform. The research strand around the corpus (how new knowledge integrates into an existing knowledge structure) lives in the author's research vault.

## Master and recipe model

The master holds the complete material for a general audience, people who do computer-based, data-driven knowledge work. The text lives exactly once, cut into modules; the module cut is proposed in `drafts/module-map.md` and confirmed by the operator.

A workshop profile is a recipe over the master. It selects modules, sets depth, case studies and language, and adds only what belongs to that single workshop, such as schedule, hands-on instructions and venue specifics. An improvement to a master module therefore reaches every workshop that uses the module. Case studies are exchangeable modules of their own (currently Hersch and Zweig for research data and digital editions), so the master core stays domain-neutral.

## Languages

Each module carries the source language it was authored in; the other language version is produced by agent translation and counts as canonical only after operator review (operator decision 2026-08-20). The platform interface is English; the script content is shown bilingually with an EN/DE toggle where both versions exist.

## Holdings map

| Holding | Location |
| --- | --- |
| Master script in modules (DE source, reviewed EN) | `script/` |
| Master slide texts with speaker notes | `slides/` |
| Workshop profiles and materials | `workshops/<id>/` |
| CLARIAH-AT workshop script (EN, profile material) | `workshops/2026-09-25-clariah-at/` |
| Slide exports (PPTX per taught state) | `workshops/<id>/` |
| Title-slide images (PNG, 16:9) | `docs/assets/covers/` |
| Workshop register | `docs/data/workshops.json` |
| Live decks | Google Slides, linked from the register |
| Executable CLARIAH hands-on package | external repo `chpollin/zbz-ocr-tei`, `workshops/clariah-at-2026/` |
| Project coordination and thematic knowledge base | the author's research vault (private) |

## Audiences

The master audience is general, computer-based and data-driven knowledge work; specialisation happens per workshop profile. Four profiles are registered: KUG/M3GIM (compact, no LLM or programming prerequisites), CLARIAH-AT Summer School (research data workflows and digital editions, DH students), Uni for Life (extended two-day variant, professionals from companies and other disciplines), VetMed Winter School (five-day extended derivation of the full master, administration and research staff). Each profile names its audience and prerequisites explicitly.
