# Page Copy (Draft)

Complete text inventory for the platform under `docs/`, written so that a later sync pass can paste the blocks into the pages. Nothing here is decided; the copy rests on `project.md`, `specification.md`, `design.md`, `drafts/module-map.md`, `drafts/media-map.md`, `drafts/card-redesign-feedback.md`, `docs/data/workshops.json` and the five workshop profiles. Paste-ready text stands in blockquotes, everything outside a blockquote is a working note.

Two marking conventions hold throughout. `[TBD: ...]` marks a fact that no artifact of this repo states, so the sync pass either fills it from an operator answer or drops the sentence. A note beginning with "Inference" marks a claim derived from the sources rather than stated in them.

Spelling is American throughout this document, as commissioned. The existing repo texts use British spelling ("specialisation", "organised", "programme"), so a sync pass has to unify one way or the other before publication; the mixture is currently a real delta. Two terms keep their canonical spelling regardless, "Scholar-Centred Design" and "Research Mission Control", because they are named terms of the corpus rather than ordinary words.

Module numbering follows the master, meaning 1 Understanding Large Language Models, 2 Prompt Engineering, 3 Knowledge and Context Engineering, 4 Agentic Engineering, 5 Critical Perspectives and Governance. Unit ids `M1` to `M19` refer to the 19-unit fine cut in `drafts/module-map.md`, which is a draft.

## 1. Start page lead

> Knowledge, Context and Agentic Engineering for Knowledge Work is a teaching line on working with frontier language models inside AI harnesses, addressed to everyone doing computer-based, data-driven knowledge work. The material exists once as a master corpus in five modules, from what a language model is through prompt, context and knowledge engineering to agentic workflows, verification and governance. Every workshop listed below is a profile over that corpus, meaning a documented selection of modules with its own depth, case material, language and hands-on.

Optional line beneath the module list, recommended in `media-map.md` so that the master page carries the running long form without individual links.

> The blog and the video channel of Digital Humanities Craft carry the same material in its running long form; the per-workshop selection lives on the workshop pages.

Note. `specification.md` requires the repository link on the start page. The lead does not carry it, so the link belongs in the hero as the single link that `design.md` allows there.

## 2. Module texts

Each module carries a two-sentence description and its unit subpoints as short noun phrases. The assignment of the 19 units to the five modules is an inference from `drafts/module-map.md`, the CLARIAH-AT profile module table and the operator decision recorded in `journal.md` that Promptotyping, verification and the case studies sit under module 4. The fine cut itself stays a draft, so unit lists on the pages are provisional.

### Module 1 Understanding Large Language Models

> What a frontier language model is as a system, meaning its jagged capability profile, confabulation and sycophancy, the latent program space it searches, and the assistant character that a product ships on top of the underlying model. The module also locates the current landscape, meaning the model ecosystems, the degrees of openness from open weights to the Open Source AI Definition, hosted access against local deployment, and the capability signals that show where the frontier currently runs.

Unit subpoints.

- Model ecosystems and degrees of openness (M3)
- Hosted access, local deployment, the harness as a system dimension (M3)
- Capability signals and the moving frontier (M4)
- Asymmetric amplification and the jaggedness argument (M4)
- Confabulation, sycophancy, jagged capability (M5)
- Latent program space, prompting as external search, reasoning as internal search (M5)
- Training stages and the assistant character (M5)
- Multimodality and vision-language models (from M14, taught inside this module in the CLARIAH-AT profile)

Note. The German instances add architecture material that the fine cut does not list as its own unit, meaning next-token prediction, the transformer, pre-training against post-training, embeddings and tokenization. `workshops/2026-04-22-vetmedai-workshop-1/profile.md` records that block as the most complete German version of module 1 in the corpus. Whether it becomes a unit of the master or stays instance material is open.

### Module 2 Prompt Engineering

