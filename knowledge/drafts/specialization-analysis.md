---
title: Specialisation Analysis of the Seven Upcoming Instances
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
status: draft
related: [additional-past-instances.md, module-map.md, past-instances-registry.md, ../project.md, ../../docs/data/workshops.json]
---

# Specialisation Analysis of the Seven Upcoming Instances

Research draft on what the operator's research vault holds about the seven upcoming instances of the teaching line, read against the register in `docs/data/workshops.json` and against the workshop profiles that exist in `workshops/`. Nothing here is applied. No file in the repo outside this draft and no file in the vault was touched.

Sources read in full are the seven workshop documents under `Teaching/Workshops/` and `Projects/VeTMedAI/`, the workshop block of `ACTIVE-WORK.md`, the register, the four existing profiles and the earlier draft `additional-past-instances.md`. Statements that the vault carries verbatim are given as findings. Statements derived by comparison are marked as inference in place. Monetary figures held in the vault offer documents are excluded by rule and are not reproduced here; contract state appears qualitatively where it gates the flow of material.

Third parties appear by role and institution throughout. Historical persons named in the corpora (Malaniuk, Hersch, Zweig) are the material the teaching operates on and keep their names, in line with the naming already used in `workshops/2026-09-25-clariah-at/profile.md`.

## Reading order finding

Three of the seven registered instances have no folder under `workshops/`, namely HEDIT Heidelberg, Fachschaft Mittelalterstudien and GDA Göttingen. Their register entries were taken from `additional-past-instances.md`, which analysed them at register-entry depth. This draft goes past that depth for those three, because the vault holds substantially more per instance than the register field `focus` can carry.

Two of the four instances that do have a folder carry a thin profile whose content is a coarse derivation from the register entry, namely KUG and Uni for Life, and both of them understate what the vault holds. For KUG that gap is the largest single finding in this analysis.

## 1. KUG Summer School M3GIM, 2026-09-16/17

### Vault coverage

One workshop document carries everything, *2026-09-16 KUG Summer School Promptotyping und Generative AI*. It is the longest workshop document in the vault. Supporting documents are the *Project Overview M³GIM* for the corpus provenance, the master slide set *2026-07-14 Knowledge und Context Engineering Master Slides* as the derivation base, *LLM-Modelllandschaft* for the model state at teaching time, and the `ACTIVE-WORK` entry.

### Specialisation

Two days at introductory level, German, with an explicit statement that the deep vault-modelling slides of the master (knowledge transformations, four-axis model, bootstrap sequence, layer model) are dropped for this audience.

Day 1 carries fundamentals. The AI-agents section of the master is cut to how a model works and where it fails, the knowledge and context engineering section is cut to the slides that ground the checking principle and the concept of a knowledge base. Hands-on A and B run on day 1.

Day 2 carries Promptotyping as the method block plus the remaining hands-on units, with governance and skills reduced to a two-to-three-slide outlook. The Promptotyping section is newly written rather than referenced, because the master carries that section as bare slides without speaker notes; the vault marks the new text as fit for write-back into the master.

The single strongest structural decision is the hands-on chain. Four exercises build on one holding, each stage changing only the technique while the domain stays constant, ordered from easy to visually impressive so that table and text precede image and map. A delivers the cleaned person index, B the schema and the extraction prompt, C the participants' own transcription, D the map.

### Case material and datasets

The estate of the mezzo-soprano Ira Malaniuk (1919–2009) in the archive of the Kunstuniversität Graz, signature UAKUG/NIM. Six index tables from Google Sheets, held locally under the m3gim repo. The exercise excerpts are drawn verbatim from those tables including the real defects.

- Hands-on A works on a prepared XLSX with seven defect classes, among them a doubled Karajan duplicate with a nobiliary-particle variant, four competing life-date formats, a hidden duplicate resolvable only through context knowledge (Callas against Kalogeropoulou), and a fabricated Wikidata identifier on the Egk record that functions as the hallucination bait for the checking rule in the prompt.
- Hands-on B works on the verbatim text of poster `UAKUG/NIM/PL_04`, a concert poster from Stanislau dated 1942-04-26, which is transferred into a controlled tuple schema of type, name and role. The litmus test is the name variant Irene against Ira; the schema limit is made visible on the Wehrmacht discount line, which carries historical weight and produces no tuple.
- Hands-on C is an OCR staircase over three templates of rising difficulty, the printed poster, a multi-column newspaper clipping or review, and a handwritten object. The poster text from B doubles as the reference transcription, which turns the performance drop from felt to measurable.
- Hands-on D normalises places and dates, has the model propose a Wikidata identifier under the same checking rule, and has participants look up the coordinates by hand and enter them into a CSV that drives a minimal static map.

