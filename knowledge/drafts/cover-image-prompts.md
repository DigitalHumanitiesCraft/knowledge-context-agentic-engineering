# Cover Image Prompts for Workshop Title Slides

Generation prompts for the title-slide images of the master deck and the four workshop decks. The images are produced with an image generator (ChatGPT image generation, Imagen), placed on the title slide in Google Slides, and the exported title slide becomes the platform cover under `docs/assets/covers/<id>.png`. The prompts are written against the design system in `knowledge/design.md`, so the covers on the platform and the decks in the room read as one family. Nothing here is decided; the prompts are drafts for the first generation round.

## Shared visual language

One vocabulary carries all five images. The ground is warm paper white, the drawing is thin near-black line art in two stroke weights, and the drawing behaves like a workflow diagram rather than an illustration, with small abstract stations, hairline connectors, right-angle turns and named nodes. This is the same motif vocabulary the platform uses for the path from source to verified artefact, so a cover is a fragment of that diagram rather than a decorative parallel world.

Exactly one accent colour appears per image, applied to a single path or a single station, and everything else stays near-black on paper. A faint watercolour wash in the accent colour may bleed under one element, echoing the DHCraft watercolor logo without imitating it; it stays optional because a generator often overdoes it, and a clean line drawing is the acceptable result.

Every image is 16:9 and keeps the upper third empty, so the slide typography of title, event and date sits on paper rather than on drawing. Excluded throughout are text, letters, numerals and logos, photorealism, and the generic AI iconography of robots, brains, circuit boards and glowing neural networks.

Fixed constraints in every prompt:

- 16:9 aspect ratio, wide landscape composition
- warm paper-white or very light ground
- thin precise line art, two stroke weights, workflow-diagram vocabulary
- one restrained accent colour, named with its hex value
- optional faint watercolour wash in the accent colour
- generous negative space in the upper third
- no text, no letters, no numerals, no logos, no photorealism, no robot or brain imagery

## What varies

| Subject | Content emphasis | Accent | Motif focus |
|---|---|---|---|
| Master deck | The whole path from source to verified artefact | turquoise `#0A7E7C` | all six stations, none enlarged |
| CLARIAH-AT | Research data workflows and digital scholarly editions | blue `#5B8FC4` | source sheet into structured record, verification gate |
| KUG (M3GIM) | First encounter with LLMs and prompting, low threshold | orange `#C87000` | prompt and response, iteration, a low step |
| Uni for Life | Knowledge work in organisations, documents to decisions | violet `#8140B8` | convergence of many documents into one decision |
| VetMed Winter School | Five-day derivation with a governance accent | green `#7C9200` | five segments inside a policy boundary |

The accent assignment uses each of the four identity colours once, so the five covers in the platform's card row reproduce the logo palette as a set, with turquoise carrying the master. Two assignments also agree with the module marks, orange for prompt engineering as the KUG centre and green for governance as the VetMed accent. The assignment is a cover-layer decision and encodes no module reference; the design rule that the identity palette is otherwise reserved for the five module marks stays untouched.

## Master deck

Emphasis: the complete path from source to verified artefact, the corpus in one line.

### Variant A, horizontal chain

```
Wide 16:9 editorial line-art illustration on a warm paper-white ground, drawn like a precise technical workflow diagram. A single horizontal chain of six small abstract stations runs across the lower half, formed by a stack of sheets, a folder of documents, a bracketed frame, a closed circular loop, a diamond checkpoint and a sealed rectangular block, connected by hairline rules with right-angle turns. Two stroke weights only, near-black hairlines, one restrained accent in deep turquoise #0A7E7C on the connecting path and the final block. A faint turquoise watercolour wash bleeds under the last station. The upper third stays empty paper. No text, no letters, no numerals, no logos, no photorealism, no robots, brains or glowing neural networks.
```

### Variant B, grouped arrangement

```
Wide 16:9 minimal line-art composition on warm paper white, drawn with thin architectural precision. Six small abstract objects rest on a shallow ground line in the lower right, a leaf of paper, a folder, an open bracket frame, a coiled loop, a small gate and a sealed block, threaded by one continuous hairline that folds back on itself once at the loop. Ample empty paper across the upper third and the left side. Two stroke weights, near-black lines, a single accent in deep turquoise #0A7E7C limited to the folded loop and the gate, plus a soft turquoise watercolour bloom at the lower left. No text, no letters, no numerals, no logos, no photorealism, no robot, brain or circuit imagery.
```

## CLARIAH-AT Summer School

Emphasis: archival source into structured, verified research data for digital scholarly editions.

### Variant A, sheet into structure

```
Wide 16:9 line-art illustration on warm paper-white ground, drawn as a calm technical diagram. In the lower left an abstract archival leaf carries a few soft wavy hairlines suggesting handwriting without any readable characters. A hairline path leads right into a nested bracket tree of small indented rectangles, an abstract structured record, and continues to a diamond checkpoint and a sealed data block at the lower right. Two stroke weights, near-black lines, one restrained accent in muted blue #5B8FC4 on the path and the checkpoint. A faint blue watercolour wash bleeds under the archival leaf. The upper third stays empty paper for typography. No text, no letters, no numerals, no logos, no photorealism, no robots or brains.
```

### Variant B, fanned leaves and grid

