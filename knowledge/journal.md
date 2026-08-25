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
updated: 2026-08-25
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

### 2026-08-24 — KUG English specialization

**Goal.** Replace the provisional KUG profile with the confirmed four-session workflow and make every prepared teaching artefact English.

**Course.** The Wednesday session now uses Stefan Zweig Digital as the explanatory case for the route from a digitised estate object through metadata, TEI XML, data modelling, authority data, semantic links and repository ingest to a research platform. Thursday transfers that logic to M³GIM: large language model foundations and AI readiness lead into source-faithful transcription and schema-based extraction with Gemini, followed by Promptotyping a small research application from the checked structured data. A reduced question from the Mobility Studies keynote can guide the hands-on sequence once supplied. The existing English course reader was imported into the workshop folder. A native Google Slides copy of the research-infrastructure material supplied the visual basis for a new 45-slide KUG deck. Reused content was translated and adapted; visible German text from the copied title graphic was replaced with an English workflow diagram. The deck passed the automated output check with zero issues and was visually inspected after PDF export. The KUG register entry, landing-page card and workshop subpage now point to the English deck and course reader.

**Outcome.** The KUG specialization has one coherent English text and slide state ready for operator review. M³GIM digitisates with matching records, reuse confirmation, the reduced keynote question and the spoken teaching language remain external inputs.

### 2026-08-24 — KUG source-slide recovery and native reuse

**Goal.** Replace the newly composed KUG draft with a presentation that directly reuses the existing teaching slides.

**Course.** All 236 slides in the three Research Infrastructure decks, the Knowledge, Context and Agentic Engineering deck, and the Promptotyping deck were inspected. Sixty-three slides were selected and copied into one presentation before translation. The resulting sequence uses 29 slides for the Stefan Zweig source-to-platform workflow, 16 for LLM foundations and the transcription case, eight for the M³GIM extraction exercise, and ten for Promptotyping. English text replaced the instructional German while source transcriptions, identifiers, interface screenshots and bibliographic titles retained their documentary form. One embedded German pipeline diagram was redrawn with native English shapes. The local deck passed overflow and template-fidelity checks with zero issues. The native Google Slides import was checked through its outline and fresh thumbnails; three import-specific text shifts were corrected in place.

**Outcome.** The live KUG deck now contains 63 verified recycled slides with an exact source inventory. The earlier 45-slide presentation is superseded as a draft. User acceptance and the external M³GIM and keynote inputs remain open.

### 2026-08-24 — Bilingual workshop-page redesign

**Goal.** Make every workshop page usable as a compact teaching and reference surface.

**Course.** The operator found that the workshop structure, session sequence and module coverage repeated the same information. Design iteration 5 replaces these blocks with one overview containing the abstract, ordered outline and learning objectives. The live slide deck now occupies the first content position in an embedded Google Slides viewer, and an available course reader appears in an embedded Google Docs viewer below the overview. Missing artefacts keep the same position as a visible preparation state. Selected literature and references close the public content. Cover images, required project inputs, module coverage and provenance were removed from detail pages. The source-to-artifact motif was also removed from the landing page. Each of the seven registered instances now has a static English and German page pair connected through the header language control. Teaching language and material language remain explicit metadata and do not change with the interface language.

**Outcome.** Fourteen workshop pages follow one responsive and accessible template. The landing page and preparation guide also have English and German variants. The KUG and CLARIAH pages embed their registered slide decks and course readers. The remaining instances present stable placeholders until their artefacts exist. Local structural checks passed without findings. GitHub Pages published commit `c88d093` from `main/docs`; the English and German landing pages and both KUG variants returned HTTP 200, and the published KUG page contains its language control, slide viewer and course-reader viewer. Operator visual acceptance remains open.

### 2026-08-25 — Compact landing page and reduced navigation

**Goal.** Make the landing page a compact overview of the teaching line and let the teaching materials begin within the first screen.

**Course.** The operator approved a two-column hero with the title and a substantive abstract on the left and the five module titles on the right. Module subtitles, the separate module section and the hero repository link were removed. Teaching Materials now follows the hero directly, followed by Workshops and a compact Preparation entry linked to the full guide. The anchors for modules, material, workshops and preparation remain stable. Across the two landing pages, two preparation pages and fourteen workshop pages, GitHub is now the only content link in the top navigation. Language controls, language-matched brand links and existing backlinks preserve navigation between pages.

**Outcome.** Design iteration 6 defines the bilingual landing-page hierarchy and common chrome. The public files implement the compact responsive layout without JavaScript or decorative rules. Local structural, link and browser verification covers both languages, wide and narrow viewports; publication remains an operator action.

### 2026-08-25 — Workshop information order and downloadable slides

**Goal.** Present the workshop scope before the teaching artefacts and reduce metadata and licence wording.

**Course.** The operator placed abstract, outline and learning objectives directly after the workshop header. Slides now follow this overview. KUG and CLARIAH-AT expose their existing Google Slides PDF exports below the embedded viewer; both export addresses return PDF files. The browser-access warning was removed because the public embed is available in current Firefox and Edge installations as well as Chromium-based browsers. Workshop metadata now contains event, language and licence. The footer names Claude Code with Fable 5 and Opus 5, Codex with GPT-5.6 Sol, and Promptotyping as the context-engineering method. Licence text is the linked identifier `CC BY 4.0`.

**Outcome.** Fourteen workshop pages share the revised information order and metadata contract. The two available decks have direct PDF downloads, and all eighteen public pages carry the same production attribution and concise licence line.

### 2026-08-25 — Shared footer and stylesheet refinement

**Goal.** Make implementation provenance and repository access consistent without adding another navigation layer.

**Course.** The footer on all eighteen public pages now identifies Digital Humanities Craft, names the documented AI harnesses and Promptotyping, and links both the project repository and the Promptotyping repository with a restrained GitHub mark. The two-family type system remains unchanged. Unused motif, sequence and excerpt selectors were removed from the shared stylesheet, and the responsive footer layout was reduced to its active elements.

**Outcome.** Every public page carries the same compact provenance and repository contract. The change adds no script or external runtime dependency.

### 2026-08-25 — Landing-page terms and German module titles corrected

**Goal.** Correct the language switch and make the two central technical terms understandable at first contact.

**Course.** The German landing page now localises the descriptive module titles. Prompt Engineering and Agentic Engineering retain their established method names. The first references to Large Language Models and AI Harnesses use the full terms and link to two compact definitions beneath the module list. The definitions remain visible in the page flow and require no modal, tooltip or JavaScript.

**Outcome.** The two language versions now differ where interface language requires it and share the same explicit conceptual entry points.

