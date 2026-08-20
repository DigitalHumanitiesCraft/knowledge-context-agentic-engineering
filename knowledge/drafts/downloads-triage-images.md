# Downloads Triage, Image Files

Inventory and assessment of the image files in the operator's Downloads folder (`C:\Users\Chrisi\Downloads`, flat) as of 2026-08-20. Documents were triaged separately and are out of scope here. The folder was read only; nothing was moved, renamed or deleted.

Two constraints from the repo knowledge govern every judgement below. `knowledge/design.md` admits only workshop title-slide covers (16:9 PNG, minimum 1280 px wide, at `docs/assets/covers/<id>.png`) and the motif line art, excluding stock imagery and generic AI illustrations. `knowledge/governance.md` forbids facsimiles in this repo, because the image rights of the Hersch and Zweig material remain with the source projects.

## Group Overview

| Group | Files | Resolution and ratio | Content type | Usability |
|---|---|---|---|---|
| CLARIAH deck, numbered PNG exports | 67 (base plus `(1)` to `(66)`) | 960x540, 16:9 | Mixed lecture slides: two section dividers, contact slides, text slides, concept diagrams, screenshots, paper citations | Below the 1280 px cover minimum. Usable as content reference, unusable as cover |
| CLARIAH deck, numbered JPG exports | 5 (base plus `(1)` to `(4)`) | 960x540, 16:9 | Contains the only genuine workshop title slide, plus case study, learning objectives, model landscape | Title slide identified here. Below the resolution minimum, needs re-export |
| CLARIAH, named high-resolution renders | 6 | 2560x1440 and 1280x720 and 1672x941, 16:9 | Redesigned slides in the platform design language, paper white with turquoise accent | Design-conformant and above the minimum. Two of them embed the Zweig facsimile, see rights section |
| CLARIAH, named title illustrations | 2 | 1774x887, 2:1 | AI-generated hero artwork, network sphere and edition workflow | Excluded by `design.md` (generic AI illustration) and by ratio |
| VetMedAI deck | 8 (base plus `(1)` to `(7)`) | 960x540, 16:9 | German content slides on LLM mechanics, tokenization, embeddings, context rot. No title slide in the set | Below the minimum and no title slide present |
| Stefan Zweig facsimiles | 4 files, 2 distinct images | 4912x7360, 2:3 portrait | Digitised archival material from the Literaturarchiv Salzburg | Forbidden in this repo, see rights section |
| Other decks (VU Forschungsinfrastruktur, Knowledge und Context Engineering Juli 2026) | 10 | 960x540, 16:9 | Slides from unrelated teaching events | Not relevant to the registered workshops |
| Standalone AI-generated illustrations | 12 | 1254x1254, 1536x1024, 1672x941, 2560x1440, 3840x1440 | Latent-program-space renders, DHCraft hexagon motif variants, pipeline diagrams | Mostly excluded by `design.md`. Two pipeline diagrams are conceptually close to the repo, see leftovers |
| Logos and screenshots | 4 | various, small | Brand and third-party marks, one Gemini UI screenshot | Not cover material |

### Duplicates inside the numbered CLARIAH sequence

The sequence is not a clean slide run. Eight numbers are byte-identical repeats of an earlier export, verified by MD5:

- `(7).png` equals `(34).png`
- `(8).png` equals `(65).png`
- `(16).png` equals `(26).png`
- `(22).png` equals `(28).png`
- `(44).png` equals `(47).png` equals `(53).png`
- `(56).png` equals `(58).png`
- `(57).png` equals `(59).png`
- `(62).png` equals `(63).png`

Outside the sequence there are two further exact duplicate pairs. `ChatGPT Image 17. Aug. 2026, 17_40_53.png` equals `Codex-Bild 18. Aug. 2026, 14_14_18.png`, and `Knowledge und Context Engineering für AI Agents Juli 2026 (2).png` equals `Knowledge und Context Engineering für AI Agents Juli 2026.png`. The facsimile triple is recorded in the rights section.

The first three PNG exports (`.png`, `(1).png`, `(2).png`) are three successive revisions of the same closing contact slide, which explains why they are the largest files in the group.