Model assignment is split deliberately, text tasks A, B and D through claude.ai, the vision task C through Google AI Studio with a Gemini model.

### Material available for intake

- Complete slide-text derivation under the delta model, meaning each slide is either a named reference to a master slide with the cut stated, or fully written text with speaker notes and sources. This is teaching-ready prose, not an outline.
- Four hands-on units with verbatim prompts, learning objectives, task slides and stepwise instruction slides.
- Two condensed slides the vault itself marks as fit for the master, *Die OCR-Treppe* and *Generieren oder Nachschlagen?*, both with speaker notes and a note on how to phrase them occasion-free.
- Newly written Promptotyping section covering the definition against vibe coding, the four phases, the `knowledge/` folder with the three analytical document types and their diagnostic use, and the Critical Expert with four checking questions.
- A working map demo exists outside this repo in the Teaching repo under `workshops/m3gim-map-demo` with `index.html` and `data.csv`.

### Rights state

The Malaniuk material is archive holdings of a partner institution and is distributed to participants through the operator's Drive. The vault gives no licence statement for it. The digitisates for staircase templates two and three are requested from the project team and not yet available, so the staircase currently carries only its first step. Verified against the filesystem: the prepared exercise file `personenindex-uebung.xlsx` and the `orte-lookup.csv` are named as deliverables in two places but do not exist yet; the Teaching repo holds only `workshops/m3gim-map-demo`, and no `kug-2026-summer-school` folder.

### Open preparation items

Operator acceptance of the hands-on material and the slide-text derivation, which gates deck production; audience, participant count and prior-knowledge level; scope per day and the split between input and hands-on; the two missing OCR digitisates; the two prepared data files; the model assignment checked against the model state at teaching time and the question whether the vision task really uses a separate environment; whether the governance and skills outlook stays at this level; write-back of the new Promptotyping section into the master.

### Deltas against register and profile

- The profile calls this a thin profile that states a planned shape rather than a settled content state. That is inaccurate. The vault holds a complete slide-text derivation and four fully worked hands-on units awaiting only operator acceptance. The instance is the second-best documented of the seven after CLARIAH-AT.
- The profile places the participant exercise under module 2 Prompt Engineering and marks modules 3 and 4 as light touch. The vault instead runs four data-work exercises whose subject is data preparation, schema extraction, vision transcription and normalisation against authority data, and it gives Promptotyping (module M12 in the fine cut) the whole of day 2. Inference: the profile's module table needs redoing against the vault, not adjusting.
- The profile marks module 5 as undecided. The vault decides it, namely a short outlook of two to three slides with the option of dropping it, which is an open operator question rather than an undecided module.
- The register audience string "participants without LLM or programming background" is not sourced in the vault, which records audience, participant count and prior knowledge as open. Inference: the string is a plausible reading of "Einführungsworkshop" and should be marked provisional until the host confirms.
- Dates and title match.

## 2. CLARIAH-AT Summer School, 2026-09-25

### Vault coverage

Two documents. The consolidated workshop knowledge document *2026-09-25 CLARIAH-AT Summer School Knowledge Context and Agentic Engineering* is the subject contract, and a separate slides document of the same name plus *Slides* holds the returned text of the designed slides. The `ACTIVE-WORK` entry carries the operational state and the standing operator gate.

### Specialisation

Single day, English, digital humanities students. The subject is a source-bound research data workflow on document 1000 of the Hersch project, *Transformer l'école ou la supprimer?*, 1973, French, pages `1000_p003` and `1000_p004`. The analytical unit is Hersch's contribution from her heading to the Illich heading, end exclusive, which makes the divergence of physical page and analytical unit the central segmentation example.

Four model calls form a controlled progression that isolates the effect of individual prompt and context components. Call 01 is a full multimodal transcription of both pages, call 02 an open baseline without research question, segment boundary, codebook or schema, call 03 a generic schema run with the research question explicitly recorded as unspecified, call 04 the research-question-bound and evidence-bound annotation. The archived local probe shows that calls 02 and 03 pull in material from the neighbouring contributions and that call 04 removes that scope contamination.

The methodological core is the three-way status contract. `evidence_status` describes how the passage carries the claim, `source_check_status` records a named human comparison with the source, `review_status` records the disciplinary acceptance. A model-generated confidence value is deliberately not used.

### Material available for intake

The repo already holds `workshop-script.md` as canonical text, so the intake question here is narrow and specific.