### 2026-08-25 — Stylesheet cache mismatch corrected

**Goal.** Ensure that a newly published HTML structure cannot appear with a cached earlier stylesheet.

**Course.** The first deployment of the concept definitions reached the browser before its updated CSS. The page therefore displayed semantic definition-list markup with browser defaults. All eighteen public pages now reference one explicit version of the shared stylesheet. Future CSS changes require the same version update across the static page set.

**Outcome.** HTML and the design system now form one observable publication state across language and detail pages.

### 2026-08-25 — Concept definitions moved into inline tooltips

**Goal.** Keep the module column dedicated to navigation while allowing the term system to grow.

**Course.** The operator rejected the permanent definition cards because further terms would accumulate beside the module index. The cards were removed. Each marked term now carries its language-matched definition in an inline tooltip that appears on pointer hover, keyboard focus or touch. The trigger uses the text colour and normal weight. A thick underline in the associated module colour distinguishes the term from an ordinary hyperlink; the style can divide the line between two module colours for cross-module concepts. Native buttons and CSS provide the interaction without JavaScript.

**Outcome.** Further technical terms can use the same local pattern without enlarging the module column or creating a glossary block on the landing page.

### 2026-08-25 — Teaching resources and reusable setup tutorial

**Goal.** Give the two maintained teaching holdings distinct public entry points and turn preparation into a tutorial that remains useful across projects.

**Course.** Teaching Materials now contains equal cards for the Full Slide Deck and the Full Lecture Notes. New slide and notes marks use the existing line language and module palette on a completely white ground. Native English and German Google Docs were created from the maintained Markdown sources and passed structural inspection after import. Their public links remain withheld from publication until link-level viewing is enabled. The paired preparation pages no longer assign setup levels to workshops. They guide a reader through browser access, Visual Studio Code, Python, a local server and an AI harness in a disposable practice folder, with an observable check after every section. A second, short paragraph in each landing-page hero links directly to the language-matched tutorial. The first visible module title now uses quotation marks around `Understanding` and `verstehen` to keep Large Language Models as the shared technical term while exposing the intended semantic question.

**Outcome.** The local platform has language-matched lecture-note links, two context-specific material marks and a project-agnostic setup path. Publication still requires public read access to both Google Docs and final browser verification.

### 2026-08-25 — Preparation expanded into a beginner learning path

**Goal.** Make the reusable Preparation page sufficient for a participant who has not worked with an editor, terminal, local Python or an AI harness.

**Course.** The paired pages now distinguish chatbots from harnesses and compare Claude Code, Codex, Pi and OpenCode. One cumulative exercise opens a disposable folder in Visual Studio Code, explains the terminal and its working directory, verifies Python, generates a small HTML/CSS/JavaScript site and serves it on localhost. A named intermediate result makes the local environment independently testable before a harness is added. Claude Code, Codex and Pi have detailed first-run tutorials with read-only folder checks. The page exposes language-matched, dependency-free Python exercises and setup-assistant prompts as downloads. Windows and macOS/Linux commands remain separate, while Node.js, Live Server, Git and GitHub appear only where needed. Current product names, access routes and installation commands were checked against the official documentation.

**Outcome.** The local Preparation draft is project-agnostic, bilingual and executable from browser access through the first constrained harness interaction. Three anonymised screenshots remain an editorial input: the shared VS Code workspace, the generated localhost page and the read-only harness check.

### 2026-08-25 — Landing-page term marks and module alignment refined

**Goal.** Reduce the visual weight of the inline definitions and balance the two columns of the landing-page hero.

**Course.** The operator retained the semantic module colours and replaced the thick term marks with fine underlines. Tooltips now use a white ground, near-black text and a narrow accent in the associated module colour. The module index is vertically centred against the complete hero copy and shifted slightly toward the right edge on wide viewports. Narrow viewports keep the index below the abstract without the horizontal offset.

**Outcome.** Design iteration 8 carries a quieter concept layer while preserving the distinction between definitions and hyperlinks.

### 2026-08-25 — Lecture-notes language mark refined

**Goal.** Integrate the English and German indicators into the line mark without making them read as status badges.

**Course.** The two filled capsules were replaced by one white segmented capsule with a neutral outline and text. A small turquoise dot identifies English and a small violet dot identifies German. The component follows the language control used in the page chrome and remains legible at the resource-card scale.

**Outcome.** The Full Lecture Notes mark now presents both maintained versions as one visual unit.

### 2026-08-25 — Official Claude Code learning resources added to Preparation

**Goal.** Connect the first-run Claude Code tutorial with the official paths for continued study and persistent project instructions.

**Course.** The English and German Claude Code sections now link to the Claude Academy product page, Anthropic's terminal quickstart and the guide to `CLAUDE.md` and auto memory. The Academy begins with Claude Code 101 and continues into context files, workflows and reference material. The quickstart covers installation, authentication, a first session and the first inspected or changed project. The memory guide distinguishes user-written persistent instructions from Claude's own accumulated notes and documents the project-level `CLAUDE.md` location.

**Outcome.** Participants can continue from the local read-only setup check into Anthropic's maintained learning materials and establish concise project instructions that carry across sessions.

### 2026-08-25 — Public module-coverage badges removed

**Goal.** Remove an unexplained encoding from the workshop register.

**Course.** The operator rejected the three-state legend and then the numbered badge rows themselves. Filled, outlined and muted circles required readers to decode full, touched and absent states before the cards became useful. Both landing pages now present the workshop cards directly without module-coverage badges. Module selection remains documented in the workshop profiles and register data.

**Outcome.** The public workshop register contains only directly readable information. The shared stylesheet no longer carries the unused badge component or its state-specific colour tokens.

### 2026-08-25 — Pi introductory video connected to the setup path

**Goal.** Give beginners one direct video entry point for Pi while keeping the broader video sequence in the teaching playlist.

**Course.** The English and German Pi tutorials now link `What I Use Instead` directly beside the official Pi documentation. A second link routes further Pi videos through the accompanying playlist, so the first-run tutorial does not require a participant to locate its starting point inside a growing collection.

**Outcome.** Pi now has one explicit introductory video in the Preparation path and one route into the maintained sequence of additional videos.

### 2026-08-25 — Video Playlist established as the third teaching holding

**Goal.** Present the growing video sequence as a maintained route through the complete teaching line.

**Course.** The Video Playlist now stands beside the Full Slide Deck and Full Lecture Notes in the project contract, register and bilingual landing pages. Its resource card describes the progression from introductory explanations to specialised treatments of the five modules. The redundant Teaching Materials lead was removed, and a purpose-specific white-ground SVG connects a video surface with the five module colours. Individual videos remain linked at the tutorial step where they provide a concrete entry point.

