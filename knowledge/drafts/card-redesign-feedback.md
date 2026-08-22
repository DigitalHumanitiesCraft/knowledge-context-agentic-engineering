# Card Redesign Feedback (operator, 2026-08-20)

Operator feedback on the workshop cards, to be applied in the next platform iteration after the current build-out lands. This supersedes the vertical card layout.

## Layout

- Horizontal card: cover image on the left, a wide information panel on the right.
- The right panel carries deeper information than the current teaser: what the workshop actually covers, so a visitor learns substance from the card itself.
- The card must make the extent of a workshop visible (how long, how deep; e.g. half-day intro vs. five-day full derivation).

## Module badges

- A badge row per card showing which of the five modules the workshop includes, using the identity colour scheme already reserved for the module marks (orange, blue, green, violet plus turquoise per `design.md`).
- A badge signals inclusion and ideally depth of coverage (e.g. full / touched / absent), so the derivation by profile becomes visible on the card.
- Modules may expose subpoints (units from the module map) on the card; some workshops list units, some do not. Keep this optional per workshop.

## Constraints

- Design system in `knowledge/design.md` holds: paper white, line-art motif, identity palette only at module marks (the badges are module marks, so the palette applies), no hairlines, max two text levels per section.
- Static markup, no client-side JSON rendering; pages stay in sync with `docs/data/workshops.json` by agents.
