---
id: research-2026-08-25-curated-agent-skills-area
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-module-00-and-module-hubs
created: 2026-08-25
requires_reply: true
canonical_refs:
  - knowledge/drafts/curated-agent-skills-library.md
  - knowledge/drafts/module-hub-architecture.md
  - docs/modules/04-agentic-engineering.html
  - docs/modules/04-agentic-engineering.de.html
---

# Add a curated Agent Skills area to Module 04

## Objective and effect

Add a dedicated curated-skills area to the Module 04 hub. The area teaches how reusable procedural packages extend an AI Harness and gives readers an inspectable route into selected external examples.

## Research Director decision

- A curated list of skills becomes its own visible area.
- Module 04 owns the area.
- Module 03 receives cross-links for skills concerned with maintained knowledge, terminology and context.
- The first external source is <https://github.com/mattpocock/skills>.

## Initial implementation boundary

Install `Curated Skills` or `Kuratierte Skills` as a dedicated subsection inside the stable `routes` section of the Module 04 page pair. Preserve the v0.3 page-count contract. Do not add a separate public page in this increment.

Render five to eight entries from the initial set in `knowledge/drafts/curated-agent-skills-library.md` as a compact semantic list. Each item shows its name, task boundary, invocation type, compatibility, review status and source link. Module relations use the existing compact icon-and-number notation.

Add a brief Module 03 cross-link to the curated list. The cross-link names the relevant knowledge and context functions without duplicating the list.

## Source status

The external repository describes small, adaptable and composable skills, distinguishes user-invoked and model-invoked forms, and documents installation for Claude Code, Codex and other agents. Treat it as an externally maintained example collection under the MIT licence. Link to source files and write original summaries. Do not copy complete skill instructions into KCE.

## Write boundary

Operations may update the Module 03 and Module 04 hub pairs when those pages are installed, the shared stylesheet, the relevant hub provisions in `knowledge/project.md`, `knowledge/design.md` and `knowledge/specification.md`, and `knowledge/journal.md`. It may add a small shared skills data register only when the HTML remains complete without JavaScript and the register removes actual duplication.

## Exclusions

- Do not install external skills into this repository.
- Do not label an entry `recommended` before its instructions, side effects and permissions have been reviewed.
- Do not use popularity as a quality signal.
- Do not reproduce the external repository as an unfiltered catalogue.
- Do not change the v0.3 public route or page-count contract.

## Verification criteria

1. Both Module 04 language versions expose the same curated entries and source statuses.
2. Each entry provides a task boundary, invocation type, compatibility, review status and source link.
3. Module 03 contains one language-matched route to the Module 04 subsection.
4. External links identify their external status and receive meaningful accessible names.
5. The list remains readable without CSS or JavaScript and creates no horizontal overflow at 320 pixels.
6. Keyboard focus, touch targets and link contrast meet the shared platform contract.
7. Source summaries remain original and the external MIT licence is recorded accurately.

## Reserved decision

A separate public Skills Library page requires evidence that the curated register has outgrown the Module 04 hub. Its route and navigation position remain open until that condition is met.
