---
title: "Making Estate Materials Digitally Accessible"
workshop: 2026-09-16-kug-m3gim
created: 2026-08-20
updated: 2026-08-24
language: en
authors: [Christopher Pollin]
status: ready for review
source: "https://docs.google.com/document/d/1DU6UbE4xURFZ3fkPn7MD2loZ2naPysFYX1ypeI0D_Kg/edit"
related: [profile.md, slide-deck.md, ../../script/full-lecture-notes-en.md]
---

# Making Estate Materials Digitally Accessible

## *Research Data Workflows with Large Language Models and Promptotyping*

Course reader for the KUG Summer School 2026

Christopher Pollin · Digital Humanities Craft OG

## **Purpose and structure**

This workshop follows one coherent research data workflow across four sessions. The Wednesday session uses Stefan Zweig Digital to show how a digitised estate object becomes a documented, structured, linked, preserved, and accessible research resource. The Thursday sessions transfer this workflow to material from the M³GIM project. Participants first examine what large language models can contribute to research data work, then create and validate text and structured data from digitised objects, and finally develop a small digital research application through Promptotyping.

The two projects have distinct functions. Stefan Zweig Digital is the explanatory case: it provides an existing infrastructure and a traceable route from an archival object to a public platform. M³GIM supplies the working material: scans or images, existing cataloguing data, and a reduced research question suitable for the hands-on exercises. This separation makes it possible to understand a mature workflow before testing selected transformations on a manageable dataset.

## **Learning outcomes**

* Explain the main transformations between a digitised estate object and its publication in a research data repository or platform.
* Distinguish digitisation, transcription, metadata creation, text encoding, data modelling, authority control, repository ingest, and presentation.
* Describe how persons, places, works, objects, and events can be represented as entities with attributes, identifiers, and relations.
* Assess whether source material and existing data are suitable for a defined model-assisted task.
* Use a multimodal language model to transcribe a scan and extract information into a predefined schema.
* Validate model outputs against the source image and existing project data.
* Translate a reduced research question and a structured dataset into requirements for a small digital research application.

# 1\. Making Estate Materials Digitally Accessible

## **1.1 What are research data?**

Research data are analogue or digital representations that are created, collected, selected, transformed, or used as evidence in scholarly work. They support the formulation, examination, and communication of research claims. In the humanities, research data can include digitised images, transcriptions, descriptive metadata, encoded texts, authority identifiers, tables, graphs, software, prompts, and documented analytical outputs. Their status depends on their function in a specific research process rather than on a single file format. [^1]

The term therefore covers more than a final spreadsheet or database. A source image can be research data when it is used as evidence. A transcription becomes a separate representation with its own production history. A person index or a set of place identifiers records interpretive and editorial work. Code, schemas, and prompts can also be research data or research artefacts when they are required to understand or reproduce a transformation.

Research data in the humanities are selective representations. A project decides which features of an object must be made explicit, how uncertainty is recorded, and which distinctions are relevant to its questions. These choices should be documented in schemas, guidelines, provenance statements, or workflow descriptions. Drucker’s distinction between data and capta is useful here: the digital representation is made through acts of selection and construction rather than simply found in the source (Drucker 2011).

## **1.2 The source object and its digital representations**

An estate object has a material history before it enters a digital system. A letter, manuscript leaf, photograph, or notebook may have an archival identifier, a physical order, writing materials, damage, additions, and relations to other objects. Digitisation creates one or more digital representations of this object. It does not replace the object and it does not automatically provide a scholarly description.

The distinction between object, image, text, and data prevents several common confusions:

* The archival object is the physical or born-digital item held by a collection.
* The digital image is a visual representation produced under specific technical and legal conditions.
* The transcription is a textual representation whose accuracy, normalisation, and treatment of uncertain readings must be specified.
* The metadata record describes the object and its representations.
* The structured research data select entities, properties, and relations for particular forms of analysis.

