---
title: Additional Instances for the Workshop Register
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
status: draft
related: [past-instances-registry.md, module-map.md, ../project.md, ../../docs/data/workshops.json]
---

# Additional Instances for the Workshop Register

Research draft on four instances of the teaching line that the register in `docs/data/workshops.json` does not carry. The sources are the operator's research vault, meaning the workshop documents under `Teaching/Workshops/`, the entries in `ACTIVE-WORK.md`, the completion log under `Vault Operations/` and the slide-text exports under `Teaching/HEDIT-Workshop 2025/`. Nothing here is applied. The register grows in a later coordinated sync pass, and no file under `docs/` was touched for this draft.

The entries follow the field schema of `docs/data/workshops.json` unchanged and the id scheme `YYYY-MM-DD-slug` established in `past-instances-registry.md`.

## Status finding, read this before pasting anything

The task that produced this draft assumed four past instances and asked for `status: "delivered"` throughout. The vault does not support that assumption. Only one of the four has been taught. The other three are contracted or agreed instances of October 2026, all of them still ahead of the current date of 2026-08-20, and every one of them carries open preparation items in `ACTIVE-WORK`.

| Instance | Date | Real status | Register value proposed here |
| --- | --- | --- | --- |
| HEDIT Workshop Lobbach | 2025-11-14/15 | taught, documented as complete | `delivered` |
| HEDIT KI-Workshop Heidelberg | 2026-10-05/06 | offer accepted, concept in draft | `planned` |
| Fachschaft Mittelalterstudien Heidelberg | 2026-10-08 | date fixed, deck copy created | `planned` |
| GDA Göttingen Pre-Conference Workshop | 2026-10-15 | offer sent, contract announced | `planned` |

The JSON blocks below therefore carry the status that matches the vault state. Setting `delivered` on the three October instances would put a false claim into a public register. If the operator wants them registered as forthcoming, the values are already correct as written.

A second consequence follows for sort order. Only the Lobbach instance sorts ahead of the two entries already prepared in `past-instances-registry.md`; the three October instances belong between the existing CLARIAH-AT and Uni for Life entries if the array stays chronological.

## 1. HEDIT Workshop Lobbach, taught 2025-11-14/15

The one genuinely delivered instance among the four, and the direct programme template for the 2026 Heidelberg repeat.

| Field | Value |
| --- | --- |
| Dates | 14. and 15. November 2025, Friday and Saturday |
| Event | Workshop of the Forschungsstelle HEDIT (Heidelberger Editionen und Texterschließung) |
| Host institution | Universität Heidelberg, Forschungsstelle HEDIT |
| Venue | Lobbach near Heidelberg, an off-site format rather than a university room |
| Format and duration | Two days on site. Day 1 runs 10:00 to 18:00 with three teaching blocks and a shared dinner, day 2 runs 10:00 to 16:00 as two hands-on units plus a closing plenary |
| Topic focus | Promptotyping as a structured middle path between vibe coding and conventional software development, applied to digital scholarly editions and TEI-XML |
| Audience | Researchers of the participating editions projects, named by discipline as German studies, history, papyrology, Romance studies and Indology. The source states a participant range of 25 to 30, which is a planning figure rather than an attendance record |
| Language | German |

### Module mapping

| Module | Coverage in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Taught in full as the opening of block 1, with transformer architecture, attention and tokenization named explicitly as the technical foundations |
| 2 Prompt Engineering | Taught in full across blocks 1 and 2, with zero-shot, few-shot and chain-of-thought as the named techniques and TEI-XML generation as the applied target |
| 3 Knowledge and Context Engineering | Present as a compact unit called *Context Engineering Grundlagen* at the end of block 2. Thinner than in every later instance of the line, which is consistent with the material state of late 2025 |
| 4 Agentic Engineering | Block 3 carries LLM integration into edition workflows, the Promptotyping method and a unit called *Agentic Coding*. Both hands-on units of day 2 apply it to participant material |
| 5 Critical Perspectives and Governance | Distributed rather than taught as a block. The summary states the critical-constructive framing as central, meaning hallucination, bias and absent domain expertise as systematically examined limits, with the hands-on exercises designed to show where human validation stays indispensable |

The edition domain layer of the teaching material, meaning the path from source through TEI to a research data package, carries the whole instance rather than appearing as one module.

### Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | `https://docs.google.com/presentation/d/1ZnOUip67gxaHt0h-Bk6p_4C7H7an486ULM_3lk5gTYc/edit` | linked from the vault workshop document, content not inspected for this draft |
| Script or lecture manuscript | none named | absent |
| Slide-text export | none held for this deck | absent from repo and vault |
| Cover | `docs/assets/covers/2025-11-14-hedit-lobbach.png` | absent |

