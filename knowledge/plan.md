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

Repo founding (skeleton, register, knowledge folder) is complete (2026-08-20). Two tracks now run in parallel; on conflicts the CLARIAH date (2026-09-25) wins. The content work list against the vault knowledge base (master alignment, atom gaps, drift decisions) is held by the vault document *Verknüpfungsanalyse CLARIAH-AT-Skriptum und Vault-Wissensbestand*; this plan holds the repo side.

## Track A — CLARIAH and platform

| Step | Content | State |
| --- | --- | --- |
| A1 | CLARIAH profile in `workshops/clariah-at-2026/` with the lecture notes as material | open |
| A2 | Design prototypes (start page, example workshop subpage) for the operator's motif, font and page-structure decisions | in progress (agents) |
| A3 | Build the platform after the design decision: start page plus workshop subpages, driven by the register | open |
| A4 | Activate GitHub Pages, check rendering and links | open |

## Track B — Master corpus

| Step | Content | State |
| --- | --- | --- |
| B1 | Module cut of the master script | top level set by the operator, five modules (journal 2026-08-20); fine cut beneath them proposed in `drafts/module-map.md`, confirmation open |
| B2 | Migrate the master script into `script/` as modules (DE source) after the operator confirms the cut | open |
| B3 | English module versions by agent translation with operator review | open |
| B4 | Migrate the master slide texts into `slides/`, aligned with the module cut | open |
| B5 | Fill `terms.md` after the drift decisions, then write back into script, slides and vault atoms | literature draft in progress |

Closing steps after both tracks: re-point the vault (source-of-truth tables, Project Overview, Repo-Verzeichnis; the vault master documents become references) and add the CC BY license statement to the repo.

Operator deliveries when available: title-slide PNGs per workshop (16:9), PPTX exports of the existing decks.
