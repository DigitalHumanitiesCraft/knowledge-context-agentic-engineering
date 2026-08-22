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
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, design.md]
---

# Platform and Repo Specification

Requirements for the public platform (`docs/`, GitHub Pages) and the carrying repo structure.

## Usage scenarios

1. A participant opens the workshop page during the course, follows the schedule, uses the hands-on links and prompts, and returns later to the same page as follow-up material.
2. An organizer or program committee checks what a unit covers, sees the real cover image, the audience and the linked deck.
3. A professional from a company or another discipline evaluates the instance aimed beyond academia and finds audience, prerequisites and scope without reading the material as a whole.
4. An agent working on the material reads the registry and the knowledge base to know which artifacts exist and where they live.

## Requirements

1. The landing page shows the material (title, one-sentence description, the five modules, repository link) and the upcoming instances as horizontal cards, each carrying the module badges of the modules it uses.
2. Each card shows date, title, event, audience and language, the cover image, and the links that exist; missing artifacts appear as quiet "in preparation" labels, never as dead links.
3. Each registered instance has its own subpage that serves as the live course resource and as follow-up material. It is built from the blocks header (title, event, date, audience, cover), specialisation prose, hands-on sequence, module coverage, materials (live deck and lecture notes where they exist) and provenance; a follow-up block joins when published material exists for the instance. Empty blocks are omitted per instance. The page carries the language of the material it presents, and there is no page-level EN/DE toggle.
4. A preparation page holds what participants do before a course, so an instance page can point at it instead of repeating it.
5. The register lives as one file, `docs/data/workshops.json`; a new instance is exactly one entry there plus one folder. One id scheme of the form `YYYY-MM-DD-slug` holds across registry, `workshops/<id>/` folders, `docs/assets/covers/<id>.png` and git tags. The register carries only upcoming instances; a delivered one leaves both register and tree and stays reachable in git history.
6. Teaching runs on the live decks; the platform links them and the repo holds PPTX exports per taught state under `workshops/<id>/`. An embedded viewer is optional and secondary to link plus cover.
7. Covers are PNG, 16:9, at least 1280 px wide, with the upper third free of content and no text in the image, delivered by the external image pipeline as `docs/assets/covers/<id>.png`. The cover is decorative beside the text that carries title and date, so it carries an empty alt attribute.
8. The site is static without a build step, plain HTML and CSS, no JavaScript required for any content, English interface, responsive, and loads no external resources beyond Google Fonts. Published links carry no tracking or sharing query parameters.

## Acceptance criteria

- Every artifact named in the registry resolves; every `null` artifact appears as an "in preparation" label.
- The pages and the registry never contradict each other. After any registry change the maintaining agent updates the affected pages in the same work step and verifies the match before committing.
- Every registered instance has a subpage, and every subpage has a register entry.
- The site is fully readable without JavaScript.
- Covers meet the format specification; the adjacent text carries title and date while the image alt stays empty.
- No published URL carries a tracking or sharing query parameter.

## Decisions

- Registry as one JSON file instead of a frontmatter collection, because one entry per instance is the smallest maintenance unit and machine-readable state must live in one place (2026-08-20).
- Covers as PNG at 16:9 with a free upper third and no text in the image, produced by the external image pipeline, because the chrome sets the title over the image (2026-08-20).
- Subpage per instance instead of a single register page, because the subpage is referenced directly in teaching and carries the course materials (operator decision 2026-08-20).
- Pages are static markup kept in sync with the registry by agents, instead of client-side rendering from JSON, because at this scale a no-JavaScript page is more robust and the sync is verifiable; revisit if the register outgrows manual sync (2026-08-20).
- The platform shows only upcoming instances, because a public course platform answers what someone can attend; delivered instances stay retrievable in git history under their tag (operator decision 2026-08-20, reversing the earlier decision to present the register as the full history of the teaching line).
- Language per module and per instance instead of a bilingual page toggle, because a taught instance has one language and a toggle would promise a parallel version that does not exist for every module (operator decision 2026-08-20).