- The slides document holds per-slide visible text, speaker notes and sources for the designed slides, plus explicit markers for what is not yet in the deck. That is a slide-level asset the repo does not carry in any form.
- The Hersch tutorial in full, meaning the four model calls with their didactic prompt cores, the expected artefact and the checking step per call, and the comparison table of introduced control against observable effect. The profile states explicitly that `workshop-script.md` does not spell this procedure out, so this is a documented gap the vault can close.
- The working codebook with five topic identifiers, each with an analytical focus and a direct text anchor.
- The required-artifacts table with a minimum content and an acceptance condition per file, the ten acceptance criteria, and the four-part checking contract covering deterministic, source, disciplinary and slide checks.
- The seven defensible claims that carry the didactic argument, in contractual English.
- The first six fixed slides in order, and the specification of the two interactive slides, a hand-raising inventory of models and harnesses and a plenary discussion on research use.
- The specification of the main visualisation, meaning the facsimile with a transparent contour on the segment start, the derived transcription fragment and annotation, and the provenance line through to review.

### Rights state

Image and distribution rights for the facsimiles need institutional clearance before any onward distribution or republication. The package carries a rights note. The repo's own governance rule already excludes facsimiles, so the intake concerns text and specification only.

### Open preparation items

Five critical-expert gates stand unreviewed in the external hands-on package, covering research question, codebook and expected annotation; the human source check for the agentically pre-checked anchors, to be documented separately; institutional image rights; independent final check of the hands-on package; design of the missing Hersch, data and checking modules in the live deck; slide density on the learning-objectives slide; the two interactive slides after a dry run; a manual decision on a footnote label in the Google Doc.

### Deltas against register and profile

- The vault's Source-of-Truth table names this repo as planned and not yet instantiated, and lists "Sichtbarkeit und Einrichtung offen" for the master repository. The repo exists. Inference: the vault entry is stale by one step and should name the repo, with `workshop-script.md` as canonical text and the Google Doc as working surface, which is how the profile already describes it.
- The vault names the Google Doc as the authority for the worked slide sections, the repo names `workshop-script.md`. This is a genuine two-way split rather than a contradiction, because the two artefacts cover different surfaces, but it deserves one sentence in the profile so the split is deliberate.
- Dates, title, audience and language match across all three artefacts.

## 3. Forschungsstelle HEDIT, Universität Heidelberg, 2026-10-05/06

### Vault coverage

*2026-10-05 HEDIT KI-Workshop Heidelberg* is the planning document. The predecessor *2025-11 HEDIT-Workshop* is the programme template. The `ACTIVE-WORK` entry carries the task list. An offer document holds the calculation and is excluded here by rule.

### Specialisation

Two days of five to six hours, structured as three hours in the morning and three in the afternoon, German, for researchers of the editions projects at the research centre. The programme follows the 2025 predecessor with three declared changes, namely the model landscape updated to the frontier state at teaching time including a locally runnable open-weight alternative, agentic coding with Claude Code moved from a side remark into a central method block, and two operational demonstration objects added, the teiCrafter tool and the agentic edition pipeline. A standing operator decision makes teiCrafter the convergence point of the edition tooling.

Day 1 is theory and method in three blocks.

1. Fundamentals of generative AI at the 2026 state, how LLMs work, the frontier landscape, prompt engineering, vibe coding against informed vibe coding.
2. TEI with LLMs, meaning TEI-XML modelling, TEI generation with LLMs, context engineering and context rot, the knowledge vault as steering instrument.
3. Agentic coding and edition workflows, meaning Claude Code in practice, Promptotyping as the structured middle path between vibe coding and classical software development, teiCrafter, and the agentic edition pipeline as a forkable template.

Day 2 is a two-part hands-on workshop on participants' own material. Part one builds the knowledge vault and a prototype from participant material in plaintext, TEI, DOCX or image form. Part two deepens that into a TEI-XML edition on the participants' own material, adds the multi-repo vault pattern for longer projects, and closes with a plenary presentation of the prototypes.

### Case material and datasets

Decided on 2026-08-05, the worked example `o_szd.1079`, a Zweig letter from Stefan Zweig Digital whose TEI header is CC-BY, with the pipeline artefacts held complete in the SZD HTR and OCR pipeline repo and the facsimiles obtainable from the GAMS repository. Alongside it the synthetic teiCrafter fixtures. The rights-restricted Zentralbibliothek Zürich material is excluded from the shared folder and is shown on the projector at most.

### Material available for intake

Programme structure with named blocks and their content, six learning objectives, the participant prerequisites including the requirement of a one-page material description, and the host's prior survey of participant experience. No slide texts exist. Inference: this is the instance where a profile would carry programme and prerequisites but no teaching text, and where the module-4 content is closest to what the master already holds.

