---
title: Module Cut Coverage
status: draft
created: 2026-08-20
language: en
covers: script/modules/
---

# Module Cut Coverage

## Status of these files

The five files in `script/modules/` are draft-canonical. They hold the text of the full corpus cut into the five modules of the teaching line, assembled from `script/full-lecture-notes-de.md` and `script/full-lecture-notes-en.md` by exact passage, without rewriting, summarising or translating. Both Full Lecture Notes files are untouched and remain the authoritative source. The module cut is an operator gate. Once the operator confirms it, the modules become canonical and the Full Lecture Notes retire.

Each unit of the nineteen-unit fine cut in `knowledge/drafts/module-map.md` was assigned one language version. Where both Full Lecture Notes cover a unit, the fuller version was carried and the other one is recorded below under parallel versions not carried. Material that exists only in the CLARIAH-AT lecture notes was not copied, because it is profile material; it is recorded as a gap.

## Unit coverage

| Unit | Module file | Source carried | Completeness | Exists only in profile material |
| --- | --- | --- | --- | --- |
| M1 Applied Generative AI in Research Data Workflows | module-01 | DE abstract, "Zu diesem Skriptum", 1.1, 1.2, 1.4, 1.5; EN "Applied Generative AI for Research Data Workflows" | full | the working-group framing attached to the term |
| M2 Research Data, Representation and Provenance | module-01 | EN "Humanities Research Data Are Constructed through Scholarly Workflows", EN "Two AI Supported Research Data Workflows & Epistemic Infrastructures" | partial | the two production workflows in detail, with OCR provider, local layout analysis, TEI transformation, entity enrichment, preserved image-text relation, character error rate and the frontend and repository links |
| M3 The Current LLM Capability Landscape | module-01 | EN "Which Frontier Models and AI Technologies Do You Use?" | partial | openness as a multidimensional property, the Open Source AI Definition, the European Open Source AI Index, open-washing, local deployment against hosted access with its governance trade-off, and the closing four dimensions of capability, openness, deployment and agentic integration |
| M4 Asymmetric Amplification and the Capability Frontier | module-01 | EN "Frontier LLMs Asymmetrically Amplify Computational Research" | partial | the developed benchmark evidence with task horizons, interactive benchmark scores, formal theorem proving, cyber evaluations and scenario work, the cyber governance dilemma, the practice-based observation, and the closing jaggedness argument against naive extrapolation and against dismissal |
| M5 What an LLM Is | module-01 | EN "LLMs as Jagged Alien Intelligences" through "Embeddings and Contextual Representations", the latent-program-space section, the mechanistic-interpretability excursus, the training and assistant-character sections | full | confabulation named as a term, and reasoning with test-time compute developed as internal search rather than listed in the terminology |
| M6 The Four Engineering Layers | module-01 and module-05 | DE 1.3 with figure 1; the layer table and the closing formula sit in DE chapter 8 in module 5 | full | none |
| M7 Prompt Engineering | module-02 | DE 3.1 through 3.5, 3.7, 3.8; EN "Prompting Strategies: There Is No Prompt to Rule Them All" | full | the four-part working structure of task, context, rules and output as an explicit didactic block |
| M8 Context Engineering | module-03 | DE 4.1 through 4.6 | full | none |
| M9 Knowledge Engineering and Knowledge Documents | module-03 | EN "Knowledge & Context Engineering"; DE 5.1 through 5.8; EN "Knowledge Modelling, Personal Information Management and Project Management" | full | none |
| M10 Agentic Engineering, AI Harnesses and Controlled Agent Workflows | module-04 | DE 2.3, 2.4, 6.1 through 6.7; EN "AI Agents Existed Long Before LLMs", "AI Harness Architecture", "AI Agent Concepts", the instruction-file and skill sections, "Model Routing", "Subagents and Epistemic Infrastructure" | partial | none |
| M11 Working Environment, API Access and Structured Output | module-02 | EN "Prepare the Working Environment before the First Prompt", EN ".txt to JSON to CSV"; structured output also in DE 3.4, carried under M7 | partial | API access as the move from a conversational interface to a pipeline component, and model-assisted review inside a harness with the rule that model agreement is not scholarly verification |
| M12 Promptotyping and Scholar-Centred Design | module-04 | DE 7.1 through 7.6, 7.9, 7.10; EN "As a ... I Want to", "Mapping Mobile Musicians", "Spec Driven Development" | full | none |
| M13 Verification, Validation and the Critical Expert | module-05 | DE 7.7, 7.8, 7.11 | partial | the three-way naming of evaluation, validation and scholarly verification with its worked examples of character error rate, schema validation and authority-record comparison |
| M14 From Facsimile to a Research Data Package | module-02 | EN "Multimodality & Vision Language Models" | partial | the conceptual question whether the task is OCR, HTR or something technically different |
| M15 Case Study Hersch | none | missing | missing | the production workflow narrative; the executable tutorial lives in the external hands-on repository |
| M16 Case Study Zweig | module-02 | EN "Transcribe a Facsimile with Gemini 3.7 Flash", "Hands on 1", "Hands on 1 (Example Result)" | partial | the reusable prompt skeleton with its placeholder slots, the catalogue metadata block, the worked context example and the critical review with its conceptual question |
| M17 Topic Annotation and Statistical Topic Modeling | none | missing | missing | nothing; the unit is absent from the Full Lecture Notes and from the CLARIAH-AT lecture notes |
| M18 Project Governance and Research Mission Control | module-05, unit heading only | missing | missing | nothing; the unit is absent from the Full Lecture Notes and from the CLARIAH-AT lecture notes |
| M19 Limits, Glossary and Apparatus | module-05 | DE chapters 8, 9 and 10; EN "References" and the four appendix templates | partial | none |

