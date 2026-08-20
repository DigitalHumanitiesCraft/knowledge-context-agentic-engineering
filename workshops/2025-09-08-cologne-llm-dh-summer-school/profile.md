---
title: Workshop Profile Cologne LLM Summer School 2025
workshop:
  id: 2025-09-08-cologne-llm-dh-summer-school
  dates: 2025-09-08/11
  title: Introductory Workshop on LLMs and Prompt Engineering & Digital Editions Track
  event: "Summer School Large Language Models in Digital Humanities Research, Cologne"
  audience: digital humanities researchers working on edition and corpus projects, with heterogeneous prior LLM experience
  language: en
  status: delivered
  slides: null
  script: null
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [workshop-slides-1-understanding-llms.txt, workshop-slides-2-llm-fundamentals.txt, workshop-slides-3-prompt-engineering-basics.txt, workshop-slides-4-advanced-prompt-engineering.txt, workshop-slides-5-ai-engineering.txt, workshop-slides-6-digital-editions.txt, ../2025-09-24-freiburg-dhlab-preworkshop/profile.md, ../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/additional-past-instances.md]
---

# Workshop Profile Cologne LLM Summer School 2025

## Profile

This instance was taught from 2025-09-08 to 2025-09-11 at the summer school *Large Language Models in Digital Humanities Research* in Cologne. The title slide of every deck carries that event line, and the school website plus a public course page are named on a later instance of the line as `https://ml-school.uni-koeln.de` and `https://chpollin.github.io/llmdh`. Teaching language is English throughout the slide text, with a small number of German-language slides that survived from earlier material.

The contribution consists of two units. The *Introductory Workshop on LLMs and Prompt Engineering* runs as a plenary strand across four decks, from a conceptual opening on what "understanding" would mean for a language model through the technical fundamentals and two prompt-engineering levels to AI engineering and agents. The *LLM-Supported Modeling, Operationalization, and Exploration for Digital Editions* unit is one of four parallel specialised tracks, and it is the one the operator taught; the other three tracks are named on the outlook slide of the opening deck and belong to other lecturers.

This is the largest delivered asset of the teaching line in slide-text form and the widest coverage of the five master modules in a single instance. It predates the master corpus, which was assembled from July 2026 onward, so the relation is upstream rather than derivative, the same relation the register already accepts for the other delivered entries.

The authoritative content state of this instance is the set of six slide-text exports in this folder. They document a delivered state and are not maintained further.

## Module mapping

The mapping is derived from the slide sequence of the six exports against the five master modules. Every row names the export it rests on. Depth statements are readings of the slide text; the decks themselves were not opened, and no attendance record, timetable or per-unit duration exists in any artefact of this profile.

