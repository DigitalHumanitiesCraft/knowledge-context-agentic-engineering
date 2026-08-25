---
id: research-2026-08-25-harness-introduction-routes
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-module-00-and-module-hubs
created: 2026-08-25
requires_reply: true
canonical_refs:
  - knowledge/drafts/harness-introduction-routes.md
  - knowledge/drafts/harness-route-icon-system.md
  - docs/tutorials/claude-code.html
  - docs/tutorials/claude-code.de.html
  - knowledge/drafts/codex-bootcamp-101-evidence.md
---

# Complete the AI Harness introduction routes

## Objective and effect

Separate foundational AI Coding Literacy from product-specific AI Harness instruction and complete a comparable set of bilingual introductions for Claude Code, Codex and Pi with a local model route.

## Research Director decision

- AI Coding Literacy remains the general Module 00 foundation and receives a neutral literacy icon.
- Claude Code, Codex and Pi are sibling product-specific routes under Module 04.
- Pi is presented as the open-source harness route with an explicit local-model configuration and verification boundary.
- Every route receives its own original line icon. Third-party logos are not copied.

## Public routes

Retain the available Claude Code pair and add:

- `docs/tutorials/codex.html`
- `docs/tutorials/codex.de.html`
- `docs/tutorials/pi.html`
- `docs/tutorials/pi.de.html`

This correction changes the v0.3 page-count contract from 32 to 36 HTML files and from sixteen to eighteen complete language pairs. The ten Module Hub files remain unchanged.

## Landing-page learning routes

Refactor the current Deep Dives row into one compact learning-routes section with three semantic groups.

1. Foundation contains AI Coding Literacy.
2. AI Harness introductions contains Claude Code, Codex and Pi with a local model.
3. Research workflow contains Research Data and Knowledge Work.

Use the icon assets under `docs/assets/routes/` when the asset lane returns. Preserve ordinary links, accurate route status and the current compact card density. The product name is visible text and provides the accessible name; decorative icons use an empty alternative or `aria-hidden="true"` according to their embedding.

## Tutorial contract

Reuse the installed Claude Code tutorial component and sidebar behaviour. Each tutorial must expose the eight-step comparable sequence in `knowledge/drafts/harness-introduction-routes.md`, while preserving product-specific terminology and current official installation sources.

Codex content uses current official OpenAI documentation and the maintained OpenAI Academy bootcamp source. Pi content uses its official repository and documentation. Installation commands, supported integrations and product capabilities carry a visible last-checked date. No volatile product claim is inferred from a third-party video alone.

The Pi tutorial must distinguish three facts explicitly: the harness source is open, the selected model provider is configured separately, and model inference is local only when the configured endpoint and observed network or process state establish that condition.

## Module integration

- Module 00 links AI Coding Literacy and the comparison route to the three Harness introductions.
- Module 04 lists all three tutorials in its `routes` section and links the curated Skills area.
- Module 03 cross-links only the parts concerned with persistent instructions, Skills, project knowledge and context selection.
- The global top navigation remains Preparation, About and Imprint, and GitHub. Product tutorials remain subordinate routes.

## Write boundary

Operations may add the four tutorial pages, integrate the new route icons, update both landing pages, the Preparation pair, the Module 03 and Module 04 hub pairs, the shared stylesheet, `CLAUDE.md`, `README.md`, and the responsible provisions in `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md`, `knowledge/plan.md`, `knowledge/handoff.md` and `knowledge/journal.md`.

## Exclusions

- Do not present AI Coding Literacy as a Claude Code course.
- Do not copy official product logos or use colour alone to identify a harness.
- Do not claim that Pi keeps inference local without an explicit local endpoint and an observable check.
- Do not duplicate the complete Curated Skills list on each product page.
- Do not make core tutorial content depend on JavaScript.

## Verification criteria

1. The public tree contains exactly 36 HTML files and eighteen reciprocal EN/DE pairs after the v0.3 integration.
2. Claude Code, Codex and Pi use the same tutorial landmarks and comparable sequence while retaining accurate product terminology.
3. Both landing pages contain the same five learning routes in the three named groups and every available route resolves locally.
4. Module 00, Module 03 and Module 04 expose the specified language-matched links without duplicating content.
5. Every product-specific installation or capability claim resolves to a current primary source and carries the recorded check date.
6. The Pi page states and tests the harness, provider and inference-location boundaries separately.
7. Icons parse as SVG, remain legible at 24 and 48 pixels, inherit `currentColor` and have no embedded raster data.
8. The complete route remains readable without CSS or JavaScript, creates no horizontal overflow at 320 pixels and has visible keyboard focus with 44-pixel coarse-pointer targets.
9. HTML validation, reciprocal-language, local-link, fragment, heading-order, unique-id, JSON, SVG and CSS checks pass.
10. Browser observation passes at desktop, 1020, 860, 780, 640, 390 and 320 pixels.

## Research Director acceptance

Extend RD-022 to cover the Module 04 route placement. Add a separate waiting acceptance point for the common Harness tutorial component and the accuracy of the Pi local-model boundary after all three pages have been technically verified.