One finding needs recording, because it affects any later intake. The vault folder `Teaching/HEDIT-Workshop 2025/` carries seven slide-text exports and its name suggests they are the material of this workshop. They are not. Six of them carry the title-slide line *Large Language Models in Digital Humanities Research. Summer School. Cologne. 8-11. September* and belong to a Cologne summer school, and the seventh is a Freiburg pre-workshop of 2025-09-24. The folder is a collection of reference decks gathered for the HEDIT preparation. An intake pass that treats it as the HEDIT source would register the wrong content.

### Teaching-line verdict

Belongs, as the precursor instance of the line. The five-module structure is fully recognisable, the method core is Promptotyping, and the vault names this workshop as the explicit programme template for the 2026 Heidelberg repeat. The qualification is chronological. The teaching material was assembled from July 2026 onward, so this instance is upstream of the material rather than a derivation from it, which is the same relation the register already accepts for the ÖAW and VetMedAI entries.

### Register entry

```json
{
  "id": "2025-11-14-hedit-lobbach",
  "dates": "2025-11-14/15",
  "title": "Digitale Edition und Künstliche Intelligenz",
  "event": "Forschungsstelle HEDIT, Universität Heidelberg (venue Lobbach)",
  "audience": "researchers from editions projects across German studies, history, papyrology, Romance studies and Indology",
  "focus": "Promptotyping for digital scholarly editions, from LLM fundamentals through prompt engineering to TEI-XML generation, with two hands-on units on participant material",
  "language": "de",
  "status": "delivered",
  "slides": "https://docs.google.com/presentation/d/1ZnOUip67gxaHt0h-Bk6p_4C7H7an486ULM_3lk5gTYc/edit",
  "script": null,
  "cover": null
}
```

## 2. HEDIT KI-Workshop Heidelberg, planned 2026-10-05/06

The second workshop for the same research centre, at the university this time rather than off site.

| Field | Value |
| --- | --- |
| Dates | Monday 5. and Tuesday 6. October 2026 |
| Event | Second AI workshop of the Forschungsstelle HEDIT |
| Host institution | Universität Heidelberg, Forschungsstelle HEDIT |
| Venue | Universität Heidelberg |
| Format and duration | Two days of 5 to 6 hours each, structured as 3 hours in the morning and 3 hours in the afternoon. Contracted volume is 12 hours including preparation |
| Topic focus | The Lobbach programme updated to the 2026 state, with three declared changes. The model landscape moves to current frontier models including an open-weight alternative, agentic coding with Claude Code moves from a side remark into day 1 block 3 as the central method, and two operational demonstration objects enter, the teiCrafter tool and the agentic edition pipeline |
| Audience | Researchers of the editions projects at the research centre, same constituency as 2025 |
| Language | German |
| Prerequisites | Frontier LLM access, own material in plaintext, XML, DOCX or image form, plus a one-page material description. The host runs a prior survey of participant experience |

### Module mapping

| Module | Coverage in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Day 1 block 1, with how LLMs work and the frontier landscape at workshop time, including locally runnable open models |
| 2 Prompt Engineering | Day 1 block 1 continued, with vibe coding against informed vibe coding as the framing pair |
| 3 Knowledge and Context Engineering | Day 1 block 2, with context engineering, context rot and the knowledge vault as a steering instrument, applied to TEI-XML modelling and TEI generation |
| 4 Agentic Engineering | Day 1 block 3 and the whole of day 2. Claude Code in practice, Promptotyping as the structured middle path, teiCrafter as the convergence point of the edition tooling, the agentic edition pipeline as a forkable template, and the multi-repo vault pattern for longer projects |
| 5 Critical Perspectives and Governance | Not programmed as a unit. The concept and the learning objectives name no verification, governance or limits block. This is a gap against the material rather than a documented decision |

### Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | none | to be derived from the Full Slide Deck, not yet created |
| Slide texts | none | not yet written |
| Drive folder | operator's Drive, URL held in the vault workshop document | exists, deliberately not reproduced in this public repo |
| Demo material | Stefan Zweig Digital worked example with a CC-BY TEI header, plus synthetic teiCrafter fixtures | decided 2026-08-05. Rights-restricted Zentralbibliothek Zürich material is excluded from the shared folder and shown on the projector at most |
| Cover | `docs/assets/covers/2026-10-05-hedit-heidelberg.png` | absent |

### Teaching-line verdict

