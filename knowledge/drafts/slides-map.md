# Full Slide Deck mapped onto the Skriptum chapters

Analysis draft, no decisions taken. Sources are the Full Slide Deck (vault document `2026-07-14 Knowledge und Context Engineering Foliensatz`, 89 entries of which 6 are section dividers), the German Full Lecture Notes (`Knowledge, Context and Agentic Engineering (Skriptum)`, 10 chapters), and the CLARIAH-AT workshop document with its Slides companion for the current deck state (state 2026-08-19).

## Mapping

Coherent slide groups are collapsed into one row. Fit is rated `direct` where the Skriptum carries the same argument, `partial` where it carries a neighbouring or narrower claim, `thin` where a single sentence is the whole anchor.

| Slide or group | Skriptum chapter | Fit |
|---|---|---|
| Titel, Lernziele und Ablauf | front matter (Abstract, Lernziele) | direct |
| Einstiegsbeispiel Subagenten-Verifikation | 3.5, 5.1 | direct |
| Knowledge und Context Engineering (definition), Was ist eine Wissensbasis, was ist ein Wissenssystem | 2.3, 2.4, 9.1 | partial; *Wissenssystem* is a deck-only term, the Skriptum says Project Knowledge Base plus Governance |
| Obsidian und der Vault, Strukturmittel im Vault, Alternativen zu Obsidian, Obsidian einrichten, Demo Obsidian und Claude Code | none | unanchored |
| Claude Code als AI Harness, AI Harness, Einen AI Harness einrichten | 3.2 | direct; the five harness functions match one to one |
| Was ist der Agentic Loop | 3.3 | direct |
| LLMs = Jagged Alien Intelligence, Latent Program Space, Training Builds the Latent Program Space, Mechanistic Interpretability, LLMs as Retrieval-ish Systems | none; 3.1 only states that an LLM generates a token sequence | unanchored |
| The Assistant Is a Trained Interaction Persona | 3.1 | thin; one sentence on post-training stabilising assistant behaviour |
| Prompting Strategies: There Is No Prompt to Rule Them All | 2.2 | direct; same sources (Schulhoff, Battle und Gollapudi) and the same model-, task- and evaluation-dependence claim |
| Epistemische Asymmetrie | 5.1 | partial; the Skriptum argues external verification without the generator-evaluator identity argument |
| AI Agents gibt es schon länger als LLMs, Reinforcement Learning Agents und LLM-Agents, The Agent Vision (Semantic Web) | none | unanchored |
| AI Agents und Agentic AI (Sapkota) | 3.1 | direct; Sapkota is cited there |
| Beleg: Human as Dispatcher (Forschungsleitstelle) | 9.2 | direct |
| AI Agent Begriffe, Tool Use | 3.2, 3.4 | direct |
| Subagents | 3.5 | direct |
| AGENTS.md / CLAUDE.md, Wie schreibt man eine gute CLAUDE.md, CLAUDE.md, Projektspezifisches CLAUDE.md | 2.4 | thin; the Skriptum names the function (Agent Instruction Document) and carries no file conventions |
| Globale CLAUDE.md | none | unanchored |
| Agent Skill, Skills definieren, MCP, MCP vs Skills, A2A | none | unanchored |
| Warum AI Agents Context brauchen, Context Window 8K, Context Rot, Context Engineering Shapes the Working Context | 2.3 | direct; Context Window against Working Context and the Liu / Hong sources are shared |
| Markdown Makes Document Structure Explicit for LLMs | 2.4 | direct |
| Knowledge Documents Make Project Knowledge Reusable, Wissensdokumente | 2.4 | direct |
| Drei Dokumenttypen und ihre Diagnostik | 2.4 | direct, with terminology drift; the slide says Action Document, the Skriptum says Agent Instruction Document |
| Knowledge Engineering: Transfer- und Modellierungssicht | 2.4 | direct; Studer, Benjamins und Fensel cited on both sides |
| Der knowledge-Ordner: Funktion vor Dateiname | 2.4 | direct; the Skriptum prints its own `knowledge/` tree, which adds `codebook.md` and `governance.md` and drops `design.md` and `plan.md` |
| Daten als capta: Datenaufbereitung | 1.2 | direct |
| Glossar Datenarbeit mit generativen Modellen | 6.1, 6.3, 10.2 | partial; vocabulary overlaps, the Skriptum glossary is a different list |
| DIKW und Langefors, Elizitation, Wissenstransformationen, Wissensmodellierung/PIM/Projektmanagement, Research-Vault vier Achsen, Bootstrap Research-Vault, Modelling/Operationalising/Exploring, Schichtenmodell agentenlesbarer Wissensbasen, Epistemische Infrastruktur, Beleg KISUG | none | unanchored |
| These der Einheit | 2.1, 2.6 | partial; the four-level thesis matches, the harness and project-management framing does not |
| Was ist Promptotyping, Die vier Phasen | 4.1, 4.3 | direct; the Skriptum renames Exploration und Mapping to Exploration and Destillation to Distillation |
| Scholar-Centred Design und Requirements Engineering, Spec Driven Development | 4.2 | direct for Scholar-Centred Design, partial for Spec Driven Development, which the Skriptum only implies |
| Was lässt sich mit Promptotyping bauen | 4.1 | partial; the Skriptum lists artefact kinds without the six use-case types |
| Promptotyping: Exploring Vibe Coding before it was cool, Vibe Coding | none; the term appears once in the bibliography | unanchored |
| Was ist Governance im Wissenssystem | 9.1, 3.4 | direct |
| Critical Expert in the Loop | 5.2 | direct |
| Asymmetric Amplification | none | unanchored |
| Auftragsformulierung: Vom Ziel zum Kontext | 3.5 (check block), 2.2 | direct |
| Model Routing: Planning und Execution | none | unanchored |
| Workflows mit AI Agents umsetzen | 3.3, 3.4 | direct |
| Wie transformiert ein Agent Forschungsdaten | 3.3, 5.1 | partial; 3.3 separates model output, script transformation and human check without the determinism argument |
| Artefakte gegen den Bestand prüfen | 5.1 | direct |
| Fallbeispiel OCR-TEI-Pipeline (zbz-ocr-tei) | 6.1, 7.1 | partial; same project as the case study, different level of description |
| Fallbeispiel Archivdaten-Pipeline (M³GIM), Fallbeispiel Statischer Journal-Generator (ride-static) | none | unanchored |
| Hands-on in vier Schritten | none; chapter 7 carries a different hands-on | unanchored |
| Kernbotschaften | 2, 3, 5 | summary across chapters |

