---
id: research-2026-08-25-research-mission-control-correction
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-research-mission-control-supplement
created: 2026-08-25
requires_reply: true
canonical_refs:
  - README.md
  - CLAUDE.md
  - knowledge/project.md
  - knowledge/governance.md
  - knowledge/INDEX.md
  - knowledge/plan.md
  - knowledge/specification.md
  - knowledge/journal.md
  - communication/INDEX.md
  - communication/PROTOCOL.md
---

# Correction: smallest canonical Research Mission Control integration

This message corrects the integration boundary in `research-2026-08-25-research-mission-control-supplement`. All other objectives, method distinctions, exclusions and verification criteria in that brief remain in force.

## Corrected document set

The smallest consistent durable change set is:

- `README.md`
- `CLAUDE.md`
- `knowledge/project.md`
- `knowledge/governance.md`
- `knowledge/INDEX.md`
- `knowledge/plan.md`
- `knowledge/specification.md`
- `knowledge/journal.md`
- `communication/INDEX.md`
- `communication/PROTOCOL.md`

Apply the following corrections:

1. Leave `AGENTS.md` structurally unchanged. It already delegates the complete action contract to `CLAUDE.md`; repeating Research Mission Control there would create a second instruction source.
2. Do not install a permanent method description in `knowledge/handoff.md`. The current release handoff may name the completed integration as evidence, but it remains a process inbox rather than a method contract.
3. Add the durable `communication/` contract to `knowledge/specification.md`: it transports bounded briefs, results and recipient state between Research and Operations and never becomes a competing canonical knowledge base.
4. In `knowledge/governance.md`, resolve the existing role-name ambiguity explicitly. The Research Director holds substantive acceptance authority. The Research Orchestrator owns research framing, evidence synthesis and implementation briefs. The Operational Orchestrator owns implementation coordination, terminal verification, integration and release. Bounded subagents inherit only the authority and write boundary of their lane. If the older `Critical Expert (operator)` label is retained, define it as the Research Director's acceptance function rather than a separate person or authority.

The public About pages, footer, `knowledge/design.md` and `knowledge/terms.md` remain outside this change. They require an additional content or interface decision if Research Mission Control later becomes part of the public teaching proposition.
