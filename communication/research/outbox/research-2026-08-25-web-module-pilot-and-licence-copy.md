---
id: research-2026-08-25-web-module-pilot-and-licence-copy
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/data/workshops.json
  - docs/index.html
  - docs/index.de.html
  - docs/workshops/2026-09-16-kug-m3gim.html
  - docs/workshops/2026-09-16-kug-m3gim.de.html
  - workshops/2026-09-16-kug-m3gim/profile.md
  - workshops/2026-09-16-kug-m3gim/lecture-notes.md
  - knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md
---

# Install the first integrated Web Module and simplify licence copy

## Objective and effect

Make the workshop detail page the primary browser-native teaching surface. The Web Module lives inside the existing workshop URL, while Google Slides remains the editable presentation surface and Lecture Notes remain the expanded reading form. The first bounded implementation uses the KUG workshop pair and establishes a reusable component for later workshop profiles.

## Research Director decisions

- Public cards show only the linked label `CC BY 4.0`. Remove `page and original text` and `Seite und eigener Text` from the card interface.
- Keep the exact licence scope in the register, governance and the About rights explanation.
- The workshop page itself hosts the Web Module. Do not create a second KUG application URL for the same learning sequence.
- Preserve the existing Slide Deck and Lecture Notes sections as supplementary surfaces after the Web Module.

## Three-surface contract

| Surface | Function |
| --- | --- |
| Web Module | Primary browser-native learning sequence with internal navigation, explanatory panels, original diagrams and observable checks. |
| Slide Deck | Editable presentation and workshop-delivery surface. |
| Lecture Notes | Expanded explanation for reading, reference and later review. |

Google artifacts remain linked and embedded where verified. A Vault workshop document or repository profile supplies research context and editorial provenance; it is not exposed as a fourth public material type.

## KUG pilot structure

Insert `Web Module` or `Web-Lernmodul` between the workshop overview and the Slide Deck on both KUG pages. Reuse the Preparation page's successful pattern of persistent internal navigation, ordinary vertical scrolling, one explanatory text area and one original schematic per unit. Use dedicated component classes so that tutorial-specific CSS remains independent.

The sequence follows the verified four-session profile.

1. **From estate object to research platform.** Trace digitisation, description, structured representation, authority data, repository ingest and publication as distinct transformations.
2. **Where language models can assist.** Locate model-supported tasks inside the research-data workflow and state the evidence and checks required for each task.
3. **From source to checked structured data.** Separate source image, transcription and extracted representation; record provenance, uncertainty and source relations.
4. **From research question to browser application.** Translate a bounded question and checked data into requirements, views, tests and a small Promptotyping artefact.
5. **Verification and responsible acceptance.** Distinguish deterministic validation, source-based scholarly verification and the decision that assigns a result its research status.

Each unit exposes its related module numbers through the existing accessible icon notation. The text must be newly written from the repository profile and Lecture Notes. Do not copy third-party slide layouts, screenshots or facsimiles. Use rights-safe HTML/CSS diagrams or synthetic file and data states.

## Register contract

Add a workshop-level `web_module` record with an explicit status. The pilot uses `available`; all other workshops use `in_preparation` until their source audit and content sequence are complete. Do not infer availability from the existence of a detail page.

The current upcoming-card release state remains separate. A muted card may still link through its title to the information page, while material actions follow the existing `materials_status` publication contract.

## Write boundary

Operations may update the workshop register, both landing pages for the simplified licence label and any status copy derived from the new data contract, both KUG workshop pages, the shared stylesheet, `CLAUDE.md`, `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md`, `knowledge/plan.md` and `knowledge/journal.md`.

## Exclusions

- Do not claim that all seven workshops already have verified Google Slides and Lecture Notes links. A separate Research source audit is in progress.
- Do not create placeholder external links.
- Do not publish Vault paths or private Drive locations.
- Do not turn the Web Module into an iframe around Google Slides or Docs.
- Do not remove the existing Slide Deck or Lecture Notes embeds from the KUG page.
- Do not expose source facsimiles or participant data.

## Verification criteria

1. Every landing-page workshop card shows only `CC BY 4.0` as its licence UI.
2. The register retains the exact `page-and-original-text` scope.
3. Both KUG language pages expose the same five-unit Web Module before Slide Deck and Lecture Notes.
4. Internal module navigation reaches every unit and remains usable by keyboard.
5. Every unit has an accessible heading, module association, explanatory content and a rights-safe original schematic or structured text visual.
6. The Web Module works without JavaScript and does not depend on an external embed.
7. Desktop, 640, 390 and 320 pixel checks show no internal scroll traps or horizontal overflow.
8. All existing Google Slide, PDF and Lecture Notes links continue to resolve.
9. HTML validation, unique-id checks, heading-order checks, local-link checks and contrast checks pass.

## Next-milestone boundary

Research will return a verified source matrix for the other six workshops. Extend the Web Module component only where the corresponding profile, Vault context and Google artifacts support a coherent learning sequence. Unknown sources remain explicitly in preparation.

