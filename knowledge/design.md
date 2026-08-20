---
title: Platform Design
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Design
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/design
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-design
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
- **Accent**: turquoise `#0A7E7C` as the primary accent for links, active states and motif highlights; the motif line art stays turquoise-only.
- **Identity palette**: four accents derived from the watercolor logo, orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`. Their single application is the five module marks (violet 01, orange 02, turquoise 03, blue 04, green 05); everything else stays monochrome plus turquoise, so the footer logo reads as the source of the palette. Text-carrying colours must pass WCAG AA, pure marks at least 3:1.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code.
- **Hierarchy**: at most two text levels per section, one heading and body; no stacked eyebrow-plus-heading labels; the motif stands without a caption; the hero is title, one sentence and one link.
- **Imagery**: only the workshop title-slide covers (16:9 PNG, minimum 1280 px wide, at `docs/assets/covers/<id>.png`) and the motif line art; no stock imagery, no generic AI illustrations.
- **Cards**: workshop entries as cards with cover, date, event, audience and links, in chronological order; missing artefacts appear as quiet "in preparation" labels, never as dead links.

## Open design decisions

- Fourth prototype `docs/drafts/design-draft-4.html` (logo palette, refactored token CSS) under operator review; on approval it is promoted to `docs/index.html`.
- Workshop subpage structure: the six-block example `docs/drafts/workshop-page-draft.html` awaits the operator's reaction; its font will be aligned to Space Grotesk afterwards.
