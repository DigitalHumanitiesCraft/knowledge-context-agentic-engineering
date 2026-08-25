---
title: VetMedAI Teaching Material Intake
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../project.md, ../governance.md, ../terms.md, slides-map.md]
---

# VetMedAI Teaching Material Intake

Source intake from four delivered VetMedAI workshops. It identifies material that may support Modules 03–05 of *Knowledge, Context and Agentic Engineering for Knowledge Work*. The findings have not been accepted into the Full Slide Deck, Full Lecture Notes or a workshop profile. Reuse requires substantive review, source verification and the applicable rights decision.

## Evidence base

The audit compared the native Google Slides decks with the corresponding workshop records in the project vault. The Google artifacts are derived teaching surfaces under repository governance. Their identifiers and inspected revisions provide stable references to the audited state.

| Workshop deck | Google Slides ID | Inspected revision | Slides | Supporting vault record |
| --- | --- | --- | ---: | --- |
| Workshop 3, *Overview of Tools and Technologies* | `1MaOKMQreml-R2i5thyMCpeStTD4p0L9qpDTuIDghOLI` | `JCKS_COivjKYIQ` | 47 | `Projects/VeTMedAI/Workshops/WS3 Überblick Tools und Technologien.md` |
| Workshop 4, *Use Cases and Multimodal Applications* | `1yTBnkJ1MGEJjQKxlzM0zInZwdUjokLWh7FJgt7y45oY` | `kwnFtgh_9lNJ4w` | 32 | `Projects/VeTMedAI/Workshops/WS4 Use Cases und multimodale Anwendungen.md` |
| Workshop 5, *Data Analysis for Administration* | `1JrVoKaAQE0wYqtP3_jMnEuBgt_Qhc9aoFU-JmGmeOVU` | `DXBtzshLyut2Mw` | 33 | `Projects/VeTMedAI/Workshops/WS5 Datenanalyse Verwaltung.md` |
| Workshop 6, *Data Analysis for Research* | `12_boMph933qCBTGnlZtLysr37DOEFJ9exf9vNwUz6vA` | `khmkUdJD1U83VA` | 36 | `Projects/VeTMedAI/Workshops/WS6 Datenanalyse Wissenschaft.md` and its slide-by-slide lecture script |

The records have unequal maturity. The Workshop 3 record is an early draft that does not document the full 47-slide deck. The Workshop 4 and Workshop 5 records describe the delivered teaching sequences. The Workshop 6 project overview and detailed lecture script confirm delivery, while its short workshop record still contains draft language and unresolved preparation notes. Deck evidence therefore remains primary for Workshop 3, while the later decks can be read together with their fuller records.

## Reusable concepts for Modules 03–05

### Module 03, Knowledge and Context Engineering

- **Retrieval and context architectures.** Workshop 3, slides 16–19, distinguishes long-context, retrieval-first and hybrid approaches and identifies silent retrieval failure, isolated snippets and missing evidence as operational risks.
- **Knowledge mechanisms.** Workshop 3, slides 24–27, compares RAG, Skills, fine-tuning and MCP. The MCP account needs revision because the protocol can expose resources as well as tool calls.
- **Functional knowledge documents.** Workshop 5, slides 15–18 and 22–26, shows how a `DATA.md` records files, sheets, headers, keys, temporal mismatches, cleaning hazards and aggregation risks before analysis.
- **Separated data and method context.** Workshop 6, slides 13–16, uses `data.md` for the data contract and `research.md` for sourced methodological knowledge. A journal records the resulting transformations.
- **Multimodal extraction and provenance.** Workshop 4, slides 20–31, follows digitised sources through transcription, structured representation and source checking. Its strongest prompt pattern separates observation, inference and contextual metadata.

### Module 04, Agentic Engineering

- **Agent and harness architecture.** Workshop 3, slides 21 and 32–35, presents an agent as a model operating through a loop with tools, memory, permissions and procedural resources.
- **Inspectable implementation cycle.** Workshop 3, slides 42–47, connects source access, a maintained knowledge document, requirements, planning, implementation, browser inspection and documented write-back.
- **Tool-mediated extraction.** Workshop 4, slides 22–28, treats image acquisition, transcription and transformation into TXT, JSON and CSV as an executable pipeline with model and deterministic checks.
- **Permissions and intermediate artifacts.** Workshop 5, slides 27–29, demonstrates terminal operations, permission gates, planning and reviewable generated files in an agentic data-analysis task.
- **Agentic research.** Workshop 6, slides 8–16, describes Deep Research as iterative decomposition, search, comparison and synthesis. It separates model opacity from process opacity that workflow design can address.
- **Specification and coordinated execution.** Workshop 6, slides 17–25, connects purpose, data contracts, user stories, tests, subagents and a local application while retaining a project journal.