### Open preparation items

The workshop concept and its slide set are still to be derived from the master deck; EditionCrafter is to be removed from concept and task list, which a standing operator decision requires and which the document has not yet carried through; the prior-experience survey is to be coordinated with the host; the demo material needs a defined state of the agentic edition pipeline and teiCrafter by the teaching date. The honorarium contract draft is outstanding on the host side, which the vault records as a precondition before material is sent.

### Deltas against register and profile

- No folder under `workshops/` exists for this registered id.
- Module 5 of the master is not programmed. Neither the concept nor the learning objectives name a verification, governance or limits block. The earlier draft judges this a gap against the master rather than a documented decision, and this analysis confirms it against the full document.
- The register title *HEDIT KI-Workshop 2026* is an inference. The vault heading reads *HEDIT KI-Workshop Heidelberg 2026* and no externally announced title exists.
- Dates, language and audience match.

## 4. Fachschaft Mittelalterstudien, Universität Heidelberg, 2026-10-08

### Vault coverage

*2026-10-08 Fachschaft Mittelalterstudien Workshop Heidelberg*, plus the `ACTIVE-WORK` entry which carries two standing operator decisions. The commissioning body is a student council, and the funding comes from quality-assurance funds.

### Specialisation

One day on site, German, for students and early-career researchers in medieval studies, under the title *Knowledge, Context und Agentic Engineering für die Forschung*, which is the German form of the teaching-line title. Participants obtain their own Claude Pro access, decided by the student council. The day opens on the fundamentals of large language models and AI agents and then works practically in Claude Code, spanning the build-up of structured project knowledge through to agentic work on a research-adjacent example. Two further persons from the Heidelberg environment with a focus on local and open-source models attend as additional respondents; whether they get their own block is open.

### Case material and datasets

The hands-on is a small TEI and handwriting-recognition project on roughly ten charters sharing persons or organisations, producing recognition output, TEI markup, a person and organisation index and a small static edition, so the full arc from source to edition runs in one day.

The source finding of 2026-08-05 is substantial and worth carrying verbatim into any profile. The Stadtbücher volume one, covering 1395 to 1400, carry no facsimile references, and digitisates through Monasterium exist only in the Vienna charter corpus 1177 to 1414. Two justified ten-item sets are prepared. The primary proposal is the Näzeuger family 1382–1414, with three connecting persons and legal transactions ranging from a court claim through an inheritance division and a house sale to a mass endowment, with all facsimile URLs documented. The alternative is the St. Peter chapel 1385–1412.

The script finding on the example facsimile is late-Gothic chancery cursive in very good preservation, which is the most favourable handwritten case for vision models, with a roughly legible but systematically faulty transcription to be expected. The recommended exercise format follows from that, namely participants check a prepared model transcription against facsimile and TEI ground truth, with a live round trip optional through their own accounts in AI Studio.

### Rights state

The licence file of the source corpus names CC BY 4.0 with copyright at the Universität Wien but is marked pending, and the Monasterium image rights are not documented in the source repo. Both need clearing before any distribution to participants. Inference: this is the tightest rights gate of the seven, because the hands-on cannot run without the images.

### Material available for intake

The two candidate charter sets with their selection rationale, the script finding with its expected failure mode, the recommended exercise format, the term apparatus drawn from the master glossary and the Promptotyping paper definitions, and the four-step next-steps list. A deck copy of the master deck exists in Google Slides, created 2026-08-05 and not yet cut to this instance. Slide texts are to be written in Markdown and transferred by the operator.

### Open preparation items

Two standing operator decisions, namely switching the hands-on base to the Näzeuger set and fixing the checking format, and whether the two additional persons get their own block. Beyond that, licence and image-rights requests, then populating the data folder and setting up the mini repo with an instruction layer and a `knowledge/` folder, and the slide-set adaptation.

### Deltas against register and profile

- No folder under `workshops/` exists for this registered id.
- The register `slides` field is null while a deck copy exists. The earlier draft recommends keeping it null until the deck is cut, on the ground that publishing the link would expose master material under this instance's name. That reasoning holds and should be preserved in the profile.
- Module 2 is not named as a block anywhere in the vault, and module 5 lives inside the hands-on design rather than in a block, because the recommended exercise teaches verification by having participants perform it. Both readings come from the earlier draft and are confirmed here.
- Dates, title, audience and language match.

## 5. Göttinger Digitale Akademie, 2026-10-15

### Vault coverage

