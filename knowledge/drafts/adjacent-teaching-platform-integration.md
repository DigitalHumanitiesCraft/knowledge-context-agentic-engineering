---
title: Adjacent Teaching Platform Integration
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../project.md, ../design.md, web-native-teaching-and-deep-dive-architecture.md, vetmed-teaching-material-intake.md]
---

# Adjacent Teaching Platform Integration

Source assessment for two local DHCraft teaching projects that overlap with the KCE teaching line. The projects remain independent sources until an accepted migration establishes a new canonical location for specific content.

## AI Coding Literacy

The Git repository `DigitalHumanitiesCraft/ai-coding-literacy` is a published German-language curriculum for researchers without prior programming experience. Its maintained concept defines seven competencies: Computational Thinking, Requirements Engineering, Context Engineering, Prompt Engineering, Code Literacy, Review and Domain Expertise. It includes the completed *Programmieren 2.0* workshop, exercises, handouts, Python and web examples, a glossary and a research dataset with a separate rights boundary.

Its strongest contribution to KCE is a focused competence model for AI-supported coding. It adds distinctions that the five KCE modules currently distribute across several places, especially problem decomposition, explicit requirements, the ability to read generated code and review against acceptance criteria.

The curriculum should remain an independent specialised learning path. Its conceptual scope is narrower than the KCE teaching line, and its rights, deployment and dataset contracts belong to its own repository. KCE can link to it as an external deep dive and can map its competencies to modules 02 through 05. Reusable definitions require reconciliation with `knowledge/terms.md` before they enter the Full Slide Deck or Lecture Notes.

Verified public route: <https://digitalhumanitiescraft.github.io/ai-coding-literacy/de/>

## AI Literacies prototype

The local folder `DHCraft/ai-literacies` is an Astro prototype without its own Git repository, action layer or maintained knowledge directory. It contains a multi-page Open Education Resource organised into three strands: AI Literacies, Promptotyping, and Knowledge and Project Management. Its AI Literacies strand carries six units derived from the VetMedAI teaching sequence. Five unit pages currently exist as source files, and the first unit is referenced by the strand index but has no corresponding page file.

The prototype is a strong design and content source for the planned KCE Web Modules. Its unit pages already combine a reading sequence, a sticky slide-like visual, video references and lesson sections. The `SlideViewer` component changes the visual label with the reading position through `IntersectionObserver`.

The Astro application should not be merged into the KCE runtime. KCE has an accepted no-build static publication contract, while the prototype brings Astro, TypeScript, npm dependencies, root-relative routes and a separate design system. Its content can be migrated into KCE's static Web Module components after source review. Its interaction pattern can inform a progressive enhancement, but the complete learning text must remain accessible without JavaScript.

## Content routing

| Source material | KCE destination | Function |
| --- | --- | --- |
| AI Coding Literacy competency model | external deep dive linked from KCE; selected reconciled terms in modules 02–05 | Specialised route for AI-supported coding competence. |
| Prompt Engineering unit from AI Literacies | future module-02 deep dive and relevant workshop Web Modules | Historical strategies, durable prompting practices, document-grounded steering and failure modes. |
| Tools and Models unit | modules 01, 03 and 04; VetMed and professional workshop Web Modules | Model and harness choice, retrieval, tools, agents and infrastructure constraints. |
| Multimodal Applications unit | modules 01, 04 and 05; VetMed Web Module | Multimodal workflows, transition from workflow to agent, verification and rights. |
| Data Analysis for Administration | professional and VetMed workshop profiles | Situated non-research case for structured data work and small applications. |
| Data Analysis for Research | research-data deep dive and VetMed profile | Research question, explicit knowledge document, analysis workflow and domain verification. |
| Promptotyping strand | module 04 and case index | Method introduction and links to case-based deep dives. |
| Knowledge and Project Management strand | module 03 and product-specific deep dives | Maintained project knowledge, Vault workflows and agentic work surfaces. |

## Canonical boundaries

- The KCE repository remains canonical for the five-module teaching line and its workshop profiles.
- `ai-coding-literacy` remains canonical for its seven-competency curriculum and published workshop assets.
- `ai-literacies` is source material and a design prototype. It has no canonical publication status until it receives its own repository contract or its accepted content is migrated.
- Migration copies no third-party images, datasets, screenshots or video material. Links and rights records remain attached to their source projects.
- A migrated unit receives a KCE module mapping, intended audience, source reference, verification date and an explicit editorial status.

## Recommended integration

Add AI Coding Literacy to a compact public deep-dive index as an external specialised route. Use the AI Literacies prototype as a source for the reusable Web Module component and migrate its Prompt Engineering unit first, because that page is the most fully realised browser-native lesson. Use the VetMedAI source intake to reconcile the Tools, Multimodal and Data Analysis units before they enter workshop pages.

Keep both source locations unchanged during migration. Remove or supersede a source only after the Research Director accepts the migrated content, rights basis, links and browser behaviour.

