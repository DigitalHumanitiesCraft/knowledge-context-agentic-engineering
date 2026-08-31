---
marp: true
title: "Making Estate Materials Digitally Accessible"
description: "Final content deck for the KUG Summer School 2026"
workshop: 2026-09-16-kug-m3gim
created: 2026-08-20
updated: 2026-08-31
language: en
authors: [Christopher Pollin]
status: ready for rehearsal
paginate: true
related: [profile.md, lecture-notes.md, data/README.md, ../../slides/full-slide-deck.md]
---

<!-- _class: lead -->

# Making Estate Materials Digitally Accessible

## Research Data Workflows with Large Language Models and Promptotyping

KUG Summer School 2026<br>
16–17 September 2026

<!-- Visual: retain the approved workshop title composition from the native reference deck. -->

---

# One workflow across four sessions

1. Trace an estate object from source to research platform.
2. Locate suitable roles for large language models.
3. Transform Bayreuth 1953 programme pages into checked data.
4. Build and test a source-critical cast explorer.

**Workshop output**<br>
Source page → checked transcription → occurrence and participation data → validated browser application

---

# Guiding question for Wednesday

How does an archival object become a documented, structured, linked, preserved, and accessible digital research resource?

The answer involves a chain of representations, decisions, standards, and institutional responsibilities.

<!-- Visual: one source object on the left and one research interface on the right, connected by the workflow used on slide 6. -->

---

# Research data are produced in research processes

- A scan records selected visual properties of a source object.
- A transcription represents readable signs as text.
- Metadata describe and manage the resource.
- Structured entities and relations support comparison and computation.
- Interfaces select what users can inspect and query.

Each representation has its own production history and evidential scope.

*Reference · Geiger 2024; Schöch 2013*

---

# The source object remains part of the evidence chain

| Layer | Example | Research function |
| --- | --- | --- |
| Physical object | letter, programme booklet, notebook | material and historical evidence |
| Digital image | scan or photograph | visual representation |
| Description | catalogue record | discovery and management |
| Transcription | plain text or encoded text | reading and analysis |
| Structured data | persons, works, events, relations | comparison and computation |
| Interface | search, detail view, visualisation | access and interpretation |

---

# A digital research resource is a transformation chain

```text
source object
    ↓ digitisation
image and technical metadata
    ↓ description and transcription
catalogue record and encoded text
    ↓ modelling and reconciliation
entities, relations, identifiers
    ↓ repository ingest and publication
interfaces, APIs, exports
```

Provenance records how each layer was created and revised.

---

# Modelling selects relevant entities and relations

A model defines which distinctions the research process can preserve and query.

- Which object or event receives an identifier?
- How are persons connected to works, places, and dates?
- Which source supports each relation?
- How are uncertainty and disagreement represented?
- Which distinctions remain available in the interface?

The model is a scholarly claim expressed through data structures.

---

# Encoding makes selected distinctions machine-processable

```xml
<persName ref="https://d-nb.info/gnd/...">
  Name as written in the source
</persName>
```

The element records a semantic category. The attribute connects the text to an identified entity. The character data preserve the source-facing form.

Encoding documents interpretation in a formal structure.

---

# File formats support different operations

| Format | Typical strength |
| --- | --- |
| TIFF or JPEG | page image and visual inspection |
| Plain text | simple transcription and exchange |
| XML and TEI | structured scholarly text representation |
| CSV | flat tabular exchange |
| JSON | nested application data |
| RDF | linked statements with Web identifiers |

Format choice follows the intended operation, validation method, and preservation context.

---

# A catalogue record answers management and discovery questions

- What is the resource?
- Who created or contributed to it?
- When and where was it created?
- Which physical and digital objects belong together?
- What are the rights and access conditions?
- Which identifier resolves to the managed resource?

The record describes the object. It does not reproduce every statement contained in the object.

---

# XML represents hierarchy explicitly

