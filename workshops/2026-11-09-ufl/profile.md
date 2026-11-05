---
title: "Workshop Profile Uni for Life 2026"
workshop:
  id: 2026-11-09-ufl
  dates: 2026-11-09/10
  title: Agentic-Engineering-Workshop
  event: Uni for Life, Universität Graz
  audience: professionals from companies and institutions across disciplines
  language: de
  status: planned
status: in preparation
created: 2026-08-20
updated: 2026-11-05
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Opus 5.5)
related: [../../knowledge/project.md, ../../knowledge/drafts/module-map.md]
---

# Workshop Profile Uni for Life 2026

## Profile

This instance runs on 2026-11-09 and 10 in the Uni for Life programme of the Universität Graz. It is taught in German, online via Zoom, to a small group of professionals from companies and institutions across disciplines. The organiser announces it as *Intermediate Prompting (Agentic Engineering)*, and the live deck carries the title *Intermediate Prompting Agentic Engineering*. The register entry in `data/workshops.json` keeps the title *Agentic-Engineering-Workshop*.

The format is three sessions of two hours each, held at the following times.

| Session | Date | Time |
| --- | --- | --- |
| 1 | Monday, 2026-11-09 | 14:00–16:00 |
| 2 | Tuesday, 2026-11-10 | 10:00–12:00 |
| 3 | Tuesday, 2026-11-10 | 14:00–16:00 |

Six contact hours make this one of the shortest instances of the line, so the profile takes a narrow cut. Its subject is the steering of agentic work, which separates the instance from the foundational generative-AI series of the same programme. Participants arrive with a subscription to a frontier LLM and a running AI harness such as Claude Desktop, Codex or Antigravity, so the workshop spends no time on installation. The audience sits outside academia, and the case material of the CLARIAH-AT profile does not transfer.

Two further runs are fixed for April and November 2027, which makes the format a recurring course. The operator's research vault holds those dates; the register describes only the 2026 instance.

## Teaching design

One project grows across the three sessions. Each hands-on slide puts a copyable prompt at its centre and introduces one concept. Participants paste the prompt into their own harness and work in parallel, and the group discusses concepts while the agents run.

The deck frames the workshop with five terms after a video by IBM Technology, Agentic, Prompt, Context, Knowledge and Harness Engineering. Topics flow across the sessions, so the deck assigns no term to a single session.

1. Session 1 opens with two posts on agentic software building, the fancy (research) tools & workflows from the author's own work and LLMs as jagged alien intelligences, and then sets up Claude Code in the desktop app. It runs three hands-ons. The first builds a knowledge base on agentic engineering and governance from a web search with two subagents, restricted to sources from 2026 whose date is checked at the source. The second distils every source against a guiding question chosen by the participant. The third answers a governance question from the knowledge base only and produces a PDF. Around them the session covers Markdown and tokens, AI agent and tool use, subagents, the context window, `AGENTS.md` and `CLAUDE.md`, governance on the levels of data and agent, permission modes, autonomy and access, AI slop and a PDF skill, and it closes with an interim summary.
2. Session 2 opens with the fourth hands-on, a knowledge dashboard that opens by double-click without a server, planned in plan mode and followed by prompts for feedback, self-verification, a reviewer subagent, refactoring and curation. The Agentic Governance Workspace shows one finished run for comparison. Computational thinking and the contrast of vibe coding, agentic engineering and Promptotyping lead to knowledge modelling, Obsidian and Git, and the fifth hands-on turns the knowledge base into a vault with frontmatter, a tag taxonomy, wikilinks under Related only, `HOME.md` and `ACTIVE-WORK.md`, with one commit per step.
3. Session 3 opens with frontier capabilities and the building blocks around a model, ordered by context, harness and loop engineering, followed by MCP, RAG and memory and by agentic search. The sixth hands-on handles a customer request with four Northwind Excel files inside the vault, checks it against the governance draft and adds a data view to the dashboard whose figures a script computes and a second prompt verifies. Subagents, agent teams and dynamic workflows, quality assurance, test-driven development, the project-folder hook, Docling, open models and three local pipelines follow. Promptotyping then maps the hands-ons onto one run of the method, loop engineering extends the data view into a recurring process, and an outlook presents Research Mission Control, Second Brain Vault, Grounded Vault and the Agentic Edition Pipeline. Asymmetric amplification closes the session with three discussion questions.

