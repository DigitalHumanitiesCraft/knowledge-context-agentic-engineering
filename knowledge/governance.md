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

Decision authority, source status and boundaries for humans and agents in this repo. Master instance of the governance function under the Promptotyping convention; the first instance lives in the method repo `DigitalHumanitiesCraft/Promptotyping`.

## Roles and authority

- The **Critical Expert (operator)** decides: canonical term wording, design approvals (motif, font, page structure), publication steps (Pages activation, license application, announcements, git tags), rights questions, deletion or relocation of canonical holdings, and every drift resolution against the vault canon.
- **Agents** execute: structure, migration, translation, platform building, register upkeep, verification. They prepare decisions with a recommendation and keep `journal.md` current.
- The repo is single-author. Write access stays with the operator; co-teachers contribute material through the operator. There is no contributor process.

## Source status

| Holding | Canonical place |
| --- | --- |
| Master script, slide texts | this repo (`script/`, `slides/`) |
| Terms (until `terms.md` is filled) | the author's vault atoms |
| Workshop register | `docs/data/workshops.json` |
| Live decks | Google Slides, as derived surfaces; divergent wording is examined as a delta |
| CLARIAH hands-on (prompts, schema, runs) | `chpollin/zbz-ocr-tei/workshops/clariah-at-2026/` |
| Project coordination | the author's vault |

## Write-back

Changes to canonical text happen here and are committed; Google artefacts are updated afterwards. Term decisions flow first into `terms.md` and from there into script, slides and the vault atoms. Findings from delivered workshops go into the workshop profile and `journal.md`. Translations follow the pipeline in `project.md`: German source, agent translation, operator review.

## Versioning

Fine-grained history lives in git. The state actually taught in a workshop receives a git tag (for example `clariah-at-2026`), set by the operator; the register and the workshop page link to the tagged state. PPTX exports are stored per taught state in the workshop folder.

## Rights and licensing

No facsimiles in this repo; image rights of the Hersch and Zweig material remain with the source projects, which are linked. No third-party personal data; workshop participant data is never stored here. Textual content is licensed CC BY 4.0 (operator decision 2026-08-20); slide decks are checked individually for embedded third-party image rights before the license statement is extended to them.

## Journal and privacy

`journal.md` is public. It records each decision with its substantive reason. Reasons that touch acquisition, partners or pricing stay in the author's vault; the journal then records the decision as made by the operator without them.

## Escalation

When repo, vault and Google artefacts contradict each other, the contradiction is never silently harmonised; it goes to the operator as a named delta.
