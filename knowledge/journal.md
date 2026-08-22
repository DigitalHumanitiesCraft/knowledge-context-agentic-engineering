---
title: Journal
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Journal
  version: 0.3
  url: https://dhcraft.org/Promptotyping/promptotyping-document/journal
  alias: https://dhcraft.org/Promptotyping/#promptotyping-document-journal
status: active
created: 2026-08-20
updated: 2026-08-20
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
---

# Journal

The journal holds the working history of this repo as a narrative of its Promptotyping iterations, with decisions, their reasons and documented dead ends. It is neither git log nor session minutes; the commits live in the git history, the journal condenses them. Addressed are the operator returning after weeks and the agent continuing without loss of context. The journal is public; the privacy rule in `governance.md` applies.

## August 2026

### 2026-08-20 — Founding, language regime and specification round

**Goal.** Create the canonical home of the teaching line and settle its operating rules.

**Course.** The repo was founded public under DigitalHumanitiesCraft, preceded by a vault-side linking analysis that mapped the CLARIAH lecture notes against the author's knowledge base; its findings ground `terms.md` and `plan.md`. A specification round with the operator settled the rules, beginning with the main title *Knowledge, Context and Agentic Engineering for Knowledge Work*, no subtitle; the repo is canonical for the corpus texts, the vault versions become references, Google artifacts remain derived surfaces; all repository files are English including file and folder names (`begriffe.md` became `terms.md`, the planned `skriptum/` became `script/`), while the script content is bilingual, German source and reviewed English translation with an EN/DE toggle on the platform; recipe model, the corpus text lives once in modules and every workshop profile selects from it; the German script is the module source and the CLARIAH lecture notes become profile material; the corpus audience is generalized to computer-based, data-driven knowledge work; each workshop gets a subpage as live course resource; texts are licensed CC BY 4.0; the repo is single-author; corpus and CLARIAH tracks run in parallel with the CLARIAH date (2026-09-25) as fixpoint; taught states receive operator-set git tags named after registry ids.

**Outcome.** The rules are encoded in charter, governance, specification and plan; the founding documents were rewritten in English the same day (originals in the git history).

### 2026-08-20 — Design iterations and module structure

**Goal.** Find the platform design at the visible object and set the top-level structure of the corpus.

**Course.** Four prototype iterations, each reviewed by the operator. The first established the line-art motif (the path from source to verified artifact) and two font candidates. The second, approved in direction, fixed Space Grotesk, removed the stacked text levels and unified the page on one paper-white ground with turquoise `#0A7E7C` as the single accent. The third removed all section hairlines, introduced the operator's five modules (Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance) and built the footer with watercolor logo, imprint, Promptotyping line and CC BY notice. The fourth, approved and promoted, derived the identity palette from the logo (orange `#C87000`, blue `#5B8FC4`, green `#7C9200`, violet `#8140B8`), applied solely at the five module marks, and refactored the CSS into a documented token architecture with verified WCAG AA contrast. The 19-unit fine cut beneath the five modules stays a draft; Promptotyping, verification and the case studies sit under module 4 as a working setting.

**Outcome.** The design system is encoded in `design.md`; the fourth iteration became `docs/index.html`.

### 2026-08-20 — Intake, CLARIAH package and platform build-out

**Goal.** Bring the authoritative texts into the repo, build the first workshop package, and launch the platform build-out.

**Course.** Two triage agents mapped the operator's downloads; the operator named the authoritative files, the English lecture notes (work in progress) and the final CLARIAH workshop script. Intake copied both, the German lecture notes export and the full deck export; the CLARIAH PPTX deliberately waits for the taught state per the versioning rule. The CLARIAH profile was derived from the final script and corrected the register, since the hands-ons are Zweig-based (Radiovortrag transcription, then information extraction), Hersch is case material whose executable package lives in the external zbz repo. The VetMed Winter School (2026-11-30 to 2026-12-04, five-day extended derivation of the full corpus) entered the register with a provisional display title. Three specification decisions followed, a subpage per workshop, static pages kept in sync with the registry by agents instead of client-side rendering, and covers as 16:9 PNG at 1280 px minimum. Facsimile-bearing images stay out per the rights rule. Commissioned in parallel were the platform build-out (header brand, navigation, reworked cards, four subpages, following the functional model of the operator's earlier teaching site llmdh), the thin workshop profiles, the draft module cut of the German lecture notes, the decision-ready terms draft, and the title-image generation prompts. The knowledge documents adopted the template fields of the Promptotyping catalog.

**Outcome.** The platform is live in the repo with real register data and the real CLARIAH cover; the remaining work runs as delegated packages; the open operator gates are listed in `plan.md`.

### 2026-08-20 — Conceptual round

**Goal.** Settle the remaining conceptual directions in one pass.

**Course.** Four operator decisions. Source language holds per module, each module keeps the language it was authored in and the other side is the reviewed translation, which legitimizes the English-only corpus blocks without back-translation. Promptotyping, verification and the case studies stay under module 4. The register documents the whole history of the teaching line, so the VetMedAI workshop 1 (2026-04-22, Vetmeduni Wien) and the ÖAW AI Winter School (February 2026) enter as delivered instances. GitHub Pages goes live after the current build-out and a full verification pass; title images may follow afterwards. In the same round the journal was normalized to the Vorlage Journal schema, the knowledge documents adopted the catalog template fields, and the CC BY 4.0 license file was added.

