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
updated: 2026-11-04
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [specification.md]
---

# Platform Design

Design stance and system values for `docs/`. The platform addresses a professional, international audience from research and industry. The maintained Slide Deck, Lecture Notes and playlist are the main resources; Preparation uses its existing Google Slides deck.

## Landing-page hierarchy

The landing page reads from top to bottom within the 1160-pixel page width. A two-line title and one introductory paragraph lead directly to the four material cards, which carry the main routes and need no section label; their titles are the section headings. The modules follow as a quieter appendix, introduced by a mono label with the playlist link on the same line, which carries the same play symbol as the method video links. Each module row has no box: a left rule in the module colour, the portable line icon, the mono number, the title, the video count in quieter ink, the definition below in secondary ink and aligned with the title, and a neutral chevron on the right that shows whether the row is open. Opening it reveals the videos as a text list with title and duration. On pointer hover and keyboard focus a wash in the module colour flows out of the left rule across the row, the icon lifts slightly and the chevron takes the module colour and moves towards its next state; video rows take a faint wash of their module colour. The material cards keep no hover state, because only their actions are links. Under reduced motion the change is immediate and the icon does not move. The icons are a jagged capability boundary inside a black box, a selected coordinate in latent space, maintained documents with a context aperture, coordinated agents inside a tool-bearing harness, and a claim inspected before an authorisation gate. Module 01 keeps the quoted title that plays on model understanding. AI Harnesses is the one inline term with a definition, shown beside the term on pointer hover, keyboard focus or tap. The interface states how it is used through its controls, so no instruction line explains the disclosure.

The fragments `module-01` through `module-05` sit on the module summaries and `video-module-01` through `video-module-05` on the groups; both open their group where the script runs. Numbered modules describe the slide structure and do not create a second public page hierarchy.

The material cards are compact. Each carries a small line mark of about 2.75rem beside its title, one sentence and its actions: a laptop with a setup check for Preparation, a slide stack, a written page, a player with a sequence and four connected blocks on a shared base for Methods. Preparation stands first on the tinted ground with a turquoise rule on top, which stays visible on grey screens. Cards have no hover outline, because only their actions are links. Available formats are bordered actions; formats still in preparation are not shown. The Methods card groups its four methods by module. Each group is headed once by the module icon, number and title in quiet ink, the same mark as in the module rows, and lists its methods as plain links with a quiet play symbol at the row end that links the video. The module icons carry the assignment, so the methods need no imagery of their own.

Below the four cards a wide reference card spans the row with the glossary mark, the title, one sentence and one action, because the glossary is a lookup tool beside the holdings and a fifth narrow card would break the row of four. It stacks below 640 pixels.

The glossary page keeps the chrome of the landing page and the hero with H1 and a back link. A jump list names the modules with number and title, the search field and module filter follow, and each module group carries the module icon, number, title and the left rule in its module colour. Entries stand in two columns, one below 1020 pixels, as a description list with the term in weight 600, its counterpart in the other language in quieter ink and the definition below. The general group closes the page without number or icon. A targeted entry takes a faint wash of its module colour.

The modules need no preview images. Text lists keep the page short, can be scanned even in the largest group and load nothing from YouTube. A hint below the modules points to the complete Video Playlist.

## Single-page navigation and Preparation

The public site is one static page per language, `index.html` and `index.de.html`. The page leads from the introduction to the material cards and the modules; DHCraft, the methods and the funding are named in the footer. There are no separate About or Preparation pages and no generic arrow-back links. The canonical legal notice remains linked in the footer, together with the licence scope. Event listings and Learning Routes remain retired; teaching sources are unchanged.

Preparation is a card with its own line mark, a description that names the English language of the slides and one Google Slides action. No Google Slides iframe is embedded, so the page loads nothing from Google until a reader follows the link. The typefaces are self-hosted. No routing layer or build step is introduced, and the one enhancement script leaves every content readable without it.

## System values

