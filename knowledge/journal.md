---
title: Journal
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Journal
  version: 0.4
  url: https://dhcraft.org/Promptotyping/promptotyping-document/journal
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-journal
status: active
created: 2026-08-20
updated: 2026-11-04
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [project.md, specification.md, handoff.md]
---

# Journal

This journal is the curated retrospective provenance index of the project. Current facts and rules remain in the responsible Declarative and Action Documents, accepted future work in `plan.md`, open received deltas in `handoff.md`, and detailed revisions in Git.

## Entries

### 2026-11-04 integrated · Methods carry their module icon and a video link

The author wanted fitting icons for the methods without arbitrary imagery. The methods are assigned to the modules they apply, Promptotyping, Grounded Vault and Second Brain Vault to 03 Knowledge and Context Engineering and Research Mission Control to 04 Agentic Engineering, and each method row reuses that module's icon, with the module named in hidden text for screen readers. A neutral play symbol at the row end links each method's introductory video, deliberately not the YouTube mark. The list becomes one column, which ends the broken line breaks of the two-column layout. Checked at four widths in both languages: no overflow and no external request.

### 2026-11-04 integrated · Material cards without label and pending note

On the author's instruction the note on Markdown and PDF versions in preparation and the visible `Materials` label above the cards are removed. The card titles become the h2 headings of the section, which keeps the heading order H1 to H2, and the section keeps `Materials` or `Material` as its accessible name. Formats without a target stay recorded as `null` in the register. Checked at four widths in both languages: no overflow, no external request and the heading order H1 followed by H2.

### 2026-11-04 integrated · Materials first, modules as appendix, no duplicated chrome

The author judged the videos to be a supplement rather than the main route and pointed to duplications. The four material cards, Preparation, Slides, Lecture Notes and Methods, now follow the introduction in one row, and the modules with their videos form a quieter appendix below: rows without boxes, a left rule in the module colour, a neutral chevron for the open state and the definition aligned with the title. The header drops the site name and the section navigation, because the H1 names the page and the two sections fit within the first screens. The Video Playlist card gives way to a playlist link beside the modules heading, which already leads to every video. The formats in preparation are named in one note below the cards, the instruction lines are removed because the controls show how they work, the workshop sentence moves into the introduction, and the publisher paragraph is replaced by two short footer sentences with the licence scope in the licence link. Checked at six widths from 1440 to 320 pixels in both languages: no page or tooltip overflow, no external request, keyboard order materials before modules, module fragments open their group, every register entry listed once, and every stylesheet class in use. At 1280 by 800 pixels the first screen shows the title, the introduction and all four cards.

### 2026-11-04 integrated · One workspace of modules and materials

The author asked why Methods was not a card of its own and whether modules, materials and videos could reach one screen. Three prototypes outside the repository tested a two-column workspace, five cards above a module library with preview images, and compact cards above module tabs. The author liked the module rows and the compact cards, and a synthesis of the workspace and the compact cards was adopted. The modules and the Video Library are now one list of five disclosure groups whose summaries show icon, number, title, count and definition and whose videos open as a text list of title and duration. The five material cards, Methods now among them, are compact, each with a small line mark beside its title, one sentence and its actions; they form the right column on wide screens and come first on narrow ones. The title shrinks to two lines, the publisher paragraph moves below the workspace, the preview images and their script are retired, and the page loads no external resource. Links to `#module-0N` and `#video-module-0N` open their group. Checked at seven widths from 1440 to 320 pixels in both languages: no page or tooltip overflow, no external request, keyboard order materials before modules, every register entry listed once, and every stylesheet class in use. At 1280 by 800 pixels the first screen shows all five module summaries and the first four material cards.

### 2026-11-04 integrated · Module list, methods card and plain holding names

