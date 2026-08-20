# Module Map (Proposal)

Draft cut of the master corpus into modules. Two sources were read in full, the German master Skriptum *Knowledge, Context and Agentic Engineering* (vault, ten chapters) and the English CLARIAH-AT lecture notes *Knowledge, Context and Agentic Engineering for Research Data Workflows & Digital Editions*. Nothing here is decided. The numbering follows a proposed teaching sequence, so module order and chapter order of the Skriptum diverge where the lecture notes place a block earlier.

Classification follows the master-profile model in `project.md`. "master-general" means the module belongs to the domain-neutral core and is available to every profile. "workshop-specific (CLARIAH)" means the module carries the case material of the CLARIAH-AT Summer School unit and would be exchanged in another profile.

## Module list

| ID | Module title | Skriptum source | Class |
| --- | --- | --- | --- |
| M1 | Applied Generative AI in Research Data Workflows | Front matter (Abstract, Lernziele, Verwendung) | master-general |
| M2 | Research Data, Representation and Provenance | Ch. 1 | master-general |
| M3 | The Current LLM Capability Landscape | none | master-general |
| M4 | Asymmetric Amplification and the Capability Frontier | none | master-general |
| M5 | What an LLM Is: Jagged Capability, Latent Program Space, Assistant Character | Ch. 3.1 (one paragraph) | master-general |
| M6 | The Four Engineering Layers | Ch. 2.1, 2.6 | master-general |
| M7 | Prompt Engineering | Ch. 2.2 | master-general |
| M8 | Context Engineering | Ch. 2.3 | master-general |
| M9 | Knowledge Engineering and Knowledge Documents | Ch. 2.4 | master-general |
| M10 | Agentic Engineering, AI Harnesses and Controlled Agent Workflows | Ch. 2.5, Ch. 3 | master-general |
| M11 | Working Environment, API Access and Structured Output | Ch. 3.4, 6.5 (partial) | master-general |
| M12 | Promptotyping and Scholar-Centred Design | Ch. 4 | master-general |
| M13 | Verification, Validation and the Critical Expert | Ch. 5 | master-general |
| M14 | From Facsimile to a Research Data Package | Ch. 6 | master-general (edition domain layer) |
| M15 | Case Study Hersch: A Documented Pilot Dataset | Ch. 7 | workshop-specific (CLARIAH) |
| M16 | Case Study Zweig: Transcribing a Complex Facsimile | none | workshop-specific (CLARIAH) |
| M17 | Topic Annotation and Statistical Topic Modeling | Ch. 8 | master-general |
| M18 | Project Governance and Research Mission Control | Ch. 9 | master-general |
| M19 | Limits, Glossary and Apparatus | Ch. 10 | master-general (cross-cutting) |

## Module summaries

M1 Applied Generative AI in Research Data Workflows. Frames the subject as the adaptation of generative methods to domain research practice rather than model development, states the learning objectives and names the four engineering layers as the conceptual spine of the corpus. Also carries the deliberate focus on frontier models with its qualifications, including the standing of smaller and open-weight models and the ecological and power-concentration questions. The Skriptum holds this only as abstract and learning objectives, while the argued framing exists in the lecture notes.

M2 Research Data, Representation and Provenance. Develops research data as a functional and institutional category, the capta argument, the representational chain from source to publication, and the four data levels of primary, intermediate, meta and para data. Adds provenance as a reconstructible relation with PROV-O classes and the Web Annotation Data Model, plus the minimal provenance record and its check criterion. The lecture-notes counterpart adds AI readiness and the standards frame of FAIR, Croissant, CARE and TEI.

M3 The Current LLM Capability Landscape. Surveys the model ecosystems, the degrees of openness from proprietary through open weights to the Open Source AI Definition, the European Open Source AI Index and open-washing, local deployment against hosted access, and the harness layer as a separate system dimension. Closes on the four dimensions of capability, openness, deployment and agentic integration. No Skriptum chapter covers this.

M4 Asymmetric Amplification and the Capability Frontier. Assembles the capability signals from task-horizon measurement, interactive benchmarks, formal theorem proving, cyber evaluations and scenario work, and reads them as a movement of the frontier across research-relevant domains rather than as a measure of research capability. Develops asymmetric amplification as the thesis that amplification scales with existing expertise, computational actionability and the quality of feedback. Includes the jaggedness argument against both naive extrapolation and dismissal.

