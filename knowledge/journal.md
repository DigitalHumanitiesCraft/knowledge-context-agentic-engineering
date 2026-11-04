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

### 2026-11-04 integrated · Hover and focus feedback on module and video rows

The author asked for an integrated hover effect. It is placed where the whole element is the control: a module row answers pointer hover and keyboard focus alike with a wash in its module colour that flows out of the left rule, a slight lift of the icon and a chevron in the module colour, and video rows take a faint module-coloured wash. The material cards stay without hover, since only their actions are links. The effect is pure CSS and becomes immediate under reduced motion. Focus was checked in headless Edge; no page overflow at three widths in both languages.

### 2026-11-04 integrated · UFL 2026 lecture notes on the three-session cut

The Uni for Life instance of 2026-11-09 was rebuilt around three sessions, each tied to one area and one learning goal: Prompt and Context Engineering in session 1 with the knowledge dashboard from a web search, Knowledge Engineering in session 2 with the layers of agentic engineering, permission modes, a write-blocking hook and governance on the levels of data and agent, and Agentic Engineering in session 3 with the research-tool workflow, loop engineering, determinism and quality assurance on the Northwind material. The lecture notes now follow the live deck including session 3, the permission-mode section explains when each mode fits, governance comes before the permission modes, and the session overview names both (`0fb462f`, `e2290b6`, `a3cd893`, `0a1aa70`). Several deck slides still carry the draft marker, and whether the synthetic customer e-mail returns to session 3 is open; both stay in the profile.

### 2026-11-04 integrated · Public site redesigned and knowledge base aligned

Over one day of author feedback, research and task tests the single page moved through several layouts; the iterations are in Git between `6c3b218` and `74ddcd4`, and the durable result is recorded here. The page now leads from the title and an introduction that names researchers and professionals as the audience to four material cards, Preparation on a tinted ground with an accent rule, Slides, Lecture Notes in two editions and Methods, and then to the five modules as a quieter appendix of disclosure rows with visible definitions and text video lists that link the full playlist. The page labels the holdings Slides and Lecture Notes, in German Folien and Skriptum, while the repository keeps Full Slide Deck and Full Lecture Notes. Methods groups Promptotyping, Grounded Vault and Second Brain Vault under module 03 and Research Mission Control under module 04, reusing the module icons, each with a quiet link to its video. The header keeps only the logo and the language control, the footer names development, methods and funding in two sentences, and formats not yet available are not shown.

Along the way the video register was synced with the playlist, now fifty entries, and moved with the workshop register to `data/` outside the published tree. Fonts are self-hosted and the page shows no video preview images, so it loads no external resource; a small script adds Escape and tap handling for the one inline definition and opens a module named in the fragment. The title-slide image, covers, route icons, downloads, preview code, dead styles and nineteen superseded drafts left the tree and stay in Git; four verified facts from the drafts moved to the VetMed profile, `project.md`, `design.md` and the glossary. Specification, design, project charter, `CLAUDE.md` and README describe the current page. Each step was checked in headless Edge at widths from 1440 to 320 pixels in both languages for overflow, external requests, keyboard order and fragment behaviour, and structurally for markup, links and unused styles. Real touch devices and screen readers were not tested, and publication and author acceptance remain open.

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