*2026-10-15 GDA Göttingen Workshop* holds organisational state, concept and fully written slide texts in one document. It is the richest slide-text asset among the instances without a repo folder, adversarially reviewed with all findings resolved, and awaiting operator acceptance. The `ACTIVE-WORK` entry carries two standing operator gates.

### Specialisation

Half a day, 3.5 hours, 09:00–12:30, hybrid with a parallel Zoom channel, German. It is the pre-conference workshop to the closing conference of the academy's digital programme, whose theme pairs sustainability and artificial intelligence, and the audience is staff of academy research projects plus guests from the state and university library. The subject is generative AI for the preparation and migration of research data and for the semi-automated maintenance of user interfaces and service endpoints.

The framing argument ties the instance to its conference. Academy projects produce data, editions and interfaces over decades; at the end of a funding period migration and maintenance fall due, and that work is repetitive, rule-governed and source-bound, which is where coding agents carry. The stated condition is machine-readable project documentation, because what is documented nowhere cannot be observed by any agent.

The central methodological slide is the one that separates agent-written scripts from direct model transformation. The agent characterises the data, writes a transformation script and tests against known cases, and executes both, so the script is deterministic, repeatable and inspectable and every correction is a diff under version control. Token-by-token transformation by the model stays limited to small individually verifiable units such as a single OCR page or a boundary case the script does not cover. The speaker notes name the misconception this slide exists to remove.

### Case material and datasets

Three case studies, all of them existing projects rather than teaching constructs.

- A music-archival pipeline that carries spreadsheet holdings into a linked-data model with project-specific extensions and generates an exploration interface, used to show schema mapping and tabular cleaning.
- A library pipeline from PDF scans to TEI in stages with deterministic schema validation and a human-set workflow status per document, used to place the OCR correction workflow.
- A static generator for a review journal, which replaces an XML-database infrastructure and whose declarative element mapping in YAML carries most display decisions without touching the code, used to show that data migration and interface maintenance are the same toolbox.

The hands-on runs on participants' own material in four steps, namely build a knowledge vault with a short instruction file and a document describing the data sample, place the sample and have the agent characterise it, formulate a bounded commission with acceptance criteria, then check the result against one's own expertise and run a correction round. A fallback dataset for participants without material is undecided.

The document additionally records a cut from the KUG hands-on material for this instance, namely hands-on A as the centre for preparation and authority-data matching, the pipeline-maintenance angle from the music-archival review as agent-supported maintenance, and hands-on C for the interface and endpoint part.

### Material available for intake

- Full slide texts with speaker notes, each fundamentals slide carrying a provenance field pointing at the master slide it adapts, which is the delta model applied cleanly.
- Four learning objectives in finished prose.
- A block raster for the morning, namely arrival, introduction, demo, break, hands-on, discussion.
- A two-part demo script with a four-step fallback chain, meaning live demonstration, prepared screencast, screenshot sequence in the deck, and a walkable end state through git log and diffs.
- The hands-on task in four numbered steps with a realistic outcome statement in the speaker notes.

### Open preparation items

The document marks its own gaps explicitly, which makes them cheap to carry over. Demo dataset for part one and the change task for part two are undecided; the partner institute must clear the demo state for public display; screencast fallbacks are unrecorded; the Zoom participation format in the hands-on is unresolved and determines supervision planning; setup instructions ahead of the workshop need a dispatch route through the host; the fallback dataset is undecided; the handout question is open; two evidence markers flag claims that need either a dated source or removal. No deck exists. The commissioning contract is outstanding on the host side, and the vault records checking that state before sending material.

The schedule finding deserves separate mention. The block raster carries no time values, and `ACTIVE-WORK` records that the alternative put to the operator for acceptance, ninety against seventy minutes of hands-on, does not appear in the document at all. The time distribution is therefore fixed nowhere.

### Deltas against register and profile

- No folder under `workshops/` exists for this registered id.
- The earlier draft names this document a candidate for intake into the master corpus rather than only into a profile. This analysis supports that for two items specifically, the agent-transformation slide and the artefact-checking slide, both of which are stated occasion-free already.
- The one qualification the earlier draft raises stands. At 3.5 hours this is the narrowest cut of the seven and sits closer to research data engineering than to the full arc of the line.
- Dates, title, audience and language match.

## 6. Uni for Life, Universität Graz, 2026-11-09/10

### Vault coverage

*2026-11-09 UFL Agentic-Engineering-Workshop*, the `ACTIVE-WORK` entry, and the related recurring foundational series *2026-04-13 UFL Generative KI Theorie und Praxis* on which this workshop sits.

### Specialisation

