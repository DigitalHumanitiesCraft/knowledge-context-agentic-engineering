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

1. The header separates two identities. The DHCraft logo is the only header element linking to `https://dhcraft.org` and carries an accessible name identifying the publisher website. The visible site name is the complete teaching-line title and links to the language-matched landing page. The section navigation holds `Materials`, `Preparation` and `Videos` (German `Material`, `Vorbereitung`, `Videos`) as fragment links. The EN/DE control connects the pair and marks the current language with `aria-current="page"`.
2. The hero carries the H1, one introductory paragraph, the list of the five modules and one compact paragraph with the id `about`. The introductory paragraph defines AI Harnesses through the one remaining inline definition and states that the slides are organised in five modules. The module list is an ordered list whose rows each join the line icon, the number and the module title, which links to the matching Video Library group `#video-module-0N`, with the language-matched definition as visible text. The ids `module-01` through `module-05` sit on the list items as stable fragment targets. Module 01 reads `“Understanding” Large Language Models` in English and `Large Language Models „verstehen“` in German, because the quotation marks carry a deliberate wordplay. The `about` paragraph opens with the sentence that each workshop selects from this material and adapts it to a field, task and teaching language, then explains DHCraft, workshop funding and public maintenance and links the repository. The page labels the holdings Slides and Lecture Notes in English and Folien and Skriptum in German, because the cards present them as the parts of one shared material; Full Slide Deck and Full Lecture Notes remain the repository names.
3. Teaching Materials (`#material`) follows the hero with four cards, Preparation, Slides, Lecture Notes in their English and German editions and the Video Playlist, and one methods card spanning the row below. They stand in one row on wide viewports, two per row below 1100 pixels and one below 640 pixels. Each card describes its holding by function. The Full Slide Deck is a reference work and the source for workshop-specific decks, and the Full Lecture Notes are its written-out counterpart. The Video Playlist description is exactly `An ordered video sequence from foundational to advanced topics, maintained and expanded over time.` in English and `Eine geordnete Videoreihe von den Grundlagen zu vertiefenden Themen, die laufend gepflegt und erweitert wird.` in German. The Full Slide Deck and each Lecture Notes edition show their Google format as a link labelled Google Slides or Google Docs, and the formats without a target as one quiet label, `Markdown and PDF soon` or `Markdown und PDF folgen`. The Lecture Notes card offers both editions as two actions named by language. Card titles are plain headings, and the cards share one height with their actions aligned at the foot.
4. The methods card (`#methods`), titled `Methods for continued work` or `Methoden für die Weiterarbeit`, presents Promptotyping, Grounded Vault, Second Brain Vault and Research Mission Control as four open methods in which DHCraft applies the foundations to its own projects. Each entry carries its name as a link to the portal or repository, one sentence on its purpose and a link to the matching video, marked as German on the English page. The four entries stand in one row on wide viewports, two per row below 1100 pixels and one below 640 pixels. The methods are presented as maintained working methods and not as recommended tools.
5. Preparation (`#preparation`) is the first card of Teaching Materials, set on the tinted ground as the step before a workshop. It carries the line mark `docs/assets/materials/preparation.svg`, a description of the English Google Slides deck [Preparation, Technical Setup](https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit) and one Google Slides action. The id `preparation` sits on the card, so the header link lands on it. Deck URL and language are registered in `data/workshops.json` under `preparation`. Both language versions state that the slides are in English.
6. The Video Library (`#videos`) renders every entry of `data/videos.json` exactly once, under its primary module, in playlist order within the group. The five groups are native disclosure sections and all start closed. A module link from the hero list opens its group on arrival. The pages carry each preview address as `data-thumb`, and `docs/assets/site.js` inserts the images when a group opens, so no request reaches YouTube before a reader opens a group. Without the script a card shows title and duration on a neutral 16:9 plate. Each card shows title, duration and a YouTube preview with empty alt text beside identifying text, and links the canonical watch URL carrying only the `v` parameter. A visible note explains that preview images load from YouTube once a group is opened, and no preview file is copied into the repository. The register keeps `module` as the required primary classification, an optional `related_modules` array where a documented cross-module relation exists and an optional `lang` for titles not in English, which the pages carry as a `lang` attribute where the title language differs from the page language. Each module entry carries its language-matched title and definition, the source of the hero module list. The registers live in `data/` at the repository root, outside the published tree.
7. The footer holds three groups, publisher identity, the provenance sentence followed by one sentence on the licence scope and a labelled link list (`Further links`, `Weiterführende Links`) with the teaching-material repository, `CC BY 4.0` and the canonical legal notice at `https://dhcraft.org/imprint`. The method repositories are linked from the methods card and from the provenance sentence. No footer names a model or model version, and dated tool provenance stays in `journal.md`.
8. The site is no-build HTML and CSS. One small script, `docs/assets/site.js`, adds Escape to dismiss a definition, lets the AI Harnesses term keep its definition open on click or tap and inserts video previews when a group opens. Every text, link and definition remains usable without it. The typefaces are served from `docs/assets/fonts/`, so the only external resources are the disclosed YouTube preview images. Each page carries a canonical URL, absolute `hreflang` alternates with `x-default` and Open Graph metadata. Both pages reference the same stylesheet version parameter. Published links carry no tracking or sharing parameters. Every public occurrence writes `Context Engineering` with a capital `C`.
9. The workshop records in `data/workshops.json` retain material provenance and generate no public event pages or navigation. Full-material and video links keep their ownership and rights boundaries.
10. `communication/` carries the Research Mission Control Context Stream. It transports bounded briefs, results, questions and recipient state and holds the Research Director Log. Durable project knowledge stays in `knowledge/`, and `communication/PROTOCOL.md` carries the message shape, endpoint ownership, immutability of published messages and the state cursors.