Every representation introduces a new layer that needs identifiers, provenance, and quality control. A stable object identifier links the layers without treating them as identical.

## **1.3 Metadata: describing and managing resources**

Metadata are structured statements about resources. They support discovery, identification, administration, preservation, and use. [^2] A useful distinction separates five functions:

* Descriptive metadata identify intellectual content, such as title, creator, date, language, people, places, and subjects.
* Administrative metadata record rights, responsibilities, access conditions, and management information.
* Technical metadata describe files, formats, image dimensions, checksums, or digitisation settings.
* Structural metadata record the order and composition of compound objects, for example pages belonging to a manuscript.
* Preservation metadata document provenance, events, validation, and changes required for long-term stewardship.

A metadata schema names fields and specifies their meaning, repeatability, data type, and constraints. A data value such as “Vienna” is useful only when the system also knows whether it denotes a place of creation, a place mentioned in a letter, a repository location, or an address. Documentation and controlled vocabularies make these distinctions explicit.

## **1.4 Data formats and representations**

The same information can be serialised in several formats. CSV is effective for a simple rectangular table. JSON represents nested objects and is widely used in web applications and interfaces. XML supports explicitly marked hierarchical structures and validation against schemas. RDF represents statements as a graph of identified resources and relations. A format should be chosen according to the structure of the material, the intended transformations, interoperability requirements, and long-term maintenance.

The format does not by itself guarantee quality or semantics. A valid XML file can contain poorly defined categories; a clean table can merge distinct entities in one column. The decisive layer is the data model: the documented account of what kinds of things exist in the dataset, which properties describe them, and which relations connect them.

## **1.5 TEI-XML and scholarly text representation**

The Text Encoding Initiative provides modular guidelines and an XML vocabulary for representing textual structure and features relevant to scholarly work. [^3] A TEI document normally combines a TEI header, which records description and provenance, with an encoded text. Depending on the project, the text can mark divisions, paragraphs, names, dates, deletions, additions, uncertain readings, or links to facsimile regions.

TEI is important in this workshop because it makes the transition from transcription to structured representation visible. A transcription preserves a sequence of characters. TEI encoding can additionally state that a string denotes a person, that a date is uncertain, or that a passage was added later. If participants have already encountered TEI in Selina Galka’s session, the Stefan Zweig Digital workflow shows where this encoding sits within a larger repository and publication process.

TEI remains a project-specific model within a shared framework. Projects select modules, elements, attributes, and controlled values and document this selection in a schema and encoding guidelines. Interoperability therefore depends on explicit customisation and mapping, not on the TEI label alone.

## **1.6 Modelling entities and relations**

A data model translates a research perspective into explicit entities, properties, and relations. For estate materials, common entities include persons, organisations, places, works, events, archival objects, collections, and digital files. Each entity should have an identifier. Properties describe the entity; relations connect it to other entities.

A simplified letter model might contain:

* Letter as an archival object with an identifier, holding institution, shelf mark, date, and language.
* Person entities for sender, recipient, and people mentioned in the text.
* Place entities for the place of writing, destination, and places mentioned.
* Relations such as sent by, addressed to, written at, mentions, belongs to, or has digital representation.
* Provenance fields that record the source of each statement, its creator, date of creation, and level of certainty.

This model enables questions that cannot be answered reliably from images alone. It also defines what the application can display. A map requires identified places and a documented relation between each place and the object. A correspondence network requires consistent person identifiers and relation types. A timeline requires normalised dates and an account of uncertainty.

## **1.7 Authority data, the Semantic Web, and Linked Open Data**

Authority data provide controlled records and persistent identifiers for entities such as persons, places, organisations, and works. [^4] Linking a local person record to the Integrated Authority File (GND), an ORCID, or another maintained identifier helps distinguish people with similar names and supports connections to external information.

