---
title: Workshop Profile Freiburg DHLab Pre-Workshop 2025
workshop:
  id: 2025-09-24-freiburg-dhlab-preworkshop
  dates: 2025-09-24
  title: Promptotyping Pre-Workshop
  event: "DHLab Freiburg"
  audience: participants of the following full-day Promptotyping workshop, mixed technical prerequisites
  language: de
  status: delivered
  slides: null
  script: null
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [workshop-slides-promptotyping-pre-workshop.txt, ../2025-09-08-cologne-llm-dh-summer-school/profile.md, ../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/additional-past-instances.md]
---

# Workshop Profile Freiburg DHLab Pre-Workshop 2025

## Profile

This instance was taught on 2025-09-24 from 10:00 to 11:30 for the DHLab in Freiburg, in German, as a ninety-minute online-capable preparation unit. The title slide states event, date and time block, and it names no host beyond the lab, so the university behind the lab is not documented in any artefact of this profile.

The unit has a declared purpose rather than a subject of its own. It prepares participants for a full-day Promptotyping workshop on 2025-10-08 by conveying the method concepts, by introducing the working mode with frontier models and by clearing technical problems in advance. The stated goal is a uniform baseline as the basis for the practice day. That makes this the only instance of the teaching line that exists as a setup unit for another instance, and the shortest delivered instance by a wide margin.

The Cologne summer school of the same month appears inside this deck as the reference outcome, with the claim that participants there built working prototypes of TEI-XML-based digital editions from their own sources within a day and a half, and with the statement that the same result is the goal of the following full-day workshop on arbitrary source data.

The authoritative content state of this instance is the slide-text export in this folder. It documents a delivered state and is not maintained further.

## Module mapping

The mapping is derived from the slide sequence of `workshop-slides-promptotyping-pre-workshop.txt` against the five master modules. Coverage is deliberately narrow, because ninety minutes of preparation carry the method and the toolchain while the technical fundamentals stay at the level the practice day needs.

| Master module | Slide-text sections drawn on | Depth and emphasis |
| --- | --- | --- |
| 1 Understanding Large Language Models | The context-window definition with its rule of thumb that fewer tokens work better and the sweet-spot formulation; the frontier-model list in the prerequisites, naming four providers and their access routes; a personal-assessment slide on the proximity of capability thresholds and on concentration of power in the technology industry, backed by a task-horizon measurement study and an industry interview | Touched only. The module appears as the minimum a participant needs to reason about token budgets and to choose a model, and it carries no architecture, tokenization or training content |
| 2 Prompt Engineering | The extraction prompt of the demonstration, with a delimiter block, source metadata, an explicit instruction and a compact-and-formal style requirement; the follow-up prompts with the stated rule that follow-ups must be adapted and the goal actively steered; the initiating prompt of the quickstart, which has the model ask its own clarifying questions before starting | Present as demonstrated practice rather than as a taught technique catalogue. No slide names a prompting technique by name, and the prompt anatomy is shown by working through one example |
| 3 Knowledge and Context Engineering | Context window and context rot as the two fundamentals, the latter with its source; the Markdown slide with the three reasons it suits language models, meaning presence in training data, token efficiency and the separation of structure from content; the structures-LLMs-understand demonstration that turns a flat commodity taxonomy into a Markdown hierarchy; the promptotyping documents and the project structure; the context-engineering slide that assembles `data.md`, `context.md`, `user-stories.md` and `architecture.md` into one request; the four worked documents themselves, given in full | The conceptual centre of the session and the reason it exists as a separate unit. The four worked documents are reproduced completely, so this export is one of the two places in the delivered material that shows a full project knowledge base rather than describing one |
| 4 Agentic Engineering | The Promptotyping definition as fast, researcher-centred, research-data-driven prototype construction with frontier models, illustrated by three prototypes with their build times and the model used; the demonstration that extracts source structure into a `DATA.md`; Scholar-Centred Design derived from User-Centred Design with the four phases and their feedback loop; user stories turned into a requirements document; the three-way distinction of vibe coding, Promptotyping and agentic coding; the quickstart from the host lab's public repository; the Promptotyping journal as the documentation artefact; the closing summary with its three working rules | The method centre. Agentic coding harnesses are named in the prerequisites and appear in the three-way distinction, and the session operates no agent itself, which is consistent with its preparation function |
| 5 Critical Perspectives and Governance | The expert-in-the-loop element of the closing summary, which lists error message, expert judgement, screenshot and logging as the four feedback channels back into the model; the reference to the author's own critique of vibe coding; the capability and power-concentration slide | Thinnest module of this instance. Verification, validation and governance are absent as a block, and what remains is the working principle that a human judgement belongs in the loop |