> Prompt engineering as the iterative development of one input sequence for a given model and task, with the four-part working structure of task, context, rules and output, and with the prompt as a bounded specification that points at persistent project rules instead of repeating them. The module carries the empirical instability of prompting effects across model, language, task and metric, together with the practical principles that survive that instability.

Unit subpoints, derived from the M7 unit summary because module 2 currently holds one unit.

- Four-part prompt structure (task, context, rules, output)
- The prompt as a bounded specification
- Instability of prompting effects across model, language, task and metric
- Practical principles and countermeasures against sycophancy
- Chain of thought against reasoning models (instance material, VetMedAI 2026-04-22)

### Module 3 Knowledge and Context Engineering

> The context window as a technical processing limit against the working context as the information state assembled for one task, with position, distraction and context-rot effects as the reason to aim at a dense sufficient context rather than a maximal one. On the knowledge side the module defines the maintained, inspectable and revisable project knowledge base, the three document functions of declarative knowledge, process and agent instruction, and the `knowledge/` folder that carries them.

Unit subpoints.

- The four engineering layers and their interplay (M6)
- Context window against working context (M8)
- Position, distraction and context rot (M8)
- Knowledge documents and their properties (M9)
- The `knowledge/` folder and its three document functions (M9)
- Markdown as a portable carrier without semantic guarantees (M9)

### Module 4 Agentic Engineering

> The step from language model to agent, with the harness defined by memory, tools, permissions, hooks and observability, and with the execution loop that keeps identifiable states, unchanged raw outputs and referenced run identities. The module carries Promptotyping as the working method, the prepared working environment with API access and structured output, verification against the source, and the case studies that run a full path from a facsimile to a research data package.

Unit subpoints.

- Harness components and least-privilege tool access (M10)
- The agentic execution loop and run identity (M10)
- Subagents with separate write territories and explicit handoffs (M10)
- Working environment, API access, structured output (M11)
- Promptotyping and Scholar-Centred Design (M12)
- Verification, validation and the critical expert (M13)
- From facsimile to a research data package (M14)
- Case study Hersch, a documented pilot dataset (M15)
- Case study Zweig, transcribing a complex facsimile (M16)

Note. The assignment of M13 is contested. `journal.md` records the operator decision that verification sits under module 4, while the CLARIAH-AT profile lists the verification section of its script under module 5. Until that is settled, the unit list of one module names verification and the badge row of the other counts it, which the pages must not present as two different facts.

### Module 5 Critical Perspectives and Governance

> Documented rules, roles and decision rights for authority, permissions, review status, rights and write-back, together with Research Mission Control as the method that separates research, operational and verification functions and fixes the passage from clarification to implementation. The module also carries the critical line running through the whole corpus, meaning openness and open-washing, the concentration of technical power and the ecological cost of frontier systems, the regulatory obligations an institution actually carries, and the rule that model agreement is no substitute for scholarly verification.

Unit subpoints.

- Project governance, rules, roles and decision rights (M18)
- Research Mission Control and the choice of verification form by object and error risk (M18)
- Openness, open-washing, local deployment (from M3)
- Power concentration and ecological cost of frontier systems (from the M1 framing)
- EU AI Act obligations for a deploying institution (instance material, VetMedAI 2026-04-22)
- Limits, glossary and apparatus (M19)

Note. Two assignments stay open. `drafts/module-map.md` asks whether M19 is a module unit at all or an appendix that every module references, and M17 (topic annotation against statistical topic modeling) is assigned to no top-level module in any artifact. The framing units M1 (Applied Generative AI) and M2 (research data, representation and provenance) are likewise unassigned; the CLARIAH-AT profile records them as carrying the domain framing of that instance without placing them in one of the five modules. `[TBD: top-level assignment of M1, M2, M17 and M19]`

## 3. Workshop card texts

