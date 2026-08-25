---
id: research-2026-08-25-header-site-identity
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-navigation-about-imprint
created: 2026-08-25
requires_reply: true
canonical_refs:
  - docs/index.html
  - docs/index.de.html
  - docs/assets/site.css
  - knowledge/design.md
  - knowledge/specification.md
---

# Separate publisher logo from the teaching-site identity

## Objective and effect

Correct the header interaction that currently sends users to `dhcraft.org` when they click the visible site name. The publisher mark and the teaching-site identity receive distinct destinations and accessible names.

## Research Director decision

- The DHCraft logo is the only header element that links to `https://dhcraft.org`.
- The visible site name is `Knowledge, Context and Agentic Engineering for Knowledge Work` in both interface languages.
- The site-name link returns to the language-matched landing page.
- Remove the visible `Digital Humanities Craft` wordmark from the header. Publisher identity remains present through the logo, its accessible label and the footer.

## Interaction contract

Replace the current single brand anchor with a `site-identity` group containing two adjacent links.

1. The logo link contains the image and has an accessible name such as `Digital Humanities Craft website` or `Website von Digital Humanities Craft`. It opens in the same tab unless the existing global link policy says otherwise.
2. The text link contains the complete teaching-site name. English pages point to the correct relative route for `index.html`; German pages point to `index.de.html`.

Files directly under `docs/` use `index.html` or `index.de.html`. Tutorial and workshop pages use the equivalent `../` targets. The landing-page title may link to the current page, but it must not carry `aria-current`, because the site navigation already defines the current location where applicable.

## Responsive contract

- Keep the logo compact and visually subordinate to the site title.
- Allow the full site title to wrap to two lines where necessary.
- Do not truncate the title into an unexplained acronym.
- Keep both links as separate keyboard stops with distinct visible focus indicators.
- Maintain at least 44 pixel touch targets on coarse pointers.
- At narrow widths, preserve logo followed by title in reading order; allow the navigation to occupy its own row.

## Write boundary

Operations may update the shared header in all 22 public HTML pages, `docs/assets/site.css`, `CLAUDE.md`, `knowledge/design.md`, `knowledge/specification.md` and `knowledge/journal.md`.

## Verification criteria

1. Every public header contains two identity links with distinct destinations.
2. Only the logo links to `https://dhcraft.org`.
3. Every visible site-name link resolves to the language-matched landing page at the correct relative depth.
4. `Digital Humanities Craft` is absent as visible header text and remains available through the logo's accessible name and footer publisher block.
5. Keyboard and screenreader inspection distinguish the external publisher link from the local home link.
6. Desktop, 640, 390 and 320 pixel checks show a readable full title without horizontal overflow.
7. HTML validation, local-link checks and reciprocal language-page checks pass.

