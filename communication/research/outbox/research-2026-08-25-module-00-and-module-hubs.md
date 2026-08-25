---
id: research-2026-08-25-module-00-and-module-hubs
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-adjacent-teaching-platforms
created: 2026-08-25
requires_reply: true
canonical_refs:
  - knowledge/drafts/module-hub-architecture.md
  - knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md
  - knowledge/drafts/adjacent-teaching-platform-integration.md
  - knowledge/drafts/vetmed-teaching-material-intake.md
  - script/modules/
  - slides/full-slide-deck.md
  - script/full-lecture-notes-en.md
  - script/full-lecture-notes-de.md
---

# Implement Module 00 and the five bilingual module hubs

## Objective and effect

Turn the module notation into a navigable learning architecture. The existing Preparation tutorial becomes Module 00, combining workshop setup with a foundational AI Coding Literacy route. Modules 01 through 05 receive stable bilingual public hubs that connect shared concepts, learning routes, deep dives, materials, videos and workshops.

This is the next coherent milestone after the current v0.2 integration. Preserve a separate verified v0.2 commit and push before integrating this larger page-count and information-architecture change as v0.3.

## Research Director decisions

- Module 00 is `Preparation and AI Coding Literacy` or `Vorbereitung und AI Coding Literacy` and retains `preparation.html` and `preparation.de.html`.
- Module 00 is a neutral prerequisite layer. The five subject modules, workshop `modules` arrays, module colours and video primary classifications remain 01 through 05.
- Every visible module title or compact module marker links to a language-matched hub wherever that interaction does not conflict with another native control.
- Each subject module has one overview hub and can branch into deep dives, tutorials, cases and workshop Web Modules.
- Module 03 remains one umbrella module with visible Context Engineering and Knowledge Engineering tracks joined by the relation between maintained knowledge and task context.
- Module 05 exposes verification and governance together with cybernetics, political economy and automation narratives.

## Public routes

Keep the Module 00 pair at its current stable routes. Add these five pairs under `docs/modules/`:

- `01-understanding-large-language-models.html` and `.de.html`
- `02-prompt-engineering.html` and `.de.html`
- `03-knowledge-context-engineering.html` and `.de.html`
- `04-agentic-engineering.html` and `.de.html`
- `05-critical-perspectives-governance.html` and `.de.html`

The public tree grows from 22 to exactly 32 HTML files and from eleven to sixteen complete language pairs. Create no Module 00 alias inside `docs/modules/`.

Use these H1 labels:

- `Module 00 · Preparation and AI Coding Literacy`
- `Modul 00 · Vorbereitung und AI Coding Literacy`
- `Module 01 · “Understanding” Large Language Models`
- `Modul 01 · Large Language Models „verstehen“`
- `Module 02 · Prompt Engineering` and `Modul 02 · Prompt Engineering`
- `Module 03 · Knowledge and Context Engineering` and `Modul 03 · Knowledge and Context Engineering`
- `Module 04 · Agentic Engineering` and `Modul 04 · Agentic Engineering`
- `Module 05 · Critical Perspectives and Governance`
- `Modul 05 · Kritische Perspektiven und Governance`

## Shared module-hub structure

Each subject hub uses one compact document-like component, not another long catalogue of large cards.

1. Module header with icon, number, definition, learning question and no more than three learning outcomes.
2. Semantic concept map with a textual reading order and decorative connection lines.
3. Source-grounded starter sequence of five to eight compact learning panels.
4. Learning routes with compact rows for deep dives, tutorials and workshop Web Modules.
5. Teaching-material links to the Full Slide Deck and the appropriate Lecture Notes.
6. A short text list of no more than five primary-module videos with a route to the complete landing-page group.
7. A short list of no more than three representative workshops derived from the register.
8. Source and maintenance note together with previous-module, next-module and teaching-line routes.

Use the stable H2 ids `scope`, `concepts`, `routes`, `material`, `videos` and `workshops` in that order.

## Initial starter sequences

Derive public copy from the maintained slide, lecture-note and module sources. Reconcile terminology against `knowledge/terms.md` and preserve source status.

### Module 00

- workspace, files and folders;
- editor, terminal, Python and localhost;
- installing and scoping an AI Harness;
- problem decomposition and requirements;
- reading generated code, output and errors;
- testing with acceptance criteria and domain expertise.

Retain all existing Preparation anchors. Group the fourteen current steps into approximately six visible chapter bands without removing the detailed targets.

### Module 01

- what a language model produces;
- training, inference and capability boundaries;
- latent representations and jagged performance;
- multimodal models;
- black-box limits, interpretability and evidence-sensitive use.

### Module 02

- the prompt as a task contract;
- task, context, rules and output;
- examples, schemas and structured results;
- iteration and model-specific behaviour;
- evaluation and failure analysis.

### Module 03

- maintained knowledge, current task state and working context;
- Markdown, Knowledge Documents, Obsidian and canonical ownership;
- models, schemas, provenance and versioning;
- context selection, ordering and compression;
- Retrieval-Augmented Generation and retrieval failure;
- persistent instructions, Skills, Model Context Protocol resources and tool-provided context.

The concept map shows two paths, maintained knowledge through selection rules and task state through working context, meeting in task-specific context.

### Module 04

- AI Harnesses as working environments;
- tools, permissions and observable action;
- agents and agentic loops;
- Subagents, isolated context and evidence integration;
- parallel sessions, Worktrees and validation;
- Research Mission Control, acceptance and write-back.