One right-panel text, one extent label and one module coverage table per registered workshop, in the chronological order that `specification.md` prescribes for the card list. The coverage table is the data the badge row encodes, with the vocabulary `full`, `touched` and `absent` from `drafts/card-redesign-feedback.md`; the basis column states where the depth reading comes from and stays out of the rendered page.

### VetMedAI Workshop 1, taught 2026-04-22

Register note. This instance is prepared in `drafts/past-instances-registry.md` and is not yet an entry in `docs/data/workshops.json`. The card text below assumes the entry is applied first; without it the card has no register row to render from.

> The session builds the German-language foundation of the corpus, from next-token prediction and the transformer through pre-training and post-training, embeddings, tokenization and the limitations of language models. Prompt engineering follows on a labeled prompt anatomy that is extended through a chain of follow-up prompts, so iteration becomes visible as the working mode. Context window, context rot, Markdown and the knowledge document give the conceptual bridge, and a short closing block defines AI agents and agentic AI without operating a harness. The EU AI Act block carries the participant exercise, in which the regulation is distilled into a knowledge document that is then loaded into a fresh conversation and queried, so the governance content and the knowledge-document method are taught in one movement. The audience is university staff in an institutional AI-competence program. `[TBD: prerequisites; the source records none]`

Extent label.

> `[TBD: duration]`, introductory, one participant exercise

Note. The profile states that duration, breaks, participant count and room are undocumented. Until the operator supplies a duration, the label carries the depth reading alone, for example "introductory, one participant exercise".

| Module | Depth | Basis |
| --- | --- | --- |
| 1 Understanding Large Language Models | full | profile, "taught in full and at the greatest depth of this instance" |
| 2 Prompt Engineering | full | profile, "taught in full with a demonstrated rather than a participant-run example" |
| 3 Knowledge and Context Engineering | touched | profile, "conceptual depth without a separate exercise" |
| 4 Agentic Engineering | touched | profile, "thinnest module of this instance, taught as a short closing block" |
| 5 Critical Perspectives and Governance | full | profile, "taught as a substantial block with the only participant exercise of this instance" |

Units worth exposing on this card, since the card may show subpoints per `drafts/card-redesign-feedback.md`. LLM architecture and limitations, prompt anatomy, knowledge documents, EU AI Act.

### KUG Summer School (M3GIM), 2026-09-16 and 17

> The compact profile of the corpus, for participants who bring neither an LLM nor a programming background. The opening carries module 1, so the session starts at what a language model is and where its capabilities are jagged. Prompt engineering follows as the module with the participant exercise, because a prompting exercise runs without programming prerequisites. Knowledge and context engineering are introduced far enough that the working context and the knowledge document become usable ideas, and agentic engineering appears as an outlook on what the introduced layers lead to. Teaching language is German.

Extent label.

> two days, introductory, no prerequisites `[TBD: whether the unit fills both days, and the daily timings]`

Note. The profile calls this the compact profile and a short introduction, while the register books two dates. The tension is real and belongs to the operator, since a two-day booking and a short introduction do not describe the same extent.

| Module | Depth | Basis |
| --- | --- | --- |
| 1 Understanding Large Language Models | full | profile, "emphasis, carries the opening and the conceptual weight" |
| 2 Prompt Engineering | full | profile, "emphasis, the participant exercise is expected here" |
| 3 Knowledge and Context Engineering | touched | profile, "light touch" |
| 4 Agentic Engineering | touched | profile, "light touch, shown as an outlook" |
| 5 Critical Perspectives and Governance | `[TBD]` | profile, "undecided at this stage" |

Note on the badge row. The vocabulary holds three values and this instance needs a fourth state for module 5, meaning undecided rather than absent. Rendering it as absent would assert a selection the profile has not made.

### CLARIAH-AT Summer School 2026, 2026-09-25

