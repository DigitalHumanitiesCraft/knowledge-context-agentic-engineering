---
title: "Workshop Profile GDA Göttingen 2026"
workshop:
  id: 2026-10-15-gda-goettingen
  dates: 2026-10-15
  title: Generative KI für Datenaufbereitung, Datenmigration und die Pflege von Interfaces
  event: "Göttinger Digitale Akademie, Akademie der Wissenschaften zu Göttingen"
  audience: staff of academy research projects and library guests
  language: de
  status: planned
status: in preparation
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/specialization-analysis.md, ../../knowledge/drafts/additional-past-instances.md]
---

# Workshop Profile GDA Göttingen 2026

## Profile

This instance is the hybrid half day registered for 2026-10-15, 09:00 to 12:30, so 3.5 hours on site in Göttingen with a parallel Zoom channel. It is taught in German for staff of the academy research projects together with guests from the Göttingen state and university library. The host is the Göttinger Digitale Akademie at the Akademie der Wissenschaften zu Göttingen, in its coordination for digitisation and data curation. The unit is the pre-conference workshop to the closing conference of the academy's digital programme on 15 and 16 October 2026, whose theme pairs sustainability and artificial intelligence. An alternative slot on the afternoon of 16 October was held open.

At 3.5 hours this is the narrowest cut of the seven upcoming instances, and its subject sits closer to research data engineering than to the full arc of the line. The subject is generative AI for the preparation and migration of research data and for the semi-automated maintenance of user interfaces and service endpoints.

The framing argument ties the instance to its conference. Academy projects produce data, editions and interfaces over decades, and at the end of a funding period migration and maintenance fall due. That work is repetitive, rule-governed and source-bound, which is where coding agents carry it. The stated condition is machine-readable project documentation, because what is documented nowhere can be observed by no agent.

The register in `docs/data/workshops.json` holds the entry and carries no deck, script or cover. Unlike the other instances without a deck, this one has its teaching text written. Full slide texts with speaker notes exist in the operator's research vault, adversarially reviewed on 2026-07-18 with all findings resolved, and awaiting operator acceptance.

## Module selection

Derived from the written slide texts, so this mapping rests on taught content rather than on a programme outline. The fine module cut in `knowledge/drafts/module-map.md` is itself a draft.

| Module | Role in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Compact opening. Frontier models at teaching time and the jagged-capability argument, sharpened onto data work, meaning that counting, arithmetic and exact string operations are the unreliable cases. |
| 2 Prompt Engineering | One dedicated slide on formulating a commission to an agent, with the four elements of goal, context, acceptance criteria and constraints, placed immediately before the hands-on as its checklist. |
| 3 Knowledge and Context Engineering | Substantial. Why agents need context, context rot, what belongs in an instruction file, and what a knowledge document and a knowledge vault are. The knowledge vault is the first working step of the hands-on. |
| 4 Agentic Engineering | The centre of the session. What an AI agent is, the agentic loop and how it is shaped, a two-part Claude Code demonstration on data preparation and on interface maintenance, and the hands-on on participants' own material. |
| 5 Critical Perspectives and Governance | Its own slide on checking artefacts against the holdings, with the two checking levels of deterministic and domain-expert, and the critical expert in the loop addressed to the participants themselves. The sustainability framing of the conference carries the same argument. |

The central methodological slide separates agent-written scripts from direct model transformation. The agent characterises the data, writes a transformation script, tests it against known cases and executes both, so the script stays deterministic, repeatable and inspectable and every correction becomes a diff under version control. Token-by-token transformation by the model stays limited to small individually verifiable units such as a single recognised page or a boundary case the script does not cover.

## Case material

Three case studies carry the instance, all of them existing projects.

- A music-archival pipeline that carries spreadsheet holdings into a linked-data model with project-specific extensions and generates an exploration interface, used to show schema mapping and tabular cleaning.
- A library pipeline that runs from PDF scans to TEI in stages, with deterministic schema validation and a human-set workflow status per document, used to place the correction workflow for recognised text.
- A static generator for a review journal that replaces an XML-database infrastructure, whose declarative element mapping in YAML carries most display decisions without touching the code, used to show that data migration and interface maintenance draw on the same toolbox.

The hands-on runs on participants' own material in four steps. Build a knowledge vault with a short instruction file and a document describing the data sample; place the sample and have the agent characterise it; formulate a bounded commission with acceptance criteria; check the result against one's own expertise and run a correction round.

Rights state. The partner institute must clear the demo state for public display before the demonstration can be shown. No further rights encumbrance is documented, because the exercise runs on material the participants bring themselves.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | to be generated from the written slide texts, register field currently null | not created |
| Slide texts with speaker notes | operator's research vault | written and adversarially reviewed 2026-07-18, all findings resolved, operator acceptance pending |
| Lecture Notes (GDA Göttingen 2026) | this folder | in preparation |
| Learning objectives | four, in finished prose | complete |
| Block raster for the morning | arrival, introduction, demo, break, hands-on, discussion | complete at block level, carries no time values |
| Demo script | two parts with a four-step fallback chain, meaning live demonstration, prepared screencast, screenshot sequence in the deck, and a walkable end state through git log and diffs | drafted |
| Cover | `docs/assets/covers/2026-10-15-gda-goettingen.png` | present |

Each fundamentals slide of the written texts carries a provenance field pointing at the slide of the Full Slide Deck it adapts, which is the delta model applied cleanly. Two of the slides are already phrased occasion-free and are candidates for intake into the full corpus rather than into this profile alone, namely the agent-transformation slide and the artefact-checking slide.

A cut from the KUG hands-on material is recorded for this instance, namely the table-cleaning exercise as the centre for preparation and authority-data matching, the pipeline-maintenance angle of the music-archival case as agent-supported maintenance, and the recognition exercise for the interface and endpoint part.

## Open points

The written document marks its own gaps, which are carried over here.

- The demo dataset for part one and the change task for part two are undecided.
- The partner institute has to clear the demo state for public display.
- Screencast fallbacks are unrecorded.
- The Zoom participation format during the hands-on is unresolved and determines supervision planning.
- Setup instructions ahead of the workshop need a dispatch route through the host.
- The fallback dataset for participants without their own material is undecided.
- The handout question is open.
- Two evidence markers flag claims that need either a dated source or removal.
- The commissioning contract is outstanding on the host side, and the sources record checking that state before material is sent.
- The time distribution is fixed nowhere. The block raster carries no time values, and the alternative put to the operator for acceptance, ninety against seventy minutes of hands-on, appears in the document itself nowhere.

## Delivery notes

Filled after the workshop is taught.
