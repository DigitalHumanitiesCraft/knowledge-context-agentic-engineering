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
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/project
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-project
status: draft
created: 2026-08-20
updated: 2026-08-25
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
knowledge-sources:
  - https://dhcraft.org/Promptotyping/
  - https://github.com/chpollin/zbz-ocr-tei
  - https://github.com/DigitalHumanitiesCraft/brand-assets
related: [specification.md, governance.md, plan.md]
---

# Project

This repo is the canonical home of the material for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*, and it carries the platform that presents the material and its workshop derivations. The project covers the teaching material itself, the Full Lecture Notes, the Full Slide Deck, the workshop profiles and the platform. The research strand around the material (how new knowledge integrates into an existing knowledge structure) lives in the author's research vault.

## Development method and orchestration

Two complementary methods carry the work. Promptotyping is the artefact-development method; the maintained documents in this folder guide iterative production, inspection and correction of teaching material, interface code and workshop packages. Research Mission Control is the orchestration contract; the Research Director holds substantive authority, the Research Orchestrator frames research and issues bounded implementation briefs, and the Operational Orchestrator coordinates authorised implementation, verification, integration and release. Bounded subagent lanes work under those orchestrators and inherit only the authority and write boundary stated for their lane. The Context Stream in `communication/` transports the current briefs, results and recipient state, while durable project knowledge stays here. Role detail lives in `governance.md`, the transport contract in `communication/PROTOCOL.md`.

## Material and derivation by profile

The material is maintained through three holdings, the Full Slide Deck, the Full Lecture Notes and the Video Playlist, and covers the whole subject for a general audience of people who do computer-based, data-driven knowledge work. Each holding is described by its intended use rather than by a count of modules. The Full Slide Deck is the complete overview of the teaching material in slide form; it serves as a reference work and as the source from which workshop-specific decks are assembled, and it is not presented as one teaching session. The Full Lecture Notes are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The Video Playlist combines DHCraft videos with selected contributions by others; its deliberate sequence runs from the foundations to more complex topics and forms a structured learning path, and it is curated, maintained and extended as suitable material appears.

The slide deck and the lecture notes deliberately express the same maintained concepts at different levels of expansion, so the text does not live in one single place. Responsibility is divided by layer. The Full Slide Deck maintains the reference structure and the selection surface from which workshop decks are assembled. The Full Lecture Notes maintain the expanded explanation. A conceptual change that touches both is reconciled across the two before any specialised export is regenerated. All three holdings share the same five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance. The playlist assigns every entry one primary module and may record further related modules without duplicating the entry. Its current 41-entry distribution is `5/1/6/22/7`; Module 05 closes the route with seven accepted videos ordered from broad accounts of ideology, power and control towards specialised AGI debates. The cut is drafted in `drafts/module-map.md` and in `script/modules/`, and it becomes canonical on operator confirmation.

A workshop is a documented specialization of the material. Its profile selects modules, sets depth, case studies and language, and adds only what belongs to that single instance, such as schedule, hands-on instructions and venue specifics. Published workshop artefacts may repeat selected explanatory slides so that each event remains usable on its own. Their shared source remains the Full Slide Deck, and a change to common material is reconciled there before the specialised exports are regenerated. Case studies are exchangeable modules of their own (currently Hersch and Zweig for research data and digital editions), so the core of the material stays domain-neutral.

A workshop instance presents that specialization through three surfaces with distinct functions. The Web Module is the primary browser-native learning sequence and lives inside the workshop URL itself; it carries internal navigation, explanatory panels, original diagrams and observable checks, and it precedes the other two surfaces on the page. The Slide Deck remains the editable presentation surface used in delivery. The Lecture Notes remain the expanded reading form for reference and later review. Google artifacts stay linked and embedded where they have been verified. The workshop profile in `workshops/<id>/` and the corresponding vault record supply research context and editorial provenance and are never exposed as a fourth public material type. The register field `web_module` states the availability of the first surface per instance and stays separate from `materials_status`, which governs the release of material actions. The KUG pair carries the installed five-unit pilot and `available`; the remaining six entries carry `in_preparation` until their sources and sequence have been accepted (Research Director decision 2026-08-25; installation formally validated 2026-08-25).

## Public learning architecture

The platform adds a neutral prerequisite to the five subject modules. Module 00 retains the bilingual Preparation routes and combines observable setup with the external German AI Coding Literacy foundation. Modules 01 through 05 have ten stable bilingual hub files under `docs/modules/`. Each hub connects a definition and learning question with a semantic concept map, a source-grounded starter sequence, learning routes, the maintained teaching holdings, primary videos and representative workshop uses. Module 00 remains outside workshop module arrays, subject colours and video classification.

Every visible module title and compact marker routes to the language-matched hub. A separate module navigation connects 00 through 05 on Module 00 and every subject hub. Module 03 keeps Knowledge Engineering and Context Engineering in one umbrella structure by connecting maintained knowledge and current task state with selected working context. Module 04 owns the Curated Skills subsection. Its eight external examples remain labelled references whose instruction and permission review is outstanding; Module 03 links to the relevant area without duplicating the list.