> The single-day unit specializes the corpus on research data workflows and digital scholarly editions, so humanities research data appear as constructed representations and the case material comes from two edition projects, the Jeanne Hersch workflow with the Zentralbibliothek Zürich and the Stefan Zweig workflow with Stefan Zweig Digital at the Literaturarchiv Salzburg. Module 1 runs at the greatest textual depth of any instance, and its vision-language section carries the specialization, because the failure mode it names, a contextually plausible reading unsupported by the facsimile, is what the transcription exercise has to expose. Prompt engineering is the one module with a participant exercise of its own, introduced on a compact example and then applied to a difficult manuscript page. Knowledge, context and agentic engineering are taught conceptually and through the two edition workflows rather than through agent operation by the participants, and the separation of evaluation, validation and scholarly verification stands as its own section. The audience is digital humanities students at BA and MA level, and the teaching language is English.

Extent label.

> one day, full depth on modules 1 and 2, two hands-on units

Note. `[TBD: timings, breaks and the placement of the unit inside the summer school week]`, which the profile states are fixed in no artifact. Prerequisites are named in no artifact either; the register states the audience only. Hands-on 1 works with a multimodal frontier model on a facsimile, so participants need model access, which is an inference from the script rather than a stated requirement.

| Module | Depth | Basis |
| --- | --- | --- |
| 1 Understanding Large Language Models | full | profile, "taught in full and at the greatest textual depth of this instance" |
| 2 Prompt Engineering | full | profile, "taught in full and as the only module with a participant exercise of its own" |
| 3 Knowledge and Context Engineering | full | profile, "conceptual depth without an exercise" |
| 4 Agentic Engineering | full | profile, taught through the two edition workflows as case material |
| 5 Critical Perspectives and Governance | touched | profile, "distributed across the session instead of taught as a closing block" |

Units worth exposing on this card. Multimodality and vision-language models, the four-part prompt structure, Promptotyping, evaluation against validation against scholarly verification.

### Uni for Life, 2026-11-09 and 10

> The extended two-day variant for professionals from companies and institutions across disciplines, taught in German. The domain framing runs through professional knowledge work, so the edition case material of the summer-school profile is replaced. Knowledge and context engineering carry the first emphasis, because a maintained knowledge base and an assembled working context transfer most directly to professional knowledge work. Agentic engineering carries the second and gives the instance its registered title, with the harness, controlled agent workflows and the prepared working environment on the second day. Module 1 is drawn on at working depth as the foundation the later modules refer back to, and prompt engineering serves as the entry layer with the four-part prompt structure and the practical principles.

Extent label.

> two days, extended breadth, emphasis on knowledge, context and agentic engineering `[TBD: day split, schedule and hands-on units]`

Note. `[TBD: prerequisites]`. The profile names none, and the audience description carries no technical assumption either way.

| Module | Depth | Basis |
| --- | --- | --- |
| 1 Understanding Large Language Models | touched | profile, "at working depth rather than in full" |
| 2 Prompt Engineering | touched | profile, "drawn on as the entry layer" |
| 3 Knowledge and Context Engineering | full | profile, "emphasis" |
| 4 Agentic Engineering | full | profile, "emphasis", named in the registered title |
| 5 Critical Perspectives and Governance | touched | profile, "drawn on, with the selection of governance topics still open" |

### VetMed Winter School, 2026-11-30 to 2026-12-04

> The five-day block week is the fullest derivation of the master corpus among the registered instances, the one profile with room for every module and for hands-on work in each of them. The audience is administration and research staff, and the instance is the follow-up format to the institution's earlier AI-competence program, whose German LLM-fundamentals material is the closest existing source for module 1. Prompt engineering, knowledge and context engineering and agentic engineering each run in full and each with a participant exercise, including the prepared working environment and controlled agent workflows. Critical perspectives and governance carry their own weight here, meaning the AI-literacy obligation, the definitions and the risk tiers of the EU AI Act alongside verification and the limits of model agreement. Teaching language is German.

Extent label.

> five days, full derivation of the master, participant exercise in every module `[TBD: distribution over the five days and placement of the hands-on units]`