Three units carry no text from the Full Lecture Notes at all. M15 and M17 have no unit heading in any module. M18 carries a unit heading in module 5 with a note that points at the adjacent material, so that the gap stays visible in the reading order.

What is missing from both Full Lecture Notes, independent of the profile material:

- M2, the data levels of primary, intermediate, meta and para data, provenance as a formalism with PROV-O classes and the Web Annotation Data Model, the minimal provenance record, and the dataset-description and governance frameworks alongside FAIR
- M10, run identities and hashes, unchanged raw outputs, hooks and observability in the harness definition, and subagents with separate write territories
- M13, the five-function checking architecture with its authority column, assessment result and scholarly decision as separate objects, the status value as their projection, the three status axes, and acceptance held apart from publication
- M14, the pipeline beyond the transcription step, meaning segmentation as a research decision, named entities with the null rule for unverified authority data, evidence-bound topic annotation, the JSON schema as an executable data contract, and the package layout with its rights gate
- M19, a limits section as such, the reproducibility requirements for a documented run, the legal and ethical gates before publication, and a glossary separate from the summary chapter

## Parallel versions not carried

One version per unit was kept. The other version stays in its Full Lecture Notes file and is listed here with what it adds, so that the operator can decide whether a passage should be merged into the kept unit or become a translation input.

| Unit | Version kept | Version not carried | What the discarded version adds |
| --- | --- | --- | --- |
| M1 | DE abstract and "Zu diesem Skriptum" | EN "Abstract", EN "About These Lecture Notes" | the framing of the full corpus around knowledge work rather than one disciplinary field, which no German passage states |
| M6 | DE 1.3 | EN "Learning Objectives and Core Concepts" | cited definitions of the four layers, and the paired definitions of AI agent and AI harness |
| M5 | EN sections | DE 2.1, 2.2, 3.6 | figures 3, 7 and 8 with their captions, and the German formulation of the latent-program-space metaphor |
| M7 | DE 3.1 through 3.5, 3.7, 3.8 | EN "Prompt Engineering", EN "Prompting Is Weird, and Keeps Changing", EN "Persona Engineering" | the three organising claims of the prompt chapter, and the persona as a structured perspective for evaluation work |
| M8 | DE 4.1 through 4.6 | EN "Context Engineering", "Context Engineering Shapes the Model's Working Context", "Context Rot", "Selecting, Structuring and Distilling Knowledge", "Why AI Agents Need Context", "Context Window, Context Rot and Distillation" | the definition of in-context learning, and the three-level architecture diagram of knowledge base, working context and context window |
| M9 | DE 5.1 through 5.8 | EN "Knowledge Engineering", "I Know Things", "Why Knowledge Must Be Made Explicit", "Markdown Makes Document Structure Explicit for LLMs", "Knowledge Documents", "Project Knowledge Base and Working Context" | the five named properties of a usable knowledge document, the gap between knowledge possessed and knowledge operationally available, and the statement that the knowledge document is the concept while Markdown is one serialization |
| M10 | DE 6.1 through 6.7 | EN "Agentic Engineering", "Why Multi Step Work Must Be Organised", "AI Harness", "AI Agent", "Tool Use", "Model Context Protocol (MCP)", "A2A (Agent to Agent)", "Subagents" | the shift from response to trajectory, and dedicated treatments of the protocol layer that the German chapter compresses into one section |
| M12 | DE 7.1 through 7.6, 7.9, 7.10 | EN "Promptotyping", "Promptotyping as an Iterative Knowledge Loop", "Scholar Centred Design and Requirements Engineering" | the diagram of the knowledge loop from maintained knowledge through working context, agentic implementation, artefact and evaluation to curated write-back |
| M13 | DE 7.7, 7.8, 7.11 | EN "Evaluation, Verification, Validation and Acceptance", EN "Critical Expert and Epistemic Infrastructure" | evaluation as a fourth assessment category beside verification, validation and acceptance, and the critical expert defined as the role that designs and maintains the epistemic conditions |
| M19 | DE chapters 8, 9 and 10, plus EN references and appendix templates | EN "Conclusion" | the closing statement on asymmetric amplification and on the design of complete technical and epistemic environments |