The Semantic Web provides standards for expressing data in forms that can be processed and linked across systems. RDF represents statements as subject–predicate–object relations identified by Internationalized Resource Identifiers. Linked Open Data applies Web identifiers and links to openly available datasets. [^5] In a simple statement, a local letter identifier can be the subject, “has sender” the predicate, and a GND URI for Stefan Zweig the object.

Links require evaluation. An authority record may describe a person at a different level of detail, contain an outdated assertion, or lack the entity required by the project. The local dataset should retain the project’s evidence and provenance while recording the external alignment. Linking extends the context of a record; it does not transfer responsibility for the local description.

## **1.8 Repositories, interfaces, and research platforms**

A research data repository manages digital objects together with the information required to preserve, identify, retrieve, and disseminate them. The Open Archival Information System reference model distinguishes information submitted to an archive, managed within it, and disseminated to users. [^6] It is a conceptual model rather than a particular software product.

In the Stefan Zweig Digital workflow, GAMS provides repository functions and exposes data to the research platform. Several standards and components can participate in such an infrastructure:

* METS can record the structure of a complex digital object and connect files with metadata.
* MODS can provide rich bibliographic and descriptive metadata.
* TEI can represent the text, editorial description, named entities, and links to facsimiles.
* IIIF can deliver images and structured presentation information for digital objects.
* OAI-PMH can expose metadata records for harvesting by other services.
* The Europeana Data Model can support aggregation across heterogeneous cultural heritage collections.
* Persistent identifiers provide stable references for objects, files, people, and published datasets.

These components have different responsibilities. The repository preserves and serves managed digital objects. Interfaces and APIs expose selected representations. The research platform combines these representations into views for reading, searching, browsing, mapping, or analysis. Aggregators such as Kulturpool can harvest and present selected metadata beyond the original platform.

## **1.9 The Stefan Zweig Digital workflow**

The complete workflow can be read as a sequence of accountable transformations:

* An estate object is selected, identified, and digitised.
* Files receive technical and administrative metadata, including rights and provenance.
* The object receives descriptive metadata and stable identifiers.
* Textual content is transcribed and, where appropriate, encoded in TEI.
* Persons, places, works, dates, and other entities are modelled and linked to authority data.
* Images, metadata, texts, identifiers, and relations are packaged and ingested into GAMS.
* Repository interfaces provide the data required by Stefan Zweig Digital.
* The platform presents the object through coordinated views and makes selected data searchable or reusable.
* Metadata can be harvested or mapped for external discovery services such as Kulturpool.

At each step, the workshop asks four practical questions: What is the input? What transformation is performed? What new representation is produced? How can a researcher check it? These questions also structure the Thursday exercises.

# 2\. Large Language Models in Research Data Workflows

## **2.1 AI readiness as a workflow property**

A model can contribute only when the task, input, expected output, and validation procedure are defined. In this reader, AI readiness means that the material is sufficiently legible, structured, documented, licensed, and representative for a specific model-assisted task. [^7] It is a property of the whole workflow, not a label attached to a dataset in isolation.

Before using a model, check:

* Is the intended task transcription, classification, extraction, reconciliation, summarisation, or application development?
* Are the relevant images and existing data available in a usable quality and format?
* Is there a target schema or an explicit output contract?
* Are examples available that show difficult cases and accepted decisions?
* Can the output be checked against the source and, where possible, a reference result?
* Do rights, confidentiality, and the chosen service permit processing of the material?
* Can prompts, model settings, corrections, and resulting data be documented?

The hands-on sequence uses scans of M³GIM objects that have already been catalogued whenever these images are available and cleared for teaching. This keeps the source image, existing description, model output, and workshop corrections aligned at object level.

## **2.2 How large language models work**

A large language model is a neural model trained to predict and generate sequences of tokens. [^8] Tokens are numerical units derived from text or other inputs. Transformer architectures use attention mechanisms to model relations between tokens in a context. During generation, the model repeatedly estimates a probability distribution for the next token.

