---
title: Plan
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: active
created: 2026-08-20
updated: 2026-08-25
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, specification.md]
---

# Plan

The build runs as work packages under the Research Mission Control role model. The Research Orchestrator frames a package and issues a bounded implementation brief, the Operational Orchestrator coordinates implementation, terminal verification and integration, and Opus subagent lanes execute inside the write boundary of their brief. A package counts as done only after verification against the real file state. Current briefs, results and recipient state travel through the Context Stream in `communication/`, and every contribution required from the Research Director lives in `communication/research/director-log.md`. On conflicts the CLARIAH date (2026-09-25) wins. The content work list against the vault knowledge base (alignment of the Full Lecture Notes, atom gaps) is held by the vault document *Verknüpfungsanalyse CLARIAH-AT-Skriptum und Vault-Wissensbestand*; this plan holds the repo side.

## Done (2026-08-20)

Repo founded; all repository files English; design iteration 4 approved as the founding visual baseline, with page chrome and favicon set committed; platform built out from `docs/index.html` with one subpage per registered instance and a shared preparation page, and a cover file present for every instance; content intake complete, the Full Lecture Notes in both languages in `script/`, the Full Slide Deck export in `slides/`, the CLARIAH lecture notes and profile in `workshops/2026-09-25-clariah-at/`; draft module cut with coverage report in `script/modules/` and `script/COVERAGE.md`; `terms.md` filled from the material; downloads triage reports in `drafts/`; specification rewritten with all decisions; id scheme unified across register, folders, covers and tags; register cut to the upcoming instances and the Full naming adopted.

## Work packages

| WP | Content | Depends on | State |
| --- | --- | --- | --- |
| 1 | Content intake from the operator's downloads per the triage verdicts; CLARIAH PPTX stays outside until the taught state | triage | done 2026-08-20 |
| 2 | Module cut: consolidate the two Full Lecture Notes into the five modules (units per `drafts/module-map.md`), verbatim, with gaps recorded | Research Director, RD-001 | draft cut and coverage report delivered 2026-08-20; the notes stay authoritative until the Research Director confirms |
| 3 | CLARIAH workshop package: profile, lecture notes, hands-on links | WP1 | done except PPTX and delivery notes, which follow the taught state |
| 4 | Workshop instances: one folder per upcoming instance in the shape `profile.md`, `slide-deck.md`, `lecture-notes.md`, `data/`, each entry matching its register record | register | every registered instance has its folder; the KUG profile, English Lecture Notes, verified English 63-slide recycled deck record and data-package documentation were reconciled on 2026-08-24 |
| 5 | Platform: paired English and German landing, preparation, focused tutorial and workshop pages | WP3, WP4 | iteration 16 remains the baseline; the separate v0.2 additions are installed, formally validated and browser-observed at seven widths; RD-017 acceptance remains outstanding; the current public tree remains twenty-two pages and eleven language pairs on stylesheet version `20260825-18` |
| 6 | Terms: canonical English wording, German equivalents and literature anchors in `terms.md` | Research Director, RD-002 | filled 2026-08-20; the editorial decisions stay reversible until the Research Director confirms them |
| 7 | Vault re-pointing: the corresponding vault documents become references to this repo; Project Overview updated | WP2 | done 2026-08-22; ACTIVE-WORK entry, Project Overview and the workshop documents in the vault point to this repo and use its names |
| 8 | Publication: LICENSE file, GitHub Pages activation and live verification | WP5; Research Director gates | complete 2026-08-24; Pages publishes `main/docs`, and both landing-page languages plus both KUG page languages returned HTTP 200 for commit `c88d093` |
| 9 | Web-native slide pilot: test a browser-first teaching deck against the current CLARIAH material while retaining Google Slides as an optional export surface | WP3, WP5; CLARIAH source audit | source and interaction audit complete 2026-08-25; a ten-slide English pilot sequence and static HTML/print-CSS architecture are defined, while implementation remains separate from iteration 16 pending the accepted slide cut and rights-safe assets |
| 10 | Codex Bootcamp evidence intake: locate an official transcript, captions or companion material and derive a source-grounded introduction | official OpenAI sources | complete 2026-08-25; `knowledge/drafts/codex-bootcamp-101-evidence.md` separates the absent maintained transcript, auto-generated captions, official event objectives, public slide deck and a source-grounded deep-dive structure |
| 11 | About page: explain the relationship between commissioned workshops, maintained knowledge work and open teaching material in both interface languages | WP5 | complete 2026-08-25; both About pages are installed, reachable from every header and footer and paired through the language control |
| 12 | Research Mission Control installation: role model, Context Stream and Research Director Log documented in the canonical knowledge base | none | complete 2026-08-25; `communication/` carries the active thread and the Director Log, while `knowledge/` stays the canonical project memory |
| 13 | Site identity in the header: separate the publisher logo from the teaching-site name, give each its own destination and accessible name, and keep the full title readable to 320 pixels | WP5 | installed on all twenty-two pages, formally validated and browser-observed at seven widths on 2026-08-25; RD-017 acceptance remains open |
| 14 | KUG Web Module pilot: the five-unit browser-native learning sequence on both KUG pages, the reusable component and the register field `web_module` | WP4, WP5 | installed with seven explicit register states and the paired five-unit KUG sequence; formally validated and browser-observed at seven widths on 2026-08-25; RD-018 acceptance remains open, so reuse is not released |
| 15 | Licence copy on public cards reduced to the linked identifier, with the exact scope retained in register, governance and About | WP5 | installed on both landing pages, formally validated and browser-observed on 2026-08-25; RD-017 acceptance remains open |
| 16 | Deep Dives route on the landing pages and the documented boundary to the two adjacent DHCraft teaching sources | WP5, WP14 | the bilingual three-entry route is installed, formally validated and browser-observed; AI Coding Literacy is external, Claude Code is local and Research Data and Knowledge Work is in preparation. The static Prompt Engineering migration remains unimplemented; RD-018/RD-020 acceptance remains open |
| 17 | Copy and density refinement: compact Video Playlist copy, aligned module rows, workshop overview and reference hierarchy, compact labelled footer and the public Research Mission Control URL | WP5, WP13–WP15 | installed, formally validated and browser-observed at seven widths on 2026-08-25; workshop order is Abstract, Learning objectives or Lernziele, Outline or Ablauf; RD-017 acceptance remains open |
| 18 | Module 05 playlist synchronisation: seven accepted videos in the Research Director's maintained introductory-to-specialised order | WP5 | installed in register and both landing-page languages; formally validated and browser-observed at desktop, 640, 390 and 320 pixels on 2026-08-25 |

