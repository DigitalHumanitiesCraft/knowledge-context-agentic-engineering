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
updated: 2026-11-04
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Opus 5.5)
related: [../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/specialization-analysis.md]
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

1. Session 1 builds a knowledge dashboard on agentic engineering and governance from a short web search restricted to sources from 2026. The project receives a `knowledge/` folder for distilled knowledge and a `sources/` folder for the found sources, and the agent works in milestones after three context questions. Around this hands-on the session explains the interplay of LLM, agent and harness, the shift from prompt form to Context Engineering and harness engineering, a reviewer subagent used as LLM-as-a-judge, and the removal of generic interface elements from generated output.
2. Session 2 manages the context window with `/context`, `/compact` and `/init`, introduces `AGENTS.md` and `CLAUDE.md` at global and project level, and separates them from memory. The hands-on transfers the collected knowledge to the participant's own organisation through a short interview with three guiding questions, turns it into a pitch of at most five slides, and saves the procedure as a skill. The session closes with access control, covering the permission modes including auto mode and a hook that blocks file writes outside the project folder.
3. Session 3 handles a synthetic customer request with the knowledge base built in sessions 1 and 2. The request asks for a workshop, slides, a small reference website and draft rules for AI use, and it deliberately carries personal data so that participants practise passing only the necessary parts to an LLM.

The learning goals on the deck are that participants can explain how LLM, AI agent and AI harness work together, build and maintain project knowledge and context so that an agent works reliably with it, and plan agentic workflows, check their results and transfer them to their own projects.

The organiser's website text announces terminal and installation for session 1. Installation is dropped because participants come prepared. A vocabulary split stays stable, with *Wissensnetz* on the course website and *Wissensbasis* and *Wissenssystem* inside the workshop.

## Module selection

| Module | Role |
| --- | --- |
| 1 Understanding Large Language Models | Session 1, at the depth the interplay of LLM, agent and harness and the context window require. |
| 2 Prompt Engineering | Entry layer in session 1, framed as the step from prompt form to context. No block of its own. |
| 3 Knowledge and Context Engineering | Emphasis. The `knowledge/` folder, context-window management, `AGENTS.md`, `CLAUDE.md` and memory in sessions 1 and 2. |
| 4 Agentic Engineering | Emphasis. Milestones, subagents, skills, permission modes and hooks across all three sessions. |
| 5 Critical Perspectives and Governance | Governance is the subject of the knowledge base itself. Data protection and the EU AI Act appear on the opening slides, and data minimisation is the explicit concept of session 3. |

The fine module cut in `knowledge/drafts/module-map.md` remains a draft and predates this teaching design.

## Case material

The case is deliberately general and uses real material that outsiders understand. Sessions 1 and 2 work on live web sources from 2026, which each participant gathers anew. Participants may substitute a project of their own.

Session 3 uses the material in [`data/`](data/README.md), a synthetic German customer e-mail with four Excel files converted from Microsoft's Northwind sample database under the MIT License. All persons and companies in it are fictional. The folder also holds the project-folder hook shown in session 2.

The synthetic institute scenario drafted on 2026-08-05 was dropped on 2026-11-03 because it did not use real data. It is preserved in git history.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | one Google Slides deck for all three sessions, operator's Drive, kept private by operator decision of 2026-11-04 and not registered in `data/workshops.json` | in preparation |
| Lecture Notes (Uni for Life 2026) | [`lecture-notes.md`](lecture-notes.md), German, following the live deck slide by slide | draft, session 3 open |
| PPTX export per taught state | this folder | open |
| Session 3 material and hook | [`data/`](data/README.md) | present |
| Participant data folder | operator's Drive | still holds files of the dropped scenario |

## Open points

- The participant data folder on Drive still carries the dropped scenario and needs the session 3 files.
- Session 3 has no slides yet. They go into the same deck as sessions 1 and 2.
- The operational counterpart of this profile, with prompts, logistics and correspondence, is the workshop document in the operator's research vault. Its slide sequence predates the current deck.

## Delivery notes

Filled after the workshop is taught.