**Outcome.** The three canonical teaching holdings are represented consistently in project knowledge, machine-readable register and public interface.

### 2026-08-25 — Material access and workshop release states

**Goal.** Make Full teaching material available through durable file formats, explain the relation between common material and workshop specialisations, and distinguish released workshop material from visible future instances.

**Course.** The operator required fixed Google, Markdown and PDF positions for the Full Slide Deck and both Full Lecture Notes languages. Final Markdown and PDF exports remain preparation states until their editorial release. The register now models Slide Decks and Lecture Notes through format objects and records workshop release separately from the event lifecycle. KUG and CLARIAH-AT carry released material; five later instances remain visible on a chronological timeline with desaturated covers, unlinked titles and explicit preparation labels. Event, language and licence scope form the common card metadata. The public licence statement covers the page and original text because complete Slide Deck licensing still requires an image-rights check. All workshop pages now use the canonical names Slide Deck and Lecture Notes in both interface languages.

The operator also reclassified the eight generated covers as placeholders. A visual audit retained the shared paper, ink and semantic-colour system while identifying new-generation requirements for CLARIAH-AT, Göttingen, Uni for Life and VetMed. The revised prompt contract excludes identifiable source surfaces and records the unresolved requirement for a VetMed case before generation.

**Outcome.** Design iteration 9 is installed in the local acceptance worktree. Desktop and narrow browser checks confirm three material cards, two released workshop cards, five preparation cards, one visible timeline and no horizontal overflow. Operator acceptance, final Full-material exports and cover generation remain open.

### 2026-08-25 — Teaching Materials cards compacted

**Goal.** Preserve the new Google, Markdown and PDF actions while correcting the excessive height of the three Teaching Materials cards.

**Course.** The operator retained the action-button concept and rejected the resulting vertical extent. Each card now places its line mark beside a compact title-and-description summary. Format actions use the full card width below that summary. Repeated Google labels are shortened visually while their accessible names retain the exact Slides or Docs destination. Pending labels use compact language-matched wording. Narrow-view padding was adjusted so all three format states remain on one row.

**Outcome.** The equal desktop cards measure 350 pixels high at the observed 1600-pixel viewport. At a 375-pixel viewport the three cards measure 243, 334 and 267 pixels, retain every action and produce no horizontal overflow. Stylesheet version `20260825-9` identifies this observable state.

### 2026-08-25 — Workshop dates moved onto the timeline rail

**Goal.** Make the workshop timeline structurally legible and remove repeated duration information from the cards.

**Course.** The operator identified that the timeline node and line lacked a convincing shared centre and that `16–17 September 2026 · two days` repeated information. Every workshop date now occupies a dedicated column to the left of the axis. Line and node use the same horizontal coordinate. One-day, two-day and five-day labels were removed. The Göttingen half-day hybrid format and the UNI for LIFE sequence of three two-hour units remain because their dates do not encode those details. Narrow viewports place the date above the card while retaining the same rail.

**Outcome.** Both landing pages contain seven dates outside the cards and no residual card stamps. Desktop and 375-pixel browser checks show centred nodes and no horizontal overflow. Stylesheet version `20260825-10` identifies this state.

### 2026-08-25 — Claude Code installation video added

**Goal.** Give participants a direct audiovisual route through Claude Code installation.

**Course.** Both Preparation pages now link the video `Installing Claude Code` from the Claude Code tutorial. The canonical YouTube short URL omits the supplied sharing parameter. The official quickstart, Visual Studio Code tutorial and Claude Academy path remain adjacent references.

**Outcome.** English and German participants can open the same installation walkthrough at the step where Claude Code is introduced.

### 2026-08-25 — Preparation rebuilt as a scrollable learning sequence

**Goal.** Give beginners continuous chapter access while presenting each setup concept beside an observable working state.

**Course.** The paired Preparation pages now contain fourteen content-driven panels. Each panel places a stable visual state beside its definition, actions and check. The linear path runs from browser access through the local workspace, terminal, Python and localhost before branching to Claude Code, Codex or Pi. A persistent sidebar links every step on wide viewports. Narrow viewports retain the same links as a sticky horizontal rail and stack the visual above its explanation. HTML and CSS interface diagrams represent the stable learning states while the planned anonymised screenshots remain unavailable. The platform contract remains static and requires no JavaScript.

**Outcome.** Desktop checks at 1440 by 900 pixels and narrow checks at 390 by 844 pixels confirm working anchor jumps, persistent navigation and no page-level horizontal overflow in either language. Stylesheet version `20260825-11` identifies this local acceptance state.

### 2026-08-25 — September workshop cards held in preparation

**Goal.** Keep KUG and CLARIAH visually pending before their September dates while preserving the prepared teaching artefacts.

**Course.** The operator withheld the landing-page release of both September workshops. Their register entries now use `materials_status: in_preparation`. Both language versions show desaturated, unlinked cards with a preparation label and no material actions. The direct workshop pages and the registered Slide Deck and Lecture Notes addresses remain intact for later editorial release.

**Outcome.** All seven upcoming workshops currently use the visible preparation state. Releasing KUG and CLARIAH in September requires one coordinated register and bilingual landing-page update.

### 2026-08-25 Preparation panel rhythm refined

**Goal.** Reduce unused vertical space in the tutorial while retaining its scrollable panel structure and persistent navigation.

**Course.** Wide panels now align their visual and explanation columns at the top. Their minimum height uses a capped responsive range, while dense sections expand to their content. The shared mock-window bar generates its three decorative controls from one element, and the setup assistant is represented as a content section in both language versions.

**Outcome.** At 1600 by 1000 pixels the English document height fell from 11,764 to 10,898 pixels and the German document height from 12,032 to 11,209 pixels. Both pages retain fourteen panels, sticky navigation, clear narrow-view anchor targets and no page-level horizontal overflow. Stylesheet version `20260825-12` identifies this local acceptance state.

### 2026-08-25 Claude Code subchapter distilled

**Goal.** Develop the supplied Claude Code material into a coherent applied subchapter of Agentic Engineering.

**Course.** The operator supplied an automatic webinar transcript, a conceptual knowledge document and five slide montages. The material was compared with the Full Slide Deck, both Full Lecture Notes and the current official Claude Code documentation. Product claims about instruction loading, context compaction, Plan Mode, intervention and data retention were corrected before reuse. A draft now separates a nine-slide conceptual talk sequence from volatile reference material and connects the first-run check with the maintained Preparation tutorial.

