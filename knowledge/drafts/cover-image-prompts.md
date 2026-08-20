# Production Prompts for Cover Images

These prompts document the selected visual direction for the Full Slide Deck and its seven workshop specialisations. Each prompt is designed for ChatGPT image generation and can be used for a new generation or as the basis for editing the current cover.

## Files

| Cover | File |
|---|---|
| Full Slide Deck | `docs/assets/covers/full.png` |
| KUG M3GIM | `docs/assets/covers/2026-09-16-kug-m3gim.png` |
| CLARIAH-AT | `docs/assets/covers/2026-09-25-clariah-at.png` |
| HEDIT Heidelberg | `docs/assets/covers/2026-10-05-hedit-heidelberg.png` |
| Fachschaft Mittelalterstudien | `docs/assets/covers/2026-10-08-fachschaft-mittelalterstudien-heidelberg.png` |
| GDA Göttingen | `docs/assets/covers/2026-10-15-gda-goettingen.png` |
| Uni for Life | `docs/assets/covers/2026-11-09-ufl.png` |
| VetMed Winter School | `docs/assets/covers/2026-11-30-vetmed-winter-school.png` |

## Shared production constraints

- Wide 16:9 landscape composition, minimum width 1280 px.
- Warm paper-white ground with the upper third left empty for slide typography.
- One integrated emblem or object in the lower centre, readable at card-thumbnail size.
- Precise deep-navy ink contours in two consistent stroke weights.
- Restrained watercolor held mainly inside designed shapes.
- DHCraft semantic palette: violet `#8140B8` for model capability, orange `#C87000` for prompting, turquoise `#0A7E7C` for knowledge and context, blue `#5B8FC4` for agentic action, green `#7C9200` for governance and verification.
- No text, letters, numerals, pseudo-writing, unrelated logos or watermarks. A named tool icon may appear only where a workshop prompt explicitly requires it.
- Historical source surfaces use sparse non-letter-like ink textures. They contain no word-shaped marks or repeated glyph sequences.
- Avoid robots, brains, circuit-board metaphors, generic dashboards, decorative orbit lines, checkmarks, badges and meaningless network graphs.

## Selection status and regeneration risks

All eight covers are selected and present in the repository. The prompts below are the production contract for later regeneration. Four subjects need explicit protection against recurrent generator defaults.

| Cover | Stable element | Regeneration guardrail |
|---|---|---|
| CLARIAH-AT | open codex carrying source, transcription and structured result | exactly three internal zones, no charts, labels or dashboard furniture |
| HEDIT Heidelberg | manuscript tray with two fold-out Promptotyping boards | page and bookbinding geometry only, no interface panels or generic networks |
| Uni for Life | document tray, context lens and agentic write-back | anchored document-handling arm, no body, head, floating polyhedron or character |
| VetMed Winter School | microscopy selection and AI-assisted analysis | equine hoof lamellar tissue as the species-specific veterinary sample |
| Fachschaft Mittelalterstudien | charter, extracted records and small Claude Code agents | current cover is a required identity reference for the agent figure |

## Full Slide Deck

```text
Use case: stylized-concept
Asset type: 16:9 title-slide cover for the Full Slide Deck
Input images: Image 1 is the DHCraft watercolor logo, used only for palette, paper texture and pigment character. If supplied, Image 2 is the current full.png, used as a composition anchor.
Primary request: Create one compact emblem of maintained project knowledge becoming a verified research artefact. Show a precise stack of knowledge documents with a transparent turquoise context frame cut into the front sheet. Inside the selected frame sits one small faceted artefact core. A single blue agentic tool stroke enters the frame, acts on the core and returns to the document stack. Enclose the object with one incomplete turquoise feedback circle and one quiet green registration notch. Use tiny restrained facets in violet, orange, turquoise, blue and green inside the core.
Style: human-directed editorial illustration, deep-navy technical ink, controlled DHCraft watercolor, flat frontal view.
Composition: one emblem in the lower centre, strong silhouette, upper third completely empty.
Constraints: apply the shared production constraints; remove all readable page marks and decorative symbols.
```

## KUG Summer School M3GIM

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current KUG cover, used as the subject and composition anchor.
Primary request: Create one open opera promptbook whose covers form an elegant proscenium stage. Use restrained red-violet curtains, a shallow orchestra-pit curve and a clear stage opening. Place one compact archival bundle of programmes, correspondence and historical photographs on the stage as the knowledge source. A transparent turquoise aperture selects one archival item. Three clean unlabeled data slips emerge into a compact index integrated into the right side of the proscenium. One blue agentic thread passes through archive, selected context and extracted data, then returns through the orchestra pit.
Style: refined archival watercolor and precise deep-navy ink, detailed enough to establish opera while remaining clear at thumbnail size.
Palette: orange #C87000 and violet #8140B8 for prompting and model capability, turquoise #0A7E7C for context, blue #5B8FC4 for the agentic path.
Constraints: apply the shared production constraints; avoid musical notation, map pins and decorative theatre ornament.
```

## CLARIAH-AT Summer School

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current CLARIAH-AT cover, used as the subject and composition anchor.
Primary request: Create one open scholarly codex that contains a complete research-data transformation in exactly three internal zones. The left zone holds an archival manuscript facsimile made from sparse non-letter-like ink textures. A transparent turquoise context window selects one passage. The centre zone resolves the passage into a clean transcription field made from broad blank rules. The right zone contains four unlabeled structured fields for information extraction. One blue agentic path connects source, selected context, transcription and structured result, then returns to the facsimile through a quiet green verification notch. The codex remains the only object.
Style: archival conservation plate combined with translucent technical overlays, deep-navy ink and controlled watercolor.
Palette: turquoise #0A7E7C and blue #5B8FC4 dominant, small orange #C87000 and green #7C9200 details.
Constraints: apply the shared production constraints; use exactly three internal zones and no more than five major shapes; omit charts, axes, legends, checkmarks, topic-model diagrams, interface cards and dashboard styling.
```