Belongs, squarely. The vault states the deck as a derivation from the Full Slide Deck *Knowledge und Context Engineering für AI Agents*, and the teaching-material strand KCE-5 in the project overview names this instance as one of three trials for the Full Slide Deck, alongside the KUG summer school and Uni for Life. It is a domain specialisation of the line toward digital scholarly editions.

### Register entry

```json
{
  "id": "2026-10-05-hedit-heidelberg",
  "dates": "2026-10-05/06",
  "title": "HEDIT KI-Workshop 2026",
  "event": "Forschungsstelle HEDIT, Universität Heidelberg",
  "audience": "researchers from the editions projects of the research centre",
  "focus": "agentic engineering for digital scholarly editions, with knowledge and context engineering on day 1 and a two-part Promptotyping workshop on participant material on day 2",
  "language": "de",
  "status": "planned",
  "slides": null,
  "script": null,
  "cover": null
}
```

The `title` value is an inference. The vault heading reads *HEDIT KI-Workshop Heidelberg 2026* and no externally announced title is fixed anywhere, so the operator should replace this string once the host publishes the programme.

## 3. Fachschaft Mittelalterstudien Heidelberg, planned 2026-10-08

The instance whose announced title is the teaching line itself, in German.

| Field | Value |
| --- | --- |
| Date | Thursday 8. October 2026, fixed on 2026-08-05 |
| Event | Workshop commissioned by the student council of medieval studies |
| Host institution | Universität Heidelberg, Fachschaft Mittelalterstudien, funded from quality-assurance funds |
| Venue | Heidelberg, rooms of the student council |
| Format and duration | One day on site, practical work in Claude Code throughout. No hour grid is documented |
| Topic focus | LLM and AI agent fundamentals, then the build-up of structured project knowledge, then agentic work on a research-adjacent example |
| Audience | Students and early-career researchers in medieval studies |
| Language | German |
| Prerequisites | Participants obtain their own Claude Pro access, decided by the student council on 2026-08-05 |

### Module mapping

| Module | Coverage in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Opening block, LLM and AI agent fundamentals, stated as the conceptual entry the audience needs |
| 2 Prompt Engineering | Implied by the hands-on rather than named as a block. The source names no prompt-engineering unit |
| 3 Knowledge and Context Engineering | Named as the build-up of structured project knowledge, and present in the title of the instance |
| 4 Agentic Engineering | The centre of the day. Practical work in Claude Code across the full arc from source to edition |
| 5 Critical Perspectives and Governance | Present in the hands-on design rather than as a block. The recommended exercise format has participants check a prepared model transcription against facsimile and TEI ground truth, which teaches verification by doing it |

The hands-on, decided on 2026-08-05, is a small TEI and handwritten-text-recognition project on about ten charters sharing persons or organisations, producing recognition output, TEI markup, a person and organisation index and a small static edition. Two open decisions sit on it, the choice of charter set and the exercise format, both recorded in `ACTIVE-WORK`.

### Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | `https://docs.google.com/presentation/d/1JSwP61Uam4oMN1drzJcKsWLGMhK8whs0WzPq6_c53CQ/edit` | created 2026-08-05 as a copy of the Full Slide Deck, adaptation pending |
| Slide texts | none | to be written in Markdown, transferred to the deck by the operator |
| Drive folder and participant data folder | operator's Drive, URLs held in the vault workshop document | exist, deliberately not reproduced here. The charter material carries a pending licence and undocumented image rights, so the folder must not be published |
| Cover | `docs/assets/covers/2026-10-08-fachschaft-mittelalterstudien-heidelberg.png` | absent |

### Teaching-line verdict

Belongs, with the strongest claim of the three planned instances. The fixed title *Knowledge, Context und Agentic Engineering für die Forschung* is the German form of the line title, the deck is a copy of the Full Slide Deck, and the term apparatus comes from the glossary of the teaching line together with the Promptotyping paper definitions. The audience is the least technical of the four, which makes this instance the closest counterpart to the KUG profile that is already registered.

### Register entry

```json
{
  "id": "2026-10-08-fachschaft-mittelalterstudien-heidelberg",
  "dates": "2026-10-08",
  "title": "Knowledge, Context und Agentic Engineering für die Forschung",
  "event": "Fachschaft Mittelalterstudien, Universität Heidelberg",
  "audience": "students and early-career researchers in medieval studies",
  "focus": "one-day Claude Code workshop, from LLM and agent fundamentals to a medieval charter mini-edition, handwriting recognition through TEI to a small static edition",
  "language": "de",
  "status": "planned",
  "slides": "https://docs.google.com/presentation/d/1JSwP61Uam4oMN1drzJcKsWLGMhK8whs0WzPq6_c53CQ/edit",
  "script": null,
  "cover": null
}
```

