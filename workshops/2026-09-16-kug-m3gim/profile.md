---
title: "Workshop Profile KUG M3GIM 2026"
workshop:
  id: 2026-09-16-kug-m3gim
  dates: 2026-09-16/17
  title: Promptotyping und Generative AI
  event: "KUG Summer School (M3GIM), Kunstuniversität Graz"
  audience: participants without LLM or programming background
  language: de
  status: planned
status: in preparation
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/specialization-analysis.md]
---

# Workshop Profile KUG M3GIM 2026

## Profile

This instance is the two-day unit registered for 2026-09-16 and 17 within the KUG Summer School (M3GIM) at the Kunstuniversität Graz, taught in German at introductory level under the title *Promptotyping und Generative AI*. Its subject is LLM fundamentals together with Promptotyping, worked through four hands-on units on a single archival holding.

The cut described below is documented rather than planned. The operator's research vault holds a complete slide-text derivation under the delta model, meaning each slide is either a named reference to a slide of the Full Slide Deck with the cut stated or fully written text with speaker notes and sources, together with four fully worked hands-on units. Both are awaiting operator acceptance, which gates deck production. The vault stays the source of the teaching material and this profile documents the cut; hands-on prompts, task slides and worked solutions are deliberately not reproduced here. The register in `docs/data/workshops.json` holds the entry and currently carries no deck, script or cover.

The register audience string, participants without an LLM or programming background, has no source in the vault, which records audience, participant count and prior-knowledge level as open. Inference: the string is a plausible reading of an introductory summer-school unit and stays provisional until the host confirms it.

## The cut

Day 1 carries the fundamentals. The agent material is cut to how a model works and where it fails, and knowledge and context engineering is cut to the slides that ground the checking principle and the concept of a knowledge base. The deep knowledge-modelling material of the Full Slide Deck, meaning knowledge transformations, the four-axis model, the bootstrap sequence and the layer model, is dropped explicitly for this audience. Hands-on units A and B run on day 1.

Day 2 carries Promptotyping as the method block together with the remaining hands-on units. The Promptotyping section is newly written for this instance because the Full Slide Deck carries it as bare slides without speaker notes, and the vault marks that new text as fit for write-back into the full corpus. Governance and skills close the day as an outlook of two to three slides.

Execution environment. The instance never leaves the browser. Text tasks run through a chat interface and the vision task through a separate environment with a vision-capable model, a split the vault makes deliberately. No harness and no repository work are part of this instance, which is what keeps the prerequisites low.

## Module selection

Derived from the slide-text derivation and the hands-on chain held in the vault. The fine module cut in `knowledge/drafts/module-map.md` is itself a draft.

| Module | Role in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Emphasis. Day 1 opens here, cut to how a model works and where it fails. |
| 2 Prompt Engineering | Drawn on throughout the four hands-on units, each of which supplies its own prompt. The instance programmes no prompt-engineering block of its own. |
| 3 Knowledge and Context Engineering | Cut to the checking principle and to the concept of a knowledge base. The deep knowledge-modelling material is dropped for this audience. |
| 4 Agentic Engineering | Carried by the Promptotyping block on day 2, covering the definition against vibe coding, the four phases, the `knowledge/` folder with its analytical document types, and the Critical Expert with the checking questions. Participants operate no agent. |
| 5 Critical Perspectives and Governance | Outlook of two to three slides on day 2, together with skills. Whether the outlook stays at this level, or is dropped, is an open operator question. |

## Hands-on chain

Four exercises build on one holding. Each stage changes the technique while the domain stays constant, and the order runs from easy to visually impressive so that table and text precede image and map.

| Unit | Task | Product |
| --- | --- | --- |
| A | Cleaning a defective persons table | a cleaned person index |
| B | Structuring the text of a 1942 concert poster into a controlled tuple schema | the schema and the extraction prompt |
| C | An OCR difficulty ladder over three sources of rising difficulty, printed poster, multi-column newspaper clipping and handwritten object | the participants' own transcription |
| D | Normalising places and dates, having an authority identifier proposed under the checking rule, then looking coordinates up by hand | a CSV driving a minimal static map |

The poster text from unit B doubles as the reference transcription for the first step of the ladder in unit C, which turns the performance drop across the three sources from felt into measurable.

## Case material

The estate of the mezzo-soprano Ira Malaniuk in the archive of the Kunstuniversität Graz, signature UAKUG/NIM. The exercise material is drawn from the index tables of that holding and from poster digitisates, with the real defects of the source tables retained.

Rights state. The material is archive holdings of a partner institution and reaches participants through the operator's Drive. No source states a licence for it. The digitisates for the second and third step of the OCR ladder are requested from the project team and not yet available, so the ladder currently carries only its first step. The two prepared exercise files, the persons table and the place lookup, are named as deliverables and do not exist yet.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | to be linked from `docs/data/workshops.json`, register field currently null | in preparation, gated on operator acceptance of the slide-text derivation |
| Slide-text derivation and hands-on units | operator's research vault | complete, awaiting operator acceptance, not held in this repo |
| Lecture Notes (KUG Summer School 2026) | this folder | in preparation |
| PPTX export per taught state | this folder | in preparation |
| Map demo | external Teaching repo, `workshops/m3gim-map-demo` | working, maintained outside this repo |
| Cover | `docs/assets/covers/2026-09-16-kug-m3gim.png` | present |

## Open points

- Operator acceptance of the hands-on material and of the slide-text derivation, which gates deck production.
- Audience, participant count and prior-knowledge level.
- Scope per day and the split between input and hands-on work.
- The two missing digitisates for the OCR ladder and the two prepared exercise files.
- The model assignment checked against the model state at teaching time, including whether the vision task really needs a separate environment.
- Whether the governance and skills outlook stays at two to three slides.
- Write-back of the newly written Promptotyping section into the full corpus.

## Delivery notes

Filled after the workshop is taught.