**Outcome.** `knowledge/drafts/claude-code-agentic-engineering-subchapter.md` contains the proposed placement, exact slide claims, speaker notes, visual briefs and editorial decisions. The canonical slide export and Full Lecture Notes remain unchanged pending operator acceptance.

### 2026-08-25 DHCraft destination and imprint made explicit

**Goal.** Connect the teaching platform's shared identity directly with the public DHCraft site and expose its legal information consistently.

**Course.** The brand in every public header now links to `https://dhcraft.org`. Local detail pages retain their language-matched backlinks into the teaching platform. Every public footer adds a language-matched Imprint or Impressum link to the canonical page at `https://dhcraft.org/imprint`. The existing footer layout supports the additional link without a stylesheet change.

**Outcome.** All twenty public pages contain one external DHCraft brand destination, one canonical imprint link and the same stylesheet version.

### 2026-08-25 Claude Code introduction and delegated research route added

**Goal.** Separate shared environment setup from a focused Claude Code introduction and incorporate the operator's use of Subagents for bounded research.

**Course.** Preparation retains installation and the first read-only check and now links a bilingual Claude Code tutorial. Thirteen panels connect the AI Harness model with working modes, `CLAUDE.md`, Context Management, screenshot verification, MCP, Skills, Plugins and Subagents. The Subagents panel explains delegation from a known direction into a precise question, source frame and return format. Each delegated investigation receives a fresh isolated context; findings return to the main agent for comparison, integration and verification. The editorial slide proposal gained one extension-map slide and one Subagents slide, expanding the sequence from nine to eleven slides.

**Outcome.** The new page pair is installed locally as a navigable introduction and deepening hub. The canonical Full Slide Deck and Full Lecture Notes remain unchanged pending operator acceptance of the slide proposal.

### 2026-08-25 Claude Code coordination routes and UI audit integrated

**Goal.** Evaluate the supplied UI specification against the current platform contract and incorporate the further Claude Code introduction material without importing transcript errors or external slide layouts.

**Course.** The UI specification was treated as a delta catalogue. Compatible ideas include shared metadata roles, canonical status wording, medium-based resource taxonomy and broader accessibility checks. A separate `DESIGN-SYSTEM.md`, abbreviated dates, universal card links, longer Google labels, hero realignment and automatic page generation conflict with existing decisions or the static platform contract and were not installed. The accompanying `UI-DESIGN.md` was later consolidated into a new interface contract in `knowledge/design.md`. That contract records the implemented type roles, spacing and breakpoints, interaction roles, card families, accessibility behaviours and data sources while rejecting its stale point-only module marks, material matrix and card-wide workshop links. `knowledge/design.md` remains the canonical design reference. The second automatic webinar transcript was checked against the official Claude Code documentation. Existing MCP, Skills, Plugins, Context Management and Subagent explanations were refined. Parallel sessions with Worktree isolation and Remote Control were added as distinct tutorial panels. The eleven-slide conceptual sequence remains stable; its extension slide now presents orthogonal functions, and optional reference material distinguishes Context strategies, sessions, Worktrees and remote execution surfaces.

**Outcome.** Both Claude Code tutorials now contain the same fifteen panels and six deepening routes. Structural and browser checks confirm paired IDs, resolving anchors, sticky navigation and no horizontal overflow at 1600 by 1000 and 390 by 844 pixels. The canonical Full Slide Deck and Full Lecture Notes remain unchanged pending operator acceptance.

### 2026-08-25 Module notation extended across workshops and videos

**Goal.** Reuse the five subject-specific module symbols wherever the platform identifies the content taught in a workshop or video.

**Course.** Five portable line icons now encode the module concepts through subject-specific relations: a jagged capability boundary inside a black box, a selected coordinate in latent space, maintained documents with a context aperture, coordinated agents inside a tool-bearing harness, and a claim inspected before an authorisation gate. The register records one ordered module subset per workshop. Landing cards and detail-page headers expose that subset as a compact icon-plus-number row without coverage states or a legend. A separate video register records all 34 public playlist entries with stable identifiers, titles, durations and one primary teaching module. The landing pages group the same entries in native disclosure sections and preserve playlist order inside each group. YouTube previews remain external and the interface discloses the request before a reader opens a group.

**Outcome.** Design iteration 16 establishes one portable module notation across the hero, seven workshop profiles and the bilingual video library. The current video groups contain 4, 1, 6, 21 and 2 entries for modules 01 to 05.

### 2026-08-25 Preparation accessibility and publication boundary completed

**Goal.** Make the tutorial structure keyboard-accessible and keep historical interface experiments outside the published GitHub Pages tree.

**Course.** Every public page received one language-matched bypass link to a unique main-content target. Tutorial sidebars now mark the addressed fragment, and the three harness tutorials are labelled as alternatives that rejoin at one final check. Requirements, localhost and optional Git gained observable checks. Code-built product surfaces identify themselves as schematic. The Codex path now includes the official OpenAI Academy bootcamp route. Adjacent visible brand text supplies the accessible name for decorative header and footer logos. Six superseded HTML prototypes moved from `docs/` to `knowledge/drafts/platform-prototypes/`, where a short readme records their historical function.

**Outcome.** The published tree contains only the twenty maintained public pages. Both Full Lecture Notes documents and the Full Slide Deck PDF export were anonymously readable during the local verification pass; final Markdown and PDF release files remain separate operator inputs.

### 2026-08-25 Official Codex bootcamp evidence mapped

**Goal.** Determine whether the OpenAI Academy recording provides a transcript or other reusable source material for the Codex introduction.

**Course.** The public recording page exposes no maintained transcript and its embedded data reports a null transcript value. The embedded player supplies one English auto-generated subtitle track, which can locate topics but does not constitute an edited word record. The official event page adds four learning objectives and a public 31-page slide deck. The slide deck supports topic verification but carries a rights notice that does not support republication in this repository. The official series page positions the recording as the introductory part of a three-level bootcamp sequence. Dates differ across the public surfaces and were left unnormalised.

**Outcome.** `knowledge/drafts/codex-bootcamp-101-evidence.md` records the official sources, a caption-supported content map and a six-part deep-dive structure. The public Codex Preparation path links the recording, while any later teaching text must be written independently and verified against playback.

### 2026-08-25 About page and accessible workshop routes added

**Goal.** Explain the commercial and editorial conditions of the public material and restore access to every workshop information page.