This mechanism explains both the usefulness and the limits of the output. A model can transform patterns across text, images, code, and structured formats without a task-specific program for every case. Its response remains a probabilistic construction. Fluency is therefore not evidence of factual accuracy, complete extraction, or faithful transcription.

For research data workflows, three configurations are especially relevant:

* A general-purpose language model processes instructions and text.
* A multimodal model processes text together with images and can support transcription or visual document analysis.
* A tool-using or agentic system combines a model with files, code execution, search, schemas, and validation steps.

## **2.3 Suitable tasks and recurrent risks**

Useful tasks include proposing a transcription, normalising a date into a specified format, extracting named entities into a schema, generating candidate authority matches, converting data between representations, explaining validation errors, and creating an initial application from a structured specification.

Recurrent risks include omitted passages, invented readings, silent normalisation, inconsistent entity boundaries, unsupported relations, unstable output formats, and plausible but incorrect identifiers. The response must therefore be treated as a candidate transformation. The source image, schema, provenance, and validation rules remain part of the evidence chain.

A practical validation protocol asks participants to mark every uncertain reading, compare extracted values with the image, distinguish explicit statements from inference, preserve the original transcription, and record corrections separately. Structured output should be validated mechanically where possible and reviewed by a domain expert.

# 3\. Sources into Data: OCR and Information Extraction with Gemini

## **3.1 Materials and research question**

The exercise uses a small set of M³GIM objects. Ideally, each object is represented by a scan or image and by the descriptive data already created in the project. Nicole K. Strohmann’s Mobility Studies keynote may provide a research question or a clearly delimited aspect that can be simplified for this dataset. The reduced question should remain recognisably connected to the keynote while being answerable within the available material.

A suitable reduced question might ask which persons move between which places, how a performance or work is connected to a journey, or which routes and temporal sequences are visible in the selected objects. The exact schema follows from the final question and the evidence present in the scans.

## **3.2 Phase A: transcription**

Participants upload or provide the permitted image to Gemini and request a diplomatic transcription. The prompt specifies language, line breaks, unclear passages, deletions or additions where relevant, and the required treatment of uncertainty. The first output is preserved before correction.

Validation proceeds directly against the image:

* Check completeness at page, line, and passage level.
* Compare names, dates, place names, numbers, and abbreviations character by character.
* Mark unreadable or uncertain passages explicitly.
* Separate source spelling from later normalisation.
* Record each manual correction and its reason.

The result is a verified working transcription linked to the object identifier and the source image. It is not automatically an edition.

## **3.3 Phase B: information extraction**

The verified transcription becomes the input for structured extraction. The prompt contains a compact schema that defines fields, allowed value types, evidence requirements, and the treatment of missing information. A JSON object is preferable when the relations between entities matter; a table can be sufficient for a flat list.

A minimal mobility-oriented schema may contain:

* object\_id: the stable identifier of the source object.
* person: the name as written, a normalised label, and an authority identifier when verified.
* place: the name as written, a normalised label, coordinates or an external identifier when verified.
* event\_or\_movement: a typed relation connecting person, place, date, work, or performance.
* date: the source expression, a normalised value, and uncertainty.
* evidence: a quotation or line reference that supports each extracted statement.
* status: verified, uncertain, or rejected after review.

The model may populate only information supported by the supplied source. Missing values remain empty. Inferences must be placed in a separate field and labelled. This separation enables participants to inspect the difference between extraction and interpretation.

## **3.4 Phase C: reconciliation and validation**

Extracted names and places can be compared with the project’s existing records and selected authority services. Candidate matches are reviewed through labels, dates, locations, occupations, and other distinguishing information. A match is stored with the consulted identifier and review status; uncertain candidates are retained as such.

The final exercise dataset contains the source identifier, verified transcription, structured statements, provenance, and validation status. This bundle supports the next unit because it connects each application feature to inspectable source evidence.