Three units of two hours each, so six contact hours in total. The first run distributes them over two days, 09.–10.11.2026, with the time of day fixed in no document. Two further runs are fixed for 2027, 19.–21.04. and 22.–24.11., each spread over three days with one unit per day, 10:00–12:00, which turns the format into a recurring course. The run of 2026 sits outside the host's own run numbering.

The thematic core is steering agentic work rather than operating a chat window, which is what separates this instance from the foundational UFL series. The host proposed the unit structure for the course website and the operator assessed it as fitting.

1. Setup, terminal and agentic fundamentals. Introduction to agentic engineering, the distinction between chatbot, assistant and agent, terminal and command line, installing and configuring Claude Code, permissions and security, a first agentic task.
2. Building a knowledge net and agentic engineering. Analysing and preparing folder structures and files, building one's own knowledge base as a working basis for agents, developing concepts and process and project plans, defining human control points, and applying all of it to grant applications, document production and multi-step work.
3. Light coding and own applications. AI-supported coding, formulating requirements, having an implementation plan produced, small applications and prototypes, simple user interfaces, and judging the possibilities and limits of agentically developed solutions.

The operator's feedback to the host adds verification of agent results against one's own holdings as an explicit point in unit two, and settles a vocabulary split. "Wissensnetz" stays as the public-facing term on the course website, while the workshop itself uses Wissensbasis and Wissenssystem.

### Case material and datasets

Deliberately general and not digital-humanities-specific, because the audience is mixed by discipline. The scenario fixed on 2026-08-05 is "KI-Strategie für Ihre Institution" at a fictitious institute abbreviated IBW. Participants draw Office files from the shared folder, meaning Word, Excel and PowerPoint documents with built-in data traps, plus a sample vault. Participants' own data is welcome alongside.

Inference on rights: a fictitious scenario with synthetic Office files carries no third-party rights, which makes this the only instance of the seven whose participant data could in principle live in a public repo. The vault states no licence for it.

### Material available for intake

The three-unit structure in the host's own wording, the recurring-course schedule for 2027, the scenario description with its file types, the vocabulary decision, and the pointer to *Steuerung agentischer Coding-Zusammenarbeit* as the conceptual base for the steering layer. No slide texts exist; the cut from the master deck onto the three units is an open task.

### Open preparation items

Audience, participant count and prior-knowledge level; the honorarium frame; the derivation of the cut from the master deck onto the three units; the time of day for the first run.

A vault-internal drift is worth flagging for any sync pass. The `ACTIVE-WORK` entry asks for the example-data state to be carried into the workshop document, on the ground that the document still lists the Office example data as open. The workshop document was updated on 2026-08-19 and now carries the IBW scenario, so the `ACTIVE-WORK` task is stale rather than the document.

### Deltas against register and profile

- The profile calls this "the extended two-day variant" and concludes that "the extended format allows the full breadth of the master corpus". Both statements are wrong against the vault. Six contact hours over two half-days is the second-shortest instance of the seven, ahead only of the 3.5-hour Göttingen half day. The register `focus` string carries the same error and is its likely source.
- The profile marks modules 3 and 4 as emphases and modules 1, 2 and 5 as drawn on. That reading survives the correction, because the three units do centre on the knowledge base and on agent operation. Inference: what changes is the depth claim, not the selection.
- The profile correctly states that the CLARIAH case material does not transfer. The vault names the concrete substitute, which the profile does not have.
- The register carries no trace of the two 2027 runs, so the instance is registered as a one-off while the vault treats it as recurring.
- Dates, title, audience and language match.

## 7. VetMed Winter School, 2026-11-30 to 2026-12-04

### Vault coverage

*VetMed Winter School* under `Projects/VeTMedAI/` is the concept document, typed as a concept with client project type rather than as a workshop document. Around it sit the parent project *VetMedAI Promptotyping und KI-Kompetenzaufbau*, the generic format *Summer School AI Data Computer Literacy* from which this instance is derived, the competence framework *AI Coding Literacy für Forschungsdaten im Museum* that supplies the level logic, and the museum workshop elaboration that supplies the setup pattern. The `ACTIVE-WORK` entry carries the task list.

### Specialisation

A five-day block week on site in Vienna, six teaching hours per day and thirty over the week, German, for administration staff and researchers without coding background. It is the fullest derivation of the seven by a wide margin.

The stated purpose is a transition, namely enabling participants to move from the pure chat interface to controlled, documented work with code, local models and an AI harness. The didactic line follows the competence framework in levels. Days one and two establish level one, meaning direct chat-based interaction plus local code execution; day three deepens that in independent data work; day four reaches level two, meaning process orchestration with an agent; day five integrates both in a participant's own application project. The cross-cutting competence over all five days is judgement, the ability to assess the quality of a generated artefact, which presupposes domain knowledge no model supplies.

