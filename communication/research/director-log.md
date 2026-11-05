# Research Director Log

Register of every contribution still required from the Research Director, covering decisions, evaluations, acceptances, authorisations, inputs and human-only actions. The Research Orchestrator owns and updates this file. The Research Director supplies the requested contribution. Operations may propose a new point through a result or question message in `communication/operations/outbox/` and does not edit the log.

The log is current coordination state. Durable project knowledge stays in `knowledge/`, and `knowledge/journal.md` receives the provenance of a contribution once it has been written back and verified. `communication/PROTOCOL.md` defines the lifecycle, and every `What I need from you` section is derived from the entries below.

Identifiers are stable and are never reused. An `open` entry can be answered now. A `waiting` entry names the required preparation. The author's scope decisions of 15 October 2026 retire event-page, cover and HTML-tutorial requests. Their disposition is recorded in `knowledge/journal.md`. Acceptance of teaching content and permissions remains separate.

## RD-001 Fine module cut

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Confirm or correct the remaining fine cut of the five Full Slide Deck modules. Promptotyping and Scholar-Centred Design are already assigned to Knowledge and Context Engineering; prompt-effect evaluation is excluded as a teaching unit.
- **Recommendation**: Accept only after the gaps and overlaps recorded in the coverage report have been reviewed.
- **Basis**: `script/COVERAGE.md`, `script/modules/`, the teaching-content sequence in `knowledge/plan.md`.
- **Effect**: Makes the module cut canonical and ends the provisional status of the module files.
- **Write-back**: `script/COVERAGE.md`, the module files and `knowledge/plan.md`.

## RD-002 Editorial term decisions

- **Type**: Decision
- **Status**: open
- **Required contribution**: Resolve the six editorial decisions recorded in `knowledge/terms.md`.
- **Recommendation**: Decide from the maintained Full Lecture Notes wording and propagate outward from there.
- **Basis**: `knowledge/terms.md`, the terminology review in `knowledge/plan.md`.
- **Effect**: Fixes canonical term wording for lecture notes, slide deck and the vault atoms.
- **Write-back**: `knowledge/terms.md` and the affected teaching material.

## RD-004 Remaining UI specification deltas

- **Type**: Decision
- **Status**: open
- **Required contribution**: Select the remaining compatible deltas from the supplied UI specification that should enter the platform contract.
- **Recommendation**: Retain only deltas that improve semantics, status clarity or accessibility while leaving the accepted static architecture intact.
- **Basis**: the interface contract in `knowledge/design.md`, `knowledge/specification.md`.
- **Effect**: Closes the audit delta and fixes which proposals are superseded.
- **Write-back**: `knowledge/design.md` and `knowledge/specification.md`.

## RD-005 Claude Code subchapter

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or revise the eleven-slide Claude Code subchapter, including the position of its installation slide.
- **Recommendation**: Keep installation as a short prerequisite bridge and reserve the conceptual sequence for agentic work.
- **Basis**: `knowledge/drafts/claude-code-agentic-engineering-subchapter.md`.
- **Effect**: Releases the subchapter into the Full Slide Deck.
- **Write-back**: the draft and afterwards `slides/full-slide-deck.md`.

## RD-006 Screenshots in the Full Slide Deck

- **Type**: Authorization
- **Status**: waiting
- **Trigger**: Rights-safe local screenshot candidates exist.
- **Required contribution**: Authorise the specific locally produced screenshots that may enter the Full Slide Deck.
- **Recommendation**: Pending evidence.
- **Basis**: `knowledge/drafts/claude-code-agentic-engineering-subchapter.md`, the rights section of `knowledge/governance.md`.
- **Effect**: Allows product screenshots in the deck under a recorded rights basis.
- **Write-back**: `slides/full-slide-deck.md` and its rights record.

## RD-008 VetMed domain case

- **Type**: Input
- **Status**: open
- **Required contribution**: Name the substantive VetMed case. The current material does not establish the proposed equine hoof-lamellae example.
- **Recommendation**: Pending evidence.
- **Basis**: the VetMed profile in `workshops/` and its source material.
- **Effect**: Establishes the domain example for the teaching material. Removed covers impose no prerequisite.
- **Write-back**: the VetMed profile and its source-based teaching material.

## RD-009 VetMed Winter School title

- **Type**: Decision
- **Status**: received
- **Required contribution**: Set the final public title of the VetMed Winter School.
- **Recommendation**: Pending evidence.
- **Basis**: `docs/data/workshops.json`, both VetMed page languages. The operator decision recorded in the vault on 2026-09-11 sets the title AI Academy for 23 to 27 November 2026, with two teaching days followed by three hackathon days.
- **Effect**: Replaces the provisional display title in register, profile and public pages.
- **Write-back**: the register, the profile and both page languages. Title, dates and instance id `2026-11-23-vetmed-ai-academy` are written back in commit `8342d11`. The page copy still describes a five-day teaching block and awaits a content revision for the two-plus-three format. The entry leaves the log once that revision and the journal entry are done.