From a second variant the author adopted three changes together. The five modules leave the running text and form a list in the hero, each row with icon, number, linked title and the definition as visible text, so the module tooltips and the repeated definitions in the video groups are retired and only AI Harnesses keeps an inline definition. The use verbs above the card titles are dropped as redundant with the titles, and the page names the holdings Slides and Lecture Notes, in German Folien and Skriptum, with the Skriptum described as the slides written out with what the talk adds; the repository names Full Slide Deck and Full Lecture Notes stay. A full-width methods card below the four cards presents Promptotyping, Grounded Vault, Second Brain Vault and Research Mission Control with one sentence and a video each, and the footer navigation shrinks to the teaching-material repository, the licence and the legal notice. On the author's remark that the list carried too many horizontal lines, and in line with the vault UI yardstick that rows are separated by whitespace and single hairlines, the list and the methods entries lose their rule lines and keep only the module-coloured underline. Checked at eight widths from 1440 to 320 pixels in both languages: no page or tooltip overflow, no external request before a video group opens, module links open their group, and no stylesheet class is left without markup. The list places Teaching Materials below the first screen at 1280 by 800 pixels.

### 2026-11-04 integrated · Preparation joins the materials as a fourth card

The author observed that the Full Slide Deck and the Preparation deck serve the same kind of function but looked different. A variant built outside the repository placed Preparation as the first of four cards beside the three holdings, each card with a use verb above its title (Prepare, Browse, Read, Watch, in German Vorbereiten, Überblicken, Nachlesen, Ansehen), and the author adopted it. The separate Preparation section and the title-slide image are retired, a new line mark `preparation.svg` follows the style of the other three, the Lecture Notes card offers its two editions as two actions named by language, and the `preparation` id moves onto the card. At 1280 pixels the page is about 470 pixels shorter. Checked at eight widths from 1440 to 320 pixels in both languages: four equal-height cards in one row down to 1100 pixels, two per row below and one below 640, no page or tooltip overflow, no external request before a video group opens, and module links still open their group. The title-slide PNG left the published tree and stays in git history.

### 2026-11-04 integrated · Interface pass from research, task tests and design review

Three read-only reviews prepared this pass, a literature and comparable-site study (Nielsen Norman Group, GOV.UK, W3C, Baymard, Carpentries, Programming Historian, MIT OpenCourseWare, DARIAH-Campus, Hugging Face), task-based tests in headless Edge at desktop and phone widths, and a visual critique. All three found that a module link in the abstract landed on a closed group, so `site.js` now opens the targeted group, and every group repeats its module definition as visible text, which also gives touch readers the definitions that a link cannot show as a tooltip. The cards keep their own heights and lose the whole-card hover, card titles are plain headings, the Google actions read Google Slides or Google Docs, and the formats in preparation share one quiet label per row. The abstract drops the sentence that repeated the three cards and the H1 widens to two lines on desktop, which moves the Teaching Materials heading from about 673 to 552 pixels at 1280 pixels width. The title-slide image shrinks and leaves the tab order, the resource marks are cropped to their drawing, the language control gets a visible hover and the footer licence becomes one sentence. Measured after the change at seven widths in both languages: no page or tooltip overflow, no YouTube request before a group opens, and a module link opens its group and loads its previews. Real touch devices and screen readers were not tested. The 80-character measure stays by the author's decision and conflicts with the vault yardstick's limit below 80.

### 2026-11-04 integrated · Privacy, definitions and register placement after the site review

