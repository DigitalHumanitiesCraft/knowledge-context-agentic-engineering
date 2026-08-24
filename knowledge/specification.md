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
updated: 2026-08-24
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, design.md]
---

# Platform and Repo Specification

Requirements for the public platform (`docs/`, GitHub Pages) and the carrying repo structure.

## Usage scenarios

1. A participant opens the workshop page during the course, follows the embedded slides, uses the course reader and returns later to the same page for literature and reference links.
2. An organizer or program committee checks the abstract, outline and learning objectives in one view and opens the real slide deck in its embedded viewer.
3. A professional from a company or another discipline evaluates the instance aimed beyond academia and finds audience, prerequisites and scope without reading the material as a whole.
4. An agent working on the material reads the registry and the knowledge base to know which artifacts exist and where they live.

## Requirements

1. Paired English and German landing pages show the material (title, one-sentence description, the five modules, repository link) and the upcoming instances as horizontal cards, each carrying the module badges of the modules it uses.
2. Each card shows date, title, event, audience and language, the cover image, and the links that exist; missing artifacts appear as quiet "in preparation" labels, never as dead links.
3. Each registered instance has a paired English and German subpage that serves as the live course resource and as follow-up material. The compact header carries title, subtitle, date, event, audience, material language, spoken language and page licence. No cover image appears on the detail page.
4. The slide deck is the first content block. A registered Google Slides artifact appears as a native embedded viewer with a direct fallback link. A missing deck appears as an explicit preparation state in the same position.
5. One overview grid follows the slides. Its three columns carry the abstract, the ordered outline and the learning objectives. It replaces the earlier separate specialisation, sequence and module-coverage blocks.
6. The course reader follows the overview. A registered Google Doc appears as an embedded preview with a direct fallback link. A missing reader appears as an explicit preparation state. A selected literature and references section closes the content page.
7. Internal planning information, required project inputs and provenance records stay in the workshop profile and do not appear on the public page.
8. Paired English and German preparation pages hold what participants do before a course, so an instance page can point at them instead of repeating it.
9. The register lives as one file, `docs/data/workshops.json`; a new instance is exactly one entry there plus one folder. One id scheme of the form `YYYY-MM-DD-slug` holds across registry, `workshops/<id>/` folders, `docs/assets/covers/<id>.png` and git tags. The register carries only upcoming instances; a delivered one leaves both register and tree and stays reachable in git history.
10. Teaching runs on the live decks; the platform embeds and links them, and the repo holds PPTX exports per taught state under `workshops/<id>/`.
11. Covers remain available for the landing-page cards. Workshop detail pages contain no cover or motif image.
12. The site is static without a build step, plain HTML and CSS, no JavaScript required for any content, responsive, and loads no external resources beyond Google Fonts and registered Google Slides or Google Docs viewers. Published links carry no tracking or sharing parameters.

## Acceptance criteria

- Every artifact named in the registry resolves; every `null` artifact appears as an "in preparation" label.
- The pages and the registry never contradict each other. After any registry change the maintaining agent updates the affected pages in the same work step and verifies the match before committing.
- Every registered instance has an English page at `<id>.html` and a German page at `<id>.de.html`; the language control and `hreflang` metadata link the pair.
- The landing page and preparation page have English and German pairs connected through the same language control and `hreflang` metadata.
- Every workshop page contains one slide position, one overview grid, one course-reader position and one references section. It contains no cover image, module-coverage block, public project-input block or provenance block.
- Existing Google Slides and Google Docs links resolve through an embedded viewer and a visible direct link.
- The site is fully readable without JavaScript.
- Cover images on the landing page meet the format specification and carry an empty alt attribute beside text that identifies the workshop.
- No published URL carries a tracking or sharing query parameter.

## Decisions

- Registry as one JSON file instead of a frontmatter collection, because one entry per instance is the smallest maintenance unit and machine-readable state must live in one place (2026-08-20).
- Covers as PNG at 16:9 with a free upper third and no text in the image, produced by the external image pipeline, because the chrome sets the title over the image (2026-08-20).
- Paired English and German subpages per instance, because the public interface should remain accessible in both languages while teaching material keeps its documented source language (operator decision 2026-08-24, replacing the single-language page decision of 2026-08-20).
- Embedded slide deck first, followed by one three-column overview, embedded course reader and references, because these four surfaces answer the participant's immediate questions without repeating the same workshop description across several blocks (operator decision 2026-08-24).
- Workshop detail pages carry no cover image, motif, module-coverage block, project-input block or provenance block. Covers remain a landing-page register device, while operational provenance stays in the workshop profile (operator decision 2026-08-24).
- Pages are static markup kept in sync with the registry by agents, instead of client-side rendering from JSON, because at this scale a no-JavaScript page is more robust and the sync is verifiable; revisit if the register outgrows manual sync (2026-08-20).
- The platform shows only upcoming instances, because a public course platform answers what someone can attend; delivered instances stay retrievable in git history under their tag (operator decision 2026-08-20, reversing the earlier decision to present the register as the full history of the teaching line).
