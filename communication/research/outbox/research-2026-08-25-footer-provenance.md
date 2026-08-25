---
id: research-2026-08-25-footer-provenance
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-navigation-about-imprint
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/assets/site.css
  - docs/index.html
  - docs/index.de.html
  - knowledge/design.md
  - knowledge/specification.md
---

# Refactor the shared footer and reference Research Mission Control

## Objective and effect

Reduce the visual height and conceptual load of the shared footer. Separate publisher identity, methodological provenance and navigation so that the footer remains readable without competing blocks. Add the canonical Research Mission Control repository as a method reference.

## Binding content

Remove volatile model names and versions from the public footer. Preserve detailed tool provenance in the repository knowledge and journal where it can be dated. The public footer names the two maintained methods that structure the work.

English provenance copy:

`Developed and maintained by Digital Humanities Craft using Promptotyping and Research Mission Control.`

German provenance copy:

`Entwickelt und gepflegt von Digital Humanities Craft mit Promptotyping und Research Mission Control.`

Link `Digital Humanities Craft` to `https://dhcraft.org`, `Promptotyping` to `https://dhcraft.org/Promptotyping/`, and `Research Mission Control` to `https://github.com/chpollin/forschungsleitstelle`. The repository URL was verified against its Git remote on 2026-08-25.

## Information hierarchy

Use three visually distinct groups inside one compact footer grid.

1. Publisher identity with the DHCraft logo, name, organisation, site and contact address.
2. The one-sentence provenance statement.
3. A compact footer navigation containing the combined local About and Imprint entry, the teaching-material repository, the Promptotyping repository, the Research Mission Control repository, the CC BY 4.0 licence and the canonical legal notice.

Use concise language-specific link labels. Avoid repeating `GitHub repository` in every label when the GitHub icon and destination context already establish the platform. Suitable labels are `Teaching material`, `Promptotyping`, `Research Mission Control`, `CC BY 4.0` and `Legal notice`; use `Lehrmaterial`, `Promptotyping`, `Forschungsleitstelle`, `CC BY 4.0` and `Rechtstext` in German.

## Layout contract

- Reduce the large blank band before and inside the footer. Start with `padding-block: var(--s5)` and retain larger spacing only where browser evidence shows that content sections need separation.
- Reduce the logo from the current 112 to 140 pixel range to a compact 72 to 96 pixel range.
- Use a three-column grid on wide screens with a bounded provenance column. Stack the groups in their semantic order on narrow screens.
- Align all wide-screen groups at their top edge. Do not vertically anchor one group to the bottom of another.
- Keep body-sized text and a comfortable line height. The provenance statement should occupy at most three lines on a normal desktop viewport.
- Keep visible focus states and at least 44 pixel touch targets on coarse pointers.

## Write boundary

Operations may update the shared footer in all 22 public HTML pages, `docs/assets/site.css`, the footer contract in `knowledge/design.md` and `knowledge/specification.md`, and the integrated decision in `knowledge/journal.md`.

## Verification criteria

1. Every public page exposes identical language-matched footer structure and destinations.
2. All three GitHub destinations resolve to the teaching-material, Promptotyping and Research Mission Control repositories.
3. No public footer names a model version.
4. Desktop rendering has three top-aligned groups without the large empty band visible in the supplied screenshot.
5. At 640, 390 and 320 pixels the groups stack in semantic order without horizontal overflow.
6. Keyboard order matches the visual order; all links retain visible focus and coarse-pointer touch targets.
7. HTML validation, local-link checks and contrast checks pass.