**Course.** Paired About pages state that commissioned workshops finance research, example development, editorial revision, technical implementation and maintenance. Generally applicable results return to the shared teaching material. The text identifies DHCraft as a company and avoids charitable or promotional framing. About or Über now precedes GitHub in the shared header and appears in every footer. All seven workshop titles link to their language-matched information pages even while material actions remain in preparation. Compact module rows link each icon and number to the full language-matched module title and provide the same title to assistive technology. Secondary text colours were darkened, touch targets and focus states were strengthened and the About article uses the 60-character reading measure.

**Outcome.** The maintained public surface grows from twenty to twenty-two bilingual HTML pages. Material release remains visually distinct from access to workshop information.

### 2026-08-25 Web-native teaching and deep-dive model distilled

**Goal.** Integrate the proposals for web-native slides, product introductions, research-data depth and a personalised archive workflow into one teaching architecture.

**Course.** The model separates five stable core modules from optional deep dives, situated cases, executable tutorials and event-specific workshop profiles. Research Data and Knowledge Work is proposed as the first conceptual deep dive across modules 03 to 05. A research-data curator moving digitised estate material toward a repository package becomes an applied case beneath it. The case distinguishes representation states, executable validation, source-based verification and responsible acceptance. It uses original schematics or synthetic material because public facsimile reproduction remains outside the repository rights boundary. A separate web-slide grammar derives typography, colour and responsive behaviour from the platform while preserving the difference between a content-driven tutorial panel and a controlled 16:9 presentation slide.

**Outcome.** `knowledge/drafts/web-native-teaching-and-deep-dive-architecture.md` contains the complete content model, critical risk analysis, rights boundary, ten-slide research-data pilot, cross-audience adaptation and open editorial decisions. The proposed architecture remains a draft and does not yet replace the current Google Slides contract.

### 2026-08-25 Research Mission Control adopted beside Promptotyping

**Goal.** Give the project a documented orchestration contract beside its artefact method and make every contribution required from the Research Director visible in one place.

**Course.** The Research Director decided that two complementary methods carry the work. Promptotyping develops the artefacts, so the maintained documents in `knowledge/` guide production, inspection and correction. Research Mission Control coordinates authority, so the Research Director accepts substantive decisions, the Research Orchestrator frames research and issues bounded implementation briefs, and the Operational Orchestrator coordinates implementation, terminal verification, integration and release. Bounded subagent lanes inherit only the authority, write boundary, exclusions and verification criteria of their brief. A first supplement had extended the change set to `AGENTS.md` and `knowledge/handoff.md`. The correction of the same day reduced it to the smallest consistent set, left `AGENTS.md` structurally untouched because it already delegates the whole action contract to `CLAUDE.md`, and left `knowledge/handoff.md` a process inbox without a permanent method description. The older label Critical Expert (operator) survives in `governance.md` as the acceptance function of the Research Director and carries no separate authority. `communication/` is documented as transport for briefs, results and recipient state, while `knowledge/` stays the canonical project memory.

The same round installed the Research Director Log at `communication/research/director-log.md` with sixteen deduplicated contributions under the stable identifiers RD-001 to RD-016, ten of them open and six waiting on a stated trigger. Each entry carries its type, status, smallest concrete contribution, recommendation or the marker that evidence is still pending, its basis, its effect and its canonical write-back target. The communication contract was fixed with it, four products from a direct answer through a situation report and a Research Director Point to an acceptance sheet, an explicit separation of draft, active installation, formal validation, observed function, substantive review and Research Director acceptance, and separate statements for installation, validation, observed function, commit, push and deployment.

**Outcome.** `README.md`, `CLAUDE.md`, `knowledge/project.md`, `knowledge/governance.md`, `knowledge/INDEX.md`, `knowledge/specification.md`, `knowledge/plan.md`, `communication/INDEX.md` and `communication/PROTOCOL.md` describe one role model. `CLAUDE.md` carries the compact trigger and points to the protocol for the rest. Every request for a Research Director contribution is derived from the log, and this journal receives the provenance once a contribution has been written back and verified.

### 2026-08-25 Iteration 16 reconciled with the verified release state

**Goal.** Bring the canonical knowledge base in line with what the working tree actually contains before the release commit.

**Course.** The public set grew to twenty-two paired pages when the bilingual About pages entered the platform, and the accessibility refinement restored the information link of all seven workshop titles while their material stays in preparation. The shared stylesheet moved to version `20260825-17`, which every public page references. The landing-page Preparation copy was replaced by one purpose-oriented sentence per language. It states that the tutorial prepares a participant for taking part in a workshop, and the inventory of browser access, local tools and AI harness stays inside the guide. The compact Preparation section near the end of each landing page carries the same wording. `knowledge/design.md` records the interface state and stays free of the orchestration method, `knowledge/specification.md` carries the requirement and the acceptance criteria for that copy and for the durable `communication/` contract, and `knowledge/plan.md` records the About page and the Research Mission Control installation as complete work packages.

**Outcome.** Structural verification on the current tree found twenty-two public HTML pages, each referencing `site.css?v=20260825-17`, seven workshop information links in each landing page, 136 resolving module links, and 34 video entries in the register and in each landing page, grouped 4, 1, 6, 21 and 2 by primary module. Ten module and material SVG files parse as XML, the shared stylesheet keeps balanced braces at 410, both JSON registers parse, every public page carries its skip link, and no published URL contains a tracking or sharing parameter. `git diff --check` passes with only the known line-ending notices. Browser behaviour at desktop and 390-pixel widths remains the observation recorded for the earlier iteration-16 pass, because this reconciliation added no new browser evidence.

### 2026-08-25 Holding roles, video contract, navigation and footer written back

**Goal.** Carry five Research Director decisions of the same day into the canonical documents so that the knowledge base states one contract for the teaching holdings, the video library, the site navigation and the shared footer.

**Course.** The first decision replaced counting with function. The Full Slide Deck is the complete overview in slide form, a reference work and the source from which workshop-specific decks are assembled, and it is not presented as one teaching session. The Full Lecture Notes are the written-out counterpart of the slides and carry the explanations and context needed for reading and later reference. The Video Playlist combines DHCraft videos with selected contributions by others in a deliberate sequence from the foundations to more complex topics, curated, maintained and extended as suitable material appears. Its correction added the point that `knowledge/project.md` had claimed the maintained text lives exactly once. The slide deck and the lecture notes deliberately express the same concepts at different levels of expansion, so the claim was replaced by responsible layers, the slide deck maintaining the reference structure and the selection surface for workshop decks, the lecture notes maintaining the expanded explanation, and a shared conceptual change being reconciled across both before any specialised export is regenerated.

