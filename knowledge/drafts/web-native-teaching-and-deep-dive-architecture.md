---
title: Web-native Teaching and Deep-dive Architecture
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../design.md, ../project.md, ../specification.md, codex-bootcamp-101-evidence.md, claude-code-agentic-engineering-subchapter.md]
---

# Web-native Teaching and Deep-dive Architecture

## Purpose

The teaching platform can develop from a catalogue of workshop materials into the primary teaching environment. Its stable five-module structure provides orientation. Web-native slide sequences, tutorials, deep dives and cases can then expose different levels of detail without forcing every audience through the same domain material.

The central design problem is differentiation. A module defines a durable conceptual field. A deep dive develops one problem within or across modules. A case follows a situated actor and a concrete transformation. A workshop selects from all three and adds its own sequence, exercises and institutional context. These forms should share visual identity and source knowledge while retaining different teaching functions.

## Content model

| Layer | Function | Typical scale | Current or proposed example |
| --- | --- | --- | --- |
| Core module | Establishes concepts and engineering distinctions that recur across audiences | stable section of the complete material | Knowledge and Context Engineering |
| Deep dive | Develops one concept family beyond the core sequence | optional reading or focused slide sequence | Research Data and Knowledge Work |
| Case | Makes a workflow inspectable through a situated goal, materials, constraints, tools and acceptance criteria | one narrative route through several modules | From digitised source to research data archive |
| Tutorial | Enables a reader to perform a bounded procedure and verify an observable result | scrollable action sequence | Preparation and product-specific introductions |
| Workshop profile | Selects and rearranges modules, deep dives and cases for a defined audience | event-specific teaching sequence | Research-data summer school or professional training |

This model prevents the five modules from becoming containers for every available detail. It also prevents domain examples from being presented as universal workflows.

## Shared module notation

The five subject-specific icons and numbers form a portable orientation system. Their public use already covers the landing hero, workshop subsets and video groups. The same notation can support further surfaces:

- a module marker in the header or footer of a web-native slide;
- the parent-module reference on a deep-dive page;
- the concepts activated by a case;
- the current position inside a tutorial sidebar;
- filtering and comparison in a later material index;
- references from Lecture Notes to related videos and cases.

Compact icon rows require an explanatory route. Each item should link to the full module title and carry that title as its accessible name. Colour and icon reinforce the label but never replace it.

## Proposed deep dive: Research Data and Knowledge Work

The research-data material should become a deep dive because it asks a broader question than a single digitisation workflow: how do representations acquire the status of research data, and how does that status change AI-supported knowledge work?

The deep dive spans modules 03, 04 and 05. Module 03 supplies explicit knowledge, representations and context. Module 04 supplies tool-supported transformations and executable workflows. Module 05 supplies provenance, authority, rights, validation and acceptance. Modules 01 and 02 enter where models interpret source material or prompts specify a transformation.

### Learning question

**When does digitised material become research data, and what knowledge must remain attached to it for later assessment, preservation and reuse?**

### Proposed internal units

1. **What counts as research data?** Research data are selected, created or transformed representations used as evidence in a research process. Their status depends on a research question, scholarly practice and documented acceptance.
2. **Data are constructed representations.** The distinction between data and capta makes selection and modelling visible. A physical object, digital image, transcription and structured representation are related but not interchangeable.
3. **What is knowledge in the workflow?** Domain concepts, source descriptions, modelling decisions, rules, examples, uncertainty and acceptance criteria have different functions. A maintained knowledge base records these relations without replacing the sources or data.
4. **Representation changes require provenance.** Every transition introduces affordances, omissions and uncertainty. The workflow records source relations, transformations, model and tool states, review actions and responsible acceptance.
5. **From working data to a preservable package.** Metadata, identifiers, formats, rights, documentation and repository requirements determine whether a result can be ingested, found, interpreted and reused. Repository transfer is an institutional process rather than a file upload alone.
6. **AI output is an intermediate state.** A fluent transcription, extraction or generated schema becomes research data only through task-specific evaluation, scholarly verification and an explicit decision about its status.
7. **How agentic work changes knowledge work.** An AI harness can coordinate files, tools, transformations and checks. Researchers remain responsible for goals, modelling choices, source interpretation, rights and acceptance.