## Acceptance criteria

- Both language versions expose the same sections in the same order, without workshop listings, dates, Learning Routes or links to retired pages.
- All local links, assets, language counterparts and fragment targets resolve, including the five module links into the Video Library. Each page has one H1, one `main` landmark with a skip link, visible focus and touch targets of at least 44 pixels on coarse pointers.
- Each module list row keeps icon, number and title together, and its definition stays visible at every width. The AI Harnesses definition opens on pointer hover, keyboard focus and tap, stays open while the pointer moves onto it, closes with Escape or a tap elsewhere where the script runs, and never passes the viewport edge.
- The Preparation card action and the register entry name the same deck on both pages.
- The Video Library contains every register entry exactly once per language under its primary module, and the register indices form one unbroken sequence in playlist order.
- The Teaching Materials cards keep the approved descriptions and format positions, and the preparation states match the register.
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
- The five modules form a visible list with definitions instead of inline terms with tooltips, the use verbs above the card titles are dropped as redundant with the titles, the holdings appear as Slides and Lecture Notes or Folien and Skriptum on the page, and a methods card presents Promptotyping, Grounded Vault, Second Brain Vault and Research Mission Control as ways to continue (author decision 2026-11-04, after a variant review). The page grows by the list and the methods card, which places Teaching Materials below the first screen at 1280 by 800 pixels.
- Preparation joins the three holdings as the first of four cards with a use verb on each card, replacing its own section and title-slide image, because the four entries are parallel and the page becomes about 470 pixels shorter at desktop width (author decision 2026-11-04, after a variant review).
- Preparation shows a locally stored title slide that links to the deck instead of an embedded Google Slides viewer, so the page loads no third-party viewer and stays legible when Google Slides is unreachable (author decision 2026-11-04; the image was retired later that day with the four-card layout).

## Cumulative edition exercise

The Research Starter Workflow connects an agreed research question and source inventory to the Agentic Edition Pipeline in section 6.7 of the German Full Lecture Notes. The English notes carry its translated explanation, the Full Slide Deck its teaching sequence and Module 04 its entry link. The sequence is a teaching integration, with a one-page pilot, local source-checking viewer, TEI and optional analysis. Each stage requires explicit acceptance before continuation. HEDIT makes TEI a core outcome. Existing reviewed inputs may satisfy a stage after provenance checks. No repository clone, particular provider or installed pipeline capability is assumed. Workshop execution, scholarly acceptance and publication remain separate from editorial verification.
