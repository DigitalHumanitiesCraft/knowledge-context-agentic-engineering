---
title: INDEX
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Index
  version: 0.4
  url: https://dhcraft.org/Promptotyping/promptotyping-document/index
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-index
status: draft
created: 2026-08-20
updated: 2026-08-25
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [project.md, specification.md, terms.md, design.md, governance.md, journal.md, plan.md, handoff.md]
---

# INDEX

This knowledge base documents the teaching-material contract, public platform, terminology, design, governance, provenance and accepted future work of *Knowledge, Context and Agentic Engineering for Knowledge Work*. It addresses the returning Research Director, reviewers and agents working under the repository action layer. Implementation artefacts stay at their repository paths, and current Research and Operations transport stays in `communication/`.

## Documents

| Path | Function | Routing question | Update trigger |
| --- | --- | --- | --- |
| `project.md` | Charter and material | What is the project, what does it maintain and where are its boundaries? | identity, scope, holdings or source boundary changes |
| `specification.md` | Specification | What must the platform and repository do, and why? | requirement, acceptance criterion or binding decision changes |
| `terms.md` | Domain knowledge | Which English and German terms and source anchors are canonical? | accepted terminology or evidence changes |
| `design.md` | Design | Which hierarchy, interaction patterns and visual values guide the interface? | accepted UI or accessibility contract changes |
| `governance.md` | Governance | Who may decide, write, verify, release and accept? | authority, provenance, rights or versioning changes |
| `journal.md` | Provenance | Which substantive transition moved from which source into which target? | integrated, rejected, corrected or condensed transitions |
| `plan.md` | Plan | Which accepted future work is next and what proves its completion? | milestone entry, exit or dependency changes |
| `handoff.md` | Process Inbox | Which received deltas still require verification or integration? | receipt or disposition of a handoff point |

## Storage zones

- `knowledge/` contains canonical Promptotyping documents.
- `knowledge/drafts/` contains decision preparation and source assessments. A draft has no canonical force until its result is written to the responsible document.
- `script/`, `slides/` and `workshops/` contain maintained teaching material and workshop specialisations.
- `docs/` contains the static public platform and its machine-readable registers.
- `communication/` transports Research Mission Control briefs, results, recipient state and completed thread capsules; it does not replace project knowledge.
- Git preserves prior wording, released states and taught workshop states.

## Reading paths

- **New task:** `project.md` → `governance.md` → the document named by the task → `handoff.md`.
- **Platform or accessibility review:** `project.md` → `design.md` → `specification.md` → current code and registers.
- **Teaching-content revision:** `project.md` → `terms.md` → the relevant Full material and workshop profile.
- **Release or acceptance:** `governance.md` → `specification.md` → `plan.md` → the Research Director Log and current Operations evidence.
- **Historical reconstruction:** `journal.md` → the referenced canonical target → Git at the cited revision.

## Research Mission Control exchange

An active Research or Operations assignment starts with `communication/PROTOCOL.md`, the applicable message and the recipient state. Required Research Director contributions are read from `communication/research/director-log.md` by stable `RD-###` identifier. Completed exchanges are condensed in `communication/capsules/` while immutable messages remain available as evidence.

## Convention

This knowledge base follows the [Promptotyping document convention](https://dhcraft.org/Promptotyping/). Each canonical document declares the current published template version where a function-specific template exists. `governance.md` follows the common Promptotyping frontmatter and routing convention because no published Governance template is currently available.

## Constitutive terms

The project distinguishes Prompt Engineering, Context Engineering, Knowledge Engineering and Agentic Engineering. Promptotyping names the artefact-development method; Research Mission Control names the orchestration contract; AI Harness names the environment that connects models, instructions, context, tools and execution. The complete bilingual terminology and its sources live in `terms.md`.
