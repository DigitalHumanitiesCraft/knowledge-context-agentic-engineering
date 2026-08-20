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

The guiding motif is the path from source to verified artifact, drawn as source, knowledge documents, working context, agentic loop, verification, artifact. It is drawn as reduced line art (inline SVG, two stroke weights) and serves as the platform's recurring diagram vocabulary; the slide decks can adopt the same vocabulary later. The operator approved this direction on the first prototype and confirmed it through the following iterations (2026-08-20).

## System values

- **Ground**: paper white as one consistent page ground, near-black typography, generous whitespace; light theme only (operator decision 2026-08-20).
- **Accent**: turquoise `#0A7E7C` as the primary accent for links, active states and motif highlights; the motif line art stays turquoise-only.
- **Identity palette**: four accents derived from the watercolor logo, orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`. Their single application is the five module marks (violet 01, orange 02, turquoise 03, blue 04, green 05); everything else stays monochrome plus turquoise, so the footer logo reads as the source of the palette. Text-carrying colors must pass WCAG AA, pure marks at least 3:1.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code.
- **Hierarchy**: at most two text levels per section, one heading and body; no stacked eyebrow-plus-heading labels; the motif stands without a caption; the hero is title, one sentence and one link.
- **Imagery**: only the covers (16:9 PNG, minimum 1280 px wide, upper third free of content, no text in the image, at `docs/assets/covers/<id>.png`) and the motif line art; no stock imagery, no generic AI illustrations.
- **Cards**: workshop entries as horizontal cards with cover, date, event, audience, the module badges of the modules the instance uses, and the links that exist, in chronological order; missing artifacts appear as quiet "in preparation" labels, never as dead links.
- **Chrome**: header brand, top navigation and footer are a single binding template; the favicon set in `docs/assets/favicon/` is committed and every page links it. Page chrome is not re-invented per page.

## Iteration status

Design iteration 4 is approved and in force (operator decision 2026-08-20). It derived the identity palette from the watercolor logo, applied it solely at the five module marks, and refactored the CSS into a documented token architecture with verified WCAG AA contrast. It is the state that `docs/index.html` and every subpage follow; the earlier prototypes in `docs/drafts/` are superseded and kept only as a record of the path.

The requirement of a bilingual EN/DE page toggle is dropped. Language is handled per module and per instance, so a page carries the language of the material it presents (operator decision 2026-08-20).
