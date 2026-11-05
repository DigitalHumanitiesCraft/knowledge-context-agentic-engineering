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

1. Session 1 runs three hands-ons. The first builds a knowledge base on agentic engineering and governance from a web search with two subagents, restricted to sources from 2026 whose date is checked at the source. The second distils every source against a guiding question chosen by the participant. The third answers a governance question from the knowledge base only and produces a PDF. Around them the session covers LLM, agent and harness, tool use, subagents, the context window, `AGENTS.md` and `CLAUDE.md`, governance on the levels of data and agent, permission modes, AI slop and a PDF skill, and it closes with an interim summary.
2. Session 2 adds a knowledge dashboard that opens by double-click without a server, with follow-up prompts for feedback, self-verification, a reviewer subagent, refactoring and curation. It introduces knowledge engineering and Obsidian, and the fifth hands-on turns the knowledge base into a vault with frontmatter, a tag taxonomy, wikilinks under Related only, `HOME.md` and `ACTIVE-WORK.md`.
3. Session 3 places frontier capabilities and the building blocks around a model, context engineering, MCP, RAG and memory, hooks, Docling, Promptotyping Documents, loop engineering, multi-agent work, determinism and quality assurance. The sixth hands-on handles a customer request with four Northwind Excel files inside the vault, checks it against the governance draft and adds a data view to the dashboard whose figures a script computes and a second prompt verifies. Slides on test-driven development and open models with three local workflows follow the outlook to four templates from ongoing work.

The organiser's website text announces terminal and installation for session 1. Installation is dropped because participants come prepared. A vocabulary split stays stable, with *Wissensnetz* on the course website and *Wissensbasis* and *Wissenssystem* inside the workshop.

## Module selection

| Module | Role |
| --- | --- |
| 1 Understanding Large Language Models | Session 1, at the depth the interplay of LLM, agent and harness and the context window require. |
| 2 Prompt Engineering | Entry layer in session 1, framed as the step from prompt form to context. No block of its own. |
| 3 Knowledge and Context Engineering | Emphasis. Context Engineering closes session 1; knowledge engineering, Promptotyping Documents and the Obsidian vault form session 2. |
| 4 Agentic Engineering | Emphasis. Milestones, subagents and skills in session 1, permission modes and hooks in session 2, loop engineering, determinism and quality assurance in session 3. |
| 5 Critical Perspectives and Governance | Governance is the subject of the knowledge base itself. Data protection and the EU AI Act appear on the opening slides, and governance on the levels of data and agent is a slide of session 2. AI watermarking sits in the appendix. |

The fine module cut in `knowledge/drafts/module-map.md` remains a draft and predates this teaching design.

## Case material

The case is deliberately general and uses real material that outsiders understand. Sessions 1 and 2 work on live web sources from 2026, which each participant gathers anew. Participants may substitute a project of their own.

Session 3 uses the material in [`data/`](data/README.md), four Excel files converted from Microsoft's Northwind sample database under the MIT License, together with a synthetic German customer e-mail. The hands-on prompt carries a shortened version of the mail without the personal remarks, phone number and address, and asks the group why those were left out. All persons and companies in it are fictional. The folder also holds the project-folder hook shown on the hook slide. Three local workflows prepared for the slide on open models live in [`lokale-workflows/`](lokale-workflows/).

The synthetic institute scenario drafted on 2026-08-05 was dropped on 2026-11-03 because it did not use real data. It is preserved in git history.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | one Google Slides deck for all three sessions, operator's Drive, kept private by operator decision of 2026-11-04 and not registered in `data/workshops.json` | in preparation |
| Lecture Notes (Uni for Life 2026) | [`lecture-notes.md`](lecture-notes.md), German, following the live deck slide by slide | draft, follows the deck including session 3 |
| PPTX export per taught state | this folder | open |
| Session 3 material and hook | [`data/`](data/README.md) | present |
| Participant data folder | operator's Drive | still holds files of the dropped scenario |

## Open points

- The participant data folder on Drive still carries the dropped scenario and needs the session 3 files.
- Several slides in the deck still carry the draft marker and await the operator's acceptance; the lecture notes follow their current text.
- The operational counterpart of this profile, with prompts, logistics and correspondence, is the workshop document in the operator's research vault. Its slide sequence predates the current deck.

## Delivery notes

Filled after the workshop is taught.