The `slides` value points at a deck that currently holds the unadapted copy of the Full Slide Deck. Publishing that link before the adaptation would expose shared material under the name of this instance, so the field should stay null in the register until the deck is cut.

## 4. GDA Göttingen Pre-Conference Workshop, planned 2026-10-15

The only hybrid instance in the whole register, and the only one whose slide texts are already written out.

| Field | Value |
| --- | --- |
| Date | Thursday 15. October 2026, 09:00 to 12:30 |
| Event | Pre-conference workshop of the closing conference *Zwischenbilanz – 5 Jahre Göttinger Digitale Akademie. Nachhaltigkeit und Künstliche Intelligenz* on 15. and 16. October 2026 |
| Host institution | Göttinger Digitale Akademie at the Akademie der Wissenschaften zu Göttingen, coordination for digitisation and data curation |
| Venue | Göttingen, with a parallel Zoom channel |
| Format and duration | Half day, 3.5 hours, hybrid. An alternative slot on the afternoon of 16. October was held open |
| Topic focus | Generative AI for the preparation and migration of research data, and for the semi-automated maintenance of user interfaces and service endpoints |
| Audience | Staff of academy research projects, plus guests from the Göttingen state and university library |
| Language | German |

### Module mapping

| Module | Coverage in this instance |
| --- | --- |
| 1 Understanding Large Language Models | Compact opening. Frontier LLMs in 2026 and the jagged-capability slide, sharpened onto data work, meaning that counting, arithmetic and exact string operations are the unreliable cases |
| 2 Prompt Engineering | One dedicated slide on formulating a commission to an agent, with the four elements of goal, context, acceptance criteria and constraints, placed immediately before the hands-on as its checklist |
| 3 Knowledge and Context Engineering | Substantial. Why agents need context, context rot, what belongs in a `CLAUDE.md`, what a knowledge document and a knowledge vault are. The knowledge vault is the first working step of the hands-on |
| 4 Agentic Engineering | The centre of the session. What an AI agent is, the agentic loop and how it is shaped, a two-part Claude Code demonstration on data preparation and interface maintenance, and the hands-on on participant material |
| 5 Critical Perspectives and Governance | Present as its own slide on checking artefacts against the holdings, with the two checking levels of deterministic and domain-expert, and the critical expert in the loop addressed to the participants themselves. The sustainability framing of the conference carries the same argument, meaning that agents lower the cost of maintenance and migration work without removing the need for curation and domain review |

Three case studies carry the instance, a music-archival pipeline from spreadsheets into a linked-data model, a library pipeline from scans to TEI, and a static generator for a review journal. All three are existing DHCraft or partner projects rather than teaching constructs.

### Materials

| Artefact | Location | State |
| --- | --- | --- |
| Live deck | none | to be generated from the vault slide-text document, awaiting operator acceptance of the texts |
| Slide texts with speaker notes | vault document `Teaching/Workshops/2026-10-15 GDA Göttingen Workshop.md` | written and adversarially reviewed on 2026-07-18, all findings resolved, acceptance pending. This is the richest slide-text asset among the four instances and is a candidate for intake into the teaching material rather than only into a profile |
| Demo scripts | drafted inside the same document as a two-part demo script with a four-step fallback chain | demo dataset and change task undecided |
| Cover | `docs/assets/covers/2026-10-15-gda-goettingen.png` | absent |

### Teaching-line verdict

Belongs, as the infrastructure and data-migration specialisation of the line. The slide texts carry explicit provenance fields pointing at the Full Slide Deck for every fundamentals slide, which is the delta model the vault defines for derivations, so this instance is a documented specialization over the material in exactly the sense the project description describes. The one qualification worth naming is coverage. At 3.5 hours the instance takes a narrow cut, and its subject sits closer to research data engineering than to the full arc of the line.

### Register entry

```json
{
  "id": "2026-10-15-gda-goettingen",
  "dates": "2026-10-15",
  "title": "Generative KI für Datenaufbereitung, Datenmigration und die Pflege von Interfaces",
  "event": "Göttinger Digitale Akademie, Akademie der Wissenschaften zu Göttingen",
  "audience": "staff of academy research projects and library guests",
  "focus": "hybrid half-day on agent-supported research data preparation and migration and on semi-automated maintenance of interfaces and endpoints, with three project case studies and a hands-on on participant material",
  "language": "de",
  "status": "planned",
  "slides": null,
  "script": null,
  "cover": null
}
```

## Resolution of "hedigt"

