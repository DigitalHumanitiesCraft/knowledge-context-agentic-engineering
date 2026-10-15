---
title: Project
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Projekt-Wissensdokument
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/project
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-project
status: draft
created: 2026-08-20
updated: 2026-10-15
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
knowledge-sources:
  methods:
    Promptotyping: https://dhcraft.org/Promptotyping/
    Research Mission Control: https://github.com/DigitalHumanitiesCraft/research-mission-control
  repositories:
    CLARIAH hands-on package: https://github.com/chpollin/zbz-ocr-tei
    DHCraft brand assets: https://github.com/DigitalHumanitiesCraft/brand-assets
related: [specification.md, governance.md, plan.md]
---

# Project

This repo is the canonical home of the material for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*, and it carries the platform that presents the shared material. Workshop derivations remain maintained source material for their teaching context. The project covers the teaching material itself, the Full Lecture Notes, the Full Slide Deck, the workshop profiles and the platform. The research strand around the material (how new knowledge integrates into an existing knowledge structure) lives in the author's research vault.

## Development method and orchestration

Two complementary methods carry the work. Promptotyping is the artefact-development method; the maintained documents in this folder guide iterative production, inspection and correction of teaching material, interface code and workshop packages. Research Mission Control is the orchestration contract; the Research Director holds substantive authority, the Research Orchestrator frames research and issues bounded implementation briefs, and the Operational Orchestrator coordinates authorised implementation, verification, integration and release. Bounded subagent lanes work under those orchestrators and inherit only the authority and write boundary stated for their lane. The Context Stream in `communication/` transports the current briefs, results and recipient state, while durable project knowledge stays here. Role detail lives in `governance.md`, the transport contract in `communication/PROTOCOL.md`.

The concepts, source selection and editorial decisions originate with Christopher Pollin. Almost all prose, interface copy, diagrams and implementation artefacts are drafted with AI harnesses and revised through Promptotyping and Research Mission Control. `README.md` carries the public authorship statement, `journal.md` condenses the substantive transitions, and Git preserves the complete revision history.

## Material and derivation by profile

The material is maintained through three holdings, the Full Slide Deck, the Full Lecture Notes and the Video Playlist, and covers the whole subject for a general audience of people who do computer-based, data-driven knowledge work. Each holding is described by its intended use rather than by a count of modules. The Full Slide Deck is the complete overview of the teaching material in slide form; it serves as a reference work and as the source from which workshop-specific decks are assembled, and it is not presented as one teaching session. The Full Lecture Notes are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The Video Playlist combines DHCraft videos with selected contributions by others; its deliberate sequence runs from the foundations to more complex topics and forms a structured learning path, and it is curated, maintained and extended as suitable material appears.

The slide deck and the lecture notes deliberately express the same maintained concepts at different levels of expansion, so the text does not live in one single place. Responsibility is divided by layer. The Full Slide Deck maintains the reference structure and the selection surface from which workshop decks are assembled. The Full Lecture Notes maintain the expanded explanation. A conceptual change that touches both is reconciled across the two before any specialised export is regenerated. All three holdings share the same five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance. The playlist assigns every entry one primary module and may record further related modules without duplicating the entry. Its current sequence and distribution live in `docs/data/videos.json`. The fine cut remains provisional in `drafts/module-map.md` and `script/modules/` until Research Director acceptance.

A workshop is a documented specialization of the material. Its profile selects modules, sets depth, case studies and language, and adds only what belongs to that single instance, such as schedule, hands-on instructions and venue specifics. Published workshop artefacts may repeat selected explanatory slides so that each event remains usable on its own. Their shared source remains the Full Slide Deck, and a change to common material is reconciled there before the specialised exports are regenerated. Case studies are exchangeable modules of their own (currently Hersch and Zweig for research data and digital editions), so the core of the material stays domain-neutral.

Workshop profiles and their material remain research and teaching sources in `workshops/`. The public site presents the shared holdings and Preparation without individual event pages.

## Public learning architecture

The public site is one static page per language, `index.html` and `index.de.html`. A compact paragraph in the opening section explains DHCraft, workshop funding and public maintenance. The page then presents the shared teaching materials, the embedded Preparation deck and the Video Library. Header links target these sections. There are no separate About or Preparation pages and no generic arrow-back links. The canonical legal notice remains linked in the footer, together with the licence scope. Event listings and Learning Routes remain retired; teaching sources are unchanged.