## Material carried beyond the module map

The English Full Lecture Notes hold a block on how large language models work, covering the training objective against the acquired capabilities, the Transformer architecture, pretraining and posttraining, parametric knowledge against retrievable and contextual information, tokenization, and embeddings with contextual representations. The nineteen-unit map has no unit for it, because the map was drafted against the CLARIAH-AT lecture notes, which do not contain it. It is carried in module 1 under M5 and needs either its own unit id or an explicit widening of M5.

## Deliberate omissions from the Full Lecture Notes

These passages were not carried into any module. Beyond them and the parallel versions listed above, nothing from either of the Full Lecture Notes was dropped, and no passage appears twice.

- the title, author and deck block of both Full Lecture Notes
- the German table of contents and the German list of figures, because they index the monolith; the figure captions themselves are carried in place
- the German chapter-container headings for chapters 1 to 7, which the module and unit headings replace; the numbered subsection headings are carried unchanged, so every passage remains traceable to its chapter

## Known issues in the assembled files

- The prompt examples, the knowledge-document example and the templates in the German Full Lecture Notes carry escaped Markdown from a document export, meaning backslashes before hyphens, hashes and angle brackets, together with empty HTML anchors. They are reproduced unchanged, because cleaning them would alter the source text.
- Unit headings sit at level two, the same level as the source section headings, so each module runs two heading families at one level.
- Footnote identifiers keep the numbering of their source lecture notes. A footnote referenced from several modules has its definition repeated in each of them; identifier 12 of the English Full Lecture Notes appears in modules 1, 2 and 4. The German and English identifier spaces do not collide in any module.
- Module 5 carries both bibliographies and both sets of templates. They are apparatus and not parallel translations of one another. The German list carries two works the English list omits entirely and several that the English Full Lecture Notes cite only in footnotes, while the English appendix templates carry fields the German ones do not.

## Open questions for the fine-cut confirmation

1. The chapter references in `knowledge/drafts/module-map.md` do not resolve against `script/full-lecture-notes-de.md`. The map was drafted against a ten-chapter Skriptum in the vault that runs from research data through the four engineering layers, the facsimile pipeline, the Hersch tutorial, topic modeling and project governance to the apparatus. The German Full Lecture Notes in this repo run from an introduction through LLM foundations, prompt, context, knowledge and agentic engineering to promptotyping, a summary, a bibliography and templates. Seven units depend on which document is the German source, M2, M11, M13, M14, M15, M17 and M18. Either the vault Skriptum enters the repo as a second German source, or the source column of the map is rewritten against the German Full Lecture Notes here.
2. The five modules and the nineteen units do not align one to one. Promptotyping has no module of its own. It currently sits in module 4, with verification, the critical expert and the acceptance hands-on split off into module 5 at the unit boundary between M12 and M13. Confirm the split, keep the German promptotyping chapter whole in module 4, or open a sixth module.
3. Unit M6 spans two modules. The four definitions and the central thesis open module 1, while the layer table and the closing formula sit in the German summary chapter in module 5. Confirm, or pull the summary chapter forward into module 1.
4. Taking one language version per unit discards a substantial part of the English Full Lecture Notes, listed above. Decide per case whether a discarded passage merges into the kept unit or whether the other language version becomes the translation input for the second language.
5. The English block on how large language models work needs a unit id, or M5 needs to be widened explicitly to cover it.
6. Unit M16 is classified as workshop-specific for the CLARIAH profile in the map, yet its material sits in the English Full Lecture Notes and is therefore carried into module 2. Either the case study leaves the full corpus and becomes profile material, or the classification changes.
7. The German Full Lecture Notes run a digital edition as their example throughout, while the English Full Lecture Notes use research data workflows and knowledge work in general. The two framings now stand side by side in modules 1 to 4. Decide which framing the full corpus carries and whether the other becomes a profile substitution.
8. The English Full Lecture Notes name a specific model in the transcription example and in the heading of that section. A heading that carries a version number ages with the model. Decide whether the pin belongs to the documented run or to the module.
9. Module 5 carries two bibliographies and two template sets. Decide whether they merge into one apparatus or stay separated by source language.
10. The escaped Markdown and the empty anchors in the German Full Lecture Notes are an export artefact. Decide whether a cleanup pass runs on the modules after confirmation or on the Full Lecture Notes before the cut is confirmed.
11. The German table of contents and list of figures were not carried. Confirm the omission, or specify where a navigation apparatus across the five modules should live.