Resolved with high confidence as **HEDIT**, the Forschungsstelle HEDIT (Heidelberger Editionen und Texterschließung) at Universität Heidelberg. The vault carries two workshops for this research centre, the delivered one of November 2025 and the planned one of October 2026, and no other event, institution or acronym in the vault matches the string.

One ambiguity remains inside the resolution and the operator has to settle it. The brief lists "one in Heidelberg" and "hedigt" as separate items, yet HEDIT is itself in Heidelberg, so three readings of the three named items are possible.

1. Heidelberg means the student-council workshop of 2026-10-08 and hedigt means one of the two HEDIT workshops. This is the reading the draft follows, because it makes the two items distinct.
2. Heidelberg means the HEDIT repeat of 2026-10-05 and hedigt means the delivered Lobbach workshop of 2025-11-14.
3. Both items point at HEDIT and the student-council workshop was not meant at all.

All four instances are documented above, so every reading is covered.

Candidates checked and ruled out.

- **HeFDI**, the Hessian research data infrastructure initiative. No occurrence anywhere in the vault, and Heidelberg is in Baden-Württemberg rather than Hesse.
- **HeDig** or a Heidelberg digital-humanities acronym of that shape. No occurrence in the vault.
- **HCDH/CAEDHET**, the Heidelberg centres that do appear in the vault. They occur only as a cooperation partner in the DIA-XAI follow-up application, never as a workshop host, and the string does not match.
- **heiBOOKS** and **hse-heidelberg**. Both occur, one as a publisher in a literature note and one as a link inside a slide export. Neither is an event.

## Adjacent instances found, outside the brief

Two further undocumented past instances surfaced while checking the HEDIT material, and both look like stronger register candidates than any of the planned October entries, because both are delivered and both have slide-text exports already in the vault.

- **Summer school on large language models in digital humanities research, Cologne, 8. to 11. September 2025.** Six slide-text exports lie in `Teaching/HEDIT-Workshop 2025/`, covering an introduction on "understanding" LLMs, LLM fundamentals, prompt engineering basics, advanced prompt engineering, AI engineering and applied generative AI, and an introduction to LLM-supported modelling for digital editions. Each names a Google Doc script or lecture manuscript on its title slide. This is an English-language, multi-day, five-module instance and the single largest unregistered asset found in this search.
- **Promptotyping pre-workshop, DHLab Freiburg, 24. September 2025, 10:00 to 11:30.** One slide-text export in the same folder, German, 90 minutes, method-focused.

Neither has a vault workshop document, so both would need a source pass of their own before entering the register.

## Inferences and unverified points

Marked here once, in the order the draft uses them.

1. **Status of the three October instances.** Read from `ACTIVE-WORK` field values and from open preparation items, not from an explicit statement that they are unheld. Verified only to the extent that all three dates lie after the current date.
2. **Participant figure for Lobbach.** The source states 25 to 30. Whether that is a cap, an expectation or an attendance record is not stated, so it stays out of the register entry.
3. **Lobbach venue reading.** The source names Lobbach near Heidelberg as the location and the Heidelberg research centre as organiser. That an off-site retreat format was chosen deliberately is an inference from the schedule, which includes a shared dinner and a Saturday session.
4. **Lobbach module mapping.** Derived from the block titles and the summary paragraph of the vault document. No slide-text export of that deck was available, so the mapping rests on the programme rather than on taught content. The deck itself was not opened.
5. **Lobbach audience formulation.** The disciplines are stated in the source. That these people come from the research centre's own editions projects is an inference.
6. **Title of the 2026 HEDIT instance.** Invented from the vault heading. No announced title exists.
7. **Module 5 gap in the 2026 HEDIT instance.** Absence of evidence in the concept document. Whether governance and verification were deliberately excluded or simply not yet written is undocumented.
8. **Module 2 in the student-council instance.** Not named in any source. Placed as implied by the hands-on design.
9. **Audience of the student-council instance.** The source names the commissioning body and the subject area. That participants are students and early-career researchers is an inference from the commissioning body.
10. **Weekday and slot claims.** Checked against the calendar for 2025-11-14, 2026-10-05, 2026-10-08 and 2026-10-15, and consistent with the source in all four cases.
11. **Drive folder URLs.** Held back deliberately. Two of the four instances have participant-data folders with unresolved rights, so the URLs are named as existing without being reproduced in a public repository. They are in the vault workshop documents.
12. **Cologne and Freiburg instances.** Read from title slides only. Dates, host and format come from the slide text, and no vault workshop document corroborates them.
13. **Cover files.** Verified. `docs/assets/covers/` holds one file, for the CLARIAH-AT instance. All four ids proposed here have no cover, so `cover` is null in every entry and no asset is expected.