The second decision corrected the video contract. `docs/data/videos.json` keeps `module` as the required primary classification and gains an optional `related_modules` array for a documented cross-module relation. A video renders exactly once, under its primary module, and a related module may surface as quiet metadata where the card carries it without materially growing in height. `Research Mission Control: Eine Forschungsleitstelle mit mehreren KI-Agenten` moves to primary `04` with related `03`, and `Just Go Local Solves Nothing. Here's What Does` moves to primary `01` with related `05`, which produces the expected primary distribution `5/1/6/22/0` across the unchanged 34 entries. Module 05 keeps its disclosure group, icon, number and title with a count of zero and states honestly that no playlist video is currently curated primarily for it, because its own selection of external sources enters the inventory only after the maintained external playlist contains it. The preview-loading disclosure becomes conditional on a group containing videos, and `Context Engineering` is written with a capital `C` in every public occurrence.

The third decision made the setup tutorial a central route. The binding top-navigation order became Preparation, then the combined About and Imprint entry, then GitHub. The About pages became that combined local entry and gained a fifth metadata field for the canonical legal notice. The local entry and the canonical legal text stay separate, because the binding legal copy remains on `dhcraft.org` and cannot then drift between two sites. Within the site navigation only the Preparation pages mark the Preparation link as the current page and only the About pages mark the combined entry, while the language control keeps its own state.

The fourth decision reduced the shared footer to three compact groups, publisher identity, one provenance sentence and a compact navigation carrying the combined About and Imprint entry, the teaching-material repository, the Promptotyping repository, the Research Mission Control repository, the licence identifier and the canonical legal notice. The provenance sentence names Digital Humanities Craft with Promptotyping and Research Mission Control and drops every model name and version, because a public page cannot carry the date at which such a version was true. The detailed dated tool and model provenance stays in this journal and in the `generated-with` field of the knowledge documents, which is now stated in `knowledge/governance.md`.

The Research Director also sharpened the division of ownership for this thread. Research owns investigation, source evaluation and new knowledge syntheses. Operations owns implementation, transfer into the interface, technical verification, git integration and deployment. This pass therefore wrote the canonical contract and left `docs/**`, `AGENTS.md`, `knowledge/INDEX.md`, `knowledge/plan.md` and `communication/**` untouched.

**Outcome.** `README.md`, `CLAUDE.md`, `knowledge/project.md`, `knowledge/governance.md`, `knowledge/design.md` and `knowledge/specification.md` carry the four contracts, and four dated decisions were appended to the decision list in `knowledge/specification.md`. `knowledge/handoff.md` stayed a process inbox and received only corrections to stale release facts, twenty-two public pages instead of twenty, stylesheet version `20260825-17` instead of `20260825-12`, the restored information link on every workshop card, and the removal of the resolved question about publishing `docs/drafts/`, whose prototypes now live under `knowledge/drafts/platform-prototypes/`.

Operations installed the interface side of the same four decisions during this pass, so the write-back describes an implemented state rather than a pending one. Verified on the current tree, the public set is twenty-two HTML pages, each referencing `site.css?v=20260825-17`, with unique document ids, one `h1`, a skip link, resolving internal anchors and local targets, and no tracking parameter. The video register holds 34 unique ids in the unbroken index sequence 1 through 34 and the primary distribution `5/1/6/22/0`; `-j4shkNnYVw` carries related module `05` and `B7TCJjcVA2k` carries related module `03`; every id appears exactly once in each language, and Module 05 renders its language-matched empty state. No lowercase spelling of Context Engineering remains anywhere in the public tree. Every site navigation carries the three required links in order at the correct directory depth, with one current-page mark on the Preparation and About pages and none elsewhere. Every footer exposes the three groups, all three repository destinations, `CC BY 4.0` and the canonical legal notice, and none names a model or version. Both About pages carry the combined heading, four editorial sections and the five-field metadata list. Both JSON registers parse, the stylesheet keeps balanced braces at 414 and `git diff --check` reports no whitespace error. Browser rendering at the required widths was not re-observed in this pass and remains an Operations statement.

One delta goes back to the Research Director. The footer destination `https://github.com/chpollin/forschungsleitstelle` returned HTTP 404 to an anonymous client on 2026-08-25, which is consistent with a private repository, while `README.md` links `https://github.com/DigitalHumanitiesCraft/research-mission-control`, which returned HTTP 200. The contract records the instructed destination, the installed footer already uses it, and the README link was left in place, so the two references stay visible as one open question instead of being silently harmonised. The destination has to resolve publicly, or the two references have to be reconciled, before the footer link goes live.

### 2026-08-25 Video Library presentation accepted

**Goal.** Settle whether the installed Video Library is finished design or an iteration still open for revision.

**Course.** The Research Director accepted the current presentation directly. The acceptance covers the native module disclosure groups, the thumbnail cards and the resulting overall visual impression, so this presentation is settled and is not reopened by a later iteration without a new decision. Only the content corrections already integrated were admissible under it, and no further visual change to the library was authorised in the same step. Those admissible corrections are the primary distribution `5/1/6/22/0` across the unchanged 34 entries, the two `related_modules` records on `-j4shkNnYVw` with related `05` and `B7TCJjcVA2k` with related `03`, and the honest empty state of module 05, which keeps its group, icon, number and title with a count of zero and says that no playlist video is currently curated primarily for it.

**Outcome.** `docs/data/videos.json` holds 34 unique ids and the accepted primary distribution `01: 5`, `02: 1`, `03: 6`, `04: 22`, `05: 0`. Both landing pages render 34 video cards each inside five native disclosure groups, and both carry the language-matched module 05 statement. `knowledge/design.md` records the acceptance in its iteration status, and this entry is its durable provenance.

### 2026-08-25 Site identity, three teaching surfaces, licence copy and adjacent sources written back

**Goal.** Carry four further Research Director decisions of the same day into the canonical documents, and state for each of them whether it is installed or authorised and still pending.

**Course.** The first decision separates the publisher mark from the teaching-site identity. The header receives one site-identity group with two adjacent links that have distinct destinations and distinct accessible names. The compact DHCraft logo becomes the only header element leading to `https://dhcraft.org`, and its accessible name identifies the publisher website in the page language. Beside it the complete teaching-line title becomes the visible site name in both interface languages and returns to the language-matched landing page, resolved at the depth of its own directory. The visible wordmark `Digital Humanities Craft` leaves the header, because the accessible name of the logo and the publisher block of the footer already carry publisher identity. Both links stay separate keyboard stops with their own visible focus and at least 44 pixels on coarse pointers, and the title wraps to a second line rather than being shortened to an unexplained acronym. The reason is an interaction defect in the installed header, where the visible site name currently sends a reader to `dhcraft.org` instead of to the teaching platform. This decision also corrects an accessibility statement that had been true only for the old markup, because a header logo without adjacent visible brand text can no longer be decorative and needs its own accessible name, while the footer logo stays decorative beside its publisher block.

