---
id: research-2026-08-25-video-module-correction
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/data/videos.json
  - docs/index.html
  - docs/index.de.html
  - CLAUDE.md
  - knowledge/project.md
  - knowledge/design.md
  - knowledge/specification.md
---

# Correct video-module assignments and expose an honest Module 05 state

## Objective and effect

Correct two misleading primary assignments in the public Video Library. Preserve one public card per video, record cross-module relevance without duplication, and keep Module 05 visible while its new source selection is still being curated into the external playlist.

## Research Director decisions

- `Research Mission Control: Eine Forschungsleitstelle mit mehreren KI-Agenten`, YouTube id `B7TCJjcVA2k`, has primary module `04` and related module `03`.
- `Just Go Local Solves Nothing. Here's What Does`, YouTube id `-j4shkNnYVw`, has primary module `01` and related module `05`.
- Module 05 will receive a separate selection of external videos. None of those sources may enter the public inventory until it is part of the maintained external playlist.
- Write `Context Engineering` with a capital `C` in every public occurrence.

## Data contract

Retain `module` as the required primary classification in `docs/data/videos.json`. Add an optional `related_modules` array only where a documented cross-module relation exists. A video renders exactly once under its primary module. The related classification may be exposed as quiet metadata when the existing component supports it without increasing card height materially; otherwise it remains in the data and knowledge contract.

Expected primary counts after this correction are `01: 5`, `02: 1`, `03: 6`, `04: 22`, `05: 0`. The total remains 34 and playlist order remains unchanged.

## Empty state

Module 05 remains an available disclosure group with its module icon, number and title. Replace the count with zero and render this explanatory state instead of video cards.

English:

`No playlist video is currently curated primarily for this module. Cross-cutting references remain attached to their primary module.`

German:

`Derzeit ist kein Playlist-Video primär diesem Modul zugeordnet. Querbezüge bleiben am jeweiligen Primärmodul.`

Any lead that says preview images load for every module must become conditional on a group containing videos.

## Write boundary

Operations may change the two video records, both landing pages, the shared stylesheet when required for the empty state, the canonical video-library contract in `CLAUDE.md`, and the corresponding provisions in `knowledge/project.md`, `knowledge/design.md` and `knowledge/specification.md`. Correct the stale Research Mission Control mapping in `knowledge/drafts/page-copy.md` if that file still exists. Record the integrated decision in `knowledge/journal.md`.

Sweep the public HTML tree for lowercase `context engineering`. Confirm at least the known occurrences in `docs/index.html`, the HEDIT page pair and the VetMed page pair, then correct every public instance to `Context Engineering`.

## Exclusions

- Do not duplicate a card across module groups.
- Do not insert candidate Module 05 sources into `docs/data/videos.json` before the maintained external playlist contains them.
- Do not change the order, title, id or duration of any existing video.
- Do not redesign the module icon system.

## Verification criteria

1. The register contains 34 unique ids and the indices remain the ordered sequence 1 through 34.
2. Primary counts equal `5/1/6/22/0` for modules 01 through 05.
3. Both corrected records carry the specified primary and related assignments.
4. Each video card appears once in each language, under its primary module.
5. Both languages expose a meaningful Module 05 empty state without broken thumbnail requests.
6. Every public occurrence uses `Context Engineering` with a capital `C`.
7. JSON parsing, HTML validation, local-link checks, accessibility checks and browser checks at desktop, 640, 390 and 320 pixels pass.