Note. The display title *VetMed Winter School* is provisional per `journal.md` and stands until the operator supplies the final one, so the card headline is `[TBD: final title]`. `[TBD: prerequisites]`, which the profile does not state.

| Module | Depth | Basis |
| --- | --- | --- |
| 1 Understanding Large Language Models | full | profile, "taught in full" |
| 2 Prompt Engineering | full | profile, "taught in full, with a participant exercise" |
| 3 Knowledge and Context Engineering | full | profile, "taught in full, with a participant exercise" |
| 4 Agentic Engineering | full | profile, "taught in full, with a participant exercise" |
| 5 Critical Perspectives and Governance | full | profile, "taught in full and with its own weight" |

## 4. Subpage copy blocks

One set per workshop, following the six-block structure of `specification.md`. Blocks with no content are omitted per workshop rather than rendered empty, so an intro sentence below is only pasted once its block has material. The materials intro covers the slides block and the script-excerpt block together, since both name teaching surfaces.

### VetMedAI Workshop 1

Header line.

> VetMedAI, Veterinärmedizinische Universität Wien · 22 April 2026 · German · university staff in an institutional AI-competence program

Schedule intro.

> `[TBD: schedule]`. The source is a slide-text export whose sequence is the taught order, so the block stays omitted until the operator supplies timings.

Materials intro.

> The record of this instance is the slide text as it was taught on 22 April 2026. No live deck and no script surface are named in the source, so both stay unlinked.

Hands-on intro.

> Participants distilled the EU AI Act into a knowledge document, then opened a fresh conversation, loaded the document and queried it against a case of their own.

Follow-up intro.

> Material that continues the two modules this session carried in full, the fundamentals of language models and prompt engineering.

Language disclaimer line.

> The linked videos and posts are in German, the teaching language of this instance.

### KUG Summer School (M3GIM)

Header line.

> KUG Summer School (M3GIM), Kunstuniversität Graz · 16 and 17 September 2026 · German · participants without an LLM or programming background

Schedule intro.

> `[TBD: schedule]`. The profile fixes no sequence and no timings, so the block stays omitted.

Materials intro.

> Deck and script for this instance are in preparation and appear here once they exist.

Hands-on intro.

> `[TBD: hands-on]`. The profile expects the participant exercise in the prompt-engineering module and fixes no task yet.

Follow-up intro.

> Material for working on alone afterwards, selected for the two modules this session emphasizes.

Language disclaimer line.

> The linked videos and posts are in German, the teaching language of this instance.

### CLARIAH-AT Summer School 2026

Header line.

> CLARIAH-AT Summer School 2026, Machine Learning for Digital Scholarly Editions · 25 September 2026 · English · digital humanities students at BA and MA level

Schedule intro.

> The taught sequence follows the section order of the lecture notes, from the domain framing through the capability landscape and prompt engineering to the two hands-on units and the closing section on verification. `[TBD: timings and breaks]`

Materials intro.

> The lecture notes are the content record of this unit; the live deck and the script surface are the teaching surfaces linked beside them. The executable hands-on package is maintained in a separate repository.

Hands-on intro.

> Two exercises run in sequence and stay separable. The first transcribes page 1 of Stefan Zweig's manuscript *Radiovortrag über Newyork* from a reusable prompt skeleton with a catalogue metadata block, then reviews the generated transcription against the facsimile. The second takes that transcription as input and extracts structured information against an explicit schema, so each representational transition carries its own failure modes and acceptance criteria.

Follow-up intro.

> Recorded sessions and posts that continue the lines of this unit, meaning transcription workflows with the editor in the loop, agentic edition pipelines and the argument behind asymmetric amplification.

Language disclaimer line.

> The videos are in German and two of the posts are in English; the language of each entry is labeled.

### Uni for Life

Header line.

