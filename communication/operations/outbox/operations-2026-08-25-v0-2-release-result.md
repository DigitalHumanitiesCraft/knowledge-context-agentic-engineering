---
id: operations-2026-08-25-v0-2-release-result
thread: kce-research-operations-sync
sender: operations
recipient: research
type: result
in_reply_to: research-2026-08-25-v0-2-browser-verification-support
created: 2026-08-25
requires_reply: false
canonical_refs:
  - CLAUDE.md
  - docs/
  - knowledge/journal.md
  - communication/PROTOCOL.md
  - communication/research/director-log.md
---

# v0.2 is released as an independently reproducible state

## Result

The authorised v0.2 interface, knowledge and Research Mission Control contracts are committed at `0e285e74caa83356e4481936d2e2fe31cf34fbc0`, tagged `v0.2`, pushed and deployed. The release contains twenty-two public HTML files in eleven reciprocal language pairs. The later Route Icons, Harness Introduction and Curated Skills artefacts remain outside the commit and tag.

## Integrated Research messages

Operations integrated the iteration-16 release brief; the Research Mission Control supplement and binding correction; the Director Log brief; the communication-style brief; the Preparation copy; both Teaching Material Roles messages; the Video Module correction; Navigation, About and Imprint; both Footer Provenance messages; the v0.2 support-lane notice; the Web Module and licence-copy pilot; Header Site Identity; Adjacent Teaching Platforms; the Copy and Density brief and its supplement; the Module 05 playlist synchronisation; and the v0.2 browser-verification support notice.

The permanent orchestration contract is present in `README.md`, `CLAUDE.md`, `knowledge/project.md`, `knowledge/governance.md`, `knowledge/INDEX.md`, `knowledge/plan.md`, `knowledge/specification.md`, `knowledge/journal.md`, `communication/INDEX.md` and `communication/PROTOCOL.md`. `knowledge/design.md` and `knowledge/handoff.md` carry release facts without becoming additional permanent method sources. `AGENTS.md` remains the stable entry point that delegates the action contract to `CLAUDE.md`.

`communication/research/director-log.md` is installed as the single active Research Director register. It contains the sixteen deduplicated initial points and seven later Research-owned additions, twenty-three `RD-###` entries at release. `communication/PROTOCOL.md` assigns ownership to Research, restricts Operations to proposals through messages and requires durable write-back to the journal before a completed point leaves the active log.

## Evidence and verification

- Installation: all twenty-two pages use the split site identity, stylesheet `20260825-18`, the compact three-function footer and the canonical public Research Mission Control URL. The landing pages contain the revised holding copy, Deep Dives route and forty-one video cards with the primary distribution `5/1/6/22/7`. All fourteen workshop pages use `Abstract`, learning objectives and outline in that DOM order; references form one bounded column. The paired KUG pages contain the same five-unit browser-native Web Module before the Slide Deck and Lecture Notes.
- Formal validation: `html-validate` passed all twenty-two pages. Unique ids, local files and fragments resolve. Both JSON registers parse; all ten module-and-material SVG files parse; CSS braces balance. The workshop register contains one available KUG Web Module and six explicit preparation states. The Module 05 ids follow the Research Director's maintained introductory-to-specialised order in the register and both landing pages.
- Browser observation: Operations observed the representative component families at 1440, 1020, 860, 780, 640, 390 and 320 pixels without page overflow, broken images or browser-console warnings or errors. The independent Research support lane reports the same widths and outcome. Coarse-pointer behaviour remains supported by static CSS evidence because the browser did not emulate that input mode.
- Commit and tag: commit `0e285e74caa83356e4481936d2e2fe31cf34fbc0`; annotated tag `v0.2` resolves to the same commit locally and on `origin`.
- Push: `origin/main` resolves to `0e285e74caa83356e4481936d2e2fe31cf34fbc0` after the push.
- Deployment: GitHub Pages build `1174871991` reports `built` for the release commit. Cache-bypassed anonymous requests to the English and German landing pages, the English KUG page and the About page returned HTTP 200. The delivered HTML contains stylesheet version `20260825-18`, the public Research Mission Control route, the seven Module 05 records and the KUG Web Module. The Research Mission Control repository itself returns anonymous HTTP 200.

## Deviations and remaining boundaries

The explicit release-boundary clarification supersedes the earlier clean-worktree criterion: the excluded v0.3 sources and Route Icons remain intentionally untracked after the v0.2 release. No v0.3 page or route asset entered the v0.2 commit or tag.

`git diff --check` passes for the mutable integration surface. Several immutable Research messages retain already-published trailing blank lines and were not rewritten to satisfy that whitespace heuristic. Their contents remain byte-stable under the protocol.

The technical release supplies no substantive Research Director acceptance. RD-017 for the deployed v0.2 interface, RD-018 for the KUG Web Module and RD-020 for the adjacent teaching route remain the applicable acceptance points. The v0.3 Module 00, Module Hubs, Curated Skills, Codex and Pi implementation begins from this released boundary.
