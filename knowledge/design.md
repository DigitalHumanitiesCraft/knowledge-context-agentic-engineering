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
updated: 2026-08-25
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [specification.md]
---

# Platform Design

Design stance and system values for `docs/`. The platform addresses a professional, international audience from research and industry. Real slide decks and course readers are the visual and functional anchors of each workshop page.

## Landing-page hierarchy

The landing page begins with a compact two-column hero. Title and a substantive abstract occupy the main reading column. The five module titles form a compact index in the right column without subtitles; on narrow viewports this index moves below the abstract. The abstract identifies the subject, audience, shared teaching material and derivation of workshops as documented specialisations.

Teaching Materials follows the hero without an intervening overview block or large section gap. It keeps direct access to the Full Slide Deck and the preparation state of the Full Lecture Notes. Workshops follow in chronological order, and a compact Preparation section links to the full bilingual guide. The anchors `#modules`, `#material`, `#workshops` and `#preparation` remain stable entry points.

## Workshop page hierarchy

The workshop page begins with a compact text header and one three-column overview containing the abstract, outline and learning objectives. The slide deck follows in a 16:9 Google Slides viewer. Available decks also provide a direct PDF export below the viewer. The course reader occupies a separate embedded document viewer, followed by selected literature and references. This order presents scope and expected outcomes before the teaching material.

Cover images remain on the landing-page cards as identifiers for the workshop series. Detail pages contain no cover image or decorative process diagram. The source-to-artifact motif developed in the earlier design round was removed from the landing page on 2026-08-24 after the operator found that it no longer contributed to the workshop-oriented information architecture.

## System values

- **Ground**: paper white as one consistent page ground, near-black typography, generous whitespace; light theme only (operator decision 2026-08-20).
- **Accent**: turquoise `#0A7E7C` as the primary accent for links, active states and motif highlights; the motif line art stays turquoise-only.
- **Identity palette**: four accents derived from the watercolor logo, orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`. The interface applies them to the five module marks (turquoise 01, orange 02, blue 03, violet 04, green 05, as implemented in `docs/assets/site.css`). Cover illustrations may use the same colors semantically inside their depicted objects. Text-carrying colors must pass WCAG AA, pure marks at least 3:1.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code.
- **Hierarchy**: at most two text levels per section, one heading and body; no stacked eyebrow-plus-heading labels. The workshop header carries title, subtitle and compact metadata for event, language and licence. The overview precedes the viewer.
- **Imagery**: covers appear on landing-page cards only. Workshop detail pages use the live slide deck as their visual surface and contain no decorative header image. Future cover regeneration excludes readable text and generic AI illustration defaults.
- **Cards**: workshop entries as horizontal cards with cover, date, event, audience, the module badges of the modules the instance uses, and the links that exist, in chronological order; missing artifacts appear as quiet "in preparation" labels, never as dead links.
- **Chrome**: header brand, top navigation, EN/DE control and footer are one binding public-page template; the favicon set in `docs/assets/favicon/` is committed and every page links it. GitHub is the only content link in the top navigation. The linked brand returns to the language-matched landing page, while detail pages retain their existing backlinks. The footer identifies DHCraft as the implementer, names the AI harnesses and Promptotyping, and links both the project and Promptotyping repositories with a quiet GitHub destination mark. Page chrome is not re-invented per page.
- **Language control**: English and German are separate static pages connected by a compact segmented control. The active language carries `aria-current="page"`; the paired files carry reciprocal `hreflang` links.
- **Embedded material**: Google Slides uses a 16:9 viewer, a visible direct link and a direct PDF export where a deck exists. Google Docs uses a tall reading surface and a visible direct link. Missing artefacts retain the same page position as a quiet preparation state. The interface does not claim that an embedded viewer requires a particular browser or account when the registered resource is publicly accessible.

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

Design iteration 7 is approved and in force (operator decision 2026-08-25). It retains the typography, colour tokens, page ground and accessibility baseline of iteration 6. Workshop pages now place abstract, outline and learning objectives before the slides. Their metadata contains event, language and licence. Available decks provide direct PDF exports. The shared footer records DHCraft as the implementer, Claude Code with Fable 5 and Opus 5, Codex with GPT-5.6 Sol, and Promptotyping as the context-engineering method. It exposes the project and method repositories through labelled GitHub links. The landing page, preparation page and every registered instance remain paired in English and German.