> Uni for Life, Universität Graz · 9 and 10 November 2026 · German · professionals from companies and institutions across disciplines

Schedule intro.

> `[TBD: schedule]`. Neither the day split nor a sequence is fixed, so the block stays omitted.

Materials intro.

> Deck and script for this instance are in preparation and appear here once they exist.

Hands-on intro.

> `[TBD: hands-on]`. The profile fixes no exercises for the two emphasized modules yet.

Follow-up intro.

> Recorded sessions that show the emphasized modules at work, meaning a maintained knowledge base built up step by step and agentic workflows on data outside edition work.

Language disclaimer line.

> The linked videos and posts are in German, the teaching language of this instance.

### VetMed Winter School

Header line.

> `[TBD: final title]`, Veterinärmedizinische Universität Wien · 30 November to 4 December 2026 · German · administration and research staff

Schedule intro.

> `[TBD: schedule]`. The distribution of the five modules over the five days is open, so the block stays omitted.

Materials intro.

> Deck and script for this instance are in preparation and appear here once they exist.

Hands-on intro.

> Every module of this derivation carries a participant exercise. `[TBD: the individual tasks and their placement]`

Follow-up intro.

> Material for each of the five modules, so that every part of the block week has a continuation to work with afterwards.

Language disclaimer line.

> The linked videos and posts are in German, the teaching language of this instance.

## 5. Footer texts

Imprint line, without a personal address.

> Christopher Pollin, Digital Humanities Craft OG · dhcraft.org · office@dhcraft.org

Note. `[TBD: registered seat, register number and VAT id]` if the site is to carry a legally complete imprint. No artifact of this repo holds those, and inventing them is out of the question. Should a full imprint be required, linking the imprint page of dhcraft.org is the cleaner route than restating it here.

License line.

> Text content licensed CC BY 4.0. Slide decks are checked individually for third-party image rights.

Optional rights line, grounded in `governance.md`, for pages that show edition case material.

> No facsimiles are hosted here; image rights of the Hersch and Zweig material remain with the source projects, which are linked.

Method line.

> Built with Promptotyping

Optional source line, for the requirement in `specification.md` that the repository is reachable.

> Source and master corpus on GitHub

## 6. Open points

1. `[TBD: top-level module assignment]` for the units M1, M2, M17 and M19, which no artifact assigns. Affects the unit subpoints of modules 1, 4 and 5.
2. Assignment of M13 (verification). `journal.md` places it under module 4, the CLARIAH-AT profile table places its script sections under module 5. The pages would otherwise state both.
3. `[TBD: badge state for an undecided module]`. The KUG profile leaves module 5 undecided, and the three-value vocabulary of `card-redesign-feedback.md` holds no state for it.
4. `[TBD: duration]` for the VetMedAI instance, and `[TBD: schedule]` for all four planned instances. Only the CLARIAH-AT unit has a fixed taught sequence, and even there the timings are open.
5. `[TBD: prerequisites]` for the CLARIAH-AT, Uni for Life and VetMed instances. Only the KUG entry states a prerequisite, namely that none are assumed.
6. `[TBD: final title]` for the VetMed Winter School, which is provisional per `journal.md`.
7. Register gap. The VetMedAI instance has a card text here but no entry in `docs/data/workshops.json`; the prepared entry lies in `drafts/past-instances-registry.md`. The ÖAW AI Winter School (2026-02-17) is in the same state and was not commissioned as a card here, so it currently has no copy.
8. Register growth. `drafts/additional-past-instances.md`, written in parallel, prepares four further instances for the register, one taught and three forthcoming. Each of them needs a card text, an extent label, a coverage table and a subpage set in the form used here once the operator applies the entries.
9. Spelling regime. This document is American, the repo texts are British. One of the two has to give before publication.
10. Follow-up entries. `media-map.md` flags five videos as possibly Patreon-exclusive and one blog post whose live text may change without its URL changing. Both states need checking before a follow-up block links them.
