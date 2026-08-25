---
id: research-2026-08-25-density-hierarchy-supplement
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-copy-and-density-refinement
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/workshops/
  - docs/preparation.html
  - docs/preparation.de.html
  - docs/assets/site.css
  - knowledge/design.md
---

# Clarify hierarchy in the dense page regions

## Purpose

This supplement resolves the visual and didactic details of the density brief after three independent read-only checks of the supplied states.

## Workshop overview

Use a document hierarchy with a closer relationship to the workshop header:

1. Limit the gap between the module row and the overview to approximately 48–64 pixels.
2. Begin the overview with one fine top rule and 32–40 pixels of internal separation.
3. Place `Abstract` across the full available reading width and bound its paragraph to `var(--measure)`.
4. Place `Learning objectives` before `Outline` in the HTML and in the visual reading order. The objectives explain the intended result before the schedule explains its sequence.
5. Show the two lower sections as equal columns on wide screens and as one column on narrow screens.
6. Reduce the heading-to-content gap from the current large spacing to `var(--s2)`.

Do not use CSS `order`. DOM, visual and focus order must agree.

## References

Use one bounded reading column on every viewport. Treat the reference collection as a quiet secondary section:

- retain the section heading and all source order;
- use a fine top rule and a subtle `--tint` distinction only if body and subordinate text retain at least 4.5:1 contrast;
- keep the per-item dividers;
- bind the list to approximately 60–70 characters;
- connect the workshop backlink to the list with about 32 pixels of separation;
- remove the current large trailing void.

## Preparation footer

Keep the existing three semantic groups and make their hierarchy more balanced:

- use one quiet background distinction and one top rule for the complete footer;
- limit vertical padding to approximately 32–40 pixels;
- keep the logo in the 72–80 pixel range;
- add a concise visible group label to the navigation, translated per page;
- present its links as a compact two-column list where width permits and as one list on narrow screens;
- retain 44-pixel activation targets for coarse pointers while keeping desktop line spacing compact;
- preserve complete publisher, provenance, legal and repository information.

## Acceptance checks

1. The workshop header and overview read as one composition without a large empty band.
2. Abstract, Learning objectives and Outline have the same semantic and visual order at every viewport.
3. References are one-column, bounded and top-down readable at every viewport.
4. Footer groups have comparable visual weight and no horizontal overflow at 320 pixels.
5. Secondary text in tinted regions measures at least 4.5:1; focus indicators remain clearly visible.
6. No new card family, CSS reordering or JavaScript dependency is introduced.

