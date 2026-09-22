# Research Director Log

Register of every contribution still required from the Research Director, covering decisions, evaluations, acceptances, authorisations, inputs and human-only actions. The Research Orchestrator owns and updates this file. The Research Director supplies the requested contribution. Operations may propose a new point through a result or question message in `communication/operations/outbox/` and does not edit the log.

The log is current coordination state. Durable project knowledge stays in `knowledge/`, and `knowledge/journal.md` receives the provenance of a contribution once it has been written back and verified. `communication/PROTOCOL.md` defines the lifecycle, and every `What I need from you` section is derived from the entries below.

Identifiers are stable and are never reused. An `open` entry can be answered now. A `waiting` entry names the trigger that has to occur first. Twenty-two entries are current, fifteen of them open, one received and six waiting. RD-022 left the active log after the subject-hub topology was withdrawn by Research Director decision on 26 August 2026. RD-013 left it as obsolete once the KUG workshop had taken place on 16 September 2026.

## RD-001 Fine module cut

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Confirm or correct the remaining fine cut of the five Full Slide Deck modules. Promptotyping and Scholar-Centred Design are already assigned to Knowledge and Context Engineering; prompt-effect evaluation is excluded as a teaching unit.
- **Recommendation**: Accept only after the gaps and overlaps recorded in the coverage report have been reviewed.
- **Basis**: `script/COVERAGE.md`, `script/modules/`, work package 2 in `knowledge/plan.md`.
- **Effect**: Makes the module cut canonical and ends the provisional status of the module files.
- **Write-back**: `script/COVERAGE.md`, the module files and `knowledge/plan.md`.

## RD-002 Editorial term decisions

- **Type**: Decision
- **Status**: open
- **Required contribution**: Resolve the six editorial decisions recorded in `knowledge/terms.md`.
- **Recommendation**: Decide from the maintained Full Lecture Notes wording and propagate outward from there.
- **Basis**: `knowledge/terms.md`, work package 6 in `knowledge/plan.md`.
- **Effect**: Fixes canonical term wording for lecture notes, slide deck and the vault atoms.
- **Write-back**: `knowledge/terms.md` and the affected teaching material.

## RD-003 Reference workshop pages

- **Type**: Evaluation
- **Status**: open
- **Required contribution**: Review the KUG and CLARIAH workshop page pairs before the remaining profiles are accepted against the same pattern.
- **Recommendation**: Use these two as the reference cases, because they carry the most developed material records.
- **Basis**: `docs/workshops/2026-09-16-kug-m3gim.html`, `docs/workshops/2026-09-25-clariah-at.html` with their German pairs and the matching `workshops/<id>/profile.md`.
- **Effect**: Establishes the accepted workshop page pattern for the five remaining profiles.
- **Write-back**: the workshop profiles and pages; a material change additionally enters `knowledge/journal.md`.

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

## RD-007 Cover motif briefs

- **Type**: Evaluation
- **Status**: open
- **Required contribution**: Accept or revise the eight cover-motif briefs.
- **Recommendation**: Retain the motifs that carry the workshop domain through one object and remove every fabricated facsimile and pseudo-readable source surface.
- **Basis**: `knowledge/drafts/cover-image-prompts.md`, the placeholder files in `docs/assets/covers/`.
- **Effect**: Releases cover regeneration; the current files remain visible placeholders until then.
- **Write-back**: `knowledge/drafts/cover-image-prompts.md` and later the cover assets.

## RD-008 VetMed domain case

- **Type**: Input
- **Status**: open
- **Required contribution**: Name the substantive VetMed case. The current material does not establish the proposed equine hoof-lamellae example.
- **Recommendation**: Pending evidence.
- **Basis**: the VetMed profile in `workshops/`, `knowledge/drafts/cover-image-prompts.md`.
- **Effect**: Unblocks the VetMed motif and the domain example inside the profile.
- **Write-back**: the VetMed profile and its cover brief.

## RD-009 VetMed Winter School title