```xml
<letter>
  <metadata>...</metadata>
  <text>
    <opener>...</opener>
    <body>...</body>
    <closer>...</closer>
  </text>
</letter>
```

Well-formed XML has one root element, properly nested elements, quoted attribute values, and escaped reserved characters.

---

# XML supports validation and transformation

- A schema defines allowed structures and values.
- Validation detects structural deviations.
- Namespaces distinguish vocabularies.
- XPath selects nodes in a document.
- XSLT transforms XML into other representations.

These operations support controlled ingest, publication, and migration.

---

# Metadata have several functions

| Function | Examples |
| --- | --- |
| Descriptive | title, creator, date, subject |
| Administrative | rights, acquisition, responsibility |
| Technical | file format, dimensions, checksums |
| Structural | page order, file-to-object relations |
| Preservation | events, agents, fixity, migrations |

*Reference · NISO, Understanding Metadata, 2017*

---

# Standards coordinate work across systems

- METS packages structural and administrative information.
- MODS describes bibliographic and archival resources.
- TEI represents scholarly text.
- IIIF delivers images and presentation structures.
- OAI-PMH exposes metadata records for harvesting.
- RDF expresses linked statements.

A project combines standards according to its objects and services.

---

# Stefan Zweig Digital connects the layers

The workflow brings together:

- digitised estate objects;
- catalogue and authority data;
- encoded texts and scholarly description;
- repository storage and dissemination;
- persistent identifiers and interfaces.

The case makes the source-to-platform chain observable within an established research infrastructure.

<!-- Visual: reuse the Stefan Zweig Digital workflow diagram from the native reference deck. -->

---

# Repository infrastructure preserves managed relations

A repository stores files together with metadata, versions, identifiers, access rules, and dissemination formats.

The GAMS infrastructure used in the Stefan Zweig Digital context supports repository ingest, semantic relations, interfaces, and standardised access routes.

*Reference · GAMS documentation and Stefan Zweig Digital project documentation*

---

# Digitisation creates a managed digital object

The workflow records:

- the relation to the physical source;
- image order and completeness;
- technical capture information;
- file integrity;
- rights and access conditions;
- responsibility for creation and review.

The scan becomes reliable research material through documentation and quality control.

---

# Repository ingest uses an explicit package

```text
object identifier
├── image files
├── descriptive metadata
├── structural metadata
├── rights information
└── encoded text or linked data
```

Validation occurs before the repository accepts the package.

---

# METS records the digital object structure

METS can connect:

- descriptive metadata sections;
- administrative and technical metadata;
- file groups;
- logical and physical structures;
- links between structure and files.

It is especially useful when one intellectual object consists of several ordered files.

*Reference · Library of Congress METS documentation*

---

# MODS provides rich descriptive metadata

MODS supports structured descriptions of titles, names, genres, origins, subjects, identifiers, and related resources.

The vocabulary is more detailed than a minimal discovery record while remaining compatible with library and repository workflows.

*Reference · Library of Congress MODS documentation*

---

# IIIF provides interoperable image access

- The Image API supports region and size requests.
- The Presentation API describes ordered canvases and annotations.
- A manifest connects images, labels, metadata, and structures.

The same managed images can be used by several compatible viewers.

*Reference · IIIF Presentation API 3.0*

---

# OAI-PMH supports metadata harvesting

OAI-PMH exposes metadata records through a small set of standard requests.

Repositories can offer records in one or more metadata formats. Aggregators harvest those records and build cross-collection discovery services.

The protocol moves metadata. Full research objects require separate access routes.

---

# EDM supports aggregation across collections

The Europeana Data Model distinguishes the cultural heritage object, its digital representations, and the aggregation supplied by a provider.

This separation helps preserve provenance when records and digital representations from many institutions appear in one discovery environment.

*Reference · Europeana Data Model documentation*

---

# Persistent identifiers stabilise references

A persistent identifier should:

- identify a managed resource;
- resolve through a maintained service;
- remain stable when storage locations change;
- support citation and data linking;
- have an accountable governance process.

Persistence is an institutional commitment supported by technical infrastructure.

---

# TEI represents scholarly text and source features

- document structure;
- persons, places, organisations, and works;
- additions, deletions, unclear text, and editorial interventions;
- manuscript and source description;
- links, notes, and critical apparatus.

Projects select a documented subset and validate encoded texts against it.

*Reference · TEI P5 Guidelines*

---

# Controlled vocabularies support consistent values

A controlled vocabulary defines permitted terms and their meaning within a domain.

It can reduce spelling variation, support multilingual labels, and connect local categories to wider systems. Governance remains essential because communities or institutions select, define, revise, and deprecate terms.

---

# SKOS represents concepts on the Web

SKOS supports:

- preferred and alternative labels;
- broader and narrower concepts;
- related concepts;
- definitions and notes;
- mappings between vocabularies.

Concept identifiers allow applications to use stable references while displaying suitable labels.

*Reference · W3C SKOS Reference*

---

# Traceability must survive publication

```text
interface statement
→ structured relation
→ transcription or metadata record
→ source page
```

The route may use links, identifiers, evidence quotations, or side-by-side views. It keeps the basis of a research statement inspectable.

---

# Wednesday synthesis

For any digital research resource, ask:

- Which source object is represented?
- Which transformations created the current data?
- Which model and standards structure it?
- Which identifiers and rights govern access?
- Which validation supports the published statement?

These questions prepare the model-assisted workflow used on Thursday.

---

<!-- _class: lead -->

# Large Language Models in Research Data Workflows

Thursday · 11:30–13:00

From task definition and AI readiness to evidence-based validation

---

# AI readiness is a workflow property

A model-assisted task requires:

- permitted and legible source material;
- stable source and page identifiers;
- a defined target structure;
- representative examples and difficult cases;
- validation rules and reference material;
- a documented hand-off to the next operation.

A powerful model cannot supply missing rights, provenance, or research criteria.

---

# Models support bounded research-data operations

- page transcription;
- entity and relation extraction;
- date and label normalisation;
- format conversion;
- candidate matching;
- code generation from documented requirements.

Each operation needs an input contract, an output contract, and a validation method.

---

# Multimodal models connect images and language

A multimodal model can process a page image together with written instructions.

This supports layout-aware transcription and document analysis. Results can still omit text, reorder columns, normalise source forms, or infer plausible content. Page-level comparison remains necessary.

<!-- Visual: one programme page with callouts for columns, names, date, and roles. -->

---

# A language model predicts token sequences

The model receives a context and repeatedly estimates a probability distribution for the next token.

Training captures statistical patterns across large corpora. The generated response can reproduce useful structures across text, data, and code. Fluency provides no independent guarantee of factual accuracy.

*Reference · Vaswani et al. 2017; Bender et al. 2021*

---

# Attention relates tokens within the context

Transformer architectures calculate contextual relations between token representations.

Attention helps the model use distant parts of the prompt, connect instructions with examples, and generate structured continuations. It does not create a stable database of verified facts inside the response.

<!-- Visual: retain the transformer or attention diagram from the native reference deck. -->

---

# Tokens are model input units

Tokens may represent words, word parts, punctuation, or other encoded units.

Tokenisation affects:

- the size of the usable context;
- the treatment of names and rare forms;
- cost and processing limits;
- alignment between page text and generated output.

Historical spelling and proper names often require close validation.

---

# Embeddings represent contextual similarity

Embeddings are numerical vectors learned by the model. Similar patterns occupy related regions in a high-dimensional space.

They support semantic comparison and retrieval. Similarity remains a model-derived relation. A high score does not establish identity, authority control, or historical equivalence.

---

# The context window contains the working evidence

The model can use the material available in its active context and connected tools.

Relevant context may include instructions, page images, transcriptions, schemas, examples, lookup data, and earlier outputs. Larger contexts still require selection and structure because competing or distant information can weaken task performance.