| Master module | Slide-text sections drawn on | Depth and emphasis |
| --- | --- | --- |
| 1 Understanding Large Language Models | Export 2 in full, meaning next token prediction and the autoregressive loop, scaling laws with the parameter progression, the three eras of LLM training, pre-training as lossy probabilistic compression with the Zebra-article Gestalt, tokenization with its own hands-on, transformer architecture, the 8K context-window arithmetic, embeddings with the dog, cat and stone illustration, the parallel-pathway account of how a model adds two numbers, confabulation with its training and evaluation causes, post-training with supervised fine-tuning, reward modelling and reinforcement learning, alignment techniques including Constitutional AI, sycophancy, reasoning models and test-time compute, mixture of experts. Export 1 adds the terminology block that separates frontier models from smaller models | Taught in full and at the greatest depth the corpus holds anywhere. The block is the English counterpart to the German fundamentals material of the later VetMedAI instance, and it carries several items no other instance has, notably the training-era cut, mixture of experts and the document-upload explanation that shows the application layer assembling the prompt |
| 2 Prompt Engineering | Export 3 in full, meaning prompt engineering as search in a latent program space, the empirical instability block with emotional stimuli, politeness and the reassessment of role prompting, the labelled prompt anatomy on a workshop-budgeting example with expert persona, main task, working style, specification and instructions, conversational against traditional prompt engineering, the prompting-technique survey with thought generation, ensembling, decomposition and in-context learning, chain of thought with its thread, tabular, tree and draft variants, prompt brittleness with punctuation, lexical, dialectal and structural sensitivity, attention sinks, system prompts and custom instructions, jailbreaking and prompt injection. Export 4 adds the advanced layer with Semantic Markdown, Sparse Priming Representations and three self-developed reasoning prompts | Taught in full and across two levels, with four participant exercises. The advanced deck is the only place in the corpus where the meta-prompt, PRISM and CASCADE frameworks appear together with the explicit admission that their selection rests on experience rather than evaluation |
| 3 Knowledge and Context Engineering | Export 3 with the dedicated slide that moves the bottleneck from how we ask to what we provide, context rot with its source, and the rules for keeping a context window compact. Export 4 with Semantic Markdown and Sparse Priming Representations as compression formats, the pseudo-syntax for context compression on a bookkeeping ontology, infini-attention and many-shot in-context learning. Export 6 with the promptotyping documents `context.md`, `data.md`, `design.md` and `architecture.md` given in full, and the `knowledge/` folder layout of the TEI hands-on | Substantial and distributed rather than taught as one block. Compression is the organising idea, meaning that the module appears as the set of techniques for putting a maximum of task-relevant structure into a minimum of tokens, and the four worked promptotyping documents are the most complete example of a project knowledge base anywhere in the delivered material |
| 4 Agentic Engineering | Export 5 in full, meaning the four-way distinction of model, reasoning model, agent and workflow, tool use with a demonstrated TEI analysis, the agent taxonomy by autonomy from tool-calling through web and code agents to computer-use and sandbox agents, the Model Context Protocol with its host, client and server architecture and a browser-automation demonstration, agentic coding systems with `AGENTS.md` and the harness extensibility account, retrieval-augmented generation with chunking, embeddings, vector database and similarity retrieval, a GraphRAG demonstration on the day-book material, and the deep-research-to-Zotero literature workflow with its RIS conversion and expert-in-the-loop validation. Export 6 adds the Promptotyping demonstration in an agentic coding harness on the DEPCHA material | The centre of the second half. It carries the harness layer at a depth no other delivered instance reaches, and the literature workflow is the only end-to-end knowledge-work pipeline in the corpus that leaves the research-data domain |
| 5 Critical Perspectives and Governance | Export 1 almost entirely, meaning the three-way cut of phenomenal, explanatory and use understanding, the competing perspectives from stochastic parrots through exotic mind-like entities to program retrieval, the hard problems of alignment, epistemic asymmetry and system coercion against the actionable ones of skills atrophy, evaluation, attribution and compute cost, the terminology and anthropomorphism problems, the consciousness debate with its welfare argument, the critique of the technology industry and its concentration of power, and a personal-assessment slide that states the author's own position. Export 2 adds the energy, water and cost figures for inference with the scale paradox. Export 6 adds the RIDE-criteria review of a generated edition | Taught in full and with its own weight, which makes this the strongest governance asset of the line alongside the EU AI Act block of the later VetMedAI instance. The research-integrity hands-on is the didactic core, because it puts the five research virtues of a 2024 preprint on the table and asks participants where the criticism holds and where a generative workflow could preserve the virtues |

The digital-editions track of export 6 carries the edition domain layer of the master corpus, meaning the path from source through modelling and operationalisation to a published research artefact. It runs as a domain specialisation over modules 2 to 5 rather than as a module of its own.

## Workshop-specific content

### Participant exercises

Nine exercises are documented in the slide text, which is the highest count of any delivered instance. They fall into three groups. Three are short mechanical exercises that give an immediate result, meaning the tokenizer comparison across languages and markup formats, the five-minute build of a summariser against a hosted model API, and the idea-development simulation that runs a review panel on a dialectical structure. Four are extraction exercises on real research material, meaning the academic-narrative extraction from a conference paper on graph representation of historical information, the connection of two academic narratives into one, the structured extraction of transactions from a plain-text ledger into CSV, XML, TEI or RDF, and a German-language metadata extraction from a historical document cover in which participants are required to check every proposed authority identifier against the live authority service and to record which ones were hallucinated. Two are the substantial track exercises, meaning the TEI knowledge-engineering exercise with its three-document knowledge folder and its validation loop through an XML editor, and the collective RIDE review of a generated edition in groups.

### The vibe-edition argument

The digital-editions track is built around one provocation and its consequences. A generated edition of a Neo-Latin poem collection is presented, then reviewed collectively against the established review criteria for scholarly digital editions, and the discussion slide asks what makes something an edition rather than text on the web. The stated position is that the criteria stay untouched while the front end loses its value, because a high-quality TEI representation permits any front end to be generated. Two AI-generated reviews of the same edition, produced by an agent system and by a deep-research system, are shown next to the human group work.

### Language

The slide text is English, and four slides are German. They sit in the prompt-engineering export as the metadata-extraction hands-on with its instructions and documentation requirements, and in the digital-editions export as the generation notice on two title slides. Some notes inside the German-language material use the informal register of an earlier German deck, which places the origin of those slides outside this instance.

### Result claim

