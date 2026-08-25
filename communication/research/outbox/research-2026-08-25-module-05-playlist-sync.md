---
id: research-2026-08-25-module-05-playlist-sync
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-video-module-correction
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/data/videos.json
  - docs/index.html
  - docs/index.de.html
  - knowledge/drafts/critical-perspectives-and-governance-source-map.md
  - knowledge/project.md
  - knowledge/design.md
  - knowledge/specification.md
---

# Synchronise Module 05 with the maintained playlist

## Objective and effect

Replace the temporary Module 05 empty state with the seven videos that the Research Director added to the maintained YouTube playlist. Keep one shared playlist as the external source and render Module 05 as its final thematic section in the public Video Library.

## Research Director decision

- The existing shared playlist remains the single maintained video source.
- Module 05 appears after Modules 01 through 04.
- The seven new playlist entries belong primarily to Module 05.
- The accepted Video Library card and disclosure design remains unchanged.

## Authoritative playlist delta

Append the following records in playlist order:

| Index | YouTube id | Title | Duration |
| --- | --- | --- | --- |
| 35 | `cvZW3TD2jNE` | Die geheime Steuerung, die niemand wählte – scobel im Gespräch: Mit Anna-Verena Nosthoff | `1:15:24` |
| 36 | `Hgdplv8Mde8` | Douglas Rushkoff – das Mindset der Tech-Milliardäre \| Sternstunde Philosophie \| SRF Kultur | `58:05` |
| 37 | `64xK-SEl3nA` | Matrix 2025: Gefangen in der Kalifornischen Ideologie – scobel | `33:13` |
| 38 | `QYeNESqKbSc` | Can $500 Billion Win the AI Race? \| Anton Leicht | `1:33:58` |
| 39 | `zOSptyQ3j9A` | Where AGI timelines go wrong \| Toby Ord, Oxford University | `2:46:03` |
| 40 | `31Uhv12ZLHU` | What the hell happened with AGI timelines in 2026? | `49:28` |
| 41 | `BZo-3ni4paU` | Kybernetik kurz erklärt \| 5 Fragen an Anna-Verena Nosthoff | `7:55` |

Set `module` to `05` for every appended record. Preserve the external playlist sequence through indices 1 to 41. Do not translate or editorially rewrite the source titles in the data register.

## Expected public state

The module distribution becomes `01: 5`, `02: 1`, `03: 6`, `04: 22`, `05: 7`, with 41 videos in total. Remove the temporary Module 05 empty-state copy from both landing pages. The German and English interfaces use the same seven source titles and thumbnail assets under their localised Module 05 heading.

## Write boundary

Operations may update `docs/data/videos.json`, both landing pages and only the shared CSS required to remove obsolete empty-state rules. It may update the responsible Video Library provisions in `knowledge/project.md`, `knowledge/design.md` and `knowledge/specification.md`, integrate the accepted set into `knowledge/drafts/critical-perspectives-and-governance-source-map.md`, and record the transition in `knowledge/journal.md`.

## Exclusions

- Do not create a second playlist.
- Do not duplicate a video card across module groups.
- Do not alter the accepted card layout, disclosure behaviour, module icon system or thumbnail loading contract.
- Do not change the primary assignments of entries 1 through 34.

## Verification criteria

1. The register contains 41 unique YouTube ids and the indices form the ordered sequence 1 through 41.
2. Primary module counts equal `5/1/6/22/7` for Modules 01 through 05.
3. Module 05 is the final disclosure group in both languages, reports seven videos and renders seven cards in playlist order.
4. Every card links to its corresponding YouTube id and requests the expected thumbnail without a broken image.
5. No Module 05 empty-state sentence remains in public HTML or CSS.
6. Each video renders once in each language under its primary module.
7. JSON parsing, HTML validation, local-link checks, accessibility checks and browser checks at desktop, 640, 390 and 320 pixels pass.

## Reserved decisions

The source selection and ordering are accepted. Further subdivision of Module 05 into thematic routes belongs to the later module-hub work and requires a separate content decision.
