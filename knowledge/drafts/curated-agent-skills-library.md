---
title: Curated Agent Skills Library
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [module-hub-architecture.md, claude-code-agentic-engineering-subchapter.md, ../terms.md]
---

# Curated Agent Skills Library

Editorial and interface contract for a maintained collection of reusable agent skills. The collection belongs to Module 04 because skills package procedures that an AI Harness can invoke during a work trajectory. Skills that maintain project knowledge or select context also carry a visible relation to Module 03.

## Teaching purpose

The collection teaches readers how to assess and adapt a skill. It does not reproduce every file from an external repository. Each entry explains the task boundary, expected evidence, required permissions, compatible harnesses and source status. Installation follows only after the learner has inspected the skill instructions and their write scope.

## Initial source

The public `mattpocock/skills` repository supplies the first external collection. Its documented design treats skills as small, adaptable and composable instruction packages. It distinguishes user-invoked orchestration skills from model-invoked procedural skills and provides installation routes for Claude Code, Codex and other agents. The repository is MIT-licensed.

Source: <https://github.com/mattpocock/skills>

The source is an example collection and remains externally maintained. Its claims and current installation commands require a recorded check date.

## Initial curated set

| Skill | Learning use | Primary relation | Related relation |
| --- | --- | --- | --- |
| `grill-with-docs` | Elicit requirements while maintaining shared terminology and decision records. | 04 Agentic Engineering | 02 Prompt Engineering, 03 Knowledge and Context Engineering |
| `research` | Delegate a bounded source investigation and return a cited repository artefact. | 04 Agentic Engineering | 03 Knowledge and Context Engineering, 05 Critical Perspectives and Governance |
| `domain-modeling` | Test project vocabulary against cases and maintain the responsible knowledge artefacts. | 03 Knowledge and Context Engineering | 04 Agentic Engineering |
| `diagnosing-bugs` | Establish an observable feedback loop before changing an implementation. | 04 Agentic Engineering | 05 Critical Perspectives and Governance |
| `tdd` | Use a failing test and an inspectable implementation loop to constrain code changes. | 04 Agentic Engineering | 05 Critical Perspectives and Governance |
| `code-review` | Compare an implementation with repository standards and the originating specification. | 04 Agentic Engineering | 05 Critical Perspectives and Governance |
| `handoff` | Transfer bounded state so another session can continue with explicit evidence and scope. | 04 Agentic Engineering | 03 Knowledge and Context Engineering |
| `writing-for-agents` | Write persistent instructions and skill documents for reliable retrieval and use. | 03 Knowledge and Context Engineering | 04 Agentic Engineering |

This initial set represents distinct teaching functions. Further entries require an explicit pedagogical use, a source inspection and a duplication check against the existing collection.

## Entry contract

Every public entry carries:

- name and concise task boundary;
- invocation type, either user-invoked or model-invoked;
- primary module and optional related modules;
- compatible harnesses and installation route;
- expected input, output and verification evidence;
- permission and write-scope note;
- source repository, licence and last-checked date;
- maintenance status, using `recommended`, `reference`, `experimental` or `retired`.

The interface must distinguish source description from project evaluation. A `recommended` label records a completed KCE review of the inspected version. Popularity or inclusion in an external collection supplies no quality judgement.

## Module 04 integration

The first v0.3 release adds a dedicated `Curated Skills` subsection to the Module 04 `routes` section. It uses a compact semantic list with filters expressed as ordinary links or controls only when the feature remains usable without JavaScript. Each row exposes task boundary, invocation type, compatibility, status and source.

The initial release may show five to eight reviewed entries. A separate library page becomes justified when the maintained register grows beyond what the hub can present without displacing its learning sequence. That later route should read from a shared register and preserve a static HTML fallback.

## Evaluation questions

1. Does the skill describe one bounded procedure with an observable result?
2. Does its invocation rule match the action it performs?
3. Are permissions, write boundaries and external side effects explicit?
4. Does it preserve evidence needed for verification or handoff?
5. Can a learner inspect and adapt the instructions without hidden dependencies?
6. Is its source, licence and checked version visible?

## Source and rights boundary

The public platform links to external skill sources and writes original summaries. It does not mirror external `SKILL.md` content unless the licence, attribution and maintenance contract have been checked for that exact use. Installation commands remain version-sensitive evidence and must be checked against the current source before publication.
