---
title: Module Hub Architecture
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../project.md, ../design.md, ../specification.md, web-native-teaching-and-deep-dive-architecture.md, adjacent-teaching-platform-integration.md]
---

# Module Hub Architecture

Public information architecture for one prerequisite module and five subject-module hubs. The hubs make the shared module notation navigable and provide stable homes for web-native learning sequences, deep dives, tools, cases, videos and workshop relationships.

## Roles of the six hubs

Module 00 enables participation. It combines the existing practical Preparation tutorial with a foundational AI Coding Literacy route. Modules 01 through 05 remain the conceptual core of the teaching line.

| Hub | Public function |
| --- | --- |
| 00 Preparation and AI Coding Literacy | Establish the working environment and the minimum competence needed to delegate, inspect and verify computer-based work. |
| 01 Understanding Large Language Models | Explain the capability boundary, training and inference concepts, multimodality, jagged performance and interpretability limits. |
| 02 Prompt Engineering | Develop task specification, instructions, examples, output contracts, iteration and evaluation for model interactions. |
| 03 Knowledge and Context Engineering | Connect maintained project knowledge with the selection and assembly of effective task context. |
| 04 Agentic Engineering | Explain AI Harnesses, tools, agents, delegated work, parallel execution, validation and coordinated research operation. |
| 05 Critical Perspectives and Governance | Examine verification, responsibility, rights, cybernetic control, political economy and automation narratives. |

## Public routes

The existing `preparation.html` and `preparation.de.html` become the Module 00 pair and retain their stable URLs. The five subject-module pairs live under `docs/modules/`.

- `01-understanding-large-language-models.html`
- `01-understanding-large-language-models.de.html`
- `02-prompt-engineering.html`
- `02-prompt-engineering.de.html`
- `03-knowledge-context-engineering.html`
- `03-knowledge-context-engineering.de.html`
- `04-agentic-engineering.html`
- `04-agentic-engineering.de.html`
- `05-critical-perspectives-governance.html`
- `05-critical-perspectives-governance.de.html`

Every icon-and-number occurrence points to the language-matched hub. The visible title is linked where space permits. Compact workshop and video notation retains the icon and number as the link with the complete module title in its accessible name.

## Shared hub structure

1. **Module header.** Icon, number, title, one definition and one learning question.
2. **Concept map.** A rights-safe HTML, CSS or inline-SVG relation among the module's principal concepts.
3. **Starter sequence.** A short ordered web-native learning path derived from maintained module sources.
4. **Deep dives.** Optional conceptual, product-specific or domain-specific routes with an explicit parent-module relation.
5. **Tools and cases.** Concrete systems and situated workflows that realise the concepts without determining the module structure.
6. **Videos and references.** The current primary-module subset from the Video Playlist and the maintained reading route.
7. **Workshop use.** Upcoming workshop profiles that include the module, linked to their information pages.
8. **Continue.** Previous and next module links together with a return route to the complete teaching material.

The common page component carries the structure. Content length follows the subject. A hub does not need the same number of deep dives or videos as another hub.

## Module 00 internal structure

The existing Preparation sidebar remains the action route. A second clearly named route introduces AI Coding Literacy without duplicating the complete external curriculum.

### Prepare the working environment

- browser and workspace;
- files and folders;
- editor and terminal;
- Python and localhost;
- AI Harness installation and scope;
- Git and final observable check.

### Develop AI Coding Literacy

- decompose a problem into inspectable steps;
- define requirements and acceptance criteria;
- read generated code, output and error messages;
- control permissions and sensitive information;
- test a result against the task and domain evidence;
- recognise the boundary at which specialist technical review is required.

The published AI Coding Literacy curriculum is a deeper external route. Requirements Engineering also relates to Module 02, Context Engineering to Module 03, and Review and Domain Expertise to Module 05. Those relations appear as cross-links rather than duplicate teaching units.

Module 00 uses a neutral visual mark and colour treatment. It stays visible before module 01 and remains outside the five-colour subject sequence.

## Module 03 two-track structure

Knowledge and Context Engineering remains one umbrella module because task context is selected from maintained knowledge and source material. The hub exposes two tracks and one bridge.

### Context Engineering

- context window and effective context use;
- selection, ordering and compression;
- Retrieval-Augmented Generation and retrieval failure;
- session context and persistent instructions;
- Skills, Model Context Protocol resources and tool-provided context;
- context decay and explicit clearing or compaction.

### Knowledge Engineering

- Markdown and Knowledge Documents;
- Obsidian and maintained Vault structures;
- concepts, rules, examples and acceptance criteria;
- data models, schemas and ontologies;
- provenance, versioning and source relations;
- curation, reconciliation and canonical ownership.

### Bridge

Maintained project knowledge supplies inspectable source material. Context Engineering assembles the subset and arrangement needed for the current task. The prompt specifies the current action and expected result.

## Module 05 strand structure

- evaluation, validation, scholarly verification and acceptance;
- rights, responsibility, research integrity and institutional governance;
- cybernetics, feedback and digital control;
- infrastructure, labour, capital and concentration;
- automation narratives and asymmetric amplification;
- critical essays, videos and literature.

The source status of every item remains visible. Capability demonstrations support claims about the demonstrated case. Industry forecasts remain dated claims. Independent research and critical analysis supply evaluation frames.

## Relationship to other teaching surfaces

| Surface | Relation to the hub |
| --- | --- |
| Full Slide Deck | Complete reference structure and source for workshop-specific deck selection. |
| Full Lecture Notes | Expanded maintained explanation and literature route. |
| Workshop Web Module | Event-specific sequence that links to the hubs it activates. |
| Deep dive | Optional depth beneath one or more parent modules. |
| Tutorial | Executable procedure with observable checks. |
| Video Playlist | Current audiovisual route, grouped by primary module and linked from the hubs. |

## Source boundaries

- Maintained KCE module text comes from the Full Slide Deck, Full Lecture Notes and module files.
- AI Coding Literacy remains canonical in its own repository and enters as a linked specialised route.
- The local AI Literacies Astro folder is a source and design prototype. Accepted content is re-authored in KCE's static component system.
- VetMedAI decks and Vault notes supply source evidence for relevant deep dives. Their product claims and rights require re-verification.
- Module 05 uses the maintained source map to distinguish public playlist candidates, literature and dated claim evidence.

## Accessibility and responsive behaviour

- Links expose icon, number and complete module title to assistive technology.
- Module colour never carries meaning alone.
- Concept maps have a textual equivalent in reading order.
- Sticky navigation becomes an ordinary horizontal or block route at narrow widths and creates no scroll trap.
- Every deep-dive and workshop relationship is represented by a native link.
- Web-native sequences remain complete without JavaScript; optional enhancements respect reduced motion.
- Headings, landmarks, language pairs and focus order follow the shared page contract.

## Acceptance boundary

The Research Director first accepts the common hub component, Module 00 and the substantive structure of each subject hub. Individual deep dives receive separate acceptance when they add new claims, source rights or volatile product instructions.