## HEDIT Heidelberg

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current HEDIT cover, used as the subject and composition anchor.
Primary request: Create one fold-out scholarly edition workstation. A bound archival manuscript bundle rests in a precise bookbinding tray at the left. A turquoise context aperture selects one passage from the participant material. Exactly two integrated paper boards extend to the right. The upper board groups four selected source fragments through simple color fields and connecting rules. The lower board arranges the same passage into four nested editorial zones. One continuous blue agentic thread connects the source, both Promptotyping stages and a verified return to the manuscript. Use one orange removable adapter at the hinge. Every component is made from paper, board, thread or bookbinding hardware.
Style: precision bookbinding and technical product illustration, shallow axonometric view, deep-navy ink and matte watercolor.
Palette: turquoise #0A7E7C and blue #5B8FC4 dominant, orange #C87000 and violet #8140B8 as small working accents.
Constraints: apply the shared production constraints; use exactly two fold-out boards; avoid readable XML, charts, interface panels, software windows, generic network graphs and dashboard styling.
```

## Fachschaft Mittelalterstudien Heidelberg

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. Image 2 is the current medieval-studies cover and is required as the identity and composition reference.
Primary request: Create one authentic medieval charter with a restrained pendent wax seal. A transparent turquoise aperture selects one precise passage from the parchment. Three small unlabeled structured record slips emerge from that passage and align along the right edge, representing handwriting recognition, structured extraction and the small digital edition. Preserve the same small geometric Claude Code agent figure from the reference image in three purposeful poses: inspecting the charter with a magnifier, selecting the passage from a small ladder and managing the verified return at the lower edge. One controlled blue path connects the source passage with the three records and returns to the charter as verified write-back. Preserve natural parchment irregularity and a clear documentary silhouette.
Style: scholarly facsimile and archival conservation drawing, precise deep-navy contours, restrained mineral watercolor.
Palette: turquoise #0A7E7C and blue #5B8FC4, orange #C87000 for the wax seal, one small green #7C9200 verification detail.
Constraints: apply the shared production constraints; preserve the supplied Claude Code agent figure consistently; keep all three figures small and subordinate to the charter; omit heraldry, XML brackets, alternative robot faces and decorative medieval motifs.
```

## GDA Göttingen

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current GDA cover, used as the subject and composition anchor.
Primary request: Create one modular research-software maintenance workbench. Several heterogeneous research-data packages and legacy carriers enter from the left. A replaceable turquoise compatibility layer selects and aligns the active context. Clean blue service modules transform the material and connect it to a maintained interface-and-endpoints component on the right. An orange removable update cartridge represents migration and repair. One integrated blue agentic feedback path connects source data, transformation, interface maintenance and verified return.
Style: Swiss technical product illustration, shallow exploded view, precise deep-navy ink and matte watercolor enamel.
Palette: turquoise #0A7E7C and blue #5B8FC4 dominant, orange #C87000 for the update component, green #7C9200 for one maintenance registration mark.
Constraints: apply the shared production constraints; avoid literal computer plugs, database cylinders, leaf icons, recycle symbols, checkmarks and generic network diagrams.
```

## Uni for Life

```text
Use case: stylized-concept
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current Uni for Life cover, used as the subject and composition anchor.
Primary request: Create one professional knowledge-work instrument. A structured violet document tray holds several layered source briefs. A movable turquoise context lens selects one relevant packet. An articulated document-handling arm is anchored directly to the tray and built from three simple hinged bars. It lifts the selected packet, works on it at a restrained drafting surface and returns a corrected version into a clearly marked write-back tray. One blue path connects source knowledge, selected context, agentic action and write-back. Replace any humanoid figure from the reference with this anchored arm.
Style: high-end editorial paper construction with mechanical precision, deep-navy ink, matte watercolor and subtle asymmetry.
Palette: violet #8140B8 dominant, turquoise #0A7E7C and blue #5B8FC4.
Constraints: apply the shared production constraints; the arm has no head, face, torso, hands, floating polyhedron or character traits; avoid robots, office clip art, screens and decorative cable loops.
```

## VetMed Winter School

```text
Use case: scientific-educational
Asset type: 16:9 workshop title-slide cover
Input images: Image 1 is the DHCraft watercolor logo, used only for palette and material character. If supplied, Image 2 is the current VetMed cover, used as the subject and composition anchor.
Primary request: Create one scientifically plausible histological cross-section of equine hoof lamellar tissue, showing the characteristic interlocking epidermal and dermal lamellae. A transparent turquoise microscopy region of interest selects one subtle tissue pattern. Inside it, a precise blue segmentation contour shows how AI-assisted image analysis can identify and compare relevant structures. Beneath the specimen, integrate a restrained evidence path from whole sample to selected context, analytical model and veterinary expert verification, returning to the specimen. Use the five semantic colors across anatomical and analytical layers without turning them into decorative rainbow bands.
Style: museum-quality veterinary scientific plate, deep-navy ink and translucent watercolor, precise and research-oriented.
Palette: violet #8140B8, orange #C87000, turquoise #0A7E7C, blue #5B8FC4 and green #7C9200.
Constraints: apply the shared production constraints; avoid human anatomy, mascots, paws, medical shields, checkmarks and generic AI symbols.
```

## Regeneration workflow

Use the current cover as Image 2 when refining a selected composition. Preserve its main silhouette and change one targeted property per iteration. Reject runs containing readable or pseudo-readable text. Export the selected result as PNG under the exact path listed above.