## Cover Candidates

### clariah-at-2026

`CLARIAH-AT Summer School 2026 Machine Learning for Digital Scholarly Editions.jpg` is the only genuine title slide anywhere in the folder. It carries the session title *Preparing Research Data for Topic Analysis with Generative AI*, the line *Knowledge, Context and Agentic Engineering for Digital Scholarly Editions*, the event name, the date 25.09.2026, the speaker line and the CC BY mark, with the CLARIAH-AT and ILDE logos top right. The layout reads as a title slide at card size, since the type block sits in the right two thirds against a quiet gradient.

The file fails the technical bar in two ways. It is 960x540, well under the 1280 px minimum, and it is JPEG where the platform expects PNG. It should be re-exported from the source deck at 2560x1440 or at least 1280x720 and saved as `docs/assets/covers/clariah-at-2026.png`. Nothing in Downloads offers the same slide at a usable resolution.

If an interim cover is needed before the re-export, `CLARIAH-AT_Prompts-Address-a-Latent-Program-Space.png` is the best compromise. It is exactly 1280x720, sits in the platform design language of paper white with turquoise accent, and its heading survives reduction to card size. It is a content slide rather than a title slide, so it should be replaced once the proper export exists.

### VetMedAI

No title slide exists in this group. All eight exports are content slides, and each of them fails the resolution bar at 960x540. A title slide has to be exported from the source deck before a cover can be placed, at 1280 px wide or more.

Two further points block a quick placement. The workshop is not yet registered, so the target filename is undetermined; the deck title *Workshop 1. VetMedAI. Grundlagen GenAI und Prompt Engineering* suggests an id along the lines of `vetmedai-2026`. The filenames also carry a typo, spelling the workshop both "VetMedAI" and "VedMedAI" in the same string, which is worth fixing at the source before exports are reused.

Should a placeholder be unavoidable, `Workshop 1. VetMedAI. Grundlagen GenAI und Prompt Engineering. VedMedAI (7).png` is the least bad choice. Its "Context Rot" heading is large and left-aligned, and a single chart fills the right half, so the slide stays readable when scaled down. The resolution deficit remains.

## Rights, Stefan Zweig Facsimiles

Both facsimile files are digitised archival material and must not enter this repo under any name or path. `knowledge/governance.md` states the rule directly, since the image rights of the Zweig material stay with the source project, which the platform links instead.

`szd-facsimile-0.png` shows a library call slip, headed *Bestellzettel Bücherausgabe*, a typewritten form filled in by hand in pencil. Legible fields name Stefan Zweig as orderer, Hotel Bellevue as residence, the shelfmark St. Z. B 488–491 and the catalogue keyword Merle d'Aubigné. The same image is present three times under different names: `szd-facsimile-0.png`, `IMG.1.png` and `stefan-zweig-bestellzettel-buecherausgabe-szd-139.png` are byte-identical. All three fall under the ban.

`szd-facsimile-1.png` shows page 1 of a handwritten manuscript on lined paper in violet ink, with red pencil corrections and rust stains from paper clips. The incipit reads *Sieht man einen alten Freund jeden Tag so bemerkt man nicht wie sein Antlitz sich verändert*. CLARIAH slide `(60)` identifies it as page 1 of the twelve-page manuscript *Radiovortrag über Newyork*, 1935, held by the Literaturarchiv Salzburg under shelfmark SZ-AAP/W27.

Two of the high-resolution named renders embed the call slip and are therefore caught by the same rule, even though they are otherwise design-conformant platform slides:

- `CLARIAH-AT_Hands-on_Run-the-Prompt-in-Google-AI-Studio.png` shows the full call slip in the left half.
- `CLARIAH-AT_Hands-on_Review-and-Verify-the-Transcription.png` shows a cropped detail of the same slip at upper right.

A third file, `Google-Gemini-08-18-2026_06_15_PM.png`, contains a thumbnail of the call slip inside a Gemini chat screenshot and is caught for the same reason. Neither of these belongs in the repo while the facsimile is visible; either the slides are re-rendered with the facsimile replaced by a link to the source project, or they stay outside.