## RD-011 Public readability of the Lecture Notes documents

- **Type**: Action
- **Status**: open
- **Required contribution**: Verify that both Full Lecture Notes Google Docs are publicly readable and stored in the intended Drive location.
- **Recommendation**: The local verification pass of 2026-08-25 observed anonymous readability of both documents and of the Slide Deck PDF export, so the remaining question is the storage location.
- **Basis**: the `full` material entry in `docs/data/workshops.json`, the publication-boundary entry in `knowledge/journal.md`.
- **Effect**: Confirms that the landing-page material actions resolve for readers without an account.
- **Write-back**: the material register and, where required, the Google artefacts.

## RD-012 Final Markdown and PDF releases

- **Type**: Action
- **Status**: waiting
- **Trigger**: The final source artefacts and the relevant rights check are complete.
- **Required contribution**: Provide the final Markdown and PDF releases for the Full Slide Deck and both Full Lecture Notes languages.
- **Recommendation**: Place the files under stable public paths and replace the `null` register entries in the same work step, so that register and pages never disagree.
- **Basis**: `docs/data/workshops.json`, `docs/downloads/`, the acceptance criteria in `knowledge/specification.md`.
- **Effect**: Turns the reserved Markdown and PDF positions from preparation states into resolving downloads.
- **Write-back**: `docs/downloads/`, the register and both landing pages.

## RD-016 Tags of taught workshop states

- **Type**: Action
- **Status**: open
- **Trigger**: A workshop has been delivered and its taught state verified. The delivery occurred for the KUG instance `2026-09-16-kug-m3gim` on 16 September 2026.
- **Required contribution**: Tag each taught workshop state with its registered identifier, now starting with the KUG instance.
- **Recommendation**: Set the tag before the folder leaves the working tree, because the register entry drops out in the same step and the tag is afterwards the only route back to the taught state.
- **Basis**: the versioning section of `knowledge/governance.md`, `docs/data/workshops.json`.
- **Effect**: Preserves the taught state and allows the delivered instance to leave tree and register.
- **Write-back**: git history and the workshop history record.

## RD-017 Shared single-page interface

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Inspect the current local English and German single pages and accept their visual presentation or identify corrections.
- **Recommendation**: Review the introduction, vertical material access, embedded Preparation deck and Video Library at wide and narrow widths.
- **Basis**: `docs/index.html`, `docs/index.de.html`, the current criteria in `knowledge/specification.md` and the dated browser evidence in `knowledge/journal.md`.
- **Effect**: Records visual acceptance of the identified local state. Teaching-content acceptance and publication remain separate.
- **Write-back**: `knowledge/design.md` and `knowledge/journal.md`.

## RD-024 Full Slide Deck Google Slides permission

- **Type**: Action
- **Status**: open
- **Required contribution**: Change the public Full Slide Deck Google Slides permission from edit access to read access and confirm the resulting anonymous view link.
- **Recommendation**: Preserve the existing document id and reduce only the public permission, so that repository and page links remain stable.
- **Basis**: the verified Drive source audit of 2026-08-26 and the Full Slide Deck material record in `data/workshops.json`.
- **Effect**: Removes unintended public write access from the canonical teaching deck.
- **Write-back**: the Google Slides permission state and `knowledge/journal.md`.

## Deliberately absent

The current interface release, the About integration, the Research Mission Control documentation and the commit and push of that change set carry no entry, because the Research Director has already authorised them. The earlier question about publishing `docs/drafts/` is obsolete; the superseded prototypes are preserved in git history at `a3cd893` under `knowledge/drafts/platform-prototypes/` and never enter the published tree.

## RD-025 Verification, Validation and Acceptance teaching section

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or correct the German lecture text, slide sequence and edition exercise in `script/drafts/verification-validation-acceptance-de.md`.
- **Recommendation**: Retain the Full Lecture Notes terminology and name schema validation explicitly as a formal check. Preserve the distinction between technical evidence, domain judgement and purpose-bound acceptance.
- **Basis**: The proposal records the local and current Google source comparison, including the inconsistent figure caption and the older CLARIAH mapping.
- **Effect**: Authorises integration of this bounded section after the identified corrections. Other term decisions, material sections, native slide design and publication remain separate.
- **Write-back**: The German Full Lecture Notes, the corresponding slide text, `knowledge/terms.md` where the decision affects its wording, and `knowledge/journal.md`.
