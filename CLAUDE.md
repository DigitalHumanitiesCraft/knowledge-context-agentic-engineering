# CLAUDE.md

Teaching material and workshop platform for the teaching line *Knowledge, Context and Agentic Engineering for Knowledge Work*. Read `knowledge/INDEX.md` first; the knowledge base in `knowledge/` is the working context for every substantial task.

## Naming

- Never write the word "Master" in this repo. The three holdings are the **Full Slide Deck** (`slides/full-slide-deck.md`), the **Full Lecture Notes** (`script/full-lecture-notes-en.md`, `script/full-lecture-notes-de.md`) and the **Video Playlist** whose public URL lives in `data/workshops.json` and whose inventory lives in `data/videos.json`. All three share the same five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance. On the public page the slide deck and the lecture notes appear as Slides and Lecture Notes, in German Folien and Skriptum; the repository names stay as given here.
- Each holding has its own function and is described by that function. A count of modules never stands in for that description. The Full Slide Deck is the complete overview in slide form, a reference work and the source from which workshop-specific decks are assembled; it is not presented as one teaching session. The Full Lecture Notes are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The Video Playlist combines DHCraft videos with selected contributions by others in a deliberate sequence from the foundations to more complex topics, and it is curated, maintained and extended as suitable material appears.
- The slide deck and the lecture notes express the same maintained concepts at different levels of expansion. The slide deck maintains the reference structure and the selection surface for workshop decks, the lecture notes maintain the expanded explanation, and a conceptual change touching both is reconciled across them before any specialised export is regenerated.
- A workshop is a documented specialization of the material. Its profile selects modules and adds what belongs to that instance alone. Published workshop artefacts may repeat selected explanatory slides so they remain usable on their own; the Full Slide Deck and Full Lecture Notes remain the maintained sources for shared text.
- The material is never called a corpus. Corpus keeps its technical sense of research data, which this line teaches on in the Hersch, Zweig and charter material. Say "the material" or "teaching material" for the whole, name the holding (Full Slide Deck, Full Lecture Notes) or the module where that is meant, and call the relation of a workshop to it a profile or a documented specialization.

## Register and instances

- `data/workshops.json` is the register and the source of truth for which instances exist. A change to an instance starts there, and the affected source profiles are updated in the same work step.
- The register uses `slide_deck` and `lecture_notes` for material artefacts. Each artefact exposes `google`, `markdown` and `pdf`; `null` means that format remains in preparation. `materials_status` controls material actions and visual release state and must not be inferred from the event field `status`. These fields retain material provenance; they no longer imply a public event page.
- Existing `web_module` records retain historical implementation metadata. They do not indicate a current public page or generate navigation; material provenance remains separate.
- Each workshop entry carries an ordered `modules` array containing the visible module numbers `01` to `05`. The subset remains metadata for the workshop material. Presence records inclusion in the teaching sequence; the interface carries no separate full, touched or absent states.
- An instance id has the form `YYYY-MM-DD-slug`. The same string names the register entry, the folder `workshops/<id>/` and the git tag of the taught state.
- A workshop folder holds `profile.md`, `slide-deck.md`, `lecture-notes.md` and `data/`.
- Only upcoming instances live in the working tree. A delivered instance is tagged, then removed from tree and register; git history keeps it. When a document has to cite removed material, verify the last commit that held it with `git log --oneline --follow -- <path>` and cite it as preserved in git history at that short SHA.

## Modules and videos

- `data/videos.json` is the source of truth for the module groups on the page. It records the maintained playlist order, stable YouTube video id, display title, the required primary `module`, duration, an optional `lang` and, per module, the title and definition in both languages. An optional `related_modules` array records a documented cross-module relation. The paired pages list the same entries by primary module and retain playlist order inside each group.
- A video renders exactly once, under its primary module. A related module never produces a second card; it may appear as quiet metadata where the existing component carries it without materially increasing card height, and otherwise stays in the data and in the knowledge record.
- Classify a video by its primary teaching function. The register records when it was last checked against the public playlist in its `checked` field. Playlist order is retained inside every module group.
- Module 05 is the final module group and carries the seven accepted videos in their maintained playlist order, moving from broad accounts of ideology, power and control towards specialised AGI debates.
- Video links use the canonical `https://www.youtube.com/watch?v=<id>` form. The page shows no preview images and loads nothing from YouTube; do not copy third-party thumbnails into the repository without a documented reuse right.
- Write `Context Engineering` with a capital `C` in every public occurrence.