# 4\. Promptotyping Research Data

## **4.1 Promptotyping as a research method**

Promptotyping is an iterative method for developing small digital research applications through natural-language specifications, a maintained knowledge base, structured data, executable prototypes, and repeated expert review. [^9] The prompt is one component of the method. The durable research context lies in the documented question, data model, source material, decisions, and validation criteria.

A promptotype is useful when it makes a research operation inspectable. Examples include an interface for filtering objects by person and place, a map of movements with links back to evidence, a timeline that exposes uncertain dates, or a detail view that places the scan, transcription, metadata, and extracted statements side by side.

## **4.2 The knowledge base**

Before implementation, the group prepares a compact knowledge base containing:

* the reduced research question and its scope;
* the available M³GIM data and the meaning of each field;
* the entity and relation model;
* source and rights information;
* uncertainty and validation rules;
* the intended users and tasks;
* a small set of representative records, including difficult cases;
* the required views and interactions;
* criteria for evaluating the prototype.

This knowledge base allows an AI-assisted coding environment to work with the same documented assumptions as the participants. It also makes it possible to revise the prototype without losing the reasoning behind data and interface choices.

## **4.3 Building the digital research application**

The group translates the question into observable application behaviour. If the question concerns movement between places, the application needs place identifiers or coordinates, a relation linking a person or event to each place, temporal information, and a view that makes the sequence inspectable. If the evidence is uncertain, the interface must display that status.

The first implementation should use the smallest dataset and feature set that can test the research operation. Participants then compare the application with the knowledge base and inspect whether:

* every visualised statement can be traced to a source object;
* filters and labels use the intended fields and relation types;
* uncertainty and missing values remain visible;
* maps or timelines do not imply precision absent from the data;
* the interface distinguishes source, transcription, extracted statement, and interpretation;
* the prototype can be revised by changing documented requirements rather than hidden assumptions.

The result is a small digital research artefact and a documented account of the data transformations it depends on. The exercise evaluates the artefact through the research question and source evidence.

# 5\. Workshop materials and outputs

## **Provided materials**

* Wednesday slides combining the relevant content from the three existing Stefan Zweig Digital teaching decks.
* Thursday slides in English covering LLM foundations, AI readiness, the M³GIM workflow, validation, and Promptotyping.
* This course reader with definitions, workflow descriptions, exercise instructions, and bibliography.
* A small M³GIM dataset with images or scans of already catalogued objects, matching descriptive data, stable identifiers, and permitted teaching use.
* Prompt templates for transcription, extraction, reconciliation, and prototype development.
* A compact schema and example records aligned with the reduced Mobility Studies question.

## **Participant outputs**

* A corrected transcription with documented uncertainty.
* A validated structured dataset linked to the source objects.
* A small digital research application developed from the structured data.
* A short validation record documenting findings, limitations, and revisions.

# 6\. Key takeaways

Digitisation begins a chain of representations. Images, transcriptions, metadata, encoded texts, structured entities, and interfaces are connected, but each has a distinct function and production history.

Research data become reusable when their model, provenance, identifiers, rights, and validation procedures are documented. Standards such as TEI, RDF, IIIF, and repository models support specific parts of this work.

Large language models can propose transformations across images, text, data, and code. Their outputs require source-based validation and an explicit output contract.

Promptotyping connects a research question, documented data, and an executable application. Its value lies in making the relation between evidence, model, and interface inspectable.

# 7\. Bibliography

Bender, Emily M., Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021\. “[On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922)” In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, 610–623.