**Outcome.** No conceptual gates remain open; what is left for the operator are content confirmations (fine cut, term wordings) and deliveries (title images, Winter School title).

### 2026-08-20 — Scope cut, Full naming and platform decisions

**Goal.** Settle what the public repo carries and under which names, after the conceptual round of the same day had pushed the register in the opposite direction.

**Course.** Three operator decisions in one pass. The first cuts the scope. Repo and register carry only the upcoming instances of the teaching line, and every delivered instance leaves the working tree. This reverses the decision of the conceptual round above, which had made the register the full history of the teaching line and had entered delivered instances as such. The reason for the reversal is what a public course platform is for. It answers which course someone can still attend, and a register that mixes past and future makes the reader sort that out first. Nothing is lost, because git history holds the removed material and each taught state carries its tag. The last commit holding the removed instances is `8d50211`; documents that cite them point there, as `terms.md` now does for the delivered Vetmeduni instance of 2026-04-22. Also removed were the Cologne summer school of 2025-09-08 and the Freiburg pre-workshop of 2025-09-24.

The second decision fixes the naming. The corpus is maintained once, as the Full Slide Deck and the Full Lecture Notes, and it is cut into five modules, Understanding Large Language Models, Prompt Engineering, Knowledge and Context Engineering, Agentic Engineering, Critical Perspectives and Governance. Every workshop is a documented specialization of that corpus. The earlier working name of the two holdings is retired across the repo, including in the journal entries above, which now carry the current names for the same objects. The files followed as `script/full-lecture-notes-en.md`, `script/full-lecture-notes-de.md` and `slides/full-slide-deck.md`, and the register gained a top-level key `full` with the deck link. The link to the lecture notes stays empty for now, because the source document holds two internal appendices that have to be split out before it can be shared.

The third decision closes the platform design. Iteration 4 is approved and in force, its page chrome and its favicon set are committed, and the requirement of a bilingual page toggle is dropped. Language is handled per module and per instance, so a page carries the language of the material it presents. The landing page with its horizontal instance cards and module badges, the instance subpages and the preparation page are built in parallel to this entry.

**Outcome.** The knowledge base states the current reality, the glossary in `terms.md` is filled from the corpus, and the naming rule together with the register rule is written into `CLAUDE.md`, so later sessions inherit both.

### 2026-08-20, Cover series selection and production contract

**Goal.** Give the Full Slide Deck and each upcoming workshop a recognizable cover that carries Knowledge, Context and Agentic Engineering through its own domain.

**Course.** The first generation round used a horizontal workflow diagram. It established paper ground, navy linework and watercolor accents, but its repeated stations read as an infographic and did not distinguish the workshop domains strongly enough. A second round moved to one integrated object per cover. Knowledge became archival or professional source material, the working context became a turquoise aperture, agentic action became a blue path or tool, and verification appeared as a restrained green registration detail. Domain objects then carried the difference between the instances, including an opera archive for KUG M3GIM, an edition codex for CLARIAH-AT, a fold-out edition workstation for HEDIT, a charter for the medieval-studies workshop, a modular research-software workbench for Göttingen, a document-handling instrument for Uni for Life and a veterinary microscopy specimen for the VetMed Winter School.

The operator selected all seven workshop images and retained the existing Full Slide Deck cover. The Full cover is stored at 1664 by 936 pixels; the workshop covers are stored at 1672 by 941 pixels. All eight files exceed the required width and are registered under their stable ids. The medieval-studies cover went through two replacements. The selected version contains three small Claude Code agent figures that inspect the charter, select a passage and manage write-back. This tool-specific figure is approved because Claude Code is the workshop environment.

The selected PNG files remain publication assets even where the generator introduced incidental pseudo-lettering, chart furniture or character-like elements. Those details are recorded as generation risks. The production prompts now constrain CLARIAH-AT to three codex zones, HEDIT to paper and bookbinding geometry, Uni for Life to a non-humanoid document-handling arm and VetMed to equine hoof lamellar tissue. The medieval prompt requires the selected cover as an identity reference for its agent figure.

**Outcome.** `docs/assets/covers/` contains the complete eight-image series, `docs/data/workshops.json` resolves every cover, the workshop profiles record the assets as present, and `knowledge/drafts/cover-image-prompts.md` holds the reproducible prompt contract for all images.

### 2026-08-22 — Naming of the material and of the knowledge documents

**Goal.** Remove two names the operator rejected, corpus for the teaching material and the labels Charter and Build Plan on the knowledge documents.

**Course.** Operator decision of 2026-08-22. Corpus keeps its technical sense of research data, which this line teaches on in the Hersch, Zweig and charter material. The teaching material is therefore called the material or teaching material, its holdings keep their names Full Slide Deck and Full Lecture Notes, and the relation of a workshop to it is a profile or a documented specialization; the recipe metaphor is retired with it. `project.md` carries the title Project and `plan.md` the title Plan, while the function keys Charter and Planning of the Promptotyping convention stay as keys in `INDEX.md`. The sweep covered the canonical documents, the platform pages and stylesheet hooks, the profiles, the coverage report, the module-cut headers and the drafts. Research-data uses of corpus stayed untouched, and the earlier entries of this journal keep their wording as provenance. The repository description on GitHub follows the same wording, and the naming rule is written into `CLAUDE.md`.

**Outcome.** Repository, platform and vault share one vocabulary of material, holdings, modules, profiles and instances.
