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
2. An organiser or programme committee checks what a taught unit covers, sees the real title slide, the audience and the linked deck.
3. A professional from a company or another discipline evaluates the extended variant and finds audience, prerequisites and scope without reading the whole corpus.
4. An agent working on the corpus reads the registry and the knowledge base to know which artefacts exist and where they live.

## Requirements

1. The start page shows the master (title, one-sentence description, the five modules, repository link) and the register of all workshop instances as cards.
2. Each workshop card shows date, title, event, audience and language, the cover image, and the links that exist; missing artefacts appear as quiet "in preparation" labels, never as dead links.
3. Each workshop has its own subpage that serves as the live course resource and as follow-up material, in six blocks: header (title, event, date, audience, cover), schedule, slides (Google Slides link plus PPTX per taught state), the script excerpt of this workshop with an EN/DE toggle, hands-on (instructions, prompts, material links), follow-up. Empty blocks are omitted per workshop.
4. The register lives as one file, `docs/data/workshops.json`; a new workshop is exactly one entry there plus one profile folder. One id scheme holds across registry, `workshops/<id>/` folders, `docs/assets/covers/<id>.png` and git tags.
5. Teaching always runs on Google Slides; the platform links the live decks and the repo holds PPTX exports per taught state under `workshops/<id>/`. An embedded viewer is optional and secondary to link plus cover.
6. Covers are the title-slide PNG per workshop, 16:9, minimum 1280 px wide, with alt text carrying title and date.
7. The site is static without a build step, plain HTML and CSS, English interface, responsive, and loads no external resources beyond Google Fonts. The script content on workshop pages is bilingual (German source, reviewed English translation).

## Acceptance criteria

- Every artefact named in the registry resolves; every `null` artefact appears as an "in preparation" label.
- The pages and the registry never contradict each other: after any registry change, the maintaining agent updates the affected pages in the same work step and verifies the match before committing.
- The site is fully readable without JavaScript.
- Covers meet the format specification; alt texts carry title and date.

## Decisions

- Registry as one JSON file instead of a frontmatter collection, because one entry per workshop is the smallest maintenance unit and machine-readable state must live in one place (2026-08-20).
- Covers as PNG exports of the real first slide, supplied by the operator, because they show the actual deck variants (2026-08-20).
- Subpage per workshop instead of a single register page, because the subpage is referenced directly in teaching and carries the course materials (operator decision 2026-08-20).
- Pages are static markup kept in sync with the registry by agents, instead of client-side rendering from JSON, because at this scale a no-JavaScript page is more robust and the sync is verifiable; revisit if the register outgrows manual sync (2026-08-20).
