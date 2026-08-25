---
title: Codex Bootcamp 101 Evidence Note
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../design.md, claude-code-agentic-engineering-subchapter.md]
---

# Codex Bootcamp 101 Evidence Note

Source-grounded intake for a future Codex introduction or focused deep dive. This note summarises public official material and does not reproduce the recording, captions or slide deck.

## Available official material

- The [OpenAI Academy recording](https://academy.openai.com/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31) identifies the session as an introductory bootcamp on agentic coding. The public page exposes no readable transcript or chapter list, and its embedded data reports no maintained transcript.
- The embedded video player exposes one English auto-generated subtitle track. The track is useful for locating sections and checking topics, but it is not an edited or authoritative word record. Its signed caption URL expires; the stable recording page remains the citation target.
- The [OpenAI Academy event page](https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-6ps1oly1yu) states four learning objectives: scoping work, providing useful context, steering work in progress and reviewing changes before acceptance.
- The event page links an [official 31-page slide deck](https://d2xo500swnpgl1.cloudfront.net/slide-upload/oaiacademy/Codex-Bootcamp-101-Agentic-Coding-7d3020f8-70e8-4d61-87ad-88f07d5155fb-1785273916586.pdf). The file supports topic verification and agenda reconstruction. Its rights notice does not support copying or adapting the slides into this repository.
- The [official bootcamp-series page](https://academy.openai.com/en/public/clubs/builders-etkn1/resources/codex-bootcamp-2026-07-18) positions 101 as the introduction, followed by team workflows in 201 and advanced automation and scaling in 301.

## Reconstructed content map

The agenda labels come from the official event material. Approximate positions come from the auto-generated captions and require confirmation against playback before they are published as timestamps.

| Approximate position | Section | Teaching function |
| --- | --- | --- |
| 00:01 | Welcome and operating frame | Establishes the session scope and prerequisites. |
| 00:02 | Introduction and setup | Introduces Codex, agentic delegation, product surfaces and initial configuration. |
| 00:16 | Product walkthrough | Demonstrates the working surface and the transition from request to inspected result. |
| 00:21 | Agentic working loop | Frames the cycle as prompt, inspect, act, validate and report. |
| 00:23 | Preparing an agent-ready workspace | Connects repository context, feedback and persistent `AGENTS.md` instructions. |
| 00:28 | Questions | Clarifies setup and working-model details. |
| 00:32 | Codex across the software lifecycle | Relates planning, implementation, testing, review and human acceptance. |
| 00:41 | Bounded delegation demonstration | Shows a constrained feature task with explicit completion conditions. |
| 00:54 | Closing questions | Consolidates workflow and review questions. |

The sources also support a compact concept set for teaching: Plugins, Skills, Scheduled Tasks, Plan Mode, review of diffs, `/review`, evidence-bearing handoffs and four prompt fields labelled Goal, Context Pointers, Constraints and Done When.

## Proposed deep-dive structure

1. **Codex as an agentic work surface.** Place the tool inside the AI Harness concept and distinguish the model from the environment that supplies files, tools, instructions and validation.
2. **Make the workspace agent-ready.** Explain persistent project instructions, source pointers, executable checks and the boundary of the authorised working area.
3. **Write a delegable task.** Use the four official prompt fields as a compact task contract.
4. **Steer through observable evidence.** Inspect the plan, diff, tests and handoff instead of evaluating fluency alone.
5. **Separate capability extensions.** Position Skills as maintained procedures, Plugins as packaged extensions and Scheduled Tasks as recurring execution surfaces.
6. **Complete the acceptance loop.** Treat human review as an explicit state following model validation evidence.

## Editorial boundaries

- Do not call the auto-generated captions an official transcript.
- Do not publish exact quotations without checking them against playback.
- Do not copy the official slide deck or its visual layout. Derive original teaching text from the verified concepts and cite the Academy sources.
- Do not normalise the session date from the currently inconsistent public metadata. The recording page, event page and embedded player expose different dates.
- Keep volatile product commands and interface details in a dated reference surface. The conceptual working loop can enter the maintained teaching material after operator acceptance.