M5 What an LLM Is: Jagged Capability, Latent Program Space, Assistant Character. Covers confabulation, sycophancy and the alien-intelligence metaphor, then the latent-program-space model with vector programs, program queries, prompt engineering as external search and reasoning as internal search. Adds how training stages shape that space, a mechanistic-interpretability excursus and the distinction between the underlying model and the assistant character shipped in a product. The Skriptum touches this in a single paragraph of Ch. 3.1.

M6 The Four Engineering Layers. Holds the layer table with object, guiding question and typical artefact per layer, and the worked interplay for one research task where knowledge base, working context, prompt and execution organisation each carry a defined part. Serves as the hinge module that every later module refers back to. The lecture notes carry the compact three-way distinction of what the project knows, what the model needs now and what it should do now.

M7 Prompt Engineering. Defines prompt engineering as iterative development of one input sequence, gives the four-part working structure of task, context, rules and output, and shows the bounded specification that points at persistent project rules instead of repeating them. Adds the empirical instability of prompting effects across model, language, task and metric, and the practical principles including the countermeasures against sycophancy. The Skriptum cites the relevant studies, while the lecture notes develop them into a didactic block.

M8 Context Engineering. Separates the context window as a technical processing limit from the working context as the assembled information state for a task, and shows that a file in the project folder is not yet in context. Covers position, distraction and context-rot effects and the resulting goal of a sufficient dense context rather than a maximal one. Coverage in both sources is close.

M9 Knowledge Engineering and Knowledge Documents. Defines the maintained, inspectable and revisable project knowledge base, the three document functions of declarative knowledge, process and agent instruction, and the concrete `knowledge/` folder layout. Adds the properties of a usable knowledge document and the argument that the persistent research record need not consist of every issued prompt. Markdown appears as a portable carrier without semantic guarantees.

M10 Agentic Engineering, AI Harnesses and Controlled Agent Workflows. Moves from language model to agent, defines the harness with memory, tools, permissions, hooks and observability, and develops the execution loop with identifiable states, unchanged raw outputs and referenced run identities. Adds least-privilege tool access with read-only sources, and subagents with separate write territories and explicit handoffs. The lecture notes contribute the history of agents before LLMs.

M11 Working Environment, API Access and Structured Output. Prepares the workspace before the first substantive prompt, meaning source material, project documentation, expected outputs and scoped file and tool permissions. Shows the model as a component inside a pipeline through an API, with the shift in scale that raises the weight of provenance, configuration, failure handling and cost. Ends at deterministic checks on structured output, including arithmetic checks on tabular data that surface internal inconsistency.

M12 Promptotyping and Scholar-Centred Design. Holds the method core, Scholar-Centred Design as the translation of research questions and responsibilities into artefact requirements, and the four recurring work forms of preparation, exploration, distillation and implementation. Adds write-back as a defined operation that targets the level where the cause sits, and the promptotype as the identifiable accepted iteration state. The lecture notes carry the method as one section with a flow diagram.

M13 Verification, Validation and the Critical Expert. Separates deterministic verification, agentic review, critical-expert verification, scholarly validation and acceptance by object, procedure and authority. Introduces assessment result and scholarly decision as distinct objects, the status value as their projection, and the three status axes for evidence, source check and review. Carries the rule that model agreement is not scholarly verification, and the separation of acceptance from publication.

M14 From Facsimile to a Research Data Package. Runs the generic pipeline of multimodal transcription, segmentation as a research decision, named entities with the null rule for unverified authority data, evidence-bound topic annotation, the JSON schema as an executable data contract, and the package layout with its rights gate. Defines the vision-language model and its characteristic failure of contextually plausible readings. The lecture notes add the conceptual question of whether this is OCR, HTR or something technically different.

M15 Case Study Hersch: A Documented Pilot Dataset. The full tutorial on two pages from the Zentralbibliothek Zürich Hersch material, with the preparatory transcription run and three annotation runs of rising specification, from open baseline through schema without research question to codebook-bound segment annotation. Carries run metadata, hashes, the validator, the comparison protocol and the five open critical-expert gates. Lives in the Skriptum as Ch. 7 and executably in the external hands-on repository.

M16 Case Study Zweig: Transcribing a Complex Facsimile. The Stefan Zweig material with the order slip as a compact four-part prompt example and the Radiovortrag manuscript page as the participant exercise, including the reusable prompt skeleton, the catalogue metadata block and the added rule against reconstructing readings from linguistic context. Followed by the critical review of a fluent but partly incorrect transcription. Exists only in the lecture notes.

