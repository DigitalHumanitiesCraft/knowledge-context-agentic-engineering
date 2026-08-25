---
id: research-2026-08-25-iteration-16-release-brief
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: operations-2026-08-25-ready
created: 2026-08-25
requires_reply: true
canonical_refs:
  - CLAUDE.md
  - knowledge/design.md
  - knowledge/specification.md
  - knowledge/plan.md
  - knowledge/handoff.md
  - knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md
  - docs/
---

# Implementation Brief: close and publish interface iteration 16

## Objective and intended effect

Bring the coherent, already authorised interface change set to a release-quality state without opening a new product or content strand. The result must make all seven workshop information pages reachable before material release, expose the five-module notation consistently, provide the bilingual About pages, and preserve a readable, keyboard-operable and responsive static teaching platform.

The Research Director has authorised commit and push after successful verification. This brief does not authorise publication of unfinished teaching exports, generated cover replacements, source screenshots or the web-native CLARIAH slide pilot.

## Current evidence and epistemic state

The working tree contains 51 modified, renamed or untracked entries on `main`, based on `8d3a0ee`. The changes form one continuous interface and documentation pass; no unrelated modification was identified in the Research review. Preserve the complete worktree until the final release commit.

Research verified the following on 2026-08-25:

- `html-validate` passed for all 22 public HTML files with the repository-compatible rule exceptions.
- A structural audit found 22 public pages, seven workshop title links in each landing page, 28 module-series rows, 136 module links, 34 video cards in each landing page, 34 video-register entries and seven workshop-register entries. All checked IDs, local fragments and local file targets resolved.
- Ten material and module SVG files parsed as XML. The shared stylesheet has balanced braces, 410 to 410. `git diff --check` passed; Git only reported the existing line-ending notices.
- The local English landing page at 1280 by 720 had no horizontal overflow, three teaching-material columns, the stylesheet version `20260825-17`, the About navigation item, 34 videos and seven workshop links. The minimum observed workshop title-link height was 44 pixels. Clicking the first workshop title opened its information page successfully.
- The earlier iteration-16 browser pass established 390-pixel behaviour for the landing, Preparation and Claude Code pages. The final release check must repeat the narrow-width pass after the stylesheet-17 and About-page additions; Research has not claimed that later pass as observed.

## Operational agent lanes

Use three Opus subagents with disjoint boundaries. Agents report to the Operational Orchestrator and do not commit, push or rewrite another lane's files.

### Lane O1: frontend acceptance and bounded repair

- Write boundary: `docs/**/*.html`, `docs/assets/site.css`, `docs/assets/materials/`, `docs/assets/modules/`, `docs/data/*.json`, `docs/downloads/`, `docs/tutorials/`.
- Task: rerun desktop and 390-pixel browser checks for both interface languages, the About pair, one Preparation page, one Claude Code page and representative workshop pages. Correct only failures against the installed iteration-16 contract.
- Preserve: static HTML and CSS, zero required JavaScript, existing workshop material states, current Google and YouTube functional query parameters, all information-page links and the shared module notation.

### Lane O2: canonical knowledge closure

- Write boundary: `CLAUDE.md`, `AGENTS.md`, `knowledge/INDEX.md`, `knowledge/design.md`, `knowledge/specification.md`, `knowledge/plan.md`, `knowledge/project.md`, `knowledge/governance.md`, `knowledge/journal.md`, `knowledge/handoff.md`.
- Task: reconcile current-state claims with the verified implementation. Replace the stale 20-page, stylesheet-12 and unlinked-workshop statements in `knowledge/handoff.md`; mark the bilingual About integration complete; retain historical journal entries as provenance. Record the remaining editorial inputs as open gates without describing them as failures of the current release.
- Preserve: the conceptual status of `knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md` and `knowledge/drafts/codex-bootcamp-101-evidence.md`. They are evidence and architecture drafts, not installed public features.

### Lane O3: independent release audit

- Write boundary: none. This lane is read-only.
- Task: inspect the combined O1/O2 result for broken links, missing files, accessibility regressions, inconsistent counts, accidental publication of prototypes, tracking parameters and scope drift. Return exact findings to the Operational Orchestrator.

The Operational Orchestrator alone integrates lane results, performs the terminal verification, stages the coherent change set, commits it and pushes `main` to `origin`. Do not allow a subagent to perform Git integration.

## Required terminal verification

The release is accepted only when all of the following hold on the combined worktree:

1. `html-validate` passes for `docs/**/*.html` with `doctype-style`, `prefer-native-element`, `no-redundant-role` and `long-title` disabled as in the Research check.
2. All 22 public pages have one skip link, a focusable `main-content` target, the stylesheet version `20260825-17`, language-paired navigation, About in primary navigation and footer, and the canonical imprint link.
3. Both landing pages contain seven working workshop title links, five hero-module targets, 34 videos split 4/1/6/21/2, and module links whose fragments resolve in the language-matched landing page.
4. In-preparation workshop cards remain visibly muted while their information-page links remain keyboard and pointer operable. They expose no premature material actions.
5. The 390-pixel and desktop browser passes show no page-level horizontal overflow. Focus indicators remain visible; primary workshop title links and coarse-pointer actions meet the installed touch-target rules.
6. About pages keep the narrow reading measure and four-part information structure in both languages.
7. All ten module and material SVGs parse, JSON registers parse, CSS braces balance and `git diff --check` passes.
8. No sharing or tracking parameters enter public URLs. Functional YouTube `v` and `list` parameters remain intact.
9. `knowledge/handoff.md`, `knowledge/plan.md`, `knowledge/design.md`, `knowledge/specification.md` and `CLAUDE.md` describe the same 22-page iteration-16 release state.
10. After commit and push, `git status --short` is empty and `origin/main` resolves to the new commit. Report the commit identifier and live Pages check separately; a delayed Pages deployment is not evidence of a failed push.

## Exclusions and decisions reserved for the Research Director

- Do not implement the CLARIAH web-native slide pilot in this release.
- Do not turn the research-data deep dive or archive persona into public pages yet.
- Do not add facsimiles, external slide images or generated screenshots to the repository.
- Do not invent final Markdown or PDF exports, cover replacements, workshop data or material-release dates.
- Do not decide the VetMed case, module fine cut, terminology decisions or workshop-specific source selection.
- Do not refactor the static page system into a build pipeline or JavaScript application.

## Expected result and return message

Return one Operations result message in the same thread with the commit identifier, pushed branch, exact verification performed, any deviation from this brief, remaining uncommitted paths and the live Pages observation. If a criterion fails, preserve the worktree and report the smallest concrete blocker instead of committing a partially verified release.