- **Type**: Decision
- **Status**: received
- **Required contribution**: Set the final public title of the VetMed Winter School.
- **Recommendation**: Pending evidence.
- **Basis**: `docs/data/workshops.json`, both VetMed page languages. The operator decision recorded in the vault on 2026-09-11 sets the title AI Academy for 23 to 27 November 2026, with two teaching days followed by three hackathon days.
- **Effect**: Replaces the provisional display title in register, profile and public pages.
- **Write-back**: the register, the profile and both page languages. Title, dates and instance id `2026-11-23-vetmed-ai-academy` are written back in commit `8342d11`. The page copy still describes a five-day teaching block and awaits a content revision for the two-plus-three format. The entry leaves the log once that revision and the journal entry are done.

## RD-010 Preparation screenshots

- **Type**: Input
- **Status**: waiting
- **Trigger**: Suitable source captures are ready.
- **Required contribution**: Supply the three stable anonymised screenshots for the workspace, the localhost result and the read-only harness check.
- **Recommendation**: Capture all three states in one anonymised session, so that the language-matched captions and checks describe one consistent environment.
- **Basis**: the preparation section of `knowledge/design.md` with the file names `prep-01-workspace.webp`, `prep-02-localhost.webp` and `prep-03-harness-scope.webp`, `docs/preparation.html`, `docs/preparation.de.html`.
- **Effect**: Replaces the schematic interface diagrams in both Preparation languages while their captions and checks stay in place.
- **Write-back**: the preparation image assets and both Preparation pages.

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

## RD-014 Public material release for KUG and CLARIAH

- **Type**: Authorization
- **Status**: waiting
- **Trigger**: The corresponding editorial material state is ready for publication.
- **Required contribution**: Release the KUG and CLARIAH material actions on the public landing pages.
- **Recommendation**: Change the register and both landing-page languages in one work step, because the acceptance criteria require register and pages to agree at every commit.
- **Basis**: `docs/data/workshops.json`, `docs/index.html`, `docs/index.de.html`.
- **Effect**: Turns two muted cards into released cards with material actions while their information pages stay unchanged.
- **Write-back**: `docs/data/workshops.json` and both landing pages.

## RD-015 CLARIAH web-slide pilot

- **Type**: Acceptance
- **Status**: waiting
- **Trigger**: The bounded rights-safe pilot is implemented and verified.
- **Required contribution**: Accept the slide cut, browser presentation and export behaviour of the CLARIAH web-slide pilot.
- **Recommendation**: Pending evidence.
- **Basis**: `knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md`, work package 9 in `knowledge/plan.md`.
- **Effect**: Decides whether the browser-first deck enters the platform contract beside the Google Slides surface.
- **Write-back**: the pilot and, after acceptance, `knowledge/specification.md` and `knowledge/design.md`.

## RD-016 Tags of taught workshop states

- **Type**: Action
- **Status**: open
- **Trigger**: A workshop has been delivered and its taught state verified. The delivery occurred for the KUG instance `2026-09-16-kug-m3gim` on 16 September 2026.
- **Required contribution**: Tag each taught workshop state with its registered identifier, now starting with the KUG instance.
- **Recommendation**: Set the tag before the folder leaves the working tree, because the register entry drops out in the same step and the tag is afterwards the only route back to the taught state.
- **Basis**: the versioning section of `knowledge/governance.md`, `docs/data/workshops.json`.
- **Effect**: Preserves the taught state and allows the delivered instance to leave tree and register.
- **Write-back**: git history and the workshop history record.

