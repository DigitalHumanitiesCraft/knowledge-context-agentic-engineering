# Knowledge, Context and Agentic Engineering for Knowledge Work

This repository is the home of a teaching line on working with large language models in research and in professional knowledge work. It covers what a language model is and where its capability is uneven, how a prompt addresses it, how project knowledge and working context are built and maintained, how multi-step agentic work is organized and controlled, and how the results are checked, governed and accepted. The audience is general, everyone who does computer-based, data-driven knowledge work.

## Derivation by profile

The material is maintained through three holdings, each with its own function. The **Full Slide Deck** is the complete overview of the teaching material in slide form. It serves as a reference work and as the source from which workshop-specific decks are assembled, and it is not presented as one teaching session. The **Full Lecture Notes** are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The **Video Playlist** combines DHCraft videos with selected contributions by others; its deliberate sequence runs from the foundations to more complex topics and forms a structured learning path that is curated, maintained and extended as suitable material appears. All three holdings share the same five modules, and the playlist assigns every entry one primary module.

The public platform presents the shared teaching resources and Preparation. Its current scope is described below.

| Module | Title |
| --- | --- |
| 1 | Understanding Large Language Models |
| 2 | Prompt Engineering |
| 3 | Knowledge and Context Engineering |
| 4 | Agentic Engineering |
| 5 | Critical Perspectives and Governance |

Every workshop taught from this material is a documented specialization. Its profile selects modules, sets depth, case studies and language, and adds what belongs to that one instance, the schedule, the hands-on instructions and the venue specifics. An improvement to a module therefore reaches every workshop that uses the module, and the core of the material stays domain-neutral because the case studies are exchangeable modules of their own.

Only upcoming instances live in this repository. Once an instance has been taught, its state is tagged and its folder leaves the working tree, while the public platform presents shared material without individual events. The material stays retrievable in git history under its tag.

## How the repository is organized

| Path | Content |
| --- | --- |
| `knowledge/` | Project knowledge base (Promptotyping documents); start at `knowledge/INDEX.md` |
| `script/full-lecture-notes-en.md`, `script/full-lecture-notes-de.md` | The Full Lecture Notes |
| `script/modules/` | The five-module cut of the lecture notes, with its coverage report in `script/COVERAGE.md` |
| `slides/full-slide-deck.md` | The Full Slide Deck as text with speaker notes; the visual deck lives in Google Slides and is linked |
| `data/videos.json` | The Video Playlist inventory, including order, primary module, any related modules and duration |
| `workshops/<id>/` | One folder per upcoming instance, holding `profile.md`, `slide-deck.md`, `lecture-notes.md` and `data/` |
| `data/` | The registers `workshops.json` and `videos.json`, outside the published tree |
| `docs/` | The platform (static site, GitHub Pages) |
| `scripts/build_glossary.py` | Generates the glossary pages from `knowledge/terms.md` |
| `communication/` | The Research Mission Control transport for current briefs, results and recipient state |

Instance ids have the form `YYYY-MM-DD-slug` and are the same string in the register, the workshop folder and the git tag.

## The platform

The public site is one static page per language, `docs/index.html` and `docs/index.de.html`. The page leads from a short introduction to four material cards, Preparation, the slides, the lecture notes and four DHCraft methods, and then to the five modules with their definitions and video lists. A glossary page per language, generated from `knowledge/terms.md`, gives one-sentence definitions of the terms in English and German. The footer links the canonical legal notice and states the licence scope.

Preparation links the English Google Slides deck [Technical Setup](https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit) from the first of the four material cards. Its URL and language are registered in `data/workshops.json` under `preparation`. The Video Library is rendered from `data/videos.json`.

The workshop records retain material provenance and generate no public event pages. The site is no-build HTML and CSS whose content needs no JavaScript, with self-hosted fonts, and its requirements are maintained in [`knowledge/specification.md`](knowledge/specification.md). Local changes require author acceptance and a separate publication step.

https://dhcraft.org/knowledge-context-agentic-engineering/

## Development method and orchestration

[Promptotyping](https://dhcraft.org/Promptotyping/) is the artefact-development method. Maintained documents in `knowledge/` guide iterative production, inspection and correction of teaching material, interface code and workshop packages.

[Research Mission Control](https://github.com/DigitalHumanitiesCraft/research-mission-control) is the orchestration contract for accountable research and implementation lanes. The Research Director retains substantive authority. The Research Orchestrator frames research and issues bounded implementation briefs. The Operational Orchestrator coordinates authorized implementation, verification, integration and release. The Context Stream in `communication/` transports current briefs, results and recipient state; durable project knowledge remains in `knowledge/`.

### AI-assisted authorship and provenance

The concepts, arguments and editorial decisions in this repository originate with Christopher Pollin. Almost all prose, interface copy, diagrams and implementation artefacts were drafted with AI harnesses and revised through repeated Promptotyping and Research Mission Control cycles. Human authorship here means responsibility for the ideas, source selection, decisions, evaluation and publication; it does not imply manual production of every sentence or file. Third-party sources and teaching materials retain their own stated authorship and rights.

The condensed decision record is maintained in [`knowledge/journal.md`](knowledge/journal.md). The complete sequence of revisions, including superseded formulations and technical iterations, remains inspectable in the Git history.

## Language and licence

Repository files are English. The teaching material is bilingual, and language is handled per module and per instance, so each holding carries the language it was authored or taught in.

Text content is licensed [CC BY 4.0](LICENSE). Slide decks are checked individually for third-party image rights before the license statement is extended to them. The executable CLARIAH-AT hands-on package lives in [zbz-ocr-tei](https://github.com/chpollin/zbz-ocr-tei).

Christopher Pollin, [Digital Humanities Craft](https://dhcraft.org)