The units should link to the complete Lecture Notes instead of duplicating their literature apparatus. A focused web-slide sequence can carry the argumentative core; the deep-dive page can provide definitions, diagrams, references and routes into cases.

## Proposed case: From digitised source to research data archive

The personalised research-data scenario is didactically strong as a case under the deep dive. It gives agentic work a concrete object and makes the difference between task execution and epistemic responsibility observable.

### Situated actor

A research-data curator at a cultural heritage institution must turn digitised estate material into a documented package that a research data repository can preserve and disseminate. The actor coordinates scholarly requirements, source context, technical formats, rights information and repository rules. This role is a teaching construct that makes requirements explicit; it is not empirical user research.

### Goal and states

The goal is a preservable, identifiable and assessable research data package. The workflow may pass through the following states:

1. archival object and collection context;
2. digital representation with stable source relation;
3. descriptive metadata and identifiers;
4. transcription with explicit uncertainty;
5. structured entities, properties and relations;
6. provenance, rights and validation records;
7. repository package and ingest checks;
8. accepted and disseminated representation with documented limits.

The states describe representational changes rather than a universal linear pipeline. Review can return a result to an earlier state. Repository requirements can alter the data model, and rights constraints can prevent dissemination even when a technical package validates.

### Agentic working loop

The case can explain Agentic Engineering through one inspectable loop:

- **Orient:** read the research question, source description, rights statement and repository profile.
- **Plan:** separate transformations, deterministic checks and scholarly decisions.
- **Select context:** provide the relevant model, examples, schema and acceptance criteria for the current transition.
- **Act with tools:** inspect files, run transformations, generate structured data and record intermediate outputs.
- **Validate:** test syntax, schema conformance, identifiers, package structure and reproducibility.
- **Verify:** compare transformations with the source and assess domain adequacy, uncertainty and interpretative consequences.
- **Accept and write back:** a responsible person assigns status, records the decision and updates maintained project knowledge.

The distinction between validation, verification and acceptance is central. A technically valid package can still be unsuitable as research data.

### Rights-safe visual strategy

The public case must not reproduce source facsimiles. It can use a schematic chain of abstract document states, a synthetic sample, file trees, metadata fragments and package manifests created for teaching. Links may lead to external project interfaces where source institutions publish the material. Any later screenshot requires a documented reuse right and removal of personal or confidential information.

## Critical assessment of the case idea

### Strengths

- A situated goal gives the engineering concepts a reason to exist.
- Representational transitions make provenance and uncertainty visible.
- The case connects Knowledge, Context, Agentic Engineering and Governance without treating them as independent techniques.
- Repository ingest supplies deterministic feedback while scholarly acceptance exposes the limits of technical validation.
- The same structure can support lecture, tutorial and exercise forms.

### Risks and corrections

| Risk | Correction |
| --- | --- |
| The case implies that digitisation automatically produces research data. | Begin with the status question and show that research use, documentation and acceptance establish the role of a representation. |
| A linear pipeline hides revision and negotiation. | Present state transitions with return paths and decision points. |
| The persona is mistaken for evidence about real users. | Label the actor as a provisional requirements construct and verify assumptions with institutional practice. |
| The domain case dominates the general teaching line. | Keep it as an optional case under a research-data deep dive and link general concepts back to the five modules. |
| Tool execution appears to replace scholarly judgement. | Separate executable validation, source-based verification and responsible acceptance on every transition. |
| Public teaching material inherits unresolved image rights. | Use original schematics and synthetic examples; link to rights-bearing source systems. |

The recommended form is therefore a two-part specialisation: a conceptual deep dive on research data and knowledge work, followed by the archive case as an applied route. Combining both into one case-only chapter would reduce the conceptual transfer to other domains.

## Relevance across audiences

The complete research-data deep dive belongs in workshops for digital humanities, cultural heritage, research software and data stewardship. Professional audiences outside research may not require repository models, scholarly representation or source criticism. They can still use the general pattern: a document moves through representations, each transformation requires context and criteria, tools produce intermediate states, and a responsible role accepts the result.

