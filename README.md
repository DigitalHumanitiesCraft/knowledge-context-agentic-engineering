# Knowledge, Context and Agentic Engineering for Knowledge Work

This repository holds the master corpus of the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*: a master script and a master slide set covering the full material, from LLM fundamentals through prompt, context, knowledge and agentic engineering to Promptotyping and verification. The master addresses everyone who does computer-based, data-driven knowledge work.

Every workshop or course taught from this material is a documented profile. A profile selects modules from the master, sets depth and case studies for its audience, and adds its own schedule and hands-on. Current profiles: CLARIAH-AT Summer School 2026 (research data workflows and digital editions), KUG/M3GIM summer school (compact, no LLM or programming prerequisites), Uni for Life (extended, for professionals from companies and other disciplines).

The platform (GitHub Pages, in preparation) presents the master and one page per workshop. The workshop page is the live resource during the course and the follow-up material afterwards: https://digitalhumanitiescraft.github.io/knowledge-context-agentic-engineering/

## How the repository is organised

| Path | Content |
| --- | --- |
| `knowledge/` | Project knowledge base (Promptotyping documents); start at `knowledge/INDEX.md` |
| `script/` | Master script in modules; German source and reviewed English translation |
| `slides/` | Master slide texts and speaker notes; the visual decks live in Google Slides and are linked |
| `workshops/` | One folder per workshop: profile, materials, slide exports per taught state |
| `docs/` | The platform (static site, GitHub Pages), including the workshop register `docs/data/workshops.json` |

The state actually taught in a workshop is marked with a git tag; the workshop page links to it.

## Method, languages, license

The repository is developed with [Promptotyping](https://dhcraft.org/Promptotyping/); the `knowledge/` folder holds the distilled project knowledge (requirements, terms, design, governance, provenance) that agents and humans work from. Repository files are English; the master script content is bilingual, German as source language with a reviewed English translation. Textual content is licensed CC BY 4.0; slide decks are checked individually for third-party image rights. The executable CLARIAH-AT hands-on package lives in [zbz-ocr-tei](https://github.com/chpollin/zbz-ocr-tei); project coordination lives in the author's research vault.

Christopher Pollin, [Digital Humanities Craft](https://dhcraft.org)
