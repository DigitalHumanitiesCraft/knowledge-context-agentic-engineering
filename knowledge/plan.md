---
title: Build Plan
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
related: [project.md, specification.md]
---

# Build Plan

The build runs as work packages, each delegated to Opus subagents and coordinated by the orchestrator; a package counts as done only after verification against the real file state. On conflicts the CLARIAH date (2026-09-25) wins. The content work list against the vault knowledge base (master alignment, atom gaps) is held by the vault document *Verknüpfungsanalyse CLARIAH-AT-Skriptum und Vault-Wissensbestand*; this plan holds the repo side.

## Done (2026-08-20)

Repo founded; all repository files English; four design iterations approved; start page promoted to `docs/index.html` with the four-workshop register and the real CLARIAH cover; content intake complete (master script EN work in progress and DE Skriptum in `script/`, master deck export in `slides/`, final CLARIAH workshop script and profile in `workshops/2026-09-25-clariah-at/`); downloads triage reports in `drafts/`; specification rewritten with all decisions; id scheme unified across register, folders, covers and tags.

## Work packages

| WP | Content | Depends on | State |
| --- | --- | --- | --- |
| 1 | Content intake from the operator's downloads per the triage verdicts; CLARIAH PPTX stays outside until the taught state | triage | done 2026-08-20 |
| 2 | Master modularisation: consolidate the master script WIP with the German Skriptum into the five modules (units per `drafts/module-map.md`); German source, reviewed English | operator: fine-cut confirmation | open |
| 3 | CLARIAH workshop package: profile, final script, hands-on links | WP1 | done except PPTX and delivery notes, which follow the taught state |
| 4 | Further workshop profiles: KUG/M3GIM, Uni for Life, VetMed Winter School as thin profiles; past instances (VetMedAI workshop 1, ÖAW winter school) if the operator registers them | operator: past-instance decision | open |
| 5 | Platform: header brand with logo, top navigation, reworked workshop cards, and the workshop subpages (CLARIAH full six blocks, three thin) | WP3 | in progress (agent) |
| 6 | Terms: fill `terms.md` with English canonical wording, German equivalents and the literature anchors from `drafts/term-references.md` | operator: drift decisions D1–D4 | open |
| 7 | Vault re-pointing: the vault master documents become references to this repo; Project Overview updated | WP2 | open |
| 8 | Publication: LICENSE file (CC BY 4.0 for texts), GitHub Pages activation, full link and rendering verification, then announcement-ready | WP5; operator gates | open |

## Steady-state duties after the build

Register and pages stay in sync in the same work step (specification acceptance criterion). Each taught workshop gets its git tag, PPTX export, cover and delivery notes. Decisions land in `journal.md` the day they are made.

## Operator deliveries

CLARIAH title slide re-export at 1280 px; title-slide PNGs for the other workshops when their decks exist; final display title of the VetMed Winter School.
