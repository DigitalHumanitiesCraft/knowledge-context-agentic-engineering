---
title: Handoff
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Handoff
  version: 0.1
  url: https://dhcraft.org/Promptotyping/promptotyping-document/handoff
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-handoff
status: active
created: 2026-08-24
updated: 2026-11-10
language: en
authors: [Christopher Pollin]
generated-with: Claude Code and Codex
related: [INDEX.md, plan.md, journal.md]
---

# Handoff

This Process Inbox contains only received deltas that still require verification, integration or reasoned rejection. Durable knowledge belongs in the responsible Declarative or Action Document, accepted future work in `plan.md`, and completed provenance in `journal.md` and Git.

## Open handoff points

### Glossary wording found by the independent site review

- **Received:** 2026-11-10
- **Source:** read-only review of the four public pages against `specification.md` and `design.md` by a fresh subagent, which read all glossary entries in both languages. Its findings on markup, contrast, touch targets and the glossary fragment are integrated and recorded in `journal.md`.
- **Target:** `terms.md`, then `python scripts/build_glossary.py`.
- **Context:** the points below concern term wording, which the author decides. None was changed.
  - AI Harness is neuter in the German Full Lecture Notes and on the landing page (das AI Harness) and masculine in the Uni for Life notes and in the German sentences of Hook and Slash Command (der AI Harness).
  - Acceptance appears as Acceptance and, in Agentic Edition Pipeline, as Abnahme. The plural of agent appears as Agenten and as Agents.
  - German headwords differ in capitalisation (kontextuell plausible Lesung beside Asymmetrische Amplifikation), and some German definitions open without an article.
  - The two languages say different things in Agent Memory (binding force, verbindliche Regeln), Docling (only the English names knowledge work, which also adds a related term on the German page), Frontier Model (only the German says Allzweck-LLM) and Governance Dilemma.
  - Single renderings read weakly: Frontmatter (aus Schlüssel und Wert), Prompt Sensitivity against Promptwirkungen, Critical Cyber Capability against the plural kritische Cyberfähigkeiten, Test-Driven against Test Driven, Over-Distillation beside an untranslated Distillation. Governance Dilemma names an author without saying which, and Agent Teams names a vendor product in its public sentence.
  - The glossary assigns Promptotyping and Grounded Vault to module 04, while the Methods card lists both under module 03.
- **Next action:** take the points into the terminology review named in `plan.md`.
- **Operator point:** term wording, see RD-002.

### Personal AI Agent in the Uni for Life deck against Always-On Agent in the glossary

- **Received:** 2026-11-10
- **Source:** the Google Slides deck of the Uni for Life workshop, slide AI Harnesses (`h9128065016e2d17_0_1`), read on 2026-11-10 at revision `ixYLax6BAfYFoQ`.
- **Target:** the entry Always-On Agent in `terms.md`, section 6.6 of the German Full Lecture Notes, the section Always-On and Proactive Agents of the English notes and the editorial slide in `slides/full-slide-deck.md`.
- **Context:** the author's slide already defines a Personal AI Agent, after Wu et al. 2026 (arXiv:2611.03092), as an agent that keeps context across conversations, looks after a person's tasks over a longer time and acts on its own within agreed authority, and it lists dots, Grok Bot, Claude Duet, Hermes Agent and OpenClaw beside coding harnesses. The material added on 2026-11-10 describes the same products under the vendors' word always-on. Two names for overlapping things now stand side by side.
- **Next action:** read Wu et al. 2026, sections 2.1, 2.2 and 4.2, then either make Personal AI Agent the headword and treat always-on as its mode of operation, or keep both with a stated relation.
- **Operator point:** term wording.

### Interface copy and one leftover asset

- **Received:** 2026-11-10
- **Source:** the same review.
- **Target:** `docs/index.html`, `docs/index.de.html`, `scripts/build_glossary.py`, `docs/assets/materials/videos.svg`.
- **Context:** the English introduction says that LLMs operate inside AI Harnesses, the German one that they are used in them. The footer sentence on funding has no clear referent for its revision. The German glossary labels the order switch Ordnung, where Reihenfolge would read more naturally. The mark `docs/assets/materials/videos.svg` of the retired playlist card is published and referenced by no page.
- **Next action:** decide the wording, and remove the unreferenced mark if it is no longer wanted.
- **Operator point:** interface copy and deletion of a published file.

### Monetary amount in a mirrored video title

- **Received:** 2026-11-10
- **Source:** the same review.
- **Target:** `CLAUDE.md` or `data/videos.json`.
- **Context:** the module 05 entry `QYeNESqKbSc` carries an amount in its original title, which both landing pages show. `CLAUDE.md` excludes monetary amounts anywhere in the repository and treats names in teaching material as research data, but says nothing on amounts in third-party titles.
- **Next action:** state in `CLAUDE.md` that mirrored titles are quoted data, or shorten the display title in the register and on both pages.
- **Operator point:** content boundary.