The second decision fixes three surfaces per workshop instance with distinct functions inside one URL. The Web Module is the primary browser-native learning sequence and sits between the overview grid and the Slide Deck; the Slide Deck stays the editable presentation and delivery surface; the Lecture Notes stay the expanded reading form for reference and later review. The Web Module reuses the reading model of the Preparation pages, works without JavaScript, needs no external embed and never wraps a Google viewer, and its text is newly written from the workshop profile and the Lecture Notes while its visuals stay rights-safe original diagrams or synthetic file and data states. The KUG instance carries the pilot with its five units, from estate object to research platform, model-supported tasks inside the research-data workflow, source to checked structured data, research question to browser application, and verification and responsible acceptance. The register gains a workshop-level `web_module` status, `available` for `2026-09-16-kug-m3gim` and `in_preparation` everywhere else, and that field stays separate from `materials_status`, because the existence of a detail page says nothing about a finished learning sequence.

The third decision reduces the visible licence on public cards to the linked identifier `CC BY 4.0`. The exact scope `page-and-original-text` stays in `docs/data/workshops.json`, in `knowledge/governance.md` and in the rights explanation of both About pages, where a reader can take it in full. A compact metadata surface cannot carry a rights statement of that kind without crowding the card.

The fourth decision orders the relation to two adjacent DHCraft teaching projects. `DigitalHumanitiesCraft/ai-coding-literacy` remains an independent published German-language curriculum with its own rights, deployment and dataset contracts and is reached as an external specialised deep dive; its seven competencies never replace the five modules of this line. The local folder `DHCraft/ai-literacies` is an unversioned Astro prototype without publication status and remains read-only migration input, so Astro, npm dependencies, TypeScript, `node_modules`, its source CSS tokens, its build configuration and its root-relative route system stay outside this repo and the platform keeps its no-build static publication contract. Migration is ordered. The Prompt Engineering unit is the first candidate and starts only after the KUG Web Module component has passed its acceptance criteria, and the Tools, Multimodal, Administration Data Analysis and Research Data Analysis units wait for the verified VetMedAI intake, because their product facts, model claims, data-protection statements and rights boundaries need re-verification. Publicly this becomes a compact Deep Dives route after the three teaching holdings and before the workshop timeline, with `AI Coding Literacy` as the first released entry, the local Claude Code tutorial as the product-specific Agentic Engineering entry, the Research Data and Knowledge Work deep dive as a visible preparation state, and no listing of the unversioned prototype.

The same round recorded the three Research support lanes authorised on 2026-08-25 as read-only, the contract audit, the browser acceptance pass and the VetMedAI source intake, and it recorded that terminal integration stays closed until the contract audit reports a named blocker finding or the absence of blockers.

**Outcome.** `CLAUDE.md`, `knowledge/project.md`, `knowledge/governance.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/plan.md` carry the four contracts, four dated decisions were appended to the decision list in `knowledge/specification.md`, and `knowledge/handoff.md` was reduced to the current working situation and the integration gate. All four contracts are authorised and pending installation, and the working tree was verified as carrying the superseded state for each of them. Every public header still holds the single brand anchor with the visible text `Digital Humanities Craft` linking to `https://dhcraft.org`. Both landing pages still print the licence scope beside the identifier, seven times each in the English and the German file. `docs/data/workshops.json` contains no `web_module` key, and no workshop page contains a Web Module. Neither landing page carries a Deep Dives route. This pass wrote canonical knowledge only and left `AGENTS.md`, `README.md`, `communication/`, `docs/` and every draft untouched; implementation, transfer into the interface, technical verification, commit, push and deployment stay with Operations.

### 2026-08-25 v0.2 interface installed and formally validated

**Goal.** Reconcile canonical knowledge with the installed v0.2 working-tree state while preserving the distinction between installation, formal validation, browser observation, Research Director acceptance and release.

**Course.** Operations installed the separate site-identity links across all twenty-two public pages, simplified the landing-card licence display to the linked `CC BY 4.0` identifier, added an explicit `web_module` state to every workshop record and placed the paired five-unit KUG Web Module before the Slide Deck and Lecture Notes. Both landing pages gained the compact three-entry Deep Dives or Vertiefungen route, identifying AI Coding Literacy as external, the language-matched Claude Code tutorial as local and Research Data and Knowledge Work as in preparation. The copy-and-density refinement replaced the compact Video Playlist wording in both languages, aligned the five-row module index, changed every workshop overview to Abstract, Learning objectives or Lernziele, then Outline or Ablauf, reduced every reference section to one bounded reading column and gave the shared footer a quiet tinted separation, compact spacing and the visible navigation label `Further links` or `Weiterführende Links`.

The Research correction superseded the private Research Mission Control route. Every active action and declarative contract now uses `https://github.com/DigitalHumanitiesCraft/research-mission-control`, and the public tree contains forty-four occurrences of that destination and none of the private route. The earlier journal paragraph remains the dated account of the discrepancy that triggered the correction; this entry records its resolution. Immutable historical briefs remain unchanged.

**Outcome.** Deterministic checks found twenty-two HTML files in eleven language pairs on stylesheet version `20260825-18`, twenty-two `site-identity` groups, seven `web_module` records, the same five KUG unit ids in both languages, no landing-card scope suffix, the exact compact playlist wording in both languages, the bilingual three-entry Deep Dives route, the required overview order in all fourteen workshop pages, one semantic reference list per workshop page and the language-matched footer label on every page. Both JSON registers parse, CSS braces balance, local identifiers and targets resolve, and the ten module-and-material SVG files parse as XML. This establishes active installation and formal validation only. The required browser observations have not been completed, the Research support contract-audit disposition has not returned, and RD-017, RD-018 and RD-020 remain waiting. No v0.2 commit, push or deployment is claimed.

The static Prompt Engineering migration remains in preparation because no lesson exists. The Module 00 and module-hub brief remains a later v0.3 milestone that may begin only after a separate verified v0.2 commit and push.

### 2026-08-25 Module 05 playlist sequence installed

**Goal.** Synchronise the public Video Library with the seven Module 05 sources added to the maintained playlist and preserve the Research Director's revised progression from introduction to specialisation.

