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
- **Status**: received
- **Required contribution**: Resolve the six editorial decisions recorded in `knowledge/terms.md`. The author confirmed all six on 2026-11-05, and `knowledge/terms.md` records the confirmation. The entry leaves the log once the terminology review named in `knowledge/plan.md` has carried the wording into the Full Lecture Notes and the Full Slide Deck.
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

## RD-011 Public readability of the Lecture Notes documents

- **Type**: Action
- **Status**: open
- **Required contribution**: Verify that both Full Lecture Notes Google Docs are publicly readable and stored in the intended Drive location.
- **Recommendation**: The local verification pass of 2026-08-25 observed anonymous readability of both documents and of the Slide Deck PDF export, so the remaining question is the storage location.
- **Basis**: the `full` material entry in `data/workshops.json`, the publication-boundary entry in `knowledge/journal.md`.
- **Effect**: Confirms that the landing-page material actions resolve for readers without an account.
- **Write-back**: the material register and, where required, the Google artefacts.

## RD-012 Final Markdown and PDF releases

- **Type**: Action
- **Status**: waiting
- **Trigger**: The final source artefacts and the relevant rights check are complete.
- **Required contribution**: Provide the final Markdown and PDF releases for the Full Slide Deck and both Full Lecture Notes languages.
- **Recommendation**: Place the files under stable public paths and replace the `null` register entries in the same work step, so that register and pages never disagree. The pages announce no format that the register records as `null`.
- **Basis**: `data/workshops.json`, the acceptance criteria in `knowledge/specification.md`. The earlier folder `docs/downloads/` left the published tree on 2026-11-04.
- **Effect**: Turns the reserved Markdown and PDF positions from preparation states into resolving downloads.
- **Write-back**: a stable public path under `docs/`, the register and both landing pages.

## RD-016 Tags of taught workshop states

- **Type**: Action
- **Status**: open
- **Trigger**: Six instances have been delivered. Their profiles and the register record the delivery since commit `aa201c9`, and each profile names the commit of the state taught.
- **Required contribution**: Set the six tags below and push them, or authorise an agent session to do so. Each tag marks the last commit before the teaching days.

  ```
  git tag -a 2026-09-16-kug-m3gim 7c4a751 -m "Taught state of 2026-09-16-kug-m3gim"
  git tag -a 2026-09-25-clariah-at 836b663 -m "Taught state of 2026-09-25-clariah-at"
  git tag -a 2026-10-05-hedit-heidelberg 836b663 -m "Taught state of 2026-10-05-hedit-heidelberg"
  git tag -a 2026-10-08-fachschaft-mittelalterstudien-heidelberg 836b663 -m "Taught state of 2026-10-08-fachschaft-mittelalterstudien-heidelberg"
  git tag -a 2026-10-15-gda-goettingen 836b663 -m "Taught state of 2026-10-15-gda-goettingen"
  git tag -a 2026-11-09-ufl c8d4a66 -m "Taught state of 2026-11-09-ufl"
  git push origin --tags
  ```
- **Recommendation**: Tag the state taught and leave the delivery notes to git history. The workshop pages and the Web Module of the KUG instance exist only up to `836b663`, so a tag on a later commit would lose the route back to them. The five earlier folders can leave the tree as soon as their tags exist. The Uni for Life folder stays until the author's report has been entered into its delivery notes. Its three local workflows moved to `local-workflows/` at the repository root on 2026-11-12, after the author said that they belong in this repository, so their removal no longer depends on the folder.
- **Basis**: the versioning section of `knowledge/governance.md`, `data/workshops.json`, the delivery notes in the six profiles under `workshops/`, and `git log` for the folders, which gives `7c4a751` of 2026-08-31, `836b663` of 2026-09-23 and `c8d4a66` of 2026-11-05 as the last commits before the respective teaching days.
- **Effect**: Preserves the taught states and allows the delivered instances to leave tree and register.
- **Write-back**: the git tags. Afterwards one commit removes the tagged folders and their register entries, rewrites the source references in `knowledge/terms.md` and in `script/drafts/verification-validation-acceptance-de.md` to the last commit that held each file, and records the step in `knowledge/journal.md`.

## RD-017 Shared single-page interface

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Inspect the English and German landing pages and both glossary pages and accept their visual presentation or identify corrections.
- **Recommendation**: Review the introduction with the AI Harnesses definition, the four material cards with Preparation as a linked card, the glossary card, the module groups with their video lists and the glossary side column, each at wide and narrow widths. The page embeds no deck. The embedded Preparation deck of the 15 October state gave way to a card action on 4 November 2026.
- **Basis**: `docs/index.html`, `docs/index.de.html`, `docs/glossary.html`, `docs/glossary.de.html`, the criteria in `knowledge/specification.md` and the dated browser evidence in `knowledge/journal.md`.
- **Effect**: Records visual acceptance of the identified state. Publication has already taken place with the author's push, and teaching-content acceptance remains separate.
- **Write-back**: `knowledge/design.md` and `knowledge/journal.md`.

## RD-024 Full Slide Deck Google Slides permission

- **Type**: Action
- **Status**: open
- **Required contribution**: In the sharing dialog of the Full Slide Deck, change general access for anyone with the link from Editor to Viewer.
- **Recommendation**: Keep the document id and lower only the link permission, so that repository and page links remain stable. The named accounts with edit access are unaffected by this step.
- **Basis**: the Full Slide Deck record in `data/workshops.json`. The permission list read through the Drive connector on 2026-11-10 still gives anyone with the link the role writer, as on 2026-08-26 and 2026-11-05.
- **Effect**: Removes unintended public write access from the deck that the public page links for every reader.
- **Write-back**: the Google Slides permission state, a re-read of the permission list and `knowledge/journal.md`.

## RD-025 Verification, Validation and Acceptance teaching section

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or correct the German lecture text, the five-slide sequence and the edition exercise in `script/drafts/verification-validation-acceptance-de.md`.
- **Recommendation**: Accept the draft as reconciled on 2026-11-10 with the terminology decision of 2026-11-05. It names the three forms of checking, Technical Verification, Agentic Review and scholarly validation, followed by Acceptance, and it names schema validation explicitly as a formal check.
- **Basis**: The proposal records the local and Google source comparison of 2026-10-15, including the inconsistent caption of figure 12 and the older CLARIAH mapping, and the reconciliation of 2026-11-10 with the entries in `knowledge/terms.md`.
- **Effect**: Authorises integration of this bounded section. Other term decisions, material sections, native slide design and publication remain separate.
- **Write-back**: section 7.7 of the German Full Lecture Notes with the caption of figure 12, the corresponding section of the English notes, the slide text in `slides/full-slide-deck.md` and `knowledge/journal.md`.

## Deliberately absent

The current interface release, the About integration, the Research Mission Control documentation and the commit and push of that change set carry no entry, because the Research Director has already authorised them. The earlier question about publishing `docs/drafts/` is obsolete; the superseded prototypes are preserved in git history at `a3cd893` under `knowledge/drafts/platform-prototypes/` and never enter the published tree.