The day structure is fixed in the vault at block level.

- Day 1, fundamentals of generative AI and setup. Current developments and the model landscape as frontier against open weights, how LLMs work through tokenisation, training and limits, a compact critical block covering social, ecological and legal dimensions with digital sovereignty as the bridge to practice, the method choice between generative AI and classical machine learning, then a setup block installing VS Code and Python and running a first script in the terminal, with terminal basics including reading error messages.
- Day 2, prompt and context engineering plus code in the terminal. A demonstration of a vague against a precise prompt on the same data, the AI coding literacy framework with its three interaction levels, then hands-on Python data analysis with LLM support on a VetMed-adjacent dataset, running chat-produced code locally, checking the result, handing the error message back to the model, and informed vibe coding as the stance.
- Day 3, data formats and data work. Tabular, structured, semi-structured and unstructured formats, structured knowledge representation through Markdown with YAML frontmatter, a compact data-critique block covering bias, representation, completeness, provenance and reproducibility, then a hands-on that prepares, parses and transforms a dataset and produces a small web display, tied back to the administration dashboard of the parent project.
- Day 4, AI harness and local models. Getting to know and configuring a harness, level-two agentic coding with process control and verification at scale, the data-protection question of the harness in this institutional context, running a local model on one's own hardware as practical digital sovereignty, then a hands-on that delegates a bounded task to an agent and spot-verifies the result.
- Day 5, application project and closing. Bringing the thread together in a project from the participant's own working area, presentations or an open closing before a wider circle, transfer into everyday work, and an outlook on AI agents and level three.

One application project runs across all five days as the red thread, with every new content tried on it. Administration participants anchor on report-adjacent or performance-record table data, researchers on measurement data from the institution's core-facility strand.

### Case material and datasets

Not yet chosen. The vault names the two anchor types and lists the choice of a concrete administration dataset and a concrete research dataset as an open point, with clearance of input rights before any LLM use. The three existing prototypes of the parent project serve as real demonstration objects and as templates for participants' own projects.

### Material available for intake

The full five-day block structure, eight learning objectives, the audience and prerequisite statement including laptop with administrator rights and willingness to install, the level logic mapped onto days, the red-thread design, and the account of what the preceding AI-literacy series already supplies so that the entry threshold is lowered rather than the material repeated.

### Open preparation items

The data-protection-compliant harness, which hangs on an unresolved data-protection question in the parent project and decides the shape of day four; local-model logistics covering participants' own hardware against a cloud pseudo-local solution, memory requirements and model choice; the two example datasets with their input-rights clearance; the exact split between input-led days and independent work; the closing format; whether prior participation in the AI-literacy series is required or recommended; participant cap and room equipment.

`ACTIVE-WORK` adds one content item, namely that the concept document still derives from the generic summer-school format and does not yet know the master corpus, which is to be pulled in as the derivation base.

### Deltas against register and profile

- The profile plans an EU AI Act emphasis under module 5, carried over from the predecessor series. The vault's day structure contains no such block. What it has instead is a compact critical block on day one covering social, ecological and legal dimensions plus digital sovereignty, and a data-critique block on day three. Inference: either the profile's module-5 plan is a proposal the concept document has not adopted, or the concept document is missing a governance decision. This needs an operator answer before the profile is written out.
- Day four carries local models and digital sovereignty as a substantial practical strand with a hardware requirement attached. No module in the fine cut `module-map.md` covers running a local model on one's own machine. Inference: this is either a module gap in the master or an instance-specific addition that stays in the profile.
- The register audience string "administration and research staff" omits the prerequisite the vault states, namely without coding background. That prerequisite is what makes days one and two setup-led and is therefore load-bearing for the profile.
- The register carries no duration beyond the date span. Six hours per day and thirty over the week is a fact the vault holds and the register does not.
- The display title is provisional in both artefacts, which is consistent.
- Dates, language and event match.

## Comparative table