On the author's instruction to implement every remaining optimisation, the review's decision points are resolved. The typefaces are self-hosted as Fontsource Latin subsets with their OFL licences, so the page makes no request to Google. Every video group starts closed, and the pages carry preview addresses as `data-thumb` that `docs/assets/site.js` turns into images when a group opens, because a headless check showed that lazy loading alone still fetched all preview images for closed groups. The same script makes the term definitions dismissible with Escape and lets the AI Harnesses button keep its definition open, while hover and focus keep working through CSS alone. Below 1180 pixels a definition becomes a bottom sheet, which removes the measured overflow at mid widths. The two new playlist entries join the register, the first under Module 03 and the second under Module 04, a classification the author accepted the same day, and the register marks German titles with `lang`, which the pages carry as attributes. The registers move from `docs/data/` to `data/`, because no page reads them and they carry working states. Canonical, absolute `hreflang` with `x-default` and Open Graph metadata are added, unavailable formats become quiet labels, the Preparation card shrinks and the footer groups repositories and legal links in separate columns. The title slide was checked against the deck and carries no further imagery. The favicon set stays unchanged because it equals the current DHCraft set in the brand-assets repository. Headless checks found no external request before a group opens, five preview requests after opening Module 01, no tooltip past the viewport edge at ten widths from 1440 to 320 pixels and no page overflow with all groups open. Past workshop instances and their tags remain with the author.

### 2026-11-04 integrated · Corrections from the five-part site review

A read-only review in five dimensions (content, accessibility, layout, data and links, code and performance) produced the findings that need no author decision, and they are corrected here. The German meta description no longer promises workshop pages, both descriptions match, and the English one capitalises Context. The hero sentence loses its semicolon, the German version adapts the material to field, task and teaching language as in English, and the tooltips say LLM where an LLM is meant. German terminology settles on Lehrmaterialien and Research Mission Control, and the pending format labels read `(soon)` and `(folgt)` instead of a middle-dot separator. The video register's German name for Module 03 now matches the page. In the stylesheet the footer links take a darker accent that clears 4.5:1 on the tinted ground, the off-screen skip link no longer casts a shadow into the page, the mobile header fits on two rows at 390 pixels, video group counts no longer break inside the parenthesis, and dead video-card selectors, a never-set second term colour, duplicate rules and decorative banners are removed. The unused font weight 700 is no longer requested, and the logo is resampled to 160 pixels width, from about 265 KB to about 76 KB. A computed-style comparison of every element on both pages at 1280, 900, 640, 390 and 320 pixels before and after the stylesheet change showed only these intended differences and no horizontal overflow. Font hosting, the default-open first video group, tooltip dismissal, the two new playlist videos, the public registers and the past workshop instances remain author decisions.

### 2026-11-04 integrated · Design history trimmed and footer separator removed

`design.md` drops its historical cover-series and v0.2 and v0.3 release sections in favour of a pointer to commit `391fc9d`, tag `v0.3` and commit `836b663`, and no longer mentions covers or a slide viewer. `CLAUDE.md` drops the historical subpage from the instance id and the iteration-16 baseline. The footer contact lists the website and the mail address on separate lines instead of a middle-dot separator. Headless browser checks of the German footer at 1280 and 390 pixels showed both lines and no horizontal overflow.

### 2026-11-04 integrated · Specification and README rewritten for the single page

The specification still carried the August contract with workshop pages, Learning Routes, HTML Preparation lessons and About pages, and both it and the README described the embedded Preparation viewer. `specification.md` now states the current single-page contract section by section, its acceptance criteria and the decisions that still bind. The superseded requirements, criteria and decisions are reduced to a pointer to commit `8f14d0b`, which holds the previous text, to commit `836b663` for the August installation and to tag `v0.3`. The README platform section and repository table follow the same state and no longer name covers or the embedded viewer. Every referenced path and commit was checked against the working tree and Git. Author acceptance remains separate.

### 2026-11-04 integrated · Stylesheet and published-tree cleanup

The stylesheet lost every rule that only addressed classes of the retired subpages, tutorials, workshop cards, timeline, Web Module and About page, along with four unused tokens. A computed-style comparison of both pages at 1280, 900 and 390 pixels showed no difference in any element's style or box. The unlinked workshop covers, route icons, module-00 icon and Preparation download files left `docs/`; they are preserved in git history at `e66901b`.

### 2026-11-04 integrated · Inline module index and wider column

