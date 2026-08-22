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
updated: 2026-08-22
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, specification.md]
---

# Plan

The build runs as work packages, each delegated to Opus subagents and coordinated by the orchestrator; a package counts as done only after verification against the real file state. On conflicts the CLARIAH date (2026-09-25) wins. The content work list against the vault knowledge base (alignment of the Full Lecture Notes, atom gaps) is held by the vault document *Verknüpfungsanalyse CLARIAH-AT-Skriptum und Vault-Wissensbestand*; this plan holds the repo side.

## Done (2026-08-20)

Repo founded; all repository files English; design iteration 4 approved and in force, with page chrome and favicon set committed; platform built out from `docs/index.html` with one subpage per registered instance and a shared preparation page, and a cover file present for every instance; content intake complete, the Full Lecture Notes in both languages in `script/`, the Full Slide Deck export in `slides/`, the CLARIAH lecture notes and profile in `workshops/2026-09-25-clariah-at/`; draft module cut with coverage report in `script/modules/` and `script/COVERAGE.md`; `terms.md` filled from the material; downloads triage reports in `drafts/`; specification rewritten with all decisions; id scheme unified across register, folders, covers and tags; register cut to the upcoming instances and the Full naming adopted.

## Work packages

| WP | Content | Depends on | State |
| --- | --- | --- | --- |
| 1 | Content intake from the operator's downloads per the triage verdicts; CLARIAH PPTX stays outside until the taught state | triage | done 2026-08-20 |
| 2 | Module cut: consolidate the two Full Lecture Notes into the five modules (units per `drafts/module-map.md`), verbatim, with gaps recorded | operator: fine-cut confirmation | draft cut and coverage report delivered 2026-08-20; the notes stay authoritative until the operator confirms |
| 3 | CLARIAH workshop package: profile, lecture notes, hands-on links | WP1 | done except PPTX and delivery notes, which follow the taught state |
| 4 | Workshop instances: one folder per upcoming instance in the shape `profile.md`, `slide-deck.md`, `lecture-notes.md`, `data/`, each entry matching its register record | register | every registered instance has its folder 2026-08-20 |
| 5 | Platform: landing page with the horizontal instance cards and module badges, one subpage per registered instance, and the preparation page | WP3, WP4 | pages built 2026-08-20 and cover fields filled; no register field yet carries the module selection of an instance |
| 6 | Terms: canonical English wording, German equivalents and literature anchors in `terms.md` | operator: confirmation of the six editorial decisions recorded in the document | filled 2026-08-20; the editorial decisions stay reversible until the operator confirms them |
| 7 | Vault re-pointing: the corresponding vault documents become references to this repo; Project Overview updated | WP2 | done 2026-08-22; ACTIVE-WORK entry, Project Overview and the workshop documents in the vault point to this repo and use its names |
| 8 | Publication: LICENSE file (CC BY 4.0 for texts, done), GitHub Pages activation, full link and rendering verification, then announcement-ready | WP5; operator gates | license done; activation and verification open |

## Steady-state duties after the build

Register and pages stay in sync in the same work step (specification acceptance criterion). Each taught workshop gets its git tag, PPTX export, cover and delivery notes; once it is taught and tagged, its folder leaves the working tree and the register drops the entry, so the public platform shows what people can still attend. Decisions land in `journal.md` the day they are made.

## Operator deliveries and open gates

The operator delivers the cover images per instance from the external image pipeline, placed as `docs/assets/covers/<id>.png`, and the final display title of the VetMed Winter School.

Three gates stay with the operator, the fine-cut confirmation at the module coverage report, the confirmation of the editorial decisions recorded in `terms.md`, and the git tag per taught workshop state. Pages activation is agreed for after the current build-out and a full verification pass (operator decision 2026-08-20).
