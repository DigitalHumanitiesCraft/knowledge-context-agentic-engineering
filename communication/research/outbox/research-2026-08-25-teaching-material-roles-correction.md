---
id: research-2026-08-25-teaching-material-roles-correction
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-teaching-material-roles
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/about.html
  - docs/about.de.html
  - docs/index.html
  - docs/index.de.html
  - knowledge/project.md
---

# Correction: propagate teaching-holding roles without ambiguity

The Research audit adds these required propagation points to `research-2026-08-25-teaching-material-roles`:

1. Update the shared-material paragraph in both About pages. It must state that the Full Slide Deck supplies the reference and source for workshop-specific decks, the Full Lecture Notes provide the written-out reading counterpart, and the Video Playlist provides the curated audiovisual route. Avoid wording that suggests all three holdings generate workshop slide decks in the same way.
2. Replace the current `knowledge/project.md` claim that the maintained text lives exactly once. The Full Slide Deck and Full Lecture Notes deliberately express the same maintained concepts at different levels of expansion. Define the responsible layers instead: the slide deck maintains the reference structure and workshop source selection; the lecture notes maintain the expanded explanation; shared conceptual changes must be reconciled across both.
3. Replace `complete sequence` in both Video Library leads with wording that identifies the playlist as the current maintained sequence. The playlist remains intentionally extensible.
4. Keep `docs/data/videos.json` as the current inventory. Do not add authorship fields in this release; the collection-level statement about DHCraft and selected external contributions is sufficient until individual provenance becomes a demonstrated interface need.

`knowledge/plan.md` and `knowledge/handoff.md` do not need a repeated permanent definition of the three functions. Their current-state release summaries may reference the completed distinction once.