At the author's request the separate Full Slide Deck module list left the landing page. The abstract now names the five modules in order, each with its icon and number, and links each to its video group; module 01 keeps its quoted title. The anchors `module-01` to `module-05` moved onto these terms. The content column now uses the full page width with an 80-character prose measure, and the video grid uses three columns on wide screens. Desktop, 1020, 390 and 320 pixel views were checked in English and German.

### 2026-11-04 integrated · Playlist sync and flatter material layout

The video register was compared with the public playlist. Seven new playlist entries were added under module 04 in playlist order, giving 48 entries; no register entry was missing from the playlist. Existing display titles and classifications were kept. Teaching Materials now shows its three holdings as side-by-side cards that stack on narrow viewports, without rules between the language editions. Preparation places its direct link beside the description and replaces the Google Slides iframe with a linked local image of the title slide. Desktop and narrow views were checked in a local browser; push and deployment remain with the operator.

### 2026-10-15 integrated · Bounded teaching-section proposal

The author commissioned preparation of one concrete KCE section alongside ACTIVE-WORK triage. The existing checking vocabulary was compared across German and English Full Lecture Notes, terms.md, the older CLARIAH profile and the native Full Slide Deck. Read-only Google retrieval confirmed that the German figure caption still uses Deterministic Validation beside the glossary's Technical Verification. The prepared German proposal under script/drafts connects a lecture text, slide sequence and explicit teaching scenario. INDEX.md routes to it and plan.md names the bounded acceptance. The proposal establishes no accepted terminology, cloud edit, executed edition test or publication state.

### 2026-10-15 corrected · Acceptance register after scope reduction

On the author's instruction to reconcile project knowledge, the Director Log was checked against the single-page implementation and the decisions recorded earlier today. RD-003, RD-007, RD-010, RD-014, RD-018, RD-020, RD-021 and RD-023 leave the active register because they request removed event pages, cover motifs, HTML Preparation assets or retired learning routes. Their closure records withdrawal of that scope, not substantive acceptance of their content. Existing source material and historical drafts remain available in the repository and Git.

RD-017 now identifies the current paired single-page interface. RD-008 retains the teaching-case question without the cover dependency. The plan records preparation of individual teaching sections, current permission checks and the remaining VetMed source correction. The existing repository ownership of Full material is retained, with comparison against Google versions required before conflicting content is reconciled. The action layer and design contract no longer describe unused covers as visible placeholders. No cloud permissions, publication state or teaching-content acceptance changed.

### 2026-10-15 integrated · Vertical reading flow

The author requested less horizontal layout before further interface and content work. The introduction, module index and material entries now follow one column on both language pages. Main content has a bounded width, material actions follow their descriptions, and video groups use at most two columns. Narrow material entries hide decorative marks to preserve reading width. The redundant Complete material labels are removed; this does not establish substantive acceptance of the linked material. The design contract records the change.

Verification checked balanced markup, unique identifiers, local links and fragments, JSON parsing and Git whitespace. Browser observation showed stacked content and no page overflow at measured viewport widths of 1533, 552 and 369 CSS pixels. The material anchor was activated with Enter; the English page and the return to the German preview were observed. The narrow decorative-mark rule was confirmed in computed styles and the final German screenshot. Existing focus, coarse-pointer and reduced-motion rules remain in the stylesheet and were inspected in source. A complete keyboard traversal, 200-percent zoom and renewed contrast measurements were not performed. This is a local interface revision; content acceptance and publication remain separate.

### 2026-10-15 integrated · Single-page material site

The author rejected generic arrow-back navigation and requested compact About information at the beginning of the main page. The English and German pages now integrate publisher, funding and maintenance information into the introduction. Preparation embeds its existing deck in the main page. Section navigation replaces page navigation, the separate About and Preparation HTML files are retired, and the footer retains the external legal notice and licence scope. This implements a static single-page site without a JavaScript router. HTML checks passed for both pages, including balanced elements, unique identifiers, local assets and fragment targets. Browser inspection covered the wide English entry, German language switching, Enter activation of the Preparation anchor and narrow layout without horizontal overflow. The existing viewer loaded inside the page. Browser zoom at 200 percent and a renewed contrast measurement were not performed; styles were unchanged. Content acceptance and publication remain separate.

