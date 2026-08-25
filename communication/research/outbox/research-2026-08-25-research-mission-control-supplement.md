---
id: research-2026-08-25-research-mission-control-supplement
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - README.md
  - CLAUDE.md
  - AGENTS.md
  - knowledge/project.md
  - knowledge/governance.md
  - knowledge/INDEX.md
  - knowledge/plan.md
  - knowledge/handoff.md
  - knowledge/journal.md
  - communication/INDEX.md
  - communication/PROTOCOL.md
---

# Implementation Brief supplement: document Research Mission Control

## Research Director decision

This repository now uses two complementary working methods. Document both in the current release:

- **Promptotyping** is the artefact-development method. Maintained project knowledge guides iterative production, inspection and correction of teaching material, interface code and workshop packages.
- **Research Mission Control (Forschungsleitstelle)** is the orchestration contract. The Research Director sets authority and accepts substantive decisions; the Research Orchestrator frames research, evaluates evidence and issues bounded implementation briefs; the Operational Orchestrator coordinates implementation, verification, integration and release. Bounded subagent lanes work under those orchestrators.

The local `communication/` Context Stream transports current briefs, results and questions between Research and Operations. It is not a second knowledge base. Durable knowledge remains in `knowledge/`; implementation remains at its canonical repository path.

## Integration boundary

Extend Lane O2 from `research-2026-08-25-iteration-16-release-brief` to include `README.md`, `communication/INDEX.md` and `communication/PROTOCOL.md`. Keep the same Opus model requirement and the same rule that subagents do not commit or push.

Apply the method distinction at these points:

1. **`README.md`**: replace the single-method explanation with a compact `Development method and orchestration` section. Add `communication/` to the repository map. Preserve Promptotyping as the method that explains `knowledge/`; describe Research Mission Control as the coordination layer used when research and implementation run in accountable lanes. While touching the repository map, align its material architecture with the current three holdings: Full Slide Deck, Full Lecture Notes and Video Playlist.
2. **`knowledge/project.md`**: add the dual development approach to the project description. Keep the existing Promptotyping frontmatter for compatibility with the Promptotyping document type; do not replace it with a new schema.
3. **`knowledge/governance.md`**: make the Research Director the substantive authority and distinguish the Research Orchestrator, Operational Orchestrator and bounded subagents. Record that only accepted briefs authorise Operations writes and that terminal integration remains with the Operational Orchestrator.
4. **`knowledge/INDEX.md`**: route new agents to `communication/PROTOCOL.md` only when they participate in an active Research/Operations exchange. Preserve `knowledge/` as the canonical project-memory entry point.
5. **`CLAUDE.md` and `AGENTS.md`**: add a short routing rule for delegated Research Mission Control work. Agents must read the applicable Context Stream message and respect its authority, write boundary, exclusions and verification criteria. Do not duplicate the full protocol.
6. **`communication/INDEX.md` and `communication/PROTOCOL.md`**: name the exchange as the repository's Research Mission Control transport and state its relation to Promptotyping and canonical knowledge. Preserve endpoint ownership, immutable published messages and recipient-owned state cursors.
7. **`knowledge/plan.md`, `knowledge/handoff.md` and `knowledge/journal.md`**: record the adopted orchestration model and the installed Context Stream at current-state locations. Retain older entries as historical provenance.

## Exclusions

- Do not create another general method manual in this repository.
- Do not copy durable project knowledge into `communication/`.
- Do not turn the orchestration model into scheduling, effort planning or administrative reporting.
- Do not change the public teaching-platform UI for this documentation decision.
- Do not modify the external Promptotyping repository or the Obsidian vault from this task.

## Verification criteria

The supplement is complete when:

1. `README.md` names and distinguishes both methods and maps `communication/`.
2. The role names and authority are consistent across `knowledge/governance.md`, `CLAUDE.md`, `AGENTS.md` and `communication/PROTOCOL.md`.
3. No current document describes all agents generically where the Research/Operations distinction controls authority.
4. `communication/` is described as transient transport; `knowledge/` remains canonical project memory.
5. The Promptotyping frontmatter and document-type links remain valid.
6. Existing Context Stream ownership and immutability rules remain unchanged.
7. `git diff --check` passes and the final Operations result names this supplement as integrated or reports an exact deviation.
