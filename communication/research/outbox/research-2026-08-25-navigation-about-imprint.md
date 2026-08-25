---
id: research-2026-08-25-navigation-about-imprint
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-iteration-16-release-brief
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/preparation.html
  - docs/preparation.de.html
  - docs/about.html
  - docs/about.de.html
  - CLAUDE.md
  - knowledge/design.md
  - knowledge/specification.md
---

# Install Preparation and the combined About and Imprint entry in the site navigation

## Objective and effect

Make the Preparation tutorial a central route from every public page and combine the local project explanation with an explicit route to the canonical legal notice. The canonical legal text remains on `dhcraft.org`, which prevents legal copy from drifting across sites.

## Research Director decisions

The binding top-navigation order is:

`Preparation / Vorbereitung` → `About & Imprint / Über & Impressum` → `GitHub`

The existing local About pages become the combined local entry. They retain their four editorial sections and add a fifth metadata field named `Canonical legal notice` or `Kanonischer Rechtstext`, linked directly to `https://dhcraft.org/imprint`.

## Write boundary

Operations may update all 22 public HTML pages, `CLAUDE.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`. Change `docs/assets/site.css` only if browser evidence shows that the longer labels need a responsive correction.

Use same-language local targets at the correct directory depth. Files under `docs/` use `preparation(.de).html` and `about(.de).html`; tutorial and workshop pages use the equivalent `../` targets.

On the two Preparation pages, only the Preparation link carries `aria-current="page"` in the site navigation. On the two About pages, only the combined local entry carries it. Landing, focused tutorial and workshop pages have no current site-navigation entry. The language navigation keeps its own independent current-page state.

Update every footer so the local link reads `About & Imprint` or `Über & Impressum`. Retain the external canonical link and label it `Legal notice on dhcraft.org` or `Rechtstext auf dhcraft.org`. Remove duplicate current-page semantics from the footer.

## Exclusions

- Do not add another public page.
- Do not duplicate the full legal text from `dhcraft.org`.
- Do not change the four existing editorial About sections.
- Do not change the language-pair or favicon contracts.

## Verification criteria

1. The public tree still contains exactly 22 HTML pages.
2. Every site-navigation landmark contains exactly three links in the required order and language.
3. All local navigation targets resolve from their directory depth.
4. Each site-navigation landmark has at most one current-page link, independently of the language navigation.
5. Both About pages use the combined title and H1, retain four editorial sections, expose five metadata fields and link to the canonical legal notice.
6. Every footer distinguishes the local combined entry from the external canonical legal notice.
7. Keyboard order follows visual order, and the skip link and focus indicators remain intact.
8. Desktop, 640, 390 and 320 pixel browser checks show no horizontal overflow and at least 44 pixel touch targets on coarse pointers.
9. HTML validation, unique-id checks, reciprocal language-link checks and local-link checks pass.