Preparation links to and embeds the existing English Google Slides deck [Preparation · Slides · Technical Setup](https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit). Its URL and language are registered in `docs/data/workshops.json` under `preparation`. Both language versions identify the English teaching language. A visible direct link remains usable if the embedded viewer cannot load. No separate HTML setup curriculum or subject-introduction sequence is maintained in that section.

The workshop records in `docs/data/workshops.json` retain material provenance and do not generate public event pages or navigation. Full-material and video links retain their existing ownership and rights boundaries. External Google files and sharing permissions are unchanged.

## Languages

The teaching material retains its source language and translations require author review. The single page has paired English and German interfaces. Both Preparation sections point to the same English Technical Setup deck; interface language does not imply a translated deck.

## Holdings map

| Holding | Location |
| --- | --- |
| Full Lecture Notes, German | `script/full-lecture-notes-de.md` |
| Full Lecture Notes, English | `script/full-lecture-notes-en.md` |
| Module cut of the lecture notes, with its coverage report | `script/modules/`, `script/COVERAGE.md` |
| Full Slide Deck, text export with speaker notes | `slides/full-slide-deck.md` |
| Video Playlist | `https://www.youtube.com/playlist?list=PLXY4kw40KBaY` |
| Video inventory, playlist order, primary module, related modules and duration | `docs/data/videos.json` |
| Workshop instance, one folder per instance | `workshops/<id>/` with `profile.md`, `slide-deck.md`, `lecture-notes.md`, `data/` |
| Preparation, existing Google Slides deck | `docs/index.html#preparation`, `docs/index.de.html#preparation` |
| Curated Skills source pending public placement | `knowledge/drafts/curated-agent-skills-library.md` |
| Slide exports (PPTX per taught state) | `workshops/<id>/` |
| Cover images (PNG, 16:9) | `docs/assets/covers/<id>.png` |
| Workshop register, material release state and module subset | `docs/data/workshops.json` |
| Live decks and documents | Google Workspace, linked from the register |
| Executable CLARIAH hands-on package | external repo `chpollin/zbz-ocr-tei`, `workshops/clariah-at-2026/` |
| Project coordination and thematic knowledge base | the author's research vault (private) |

Only upcoming instances live in the working tree. A delivered instance is removed after its teaching state has been tagged, and it stays retrievable in git history; the register in `docs/data/workshops.json` is the source of truth for which instances are current (operator decision 2026-08-20).

## Adjacent teaching sources

Two neighbouring DHCraft teaching projects overlap with this line and remain separate sources. Their material can reach the platform through a documented migration, while their ownership, rights and runtime stay where they are (Research Director decision 2026-08-25).

`DigitalHumanitiesCraft/ai-coding-literacy` is an independent published German-language curriculum for researchers without prior programming experience, organised around seven competencies for AI-supported coding. It keeps its own repository contract, its own deployment and its own dataset rights boundary. The independent curriculum remains available at `https://digitalhumanitiescraft.github.io/ai-coding-literacy/de/`. Its competency model may be mapped onto the teaching line, and a reusable definition enters the Full Slide Deck or the Full Lecture Notes only after reconciliation with `terms.md`. Its KCE relation remains a source relation; it does not become a numbered KCE module.

The local folder `DHCraft/ai-literacies` is an unversioned Astro prototype without its own repository, action layer or maintained knowledge directory, so it carries no publication status. It stays read-only input for the migration into Web Modules, and its content and design patterns are re-authored in this design system. Astro, npm dependencies, TypeScript, `node_modules`, its source CSS tokens, its build configuration and its root-relative route system stay outside this repo, because the platform holds its no-build static publication contract. Its `IntersectionObserver` reading pattern may at most inform a progressive enhancement, and the complete learning text stays readable without JavaScript.

The migration is ordered. The Prompt Engineering unit is the first candidate and remains in preparation because no static KCE lesson exists. Research Data and Knowledge Work is reconciled into the maintained slides instead of receiving a public route. RD-018, RD-020, RD-021 and RD-023 acceptance remain outstanding. The Tools, Multimodal, Administration Data Analysis and Research Data Analysis units additionally wait for the verified VetMedAI intake, because their product facts, model claims, data-protection statements and rights boundaries need re-verification. A migrated unit carries its module mapping, audience, source reference, verification date and editorial status, and no dataset, screenshot, external slide image or video thumbnail is copied.

## Audiences

The audience of the material is general, computer-based and data-driven knowledge work; specialization happens per workshop profile. Each profile names its audience and prerequisites explicitly, and the register holds the current set of instances with their audience and language fields. The registered range runs from summer-school participants without LLM or programming background, through digital humanities students and staff of academy and editions projects, to professionals from companies and institutions outside academia.