---

# Context quality determines task quality

Useful context is:

- relevant to the current operation;
- explicit about source identity and scope;
- structured around the target schema;
- representative of routine and difficult cases;
- small enough to inspect and revise.

Context engineering maintains these conditions across several operations.

---

# A prompt defines one operation

1. Source and page identifiers
2. Operation to perform
3. Allowed evidence
4. Output schema
5. Rules for missing and uncertain values
6. Required validation output

Examples clarify boundaries when the schema alone leaves room for interpretation.

---

# Context engineering maintains the wider contract

- the research question;
- source and rights information;
- the data model;
- controlled values and examples;
- validation rules;
- previous decisions and corrected outputs.

This material keeps transcription, extraction, and application development coherent.

---

# Recurrent model failures affect research claims

- omitted or reordered text;
- invented readings;
- silent spelling normalisation;
- inconsistent entity boundaries;
- unsupported identifiers and relations;
- valid-looking output with missing fields;
- confident explanations for incorrect decisions.

Output is a candidate transformation until it passes source-based checks.

---

# Validation combines human and mechanical checks

| Check | Method |
| --- | --- |
| Page completeness | compare image regions with transcription |
| Names and values | character-level source comparison |
| JSON structure | schema or parser validation |
| Relation meaning | domain review against the data model |
| Cross-source claims | assertion-level comparison by evidence type |
| Application behaviour | acceptance tests with difficult records |

---

# The source-to-data pipeline has explicit gates

```text
page image
→ candidate transcription
→ checked transcription
→ candidate JSON
→ page and cross-source validation
→ human-validated JSON
```

Only the final dataset enters the application exercise. Earlier versions remain available for comparison and correction.

---

# The Bayreuth packet tests the method

- stable programme structures;
- existing record errors;
- one participation with two stage roles;
- daily and season-level cast statements;
- biographies with a different documentary scope.

The exercise uses these cases to test transcription, modelling, provenance, and validation.

---

<!-- _class: lead -->

# Sources into Data with Gemini

Thursday · 15:00–16:30

Bayreuth Festival 1953 programme booklets in M³GIM

---

# Research question

## How do daily programmes, season lists, and biographies represent who was announced to do what at the Bayreuth Festival in 1953?

The question is documentary. It asks what each source represents and how those statements can be compared.

---

# The source packet contains seven objects

| Sources | Material | Exercise role |
| --- | --- | --- |
| 3, 7, 8, 9, 10 | daily programme booklets | dated work and cast structures |
| 11 | daily programme and *Wer singt was?* | daily and season-level comparison |
| 12 | schedules, cast matrices, staff lists, biographies | season-level and biographical evidence |

The complete packet contains 40 scan pages. Participants work with a controlled page subset.

---

# Evidence type determines claim scope

| Evidence type | Supported statement |
| --- | --- |
| `daily_program` | an assignment announced for one dated programme |
| `season_list` | an assignment documented for the festival season |
| `biography` | a statement made in one biographical text |
| `object_metadata` | a statement contained in the M³GIM object record |

Cross-source comparison preserves these labels and page references.

---

# Participant source allocation

- **Demonstration** · Source 3 and known record errors
- **Group A** · Sources 7 and 8 with regular cast structures
- **Group B** · Source 10 with two roles in one participation
- **Group C** · Source 11 with daily and season-level statements
- **Comparison** · Selected pages from source 12

Source 9 and further pages from source 12 extend the exercise after the core task.

---

# Prompt 1 transcribes one identified page

```text
SOURCE_ID: [supplied identifier]
PAGE_ID: [supplied page or folio]
DOCUMENT_TYPE: [daily_program | season_list | biography]

Preserve spelling, punctuation, line breaks, and column order.
Mark unreadable text as [unclear].
Do not translate, normalise, summarise, or supplement the page.
Return only the identifiers and transcription.
```

