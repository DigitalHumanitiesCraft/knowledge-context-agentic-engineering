---
id: research-2026-08-25-mission-control-communication-style
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-director-log-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - CLAUDE.md
  - knowledge/governance.md
  - communication/PROTOCOL.md
  - communication/research/director-log.md
---

# Implementation Brief: Research Mission Control communication contract

## Research Director decision

Use the Research Mission Control style for project communication as well as orchestration. The style must make the current result, its evidential maturity, practical effect and required Director contribution immediately visible while keeping coordination overhead minimal.

Integrate this contract into `communication/PROTOCOL.md`, `knowledge/governance.md` and the compact operational rules in `CLAUDE.md`. Do not create another style document.

## Communication products

Choose the smallest product that matches the situation:

1. **Direct answer** for a bounded factual or conceptual question.
2. **Situation report** for complex active work. It states the current result, observed evidence, current action, material open points and any Director contribution.
3. **Research Director Point** when one contribution is required. It names the Director Log ID, type, smallest concrete contribution, recommendation, effect and evidence.
4. **Acceptance sheet** for a result that the Research Director can inspect and accept against explicit criteria.

## Required communication behaviour

- Lead with the current result, its scope and practical relevance.
- Distinguish explicitly between draft, active installation, formal validation, observed function, substantive review and Research Director acceptance. Claim only the stage supported by evidence.
- Name evidence close to the claim it supports. Files and technical counts appear only when they help verify or decide.
- Derive every `What I need from you` section from `communication/research/director-log.md`. Name the ID and classify the contribution as Decision, Evaluation, Acceptance, Authorization, Input or Action.
- Ask for the smallest contribution that releases the next bounded action and include an evidence-backed recommendation.
- State the action Research or Operations continues without Director input.
- Report only material progress, a changed direction, a blocker or a required contribution. Routine tool activity does not require narration.
- Keep plans, schedules, effort estimates and administrative phase language out of the communication contract.
- Limit completion claims to the verified scope and name pending substantive review, Director acceptance or canonical write-back where applicable.

## Operations result requirement

Every Operations result must map its evidence to the accepted brief criteria and distinguish implementation, validation, observed browser behaviour, commit, push and live deployment. A successful local test does not imply a pushed or deployed state.

## Verification criteria

1. `communication/PROTOCOL.md` defines the four communication products and required behaviour.
2. `knowledge/governance.md` assigns Research communication and Director Points to the Research Orchestrator and evidence-backed Operations results to the Operational Orchestrator.
3. `CLAUDE.md` contains only the compact trigger and links to the protocol instead of duplicating it.
4. The Director Log remains the only source for required Research Director contributions.
5. No new scheduling or project-management layer is introduced.