A later instance of the line states that participants built working prototypes of TEI-XML-based digital editions from their own sources within a day and a half. The claim is recorded in the operator's research vault twice, in the pre-workshop deck of the Freiburg instance and in a knowledge document on LLM-supported TEI modelling. It is a self-report of the delivery and not a documented evaluation.

### Schedule

The source states none. Six exports document the taught sequence within each unit, and the outlook slide of the opening deck gives the order of the plenary units as fundamentals, prompt engineering, advanced prompt engineering, AI engineering, hands-on workshop and terms and concepts. How these were distributed across the four days, and where the specialised tracks sat, is not fixed in any artefact of this profile.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Slide text, opening unit on "understanding" LLMs | `workshop-slides-1-understanding-llms.txt` | delivered state of September 2025 |
| Slide text, LLM fundamentals | `workshop-slides-2-llm-fundamentals.txt` | delivered state of September 2025 |
| Slide text, prompt engineering basics | `workshop-slides-3-prompt-engineering-basics.txt` | delivered state of September 2025 |
| Slide text, advanced prompt engineering | `workshop-slides-4-advanced-prompt-engineering.txt` | delivered state of September 2025 |
| Slide text, AI engineering and applied generative AI | `workshop-slides-5-ai-engineering.txt` | delivered state of September 2025 |
| Slide text, digital editions track | `workshop-slides-6-digital-editions.txt` | delivered state of September 2025 |
| Google Doc scripts and lecture manuscripts | named on the title slide of each export, five distinct documents | existence documented, access state unverified |
| Live decks | not identified | the exports carry no deck URL of their own |
| Course page | `https://chpollin.github.io/llmdh`, named on a later instance of the line | outside this repo |
| Cover | `docs/assets/covers/2025-09-08-cologne-llm-dh-summer-school.png` | absent |

The link inventory in `knowledge/drafts/google-artefacts.md` verifies none of the Google artefacts of this instance, so both register fields stay null until an access check has run. The scripts are the largest unclaimed asset of this instance, because five separate documents of lecture prose exist for material the master corpus currently carries only as slides.

### Provenance and cleaning

The six exports were copied unchanged from the folder `Teaching/HEDIT-Workshop 2025/` of the operator's research vault. The folder name is misleading, because it holds reference decks gathered for the preparation of a different workshop rather than the material of that workshop; the finding is recorded in `knowledge/drafts/additional-past-instances.md`.

Every export was checked for embedded URLs carrying an `ouid=` or `authuser=` query parameter, which would expose the numeric identifier of the owning Google account. None was found in any of the six files. Personal names inside the slide text are research data and stay untouched.

Two redactions were applied before publication (2026-08-20). Seven LinkedIn URLs across four exports carried `utm` sharing parameters with an `rcm=` token bound to a LinkedIn member account; the query strings were stripped, the target URLs stay intact. The URL of the Drive folder offered to participants for sharing their own material was withheld, because the folder may hold participant material whose rights state is unclear. Beyond that, nine Google URLs are published with these files, meaning six documents (the five scripts and lecture manuscripts plus one deep-research output shown as a demonstration), two earlier decks referenced as prior work and one file URL of a historical document image used in an exercise. The access state of these is unverified, and two further URLs point at shared sessions in hosted assistant products.

## Delivery notes

Taught from 2025-09-08 to 2025-09-11 in Cologne in English, as a plenary introductory strand plus one of four parallel specialised tracks. Delivery ran on slides with live demonstrations and nine participant exercises, and it opened with a stand-up survey that reads the room by hand signals on eleven statements about LLM use, confidence, institutional guidelines and prior successes and failures.

The introduction round of the editions track is transcribed in the export as a list of participant projects, covering ancient Greek critical editions, a biographical edition from diaries and letters, archival PDF holdings of a philosophical estate, Low German dictionaries, corpus building in linguistics, a Persian epic with entity modelling against a cultural-heritage ontology, annotation and commentary layers in Nordic editions, an Old French medical manuscript, Byzantine manuscripts, an early medieval hybrid edition and library catalogue and newspaper digitisation. The list documents the actual audience of that track and is the basis for the audience formulation of the register entry.

Open points that the source does not settle.

- Participant count, per-unit durations and the distribution of the units across the four days are undocumented.
- The host institution is an inference from the school domain named on a later instance of the line, and no artefact of this profile states it directly.
- The audience formulation is an inference from the introduction round of the editions track and from the stand-up survey, which together describe the track audience rather than the plenary audience.
- Whether the four Google Doc scripts and the one lecture manuscript are publicly readable is unchecked, so both register link fields are null.
- Two hands-on exercises reference material held in a shared Drive folder, whose rights state was never established.
