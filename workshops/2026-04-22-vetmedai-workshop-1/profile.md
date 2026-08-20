---
title: Workshop Profile VetMedAI Workshop 1
workshop:
  id: 2026-04-22-vetmedai-workshop-1
  dates: 2026-04-22
  title: Grundlagen Generativer KI und Prompt Engineering
  event: "VetMedAI, Veterinärmedizinische Universität Wien"
  audience: university staff in an institutional AI-competence programme
  language: de
  status: delivered
  slides: https://docs.google.com/presentation/d/1OCx8nGmlrpwM3X9ShR7z-NlkgyYMCO29Z26nPoXxsYM/edit
  script: null
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [workshop-script.txt, ../2026-11-30-vetmed-winter-school/profile.md, ../../knowledge/project.md, ../../knowledge/drafts/module-map.md, ../../knowledge/drafts/downloads-triage-documents.md]
---

# Workshop Profile VetMedAI Workshop 1

## Profile

This instance was taught on 2026-04-22 at the Veterinärmedizinische Universität Wien under the title *Grundlagen Generativer KI und Prompt Engineering*, framed on its title slide as AI-competence building for the university. The audience is university staff; the source states the institutional framing without naming a participant group more precisely, so the reading of staff comes from the registry entry of the follow-up format and from the triage in `knowledge/drafts/downloads-triage-documents.md`. Teaching language is German. The slide text is German throughout, while several speaker-note passages in the LLM-fundamentals and prompt-engineering blocks are written in English.

The unit is designated *Workshop 1* and belongs to a series called VetMedAI. That series name and the unit number come from the file name of the source export rather than from the slide text, and how many further units the series held is not documented in any artefact of this profile. The registered instance `2026-11-30-vetmed-winter-school` describes itself as the follow-up format to the VetMedAI programme at the same institution.

The authoritative content state of this instance is the slide-text export in `workshop-script.txt`. It is a delivered state, so it documents what was taught and is not maintained further.

## Module mapping

The mapping below is derived from the section sequence of `workshop-script.txt` against the five master modules. Two modules carry the weight of this instance. Module 1 holds the most complete German version of the LLM-fundamentals material anywhere in the corpus, and module 5 holds the EU AI Act block with its own hands-on, which is the largest governance asset the corpus currently has.

| Master module | Script sections drawn on | Depth and emphasis |
| --- | --- | --- |
| 1 Understanding Large Language Models | LLM Grundlagen with next token prediction and the autoregressive loop; Transformer-Architecture; Pre-Training against Post-Training; Embeddings with the dog, cat and stone example and the King minus Man plus Woman illustration; Die Gestalt eines Wikipedia-Artikels über Zebras; Tokenization with the cleaning, tokenizer and ID chain; the Shakespearean against modern English pair on prompt brittleness; Limitationen von LLMs | Taught in full and at the greatest depth of this instance. The block is the German counterpart to the architecture sections of the English master script, so it closes a language gap in the master rather than only serving this instance. The limitations list runs from arithmetic and spelling through sycophancy and non-determinism to the absence of internal verification, hallucination and data protection |
| 2 Prompt Engineering | Prompting ist seltsam with the emotional-stimuli studies and the reassessment of role prompting; the labelled prompt anatomy of Persona, Hauptaufgabe, Spezifikation, Anweisungen and Regeln on the workshop-budgeting example; Chain of Thought against Reasoning Model; the worked calculation with follow-up prompts into a spreadsheet and a slide deck | Taught in full with a demonstrated rather than a participant-run example. The anatomy is introduced on one prompt that is then extended through a chain of follow-up prompts, so the block shows iteration as the working mode |
| 3 Knowledge and Context Engineering | Model Context Window with the token arithmetic of an 8K window; Context Rot; Markdown with the three reasons it suits language models; Wissensdokumente with the properties of dual readability, compactness and portability | Conceptual depth without a separate exercise, since the exercise that applies it sits in module 5. The script positions the context-window and context-rot slides inside the fundamentals block, so the module boundary here is analytical rather than a break in the taught sequence |
| 4 Agentic Engineering | AI Agents with the four components of model core, tool access, memory and planning; the contrast of the chatbot flow against the agent flow; the distinction between AI agents and agentic AI | Thinnest module of this instance, taught as a short closing block that defines the terms without an exercise or a harness demonstration |
| 5 Critical Perspectives and Governance | Der EU AI Act in Kurzform with the AI-literacy obligation of Article 4, the prohibited practices of Article 5 and the provider and deployer definitions of Article 3(3); the research exemption of Article 2(6) and the threshold at which a research system becomes high-risk; Hands-On Wissensdokument zum EU AI Act with its worked model solution; the follow-up question on an outbreak-prediction system; the data-protection and verification entries of the limitations list | Taught as a substantial block with the only participant exercise of this instance. Participants distil the regulation into a knowledge document, then open a fresh conversation, load the document and query it, so the governance content and the knowledge-document method are taught in one movement |

