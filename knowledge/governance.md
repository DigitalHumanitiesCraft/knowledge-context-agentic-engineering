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
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [project.md, plan.md]
---

# Governance

Decision authority, source status and boundaries for humans and agents in this repo. It realizes the governance function of the Promptotyping convention; the reference instance lives in the method repo `DigitalHumanitiesCraft/Promptotyping`.

## Roles and authority

- The **Critical Expert (operator)** decides canonical term wording, design approvals (motif, font, page structure), publication steps (Pages activation, license application, announcements, git tags), rights questions, deletion or relocation of canonical holdings, and every drift resolution against the vault canon.
- **Agents** execute structure, migration, translation, platform building, register upkeep and verification. They prepare decisions with a recommendation and keep `journal.md` current.
- The repo is single-author. Write access stays with the operator; co-teachers contribute material through the operator. There is no contributor process.

## Source status

| Holding | Canonical place |
| --- | --- |
| Full Lecture Notes, Full Slide Deck | this repo (`script/`, `slides/`) |
| Terms | `terms.md` in this repo; it is filled from the material and supersedes the vault atoms, whose wording is now examined against it as a delta |
| Workshop register and the current set of instances | `docs/data/workshops.json` |
| Delivered instances | git history, reachable through the tag of the taught state |
| Live decks and documents | Google Workspace, as derived surfaces; divergent wording is examined as a delta |
| CLARIAH hands-on (prompts, schema, runs) | `chpollin/zbz-ocr-tei/workshops/clariah-at-2026/` |
| Project coordination | the author's vault |

## Write-back

Changes to canonical text happen here and are committed; Google artifacts are updated afterwards. Term decisions flow first into `terms.md` and from there into script, slides and the vault atoms. Findings from delivered workshops go into the workshop profile and `journal.md`. Translations follow the pipeline stated in `project.md`, German source, agent translation, operator review.

## Versioning

Fine-grained history lives in git. The state actually taught in a workshop receives a git tag named after the registry id (for example `2026-09-25-clariah-at`), set by the operator; the register and the workshop page link to the tagged state. Workshop folder names equal registry ids; a single id scheme holds across register, folders, covers and tags. PPTX exports are stored per taught state in the workshop folder.

The working tree carries only upcoming instances (operator decision 2026-08-20). Once an instance has been taught and its state tagged, its folder is removed and its register entry drops out, so the public platform shows what people can still attend. Nothing is lost, because git history holds the material and the tag names the taught state. A document that cites a removed file names it as preserved in git history at the short SHA of the last commit that held it.

## Rights and licensing

No facsimiles in this repo; image rights of the Hersch and Zweig material remain with the source projects, which are linked. No third-party personal data; workshop participant data is never stored here. Textual content is licensed CC BY 4.0 (operator decision 2026-08-20); slide decks are checked individually for embedded third-party image rights before the license statement is extended to them.

## Journal and privacy

`journal.md` is public. It records each decision with its substantive reason. Reasons that touch acquisition, partners or pricing stay in the author's vault; the journal then records the decision as made by the operator without them.

## Escalation

When repo, vault and Google artifacts contradict each other, the contradiction is never silently harmonized; it goes to the operator as a named delta.