The landing-page learning routes separate Foundation, AI Harness introductions and Research workflow. The local Harness routes cover Claude Code, Codex and Pi in English and German through a shared eight-step sequence, `goal`, `prerequisites`, `install`, `workspace`, `instructions`, `permissions`, `extensions` and `first-check`. The Pi route keeps harness source, provider configuration and inference location as separate facts. Research Data and Knowledge Work remains a prepared route without a public destination. Release v0.3 contains 36 HTML files in eighteen language pairs on stylesheet version `20260825-19`; formal validation, browser observation, commit, tag, push and deployment are evidenced, while RD-021, RD-022 and RD-023 remain open for substantive acceptance.

The canonical names of the three holdings are Full Slide Deck, Full Lecture Notes and Video Playlist. The earlier working name of the document holdings is retired and is not used anywhere in the repo (operator decisions 2026-08-20 and 2026-08-25, rule text in `CLAUDE.md`).

## Languages

Each module carries the source language it was authored in; the other language version is produced by agent translation and counts as canonical only after operator review (operator decision 2026-08-20). The landing page, Module 00, five subject hubs, three focused Harness tutorials, About page and every workshop instance are presented through paired English and German static pages. The active installation therefore contains eighteen pairs. Interface language is independent of teaching language, while the register field `language` continues to record the language of the course material (operator decision 2026-08-24, replacing the single-language workshop pages fixed on 2026-08-20).

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
| Workshop Web Module, the browser-native learning sequence | inside the paired workshop pages `docs/workshops/<id>.html` and `docs/workshops/<id>.de.html` |
| Module 00, Preparation and AI Coding Literacy | `docs/preparation.html`, `docs/preparation.de.html` |
| Subject-module hubs 01 through 05 | ten paired files under `docs/modules/` |
| AI Harness introductions | paired Claude Code, Codex and Pi routes under `docs/tutorials/` |
| Curated Skills area | `#curated-skills` inside the Module 04 hub pair |
| Slide exports (PPTX per taught state) | `workshops/<id>/` |
| Cover images (PNG, 16:9) | `docs/assets/covers/<id>.png` |
| Workshop register, material release state and module subset | `docs/data/workshops.json` |
| Live decks and documents | Google Workspace, linked from the register |
| Executable CLARIAH hands-on package | external repo `chpollin/zbz-ocr-tei`, `workshops/clariah-at-2026/` |
| Project coordination and thematic knowledge base | the author's research vault (private) |

Only upcoming instances live in the working tree. A delivered instance is removed after its teaching state has been tagged, and it stays retrievable in git history; the register in `docs/data/workshops.json` is the source of truth for which instances are current (operator decision 2026-08-20).

## Adjacent teaching sources

Two neighbouring DHCraft teaching projects overlap with this line and remain separate sources. Their material can reach the platform through a documented migration, while their ownership, rights and runtime stay where they are (Research Director decision 2026-08-25).

`DigitalHumanitiesCraft/ai-coding-literacy` is an independent published German-language curriculum for researchers without prior programming experience, organised around seven competencies for AI-supported coding. It keeps its own repository contract, its own deployment and its own dataset rights boundary. The installed Foundation learning route identifies it as an external German-language curriculum and links `https://digitalhumanitiescraft.github.io/ai-coding-literacy/de/`. Its competency model may be mapped onto modules 02 through 05, and a reusable definition enters the Full Slide Deck or the Full Lecture Notes only after reconciliation with `terms.md`. The curriculum contributes to Module 00 and never replaces the five subject modules.

The local folder `DHCraft/ai-literacies` is an unversioned Astro prototype without its own repository, action layer or maintained knowledge directory, so it carries no publication status. It stays read-only input for the migration into Web Modules, and its content and design patterns are re-authored in this design system. Astro, npm dependencies, TypeScript, `node_modules`, its source CSS tokens, its build configuration and its root-relative route system stay outside this repo, because the platform holds its no-build static publication contract. Its `IntersectionObserver` reading pattern may at most inform a progressive enhancement, and the complete learning text stays readable without JavaScript.

The migration is ordered. The Prompt Engineering unit is the first candidate and remains in preparation because no static KCE lesson exists; installation of the Module 02 preparation row supplies no migrated teaching content. Research Data and Knowledge Work also remains a visible preparation state. RD-018, RD-020, RD-021, RD-022 and RD-023 acceptance remain outstanding. The Tools, Multimodal, Administration Data Analysis and Research Data Analysis units additionally wait for the verified VetMedAI intake, because their product facts, model claims, data-protection statements and rights boundaries need re-verification. A migrated unit carries its module mapping, audience, source reference, verification date and editorial status, and no dataset, screenshot, external slide image or video thumbnail is copied.

## Audiences

The audience of the material is general, computer-based and data-driven knowledge work; specialization happens per workshop profile. Each profile names its audience and prerequisites explicitly, and the register holds the current set of instances with their audience and language fields. The registered range runs from summer-school participants without LLM or programming background, through digital humanities students and staff of academy and editions projects, to professionals from companies and institutions outside academia.