The opening survey block, which asks which tools participants use privately and professionally, what their greatest challenge is and what they want to learn, carries the audience framing of this instance and belongs to no master module. The image-generation slide with the corporate-design prompt and the two shared conversations that contrast a free-tier answer against a reasoning model with context material sit alongside module 2 as demonstrations.

## Workshop-specific content

**EU AI Act material.** The block is written for a research institution that uses AI systems without building them, so it reduces the regulation to the two obligations that bind such an institution now and states explicitly that the bulk of the Act is product regulation aimed at providers. The veterinary and medical framing appears in the concrete triggers, meaning the Medical Devices and In Vitro Diagnostics regulations as the path by which a research tool crosses into a regulated application, and virology research as the worked example of that transition.

**Model solution as a dated artefact.** The worked knowledge document embedded in the script carries a version and a date of its own and synthesises the regulation as published in July 2024, covering the risk tiers, the requirements for high-risk systems, the obligations by actor type, general-purpose AI models, innovation support, governance, market surveillance and penalties, the application timeline and three reference annexes. It belongs in the corpus as a dated artefact of this instance. A maintained master module on governance would have to restate the material against the state of the regulation at its own time.

**Schedule.** The source states none. It is a slide-text export whose sequence is the taught order. Duration, breaks and the placement of the unit inside the VetMedAI series are not fixed in any artefact of this profile.

## Materials

| Artefact | Location | State |
| --- | --- | --- |
| Slide text (DE, with EN speaker notes) | `workshop-script.txt` in this folder | delivered state of 2026-04-22, the authoritative content record of this instance |
| Slide image exports (PNG) | operator's downloads folder | exports available, intake pending |
| Live deck | `https://docs.google.com/presentation/d/1OCx8nGmlrpwM3X9ShR7z-NlkgyYMCO29Z26nPoXxsYM/edit` | not named in the script source; found in the operator's vault and verified publicly readable on 2026-08-20 (`knowledge/drafts/google-artefacts.md`) |
| PPTX export per taught state | absent | not held in this repo |
| Cover | `docs/assets/covers/2026-04-22-vetmedai-workshop-1.png` | absent |
| Shared demonstration conversations | linked inside `workshop-script.txt` | external, provider-hosted, no guarantee of persistence |

The source names no Google Slides deck and no Google Doc script, so both register fields stay null until the operator supplies them.

## Delivery notes

Taught on 2026-04-22 at the Veterinärmedizinische Universität Wien in German, as the first documented unit of the VetMedAI series. Delivery ran on slides with two live demonstrations, the image-generation prompt in corporate design and the workshop-budgeting prompt with its follow-up chain, plus one participant hands-on on the EU AI Act.

Open points that the source does not settle.

- Participant count, duration and room are not documented.
- The series name VetMedAI and the unit number come from the file name of the export rather than from the slide text.
- Whether further units of the series were taught, and with which content, is undocumented here.
- The institutional AI terms of use of the university are linked in the script, so the instance was taught against a local policy that this repo does not hold.