The organiser's website text announces terminal and installation for session 1. Installation is dropped because participants come prepared. A vocabulary split stays stable, with *Wissensnetz* on the course website and *Wissensbasis* and *Wissenssystem* inside the workshop.

## Module selection

| Module | Role |
| --- | --- |
| 1 Understanding Large Language Models | Session 1, at the depth that jagged capability, the interplay of LLM, agent and harness and the context window require. Session 3 opens with frontier capabilities and benchmarks. |
| 2 Prompt Engineering | Entry layer in session 1, framed as the step from prompt form to context. No block of its own. |
| 3 Knowledge and Context Engineering | Emphasis. Session 1 treats knowledge documents, distillation and the context window, session 2 knowledge modelling and the Obsidian vault, session 3 MCP, RAG, memory, agentic search, Docling and the Promptotyping document types. |
| 4 Agentic Engineering | Emphasis. Session 1 treats tool use, subagents, permission modes and skills, session 2 plan mode with milestones, the reviewer subagent, computational thinking, the three ways of working and Git, session 3 multi-agent forms, quality assurance, test-driven development, the hook, local pipelines, Promptotyping and loop engineering. |
| 5 Critical Perspectives and Governance | Governance is the subject of the knowledge base itself. Data protection and the EU AI Act appear on the opening slides, governance on the levels of data and agent and AI slop in session 1, open models and asymmetric amplification in session 3, and AI watermarking in the appendix. |

The fine module cut in `knowledge/drafts/module-map.md` remains a draft and predates this teaching design.

## Case material

The case is deliberately general and uses real material that outsiders understand. Sessions 1 and 2 work on live web sources from 2026, which each participant gathers anew. Participants may substitute a project of their own.

Session 3 uses the material in [`data/`](data/README.md), four Excel files converted from Microsoft's Northwind sample database under the MIT License, together with a synthetic German customer e-mail. The hands-on prompt carries a shortened version of the mail without the personal remarks, phone number and address, and asks the group why those were left out. All persons and companies in it are fictional. The folder also holds the project-folder hook shown on the hook slide. The three local pipelines on the slide that follows open models, mail redaction, PDF to Markdown and speech to text, live in [`lokale-workflows/`](lokale-workflows/), each with its script, check and a README carrying the measurements of 2026-11-05. The mail redaction runs on the customer e-mail and `mitarbeitende.xlsx` from `data/`.

The synthetic institute scenario drafted on 2026-08-05 was dropped on 2026-11-03 because it did not use real data. It is preserved in git history.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | one Google Slides deck for all three sessions, operator's Drive, kept private by operator decision of 2026-11-04 and not registered in `data/workshops.json` | in preparation |
| Lecture Notes (Uni for Life 2026) | [`lecture-notes.md`](lecture-notes.md), German, following the live deck slide by slide | draft, follows the deck including session 3 |
| PPTX export per taught state | this folder | open |
| Session 3 material and hook | [`data/`](data/README.md) | present |
| Local pipelines for the slide on own pipelines | [`lokale-workflows/`](lokale-workflows/) | present, measured on 2026-11-05 |
| Participant data folder | operator's Drive | still holds files of the dropped scenario |

## Open points

- The participant data folder on Drive still carries the dropped scenario and needs the session 3 files.
- In the deck state of 2026-11-05 the slides Das Wissensdokument im Vault, Aufbau des Vaults, Docling, Loop Engineering, Promptotyping Documents and AI Watermarking carry the draft marker, the slides Second Brain Vault, Grounded Vault and Agentic Edition Pipeline still announce their figure as to follow, and the slide between the local pipelines and Promptotyping holds only a speaker note left from another deck. These slides await the operator's acceptance, and the lecture notes follow their current text.
- The deck's run-through and appendix slides name the document types Declarative, Process and Action Documents and list Verification, Validation and Curation as phases, as `knowledge/terms.md` does. The lecture notes follow the Promptotyping paper 1.0 with Declarative Knowledge Documents, Process Knowledge Documents and Agent Instruction Documents and treat Verification, Agentic Review, Scholarly Validation and Knowledge Curation as cross-cutting. The common wording is an operator decision.
- The materials slide and the lecture notes link the German glossary page, which reaches the public site only with the author's push of the local commits. On 2026-11-05 the live URL answered with 404.
- The operational counterpart of this profile, with prompts, logistics and correspondence, is the workshop document in the operator's research vault. Its slide sequence predates the current deck.

## Delivery notes

Filled after the workshop is taught.