| Instance | Audience | Duration | Module emphasis | Hands-on character | Case material |
| --- | --- | --- | --- | --- | --- |
| KUG Summer School M3GIM, 16.–17.09. | Summer-school participants; the register's no-prerequisites claim is unsourced in the vault | Two days, scope per day open | Fundamentals and Promptotyping carry the weight; knowledge and context engineering cut to the checking principle; governance a closing outlook | Four building exercises on one holding, chat interface and a vision tool, no harness, no repo work | Malaniuk estate, archive of the Kunstuniversität Graz, index tables and poster digitisates |
| CLARIAH-AT Summer School, 25.09. | Digital humanities students, BA and MA level, English | One day | Prompt engineering is the only module with an exercise of its own; agentic engineering taught through case material; verification distributed through the session | Two participant exercises plus a four-call progression demonstrated on archived runs; evidence and status discipline is the object of study | Hersch document 1000 with the Zentralbibliothek Zürich, Zweig manuscript from the Literaturarchiv Salzburg |
| HEDIT Heidelberg, 05.–06.10. | Researchers of the editions projects at the research centre | Two days of five to six hours | Agentic engineering across day 1 block 3 and all of day 2; TEI-specific knowledge and context engineering; module 5 not programmed | A full second day of workshop on participants' own material, ending in prototype presentations | Zweig letter from Stefan Zweig Digital with a CC-BY TEI header, plus synthetic tool fixtures |
| Fachschaft Mittelalterstudien Heidelberg, 08.10. | Students and early-career researchers in medieval studies | One day, no hour grid | Agentic engineering is the centre; knowledge engineering in the title; verification taught by performing it | Practical work in Claude Code throughout, full arc from source to static edition, participants bring their own access | Medieval charters from a Vienna charter corpus, primary set a family holding 1382–1414, rights pending |
| GDA Göttingen, 15.10. | Staff of academy research projects plus library guests | Half a day, 3.5 hours, hybrid | Agentic engineering and knowledge and context engineering; artefact checking as its own slide; sustainability as the framing argument | One guided run on participants' own material in four steps, plus a two-part live demonstration with a four-step fallback chain | Three existing project pipelines as case studies, participants' own data for the exercise |
| Uni for Life, 09.–10.11. | Professionals from companies and institutions across disciplines | Three units of two hours, six contact hours | Knowledge base and agent operation carry units 2 and 3; setup and security carry unit 1; verification added to unit 2 on operator feedback | Progressive across the three units from a first agentic task to a small own application, in the terminal | Fictitious institute scenario with Office files carrying built-in data traps, plus a sample vault |
| VetMed Winter School, 30.11.–04.12. | Administration staff and researchers without coding background | Five days, six hours per day | Every module in full, with a compact critical block on day 1, data critique on day 3 and harness plus local models on day 4 | An exercise every day and one application project as a red thread across the week, from chat through terminal to harness | Not yet chosen; anchors named as administration report data and core-facility measurement data |

## Cross-cutting findings

**Differentiation is real and along three axes.** The seven do not differ mainly by depth. They differ by domain (edition philology for HEDIT and Fachschaft, research data infrastructure for GDA and CLARIAH, archival data work for KUG, professional knowledge work for Uni for Life, institutional data literacy for VetMed), by execution environment (chat interface only for KUG, chat plus vision tool for CLARIAH, harness for Fachschaft, GDA, Uni for Life and VetMed), and by whose material the exercise runs on (prepared corpus for KUG, CLARIAH and Fachschaft, participants' own material for HEDIT, GDA and VetMed, a synthetic scenario for Uni for Life). Any profile template should carry those three fields explicitly, because they predict what a given instance needs far better than the module table does.

**The harness boundary is the sharpest line.** Three instances never leave the browser, four install and operate an agent. That decides prerequisites, room requirements and failure modes, and it is currently visible in no register field.

**Two instances hold teaching-ready text the repo does not have.** The KUG document and the GDA document each hold complete slide texts with speaker notes and sources under the delta model. Both are awaiting operator acceptance and neither has a deck. These are the two largest intake candidates, and the GDA document additionally holds two slides that are already phrased occasion-free and belong in the master rather than in a profile.

**Rights states differ enough to need recording per instance.** CLARIAH facsimiles need institutional clearance, Fachschaft charter images have an undocumented rights state and a pending licence, HEDIT deliberately splits its material into a distributable part and a projector-only part, KUG uses partner archive holdings without a stated licence, Uni for Life uses a synthetic scenario with no rights encumbrance, VetMed has not chosen its data and names input-rights clearance as a precondition. Inference: a `rights` field per profile would carry real information, unlike the current uniform silence.

**Three registered instances have no folder.** HEDIT, Fachschaft and GDA are in `docs/data/workshops.json` and absent from `workshops/`. The register describes seven instances, the repo profiles four, which is the most visible inconsistency for anyone reading the platform.

**Two profiles need correction rather than extension.** The Uni for Life profile states a duration that is wrong by a factor of two in contact hours, and its error is inherited from the register `focus` string. The KUG profile declares itself thin while the vault holds a complete derivation. Both were derived from register entries rather than from the vault, which is the mechanism worth fixing before the remaining three profiles are written.
