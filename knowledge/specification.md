---
title: Platform and Repo Specification
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Specification
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/specification
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-specification
status: draft
created: 2026-08-20
updated: 2026-11-04
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [project.md, design.md]
---

# Platform and Repo Specification

Requirements for the public platform (`docs/`, GitHub Pages) and the carrying repo structure. Visual rules and the information hierarchy live in `design.md`.

## Usage scenarios

1. A participant preparing for a workshop opens the page, follows the Preparation deck and returns later to the shared material and the videos.
2. A reader who meets the teaching line for the first time learns its five modules from the opening paragraph and reaches the videos of any module in one step.
3. An organiser checks what the shared material contains and opens the Full Slide Deck or the Full Lecture Notes directly.
4. An agent working on the material reads the registers and the knowledge base to know which artefacts exist and where they live.

## Public contract

The public site is one static page per language, `docs/index.html` and `docs/index.de.html`. Both pages carry the same structure in the same order.

1. The header holds the DHCraft logo, the only header link to `https://dhcraft.org`, with an accessible name identifying the publisher website, and the EN/DE control, which marks the current language with `aria-current="page"`. The page has no section navigation and no header site name, because the H1 names the page and its two sections sit within the first screens; the skip link reaches the main content.
2. The page reads from top to bottom. Below the header stand the H1 and one introductory paragraph; then the four material cards; then the modules and videos as a quieter appendix; then the footer. The introductory paragraph defines AI Harnesses through the one inline definition and states that workshops select from the five modules and adapt them to a field, task and teaching language. The page labels the holdings Slides and Lecture Notes in English and Folien and Skriptum in German; Full Slide Deck and Full Lecture Notes remain the repository names.
3. Materials (`#material`, named `Materials` or `Material` for assistive technology only, with no visible label) are four cards in one row, whose titles are the h2 headings of the section, two per row below 1020 pixels and one below 640 pixels: Preparation, Slides, Lecture Notes and Methods. Each card has a small line mark beside its title, one sentence on its use and its actions at the foot. Slides and Lecture Notes link their Google formats; formats without a target are not announced on the page, and `data/workshops.json` records them as `null`. Preparation (`#preparation`) stands first on the tinted ground and links the English Google Slides deck [Preparation, Technical Setup](https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit), whose URL and language are registered in `data/workshops.json` under `preparation`. Methods (`#methods`) links Promptotyping, Grounded Vault, Second Brain Vault and Research Mission Control as maintained DHCraft methods, not as recommended tools. Each method carries the icon of the module it applies, 03 Knowledge and Context Engineering for the first three and 04 Agentic Engineering for Research Mission Control, with the module named in hidden text, and a quiet play link to its introductory video. The Video Playlist is linked from the heading row of the modules, which already lead to every video.
4. Modules and videos (`#videos`) follow the materials as one list of five native disclosure groups `#video-module-0N`, all closed at first, separated by whitespace and a left rule in the module colour, with a neutral chevron for the open state. Each summary carries the line icon, the number, the module title, the video count and the module definition as visible text, and its id `module-0N` keeps the earlier fragment targets. Opening a group shows its videos as a text list of linked title and duration in playlist order; every entry of `data/videos.json` appears exactly once, under its primary module, with a canonical watch URL carrying only the `v` parameter. The page loads no preview image, so no request reaches YouTube before a reader follows a link. A link to `#module-0N` or `#video-module-0N` opens that group where `docs/assets/site.js` runs. Module 01 reads `“Understanding” Large Language Models` in English and `Large Language Models „verstehen“` in German. The register keeps `module` as the required primary classification, an optional `related_modules` array, an optional `lang` for titles not in English, which the pages carry as a `lang` attribute where it differs from the page language, and per module the language-matched title and definition. The registers live in `data/` at the repository root, outside the published tree.
5. The footer holds three groups, publisher identity, two short sentences on development, the methods used and the funding by commissioned workshops, and a labelled link list (`Further links`, `Weiterführende Links`) with the teaching-material repository, `CC BY 4.0 for the original text` or `CC BY 4.0 für die eigenen Texte` and the canonical legal notice at `https://dhcraft.org/imprint`. No footer names a model or model version, and dated tool provenance stays in `journal.md`.
6. The site is no-build HTML and CSS. One small script, `docs/assets/site.js`, adds Escape to dismiss a definition, lets the AI Harnesses term keep its definition open on click or tap and opens a module group named in the fragment. Every text, link and definition remains usable without it. The typefaces are served from `docs/assets/fonts/`, and the page loads no external resource. Each page carries a canonical URL, absolute `hreflang` alternates with `x-default` and Open Graph metadata. Both pages reference the same stylesheet version parameter. Published links carry no tracking or sharing parameters. Every public occurrence writes `Context Engineering` with a capital `C`.
7. The workshop records in `data/workshops.json` retain material provenance and generate no public event pages or navigation. Full-material and video links keep their ownership and rights boundaries.
8. `communication/` carries the Research Mission Control Context Stream. It transports bounded briefs, results, questions and recipient state and holds the Research Director Log. Durable project knowledge stays in `knowledge/`, and `communication/PROTOCOL.md` carries the message shape, endpoint ownership, immutability of published messages and the state cursors.

## Acceptance criteria

