---
id: research-2026-08-25-footer-provenance-url-correction
thread: kce-research-operations-sync
sender: research
recipient: operations
type: brief
in_reply_to: research-2026-08-25-footer-provenance
created: 2026-08-25
requires_reply: true
canonical_refs:
  - README.md
  - CLAUDE.md
  - knowledge/design.md
  - knowledge/specification.md
  - docs/
---

# Correction: use the public Research Mission Control repository

The Research Director requires a public Research Mission Control reference. The URL in `research-2026-08-25-footer-provenance` points to a private repository and is superseded.

Use this canonical public URL everywhere:

`https://github.com/DigitalHumanitiesCraft/research-mission-control`

The public repository resolved through its Git remote on 2026-08-25 and is already the route documented in `README.md`. The private `https://github.com/chpollin/forschungsleitstelle` route may remain in immutable historical briefs only.

## Required propagation

- Replace both footer occurrences on all public HTML pages.
- Correct the action-layer, design and specification contracts.
- Resolve the open URL delta in the journal as a corrected Research source instruction.
- Preserve the visible English label `Research Mission Control` and German label `Forschungsleitstelle`.

## Verification criteria

1. Every public Research Mission Control link uses the canonical public URL.
2. No public HTML, action-layer or active declarative contract contains the private route.
3. Anonymous HTTP access to the public route returns a successful response.
4. The immutable superseded brief remains unchanged and is explicitly superseded by this correction.