Berners-Lee, Tim. 2006\. “[Linked Data](https://www.w3.org/DesignIssues/LinkedData.html).” Design Issues. Last modified 18 June 2009\.

Consultative Committee for Space Data Systems. 2012\. [Reference Model for an Open Archival Information System (OAIS)](https://public.ccsds.org/Pubs/650x0m2.pdf). CCSDS 650.0-M-2. Washington, DC: CCSDS.

Drucker, Johanna. 2011\. “[Humanities Approaches to Graphical Display](https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html).” Digital Humanities Quarterly 5 (1).

Geiger, Jonathan D. 2024\. “[Daten / Forschungsdaten](https://doi.org/10.17175/wp_2023_003_v2).” In Begriffe der Digital Humanities: Ein diskursives Glossar, Working Papers 2, version 2.0.

International Image Interoperability Framework Consortium. 2020\. [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/).

National Information Standards Organization. 2017\. [Understanding Metadata: What Is Metadata, and What Is It For? A Primer](https://www.niso.org/publications/understanding-metadata-2017). Baltimore: NISO.

Pollin, Christopher. 2025\. [Digital Scholarly Editions als Interface: Am Beispiel der digitalen Briefedition Stefan Zweig Digital](https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602). Doctoral dissertation, University of Graz.

Pollin, Christopher. 2026\. “[Ein Promptotyping-Projekt anlegen: Von den Forschungsdaten zum Forschungsartefakt](https://dhcraft.org/excellence/blog/Was-ist-Promptotyping/).” Digital Humanities Craft, 19 July 2026\.

Schöch, Christof. 2013\. “[Big? Smart? Clean? Messy? Data in the Humanities](https://zenodo.org/records/8432).” Journal of Digital Humanities 2 (3): 2–13.

Text Encoding Initiative Consortium. 2026\. [TEI P5: Guidelines for Electronic Text Encoding and Interchange](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/index.html). Version 4.12.0.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017\. “[Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html).” Advances in Neural Information Processing Systems 30\.

Wilkinson, Mark D., Michel Dumontier, IJsbrand Jan Aalbersberg, et al. 2016\. “[The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18).” Scientific Data 3: 160018\.

World Wide Web Consortium. 2014\. [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). W3C Recommendation, 25 February 2014\.

[^1]: This reader uses research data as a functional umbrella term. It includes source representations, descriptions, identifiers, structured entities and relations, software, prompts, and documented outputs when they are created, selected, or transformed as evidence in a research process. For the definitional debate in the humanities, see Geiger 2024 and Schöch 2013\.

[^2]: Metadata are structured statements about resources. They may be descriptive, administrative, technical, structural, or preservation-oriented. See National Information Standards Organization 2017\.

[^3]: The Text Encoding Initiative publishes a modular XML vocabulary and guidelines for representing textual structure, scholarly description, and features relevant to computer-assisted processing. See Text Encoding Initiative Consortium 2026\.

[^4]: Authority data provide controlled records and persistent identifiers for entities such as persons, places, organisations, or works. The Integrated Authority File (GND), ORCID, and GeoNames are examples with different scopes and governance models.

[^5]: RDF expresses statements as subject–predicate–object relations whose components can be identified with IRIs. Linked Open Data uses Web identifiers and links so that datasets can be connected and explored across systems. See World Wide Web Consortium 2014 and Berners-Lee 2006\.

[^6]: OAIS is a conceptual reference model for long-term preservation. It distinguishes the information submitted to an archive, managed within it, and disseminated to users. It does not prescribe a particular software product. See Consultative Committee for Space Data Systems 2012\.

[^7]: AI readiness is used here as an operational workshop term. It describes whether material, documentation, rights, target structure, representative examples, and validation procedures are adequate for a defined model-assisted task.

[^8]: An LLM is a neural language model trained to predict and generate token sequences. Current frontier systems may combine language modelling with images, tools, or code execution, but fluent output remains probabilistic and can be factually wrong. See Vaswani et al. 2017 and Bender et al. 2021\.

[^9]: Promptotyping is an iterative method developed for producing digital research applications through natural-language specifications, a maintained project knowledge base, structured data, executable prototypes, and repeated expert review. See Pollin 2026\.