[Open the complete workshop prompts](https://drive.google.com/file/d/1HGzaJ4XtU2APn40_2YQH6Kj8IaGTJ8_Y/view)

---

# Prompt 2 extracts occurrences and participations

```text
occurrence
├── date, work, place, documentary status
└── participations[]
    ├── person as written and normalised label
    ├── functions[]
    ├── stage_roles[]
    ├── source_id, page_id, evidence_type
    └── quotation, certainty, unresolved issues
```

One participation may contain several stage roles. Functions and performed characters remain separate fields.

---

# Prompt 3 validates assertions across sources

The comparison table records:

- assertion;
- source and page;
- evidence type;
- extracted value;
- spelling or substantive difference;
- decision and reason.

Conflicting statements remain source-specific. Corrections preserve provenance and add validation notes.

**Group output**<br>
Checked transcription + source-specific JSON + validation table

---

<!-- _class: lead -->

# Promptotyping Research Data

Thursday · 17:00–18:30

Build a source-critical Bayreuth 1953 Cast Explorer

---

# The application follows the question

The selected performance occurrences share the festival location. A map would add little analytical value to the core dataset.

The application supports:

- comparison of dated programmes;
- filtering by person, function, and stage role;
- comparison by evidence type;
- inspection of page evidence and validation notes.

---

# Promptotyping develops an executable research claim

```text
research question
→ documented requirements
→ structured and validated data
→ executable application
→ expert inspection
→ revised requirements and data
```

The repository preserves the context required to understand and revise the artefact.

*Reference · Promptotyping method documentation, 2026*

---

# Users need observable research operations

**Source-critical researcher**<br>
Compare related assignments without losing documentary scope.

**Music historian**<br>
Inspect who is connected to a dated work through which function or character.

**Data curator**<br>
Trace a displayed value to its source page, quotation, certainty, and validation state.

---

# Four knowledge files define the promptotype

| File | Contract |
| --- | --- |
| `project.md` | research question, scope, users, exclusions |
| `data-model.md` | occurrences, participations, evidence types, uncertainty |
| `design.md` | views, labels, filters, evidence interaction |
| `validation.md` | acceptance cases and observed results |

The build prompt refers to these maintained files and the validated JSON.

---

# The data contract preserves difficult cases

- Each assignment has a source and page reference.
- Functions and stage roles use separate arrays.
- One participation can display two characters.
- Missing values remain empty and visible.
- Conflicting source statements remain separate records.

The interface must preserve these distinctions.

---

# Three views answer the research question

1. **Performance list**<br>
   Date, work, documentary status, and evidence type

2. **Cast view**<br>
   Filterable persons with functions and stage roles

3. **Evidence detail**<br>
   Source, page, quotation, certainty, and validation note

Every displayed assignment links to the evidence detail.

---

# The build prompt defines observable behaviour

```text
Build a static Bayreuth 1953 Cast Explorer.
Use the validated JSON and the four knowledge files.
Keep conflicting source statements side by side.
Display multiple roles within one participation.
Expose evidence and uncertainty for every assignment.
Report schema mismatches before implementation.
```

The application runs locally with HTML, CSS, and JavaScript.

---

# Acceptance tests use the difficult cases

| Test | Expected observation |
| --- | --- |
| Multiple-role case | both roles appear within one participation |
| Evidence filter | all evidence types remain distinct |
| Evidence link | every assignment opens the correct page detail |
| Missing value | absence remains visible and causes no invented label |
| Conflict | statements appear side by side with validation notes |
| Narrow screen | content remains readable and operable |

Record observed results in `validation.md`.

---

# Retain the complete workshop output

1. Checked page transcription
2. Source-specific occurrence and participation JSON
3. Cross-source validation table
4. Human-validated application dataset
5. Bayreuth 1953 Cast Explorer
6. Recorded acceptance-test results

The retained identifiers, quotations, evidence types, and validation notes connect the application to the supplied source pages.