### 2026-10-15 integrated · Shared material site and existing Preparation deck

On direct author instruction, the individual workshop listings and Learning Routes were removed from both landing pages and their event and Harness tutorial HTML pages were removed from the public tree. Workshop sources and material provenance remain available. Preparation now presents the existing Google Slides deck `19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8`, identified through Drive search and checked against its technical-setup content. The paired pages identify the deck's English language. The design, specification, project, plan, governance and action layer record the reduced public scope. Local HTML parsing verified tag balance, unique identifiers, local links and fragment targets across the remaining public pages; the data registers parse as JSON. Browser inspection confirmed the embedded Preparation deck and the reduced landing page in wide and narrow views. Teaching source folders were unchanged. This is a local implementation; publication and author acceptance remain separate.

### 2026-09-23 integrated · Cumulative edition exercise and HEDIT adaptation

The operator requested a connection between the research starter and the Agentic Edition Pipeline using the CLARIAH and musicology teaching material. Section 6.7 of the German Full Lecture Notes now supplies the maintained task prompts, with the English explanation, Full Slide Deck and Module 04 aligned. HEDIT's profile and former material stubs apply the sequence to participant data and make TEI a core outcome. The register and paired page copy reflect the sequence without releasing material actions. Prepared pipeline repositories and teiCrafter remain optional demonstrations requiring capability checks. This records an editorial integration, not a taught or executed pipeline.


### 2026-08-20 integrated · Project foundation and teaching-material contract

- **Source:** the Full Slide Deck, both Full Lecture Notes, the CLARIAH workshop material and the vault-side linking analysis.
- **Target:** `project.md`, `governance.md`, `specification.md`, `terms.md`, `plan.md` and the initial repository structure.
- **Result:** the repository became the canonical home of the teaching line. The three holdings, five modules, bilingual source-and-translation regime, workshop-specialisation model, rights boundary and taught-state tagging rule were established.

### 2026-08-20 corrected · Public instance scope and naming

- **Source:** the first register draft and the Research Director review recorded in Git before commit `8d50211`.
- **Target:** `project.md`, `CLAUDE.md`, the workshop register and material paths.
- **Result:** the public tree was restricted to upcoming workshops; delivered states remain recoverable through Git tags and history. The terms Full Slide Deck, Full Lecture Notes, material, profile and documented specialisation replaced the rejected corpus and recipe language.

### 2026-08-20 integrated · Visual system and module identity

- **Source:** four reviewed interface prototypes and the DHCraft watercolor identity.
- **Target:** `design.md`, `docs/assets/site.css`, the module icons and the initial public pages.
- **Result:** the paper-white interface, readable near-black typography, restrained turquoise interaction colour and five subject-specific module marks became the design baseline. Icons supplement text and colour without carrying meaning alone.

### 2026-08-24 integrated · KUG specialisation and bilingual workshop surface

- **Source:** the Stefan Zweig research-infrastructure decks, the KCE and Promptotyping decks, the KUG brief and the maintained workshop notes.
- **Target:** `workshops/2026-09-16-kug-m3gim/`, the register and the paired workshop pages.
- **Result:** 63 selected and adapted source slides, English Lecture Notes and a four-session research-data workflow formed the KUG specialisation. Workshop pages adopted a shared bilingual structure with overview, learning objectives, outline, material surfaces and references.

### 2026-08-25 integrated · Preparation, accessibility and public material access

- **Source:** repeated Research Director UI reviews, official product documentation and browser observations preserved in the Git history before release v0.2.
- **Target:** the paired Preparation pages, shared page chrome, Teaching Materials cards, workshop timeline and `design.md`.
- **Result:** Preparation became a scrollable Module 00 tutorial with persistent navigation, observable checks and alternative Harness paths. The public platform gained consistent language pairs, focus and skip-link behaviour, readable contrast, compact material actions, centred timeline dates, linked workshop information pages and a combined About and Imprint entry.

