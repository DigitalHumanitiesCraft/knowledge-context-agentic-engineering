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

Repo founding, the English switch and four design iterations are complete (2026-08-20). The build now runs as work packages, each delegated to Opus subagents and coordinated by the orchestrator; a package counts as done only after verification against the real file state. On conflicts the CLARIAH date (2026-09-25) wins. The content work list against the vault knowledge base (master alignment, atom gaps, drift decisions) is held by the vault document *Verknüpfungsanalyse CLARIAH-AT-Skriptum und Vault-Wissensbestand*; this plan holds the repo side.

## Work packages

| WP | Content | Depends on | State |
| --- | --- | --- | --- |
| 1 | Content intake: move the authoritative operator files (current master script WIP, final CLARIAH workshop script, full-slidedeck text, PPTX export, cover-candidate PNGs) from the downloads into their repo locations, following the two triage verdicts in `drafts/` | triage drafts | triage in progress |
| 2 | Master modularisation: consolidate the current master script WIP with the vault Skriptum into the five modules (units beneath per `drafts/module-map.md`); German source and reviewed English per the language pipeline | WP1; operator: fine-cut confirmation | open |
| 3 | CLARIAH workshop package: profile (recipe over the master), final workshop script, hands-on links to the zbz package, PPTX per taught state | WP1 | open |
| 4 | Further workshop profiles: KUG/M3GIM and Uni for Life as thin "in preparation" profiles; VetMedAI if the operator registers it | operator: VetMedAI decision | open |
| 5 | Platform: promote the approved design to `docs/index.html`, build the workshop subpages in the approved six-block structure, integrate the covers, keep the pages in sync with the registry `docs/data/workshops.json` | operator: design and subpage approval; WP1, WP3 | open |
| 6 | Knowledge-base completion: `specification.md` rewritten in English with all decisions; `terms.md` filled with English canonical wording, German equivalents and the literature anchors from `drafts/term-references.md` | operator: drift decisions | open |
| 7 | Vault re-pointing: the vault master documents become references to this repo; Project Overview updated | WP2 | open |
| 8 | Publication: LICENSE file (CC BY 4.0 for texts), GitHub Pages activation, link and rendering verification | WP5; operator gates | open |

## Open operator gates

Design promotion, subpage structure, VetMedAI registration, name of the fifth module, drift decisions on term wording, Pages activation, git tags per taught workshop state.