```
Wide 16:9 minimal editorial line art on very light paper ground. Three abstract archival leaves lie fanned in the lower left, marked only by faint wavy strokes with no readable writing. Thin lines rise from one leaf and cross to a fine grid of small nested rectangles in the lower right, where a single cell is outlined more strongly and marked by a small magnifier glyph for verification. Two stroke weights, near-black hairlines, one accent in muted blue #5B8FC4 on the crossing line and the marked cell, and an optional pale blue watercolour wash under the leaves. Generous empty paper in the upper third. No text, no letters, no numerals, no logos, no photorealism, no AI robot or brain imagery.
```

## KUG Summer School (M3GIM)

Emphasis: an approachable first encounter with LLMs and prompting, deliberately low threshold.

### Variant A, exchange over a low step

```
Wide 16:9 friendly minimal line-art illustration on warm paper-white ground. Two empty rounded frames face each other in the lower centre, suggesting an exchange, with nothing written inside them. Beneath them three shallow wide steps rise gently from left to right, a very low threshold, traced by one continuous line. Strokes are thin and softly curved rather than strictly geometric, in two weights, near-black, with a single warm accent in ochre orange #C87000 on the step line and the right-hand frame. A soft orange watercolour wash sits faintly under the steps. The upper third remains empty paper. No text, no letters, no numerals, no logos, no photorealism, no robots, brains or glowing neural networks.
```

### Variant B, notebook and loop

```
Wide 16:9 warm minimal line drawing on very light paper ground, thin lines with a slightly relaxed hand-drawn quality. In the lower right an open notebook shape lies beside a simple rounded speech frame with no writing inside; one hairline runs from the notebook to the frame, curls back once and returns, with three small dots marking the repetitions. Everything else is empty paper, especially the upper third and the left half. Two stroke weights, near-black, one accent in ochre orange #C87000 on the curling line and the three dots, plus an optional faint orange watercolour bloom under the notebook. No text, no letters, no numerals, no logos, no photorealism, no robot or brain motifs.
```

## Uni for Life

Emphasis: knowledge work in organisations, from scattered documents to a decision that holds.

### Variant A, convergence into a decision

```
Wide 16:9 line-art illustration on warm paper-white ground, drawn like a precise process diagram. In the lower left a loose fan of abstract document sheets spreads out; hairlines run from each sheet and converge through a narrow lens-shaped opening in the lower centre into one single clear line, which ends at a small solid marker in the lower right, the decision. Two stroke weights, near-black hairlines, one restrained accent in violet #8140B8 on the converging lines and the final marker. A faint violet watercolour wash lies under the fan of sheets. The upper third stays generous empty paper for typography. No text, no letters, no numerals, no logos, no photorealism, no robots or brains.
```

### Variant B, shelf and single outgoing line

```
Wide 16:9 minimal editorial line art on very light paper ground. In the lower left a tidy grid of stacked rectangular document blocks suggests an organisation's holdings. Thin hairlines leave the grid, meet at one small round node in the lower centre, and continue as a single line to a diamond checkpoint and a small flag shape at the lower right. Precise geometry, two stroke weights, near-black, with one restrained accent in violet #8140B8 on the single outgoing line and the flag, and an optional pale violet watercolour wash behind the document grid. The upper third and upper right stay empty paper. No text, no letters, no numerals, no logos, no photorealism, no AI robot or brain imagery.
```

## VetMed Winter School

Emphasis: the full five-day derivation, held inside a governance frame with an EU AI Act accent.

### Variant A, five segments and a seal

```
Wide 16:9 line-art illustration on warm paper-white ground, drawn as a calm technical diagram. Five slender vertical bands of gently increasing internal detail stand side by side across the lower half, each holding a few small abstract nodes. One continuous hairline threads through all five from left to right and ends at a simple gate framed by a bracket, beside a small circular seal outline. Two stroke weights, near-black lines, one restrained accent in olive green #7C9200 on the threading line, the gate and the seal. A faint green watercolour wash bleeds under the last band. The upper third remains empty paper. No text, no letters, no numerals, no logos, no photorealism, no robots, brains or circuit boards.
```

### Variant B, process inside a policy boundary

```
Wide 16:9 minimal line-art composition on very light paper ground. A horizontal chain of five small abstract stations, connected by hairlines with right-angle turns, runs across the lower half. A thin dashed boundary line encloses the whole chain like a policy frame, and small diamond checkpoints sit where the chain crosses that boundary. Precise technical drawing, two stroke weights, near-black, with one restrained accent in olive green #7C9200 on the dashed boundary and the checkpoints, plus an optional soft green watercolour wash inside one corner of the frame. Generous empty paper above the boundary across the entire upper third. No text, no letters, no numerals, no logos, no photorealism, no robot or brain imagery.
```

## Usage

Generate four to six images per prompt before judging, because the variance between runs of the same prompt is larger than the difference between the two variants. Pick one, then regenerate around it by changing a single clause, usually the composition line, the number of stations, the strength of the watercolour wash or the position of the empty zone. Keep the hex value verbatim in every regeneration, since generators drift towards a saturated default the moment the colour is named without its code. If a run writes letters or pseudo-writing into the image anyway, discard it and generate again; retouching a fake glyph out of line art costs more than a new run.

The stated empty zone follows the requirement that slide typography sits on paper. The existing CLARIAH title slide places its text block in the right two thirds, so if that layout stays, replace the upper-third clause with a request for the right half to stay empty, and keep the drawing in the left band.

The generated image is an input, never the published cover. Place it on the title slide in Google Slides, set title, event and date over the empty zone, and export the finished title slide as a 16:9 PNG of at least 1280 px width to `docs/assets/covers/<id>.png`. The platform card shows that exported slide, so the cover carries the deck's own typography and the raw image alone never appears on the platform.
