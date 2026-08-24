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
updated: 2026-08-24
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [specification.md]
---

# Platform Design

Design stance and system values for `docs/`. The platform addresses a professional, international audience from research and industry. Real slide decks and course readers are the visual and functional anchors of each workshop page.

## Workshop page hierarchy

The workshop page begins with a compact text header and the real slide deck in a 16:9 Google Slides viewer. Abstract, outline and learning objectives follow as one three-column overview. The course reader occupies a separate embedded document viewer, followed by selected literature and references. This order supports use during teaching and later consultation from the same page.

Cover images remain on the landing-page cards as identifiers for the workshop series. Detail pages contain no cover image or decorative process diagram. The source-to-artifact motif developed in the earlier design round was removed from the landing page on 2026-08-24 after the operator found that it no longer contributed to the workshop-oriented information architecture.

## System values

- **Ground**: paper white as one consistent page ground, near-black typography, generous whitespace; light theme only (operator decision 2026-08-20).
- **Accent**: turquoise `#0A7E7C` as the primary accent for links, active states and motif highlights; the motif line art stays turquoise-only.
- **Identity palette**: four accents derived from the watercolor logo, orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`. The interface applies them to the five module marks (turquoise 01, orange 02, blue 03, violet 04, green 05, as implemented in `docs/assets/site.css`). Cover illustrations may use the same colors semantically inside their depicted objects. Text-carrying colors must pass WCAG AA, pure marks at least 3:1.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code.
- **Hierarchy**: at most two text levels per section, one heading and body; no stacked eyebrow-plus-heading labels. The workshop header carries title, subtitle and compact metadata. The viewer is the first large surface.
- **Imagery**: covers appear on landing-page cards only. Workshop detail pages use the live slide deck as their visual surface and contain no decorative header image. Future cover regeneration excludes readable text and generic AI illustration defaults.
- **Cards**: workshop entries as horizontal cards with cover, date, event, audience, the module badges of the modules the instance uses, and the links that exist, in chronological order; missing artifacts appear as quiet "in preparation" labels, never as dead links.
- **Chrome**: header brand, top navigation, EN/DE control and footer are one binding public-page template; the favicon set in `docs/assets/favicon/` is committed and every page links it. Page chrome is not re-invented per page.
- **Language control**: English and German are separate static pages connected by a compact segmented control. The active language carries `aria-current="page"`; the paired files carry reciprocal `hreflang` links.
- **Embedded material**: Google Slides uses a 16:9 viewer and a visible direct link. Google Docs uses a tall reading surface and a visible direct link. Missing artefacts retain the same page position as a quiet preparation state.

## Cover series

The operator selected the Full Slide Deck cover and all seven workshop covers on 2026-08-20. The repository holds `full.png` at 1664 by 936 pixels and each workshop cover at 1672 by 941 pixels. Every file exceeds the minimum width and conforms to the 16:9 cover slot.

The series uses one domain-bearing object per cover. Shared concepts are encoded through the object rather than added as a surrounding infographic.

- Maintained documents, archival bundles and scientific specimens carry knowledge.
- A turquoise aperture identifies the working context.
- A blue line or articulated tool carries agentic action and write-back.
- A green registration detail carries verification or governance where the subject requires it.
- The workshop domain determines the main object, including opera archive, scholarly codex, edition workstation, medieval charter, research-software workbench, professional document instrument and veterinary tissue specimen.

The current PNG files are the selected publication assets. Some retain incidental generator defaults such as pseudo-lettering, chart furniture or character-like agent forms. These details do not define the system. `knowledge/drafts/cover-image-prompts.md` is the production contract for later regeneration and constrains them explicitly. The medieval-studies cover is the single approved tool-identity exception. It uses the supplied small Claude Code agent figure because the workshop itself is conducted in Claude Code; the current cover remains the required identity reference.

## Iteration status

Design iteration 5 is approved and in force (operator decision 2026-08-24). It retains the typography, colour tokens, page ground, brand chrome and accessibility baseline of iteration 4. It replaces the cover-led detail page and repeated descriptive blocks with the embedded slides, the three-column overview, the embedded course reader and selected references. The landing page, preparation page and every registered instance have English and German page pairs. The landing-page motif was removed in the same revision.