**Course.** The immutable Research brief established the seven ids, source titles, durations and primary Module 05 assignment. The Research Director then supplied the maintained playlist's revised order directly: Californian ideology, the technology-billionaire worldview, digital control, the short cybernetics introduction, the retrospective on 2026 AGI forecasts, Toby Ord's critique of AGI timelines and the AI-investment-race analysis. This direct ordering decision supersedes only the index order in the earlier brief. The accepted disclosure, card and thumbnail design remains unchanged.

**Outcome.** `docs/data/videos.json` now contains 41 unique ids in the unbroken sequence 1 through 41 with the distribution `01: 5`, `02: 1`, `03: 6`, `04: 22`, `05: 7`. Both landing pages render the same seven Module 05 cards once and in the revised maintained-playlist order. The former empty-state markup and CSS are removed. `knowledge/drafts/critical-perspectives-and-governance-source-map.md` records the accepted sequence and its didactic transition from broad political and cybernetic frames to specialised AGI disputes.

### 2026-08-25 v0.2 released and observed on GitHub Pages

**Goal.** Preserve the installed v0.2 platform as an independently reproducible release before the Module 00, Module Hub, Curated Skills and Harness Introduction architecture changes the public topology.

**Course.** Operations repeated the terminal contract checks against the complete release scope. All twenty-two public pages passed HTML validation; their ids, local files and fragments resolve; both JSON registers parse; CSS braces balance; and the ten material and module SVG files parse as XML. The video register contains forty-one unique entries with the distribution `5/1/6/22/7`, and Module 05 follows the Research Director's maintained introductory-to-specialised order. Operations observed the representative component families at 1440, 1020, 860, 780, 640, 390 and 320 pixels without page overflow, broken images or console warnings or errors. The independent Research support lane supplied a second observation at the same widths. Coarse-pointer behaviour remains static CSS evidence because the browser did not emulate that input mode.

The release-boundary clarification kept `docs/assets/routes/`, the Harness Introduction, Harness Route Icon and Curated Agent Skills drafts, and their new Research messages outside the commit and tag. The immutable Research messages included in the v0.2 transport retain their published bytes, including existing trailing blank lines, while the mutable integration surface passes `git diff --check`.

**Outcome.** Commit `0e285e74caa83356e4481936d2e2fe31cf34fbc0` carries the v0.2 state and the annotated tag `v0.2`. `origin/main` and the remote tag resolve to that commit. GitHub Pages build `1174871991` completed for it. Anonymous cache-bypassed requests to both landing pages, the KUG workshop page and the About page returned HTTP 200 and delivered stylesheet version `20260825-18`, the canonical public Research Mission Control URL, the seven Module 05 videos and the five-unit KUG Web Module. Installation, formal validation, observed function, commit, push and deployment are therefore evidenced separately. RD-017, RD-018 and RD-020 remain substantive Research Director acceptance points.

### 2026-08-25 v0.3 architecture installed, formally validated and browser-observed

**Goal.** Integrate Module 00, the five bilingual subject hubs, grouped Learning Routes, the comparable Harness introductions and the Module 04 Curated Skills area as one coherent v0.3 pre-release state after the independently published v0.2 baseline.

**Course.** Operations preserved the no-build and no-JavaScript contract while extending the public tree to thirty-six HTML files in eighteen reciprocal language pairs. Preparation now carries Module 00; `docs/modules/` contains ten language-matched hub files; module markers across landing, workshop, Web Module and Video Library surfaces lead to the corresponding hub. Claude Code, Codex and Pi expose the common sequence `goal`, `prerequisites`, `install`, `workspace`, `instructions`, `permissions`, `extensions`, `first-check`. Module 04 contains eight Curated Skills references per language, including visible source and review fields. Module 05 retains the accepted seven-video sequence. All thirty-six pages use stylesheet cache version `20260825-19`, and every public occurrence uses the canonical `Context Engineering` spelling.

The terminal contract check found thirty-six pages, eighteen reciprocal pairs, ten hubs, the required hub heading order, one current item in every six-entry module navigation, resolving local files and fragments, unique identifiers, parseable JSON and SVG, balanced CSS and no private Research Mission Control route on active public or canonical surfaces. HTML validation passed with the four documented project exceptions and an active `aria-label-misuse` rule. The five hub-header marks use their module SVG as a CSS mask so the original `currentColor` geometry renders in the module colour. The 320-pixel correction gives Skill metadata a shrinkable width and an explicit emergency wrap without changing the correctly encapsulated horizontal module navigation.

Operations observed representative landing, Module 00, subject-hub, Harness and KUG component families at 1440, 1020, 860, 780, 640, 390 and 320 pixels. The final tree showed no page overflow, broken image or browser-console message. Research independently repeated the structural, accessibility and responsive checks and confirmed the corrected Module 04 German page at 320 pixels with no document or Skill overflow and an empty console. Coarse-pointer support remains static CSS evidence because the browser matrix did not emulate that input mode.

**Outcome.** Active installation, formal validation and observed browser function are evidenced for the v0.3 working tree. Git commit, annotated tag, push, GitHub Pages deployment and substantive Research Director acceptance remain open and require their own evidence. RD-021, RD-022 and RD-023 remain waiting at the requested pre-commit checkpoint.

### 2026-08-25 v0.3 released and observed on GitHub Pages

**Goal.** Preserve the validated Module 00, Module Hub, Harness Introduction and Curated Skills architecture as a reproducible public release and keep technical release evidence separate from substantive acceptance.

**Course.** Research returned 70 of 70 final browser observations without overflow or console messages and authorised the release. Operations committed the complete thirty-six-page state, created the annotated `v0.3` tag, pushed `main` and the tag, and waited for the matching GitHub Pages deployment. GitHub Actions run `32892116537` completed successfully for the release SHA. The Pages API reports the same commit as `built`. The workflow carried one non-blocking GitHub-owned action annotation about forcing `actions/upload-artifact@v4` from its deprecated Node 20 target onto Node 24; its build and deployment jobs both succeeded.

Operations then requested the landing page, Module 00, Module 04, all three Harness introductions and the KUG workshop page anonymously with cache-bypassing query values. All seven routes returned HTTP 200 and contained the expected v0.3 markers: stylesheet version `20260825-19`, the Module 00 and Module 04 destinations, the shared `first-check` landmark and the five-unit KUG Web Module.

**Outcome.** Commit `aa4193378413a9723a2144d155b186b933229435` carries release v0.3. Annotated tag object `469bb81025a870e49f10eed919fa9a149c413a7d` peels to that commit locally and on `origin`; remote `main` resolved to the same commit at release. Installation, formal validation, browser observation, commit, tag, push and deployment are evidenced separately. RD-021, RD-022 and RD-023 remain open for substantive Research Director acceptance and are not accepted by this technical release.