### 2026-08-25 corrected · Cover and material-release status

- **Source:** visual review of the generated cover series and the pre-event editorial boundary.
- **Target:** `CLAUDE.md`, cover briefs, the workshop register and landing-page cards.
- **Result:** the generated covers were retained as visible placeholders pending renewed motif approval. Workshop information pages remain accessible before events, while material actions are controlled separately by the register and rights review.

### 2026-08-25 integrated · AI Harness introductions and product evidence

- **Source:** supplied Claude Code material, official Claude Code and Codex documentation, the OpenAI Academy Codex bootcamp evidence audit and the Pi source documentation.
- **Target:** the paired Claude Code, Codex and Pi tutorials plus their source-assessment drafts.
- **Result:** the three Module 04 routes adopted one comparable sequence from goal and prerequisites through permissions and extensions to a reversible first check. Product claims remain source-grounded and dated; Pi separates harness location, provider configuration and inference location.

### 2026-08-25 integrated · Module navigation, video library and critical perspectives

- **Source:** the maintained playlist, the Full Slide Deck and Lecture Notes, Research Director module classifications and the accepted Module 05 ordering.
- **Target:** `docs/data/videos.json`, module hubs, landing pages and module notation.
- **Result:** every video received one primary module and optional related modules, every visible module marker gained a language-matched hub destination, and Module 05 closed the playlist with seven sources ordered from broad political and cybernetic frames towards specialised AGI debates.

### 2026-08-25 integrated · Web-native learning and adjacent teaching sources

- **Source:** the KUG Web Module pilot, the web-slide and deep-dive analysis, `ai-coding-literacy`, the local `ai-literacies` prototype and the VetMed source assessment.
- **Target:** `project.md`, `design.md`, `specification.md`, the KUG page pair and the landing-page learning routes.
- **Result:** Web Module, Slide Deck and Lecture Notes were assigned distinct functions. AI Coding Literacy remains an external foundation; migrated browser-native units use this repository's static design system; Research Data and Knowledge Work and the first Prompt Engineering migration remain prepared routes until their source and content gates are met.

### 2026-08-25 integrated · Research Mission Control

- **Source:** the Research Director's orchestration decision and the Research Mission Control contract.
- **Target:** `README.md`, `CLAUDE.md`, `governance.md`, `communication/` and the Research Director Log.
- **Result:** Promptotyping remained the artefact-development method, while Research Mission Control established accountable Research, Operations and bounded-lane roles. The Context Stream transports briefs and evidence; canonical project knowledge remains in `knowledge/`; substantive user contributions use stable `RD-###` identifiers.

### 2026-08-25 integrated · Release v0.2

- **Source:** Operations release result and independent Research browser observation.
- **Target:** commit `0e285e74caa83356e4481936d2e2fe31cf34fbc0`, tag `v0.2` and GitHub Pages.
- **Result:** the verified shared interface baseline, KUG Web Module, Learning Routes, licence copy, Video Library and Module 05 sequence were committed, tagged, pushed and deployed. Technical release did not constitute substantive Research Director acceptance.

### 2026-08-25 integrated · Release v0.3

- **Source:** the binding Module 00, module-hub, Harness and Curated Skills briefs; 70 final browser observations; Operations release result `operations-2026-08-25-v0-3-release-result`.
- **Target:** commit `aa4193378413a9723a2144d155b186b933229435`, annotated tag `v0.3` and GitHub Pages run `32892116537`.
- **Result:** 36 static pages in 18 English/German pairs, Module 00, five bilingual module hubs, three bilingual Harness introductions and the Module 04 Curated Skills area were formally validated, browser-observed, committed, tagged, pushed and deployed. RD-021 through RD-023 remain substantive acceptance points.

