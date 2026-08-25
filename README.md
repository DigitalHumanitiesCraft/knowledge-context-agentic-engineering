# Knowledge, Context and Agentic Engineering for Knowledge Work

This repository is the home of a teaching line on working with large language models in research and in professional knowledge work. It covers what a language model is and where its capability is uneven, how a prompt addresses it, how project knowledge and working context are built and maintained, how multi-step agentic work is organized and controlled, and how the results are checked, governed and accepted. The audience is general, everyone who does computer-based, data-driven knowledge work.

## Derivation by profile

The material is maintained through three holdings, each with its own function. The **Full Slide Deck** is the complete overview of the teaching material in slide form. It serves as a reference work and as the source from which workshop-specific decks are assembled, and it is not presented as one teaching session. The **Full Lecture Notes** are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The **Video Playlist** combines DHCraft videos with selected contributions by others; its deliberate sequence runs from the foundations to more complex topics and forms a structured learning path that is curated, maintained and extended as suitable material appears. All three holdings share the same five modules, and the playlist assigns every entry one primary module.

The public learning architecture adds **Module 00 · Preparation and AI Coding Literacy** as a neutral prerequisite. Modules 01 through 05 each have a bilingual overview hub that connects their concepts, starter sequence, teaching material, videos and workshop uses. Module 00 does not enter workshop module arrays or video classification.

| Module | Title |
| --- | --- |
| 1 | Understanding Large Language Models |
| 2 | Prompt Engineering |
| 3 | Knowledge and Context Engineering |
| 4 | Agentic Engineering |
| 5 | Critical Perspectives and Governance |

Every workshop taught from this material is a documented specialization. Its profile selects modules, sets depth, case studies and language, and adds what belongs to that one instance, the schedule, the hands-on instructions and the venue specifics. An improvement to a module therefore reaches every workshop that uses the module, and the core of the material stays domain-neutral because the case studies are exchangeable modules of their own.

Only upcoming instances live in this repository. Once an instance has been taught, its state is tagged and its folder leaves the working tree, so the platform shows what people can still attend. The material stays retrievable in git history under its tag.

## How the repository is organized

| Path | Content |
| --- | --- |
| `knowledge/` | Project knowledge base (Promptotyping documents); start at `knowledge/INDEX.md` |
| `script/full-lecture-notes-en.md`, `script/full-lecture-notes-de.md` | The Full Lecture Notes |
| `script/modules/` | The five-module cut of the lecture notes, with its coverage report in `script/COVERAGE.md` |
| `slides/full-slide-deck.md` | The Full Slide Deck as text with speaker notes; the visual deck lives in Google Slides and is linked |
| `docs/data/videos.json` | The Video Playlist inventory, including order, primary module, any related modules and duration |
| `workshops/<id>/` | One folder per upcoming instance, holding `profile.md`, `slide-deck.md`, `lecture-notes.md` and `data/` |
| `docs/` | The platform (static site, GitHub Pages), including the register `docs/data/workshops.json` and the covers in `docs/assets/covers/` |
| `docs/modules/` | Five bilingual subject-module hubs for Modules 01 through 05 |
| `docs/tutorials/` | Bilingual AI Harness introductions for Claude Code, Codex and Pi |
| `communication/` | The Research Mission Control transport for current briefs, results and recipient state |

Instance ids have the form `YYYY-MM-DD-slug` and are the same string in the register, the workshop folder, the cover file, the subpage and the git tag.

## The platform

The platform is a no-build static site in `docs/`; its content and navigation require no JavaScript. The installed v0.3 tree contains 36 HTML files in eighteen English/German pairs on stylesheet version `20260825-19`. Module 00 retains the stable Preparation routes, and ten files under `docs/modules/` provide the five bilingual subject hubs. Every visible module marker routes to the language-matched hub.

The landing pages organise five learning routes into Foundation, AI Harness introductions and Research workflow. AI Coding Literacy is the external German foundation. Claude Code, Codex and Pi are local bilingual Module 04 routes. Research Data and Knowledge Work remains visibly in preparation. The three Harness introductions use a comparable eight-step sequence from purpose and prerequisites to a first reversible check. Module 04 also carries an embedded Curated Skills area with externally maintained examples and explicit review status.

This v0.3 working tree is actively installed, formally validated and browser-observed at the seven required widths. Commit, tag, push, deployment and Research Director acceptance remain separate states.

https://digitalhumanitiescraft.github.io/knowledge-context-agentic-engineering/

## Development method and orchestration

[Promptotyping](https://dhcraft.org/Promptotyping/) is the artefact-development method. Maintained documents in `knowledge/` guide iterative production, inspection and correction of teaching material, interface code and workshop packages.

[Research Mission Control](https://github.com/DigitalHumanitiesCraft/research-mission-control) is the orchestration contract for accountable research and implementation lanes. The Research Director retains substantive authority. The Research Orchestrator frames research and issues bounded implementation briefs. The Operational Orchestrator coordinates authorized implementation, verification, integration and release. The Context Stream in `communication/` transports current briefs, results and recipient state; durable project knowledge remains in `knowledge/`.

## Language and licence

Repository files are English. The teaching material is bilingual, and language is handled per module and per instance, so each holding carries the language it was authored or taught in.

Text content is licensed [CC BY 4.0](LICENSE). Slide decks are checked individually for third-party image rights before the license statement is extended to them. The executable CLARIAH-AT hands-on package lives in [zbz-ocr-tei](https://github.com/chpollin/zbz-ocr-tei).

Christopher Pollin, [Digital Humanities Craft](https://dhcraft.org)
