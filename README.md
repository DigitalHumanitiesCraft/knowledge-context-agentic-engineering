# Knowledge, Context and Agentic Engineering for Knowledge Work

This repository is the home of a teaching line on working with large language models in research and in professional knowledge work. It covers what a language model is and where its capability is uneven, how a prompt addresses it, how project knowledge and working context are built and maintained, how multi-step agentic work is organized and controlled, and how the results are checked, governed and accepted. The audience is general, everyone who does computer-based, data-driven knowledge work.

## Derivation by profile

The material is maintained once. Two holdings carry it, the **Full Slide Deck** and the **Full Lecture Notes**, and both are cut into five modules.

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
| `workshops/<id>/` | One folder per upcoming instance, holding `profile.md`, `slide-deck.md`, `lecture-notes.md` and `data/` |
| `docs/` | The platform (static site, GitHub Pages), including the register `docs/data/workshops.json` and the covers in `docs/assets/covers/` |

Instance ids have the form `YYYY-MM-DD-slug` and are the same string in the register, the workshop folder, the cover file, the subpage and the git tag.

## The platform

The platform is a static site served by GitHub Pages from `docs/`. The landing page presents the material with its five modules and the upcoming instances as cards; each instance has its own subpage, which is the live resource during the course and the follow-up material afterwards. A shared preparation page holds what participants set up before a course.

https://digitalhumanitiescraft.github.io/knowledge-context-agentic-engineering/

## Method, language, license

The repository is developed with [Promptotyping](https://dhcraft.org/Promptotyping/), an iterative, document-based method for building research artifacts with LLM-based agents. Its `knowledge/` folder holds the distilled project knowledge, the project description, requirements, terms, design, governance and provenance that agents and humans work from.

Repository files are English. The teaching material is bilingual, and language is handled per module and per instance, so each holding carries the language it was authored or taught in.

Text content is licensed [CC BY 4.0](LICENSE). Slide decks are checked individually for third-party image rights before the license statement is extended to them. The executable CLARIAH-AT hands-on package lives in [zbz-ocr-tei](https://github.com/chpollin/zbz-ocr-tei).

Christopher Pollin, [Digital Humanities Craft](https://dhcraft.org)
