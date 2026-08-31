---
title: "Workshop Profile KUG Summer School 2026"
workshop:
  id: 2026-09-16-kug-m3gim
  dates: 2026-09-16/17
  title: "Making Estate Materials Digitally Accessible"
  event: "KUG Summer School 2026, University of Music and Performing Arts Graz"
  audience: "KUG Summer School participants"
  language: en
  status: planned
status: ready for rehearsal
created: 2026-08-20
updated: 2026-08-31
language: en
authors: [Christopher Pollin]
related: [../../knowledge/project.md, ../../slides/full-slide-deck.md, ../../script/full-lecture-notes-en.md]
---

# Workshop Profile KUG Summer School 2026

## Profile

*Making Estate Materials Digitally Accessible: Research Data Workflows with Large Language Models and Promptotyping* is a four-part workshop for the KUG Summer School 2026. The sessions form one research data workflow. Wednesday explains how a digitised estate object becomes a documented, structured, linked, preserved, and accessible research resource. Thursday applies this workflow to M³GIM material, introduces large language models, produces structured data from digitised objects, and develops a small digital research application through Promptotyping.

All slides, lecture notes, prompts, task descriptions, and participant materials for this workshop are in English. The spoken teaching language remains to be confirmed.

## Session sequence

| Date and time | Session | Function | Result |
| --- | --- | --- | --- |
| Wednesday, 16 September, 17:00–19:00 | *Making Estate Materials Digitally Accessible: The Stefan Zweig Digital Workflow* | Trace an archival object through digitisation, metadata, TEI XML, data modelling, authority data, Semantic Web and Linked Open Data, repository ingest, and platform publication. | Participants can locate individual modelling and infrastructure decisions within a complete source-to-platform workflow. |
| Thursday, 17 September, 11:30–13:00 | *Large Language Models in Research Data Workflows* | Explain language and multimodal models, AI readiness, context, evidence, and suitable roles for generative AI in research data work. | Participants can identify tasks that a model can support and define the checks required for research use. |
| Thursday, 17 September, 15:00–16:30 | *Sources into Data: OCR and Information Extraction with Gemini* | Transcribe selected pages from the Bayreuth Festival 1953 source packet, extract occurrences and participations, and compare claims from daily programmes, season lists, and biographies. | Participants produce a checked source-specific data extract with page evidence, functions, stage roles, and uncertainty. |
| Thursday, 17 September, 17:00–18:30 | *Promptotyping Research Data: Building a Digital Research Application* | Translate a human-validated Bayreuth dataset into requirements, views, and a small cast explorer. | Participants evaluate whether the application preserves source type, evidence, uncertainty, and multiple roles within one participation. |

## Cases and continuity

Stefan Zweig Digital is the explanatory case on Wednesday. It provides an existing infrastructure and a traceable route from estate material to a published research platform. M³GIM is the working dataset on Thursday. The hands-on units use seven Bayreuth Festival 1953 source objects. Six are performance programme booklets. One documents the season across schedules, cast matrices, staff lists, and biographies.

The source packet supports one delimited question: *How do daily programmes, season lists, and biographies represent who was announced to do what at the Bayreuth Festival in 1953?* The question is answerable from the supplied pages and exposes a substantive modelling problem. A daily programme, a season list, and a biography describe related assignments at different documentary levels. They require separate evidence types and must not be merged silently.

The participant exercise uses a controlled subset. One page from source 3 demonstrates transcription and known record errors. Sources 7 and 8 provide regular cast structures. Source 10 contains a participation with two stage roles in one occurrence. Source 11 adds the season-level list *Wer singt was?* Selected pages from source 12 support cross-source comparison. Sources 9 and the remaining pages of source 12 remain extension material.

The placement of the digital edition and TEI XML session before this workshop is pedagogically useful. Participants can recognise TEI XML as one component of the larger research data workflow instead of encountering it only as an isolated format.

## Relationship to the Full Teaching Material

This specialization draws on the shared teaching line without duplicating its general explanations.

| Shared module | Use in this workshop |
| --- | --- |
| Understanding Large Language Models | Model basics, context, multimodality, limitations, and evidence-sensitive use. |
| Prompt Engineering | Task definition, output schemas, examples, constraints, and validation prompts in the hands-on unit. |
| Knowledge and Context Engineering | Research data as documented transformation, knowledge files, authority data, provenance, and explicit project constraints. |
| Agentic Engineering | Promptotyping as a repository-based method for turning structured research data into a tested digital artefact. |
| Critical Perspectives and Governance | Source rights, uncertainty, verification, traceability, and the limits of generated output. |

The Stefan Zweig workflow and the M³GIM exercise chain are instance-specific. Reusable definitions and method blocks remain anchored in the Full Slide Deck and Full Lecture Notes.

## Material state

| Artefact | Location | State |
| --- | --- | --- |
| English course reader | [Google Doc](https://docs.google.com/document/d/1DU6UbE4xURFZ3fkPn7MD2loZ2naPysFYX1ypeI0D_Kg/edit) and [repository text](lecture-notes.md) | repository text updated for the Bayreuth case; Google Doc still reflects the earlier generic exercise |
| Canonical English KUG slide content | [repository Markdown](slide-deck.md) | content complete; functional rehearsal and user acceptance remain open |
| Earlier native presentation | [Google Slides](https://docs.google.com/presentation/d/1m9c6RAUKz_4QTaICfMf11CPmjOY3H-SnFA26UEWkXkU/edit) | retained unchanged as a visual reference; Bayreuth revisions are not synchronised into it |
| Exercise prompts | [Google Drive](https://drive.google.com/file/d/1HGzaJ4XtU2APn40_2YQH6Kj8IaGTJ8_Y/view) | updated and reloaded successfully on 2026-08-31; the exact Gemini run remains to be rehearsed |
| M³GIM source packet | seven Bayreuth Festival 1953 PDFs in controlled local storage | all 40 scan pages inspected through OCR and targeted visual checks; reuse permission remains to be confirmed |
| Reference integration workbook | M³GIM project output with cast, function, participation, and validation sheets | structurally and visually validated; serves as facilitator reference data |
| Public workshop page | generated from the workshop register | still reflects the earlier generic exercise; web synchronisation remains outside this change |

## Required inputs

- Confirmation that the seven supplied Bayreuth digitisates may be shown and processed in the Summer School.
- A facilitator-prepared, human-validated JSON subset derived from the integration workbook.
- A page mapping that connects each participant image to its M³GIM object identifier and scan page or folio identifier.
- One full rehearsal of the exact Gemini prompts on the selected participant images.
- Confirmation of the spoken teaching language.

## Delivery notes

Filled after the workshop is taught.