## Workshop-specific content

### Prerequisites as the actual deliverable

One slide carries the operative content of the unit. It requires a working installation of an editor with a live-server extension, working frontier-model access for every participant with four named providers, an installed Python that can run scripts from a terminal, very basic web development knowledge, familiarity with the browser as a development tool, optionally a version-control account with its desktop client, and access to an agentic coding harness. The unit is written so that a participant who cannot satisfy one of these items raises it here rather than on the practice day.

### Material brief

A second operative slide asks what participants must prepare, and it answers on one worked example of a small Neo-Latin poetry edition. The requirements are a transcription in a word-processor file with basic structure preserved, a facsimile in an image format, an accompanying contextual or introductory text and a research question. The last item is set off from the rest, which makes the brief a research-design requirement as much as a data requirement.

### Web technology primer

The unit teaches the three web technologies at the level of one example each, so that participants can read what a model generates. The framing is that a frontier model produces a complete interactive web document in a single file, which is what the practice day builds.

### Version control block

The closing block introduces version control from the problem it solves, then the desktop client, the initial clone and the four-step working cycle of pull, edit, commit and push, with the rule to pull before starting and push after finishing. It is written for participants with no prior exposure and is marked optional in the prerequisites.

### Schedule

The title slide states the time block of 10:00 to 11:30. No internal timing exists, and the slide order is the taught sequence.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Slide text (DE) | `workshop-slides-promptotyping-pre-workshop.txt` in this folder | delivered state of 2025-09-24, the authoritative content record of this instance |
| Live deck | not identified | the export carries no deck URL of its own |
| Script or lecture manuscript | none named | absent, and consistent with the length of the unit |
| Promptotyping quickstart | public repository of the host lab, linked in the export | maintained outside this repo |
| Promptotyping journal example | public repository of the demonstration edition, linked in the export | maintained outside this repo |
| Cover | `docs/assets/covers/2025-09-24-freiburg-dhlab-preworkshop.png` | absent |

The export names no Google Slides deck and no Google Doc script, and the link inventory in `knowledge/drafts/google-artefacts.md` holds no artefact for this instance, so both register fields stay null.

### Provenance and cleaning

The export was copied unchanged from the folder `Teaching/HEDIT-Workshop 2025/` of the operator's research vault, where it lies alongside the six Cologne exports as a reference deck rather than as material of the workshop the folder is named after.

The file was checked for embedded URLs carrying an `ouid=` or `authuser=` query parameter. None was found, so no query parameter was stripped and the export is byte-identical to the vault original. The two Google URLs it contains are product entry points rather than documents, and no Drive folder or shared document is linked. Personal names inside the slide text are research data and stay untouched.

## Delivery notes

Taught on 2025-09-24 in German as a ninety-minute preparation unit for the DHLab in Freiburg. Delivery ran on slides with one live demonstration, the extraction of source structure from a historical ledger into a compressed data document with a chain of follow-up prompts, and it closed on a version-control block for participants without prior exposure.

Open points that the source does not settle.

- No workshop document for this instance exists in the operator's research vault, so date, host and format rest on the title slide alone.
- The institution behind the lab is not named in any artefact of this profile.
- Participant count and delivery mode, meaning on site or online, are undocumented.
- The full-day workshop of 2025-10-08 that this unit prepares is named in the export and is absent from the register. Whether it belongs there is an operator decision, and no slide-text export of it has been found.