## Covers

The historical workshop covers left the published tree on 2026-11-04 together with the register's `cover` fields, because the single-page site does not display them. They are preserved in git history at `e66901b` under `docs/assets/covers/`. Any later reuse requires a concrete author decision.

## Link hygiene

Never publish a URL carrying tracking or sharing parameters, among them `ouid=`, `authuser=`, `rcm=` and anything beginning with `utm_`. Remove those parameters while preserving parameters required by the destination, including YouTube `v` and `list`. For a Google artifact the `/edit` path stays, so a cleaned link ends at `/edit`. Check any link before it enters the register, a page or a knowledge document.

## Content boundaries

- No third-party personal names in documents produced here. Use role and institution. Names inside slide-text exports, lecture notes, transcripts and other teaching material are research data and stay untouched.
- No monetary amounts anywhere in this repo, including offers, rates and budgets.
- No facsimiles. Image rights for the Hersch and Zweig material remain with the source projects; link, do not copy.
- CC BY 4.0 covers the public page and original text. A Slide Deck receives the same material licence only after its embedded third-party image rights have been checked. The footer licence link names the scope as `CC BY 4.0 for the original text` or `CC BY 4.0 für die eigenen Texte`; the exact scope `page-and-original-text` stays recorded in `data/workshops.json` and in `knowledge/governance.md`.
- Grokipedia is never a source.

## Platform

The public site is one static page per language, `index.html` and `index.de.html`. The page leads from the title and introduction to four material cards (Preparation, Slides, Lecture Notes, Methods) and then to the modules with their definitions and video lists, which link the full playlist. There are no separate About or Preparation pages and no generic arrow-back links. The canonical legal notice remains linked in the footer, together with the licence scope. Event listings and Learning Routes remain retired; teaching sources are unchanged.

Preparation links to the existing English Google Slides deck [Technical Setup](https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit). Its URL and language are registered in `data/workshops.json` under `preparation`. Both language versions identify the English teaching language. It appears as the first material card, with its own line mark `docs/assets/materials/preparation.svg` and a direct Google Slides action; no Google Slides iframe or slide image is embedded. No separate HTML setup curriculum or subject-introduction sequence is maintained in that section.

The workshop records in `data/workshops.json` retain material provenance and do not generate public event pages or navigation. Full-material and video links retain their existing ownership and rights boundaries. External Google files and sharing permissions are unchanged.

- Public entry points are `index.html` and `index.de.html`; the language control connects them.

- The platform in `docs/` is static HTML and CSS with no build step and no JavaScript required for any content; `docs/assets/site.js` only enhances the term definition and opens a module group named in the fragment. Fonts are self-hosted under `docs/assets/fonts/`, and the page loads no external runtime resource. Slide decks are linked from card actions and never embedded. The registers live in `data/` outside the published tree, because the pages do not read them and they carry working states.
- The public tree and its registers are the source of truth for installed topology. Release evidence belongs in Git and `knowledge/journal.md`; current substantive acceptance points belong in `communication/research/director-log.md`.
- The general public learning surface consists of the language-matched single page. The five subject modules retain numbers 01 through 05 as the Full Slide Deck structure and as workshop and video classifications; they do not own public overview hubs. Landing-page fragment ids `module-01` through `module-05` remain stable compatibility targets.
- The maintained Curated Skills source remains in `knowledge/drafts/curated-agent-skills-library.md`. It has no current public placement; any later placement requires a separate author decision; entries are never presented as installed or recommended before instruction and permission review.
- The page chrome of logo, language control and footer is binding and identical on both pages, and the favicon set in `docs/assets/favicon/` is linked by both. The DHCraft logo is the only header link to `https://dhcraft.org`; the H1 names the page, so the header carries no site name and no section navigation. Generic arrow-back links are excluded. Before any UI work read `knowledge/design.md` and follow it; `knowledge/specification.md` records the current requirements.
- The shared footer is one compact grid of three groups, publisher identity, two short sentences on development, methods and funding, and a short navigation carrying the teaching-material repository, the licence link `CC BY 4.0 for the original text` and the canonical DHCraft imprint at `https://dhcraft.org/imprint`. The navigation carries the visible label `Further links` or `Weiterführende Links`. The provenance sentence names Digital Humanities Craft with Promptotyping and Research Mission Control and links them; the Methods card links the method repositories. No model name or version appears, because those age between releases. Detailed dated tool and model provenance stays in `knowledge/journal.md`.
- Historical HTML prototypes are preserved in git history at `a3cd893` under `knowledge/drafts/platform-prototypes/`; prototypes never live under the published `docs/` tree.

