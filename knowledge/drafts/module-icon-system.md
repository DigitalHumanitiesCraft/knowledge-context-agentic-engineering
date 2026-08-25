---
title: Module Icon System
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: proposal
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../design.md, ../terms.md, module-map.md]
---

# Module Icon System

This proposal defines five portable line icons for the visible module labels. The text label remains the accessible and semantic source. Each icon is a decorative carrier that adds a stable visual distinction without asking the reader to decode the image.

## Shared construction

- Every asset uses a 48 by 48 view box and declares the same 48 pixel intrinsic size.
- A two-unit `currentColor` contour with round caps and joins forms the common grammar.
- The live drawing stays within a four-unit outer margin. Filled marks identify a selected or active state and use the same `currentColor` value.
- The silhouettes remain legible at 24 to 32 pixels. Internal detail is limited to structural relations that survive this reduction.
- The files contain no text, raster image, font, script, external reference or embedded style block.
- Each root SVG carries `aria-hidden="true"` and `focusable="false"`. A surrounding visible module label supplies the accessible name.

## Semantic matrix

| Module | Asset | Primary object | Encoded relation |
| --- | --- | --- | --- |
| 01 “Understanding” Large Language Models | `01-understanding-llms.svg` | Bounded black box with an irregular internal contour | The outer system is observable through inputs and outputs, while capability remains uneven inside the box. |
| 02 Prompt Engineering | `02-prompt-engineering.svg` | Coordinate field with one activated point | A prompt steers model behaviour toward a selected region in latent program space. The remaining points show other available responses without forming a network. |
| 03 Knowledge and Context Engineering | `03-knowledge-context-engineering.svg` | Stack of maintained documents with one context aperture | Project knowledge persists across documents. A bounded selection enters the current working context. |
| 04 Agentic Engineering | `04-agentic-engineering.svg` | Harness boundary containing three communicating agent units | The harness organises delegated units and connects their work to explicit tool ports. The filled message marks show communication inside the bounded runtime. |
| 05 Critical Perspectives and Governance | `05-critical-perspectives-governance.svg` | Claim under an inspection lens followed by an open gate | A claim is inspected before an authorised downstream path becomes available. The gate represents decision authority and controlled continuation. |

## Distinctions carried by geometry

The system uses different relations rather than five variations of one generic technology symbol. Module 01 contains uncertainty inside a bounded model. Module 02 selects a coordinate. Module 03 selects information from a maintained document stack. Module 04 coordinates acting units and tool access. Module 05 places inspection and authority before downstream use.

The icon family excludes brains, robots, shields, scales, light bulbs, decorative checkmarks and generic node networks. Module 04 contains connected units because communication inside a harness is its subject. Its enclosure and external ports make this a specific system relation rather than a free-standing network motif.

## Use contract

Inline SVG use inherits the host element's `color` through `currentColor`. This allows the existing module palette to colour the same files without asset variants. When a file is loaded through an HTML `img` element, the external SVG document does not inherit the surrounding CSS color and renders with its own default text colour. A coloured web implementation should therefore inline the SVG or use an equivalent technique that supplies the colour inside the SVG document.

When the icon sits beside its visible module name, an HTML image reference uses an empty `alt` value. An inline copy keeps the supplied `aria-hidden` attribute. The icon never replaces the module number or title and never carries status by colour alone.

## Acceptance checks

The proposal is structurally ready when all five files parse as XML, expose the same view box and intrinsic dimensions, use `currentColor`, contain no text or raster elements and keep one shared stroke grammar. Visual acceptance remains with the operator after inspection at 48, 32 and 24 pixels.
