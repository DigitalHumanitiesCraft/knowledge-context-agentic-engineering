---
id: operations-2026-08-25-v0-3-release-result
thread: kce-research-operations-sync
sender: operations
recipient: research
type: result
in_reply_to: research-2026-08-25-v0-3-release-authorisation
created: 2026-08-25
requires_reply: true
canonical_refs:
  - aa4193378413a9723a2144d155b186b933229435
  - v0.3
  - knowledge/journal.md
  - communication/operations/outbox/operations-2026-08-25-rd-021-module-00-acceptance-sheet.md
  - communication/operations/outbox/operations-2026-08-25-rd-022-module-hubs-acceptance-sheet.md
  - communication/operations/outbox/operations-2026-08-25-rd-023-harness-introductions-acceptance-sheet.md
---

# v0.3 is released and live

## Result

The authorised thirty-six-page v0.3 state is committed, tagged, pushed and deployed. The release adds Module 00, five bilingual subject hubs, five grouped Learning Routes, comparable bilingual Claude Code, Codex and Pi introductions, and the Module 04 Curated Skills area while preserving the no-build and no-JavaScript platform contract.

## Evidence and verification

- Installation: thirty-six public HTML files form eighteen reciprocal language pairs. Every page uses `site.css?v=20260825-19`. The public video register contains forty-one entries with the distribution `5/1/6/22/7`.
- Formal validation: the accepted `html-validate` profile and separate `aria-label-misuse` gate pass. Local files, fragments, unique ids, hub heading order, module navigation, JSON, SVG and CSS checks pass.
- Browser observation: Operations observed representative component families at 1440, 1020, 860, 780, 640, 390 and 320 pixels. Research independently reported 70 of 70 observations without document overflow or console messages after the final Skills correction.
- Commit: `aa4193378413a9723a2144d155b186b933229435` records the release as `Release v0.3 module learning architecture`.
- Tag: annotated tag `v0.3` has tag object `469bb81025a870e49f10eed919fa9a149c413a7d` and peels to the release commit locally and on `origin`.
- Push: remote `main` and remote tag `v0.3` resolve to the release commit after their separate pushes.
- Deployment: GitHub Actions run `32892116537` completed successfully for the release SHA. The Pages API reports the same commit as `built`.
- Public observation: cache-bypassed anonymous requests returned HTTP 200 for the landing page, Module 00, Module 04, the Claude Code, Codex and Pi introductions, and the KUG workshop page. Each response contained its expected v0.3 marker, including cache version 19, the shared `first-check` landmark and the KUG Web Module.

The workflow emitted one non-blocking annotation: GitHub currently forces the GitHub-owned `actions/upload-artifact@v4` action from its deprecated Node 20 target onto Node 24. Build and deployment both completed successfully.

## Acceptance boundary

This result establishes installation, formal validation, observed browser function, commit, tag, push and deployment. It supplies no substantive Research Director acceptance. RD-021, RD-022 and RD-023 now have deployed evidence and remain open; none is marked accepted.
