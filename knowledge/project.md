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

This repo is the canonical home of the corpus for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*, and it carries the platform that presents the corpus and its workshop derivations. The project covers the teaching material itself, the Full Lecture Notes, the Full Slide Deck, the workshop profiles and the platform. The research strand around the corpus (how new knowledge integrates into an existing knowledge structure) lives in the author's research vault.

## Corpus and recipe model

The corpus is maintained once, as the Full Slide Deck and the Full Lecture Notes, and holds the complete material for a general audience of people who do computer-based, data-driven knowledge work. The text lives exactly once, cut into five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance. The cut is drafted in `drafts/module-map.md` and in `script/modules/`, and it becomes canonical on operator confirmation.

A workshop is a documented specialization of the corpus. Its profile selects modules, sets depth, case studies and language, and adds only what belongs to that single instance, such as schedule, hands-on instructions and venue specifics. An improvement to a module therefore reaches every workshop that uses the module. Case studies are exchangeable modules of their own (currently Hersch and Zweig for research data and digital editions), so the corpus core stays domain-neutral.

The canonical names of the two holdings are Full Slide Deck and Full Lecture Notes; the earlier working name they carried is retired and is not used anywhere in the repo (operator decision 2026-08-20, rule text in `CLAUDE.md`).

## Languages

Each module carries the source language it was authored in; the other language version is produced by agent translation and counts as canonical only after operator review (operator decision 2026-08-20). The platform interface is English. Language is handled per module and per instance, so a page shows the language its material was taught in and the register field `language` carries the instance language (operator decision 2026-08-20, replacing the earlier requirement of a bilingual page toggle).

## Holdings map

| Holding | Location |
| --- | --- |
| Full Lecture Notes, German | `script/full-lecture-notes-de.md` |
| Full Lecture Notes, English | `script/full-lecture-notes-en.md` |
| Module cut of the lecture notes, with its coverage report | `script/modules/`, `script/COVERAGE.md` |
| Full Slide Deck, text export with speaker notes | `slides/full-slide-deck.md` |
| Workshop instance, one folder per instance | `workshops/<id>/` with `profile.md`, `slide-deck.md`, `lecture-notes.md`, `data/` |
| Slide exports (PPTX per taught state) | `workshops/<id>/` |
| Cover images (PNG, 16:9) | `docs/assets/covers/<id>.png` |
| Workshop register | `docs/data/workshops.json` |
| Live decks and documents | Google Workspace, linked from the register |
| Executable CLARIAH hands-on package | external repo `chpollin/zbz-ocr-tei`, `workshops/clariah-at-2026/` |
| Project coordination and thematic knowledge base | the author's research vault (private) |

Only upcoming instances live in the working tree. A delivered instance is removed after its teaching state has been tagged, and it stays retrievable in git history; the register in `docs/data/workshops.json` is the source of truth for which instances are current (operator decision 2026-08-20).

## Audiences

The corpus audience is general, computer-based and data-driven knowledge work; specialization happens per workshop profile. Each profile names its audience and prerequisites explicitly, and the register holds the current set of instances with their audience and language fields. The registered range runs from summer-school participants without LLM or programming background, through digital humanities students and staff of academy and editions projects, to professionals from companies and institutions outside academia.