### Module 05, Critical Perspectives and Governance

- **Critical expert and verification condition.** Workshop 5, slide 24, and Workshop 6, slides 5–6 and 13–16, make domain expertise and explicit verification conditions part of the workflow rather than a final review gesture.
- **Research integrity and disclosure.** Workshop 6, slides 2–8, connects delegated work with transparency, responsibility, documented use and verification milestones.
- **Infrastructure and digital sovereignty.** Workshop 4, slides 18 and 31–32, compares frontier services with local specialist tools through fitness for purpose, competence requirements and infrastructure dependencies.
- **Privacy and permission boundaries.** Workshop 3, slide 23, and the Workshop 5 agentic demonstration identify data access, retention claims and filesystem scope as governance questions.
- **Automation narratives and asymmetric amplification.** Workshop 3, slides 4–8, and Workshop 5, slides 11–14, provide material for examining the inference from capability demonstrations to claims about automated research and institutional change.

## Deep-dive candidates

### 1. Retrieval architectures and silent failure

Use Workshop 3, slides 16–19, to compare long-context, retrieval-first and hybrid systems. A deep dive should ask participants to identify what a response omits when retrieval returns plausible fragments while hiding missing evidence. Product-specific architectural claims should be replaced with verified technical examples.

### 2. RAG, Skills, fine-tuning and MCP as distinct mechanisms

Use Workshop 3, slides 24–27, as the starting classification. The revised treatment should distinguish retrieved factual context, persistent procedural instructions, learned model behaviour and protocol-mediated access to tools or resources. A classification exercise can test which mechanism supplies knowledge, procedure or action capacity in a concrete workflow.

### 3. Data contract and method context as paired knowledge documents

Combine Workshop 5's `DATA.md` sequence with Workshop 6's `data.md` and `research.md`. Participants first document structure, keys, quality issues and permissible transformations, then attach sourced methodological knowledge. The pair becomes the maintained context for an analysis rather than a transient collection of uploaded files.

### 4. Provenance-bearing multimodal extraction

Use Workshop 4, slides 20–31, for a source-to-data workflow. The exercise should preserve the source image, unchanged transcription, structured output, transformation rules, uncertainty markers and a checked link back to the source segment. Deterministic plausibility checks and scholarly source checking remain separate operations.

### 5. Agentic implementation with verification and write-back

Use Workshop 3, slides 42–47, together with Workshop 5, slides 27–29. The deep dive should move from a bounded source through knowledge distillation and explicit requirements to a local implementation, browser inspection and a documented correction of the maintained knowledge. Permission choices and failed checks remain visible in the record.

### 6. Deep Research with process evidence and expert gates

Use Workshop 6, slides 6–16. The unit should compare an opaque generated report with a workflow that records the research question, search scope, selection criteria, extracted claims, sources and expert decisions. This supports Module 04's account of agentic research and Module 05's distinction between generated evidence, technical checks and substantive acceptance.

## Rights and volatility limits

- Shared access to a Google Slides deck does not establish a public reuse licence.
- The vault records cite the workshop series through Zenodo DOI `10.5281/zenodo.10647754`, version 1.3.0. The licence and exact contents of that deposit require inspection before reuse.
- A source-specific open licence covers only the identified source item. It does not extend automatically to the surrounding slide, the deck or an export.
- Third-party screenshots, logos, press images, product interfaces, video material and quoted visual sources require individual review. AI-generated images in the decks have a general disclosure, while their generation records and publication rights were not established in this audit.
- Product names, model capabilities, pricing, access tiers, context limits, benchmarks, privacy and retention terms, connector behaviour and remote-control features are dated claims. They require verification against current primary documentation before teaching use.
- Legal claims about the European Union AI Act require specialist review before publication or instruction. The current deck wording should be treated as a dated workshop interpretation.
- Exact processing costs, token estimates and energy comparisons are unsuitable for transfer without a dated calculation and a documented source basis.
- Workshop 3's harness definition was generated from video transcripts according to the deck. Its wording requires reconstruction from primary sources rather than direct reuse.
- Public teaching should link to third-party visual material unless a documented right permits copying it into the repository.

## Intake status

This document records candidate evidence and teaching patterns. It establishes no canonical terminology, module allocation, licence extension or publication decision. Acceptance requires comparison with the maintained module text, verification of every retained claim against its primary source, rights review for embedded material and a Research Director decision on integration.
