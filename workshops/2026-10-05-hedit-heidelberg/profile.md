---
title: "Workshop Profile HEDIT Heidelberg 2026"
workshop:
  id: 2026-10-05-hedit-heidelberg
  dates: 2026-10-05/06
  title: HEDIT KI-Workshop 2026
  event: "Forschungsstelle HEDIT, Universität Heidelberg"
  audience: researchers from the editions projects of the research centre
  language: de
  status: planned
status: in preparation
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/specialization-analysis.md, ../../knowledge/drafts/additional-past-instances.md]
---

# Workshop Profile HEDIT Heidelberg 2026

## Profile

This instance is the two-day unit registered for 2026-10-05 and 06 at the Forschungsstelle HEDIT (Heidelberger Editionen und Texterschließung) of the Universität Heidelberg, taught in German for researchers of the editions projects at the research centre. The format is two days of five to six hours each, structured as three hours in the morning and three in the afternoon. It is the second AI workshop for this research centre and follows a predecessor taught in November 2025 at an off-site venue near Heidelberg, whose programme is the template for this one.

Three changes against the predecessor are declared in the sources. The model landscape moves to the frontier state at teaching time and includes a locally runnable open-weight alternative. Agentic coding with Claude Code moves from a side remark into a central method block. Two operational demonstration objects enter, the teiCrafter tool and the agentic edition pipeline. A standing operator decision makes teiCrafter the convergence point of the edition tooling.

The register in `docs/data/workshops.json` holds the entry and carries no deck, script or cover. This profile documents the programme and the prerequisites. No slide texts exist for this instance in any source, so the profile carries no teaching text.

The register title *HEDIT KI-Workshop 2026* is an inference. The source heading reads *HEDIT KI-Workshop Heidelberg 2026* and no externally announced title is documented anywhere, so the string should be replaced once the host publishes the programme.

## Programme

Day 1 is theory and method in three blocks.

1. **Fundamentals of generative AI at the 2026 state.** How large language models work, the frontier landscape at teaching time, prompt engineering, and vibe coding against informed vibe coding as the framing pair.
2. **TEI with large language models.** TEI-XML modelling, TEI generation with models, context engineering and context rot, and the knowledge vault as a steering instrument.
3. **Agentic coding and edition workflows.** Claude Code in practice, Promptotyping as the structured middle path between vibe coding and classical software development, teiCrafter, and the agentic edition pipeline as a forkable template.

Day 2 is a two-part hands-on workshop on participants' own material. Part one builds the knowledge vault and a prototype from participant material supplied as plaintext, TEI, DOCX or images. Part two deepens that into a TEI-XML edition on the same material, adds the multi-repo vault pattern for longer projects, and closes with a plenary presentation of the prototypes.

Prerequisites. Participants need access to a frontier model, their own material in plaintext, XML, DOCX or image form, and a one-page description of that material. The host runs a prior survey of participant experience.

## Module selection

Derived from the programme blocks and the six documented learning objectives. It is a derivation and no confirmed cut exists. The fine module cut in `knowledge/drafts/module-map.md` is itself a draft.

| Module | Role in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Day 1 block 1, with how models work and the frontier landscape at teaching time, including locally runnable open-weight models. |
| 2 Prompt Engineering | Day 1 block 1 continued, with vibe coding against informed vibe coding as the framing pair. |
| 3 Knowledge and Context Engineering | Day 1 block 2, with context engineering, context rot and the knowledge vault as a steering instrument, applied to TEI-XML modelling and TEI generation. |
| 4 Agentic Engineering | Day 1 block 3 and the whole of day 2. Claude Code in practice, Promptotyping, teiCrafter as the convergence point of the edition tooling, the agentic edition pipeline as a forkable template, and the multi-repo vault pattern. This is the emphasis of the instance. |
| 5 Critical Perspectives and Governance | Not programmed. Neither the concept nor the learning objectives name a verification, governance or limits block. This is a documented absence in the sources rather than a documented decision, and it is the one gap of this instance against the complete material. |

## Case material

Decided on 2026-08-05. The worked example is the letter `o_szd.1079` from Stefan Zweig Digital, whose TEI header carries a CC-BY licence. The pipeline artefacts are held complete in the associated handwriting and optical character recognition pipeline repository, and the facsimiles are obtainable from the GAMS repository. Alongside it stand the synthetic teiCrafter fixtures.

Rights state. The rights-restricted material of the Zentralbibliothek Zürich is excluded from the shared participant folder and is shown on the projector at most. The Drive folder for this instance exists in the operator's own Drive and its URL is deliberately not reproduced in this public repository.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | to be derived from the Full Slide Deck, register field currently null | not created |
| Slide texts | none | none exist in any source |
| Lecture Notes (HEDIT Heidelberg 2026) | this folder | in preparation |
| Programme, learning objectives and prerequisites | operator's research vault | complete, the substance of this profile |
| Drive folder | operator's Drive | exists, URL deliberately not reproduced here |
| Demo material | worked Zweig example plus synthetic teiCrafter fixtures | decided 2026-08-05 |
| Cover | `docs/assets/covers/2026-10-05-hedit-heidelberg.png` | present |

## Open points

- The workshop concept and its slide set are still to be derived from the Full Slide Deck.
- EditionCrafter is to be removed from the concept and from the task list, which a standing operator decision requires and which the concept document has not yet carried through.
- The prior-experience survey is to be coordinated with the host.
- The demo material needs a defined state of the agentic edition pipeline and of teiCrafter by the teaching date.
- The contract draft is outstanding on the host side, which the sources record as a precondition before material is sent.
- Whether module 5 is added, and in what form, needs an operator answer. The absence is documented, its reason is undocumented.

## Delivery notes

Filled after the workshop is taught.