Where the facsimiles do belong is the Stefan Zweig Digital case study material held by the source project, referenced from the platform by link. They may also stay in the private working material for the deck. Both files are already in the operator's own hands and need no separate securing action from this repo.

## Leftovers

**Named high-resolution CLARIAH renders, clean of facsimiles.** Three files sit in the platform design language, above the resolution minimum, and carry no rights encumbrance. `CLARIAH-AT_Context-Engineering_Context-Window-Context-Drop-and-Context-Rot.png` (2560x1440) diagrams how information enters the context window, alongside context drop and context rot; note that the "Project environment" box has a broken bullet where a stray "t" separated from the label. `CLARIAH-AT_Hands-on_Evaluate-the-Result-and-Choose-the-Model.png` (2560x1440) carries a model comparison table and a selection rule. `CLARIAH-AT_Prompts-Address-a-Latent-Program-Space.png` (1280x720) is the conceptual prompting slide named above as the interim cover candidate. These are the strongest candidates in the whole folder for illustrating module pages, if the platform ever admits slide figures beyond covers.

**Pipeline diagrams.** `Codex-Bild 18. Aug. 2026, 14_20_33.png` (3840x1440) is a dark-background workflow diagram tracing a Hersch source segment through multimodal transcription, entity and topic annotation into structured research data, with a provenance and review-point rail along the bottom, labelled by the four engineering terms of the project. `exec-34223566-462e-444a-a4a3-bf9a291850a8.png` (1628x966) is a related edition-workflow render. Both are conceptually on-topic. The dark ground of the first contradicts the paper-white design system, so it would need a light re-render before use.

**AI-generated hero illustrations.** `CLARIAH-AT-Knowledge-Context-Agentic-Engineering-Title-Illustration.png` and `CLARIAH-AT-Knowledge-Context-Agentic-Engineering-Research-Workflow-Title-Illustration.png` (both 1774x887), the four `Prompt Engineering *.png` renders (1536x1024 and 2560x1440), `CLARIAH-AT_Prompts-Address-a-Latent-Program-Space_Vector-Program-Manifold.png` (1672x941) and `Codex-Bild 18. Aug. 2026, 14_14_18.png` (1254x1254). All are excluded by the `design.md` rule against generic AI illustration, independent of their resolution.

**DHCraft motif variants.** `ChatGPT Image 17. Aug. 2026, 17_40_53.png`, `17_49_48.png`, `17_52_33.png`, `18_03_07 (1).png` and `18_03_07 (2).png` are watercolour hexagon compositions with the DHCraft wordmark, in square and 16:9 framings. They are brand experiments rather than repo assets. Canonical brand material lives in `DigitalHumanitiesCraft/brand-assets`, which also holds `dhcraft_logo_watercolor_transparent.C-w39ijb_Z2vFMWc.webp`, present here as a stray download copy.

**Unrelated decks.** The three `2026-06-08_VU 4.4 Forschungsinfrastruktur_Tag1*.png` files and the seven `Knowledge und Context Engineering für AI Agents Juli 2026*.png` files are exports from other teaching events at 960x540. They overlap thematically with the corpus, in particular a capta-versus-data slide and a context-window slide, so they may be worth consulting as content references. They are not candidates for any registered workshop cover.

**Third-party marks and screenshots.** `Microsoft_Office_Word_(2019–2025).svg.webp` and `images.png` (707x434, the Markdown mark) are third-party logos pulled for slide use. `Codex-Bild 18. Aug. 2026, 18_28_14.webp` is a Gemini benchmark comparison table from vendor material. None belongs in the repo.

## Open Points

- Re-export the CLARIAH title slide at 1280 px wide or more as PNG, then place it as `docs/assets/covers/clariah-at-2026.png`.
- Export a VetMedAI title slide; none exists among the current files.
- Register the VetMedAI workshop and settle its id before a cover path is fixed. The KUG/M3GIM and Uni for Life workshops have no exports in this folder at all.
- Decide whether the facsimile-bearing hands-on slides get a re-render without the facsimile, or stay out of the repo entirely.