## RD-017 shared interface baseline

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Inspect the guided acceptance route and accept the shared interface baseline as continued in v0.3, or name concrete corrections.
- **Recommendation**: Review one representative page per component family after the reduced 26-page tree has passed its own parity and browser checks.
- **Basis**: the v0.2 and v0.3 release results, the deployed public pages and the acceptance sheets for RD-021 through RD-023.
- **Effect**: Establishes the accepted interface baseline for later content and Web Module work.
- **Write-back**: `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## RD-018 KUG Web Module pilot

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or correct the learning sequence, the relation of visuals to explanations and the boundary between Web Module, Slide Deck and Lecture Notes.
- **Recommendation**: Accept the component architecture independently of the later M3GIM exercise-data release; the rights-safe conceptual sequence can be reviewed first.
- **Basis**: `communication/research/outbox/research-2026-08-25-web-module-pilot-and-licence-copy.md`, the KUG profile and Lecture Notes.
- **Effect**: Releases the component for reuse in other workshop profiles.
- **Write-back**: the KUG page pair, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## RD-019 CLARIAH Google Slides permission

- **Type**: Action
- **Status**: open
- **Required contribution**: Change the public CLARIAH Google Slides permission from edit access to read access and confirm the resulting anonymous view link.
- **Recommendation**: Preserve the existing document id and reduce only the public permission, so that repository and page links remain stable.
- **Basis**: the verified Drive source audit of 2026-08-25 and the CLARIAH material record in `docs/data/workshops.json`.
- **Effect**: Removes unintended public write access before the material is released.
- **Write-back**: the Google Slides permission state and `knowledge/journal.md`.

## RD-020 Adjacent teaching paths

- **Type**: Acceptance
- **Status**: waiting
- **Trigger**: The compact deep-dive integration and first migrated browser-native unit are implemented and verified.
- **Required contribution**: Accept the public placement of AI Coding Literacy and the migrated Prompt Engineering unit.
- **Recommendation**: Keep AI Coding Literacy external and keep the migrated unit inside the KCE design system, preserving the source ownership boundary.
- **Basis**: `knowledge/drafts/adjacent-teaching-platform-integration.md` and `communication/research/outbox/research-2026-08-25-adjacent-teaching-platforms.md`.
- **Effect**: Establishes the cross-repository learning-path contract for subsequent migrations.
- **Write-back**: `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## RD-021 Preparation

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or correct the relation between the technical setup, the external AI Coding Literacy curriculum and the four compact subject introductions.
- **Recommendation**: Keep technical setup and AI Coding Literacy distinct, retain one clear Preparation H1 and the compact six-link index, and accept the four introductions together only after they have been reconstructed from the existing slides. Until then, their public cards expose only accepted titles, topic assignments and video routes.
- **Basis**: the Preparation page pair, the AI Coding Literacy source assessment, `communication/operations/outbox/operations-2026-08-25-rd-021-module-00-acceptance-sheet.md` and `communication/operations/outbox/operations-2026-08-25-v0-3-release-result.md`.
- **Effect**: Establishes Preparation as an independent main page and fixes the boundary between setup, external curriculum and slide-derived introductions.
- **Write-back**: the Preparation page pair, `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## RD-023 AI Harness introduction routes

- **Type**: Acceptance
- **Status**: open
- **Required contribution**: Accept or correct the shared tutorial sequence, the distinction between AI Coding Literacy and product instruction, and the accuracy of the Pi harness, provider and inference-location boundary.
- **Recommendation**: Review the common component once, then inspect the first reversible check and source note on each product page. Give the Pi boundary a separate substantive check because a locally running harness can still call a remote model.
- **Basis**: `knowledge/drafts/harness-introduction-routes.md`, `communication/research/outbox/research-2026-08-25-harness-introduction-routes.md`, `communication/operations/outbox/operations-2026-08-25-rd-023-harness-introductions-acceptance-sheet.md` and `communication/operations/outbox/operations-2026-08-25-v0-3-release-result.md`.
- **Effect**: Establishes Claude Code, Codex and Pi as comparable routes from the Agentic Engineering introduction in Preparation and releases their reuse in workshop Web Modules.
- **Write-back**: the tutorial page pairs, `knowledge/project.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## RD-024 Full Slide Deck Google Slides permission

- **Type**: Action
- **Status**: open
- **Required contribution**: Change the public Full Slide Deck Google Slides permission from edit access to read access and confirm the resulting anonymous view link.
- **Recommendation**: Preserve the existing document id and reduce only the public permission, so that repository and page links remain stable.
- **Basis**: the verified Drive source audit of 2026-08-26 and the Full Slide Deck material record in `docs/data/workshops.json`.
- **Effect**: Removes unintended public write access from the canonical teaching deck.
- **Write-back**: the Google Slides permission state and `knowledge/journal.md`.

## Deliberately absent

The current interface release, the About integration, the Research Mission Control documentation and the commit and push of that change set carry no entry, because the Research Director has already authorised them. The earlier question about publishing `docs/drafts/` is obsolete, since the superseded prototypes now live under `knowledge/drafts/platform-prototypes/` outside the published tree.
