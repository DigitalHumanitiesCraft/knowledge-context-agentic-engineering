# Google Artefacts of the Teaching Line

Link inventory for the register (`docs/data/workshops.json`) and the workshop subpages. Sources are this repository (`workshops/`, `script/`, `slides/`, `knowledge/`) and the author's research vault (`Teaching/Workshops/`, `Projects/`, `ACTIVE-WORK.md`). Nothing here is decided and no register file was changed.

Access was verified on 2026-08-20 from an unauthenticated client, by requesting the export endpoint of each document (`/export/pdf` for a deck, `/export?format=txt` for a document, `/export?format=csv` for a sheet) and by following the folder URL of each Drive folder to its final address. A redirect into `googleusercontent.com` means the file is readable by anyone with the link; an HTTP 401 or a landing on the Google sign-in page means it is not. The identity of every readable artefact was confirmed against its document title, so no row rests on the recorded link alone.

## What exists

Twelve Google artefacts belong to this teaching line, six of them readable without a login. The corpus itself is fully covered on both surfaces, meaning the master deck and the master script both live as public Google files. Of the four registered future instances only CLARIAH-AT has a live deck and a script surface, and both are public, which is why the register already carries them.

The two delivered instances close a gap the register still shows as `null`. The ÖAW AI Winter School has a public deck, public lecture notes, a public hands-on sheet and a public material folder, all reachable through the two short links printed on its title slide. The VetMedAI workshop 1 has a public German deck recorded in the vault, so the `slides` field of that entry can be filled.

What is missing is the middle of the pipeline. KUG/M3GIM, Uni for Life and the VetMed Winter School have no deck and no script surface at all, because their slide texts are still being worked out in the vault and the decks are derived from the master only after the operator has signed off the hands-on material. For KUG and Uni for Life the only Google artefacts are two Drive folders each, one for workshop material and one for participant data, and all four are login-gated, so nothing from them can go on a public subpage. The VetMed Winter School has no Google artefact whatsoever.

Three constraints apply before anything is published.

- The ÖAW spreadsheet URL as recorded in the source material carries the numeric id of the owning Google account (`ouid=` parameter) together with `rtpof` and `sd` parameters from an upload. The file is public, so the link works after the query string is cut back to `/edit?usp=sharing`. This inventory stores only the cleaned form; the source form must never be published, and the ÖAW profile has to be redacted accordingly before it enters the repo.
- The two short links of the ÖAW instance resolve to the canonical document URLs given below. A short link hides its target and can be repointed, so the register should carry the resolved URL and keep the short link only where it is quoted as printed material.
- The master script document holds two appendices after the script text, an older workshop concept with its glossary and slide planning, and the infographic design system. Publishing the document publishes those as well.

## Inventory

