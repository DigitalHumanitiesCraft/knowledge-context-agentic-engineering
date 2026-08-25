---
id: research-2026-08-25-director-log-brief
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-research-mission-control-correction
created: 2026-08-25
requires_reply: true
canonical_refs:
  - knowledge/governance.md
  - knowledge/handoff.md
  - knowledge/plan.md
  - knowledge/journal.md
  - communication/INDEX.md
  - communication/PROTOCOL.md
---

# Implementation Brief: install the Research Director Log

## Research Director decision

Research Mission Control must maintain one visible register of every contribution still required from the Research Director. This includes decisions, evaluations, acceptances, authorisations, inputs and human-only actions. Every future `What I need from you` section must be derived from this register, so requests cannot disappear in chat history, plans or handoffs.

## Canonical operational file

Create `communication/research/director-log.md`.

- The Research Orchestrator owns and updates the file.
- The Research Director supplies the requested contribution.
- Operations may propose a new point through an Operations result or question message and must not edit the log directly.
- The log is current coordination state. It never replaces durable knowledge, acceptance evidence or decision provenance.
- `communication/INDEX.md` must link the log and `communication/PROTOCOL.md` must define its lifecycle.

## Entry model

Use one section per contribution with a stable, never-reused `RD-###` identifier and these fields:

- `Type`: `Decision`, `Evaluation`, `Acceptance`, `Authorization`, `Input` or `Action`
- `Status`: `open`, `waiting` or `received`
- `Required contribution`: the smallest concrete contribution that releases the work
- `Recommendation`: Research's evidence-backed recommendation, or `Pending evidence` when one cannot yet be justified
- `Basis`: canonical files and Context Stream message identifiers
- `Effect`: the exact work, contract or state released by the contribution
- `Write-back`: the canonical document or artefact that receives the outcome
- `Trigger`: required only for `waiting` items
- `Received`: required only after an explicit Research Director response

Do not add priorities, deadlines, effort estimates or phase planning.

## Lifecycle

1. Before Research asks the Director for a contribution, the Research Orchestrator creates or updates the matching log entry.
2. One subject and one write-back target produce one entry. Additional evidence extends `Basis`; it does not create a duplicate request.
3. Silence, technical implementation and broad approval do not imply a substantive decision or acceptance.
4. An authorisation applies only to the named action and identified state.
5. A received contribution first moves to `received`. After canonical write-back and verification, remove it from the active log. Git history and `knowledge/journal.md` preserve the completed provenance.
6. Record a Decision, Acceptance or Authorization in `knowledge/journal.md` when it changes the project contract or publication state. Record Evaluations when they cause a material correction or a reasoned retention. Inputs and Actions enter the journal only when they establish a durable artefact state.
7. Before every Research brief, handoff or user-facing `What I need from you` section, reconcile the log against the current repository and remove resolved or obsolete requests through the lifecycle above.
8. When no open item is currently answerable, state this explicitly; waiting items remain visible in the log with their trigger.

## Initial register

Install the following deduplicated current contributions. Use `open` unless a waiting trigger is stated.

1. **RD-001 — Acceptance:** confirm or correct the proposed fine module cut. Write back to `script/COVERAGE.md`, module files and `knowledge/plan.md`. Recommendation: accept only after the coverage report's gaps and overlaps have been reviewed.
2. **RD-002 — Decision:** resolve the six editorial decisions recorded in `knowledge/terms.md`. Write back to that file and affected teaching material. Recommendation: decide from the maintained Full Lecture Notes wording, then propagate outward.
3. **RD-003 — Evaluation:** review the KUG and CLARIAH workshop page pairs before the remaining profiles are accepted against the same pattern. Write back to profiles, pages and, for material changes, `knowledge/journal.md`. Recommendation: use these two as the reference cases because they contain the most developed material records.
4. **RD-004 — Decision:** select any remaining compatible deltas from the supplied UI specification that should enter the platform contract. Write back to `knowledge/design.md` and `knowledge/specification.md`. Recommendation: retain only deltas that improve semantics, status clarity or accessibility without changing the accepted static architecture.
5. **RD-005 — Acceptance:** accept or revise the eleven-slide Claude Code subchapter, including the installation slide's position. Write back to `knowledge/drafts/claude-code-agentic-engineering-subchapter.md` and later the Full Slide Deck. Recommendation: keep installation as a short prerequisite bridge and reserve the conceptual sequence for agentic work.
6. **RD-006 — Authorization, waiting:** authorise specific locally produced screenshots for the Full Slide Deck. Trigger: rights-safe local screenshot candidates exist. Write back to the deck and its rights record.
7. **RD-007 — Evaluation:** accept or revise the eight cover-motif briefs. Write back to `knowledge/drafts/cover-image-prompts.md` and later cover assets. Recommendation: retain motifs that represent the workshop workflow without fabricated facsimiles or pseudo-readable source text.
8. **RD-008 — Input:** confirm the substantive VetMed case. The current material does not establish the proposed equine hoof-lamellae case. Write back to the VetMed profile and cover brief.
9. **RD-009 — Decision:** set the final public VetMed Winter School title. Write back to the register, profile and both page languages.
10. **RD-010 — Input, waiting:** provide stable anonymised screenshots for the workspace, localhost result and read-only harness check. Trigger: suitable source captures are ready. Write back to Preparation assets and pages.
11. **RD-011 — Action:** verify that both Full Lecture Notes Google Docs are publicly readable and stored in the intended Drive location. Write back to the material register and, if necessary, the Google artefacts.
12. **RD-012 — Action, waiting:** provide final Markdown and PDF releases for the Full Slide Deck and both Full Lecture Notes languages. Trigger: final source artefacts and the relevant rights check are complete. Write back to downloads, register and landing pages.
13. **RD-013 — Input:** provide the KUG source package: suitable M3GIM digitisates, confirmation of Summer School use, the reduced Mobility Studies research question and the spoken teaching language. Write back to the KUG profile, data package and teaching material.
14. **RD-014 — Authorization, waiting:** release KUG and CLARIAH material actions on the public landing pages. Trigger: the corresponding editorial material state is ready for publication. Write back to `docs/data/workshops.json` and both landing pages.
15. **RD-015 — Acceptance, waiting:** accept the CLARIAH web-slide pilot's slide cut, browser presentation and export behaviour. Trigger: the bounded rights-safe pilot is implemented and verified. Write back to the pilot and, after acceptance, the platform contract.
16. **RD-016 — Action, waiting:** tag each taught workshop state with its registered identifier. Trigger: the workshop has been delivered and its taught state verified. Write back to Git history and the workshop history record.

Do not add a separate entry for the current interface release, About integration, Research Mission Control documentation or commit and push: the Research Director has already authorised those changes. Do not restore the obsolete question about public `docs/drafts/`; the prototypes now live outside the published tree.

## Verification criteria

1. `communication/research/director-log.md` exists and contains the sixteen deduplicated entries with stable IDs and correct open or waiting states.
2. `communication/INDEX.md` exposes the log as the Director contribution register.
3. `communication/PROTOCOL.md` assigns write ownership to Research, proposal rights to Operations and contribution authority to the Research Director.
4. `knowledge/governance.md` names the log as the active control surface and `knowledge/journal.md` as the durable decision-provenance target.
5. No active Research Director request remains only in `knowledge/handoff.md`, `knowledge/plan.md` or a Context Stream message.
6. No resolved decision is duplicated permanently between the active log and the journal.
7. `git diff --check` passes and the Operations result reports the installed log path and entry count.
