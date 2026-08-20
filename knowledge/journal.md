---
title: Journal
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: active
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
---

# Journal

Chronicle of decisions, milestones and workshop deliveries, newest first. Public document; the privacy rule in `governance.md` applies.

## 2026-08-20 — Top-level module structure set

The operator set the top-level structure of the master: five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, and a fifth module for the critical, societal and governance level (English wording proposed as Critical Perspectives and Governance, confirmation open). The finer cut proposed in `drafts/module-map.md` continues as units beneath these five; the assignment of Promptotyping, verification and the hands-on case studies to Agentic Engineering is a working proposal until confirmed.

## 2026-08-20 — Design decisions on the first prototypes

The operator reviewed the start-page prototype: direction approved, Space Grotesk chosen as the platform typeface, text hierarchy reduced to at most two levels per section, colours converged to a single turquoise accent on one consistent paper-white ground. The second prototype (`docs/drafts/design-draft-2.html`) implements this and already carries real data, the proposed module structure and the workshop register entries. The workshop-subpage example awaits the operator's reaction.

## 2026-08-20 — Specification round and language switch

The knowledge documents were walked through with the operator and the open questions answered. Decisions:

- All repository files are English, including file and folder names (`begriffe.md` became `terms.md`, the planned `skriptum/` became `script/`). The script content is bilingual, German source and reviewed English translation, with an EN/DE toggle on the platform; the platform interface stays English. The founding documents were rewritten in English the same day (originals in git history); `design.md`, `specification.md` and `terms.md` follow once the commissioned drafts are in.
- The master title stands alone; there is no subtitle.
- Recipe model: the master text lives once, cut into modules; a workshop profile selects modules and adds only workshop-specific content.
- The German master script is the module source. The English CLARIAH lecture notes become material of the CLARIAH profile. English master versions arise through agent translation with operator review.
- The master audience is generalised to computer-based, data-driven knowledge work; specialisation happens per profile.
- Each workshop gets its own platform subpage that serves as the live course resource and as follow-up material. Page structure and visual motif will be decided on prototypes; drafts were commissioned.
- Textual content is licensed CC BY 4.0; slide decks are checked separately for third-party image rights.
- Single-author repo; co-teachers contribute material through the operator.
- Master migration and CLARIAH profile are built in parallel; on conflicts the CLARIAH date (2026-09-25) wins.
- The state actually taught in a workshop is marked with a git tag set by the operator.
- Preparation drafts were commissioned from agents: module map, slides-to-chapter map, term literature anchors, and design prototypes (start page and example workshop subpage). The module-map proposal arrived the same day (`drafts/module-map.md`).

## 2026-08-20 — Repository founding

The repo was created as a public repository under DigitalHumanitiesCraft, with the knowledge folder, the workshop register and the root documents. It was preceded by a linking analysis in the author's vault that mapped the CLARIAH lecture notes against the existing knowledge base; its findings (term coverage register, deficit zones, execution plan) ground `terms.md` and `plan.md`.

Operator decisions of that day:

- Main title *Knowledge, Context and Agentic Engineering for Knowledge Work*; research data and editions are one specialisation (CLARIAH profile), alongside the compact KUG variant and the extended Uni for Life variant.
- The repo is the canonical home of the master texts; the vault versions become references, Google artefacts remain derived surfaces.
- Repo public, platform via GitHub Pages, platform language English.
- Teaching runs on Google Slides; PPTX exports per taught state and title-slide PNGs are kept in the repo.