## Adjacent teaching sources

Two neighbouring DHCraft teaching projects supply material to this line without merging into it. Both source folders stay read-only during any integration.

- `DigitalHumanitiesCraft/ai-coding-literacy` remains an independent published German-language curriculum with its own rights, deployment and dataset contracts. Its independent curriculum is available at `https://digitalhumanitiescraft.github.io/ai-coding-literacy/de/`. Its seven competencies do not replace the five subject modules or the Preparation deck.
- The local folder `DHCraft/ai-literacies` is an unversioned Astro prototype and stays read-only migration input with no publication status. Nothing of its runtime enters this repo, which excludes Astro, npm dependencies, TypeScript, `node_modules`, its source CSS tokens, its build configuration and its root-relative route system. The platform stays a no-build static publication.
- Migrated content is re-authored in this design system, reconciled against `knowledge/terms.md` and carries its module mapping, audience, source reference, verification date and editorial status. No dataset, screenshot, external slide image or video thumbnail is copied.
- The Prompt Engineering unit is the first migration candidate and remains in preparation because no static KCE lesson exists. Former route acceptance points require reconciliation with the reduced public scope before further implementation. The Tools, Multimodal, Administration Data Analysis and Research Data Analysis units additionally wait for the verified VetMedAI intake, because their product facts, model claims, data-protection statements and rights boundaries need re-verification.

## Research Mission Control

Promptotyping develops the artefacts, and Research Mission Control coordinates who decides, who implements and who verifies. `communication/PROTOCOL.md` carries the full contract; this section is only the trigger.

- Delegated work that arrives through the Context Stream in `communication/` starts by reading the applicable message and holding to its authority, write boundary, exclusions and verification criteria. Durable knowledge stays in `knowledge/`, and the stream stays transport.
- Communication uses the smallest fitting product, a direct answer, a situation report, a Research Director Point or an acceptance sheet.
- Claim only the maturity stage the evidence supports, separating draft, active installation, formal validation, observed function, substantive review and Research Director acceptance.
- Every required Research Director contribution comes from `communication/research/director-log.md` and is named by its `RD-###` identifier and type.
- Report installation, formal validation, observed function, commit, push and deployment as separate statements. A passing local check is no evidence of a pushed or deployed state.

## Working rules

- Produced text is English, including file and folder names. The teaching material itself is bilingual and each holding keeps its own language.
- `knowledge/drafts/` holds agent-written decision preparation. Drafts are proposals, never canonical.
- Term wording, design approvals, publication steps, git tags, rights questions and everything `knowledge/governance.md` marks as operator-gated go to the operator. Prepare such a decision with a recommendation and leave the taking of it to the operator.
- The authorised integrator records substantive transitions in `knowledge/journal.md` and keeps accepted future work in `knowledge/plan.md`. A delegated lane writes either document only when its explicit write boundary includes that path.
- `knowledge/handoff.md` is the Process Inbox for received deltas that still require verification, integration or reasoned rejection. Completed states belong in the responsible knowledge document, `knowledge/journal.md` and Git. Do not promote an active installation to formal validation, observed function or release without the corresponding gate evidence.
