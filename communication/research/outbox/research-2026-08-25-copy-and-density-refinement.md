---
id: research-2026-08-25-copy-and-density-refinement
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-teaching-material-roles-correction
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/index.html
  - docs/index.de.html
  - docs/workshops/
  - docs/preparation.html
  - docs/preparation.de.html
  - docs/assets/site.css
  - knowledge/design.md
  - knowledge/specification.md
---

# Refine playlist copy, reference lists and dense page regions

## Objective and effect

Reduce explanatory and visual density in four repeated interface regions. Preserve content while improving hierarchy, line length and scanability.

## Video Playlist copy

Supersede the longer collection-level copy from the teaching-holding roles brief. Do not name DHCraft or distinguish video authorship in this compact card description.

English:

`An ordered video sequence from foundational to advanced topics, maintained and expanded over time.`

German:

`Eine geordnete Videoreihe von den Grundlagen zu vertiefenden Themen, die laufend gepflegt und erweitert wird.`

Use the same wording wherever the compact teaching-holding description is repeated. Longer editorial provenance remains in the About and knowledge records.

## Literature and references

Render every workshop reference section as one reading column. Use one semantic list with a readable maximum line length. Each item contains the linked title followed by its concise function or description and is separated by a fine horizontal rule or equivalent spacing.

- Remove the two-column desktop layout.
- Use a maximum text measure around 72 characters.
- Keep descriptions visibly subordinate without reducing contrast below the body-text contract.
- Reduce the large gap before the workshop backlink.
- Preserve source order and every URL.

## Landing module list

Improve alignment and clickability in the current module index and carry the same geometry into the forthcoming hub links.

- Use one consistent column for icon plus number and one flexible title column.
- Align every title to the first text line of its number.
- Use balanced wrapping and a line height around 1.2.
- Give the complete row a visible focus state and coarse-pointer target of at least 44 pixels once it becomes a hub link.
- Keep enough vertical separation to distinguish rows while reducing irregular gaps caused by wrapped titles.
- Preserve all five existing module colours and icons. Module 00 remains a separately spaced neutral prerequisite when the v0.3 hub brief is implemented.

## Workshop overview hierarchy

The current `Abstract`, `Outline` and `Learning objectives` three-column row is too dense for long content. Refactor every workshop page to this reading order:

1. `Abstract` as a full-width introductory block with a bounded text measure.
2. `Outline` and `Learning objectives` as two clearly separated columns below it on wide screens.
3. A single-column order on narrow screens.

Use whitespace and a fine top rule to distinguish the two lower sections. Do not turn them into another large shaded card family. Preserve the complete text, list semantics and source order.

## Footer density

Retain the three semantic footer groups already installed, while making the footer more compact and visibly separate from the teaching content.

- Use a clear top rule or quiet background distinction.
- Reduce vertical padding and line height where it does not compromise touch targets.
- Keep the compact publisher logo.
- Keep the provenance statement to a short block.
- Allow the footer navigation to form a compact multi-column list on wide screens and a single readable list on narrow screens.
- Preserve the public Research Mission Control URL correction and all required legal and repository links.

## Write boundary

Operations may update both landing pages, all fourteen workshop pages, both Preparation pages, the Claude Code pair where shared footer markup requires it, both About pages, `docs/assets/site.css`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## Verification criteria

1. The compact playlist description in both languages matches the approved wording and contains no DHCraft authorship statement.
2. Every workshop reference section is a one-column semantic list with all original links and descriptions.
3. All module-list rows align icon, number and title consistently and retain visible focus when linked.
4. Every workshop overview places Abstract above the two-column Outline and Learning Objectives pair at wide viewports and uses one column on narrow viewports.
5. The footer remains semantically complete, uses the canonical public Research Mission Control route and occupies less vertical space than the supplied state.
6. Desktop, 1020, 860, 780, 640, 390 and 320 pixel observations show readable line lengths, no overflow and no collision.
7. Keyboard order, visible focus, 44-pixel coarse-pointer targets, heading order, HTML validation and local-link checks pass.