Section dividers (Vorbereitung, AI Agents, Knowledge und Context Engineering, Promptotyping, Governance und Skills, Workflows) carry no content and are excluded.

## Slides without an anchor in the Skriptum

36 content slides, grouped by theme.

- **Working environment and Obsidian** (5). Obsidian und der Vault als Arbeitsumgebung, Strukturmittel im Vault, Alternativen zu Obsidian, Obsidian einrichten, Demo Obsidian und Claude Code
- **LLM properties and interpretability** (5). LLMs = Jagged Alien Intelligence, Prompt Engineering: Finding Coordinates in a Latent Program Space, Training Builds and Shapes the Latent Program Space, Mechanistic Interpretability Tests Internal Representations, LLMs as Retrieval-ish Systems
- **Agent history and lineage** (3). AI Agents gibt es schon länger als LLMs, Reinforcement Learning Agents und LLM-Agents, The Agent Vision (Semantic Web)
- **Agent ecosystem standards** (5). Agent Skill, Skills definieren, MCP, MCP vs Skills, A2A
- **Knowledge theory and vault architecture** (10). Von Daten zu Information (DIKW und Langefors), Elizitation, Wissenstransformationen, Wissensmodellierung/PIM/Projektmanagement, Einen Research-Vault modellieren, Bootstrap Research-Vault, Modelling/Operationalising/Exploring, Schichtenmodell agentenlesbarer Wissensbasen, Epistemische Infrastruktur, Beleg KISUG
- **Remaining singles** (8). Globale CLAUDE.md, Promptotyping: Exploring Vibe Coding before it was cool, Vibe Coding, Asymmetric Amplification, Model Routing, Fallbeispiel M³GIM, Fallbeispiel ride-static, Hands-on in vier Schritten