| Workshop or corpus | Artefact and type | Lang | URL | Access state | Linkable |
| --- | --- | --- | --- | --- | --- |
| Master corpus | Master slide deck *Knowledge, Context and Agentic Engineering for Knowledge Work. Full Slidedeck.* | de, English title slide | https://docs.google.com/presentation/d/1FtJpBn8l49I6B-r6b8bdIsbTngLQ9-LdP5BeylXD3M4/edit | public, export granted | yes; canonical live deck of the corpus, referenced from `script/master-script-en.md` |
| Master corpus | Master script as Google Doc, same title as the deck | de | https://docs.google.com/document/d/1yYEGgC2R8CDnkqqh8z6ApKfQYSETsYyez2vxwPHK8_k/edit | public, export granted | with reservation; the document continues past the script into two internal appendices (older workshop concept with glossary and slide planning, infographic design system), which a public link exposes |
| CLARIAH-AT 2026-09-25 | Live deck *CLARIAH-AT Summer School 2026 Machine Learning for Digital Scholarly Editions* | en | https://docs.google.com/presentation/d/1IdZJOM_xwg6WZXyu3-Am2MXVUkr0N-ivvhBU3Xn2Y4Q/edit | public, export granted | yes; already the `slides` value in the register |
| CLARIAH-AT 2026-09-25 | Script surface *CLARIAH AT Summer School 2026 Final Workshop Script* | en | https://docs.google.com/document/d/1a9wl2r9X9Y72DMvCK-vTAIc1vIYZTCUg9MCJRm1MLxY/edit | public, export granted | yes; already the `script` value in the register. The canonical text state stays `workshops/2026-09-25-clariah-at/workshop-script.md` |
| ÖAW AI Winter School 2026-02-17 (delivered) | Deck *ÖAW AI Winter School 2026. Vibe Coding & Promptotyping* | en | https://docs.google.com/presentation/d/1Fnyj8AhGy2difRHr_X5xa0vT7UYr5jVjOS8l7FAyo7w/edit | public, export granted | yes; this is the target of the title-slide short link `https://tinyurl.com/vibing-26`, which the profile records unresolved |
| ÖAW AI Winter School 2026-02-17 (delivered) | Lecture notes *Skriptum ÖAW AI Winter School 2026*, English body text | en | https://docs.google.com/document/d/1LK8nLJ6elOMukM_iUtNKXFvn0CHKvBVeyC1jnd0kBYM/edit | public, export granted | yes; target of the short link `https://tinyurl.com/vibing-26-notes` |
| ÖAW AI Winter School 2026-02-17 (delivered) | Hands-on sheet *workshop_graz_improved.xlsx* for the follow-up-prompt exercise | en | `https://docs.google.com/spreadsheets/d/1m1C22BaKY7gr9EFIVG5CVT0iAmH7VkEX/edit?usp=sharing` (cleaned; source form carried the owner account id and upload parameters, see summary note) | public, export granted | yes, in this cleaned form only |
| ÖAW AI Winter School 2026-02-17 (delivered) | Drive folder *Use Case 1*, material of the Patent Cooperation Network demo, holding synthetic data (`db_networkCoPat_fake.rds`) alongside the public demo repository | en | https://drive.google.com/drive/folders/130-QQjPfHEzWWD9_Py1_X3bhVc_5t1ci | public folder, listing served without login | yes; the data is declared synthetic, so a content check before publishing is a formality rather than a blocker |
| VetMedAI workshop 1 2026-04-22 (delivered) | Deck *Workshop 1. VetMedAI. Grundlagen GenAI und Prompt Engineering* | de | https://docs.google.com/presentation/d/1OCx8nGmlrpwM3X9ShR7z-NlkgyYMCO29Z26nPoXxsYM/edit | public, export granted | yes; fills the `slides` field the register entry currently leaves at `null` |
| KUG/M3GIM 2026-09-16 | Drive folder, workshop material | de | https://drive.google.com/drive/folders/1TaqB-BvNt20uAvOCCnQMQBk_2cV0gLjW | login-gated, redirects to the Google sign-in page | no; a public link would present a sign-in wall as workshop material |
| KUG/M3GIM 2026-09-16 | Drive folder, participant data for the Malaniuk demo corpus | de | https://drive.google.com/drive/folders/1Q5iiPsBfiaAWOK7Tuy9Z5LyiO0EUaZFJ | login-gated | no; participant distribution runs through the event, and the corpus rights are not settled |
| Uni for Life 2026-11-09 | Drive folder, workshop material | de | https://drive.google.com/drive/folders/1-nAcWTpwbA1d4v0SM_c9Ol9-Ev1NHUSr | login-gated | no |
| Uni for Life 2026-11-09 | Drive folder, participant data for the fictional-institute scenario with office files and a sample vault | de | https://drive.google.com/drive/folders/1qFTFVFYaV8e_7JwgGzG1DYTZF8wTtY6A | login-gated | no |
| VetMed Winter School 2026-11-30 | none | de | none | none | nothing exists; the concept document derives from the generic format and no Google surface has been created |

### Unregistered derivations of the master

These three instances are named in the vault as derivations of the master corpus and are absent from `docs/data/workshops.json`. They are listed apart because registering them is an operator decision, and none of their artefacts is publishable today.

