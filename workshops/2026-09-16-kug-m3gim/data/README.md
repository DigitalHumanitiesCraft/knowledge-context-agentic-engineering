---
title: "Example Data KUG Summer School 2026"
workshop: 2026-09-16-kug-m3gim
created: 2026-08-20
updated: 2026-08-31
language: en
authors: [Christopher Pollin]
status: ready for rehearsal
related: [../profile.md, ../lecture-notes.md]
---

# Example Data KUG Summer School 2026

Thursday uses an access-controlled M³GIM working set. The public repository documents the data package and exercise logic. It does not store partner facsimiles or other files whose reuse rights have not been confirmed.

## Current working files

| File | Intended use | State |
| --- | --- | --- |
| `prompts.md` | Page transcription, source-critical cast extraction, cross-source validation, and the cast-explorer build prompt | updated in place and reloaded successfully on 2026-08-31 |
| Bayreuth 1953 source packet | Seven PDFs with 40 scan pages covering daily programmes, a season list, cast matrices, staff lists, and biographies | analysed locally; teaching reuse still depends on rights confirmation |
| `M3GIM-Bayreuth-1953-Integrationsvorlage.xlsx` | Facilitator reference with source inventory, cast rows, functions, participation proposals, and validation issues | structurally and visually validated |
| `bayreuth-1953-validated.json` | Stable input for the Promptotyping session | must be exported from the checked workbook subset before rehearsal |
| `plakattext-pl04.txt`, `personenindex-uebung.xlsx`, `orte-lookup.csv`, `m3gim-map-demo.zip` | Earlier mobility and map exercises | retained as reference material; outside the final Bayreuth hands-on path |

The prompt file remains in the controlled workshop Drive. The source packet is currently stored locally. The reference workbook belongs to the M³GIM project output. Before delivery, the permitted participant subset and validated JSON must be assembled in the controlled workshop folder. This repository documents the package without publishing partner source material.

## Participant source allocation

| Use | Source material | Teaching function |
| --- | --- | --- |
| Facilitator demonstration | Source 3, cast page | Show page-level transcription, compare it with the existing record, and identify known name and function errors. |
| Group A | Sources 7 and 8, cast pages | Extract regular occurrence and participation structures from two daily programmes. |
| Group B | Source 10, cast page | Model one participation with two stage roles in the same announced occurrence. |
| Group C | Source 11, daily cast page and *Wer singt was?* page | Compare daily and season-level statements without silent merging. |
| Cross-source validation | Selected schedule, cast-matrix, and biography pages from source 12 | Compare evidence types and record source-specific claims. |
| Extension | Source 9 and the remaining pages of source 12 | Test additional works, staff functions, and biography statements after the core exercise. |

Each distributed page requires:

1. a permitted page image;
2. the stable M³GIM source identifier;
3. a scan page or folio identifier;
4. its evidence type;
5. a facilitator reference transcription or checked data row;
6. an explicit validation issue where the page represents a difficult case.

The full 24-page source 12 booklet is too dense for live transcription within the hands-on session. Participants receive selected pages for comparison. The facilitator reference retains the complete analysis.

## Data model used in the exercise

The dated work or programme is represented as an `occurrence`. A person's contribution to that occurrence is represented as a `participation`. Production functions and performed characters occupy separate fields. One participation may contain several `stage_roles`. Every extracted participation stores `source_id`, `page_id`, `evidence_type`, an exact evidence quotation, certainty, and validation state.

The controlled evidence types are `daily_program`, `season_list`, `biography`, and `object_metadata`. A programme documents an announced assignment. It does not independently establish that the performance occurred with the announced cast.

## Exercise outputs

Participant outputs are derived teaching artefacts. They retain the source and page identifiers, model and prompt context, evidence type, source quotation, uncertainty markers, and human-validation result. Generated values become research claims only after comparison with the page and the facilitator reference.

The Promptotyping session uses `bayreuth-1953-validated.json`. This stable hand-off prevents extraction variation between groups from blocking application work. Participant JSON remains available for comparison and correction.

## Verified and open states

- The seven PDFs and all 40 scan pages were processed during source analysis.
- Critical cast, function, and cross-source cases were visually checked against the page images.
- The integration workbook passed structural, formula, and visual checks.
- The revised Drive prompt file was reloaded after replacement.
- The exact prompts have not yet been executed in Gemini on the selected participant pages.
- Rights confirmation, the validated JSON export, functional rehearsal, and participant acceptance remain open.