M17 Topic Annotation and Statistical Topic Modeling. Separates the explicit, evidence-bound annotation record from latent topic estimation over a corpus, compares both along unit, categories, research question, result and required checking, and states what a later corpus study would need. Names the pilot as preparation rather than as a corpus result. No lecture-notes counterpart.

M18 Project Governance and Research Mission Control. Covers documented rules, roles and decision rights for authority, permissions, review status, rights and write-back, then the mission-control method with research, operational and verification functions and the passage from clarification to implementation. Adds the choice of verification form by object and error risk, and the minimal exchange of implementation brief, result with evidence and verification finding. No lecture-notes counterpart.

M19 Limits, Glossary and Apparatus. Holds the methodological and practical limits, the reproducibility requirements for a documented run, the legal and ethical gates before publication, the glossary of working definitions, the literature and the slide contract. Functions as a cross-cutting appendix that every module draws on rather than as a taught unit.

## Mapping from lecture-notes sections to modules

Coverage states how the lecture-notes section relates to the Skriptum material behind the module. "full" means both sources carry it, "partial" means the module exists but one source adds substance, "gap" means no Skriptum counterpart exists.

| Lecture-notes section | Module | Coverage |
| --- | --- | --- |
| Abstract | M1 | partial |
| Applied Generative AI for Research Data Workflows | M1 | gap |
| Humanities Research Data Are Constructed through Scholarly Workflows | M2 | partial |
| Learning Objectives and Core Concepts | M1, M6 | full |
| AI-Supported Research Data Workflows & Epistemic Infrastructures | M14, M15, M16 | gap |
| The Current LLM Capability Landscape | M3 | gap |
| Frontier LLMs Asymmetrically Amplify Computational Research | M4 | gap |
| LLMs as Jagged Alien "Intelligences" | M5 | gap |
| Prepare the Working Environment before the First Prompt | M11 | partial |
| Generative Models through an API | M11 | gap |
| Model-Assisted Review inside an AI Harness | M13, M10 | partial |
| From Generated Text to Structured Data | M11, M14 | partial |
| Prompt Engineering | M7 | full |
| Prompting Is Weird and Keeps Changing | M7 | partial |
| Transcribe a Facsimile with Gemini | M16, M7 | gap |
| Hands-on 1: Transcribe a Complex Facsimile | M16 | gap |
| Example Result and Critical Review | M16, M13 | gap |
| Multimodality and Vision-Language Models | M14 | partial |
| Prompt Engineering as Search in a Latent Program Space | M5 | gap |
| Reasoning and Test-Time Compute as Internal Search | M5 | gap |
| Training Shapes the Latent Program Space | M5 | gap |
| Excursus: Mechanistic Interpretability | M5 | gap |
| The Assistant Is a Character Generated by the Model | M5 | gap |
| Practical Prompting Principles | M7 | partial |
| From Prompt Engineering to Knowledge and Context Engineering | M6 | full |
| Context Engineering Shapes the Working Context | M8 | full |
| Markdown and Knowledge Documents | M9 | partial |
| Promptotyping | M12 | partial |
| Agentic Engineering and AI Harnesses | M10 | full |
| AI Agents Existed Long before LLMs | M10 | gap |
| Hands-on 2: From Transcription to Information Extraction | M15, M16 | partial |
| Evaluation, Validation and Scholarly Verification | M13 | partial |
| Conclusion | M1, M19 | full |

## Deltas

### In the lecture notes without a Skriptum counterpart

