---
title: Governance
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
created: 2026-08-20
updated: 2026-08-25
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, plan.md]
---

# Governance

Decision authority, source status and boundaries for humans and agents in this repo. It realizes the governance function of the Promptotyping convention; the reference instance lives in the method repo `DigitalHumanitiesCraft/Promptotyping`.

## Roles and authority

The role model comes from Research Mission Control and binds humans and agents alike in this repo.

- The **Research Director** holds substantive decision and acceptance authority. It covers canonical term wording, design approvals (motif, font, page structure), publication steps (Pages activation, licence application, announcements, git tags), rights questions, deletion or relocation of canonical holdings, and every drift resolution against the vault canon. The earlier label *Critical Expert (operator)* names the acceptance function of the same person and carries no separate authority.
- The **Research Orchestrator** owns research framing, evidence synthesis and bounded implementation briefs. It maintains the Research Director Log, carries Research communication and raises every Research Director Point.
- The **Operational Orchestrator** owns implementation coordination, terminal verification, integration and release. It returns evidence-backed Operations results that map to the criteria of the accepted brief. It writes repository artefacts only under an accepted brief or a direct Research Director instruction, and terminal integration stays with it.
- **Bounded subagents** execute structure, migration, translation, platform building, register upkeep and verification. They inherit only the authority, write boundary, exclusions and verification criteria stated for their lane, prepare decisions with a recommendation and keep `journal.md` current.
- The repo is single-author. Write access stays with the Research Director; co-teachers contribute material through that route. There is no contributor process.
- **Research support lanes** are read-only by construction. The Research Director authorised three of them on 2026-08-25, a contract audit reconciling every Research brief against the action layer, the design and specification documents and the public tree, a browser acceptance pass observing representative English and German pages at desktop, 640, 390 and 320 pixels, and a VetMedAI source intake whose only write target is `drafts/vetmed-teaching-material-intake.md`. A lane forwards only a finding that changes an implementation or release decision, and none of them authorises public teaching material, canonical knowledge or terminal integration.

## Control surface and provenance

`communication/research/director-log.md` is the active control surface for every contribution the Research Director still has to supply. It carries one entry per contribution under a stable `RD-###` identifier, and an entry leaves the log after canonical write-back and verification. `journal.md` is the durable target for decision provenance and receives a decision, acceptance or authorisation whenever it changes the project contract or the publication state. The lifecycle of the log and the communication contract live in `communication/PROTOCOL.md`; `communication/` transports current state and never becomes a second knowledge base.

Tool and model provenance follows the same split. The public interface names only the two maintained methods that structure the work, Promptotyping and Research Mission Control, because a model name or version ages between releases and a public page cannot carry the date at which it was true. The detailed, dated record of which harness and which model produced or revised a state stays in `journal.md`, where each entry carries its date, and in the `generated-with` field of the knowledge documents.

## Source status

| Holding | Canonical place |
| --- | --- |
| Full Lecture Notes, Full Slide Deck | this repo (`script/`, `slides/`) |
| Terms | `terms.md` in this repo; it is filled from the material and supersedes the vault atoms, whose wording is now examined against it as a delta |
| Workshop register, module subsets, material release states and available formats | `docs/data/workshops.json` |
| Video inventory, playlist order, primary module, related modules and duration | `docs/data/videos.json` |
| Delivered instances | git history, reachable through the tag of the taught state |
| Live decks and documents | Google Workspace, as derived surfaces; divergent wording is examined as a delta |
| CLARIAH hands-on (prompts, schema, runs) | `chpollin/zbz-ocr-tei/workshops/clariah-at-2026/` |
| Workshop Web Module | the paired workshop pages in `docs/workshops/`; its availability per instance in the `web_module` field of `docs/data/workshops.json` |
| AI Coding Literacy curriculum | the independent repo `DigitalHumanitiesCraft/ai-coding-literacy`, linked as an external deep dive and never copied here |
| AI Literacies prototype | the local unversioned folder `DHCraft/ai-literacies`, read-only migration input without publication status |
| Project coordination | the author's vault |

## Write-back

Changes to canonical text happen here and are committed; Google artifacts are updated afterwards. Term decisions flow first into `terms.md` and from there into script, slides and the vault atoms. Findings from delivered workshops go into the workshop profile and `journal.md`. Translations follow the pipeline stated in `project.md`, German source, agent translation, Research Director review.

## Versioning

Fine-grained history lives in git. The state actually taught in a workshop receives a git tag named after the registry id (for example `2026-09-25-clariah-at`), set by the Research Director; the register and the workshop page link to the tagged state. Workshop folder names equal registry ids; a single id scheme holds across register, folders, covers and tags. PPTX exports are stored per taught state in the workshop folder.

The working tree carries only upcoming instances (operator decision 2026-08-20). Once an instance has been taught and its state tagged, its folder is removed and its register entry drops out, so the public platform shows what people can still attend. Nothing is lost, because git history holds the material and the tag names the taught state. A document that cites a removed file names it as preserved in git history at the short SHA of the last commit that held it.

## Rights and licensing

No facsimiles in this repo; image rights of the Hersch and Zweig material remain with the source projects, which are linked. No third-party personal data; workshop participant data is never stored here. The public pages and original text are licensed CC BY 4.0 (operator decision 2026-08-20). The register records this scope as `page-and-original-text`, and this document and the rights explanation of the About pages carry the same wording. A public card shows the linked identifier `CC BY 4.0` alone, because the card is a compact metadata surface and the exact scope belongs where it can be read in full (Research Director decision 2026-08-25). Each Slide Deck is checked individually for embedded third-party image rights before the licence is extended to the complete material artefact.

## Journal and privacy

`journal.md` is public. It records each decision with its substantive reason. Reasons that touch acquisition, partners or pricing stay in the author's vault; the journal then records the decision as taken by the Research Director without them.

## Escalation

When repo, vault and Google artifacts contradict each other, the contradiction is never silently harmonized; it goes to the Research Director as a named delta.