## Research support lanes and the integration gate

Three Research support lanes run beside the work packages under the authorisation of 2026-08-25 and are read-only by construction. The contract audit reconciles every Research brief against `CLAUDE.md`, `design.md`, `specification.md` and the public tree and classifies each finding as a release blocker, a required correction or a verified contract. The browser acceptance pass observes representative English and German pages at desktop, 640, 390 and 320 pixels and keeps observed behaviour separate from code inference. The VetMedAI source intake writes only to `drafts/vetmed-teaching-material-intake.md` and authorises no public teaching material. A lane forwards only a finding that changes an implementation or release decision. The independent Research browser-support notice is present in the Context Stream and reports no overflow or console errors across the seven required widths. A final Operations contract audit found no further implementation blocker after the two reported state deltas were resolved.

Research directed Operations to finish the independent v0.2 gate after the browser-support return. Terminal verification remains the immediate release condition. Commit, push and deployment remain with the Operational Orchestrator under the accepted release brief, and each state receives separate evidence.

## Steady-state duties after the build

Register and pages stay in sync in the same work step (specification acceptance criterion). Each taught workshop gets its git tag, PPTX export, cover and delivery notes; once it is taught and tagged, its folder leaves the working tree and the register drops the entry, so the public platform shows what people can still attend. Preparation commands and harness links are rechecked against their official sources before publication. Decisions land in `journal.md` the day they are made.

## Research Director contributions

`communication/research/director-log.md` is the register of every contribution still required from the Research Director. The work packages depend on it as follows.

| Work | Required contribution |
| --- | --- |
| Module cut (WP2) | RD-001 |
| Terms (WP6) | RD-002 |
| Workshop instances (WP4) | RD-003, RD-008, RD-009, RD-013 |
| Platform (WP5) | RD-004, RD-010, RD-011, RD-012, RD-014 |
| Full Slide Deck subchapter | RD-005, RD-006 |
| Cover series | RD-007 |
| Web-native slide pilot (WP9) | RD-015 |
| Taught workshop states | RD-016 |
| v0.2 interface release (WP5, WP13, WP15, WP17) | RD-017 |
| KUG Web Module pilot (WP14) | RD-018 |
| Adjacent teaching paths (WP16) | RD-020 |

GitHub Pages activation and the first live verification were completed on 2026-08-24. The bounded CLARIAH web-slide pilot leaves the current published material contract in force until its source cut, browser presentation and export behaviour have been accepted.