1. Applied Generative AI as a disciplinary framing, including the argument for the term against the broader machine-learning label and the reasoned focus on frontier models with its qualifications.
2. AI readiness of research data, plus Croissant and CARE alongside FAIR. The Skriptum names FAIR once in Ch. 1.1 and carries no dataset-description or governance frameworks.
3. The two project workflows as narrative case material, meaning the Zentralbibliothek Zürich production pipeline with document OCR, local layout analysis, TEI transformation and entity enrichment, and the Stefan Zweig Digital transcription workflow with preserved image-text relation and character error rate. The Skriptum uses Hersch data without the production workflow, and Stefan Zweig Digital appears nowhere.
4. The whole capability-landscape block, meaning ecosystems, openness dimensions, the Open Source AI Definition, the European Open Source AI Index, open-washing, local deployment and the enumeration of harness environments (module M3).
5. The whole asymmetric-amplification block with its benchmark signals and the jaggedness argument (module M4).
6. The nature-of-LLMs block, meaning confabulation, sycophancy, the latent-program-space model, reasoning as internal search, the training-stages account, the mechanistic-interpretability excursus and the assistant character (module M5).
7. Workspace preparation as a methodological step before the first prompt, and API access as the move from conversational interface to pipeline component.
8. Deterministic checks on numerical tables as a feedback pattern, where row and column sums surface internal inconsistency.
9. The history of AI agents before LLMs, with the classical agent definition and embodied examples.
10. The complete Zweig hands-on material, meaning the order slip example, the prompt skeleton, the catalogue metadata block, the rule against contextual reconstruction and the critical review of the result (module M16).
11. The conceptual questions of whether the task is OCR, HTR or something technically different, and to what extent zero-shot handwriting recognition is emergent.

### In the Skriptum without a lecture-notes counterpart

1. The data-level terminology of primary, intermediate, meta and para data, with the rule that these levels stay in separate fields.
2. Provenance as formalism, meaning PROV-O classes, the Web Annotation Data Model, the minimal provenance record and the separation of provenance from validity.
3. The four-layer table with a named artefact per layer, and the assignment exercise that forces each rule and each piece of information to one primary layer.
4. The knowledge-document typology of declarative, process and agent-instruction documents, and the concrete `knowledge/` folder layout.
5. The agentic execution loop with identifiable states, unchanged raw outputs, run identities and hashes; the least-privilege principle with read-only sources and human-set status values; subagents with separate write territories and explicit handoffs.
6. The internal structure of Promptotyping, meaning Scholar-Centred Design, the four work forms, write-back as a targeted operation and the promptotype as an accepted iteration state.
7. The five-function checking architecture with its authority column, assessment result and scholarly decision as separate objects, the status value as projection, the three status axes, and acceptance against publication. The lecture notes carry the three-way distinction of evaluation, validation and scholarly verification only.
8. Segmentation as a research decision, with the three identities of document, page and analytical segment.
9. Named entity recognition with identifiers and the rule that unverified authority links stay null.
10. Evidence-bound topic annotation with codebook, claim and exact quotation, the JSON schema as data contract including the ban on uncontrolled fields such as confidence, and the research data package layout with its rights gate.
11. The complete Hersch tutorial with four documented runs, run metadata, validator suite, comparison protocol and the five open critical-expert gates (module M15).
12. Topic annotation against statistical topic modeling, including the corpus-design requirements for a later study (module M17).
13. Project governance and Research Mission Control in full, including the verification form chosen by object and error risk (module M18).
14. The apparatus, meaning the limits section, the glossary, the literature and the slide and Google-Doc contract.
15. The didactic contract of the Skriptum itself, meaning the per-chapter pattern of definition box, example, executable check with observable criterion, limit and slide connection. The lecture notes run as continuous prose with two hands-on sections.

## Open questions for the operator

1. Hands-on identity for the CLARIAH unit. The task framing names an OCR-to-TEI hands-on on a correspondence corpus, the Skriptum tutorial works on two journal pages from the Hersch material and produces JSON annotations, and the lecture notes work on Stefan Zweig manuscripts and produce plain-text transcriptions. Which case is canonical for 2026-09-25, and does TEI become a target representation, which no source currently teaches as an output format.
2. Whether M15 and M16 both survive as parallel case-study modules or one replaces the other. The repo charter names Hersch and Zweig as the exchangeable case studies, which supports keeping both, while a single session probably carries one.
3. Whether the LLM-nature blocks M3, M4 and M5 enter the German master Skriptum as chapters, or stay an English lecture-notes layer that profiles draw on. This is the largest one-sided delta and decides whether the Skriptum stays the single master or becomes one of two masters.
4. Granularity of chapter 2. The proposal splits it into M6 through M9 so that a profile can select prompt engineering at depth without taking all four layers, at the cost of four modules where the Skriptum has one chapter.
5. Whether M19 counts as a module at all or as an appendix that every module references.
6. Model pins in the hands-on modules. The lecture notes name one Gemini model in the demonstration and a different Gemini identifier for the Zweig project run, and the Skriptum documents its Hersch run under a different provider entirely. A module map needs one decided pin per hands-on, or an explicit statement that the pin belongs to the run and not to the module.