| Workshop | Artefact and type | Lang | URL | Access state | Linkable |
| --- | --- | --- | --- | --- | --- |
| HEDIT Heidelberg 2026-10-05 | Drive folder, workshop material | de | https://drive.google.com/drive/folders/1HvO-_JWl3-r2opnCw6V805cIvq79WYgt | login-gated | no |
| HEDIT Heidelberg 2026-10-05 | Drive folder, participant data for the edition demo material | de | https://drive.google.com/drive/folders/1jVgB96iKYKvhPqQh4e-FwQTqjG8uhoVm | login-gated | no |
| Fachschaft Mittelalterstudien Heidelberg 2026-10-08 | Deck, a copy of the master deck taken as the derivation base | de | https://docs.google.com/presentation/d/1JSwP61Uam4oMN1drzJcKsWLGMhK8whs0WzPq6_c53CQ/edit | restricted, HTTP 401 on export, no title served | no; the file is not shared, and the deck is a working copy rather than a taught state |
| Fachschaft Mittelalterstudien Heidelberg 2026-10-08 | Drive folder, workshop material | de | https://drive.google.com/drive/folders/1sq_U3hcJFBtAJrWl4yjRyYT6J6Nic9wy | login-gated | no |
| Fachschaft Mittelalterstudien Heidelberg 2026-10-08 | Drive folder, participant data for the charter selection | de | https://drive.google.com/drive/folders/1pk-sNdtffVJvXDAJu1810nJbM9aqfrNM | login-gated | no; the licence of the charter set and the image rights of the source portal are unsettled |
| GDA Göttingen 2026-10-15 | none | de | none | none | the slide texts exist in the vault and carry origin fields into the master deck; no deck has been built |

## Exclusion list

Artefacts found in the same vault folders that belong to a different lecture line. The boundary criterion is derivation from the master corpus, meaning a document counts as inside the line when the vault records it as a master derivation or when this repository registers the instance.

- HEDIT Heidelberg 2025, deck of the first Heidelberg workshop (`https://docs.google.com/presentation/d/1ZnOUip67gxaHt0h-Bk6p_4C7H7an486ULM_3lk5gTYc/edit`), public. It belongs to the 2025 LLM and digital editions school that predates the master corpus.
- Uni for Life *Generative KI Theorie und Praxis* (`https://docs.google.com/presentation/d/1BmPZTnL2JULg_nXrU8mx2EBfmhaDPaVnoiaZU8G1rjI/edit`), the recurring two-hour fundamentals webinar that runs beside the agentic-engineering workshop and covers the basics rather than deriving from the master.
- VetMedAI workshops 2 to 6, five separate decks inside the institutional competence programme at the veterinary university. Only workshop 1 is registered here as a delivered instance, so the rest stay outside.
- The museum line with the three-part *KI im Museum* series of autumn 2025, *Programmieren 2.0* with its preparation deck and material folder, the two decks of the 2026 museum-association workshop at the natural history museum, and the brainstorming workshop on cultural-history objects.
- Single events on adjacent subjects, meaning the economics-institute workshop *AI for Data Analysis* with its deck and notes document, the regional-museums collection talk, and the three decks of the computing-centre training at Trier.
- Project talks, which serve a project audience and teach no module. This covers the two SuGW frontend decks and its two workshop decks, the Promptotyping workshop deck of the Zurich OCR and TEI project, and the stained-glass case-study deck.
- Business and research-administration documents, meaning offers, framework contracts, one-pager templates, the paper review document of the Promptotyping article and the working version of a funding application. None of them is a slide or a script, and none has a place in a public register.

## Consequences for the register

- Fill the two delivered entries. The ÖAW entry can carry the resolved deck and notes URLs instead of the short links; the VetMedAI entry can carry its deck.
- Decide the master entry. `master.slides` and `master.script` are `null` while both public master artefacts exist. The reservation on the script document is the only open question.
- Leave KUG, Uni for Life and VetMed Winter School at `null`. Every Google artefact they have is login-gated, and a gated link on a public page is worse than no link.
- Keep the login-gated folder ids out of `docs/`. They are recorded here so the operator sees the full state of each instance.
