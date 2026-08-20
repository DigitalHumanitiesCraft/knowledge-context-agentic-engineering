# Media Map (Proposal)

Mapping of the author's published blog posts and videos to the five master modules and to the registered workshop instances, so that the follow-up blocks of the workshop subpages can be filled from existing material. Sources are the content collection of the DHCraft site repository (`src/content/blog`, nine live posts), the channel feed cache of that repository (`src/lib/videos-cache.json`, the fifteen most recent uploads) and the videography document in the author's vault, which carries the topic descriptions and five further video identifiers that the feed no longer holds. Nothing here is decided; module and workshop assignments are proposals derived from the post metadata, the video descriptions and the module selections in the four workshop profiles.

Module numbering follows the master, meaning 1 Understanding Large Language Models, 2 Prompt Engineering, 3 Knowledge and Context Engineering, 4 Agentic Engineering, 5 Critical Perspectives and Governance. Workshop shorthands are KUG for the KUG/M3GIM summer school, CLARIAH for the CLARIAH-AT Summer School, UFL for Uni for Life, VetMed for the VetMed Winter School, plus the two delivered instances VetMedAI workshop 1 and ÖAW AI Winter School.

## Blog posts

All nine live posts sit on the subject of the corpus, so the table maps all of them. The language column states the language of the post; the site serves every post under both a German and an English route, and the text itself is not translated.

| Title | URL | Lang | Modules | Workshops | Why |
| --- | --- | --- | --- | --- | --- |
| System 1.42. Wie (Frontier-)LLMs "tatsächlich" funktionieren | https://dhcraft.org/excellence/blog/System1-42 | de | 1 | KUG, UFL, VetMed | The German long form of module 1, from autocomplete through emergence and grokking to reasoning, with the confabulating-reasoner thesis that the jagged-capability block states in compressed form |
| Asymmetric Amplification. Why AI Does Not Automate Research | https://dhcraft.org/excellence/blog/Asymmetric-Amplification | en | 1, 5 | CLARIAH | The source text of the asymmetric-amplification argument module 1 carries, with the access and infrastructure passages module 5 takes up |
| Asymmetric Amplifications and Epistemic Infrastructures | https://dhcraft.org/excellence/blog/Asymmetric-Amplifications-Epistemic-Infrastructures | en | 3, 5 | CLARIAH, ÖAW AI Winter School | Develops epistemic infrastructure as the methodological response, which is the argument behind the maintained knowledge base of module 3 and the verification stance of module 5; written for the ÖAW prize question 2026, so it doubles as the reading for that delivered instance |
| Ein Promptotyping-Projekt anlegen. Von den Forschungsdaten zum Forschungsartefakt | https://dhcraft.org/excellence/blog/Was-ist-Promptotyping | de | 3, 4 | KUG, UFL, VetMed | The current tutorial for doing it alone afterwards, from repository and `knowledge/` folder through CLAUDE.md and distillation to implementation with verification milestones |
| Promptotyping. Von der Idee zur Anwendung | https://dhcraft.org/excellence/blog/Promptotyping | de | 4, 2 | KUG, UFL | The conceptual paper behind the method, with Promptotyping Documents, Scholar-Centred Design and context compression; dated 2025 and superseded in practice by the tutorial above, so it belongs in a follow-up block as background |
| Promptotyping mit Claude Sonnet 4. Vibe-Coding erfordert den Critical-Expert-in-the-Loop | https://dhcraft.org/excellence/blog/Critical-Vibing-Claude-4 | de | 4, 5 | KUG, UFL, VetMed | A worked two-hour case in which the critical expert catches model agreement, which is the verification rule of module 5 in narrative form; the model generation named in it is dated |
| Haters gonna hate. Warum die Kritik an Vibe Coding berechtigt ist | https://dhcraft.org/excellence/blog/Vibe-Coding | de | 5, 4 | UFL, KUG | The critical counterweight to the coding demos, arguing where prompt-driven building fails; useful where an audience arrives with either enthusiasm or rejection |
| OpenAI's Deep Research und erste "Task-A(G)I" Systeme? | https://dhcraft.org/excellence/blog/Task-A(G)I | de | 1, 5 | VetMed, UFL | Task-specific capability against general capability, an early formulation of the jaggedness argument; from February 2025, so it reads as a time-stamped snapshot and should be labelled as one |
| New Year, New AI. Das große Monopoly um die "Intelligence" | https://dhcraft.org/excellence/blog/New-Year-New-AI-IdeaLab-25 | de | 5, 1 | UFL, VetMed | Power concentration among the labs and the reasoning-model race, which is the infrastructure-concentration topic of module 5; the model landscape it describes is from January 2025 |

### Not mapped