The professional-training profile should therefore receive the module concepts and a domain-near case from organisational knowledge work. The research-data deep dive remains available for reference and comparison. This arrangement preserves access without treating every specialised unit as compulsory.

## Web-native teaching surfaces

The current Preparation page demonstrates a useful reading model: persistent navigation, ordinary scrolling, direct anchors, one visual state beside one explanation and responsive stacking. Its exact tutorial panels should not become presentation slides. Tutorials contain definitions, actions and checks; a slide must express one claim or question in a controlled 16:9 composition without internal scrolling.

The platform should derive three visual grammars from the same tokens:

- **Reading page:** continuous text for About, deep dives and references;
- **Tutorial sequence:** content-driven panels with actions and observable checks;
- **Web slide deck:** 16:9 sections with an assertion title, one principal visual relation, quiet module marker, direct anchor and print-to-PDF rules.

Google Slides can remain a supplementary editable or downloadable surface. A web-native deck can become the maintained presentation surface only after its source text, print export, presenter navigation and offline behaviour have been verified.

## First web-slide pilot

The current research-data workshop is the strongest pilot because its Lecture Notes are the authoritative source and already contain the required conceptual arc. A ten-slide English sequence can test the web-slide grammar:

1. When does model output become research data?
2. Research data are constructed through scholarly workflows.
3. Model output is an intermediate state.
4. A research prompt separates task, context, rules and output.
5. Prefer explicit uncertainty to plausible reconstruction.
6. Fluent interpretation is not evidence of source fidelity.
7. Project knowledge, working context and the prompt answer different questions.
8. An AI harness operationalises the Promptotyping feedback loop.
9. Source to transcription and transcription to structured information are different transitions.
10. Evaluation, validation and scholarly verification answer different questions.

The pilot should use original HTML/CSS diagrams and source-grounded text from the repository. It should not copy the external slide deck, source images or layouts with unresolved reuse rights.

## Product deep dives and the same architecture

The dedicated Claude Code introduction and the source note for Codex Bootcamp 101 demonstrate a second deep-dive family. Product deep dives should explain how a specific harness realises the general Agentic Engineering concepts. Volatile commands and interface details belong in dated reference panels. Persistent concepts such as workspace instructions, bounded delegation, context management, review and validation link back to module 04.

The platform can therefore support several deep dives without losing coherence:

- Research Data and Knowledge Work under modules 03–05;
- the archive case as an applied research-data route;
- Claude Code and Codex as harness-specific routes under module 04;
- later governance or evaluation deep dives under module 05.

Every deep dive declares its parent modules, intended audience, prerequisites, maintained source, verification date and relation to workshop profiles.

## Publication and business model

The About page explains why these surfaces are publicly available. Commissioned workshops finance research, editorial revision, technical implementation and maintenance. Each commission receives a domain-specific teaching profile. Generally applicable results return to the shared public material. This formulation connects commercial work with transparent knowledge maintenance without presenting DHCraft as a charitable provider or reducing the platform to an acquisition surface.

## Recommended decision

Adopt a three-level teaching architecture:

1. five stable core modules for shared orientation;
2. optional deep dives for conceptual or product-specific depth;
3. situated cases that traverse several modules through one inspectable workflow.

Develop Research Data and Knowledge Work as the first conceptual deep dive. Place the archive persona beneath it as a concrete case. Use the current research-data workshop for the first ten-slide web-native pilot. Keep the professional-training profile on the shared module path and offer the research-data material as optional reference.

This decision would preserve a coherent teaching line while allowing depth, audience adaptation and public reuse. It also creates a source model in which complete material, workshops, tutorials, videos and future web slides can refer to the same maintained concepts instead of becoming separate content collections.

## Open editorial decisions

- Confirm the final title and module ownership of the Research Data and Knowledge Work deep dive.
- Confirm whether the archive case uses a fully synthetic teaching package or links to an external institutional example.
- Accept the ten-slide pilot cut before `slide-deck.md` becomes a maintained source.
- Define the minimum metadata record for deep dives and cases.
- Decide when a web-native deck becomes the primary presentation surface and Google Slides becomes a derived export.
- Select rights-safe logos, diagrams and screenshots, if any, for the pilot.
