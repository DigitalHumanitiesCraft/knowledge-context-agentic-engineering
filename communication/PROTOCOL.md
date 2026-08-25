# Research Mission Control Context Stream Protocol

This local two-context stream transports bounded briefs, results, questions and recipient state between Research and Operations. It is the transport layer of Research Mission Control. Promptotyping remains the artefact-development method, maintained project knowledge remains in `knowledge/`, and implementation artefacts remain at their canonical repository paths. A message can establish an assignment or report evidence, but it does not become a competing knowledge base.

## Roles and authority

- The Research Director holds substantive decision and acceptance authority.
- The Research Orchestrator frames research, evaluates evidence and issues bounded implementation briefs.
- The Operational Orchestrator coordinates authorized implementation, terminal verification, integration and release.
- Bounded subagents inherit only the authority, write boundary, exclusions and verification criteria stated for their lane.

## Rules

- Research writes new messages only to `communication/research/outbox/`.
- Operations writes new messages only to `communication/operations/outbox/`.
- Published messages are immutable. A correction is a new message that names the superseded message.
- Each recipient updates only its own `state.md`, after processing a message successfully.
- Every message keeps one stable `thread` identifier and references canonical files instead of copying durable project knowledge.
- Operations writes repository artefacts only under an accepted brief or direct Research Director instruction. Terminal integration remains with the Operational Orchestrator.
- The shared filesystem transports messages but does not wake another Codex task. Direct task messaging or later re-entry supplies notification.

## Message shape

```yaml
id: <role>-<date>-<slug>
thread: <stable-thread-id>
sender: <research|operations>
recipient: <research|operations>
type: <brief|result|question|notice>
in_reply_to: <message-id|null>
created: <observed ISO-8601 date or datetime>
requires_reply: <true|false>
canonical_refs:
  - <repository-relative path or revision>
```

Research sends an Implementation Brief containing the objective, canonical sources, authority, write boundary, exclusions, expected result, verification criteria and decisions reserved for the Research Director. Operations returns the actual result, inspectable evidence, verification performed, deviations, integration state and the next required action. Transport state, implementation state, verification and substantive acceptance remain separate statements.

## Research Director Log

`communication/research/director-log.md` is the single register of contributions required from the Research Director. The Research Orchestrator owns and updates it. Operations proposes a new point through a result or question message and never edits the log. The Research Director supplies the contribution itself.

One subject with one write-back target produces one entry under a stable, never-reused `RD-###` identifier. Further evidence extends the `Basis` field of that entry. An entry carries its type, status, smallest concrete contribution, recommendation or `Pending evidence`, basis, effect and write-back target; a `waiting` entry additionally names its trigger. The log carries no priorities, deadlines, effort estimates or phase planning.

A received contribution first moves to `received`. After canonical write-back and verification it leaves the active log, and git history together with `knowledge/journal.md` preserves the completed provenance. A decision, acceptance or authorisation enters `knowledge/journal.md` when it changes the project contract or the publication state; an evaluation enters it when it causes a material correction or a reasoned retention; inputs and actions enter it when they establish a durable artefact state.

Silence, technical implementation and broad approval do not constitute a substantive decision or acceptance. An authorisation covers only the named action and the identified state. Before every brief, handoff or `What I need from you` section, the log is reconciled against the current repository and resolved or obsolete requests are removed through this lifecycle. When no open item is currently answerable, the communication says so, and waiting items remain visible with their trigger.

## Communication contract

The same contract governs project communication and orchestration. Choose the smallest product that matches the situation.

1. **Direct answer** for a bounded factual or conceptual question.
2. **Situation report** for complex active work, stating the current result, observed evidence, current action, material open points and any required Director contribution.
3. **Research Director Point** when one contribution is required, naming the Director Log identifier, type, smallest concrete contribution, recommendation, effect and evidence.
4. **Acceptance sheet** for a result that the Research Director can inspect and accept against explicit criteria.

Required behaviour:

- Lead with the current result, its scope and its practical relevance.
- Distinguish draft, active installation, formal validation, observed function, substantive review and Research Director acceptance, and claim only the stage the evidence supports.
- Name evidence next to the claim it supports. Files and technical counts appear where they help verification or a decision.
- Derive every `What I need from you` section from the Director Log, name the identifier and classify the contribution as Decision, Evaluation, Acceptance, Authorization, Input or Action.
- Ask for the smallest contribution that releases the next bounded action and supply an evidence-backed recommendation.
- State the action Research or Operations continues without Director input.
- Report material progress, a changed direction, a blocker or a required contribution. Routine tool activity stays unnarrated.
- Keep plans, schedules, effort estimates and administrative phase language out of the exchange.
- Limit a completion claim to the verified scope and name pending substantive review, Director acceptance or canonical write-back where they apply.

Every Operations result maps its evidence to the criteria of the accepted brief and reports installation, formal validation, observed browser behaviour, commit, push and live deployment as separate statements. A successful local check does not imply a pushed or deployed state.