Borderline cases counted as anchored rather than unanchored: The Assistant Is a Trained Interaction Persona and the four CLAUDE.md slides, each resting on a single sentence in 2.4 or 3.1.

## Zielfundus of the CLARIAH deck

Six planned slide texts are marked "Noch nicht im Deck" in the CLARIAH Slides document. All six have a Skriptum anchor, so none extends the unanchored list.

| Planned item | Skriptum chapter |
|---|---|
| System properties (tools, reasoning modes, harness effect on reliability) | 3.2, 3.4 |
| Zweig-Bestellzettel model output with review questions and model-selection note | 6.1 (partial; the Skriptum source is Hersch, the slide uses Zweig) |
| Context Engineering chapter opener, from a prompt to the complete information environment | 2.3 |
| Knowledge document property *Revisable* | 2.4 |
| Promptotyping extends Knowledge Engineering, with write-back | 4.1, 4.4 |
| An AI harness operationalizes the feedback loop | 3.2, 3.3 |

## Skriptum chapters with no or thin slide coverage

| Chapter | Coverage in the Full Slide Deck |
|---|---|
| 1. Forschungsdaten, Repräsentation und Provenienz | thin; only 1.2 is covered by the capta slide. 1.1 (Forschungsdaten as project-bound term), 1.3 (Primär-, Intermediär-, Meta- und Paradaten) and 1.4 (Provenienz, PROV-O) have no slide at all |
| 5. Verifikation, Validierung und Critical Expert | partial; 5.1 and 5.2 are covered, 5.3 (Assessment Result und Scholarly Decision), 5.4 (three status axes) and 5.5 (Acceptance und Publication) have none |
| 6. Vom Faksimile zum Forschungsdatenpaket | uncovered; only the zbz-ocr-tei case-study slide and parts of the data glossary touch it |
| 7. Hersch-Fallstudie | uncovered; the Full Slide Deck carries no slide of the tutorial. The CLARIAH deck covers it in full |
| 8. Topic Annotation und statistisches Topic Modeling | uncovered; no slide in the Full Slide Deck. The CLARIAH deck has one slide |
| 9. Project Governance und Forschungsleitstelle | partial; 9.1 and 9.2 are covered, 9.3 (Klärung zur Umsetzung), 9.4 (verification by object and error risk) and 9.5 (minimal exchange and synchronisation) have none |
| 10. Grenzen, Glossar und Referenzen | thin; the data glossary slide is a different vocabulary, the methodological limits of 10.1 appear on no slide |

Chapters 2, 3 and 4 are the well covered part, each with several direct anchors and no gap worth naming.

## Verdict

Deck and script overlap on a stable core and diverge at both ends. The four engineering levels, the harness and agentic loop, and Promptotyping (chapters 2 to 4) are carried by direct slide anchors on nearly every section, so a derivation from the Full Slide Deck can teach those chapters without new material. Beyond that core the two artefacts pull apart in opposite directions. The Full Slide Deck invests heavily in material the Skriptum never took up, above all the Obsidian and vault-architecture line, the LLM-property and interpretability line, the agent-history line and the ecosystem standards (MCP, A2A, Skills), which together account for 36 unanchored slides, roughly two fifths of the fund. The Skriptum in turn built out the research-data half (chapters 1, 5 to 8) that the Full Slide Deck never had, and the Hersch tutorial now sits in the CLARIAH deck. The alignment gap is therefore a division of labour that hardened over time. No case exists where slide and chapter assert different things; the substantive divergences amount to terminology drift at two points (Action Document against Agent Instruction Document, Wissenssystem against Project Knowledge Base plus Governance) and one differing `knowledge/` file list.
