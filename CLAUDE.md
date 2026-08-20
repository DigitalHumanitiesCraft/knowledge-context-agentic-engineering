# CLAUDE.md

Corpus and workshop platform for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*. Read `knowledge/INDEX.md` first; the knowledge base in `knowledge/` is the working context for every substantial task.

## Naming

- Never write the word "Master" in this repo. The two holdings are the **Full Slide Deck** (`slides/full-slide-deck.md`) and the **Full Lecture Notes** (`script/full-lecture-notes-en.md`, `script/full-lecture-notes-de.md`). The corpus they carry is cut into five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance.
- A workshop is a documented specialization of the corpus. Its profile selects modules and adds what belongs to that instance alone. Corpus text is referenced from the workshop folder rather than duplicated into it.

## Register and instances

- `docs/data/workshops.json` is the register and the source of truth for which instances exist. A change to an instance starts there, and the affected pages are updated in the same work step.
- An instance id has the form `YYYY-MM-DD-slug`. The same string names the register entry, the folder `workshops/<id>/`, the cover `docs/assets/covers/<id>.png`, the subpage and the git tag of the taught state.
- A workshop folder holds `profile.md`, `slide-deck.md`, `lecture-notes.md` and `data/`.
- Only upcoming instances live in the working tree. A delivered instance is tagged, then removed from tree and register; git history keeps it. When a document has to cite removed material, verify the last commit that held it with `git log --oneline --follow -- <path>` and cite it as preserved in git history at that short SHA.

## Covers

Covers arrive from an external image pipeline and are placed as `docs/assets/covers/<id>.png`. They are PNG, 16:9, at least 1280 px wide, with the upper third free of content and no text inside the image, because the page chrome sets the title over it. Do not generate covers here and do not scale a smaller image up.

## Link hygiene

Never publish a URL carrying tracking or sharing parameters, among them `ouid=`, `authuser=`, `rcm=` and anything beginning with `utm_`. Strip the query string from a pasted link. For a Google artifact the `/edit` path stays, so a cleaned link ends at `/edit`. Check any link before it enters the register, a page or a knowledge document.

## Content boundaries

- No third-party personal names in documents produced here. Use role and institution. Names inside slide-text exports, lecture notes, transcripts and other corpus material are research data and stay untouched.
- No monetary amounts anywhere in this repo, including offers, rates and budgets.
- No facsimiles. Image rights for the Hersch and Zweig material remain with the source projects; link, do not copy.
- Grokipedia is never a source.

## Platform

- The platform in `docs/` is static HTML and CSS with no build step and no JavaScript required for any content. External resources are limited to Google Fonts.
- The page chrome of header brand, navigation and footer is binding and identical across pages, and the favicon set in `docs/assets/favicon/` is linked by every page. Before any UI work read `knowledge/design.md` and follow it. Design iteration 4 is the state in force.
- Language is handled per module and per instance. A page carries the language of the material it presents, and there is no page-level EN/DE toggle.

## Working rules

- Produced text is English, including file and folder names. The teaching material itself is bilingual and each holding keeps its own language.
- `knowledge/drafts/` holds agent-written decision preparation. Drafts are proposals, never canonical.
- Term wording, design approvals, publication steps, git tags, rights questions and everything `knowledge/governance.md` marks as operator-gated go to the operator. Prepare such a decision with a recommendation and leave the taking of it to the operator.
- Record decisions and session outcomes in `knowledge/journal.md`, and keep `knowledge/plan.md` current when a work package changes state.