Link the existing Claude Code tutorial as the first available product-specific route. Link the public Research Mission Control repository as a method route.

### Module 05

- evaluation, validation, scholarly verification and acceptance;
- rights, responsibility and research integrity;
- cybernetics, feedback and digital control;
- infrastructure, labour, capital and concentration;
- automation narratives and asymmetric amplification;
- critical videos, essays and literature with visible source status.

Do not populate the public Video Playlist from the Module 05 source map until the external playlist contains the accepted sources.

## Module 00 visual and component refactor

Create `docs/assets/modules/00-workspace.svg` as a neutral `currentColor` line mark following the existing 48 by 48 geometry. It depicts a workspace through a file surface and terminal line. Use `var(--ink-3)` and no subject-module colour.

Generalise the useful Preparation component logic into:

- `.learning-shell`
- `.learning-nav`
- `.learning-sequence`
- `.learning-panel`
- `.learning-visual`
- `.learning-copy`

Preserve Preparation-specific selectors only for genuine exceptions. Remove the generic dependence on near-viewport panel minimum heights. A hub panel is content-driven and compact.

## Navigation and inbound links

Keep the global navigation as `Preparation`, `About & Imprint`, `GitHub` and its German equivalent. Every Module 00 and subject-hub page receives a separate module navigation in the order 00 through 05 with exactly one current-page link.

Propagate language-matched hub links to:

- the five landing-page hero module titles;
- the 34 module markers in the seven workshop cards per language;
- the 34 module markers in the seven workshop pages per language;
- module markers inside workshop Web Module units;
- every local deep-dive parent-module mark;
- the Claude Code tutorial as a child route of Module 04.

Add one `Open module overview` or `Modulübersicht öffnen` link directly after each Video Library summary. Do not place an interactive link inside `<summary>`. Give the five groups stable ids `video-module-01` through `video-module-05`.

Keep landing ids `module-01` through `module-05` for external fragment compatibility, while internal module navigation moves to the new hubs.

## Deep-dive integration

- Module 00 links the external German AI Coding Literacy curriculum and labels its language and external status.
- Module 02 exposes the migrated Prompt Engineering lesson as `in preparation` until the static KCE version exists.
- Module 03 exposes Research Data and Knowledge Work plus Knowledge and Project Management as prepared routes with accurate status.
- Module 04 exposes Claude Code as available and Codex as in preparation.
- Module 05 exposes Evaluation and Governance as in preparation and links only source-grounded public material.

No prepared route receives a dead link. External routes identify their source and language.

## Write boundary

Operations may add the ten module-hub HTML files and the Module 00 SVG; update both landing pages, both Preparation pages, the Claude Code pair, all fourteen workshop pages, the shared stylesheet, any KUG Web Module markup already integrated, and the relevant module files. It may update `CLAUDE.md`, `knowledge/INDEX.md`, `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md`, `knowledge/plan.md`, `knowledge/handoff.md` and `knowledge/journal.md` to the installed and verified contract.

The source repositories `ai-coding-literacy` and local `ai-literacies` remain read-only.

## Exclusions

- Do not add Module 00 to workshop register arrays or `videos.json`.
- Do not import Astro, TypeScript, npm dependencies or the AI Literacies runtime.
- Do not duplicate all 34 video cards on the module hubs.
- Do not repeat workshop covers on module hubs.
- Do not use third-party slide layouts, screenshots, facsimiles or rights-unclear imagery.
- Do not make any learning content depend on JavaScript.
- Do not present prepared deep dives as released.

## Formal verification criteria

1. The public tree contains exactly 32 HTML files and sixteen complete EN/DE pairs.
2. Exactly ten hub files exist under `docs/modules/`; Module 00 has no alias there.
3. Every pair has reciprocal `hreflang`, correct `lang`, language navigation and stylesheet version.
4. Every hub has one H1 and the required H2 ids in the required order.
5. Every module navigation contains 00 through 05 in order and exactly one current-page link.
6. All compact module markers resolve to the visible number's language-matched hub.
7. Both landing pages contain five hero-hub links and five Video Library hub links.
8. Workshop cards and workshop pages each contain the expected 34 hub links per language.
9. No interactive element is nested inside a Video Library summary.
10. Module 00 appears in neither workshop module arrays nor the video classification.
11. Concept maps remain meaningful as ordered text when CSS is unavailable.
12. All core content and navigation remain available without JavaScript.
13. HTML validation, unique-id, heading-order, local-link, fragment, JSON, SVG and CSS parsing checks pass.
14. Desktop, 1020, 860, 780, 640, 390 and 320 pixel observations show no page-level overflow, hidden navigation or internal scroll trap.
15. Keyboard order matches visual order, focus is visible and coarse-pointer controls meet the 44-pixel target.
16. The public Research Mission Control route uses only `https://github.com/DigitalHumanitiesCraft/research-mission-control`.

## Research Director acceptance

Return separate acceptance sheets for RD-021 and RD-022. Module 00 is assessed for the distinction and transition between practical setup and literacy. The subject hubs are assessed once for the shared component and then by module for learning question, concept map, starter sequence and deep-dive cut.

After those checks, commit, tag, push and deployment remain separately evidenced states. Do not claim v0.3 deployed until the public Pages URLs have been checked.