- Both language versions expose the same sections in the same order, without workshop listings, dates, Learning Routes or links to retired pages.
- All local links, assets, language counterparts and fragment targets resolve, including `#module-0N` and `#video-module-0N`. Each page has one H1, one `main` landmark with a skip link, visible focus and touch targets of at least 44 pixels on coarse pointers.
- Each module summary keeps icon, number and title together, and its definition stays visible at every width. The AI Harnesses definition opens on pointer hover, keyboard focus and tap, stays open while the pointer moves onto it, closes with Escape or a tap elsewhere where the script runs, and never passes the viewport edge.
- The Preparation card action and the register entry name the same deck on both pages.
- The module groups contain every register entry exactly once per language under its primary module, and the register indices form one unbroken sequence in playlist order.
- The four material cards keep their descriptions and actions, and the preparation states match the register. At 1280 by 800 pixels the first screen shows the title, the introduction and all four cards.
- Wide and narrow browser checks at 1280, 1020, 900, 640, 390 and 320 pixels show no page-level horizontal overflow and no console errors. Structural checks and observed rendering stay distinct from author acceptance and publication.

## Earlier states

The August installation with workshop pages, Learning Routes, HTML Preparation lessons, Harness introductions and About pages was superseded on 15 October 2026 by the single-page contract. Its last state is commit `836b663`, and the v0.3 release with Module 00 and subject hubs is tag `v0.3`. The 15 October single page embedded the Preparation deck in a Google Slides viewer and listed the modules in a separate column beside the abstract. Both were replaced on 4 November 2026. The full superseded requirements, acceptance criteria and decisions remain readable in this file at commit `8f14d0b`.

## Decisions

- Registry as one JSON file instead of a frontmatter collection, because one entry per instance is the smallest maintenance unit and machine-readable state must live in one place (2026-08-20).
- Pages are static markup kept in sync with the registers by agents instead of client-side rendering from JSON, because at this scale a page whose content needs no JavaScript is more robust and the sync is verifiable (2026-08-20).
- The three holdings are described by their intended use rather than by a count of modules. The Full Slide Deck and the Full Lecture Notes express the same concepts at different levels of expansion, so a shared conceptual change is reconciled across both (Research Director decision 2026-08-25).
- The video register keeps one primary module per entry and an optional `related_modules` array, so each video renders once while cross-module relations stay recorded (Research Director decision 2026-08-25).
- The header separates the publisher mark from the teaching-site identity, because a reader who clicks the site name expects the site rather than the publisher (Research Director decision 2026-08-25).
- The footer names the two maintained methods and no model or model version, because a public page cannot carry the date at which a version was true (Research Director decision 2026-08-25).
- The public site became one page per language on 15 October 2026. Event listings, Learning Routes and the separate About and Preparation pages were retired, and the About text moved into the hero (author decision 2026-10-15).
- The modules are named inline in the abstract, with icon, number and colour, and each links to its video group. The separate module column was removed as duplicate information, and the content column widened to about 80 characters per line (author decision 2026-11-04).
- Fonts are self-hosted, every video group starts closed, the registers leave the published tree and a small enhancement script makes the definitions dismissible, so a page view sends no request to a third party before the reader acts and the definitions meet WCAG 1.4.13 (author decision 2026-11-04, after the five-part site review).
- After a research, task-test and design review on 4 November 2026, module links open their video group, the module definitions appear as visible text in the groups, cards keep their own heights without a whole-card hover, formats in preparation share one label, the Google actions name their product, the playlist and the title slide are no longer duplicate keyboard stops, and the abstract drops the sentence that repeated the three cards (author instruction to implement the optimisations, 2026-11-04). The reading measure stays at 80 characters by the author's earlier decision, although the UI yardstick in the vault asks for under 80.
- The material cards move above the modules, which become a quieter appendix without boxes; the header loses its site name and section navigation as duplicates of the H1 and the section labels; the Video Playlist card gives way to a playlist link beside the modules; the publisher paragraph is absorbed by the introduction and a shorter footer; and the formats in preparation are named once (author feedback 2026-11-04).
- Modules and videos merge into one list of disclosure groups with visible definitions and text video lists, and the five material cards, Methods included, form a compact column beside them. This brings the entry points of the page onto one screen on desktop and removes the YouTube preview images (author decision 2026-11-04, after three prototypes and a synthesis).
- The five modules form a visible list with definitions instead of inline terms with tooltips, the use verbs above the card titles are dropped as redundant with the titles, the holdings appear as Slides and Lecture Notes or Folien and Skriptum on the page, and a methods card presents Promptotyping, Grounded Vault, Second Brain Vault and Research Mission Control as ways to continue (author decision 2026-11-04, after a variant review). The page grows by the list and the methods card, which places Teaching Materials below the first screen at 1280 by 800 pixels.
- Preparation joins the three holdings as the first of four cards with a use verb on each card, replacing its own section and title-slide image, because the four entries are parallel and the page becomes about 470 pixels shorter at desktop width (author decision 2026-11-04, after a variant review).
- Preparation shows a locally stored title slide that links to the deck instead of an embedded Google Slides viewer, so the page loads no third-party viewer and stays legible when Google Slides is unreachable (author decision 2026-11-04; the image was retired later that day with the four-card layout).

## Cumulative edition exercise

The Research Starter Workflow connects an agreed research question and source inventory to the Agentic Edition Pipeline in section 6.7 of the German Full Lecture Notes. The English notes carry its translated explanation, the Full Slide Deck its teaching sequence and Module 04 its entry link. The sequence is a teaching integration, with a one-page pilot, local source-checking viewer, TEI and optional analysis. Each stage requires explicit acceptance before continuation. HEDIT makes TEI a core outcome. Existing reviewed inputs may satisfy a stage after provenance checks. No repository clone, particular provider or installed pipeline capability is assumed. Workshop execution, scholarly acceptance and publication remain separate from editorial verification.
