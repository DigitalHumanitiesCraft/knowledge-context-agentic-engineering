---
title: "Workshop Profile Fachschaft Mittelalterstudien Heidelberg 2026"
workshop:
  id: 2026-10-08-fachschaft-mittelalterstudien-heidelberg
  dates: 2026-10-08
  title: Knowledge, Context und Agentic Engineering für die Forschung
  event: "Fachschaft Mittelalterstudien, Universität Heidelberg"
  audience: students and early-career researchers in medieval studies
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

# Workshop Profile Fachschaft Mittelalterstudien Heidelberg 2026

## Profile

This instance is the one-day unit registered for 2026-10-08 at the Universität Heidelberg, commissioned by the student council of medieval studies and funded from quality-assurance funds. The date was fixed on 2026-08-05. It is taught in German for students and early-career researchers in medieval studies, in the rooms of the student council, under the title *Knowledge, Context und Agentic Engineering für die Forschung*, which is the German form of the title of the teaching line. This gives the instance the strongest title claim of the seven.

The day opens on the fundamentals of large language models and AI agents and then works practically in Claude Code throughout, spanning the build-up of structured project knowledge to agentic work on a research-adjacent example. Participants obtain their own access to a frontier subscription, a decision taken by the student council on 2026-08-05. No hour grid is documented in any source.

Two further respondents from the Heidelberg environment, both with a focus on local and open-source models, attend the day. Whether they receive a block of their own is undecided.

The register in `docs/data/workshops.json` holds the entry and carries no deck, script or cover. This profile documents the cut and the source state. The teaching text does not exist yet.

## Module selection

Derived from the concept and the hands-on design held in the sources. It is a derivation and no confirmed cut exists. The fine module cut in `knowledge/drafts/module-map.md` is itself a draft.

| Module | Role in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Opening block, covering the fundamentals of models and of AI agents as the conceptual entry the audience needs. |
| 2 Prompt Engineering | Implied by the hands-on work rather than programmed. No source names a prompt-engineering unit for this instance. Inference from the hands-on design. |
| 3 Knowledge and Context Engineering | The build-up of structured project knowledge, which the title of the instance names explicitly. |
| 4 Agentic Engineering | The centre of the day. Practical work in Claude Code across the full arc from source to edition, which makes this the emphasis of the instance. |
| 5 Critical Perspectives and Governance | Present inside the hands-on design rather than as a block. The recommended exercise format has participants check a prepared model transcription against facsimile and TEI ground truth, which teaches verification by having them perform it. Inference from the exercise design. |

## Hands-on

A small TEI and handwriting-recognition project on roughly ten charters that share persons or organisations, decided on 2026-08-05. It produces recognition output, TEI markup, a person and organisation index and a small static edition, so the full arc from source to edition runs within one day. The instance operates a harness throughout, which sets its prerequisites and separates it from the browser-only instances of the line.

The source finding of 2026-08-05 shapes the exercise. The first volume of the town-book corpus, covering 1395 to 1400, carries no facsimile references, and digitisates through Monasterium exist only in a Vienna charter corpus covering 1177 to 1414. Two justified ten-item sets are prepared from that corpus. The primary proposal is a family holding of 1382 to 1414 with three connecting persons, whose legal transactions run from a court claim through an inheritance division and a house sale to a mass endowment, and whose facsimile URLs are documented in full. The alternative is a chapel holding of 1385 to 1412.

The script of the example facsimile is late-Gothic chancery cursive in very good preservation, which is the most favourable handwritten case for vision models. A roughly legible but systematically faulty transcription is therefore the expected output. The recommended exercise format follows from that expectation, namely that participants check a prepared model transcription against facsimile and TEI ground truth, with a live round trip through their own accounts as an option.

## Rights state

This is the tightest rights gate among the upcoming instances, because the hands-on cannot run without the images. Inference from the dependency of the exercise on the facsimiles.

The licence file of the source corpus names CC BY 4.0 with copyright at the Universität Wien and is marked pending. The Monasterium image rights are not documented in the source repository at all. Both need clearing before any distribution to participants. The participant data folder therefore must not be published, and its URL is deliberately not reproduced in this public repository.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | a copy of the Full Slide Deck exists in the operator's Drive, created 2026-08-05 | unadapted. The register field stays null and the URL is not published here, because the copy currently holds full-corpus material under the name of this instance |
| Slide texts | none | to be written in Markdown and transferred to the deck by the operator |
| Lecture Notes (Fachschaft Mittelalterstudien Heidelberg 2026) | this folder | in preparation |
| Drive folder and participant data folder | operator's Drive | exist, URLs deliberately not reproduced here, publication blocked by the rights gate |
| Mini repository with instruction layer and `knowledge/` folder | not created | planned |
| Term apparatus | drawn from the glossary of the full corpus and the Promptotyping paper definitions | available |
| Cover | `docs/assets/covers/2026-10-08-fachschaft-mittelalterstudien-heidelberg.png` | present |

## Open points

- Two standing operator decisions, namely switching the hands-on base to the primary charter set and fixing the checking format.
- Whether the two additional respondents receive a block of their own.
- The licence request and the image-rights request, both of which gate the hands-on.
- Populating the data folder and setting up the mini repository with its instruction layer and `knowledge/` folder.
- The adaptation of the deck copy to this instance.
- The hour grid for the day is undocumented.

## Delivery notes

Filled after the workshop is taught.
