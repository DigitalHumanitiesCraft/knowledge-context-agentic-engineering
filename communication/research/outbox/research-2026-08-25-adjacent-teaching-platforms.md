---
id: research-2026-08-25-adjacent-teaching-platforms
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-web-module-pilot-and-licence-copy
created: 2026-08-25
requires_reply: true
canonical_refs:
  - knowledge/drafts/adjacent-teaching-platform-integration.md
  - knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md
  - knowledge/drafts/vetmed-teaching-material-intake.md
  - knowledge/design.md
  - knowledge/specification.md
---

# Integrate adjacent DHCraft teaching platforms without merging their runtimes

## Objective and effect

Use the mature AI Coding Literacy curriculum and the local AI Literacies web prototype to extend KCE's learning routes. Preserve one canonical runtime and make source ownership visible.

## Source decisions

- `C:/Users/Chrisi/Documents/GitHub/DHCraft/ai-coding-literacy` remains an independent published curriculum. Link it as an external specialised deep dive; do not copy its dataset or runtime into KCE.
- `C:/Users/Chrisi/Documents/GitHub/DHCraft/ai-literacies` is an unversioned Astro prototype. Use its content and design patterns as research input for KCE Web Modules. Do not add Astro, npm dependencies or its root-relative route system to KCE.
- Both source folders remain read-only during this integration.

## Public integration

Add a compact `Deep Dives` or `Vertiefungen` route to the landing-page information architecture after the three teaching holdings and before the workshop timeline. The first released entry is `AI Coding Literacy`, linked to <https://digitalhumanitiescraft.github.io/ai-coding-literacy/de/> and labelled as a German-language specialised curriculum for AI-supported coding competence.

The existing local Claude Code tutorial becomes the product-specific Agentic Engineering entry in the same system. The Research Data and Knowledge Work deep dive remains visibly in preparation until its source and pilot are accepted. Do not list the local AI Literacies prototype as a public destination.

## Content migration

After the KUG Web Module component has passed its acceptance criteria, migrate the AI Literacies Prompt Engineering unit as the first reusable module-02 deep dive. Re-author its content in the KCE design system and reconcile its terms against `knowledge/terms.md`. Preserve the core content without copying the Astro component implementation.

Use the verified VetMedAI intake before migrating Tools, Multimodal, Administration Data Analysis or Research Data Analysis. Their product facts, model claims, data protection statements and rights boundaries require re-verification.

## Write boundary

Operations may update both landing pages, the shared stylesheet, `CLAUDE.md`, `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md`, `knowledge/plan.md` and `knowledge/journal.md`. A new bilingual deep-dive index page is authorised only if the landing-page cards would otherwise carry detailed descriptions; keep the first implementation compact.

## Exclusions

- No edits to either source folder.
- No import of Astro, TypeScript, `node_modules`, source CSS tokens or build configuration.
- No copied research dataset, screenshots, external slide images or video thumbnails.
- No claim that the unversioned prototype is published or canonical.
- No replacement of KCE's five modules by the seven AI Coding Literacy competencies.

## Verification criteria

1. The public AI Coding Literacy route resolves and is identified as an external German-language curriculum.
2. The Claude Code route is identified as a local product-specific deep dive.
3. The future research-data route has a clear preparation state and no dead link.
4. The landing page retains a clear hierarchy and no horizontal overflow at desktop, 640, 390 and 320 pixels.
5. KCE remains a no-build static publication without new runtime dependencies.
6. Canonical knowledge records source ownership, mapping and migration boundaries.
7. Local links, HTML validation, keyboard order, focus visibility and contrast checks pass.