### 2026-08-25 condensed · Provenance and process documents

- **Source:** the 50-entry journal and completed release handoff preserved at commit `370d25938e740c7324a79d34668ac8b5e27f4dc0`, plus Promptotyping Journal 0.4, Index 0.4, Project 0.3, Plan 0.3, Handoff 0.1 and Domain Knowledge 0.3.
- **Target:** `README.md`, the canonical documents in `knowledge/` and the completed Research Mission Control capsule.
- **Result:** the public AI-assisted authorship statement now distinguishes ideas, editorial responsibility, AI-generated drafts and third-party sources. This journal was reduced to substantive transitions, the Handoff returned to its empty Process Inbox state, template provenance was updated, and the completed v0.3 Research and Operations exchange was closed without altering immutable messages.

### 2026-08-26 decided and installed · Simplified public learning architecture

- **Source:** direct Research Director review of the module hubs, Preparation hierarchy and landing-page Learning Routes.
- **Target:** the active `docs/` tree, `CLAUDE.md`, `project.md`, `design.md`, `specification.md`, `plan.md`, `script/COVERAGE.md` and the Research Director Log.
- **Result:** the ten bilingual subject hubs and the Module 00 framing were removed from the active public tree. The five numbered modules remain the Full Slide Deck, workshop and video classification structure. Preparation became an independent main page with a clear H1, technical learning objectives and four visibly pending slide-derived introductions. Promptotyping and Scholar-Centred Design moved to Knowledge and Context Engineering; prompt-effect evaluation was excluded as a teaching unit; Critical Perspectives and Governance stayed in the Full Slide Deck. Preparation and four compact Learning Routes now share one section after Workshops, while Research Data and Knowledge Work returns to the maintained slides instead of appearing as a separate public route. The v0.3 topology remains recoverable at tag `v0.3`; the simplified state still requires browser verification and release.

### 2026-08-26 corrected and verified · Compact public preparation surface

- **Source:** subsequent Research Director review of the landing-page module index, Preparation density, public process language and subject terminology.
- **Target:** the landing-page pair, Preparation pair, shared stylesheet, German workshop terminology and the current architecture contract.
- **Result:** the Full Slide Deck index became a non-interactive five-item overview; the explanatory architecture note and duplicate divider treatment left the public surface. Preparation now exposes six navigation destinations and four compact introduction cards without review labels or generated teaching copy. Promptotyping and Scholar-Centred Design remain assigned to Knowledge and Context Engineering, while Critical Perspectives and Governance remains exclusive to the Full Slide Deck.
- **Verification:** all 26 HTML pages form thirteen reciprocal language pairs on stylesheet version `20260826-2`; local structural checks report no duplicate IDs, broken internal destinations or fragment failures. Desktop, 640, 390 and 320 pixel browser observations report no page-level overflow or console errors. Research Director content acceptance and release remain open.

### 2026-08-31 integrated · KUG Bayreuth source exercise and Markdown deck

- **Source:** seven M³GIM Bayreuth Festival 1953 programme objects, the object-level source analysis, the checked integration workbook and the earlier 63-slide KUG presentation.
- **Target:** `workshops/2026-09-16-kug-m3gim/`, the controlled Drive prompt file and this provenance index.
- **Result:** the generic mobility exercise was replaced by a source-critical cast workflow based on daily programmes, season lists, biographies and object metadata. The exercise now models occurrences and participations, separates functions from stage roles, preserves multiple roles in one participation and keeps source-type differences visible. The repository contains the complete 63-slide English Markdown deck. The earlier Google Slides presentation remains unchanged as a visual reference.
- **Verification:** the Drive prompt file was reloaded after replacement; the deck contains 63 slide-level headings and 64 Marp separators including the metadata boundary. The supplied PDFs and reference workbook were previously inspected. The exact Gemini prompt chain, validated JSON export, full teaching rehearsal, source-reuse permission and user acceptance remain open.
