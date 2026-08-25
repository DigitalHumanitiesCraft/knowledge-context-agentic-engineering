# Research Mission Control Context Stream

This register locates the active Research and Operations exchange for this repository. The stream is the transport layer of Research Mission Control. Promptotyping remains the artefact-development method, and `knowledge/` remains the canonical project memory. Research maintains this register after the initial installation.

## Endpoints

| Context | Outbox | Recipient state |
| --- | --- | --- |
| Research | `research/outbox/` | `research/state.md` |
| Operations | `operations/outbox/` | `operations/state.md` |

## Director contribution register

`research/director-log.md` holds every contribution currently required from the Research Director, with a stable `RD-###` identifier, its type, its status and the canonical document that receives the outcome. The Research Orchestrator maintains it, Operations proposes points through its outbox, and every `What I need from you` section is derived from it. `communication/PROTOCOL.md` defines its lifecycle.

## Active threads

| Thread | State | Objective | Expected message |
| --- | --- | --- | --- |
| `kce-research-operations-sync` | v0.3 released | Preserve release evidence and obtain substantive Research Director acceptance for Module 00, the five module hubs and the three Harness routes | RD-021, RD-022 and RD-023 contributions |

## Completed capsules

No completed capsules.
