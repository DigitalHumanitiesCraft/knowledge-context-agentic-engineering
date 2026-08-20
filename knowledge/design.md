---
title: Platform Design
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [specification.md]
---

# Platform Design

Design stance, motif and system values for `docs/`. The platform addresses a professional, international audience from research and industry; it must feel calm, precise and high-grade, and it shows the real slide decks as visual anchors instead of an invented illustration world.

## Motif

The guiding motif is the path from source to verified artefact: source, knowledge documents, working context, agentic loop, verification, artefact. It is drawn as reduced line art (inline SVG, two stroke weights) and serves as the platform's recurring diagram vocabulary; the slide decks can adopt the same vocabulary later. The operator approved this direction on the first prototype (2026-08-20); final tuning happens in the second iteration.

## System values

- **Ground**: paper white as one consistent page ground, near-black typography, generous whitespace; light theme only (operator decision 2026-08-20).
- **Accent**: turquoise as the single accent family for links, active states and motif highlights; exact values are tuned in the second prototype.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code.
- **Hierarchy**: at most two text levels per section, one heading and body; no stacked eyebrow-plus-heading labels; the motif stands without a caption; the hero is title, one sentence and one link.
- **Imagery**: only the workshop title-slide covers (16:9 PNG, minimum 1280 px wide, at `docs/assets/covers/<id>.png`) and the motif line art; no stock imagery, no generic AI illustrations.
- **Cards**: workshop entries as cards with cover, date, event, audience and links, in chronological order; missing artefacts appear as quiet "in preparation" labels, never as dead links.

## Open design decisions

- Final colour tuning and level reduction: second prototype `docs/drafts/design-draft-2.html`, under operator review.
- Workshop subpage structure: the six-block example `docs/drafts/workshop-page-draft.html` awaits the operator's reaction; its font will be aligned to Space Grotesk afterwards.
