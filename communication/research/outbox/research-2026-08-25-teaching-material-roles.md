---
id: research-2026-08-25-teaching-material-roles
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/index.html
  - docs/index.de.html
  - README.md
  - CLAUDE.md
  - knowledge/project.md
  - knowledge/design.md
  - knowledge/specification.md
---

# Content correction: define the roles of the three teaching holdings

## Research Director decision

Describe each teaching holding by its intended use. Module count is secondary at this point.

- The **Full Slide Deck** is a complete overview of the teaching material in slide form. It is designed for reference and supplies the source from which workshop-specific decks are assembled. It is not presented as one teaching session.
- The **Full Lecture Notes** are the written-out counterpart to the slides, carrying the explanations and context needed for reading and later reference.
- The **Video Playlist** combines DHCraft videos with selected contributions by others. Its deliberate sequence starts with foundations and progresses to more complex topics, creating a structured learning path. It is actively curated, maintained and expanded when useful material becomes available.

## Required bilingual card copy

### Full Slide Deck

English:

> A complete overview of the teaching material in one slide deck. It serves as a reference and as the source for workshop-specific decks.

German:

> Ein vollständiger Überblick über das Lehrmaterial in einem Foliensatz. Er dient als Nachschlagewerk und als Quelle für workshopspezifische Foliensätze.

### Full Lecture Notes

English:

> The written-out version of the slides, with explanations and context for reading and reference.

German:

> Die ausformulierte Fassung der Folien mit Erklärungen und Kontext zum Lesen und Nachschlagen.

### Video Playlist

English:

> A curated sequence of DHCraft videos and selected contributions by others. It begins with the foundations and progresses to more complex topics, forming a structured learning path. The playlist is continuously maintained and expanded.

German:

> Eine kuratierte Folge von DHCraft-Videos und ausgewählten Beiträgen anderer. Sie beginnt mit den Grundlagen und führt zu komplexeren Themen, sodass ihre Reihenfolge einen strukturierten Lernweg bildet. Die Playlist wird laufend gepflegt und erweitert.

## Canonical propagation

Apply the role distinction to the current-state descriptions in `README.md`, `CLAUDE.md`, `knowledge/project.md`, `knowledge/design.md` and `knowledge/specification.md`. Preserve the canonical holding names, existing links, format actions, video ordering, module mapping and workshop derivation contract. Historical journal entries remain unchanged.

The public About pages may retain their concise statement that the three holdings form the shared basis. No new About paragraph is required.

## Verification criteria

1. Both landing pages use the exact language-matched card copy above.
2. No current canonical description reduces the Full Slide Deck to a count of modules or describes it as a single workshop unit.
3. The Full Lecture Notes are consistently described as the written-out slide counterpart.
4. The playlist description names both DHCraft and selected third-party contributions, deliberate progression and continuing curation.
5. Existing resource links and actions remain unchanged.
6. `html-validate` and `git diff --check` pass.

This content decision is complete and does not remain as an open Research Director Log entry.