- `Asymmetric-Amplification-v1.md` and `Asymmetric-Amplification-v2.md` in the site repository carry `published: false` and produce no public page. The second is a substantially revised version of the live post and declares the same URL, so the live text under `/Asymmetric-Amplification` may change without the link changing. Check the state before a follow-up block cites the argument in detail.
- No live post is off topic. The blog runs on the same subject as the corpus, which is why the table has no discarded entries.

## Videos

Public identifiers and topic descriptions come from the vault videography document where it covers the video, otherwise from the channel feed cache. Every video is German. For the English CLARIAH instance the domain fit is high and the language is not, so those entries need a language label wherever they appear.

Availability was checked through the YouTube oEmbed endpoint on 2026-08-20. All identifiers below resolve except the one listed as unavailable.

| Title | URL | Lang | Modules | Workshops | Why |
| --- | --- | --- | --- | --- | --- |
| Wie LLMs funktionieren | https://www.youtube.com/watch?v=u4RRxi5tgTA | de | 1 | KUG, UFL, VetMed | The recorded module 1 lecture in German, the closest existing follow-up for an audience without an LLM background |
| Prompt Engineering | https://www.youtube.com/watch?v=Sj3F4oPWB8A | de | 2 | KUG, UFL, VetMed | The recorded module 2 lecture in German, current as of May 2026 |
| Prompt Engineering Grundlagen 1 | https://www.youtube.com/watch?v=syZYqNwsk5A | de | 2 | KUG | The earlier basics recording, slower and more elementary, which suits the profile without prerequisites |
| Einführung in Promptotyping (Teil 1) | https://www.youtube.com/watch?v=8sUe4Jkh3uQ | de | 4, 3 | KUG, UFL, VetMed | Concept and method on a project example, the entry point for anyone who wants the method after a short session |
| Einführung in Promptotyping (Teil 2, Live Demo mit Claude Code) | https://www.youtube.com/watch?v=hd_a-NBO_S4 | de | 4 | KUG, UFL, VetMed | The practical continuation of part 1 inside an AI harness; marked Patreon-exclusive in the vault, see the access note |
| Agentic Engineering und digitale Edition mit Claude Code und Fable 5 (Live Demo) | https://www.youtube.com/watch?v=kQaTu4oFjSo | de | 4, 5 | CLARIAH, VetMed | The full unedited path from digitised holdings to a static proto-edition with a verification frontend, with subagents for handwritten text recognition, optical character recognition and TEI modelling, verified by text-image synopsis, schema validation and model-assisted review; the closest video counterpart to the CLARIAH hands-on line |
| Promptotyping. TEI-Edition aus Word in 60 Minuten | https://www.youtube.com/watch?v=0DtX0pLv4TA | de | 4 | CLARIAH | A short, closed example of the same path, from a word-processor document to a TEI edition |
| Live Hands-On coOCR/HTR. Ein Promptotype für "Editor in the Loop" Transkriptionsworkflows | https://www.youtube.com/watch?v=VJyhVc_ujeA | de | 4, 2 | CLARIAH | Browser-based transcription experimentation with the editor kept in the loop, the direct counterpart to the Zweig transcription hands-on |
| Agentic Edition Workflow. Projektstatus und TEI-XML-Pipeline mit Claude Code | https://www.youtube.com/watch?v=3W9FjwCY24Q | de | 4 | CLARIAH | A complete TEI-XML pipeline on a prosopographic database of medieval Viennese legal transactions, showing the workflow at project scale |
| Live Hands-On. LLM-gestützte Registeranreicherung für das Handschriftenportal | https://www.youtube.com/watch?v=_CYNndO4VH4 | de | 4 | CLARIAH | Index enrichment on historical manuscript data, an authority-data task with a clear verification obligation; marked Patreon-exclusive in the vault, see the access note |
| MediaWiki zu Forschungsdaten. Agentic Coding am Beispiel der Klawiter-Bibliographie | https://www.youtube.com/watch?v=KG35VGVctJw | de | 4, 3 | UFL, VetMed | From a grown wiki database to structured research data and a faceted web application, a domain-neutral case for audiences outside edition work |
| Live Hands-On. Von der Kulturpool-API zum explorativen Sammlungsinterface | https://www.youtube.com/watch?v=tQBaaVhPu5U | de | 4 | CLARIAH, UFL | From an institutional collection interface to an explorative frontend, showing API access and structured output in one run |
| Wissens- und Projektmanagement mit Obsidian und Claude Code. Einführung | https://www.youtube.com/watch?v=31Y6uRLnkQA | de | 3, 4 | UFL, VetMed | An empty knowledge base built up step by step until it documents its own construction, which is the knowledge-engineering claim of module 3 in visible form |
| Grounded Vault. Quellenbasiertes Arbeiten mit AI Agents (Live Demo) | https://www.youtube.com/watch?v=K1sZBOUSZ_0 | de | 3, 5 | UFL, VetMed | Sources into markdown representations, distillates and assertions, with the provenance chain traced back from the output to the passage it rests on; the strongest single demonstration of grounding and its verification |
| Obsidian Vault-Pflege mit Claude Code | https://www.youtube.com/watch?v=CioCSbQWGXw | de | 3 | UFL | Systematic curation of an existing knowledge base, including overruling the model's counterarguments; marked Patreon-exclusive in the vault, see the access note |
| Wissensorganisation mit Obsidian, Claude Code und Nano Banana 2 | https://www.youtube.com/watch?v=aCMDWtCKGNw | de | 3 | UFL | Extraction, synthesis and feedback of the result into teaching slides, a knowledge-work loop outside research data; marked Patreon-exclusive in the vault, see the access note |
| Work in Progress Hands-On. Agentenbasierte makroökonomische Datenanalyse (Opus 4.5) | https://www.youtube.com/watch?v=21815nd9WMM | de | 4, 5 | UFL, VetMed, VetMedAI workshop 1 | Three subagent roles for analysis, implementation and synthesis on a European input-output dataset, with a documented and versioned run; the one agentic case in a statistical rather than an edition domain; marked Patreon-exclusive in the vault, see the access note |
| Keynote Digital Humanities Day Leipzig 2025 | https://www.youtube.com/watch?v=zD2rouUJNG0 | de | 4, 5 | CLARIAH, UFL | The framing talk on Promptotyping, agentic coding and research software development, which works as an overview link on any subpage rather than as module material |