- **Ground**: paper white as one consistent page ground, near-black typography, generous whitespace; light theme only (operator decision 2026-08-20).
- **Accent**: turquoise `#0A7E7C` as the primary accent for links, active states and motif highlights. On the tinted footer ground it reaches only 4.4:1, so footer links use the darker `--accent-on-tint` `#097472` at 5.0:1; the motif line art stays turquoise-only.
- **Identity palette**: four accents derived from the watercolor logo, orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`. The interface applies them to the five module marks (turquoise 01, orange 02, blue 03, violet 04, green 05, as implemented in `docs/assets/site.css`). Text-carrying colors must pass WCAG AA, pure marks at least 3:1.
- **Brand**: DHCraft watercolor logo (standard variant from `DigitalHumanitiesCraft/brand-assets`), set sparingly.
- **Typography**: Space Grotesk throughout with system fallback (operator decision 2026-08-20); IBM Plex Mono for prompts and code. Both are served from `docs/assets/fonts/` as Latin subsets.
- **Definitions**: the module definitions are visible text in the module summaries. The AI Harnesses definition opens below its term on wide viewports and stays open while the pointer moves onto it. Below 1180 pixels and on touch screens it appears as a sheet fixed to the bottom of the screen, so it never passes the viewport edge. Escape or a tap elsewhere closes it where `site.js` runs.
- **Hierarchy**: at most two text levels per section, one heading and body. Each material card holds mark, title, one sentence and actions.
- **Imagery**: the line marks of the four cards and the glossary card and the five module icons are the only images; no third-party image is loaded.
- **Cards**: four material cards present Preparation, the holdings and the methods with their available formats. The videos sit as text lists inside the native module disclosure groups.
- **Chrome**: the shared header contains the logo and the EN/DE control. The footer links the external legal notice and states the licence scope. Both pages retain the keyboard skip link, favicon and visible focus. No generic arrow-back navigation is used.
- **Current topology**: one English and one German static page contain the complete public interface. Author acceptance and publication remain separate.
- **Site identity**: the header carries the compact DHCraft logo, which leads to `https://dhcraft.org` and whose accessible name names the publisher website, and the language control. The H1 names the page, so the header repeats neither the title nor the section labels. The logo keeps at least 44 pixels on coarse pointers.
- **Footer**: one compact grid of three visually distinct groups, aligned at their top edge on wide viewports and stacked in the same semantic order on narrow ones. A quiet tinted ground and fine top rule separate it from teaching content. Vertical padding stays between 32 and 40 pixels, and the publisher logo remains between 72 and 80 pixels. The first group carries publisher identity, the second two short sentences on development, methods and funding, and the third a navigation labelled `Further links` or `Weiterführende Links`. `Digital Humanities Craft` links to `https://dhcraft.org`, `Promptotyping` to `https://dhcraft.org/Promptotyping/` and every Research Mission Control occurrence to `https://github.com/DigitalHumanitiesCraft/research-mission-control`. The navigation is one short column with the teaching-material repository, the licence link `CC BY 4.0 for the original text` and the canonical legal notice; the method repositories are linked from the methods card. The public footer names no model and no version; dated tool and model provenance stays in `knowledge/journal.md`. Focus states and coarse-pointer touch targets of at least 44 pixels remain intact.
- **Language control**: English and German are separate static pages connected by a compact segmented control. The active language carries `aria-current="page"`; the paired files carry reciprocal `hreflang` links.
- **Module language**: the first visible module title uses quotation marks to expose the semantic play between model understanding and claims that a model itself understands: `“Understanding” Large Language Models` in English and `Large Language Models „verstehen“` in German. The remaining English titles use their canonical forms. The German page translates descriptive titles and retains established method names such as Prompt Engineering and Agentic Engineering.
- **Slide previews**: Slide decks are never embedded as iframes. Preparation links its deck from a card action. The cards link the Google format of the slides and both editions of the lecture notes; Markdown and PDF appear once the register holds them. The Video Playlist is linked beside the modules heading. Formats still in preparation are not shown. The interface does not claim that an embedded viewer requires a particular browser or account when the registered resource is publicly accessible.

## Interface contract

`docs/assets/site.css` contains the executable token values; this document records their roles and the reasons for their use. The external `UI-DESIGN.md` supplied on 2026-08-25 was evaluated as a design-system audit and has been consolidated here where it matches the accepted interface. Its proposals for a separate design document, point-only module marks, a material matrix, card-wide workshop links, fixed 768/1024 breakpoints and a top-aligned hero index are superseded by the implemented decisions above.

The type system has two semantic families. Space Grotesk carries reading text, titles and controls. IBM Plex Mono carries dates, sequence numbers, module numbers, category labels, code and prompt surfaces. The responsive scale is defined by `--text-sm` through `--text-hero`; body copy resolves between 16 and 17 pixels, card titles at 18 pixels and the landing title between 32 and 48 pixels. Prose uses an 80-character measure, which yields roughly 75 to 90 characters per line of running text. The mono uppercase label `Modules and videos` is a real h2 in markup and only looks like metadata; the material cards need no label because their titles are the section headings.

The spatial system uses an eight-pixel base from `--s1` through `--s6`, one maximum width of 1160 pixels shared by header, main content and footer, and section gaps that remain larger than the internal gaps of their components. The responsive rules are content-specific instead of being treated as device classes. The hero remains single-column at every width, and its H1 is capped at 32 characters so the title takes two lines on wide viewports. The material cards use four columns, two below 1020 pixels and one below 640 pixels. The remaining responsive rules adapt the header, the footer and compact component layouts. Every grid child can shrink through `min-width: 0`, and no component may create page-level horizontal scrolling.

Interactive elements have three visual roles. Inline links are underlined and identify destinations in prose or local navigation. Bordered actions expose an available external or downloadable resource. Plain links in ink, which turn turquoise on hover, list methods and videos. Formats that are not yet available are not shown. Focus uses the shared two-pixel turquoise outline with a three-pixel offset; hover never supplies information that keyboard focus cannot reveal.

White bordered cards present the materials; Preparation alone is tinted. Module rows carry no box. The only images are the line marks and module icons, which keep their declared ratio. The five module icons share one construction: a 48-unit view box, a two-unit `currentColor` contour with round caps and joins inside a four-unit margin, legible at 24 to 32 pixels, without text, raster, font or script. They are decorative (`aria-hidden="true"`), never replace number and title, and carry no status by colour alone. The family avoids brains, robots, shields, scales, light bulbs, checkmarks and generic node networks.

Material and Preparation links originate in `data/workshops.json`; its workshop records retain provenance without generating public pages. Playlist state originates in `data/videos.json`. Paired static HTML is updated with these sources in the same maintenance step. Runtime JavaScript does not repair inconsistent content. HTML supplies one `h1`, native disclosure controls and one main-content target per page. Module colour, icon and number reinforce one another; unavailable formats include visible text.

## Earlier states

The cover series of 2026-08-20 and its motif contract served the retired workshop cards. The images are preserved in git history at `e66901b` under `docs/assets/covers/`, and their motif contract is preserved at the same commit as `knowledge/drafts/cover-image-prompts.md`. The v0.2 and v0.3 interface states with workshop pages, Learning Routes, Harness introductions and About pages are tag `v0.3` and commit `836b663`. Their iteration history and acceptance records remain readable in this file at commit `391fc9d`.