### Not mapped

- RealmCraft, a strategy role-playing game played with an AI harness (https://www.youtube.com/watch?v=U_4OXqQ9SJ4). It demonstrates harness behaviour in a game setting and carries no module content.
- FIGARO-NAM, named entity recognition for historical periodicals. The vault videography lists the identifier `pNrRHjnFBSA`, and the oEmbed check returns 404, so the video is unavailable. Do not link it. The vault entry needs a correction, which is an operator matter because vault writes are outside this repository.

### Access note

The vault videography marks five videos as Patreon-exclusive, of which four appear in the public channel feed and all five resolve publicly. The marking is therefore either stale or means early access rather than restricted access. Confirm the access state of these five before any of them enters a public follow-up block, because a link that asks for a membership breaks the promise of a workshop follow-up page.

## Visual assets of the DHCraft site

The design rule admits real workshop title-slide covers, the line-art motif and the watercolor logo, and it excludes stock imagery and generic AI illustration. Measured against it, almost nothing in the site repository qualifies.

What qualifies:

- The brand mark in icon sizes, meaning `public/favicon.ico`, `public/favicon-32x32.png`, `public/apple-touch-icon.png` and `public/dhcraft_logo_invert.svg`. These are identity rather than imagery, and the platform currently declares no favicon at all, so they close a real gap. The canonical source stays the brand-assets repository; the site set shows which sizes are needed.
- `public/og-image.png` as a pattern for a share card, meaning the watercolor logo on the paper ground with a wordmark and a domain line. The file itself carries the company wordmark and cannot be reused as the platform's card.
- `src/assets/dhcraft_logo_watercolor_transparent.png` is the same logo already present as `docs/assets/dhcraft-logo-watercolor.png`, so it adds nothing.

What does not qualify:

- The roughly forty blog figures under `public/excellence/blog/img` are screenshots, memes, model-generated illustrations, benchmark charts and a third-party portrait. None is a workshop title slide, none is the platform motif, and several carry third-party rights.
- `public/excellence/blog/img/asymmetric-amplifications-epistemic.svg` comes closest in form, a hand-authored vector on the same paper ground with a reduced hexagon sequence. It is a blog header in the purple brand accent with gradient washes, and the platform motif is the turquoise line-art path from source to verified artefact. Taking it over would mean redrawing it in the platform's own vocabulary, which makes it an inspiration rather than an asset.
- The 28 institution logos under `src/assets/logos` include the four registered instances. Logos of third parties sit outside the imagery rule, carry their own rights and read as an endorsement claim, so using them requires an operator decision and a rule change.
- Project images and staff portraits are outside the rule without qualification.

Covers therefore keep coming from the real title slides, of which one exists so far.

## Integration recommendation

Media belong on the workshop subpages inside the existing follow-up block and stay off the master page, with one exception. Each subpage carries four to six entries at most, selected for the modules that instance emphasises, each with title, language label and one sentence stating what it shows and which module it continues, so the block reads as a curated continuation of the session rather than as a list of everything published. The English CLARIAH page needs the language label on every video entry and should lead with the two English posts. The master page gets a single line beneath the module list pointing to the blog and the channel as the running long form of the material, without individual links, which keeps the corpus the subject of the page and leaves the mapping in this document as the place where the per-instance selection is decided.
