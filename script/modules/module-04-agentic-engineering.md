---
title: Agentic Engineering
module: 4
source-language: [de, en]
status: draft
created: 2026-08-20
units: [M10, M12]
canonical: false
canonical-gate: operator confirmation of the module cut
source-lecture-notes: [script/full-lecture-notes-de.md, script/full-lecture-notes-en.md]
---

# Module 4 — Agentic Engineering

> Draft cut of the full corpus. Every passage below is reproduced verbatim from the Full
> Lecture Notes; only the module heading, the unit headings and the provenance lines are added.
> The Full Lecture Notes stay authoritative until the operator confirms the cut. Coverage, discarded
> parallel versions and open questions are recorded in `script/COVERAGE.md`.


## Unit M10 — Agentic Engineering, AI Harnesses and Controlled Agent Workflows

*Source: `full-lecture-notes-de.md`, sections 2.3 and 2.4.*

## 2.3 Vom Modell zum Agenten

Ein isolierter Modellaufruf erzeugt eine Ausgabe. Ein Agent verfolgt dagegen ein Ziel über mehrere Modell- und Werkzeugaufrufe hinweg. Er kann seine Umgebung untersuchen, eine Handlung auswählen, das Ergebnis beobachten und sein Vorgehen aktualisieren.

Im Editionsbeispiel kann ein Agent:

1. den Projektordner untersuchen,  
2. die editorischen Richtlinien lesen,  
3. eine TEI-Datei erzeugen,  
4. einen Validator ausführen,  
5. die Fehlermeldung analysieren,  
6. die Datei korrigieren,  
7. eine Transformation starten,  
8. das Frontend prüfen,  
9. offene fachliche Fragen dokumentieren.

Das LLM bildet dabei das flexible Planungs- und Interpretationsmodul. Seine tatsächlichen Handlungsmöglichkeiten entstehen erst durch Werkzeuge und eine Arbeitsumgebung.

## 2.4 Das AI Harness

Ein **AI Harness** ist die technische Software-Schicht, über die ein LLM-basierter Agent Kontext erhält, Werkzeuge aufruft, auf Dateien zugreift, Programme ausführt und Rückmeldungen verarbeitet. Systeme wie Claude Code, Codex oder Cursor stellen unterschiedliche Formen eines solchen Harness bereit.[^3]

Das Harness kann beispielsweise festlegen:

- welche Ordner gelesen oder verändert werden dürfen;  
- welche Befehle ohne Bestätigung ausgeführt werden können;  
- wie Werkzeugausgaben in den Modellkontext zurückgelangen;  
- wie lange ein Lauf fortgesetzt wird;  
- wann ein Mensch einbezogen werden muss;  
- wie Zwischenergebnisse gespeichert werden.

Das Harness stellt technische Kontrollmöglichkeiten bereit. Es entscheidet jedoch nicht, ob eine editorische Modellierung wissenschaftlich angemessen ist. Ein XML-Validator kann feststellen, dass `<unclear>` an einer bestimmten Stelle zulässig ist. Er kann nicht entscheiden, ob die Quelle tatsächlich unleserlich ist oder ob eine alternative Lesung wahrscheinlicher wäre.

*Source: `full-lecture-notes-en.md`, "AI Agents Existed Long Before LLMs".*

## **AI Agents Existed Long Before LLMs**

The concept of an **intelligent agent** predates large language models by decades. Classical work defines agents through their relationship with an environment and their capacity for autonomous, reactive and goal directed action.[^45]

Wooldridge and Jennings identify properties such as autonomy, reactivity, proactiveness and social ability. Earlier AI systems such as AlphaGo and multi agent reinforcement learning environments demonstrate that agency is not intrinsically tied to language models.

LLMs changed the practical design space because natural language, code and heterogeneous digital resources can now become part of a common interface for planning and action. Systems such as *Voyager* demonstrated how an LLM can guide an embodied agent through repeated interaction with a complex environment.[^46]

LLM based agents should therefore be understood as a contemporary form of a much older AI concept.

*Source: `full-lecture-notes-de.md`, sections 6.1 through 6.7.*

## 6.1 Warum mehrschrittige Arbeit organisiert werden muss

Mit wachsender Aufgabendauer steigt nicht nur die mögliche Leistung eines Agents, sondern auch die Zahl der Stellen, an denen Fehler in spätere Schritte eingehen können.

Ein Agent liest eine veraltete Richtlinie, erzeugt daraufhin ein ungeeignetes TEI-Muster, transformiert dieses in HTML und passt anschließend das Frontend an die falsche Struktur an. Jeder einzelne Schritt kann technisch plausibel wirken. Der ursprüngliche Fehler wird dennoch über die gesamte Arbeitstrajektorie fortgeschrieben.

**Agentic Engineering** bezeichnet die systematische Organisation und Kontrolle mehrschrittiger agentischer Arbeit. Es betrifft:

- Abgrenzung und Zerlegung von Aufgaben,  
- Werkzeugnutzung,  
- Verarbeitung von Zwischenergebnissen,  
- Zustände und Übergaben,  
- Abbruch- und Eskalationsbedingungen,  
- Prüfung und Fortführung.

Die zentrale Frage lautet nicht nur, ob ein Agent handeln kann, sondern unter welchen Bedingungen seine Handlungen nachvollziehbar, begrenzt und korrigierbar bleiben.

## 6.2 Agentische Ausführungsschleife

Eine vereinfachte Ausführungsschleife lautet:

**Abbildung 10: Agentische Ausführungsschleife.**  
*Der Agent erfasst den aktuellen Projektzustand, plant einen begrenzten nächsten Schritt, verwendet ein Werkzeug, beobachtet dessen Ergebnis und aktualisiert sein Vorgehen. Der Zyklus bleibt an dokumentierte Anforderungen, Berechtigungen, Abbruchbedingungen und menschliche Interventionspunkte gebunden.*

> **Zustand erfassen → nächsten Schritt planen → Werkzeug oder Aktion ausführen → Ergebnis beobachten → Vorgehen aktualisieren**

Im Editionsprojekt:

1. Agent liest Aufgabe und relevante Wissensdokumente.  
2. Agent untersucht die vorhandene Transkription.  
3. Agent erzeugt TEI.  
4. Agent führt Schema-Validierung aus.  
5. Agent liest Fehlermeldungen.  
6. Agent korrigiert technische Fehler.  
7. Agent dokumentiert verbleibende fachliche Unsicherheiten.  
8. Agent transformiert TEI in HTML.  
9. Agent prüft die Darstellung.  
10. Agent schlägt Write-back vor.

Autonomie bezeichnet dabei den Umfang der Arbeit zwischen zwei menschlichen Eingriffen. Sie bedeutet nicht Abwesenheit menschlicher Kontrolle.

## 6.3 Planung, Ausführung und Feedback

Komplexe Aufgaben können in Planung und Ausführung getrennt werden. Ein Plan sollte bestimmen:

- welche Teilprobleme vorliegen,  
- welche Informationen fehlen,  
- welche Werkzeuge benötigt werden,  
- welche Prüfungen vorgesehen sind,  
- welche Reihenfolge sinnvoll ist.

Planung ist jedoch kein Selbstzweck. Ein umfangreicher Plan vor der Untersuchung des Projektbestands kann falsche Sicherheit erzeugen. Gute Pläne sind kompakt, gegen den aktuellen Zustand prüfbar und revidierbar.

Feedback kann aus unterschiedlichen Quellen stammen:

- Validatoren,  
- Tests,  
- Fehlermeldungen,  
- Werkzeugausgaben,  
- Reviews anderer Agents,  
- menschliche Rückmeldungen,  
- veränderte Anforderungen.

Agentic Engineering organisiert, wie dieses Feedback in weitere Schritte überführt wird.

## 6.4 Werkzeuge, Berechtigungen und Reversibilität

Werkzeuge erweitern ein LLM von einem Textgenerator zu einem System, das auf eine Umgebung einwirken kann. Dazu gehören:

- Dateizugriff,  
- Terminal,  
- Codeausführung,  
- Websuche,  
- Datenbankabfragen,  
- Browsersteuerung,  
- Validatoren,  
- spezialisierte APIs.

Ein Werkzeugaufruf kann den Projektzustand verändern. Daher sollten Zugriffe nach dem Prinzip der geringsten erforderlichen Berechtigung vergeben werden.

Im Editionsprojekt:

- Quelldateien dürfen gelesen, aber nicht überschrieben werden.  
- Generierte TEI-Dateien dürfen in einem Arbeitsordner verändert werden.  
- Schema-Validatoren dürfen ohne Bestätigung laufen.  
- Veröffentlichungs- oder Deployment-Schritte benötigen eine explizite Freigabe.  
- Änderungen sollten versioniert und reversibel bleiben.

## 6.5 MCP, Subagents und Agent-to-Agent-Kommunikation

Das **Model Context Protocol (MCP)** standardisiert die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Ein MCP-Server kann beispielsweise Zugriff auf ein Repository, eine Datenbank oder einen Validator bereitstellen.[^5]

MCP löst ein technisches Integrationsproblem. Es entscheidet nicht, ob ein Werkzeug für die Aufgabe geeignet ist oder wie seine Ergebnisse fachlich interpretiert werden.

Ein **Subagent** ist eine abgegrenzte Agenteninstanz mit einer Teilaufgabe. Im Editionsprojekt könnten parallel arbeiten:

- ein Agent für Datenprofil und TEI-Struktur,  
- ein Agent für Schema-Validierung,  
- ein Agent für Frontend-Tests,  
- ein Agent für den Vergleich von Anforderungen und Implementation.

Mehr Agents erzeugen nicht automatisch bessere Ergebnisse. Sie erhöhen Koordinations- und Prüfaufwand. Jeder Subagent benötigt einen klaren Auftrag, begrenzten Kontext, ein definiertes Rückgabeformat und Regeln für Unsicherheit.

Agent-to-Agent-Protokolle verbinden eigenständige Agents. Die methodischen Fragen bleiben:

- Welche Zuständigkeit besitzt jeder Agent?  
- Welche Informationen werden übergeben?  
- Wie werden Konflikte sichtbar?  
- Wer entscheidet bei widersprüchlichen Ergebnissen?

## 6.6 Versionierte Zwischenstände und menschliche Intervention

Mehrschrittige Arbeit sollte in überprüfbaren Inkrementen erfolgen. Ein sinnvoller Zwischenstand ist:

- ausführbar oder untersuchbar,  
- einem definierten Projektzustand zuordenbar,  
- gegen Anforderungen prüfbar,  
- klein genug, um Fehlerursachen zu rekonstruieren.

Zwischenergebnisse sollten nicht ausschließlich im Chatverlauf verbleiben. Relevante Pläne, Entscheidungen, Prüfergebnisse und offene Fragen gehören in persistente Projektartefakte.

Typische menschliche Interventionspunkte sind:

- widersprüchliche Anforderungen,  
- fehlende fachliche Grundlagen,  
- schwer reversible Änderungen,  
- sensible Ressourcen,  
- fachlich folgenreiche Modellierungsentscheidungen,  
- Validierung und Acceptance.

Agents können Evidenz sammeln. Sie übernehmen dadurch nicht automatisch die Autorität, ein Ergebnis fachlich zu validieren oder für einen Zweck zu akzeptieren.

## 6.7 Hands-on: TEI erzeugen, validieren und ein Frontend implementieren

### Teil A: TEI erzeugen

Der Agent erhält:

- Seitenbild,  
- Rohtranskription,  
- Wissensdokumente,  
- Schema,  
- zwei geprüfte Beispiele.

Auftrag:

1. TEI erzeugen,  
2. Schema validieren,  
3. technische Fehler korrigieren,  
4. fachliche Unsicherheiten separat dokumentieren.

### Teil B: Frontend implementieren

Das lokale Frontend soll zeigen:

- Faksimile,  
- diplomatische Transkription,  
- normalisierte Ansicht,  
- Unsicherheiten,  
- Annotationen.

### Teil C: Rückkopplung prüfen

Fragen:

- Sind Seiten- und Zeilenwechsel sichtbar?  
- Werden Unsicherheiten als Unsicherheiten dargestellt?  
- Erzeugt die Oberfläche falsche Eindeutigkeit?  
- Welche Modellierungsprobleme werden erst im Interface sichtbar?  
- Welche Wissensdokumente müssen revidiert werden?

*Source: `full-lecture-notes-en.md`, "AI Harness Architecture" and "AI Agent Concepts".*

## **AI Harness Architecture**

A useful systems perspective treats the harness as the runtime substrate that enables a foundation model to operate as an agent. Zhong and Zhu argue that software engineering capability arises from a **model, harness and environment system** rather than from the model in isolation.[^12]

The harness can manage task specification, context selection, file and tool access, action execution, current state, feedback, permissions, verification and intervention points. This changes what should be evaluated. A final patch, document or answer provides only partial evidence about the process that produced it.

A stronger harness can preserve execution traces, test results, failure information and other evidence that makes an agentic trajectory inspectable and easier to continue or correct.

## **AI Agent Concepts**

Several technical concepts recur across contemporary agent systems. **Tool Use** connects models with executable functions and external resources. **AI Harnesses** organise the runtime environment. **Instruction files** such as `AGENTS.md` or `CLAUDE.md` provide persistent project guidance. **Agent Skills** package reusable procedural knowledge. **MCP** standardises connections to tools and resources. **A2A** standardises communication among independent agents. **Subagents** provide isolated contexts for delegated tasks.[^47]

These concepts solve different problems. They should not be treated as interchangeable labels for “agent functionality”. The engineering task is to decide which mechanism should carry which type of information or capability.

*Source: `full-lecture-notes-en.md`, "AGENTS.md and CLAUDE.md" through "Agent Skill".*

## **AGENTS.md and CLAUDE.md**

`AGENTS.md` is an open Markdown based format for providing coding agents with project specific instructions such as setup commands, tests, code conventions and repository guidance.[^48] `CLAUDE.md` is the corresponding Claude Code mechanism for persistent project, user or organisation level instructions.[^49]

The formats should not be collapsed. Different tools implement different discovery and precedence rules. Claude Code reads `CLAUDE.md` natively and can import an existing `AGENTS.md`; the broader `AGENTS.md` format is intended to work across many coding agents.[^48][^49]

The methodological principle is broader than either file name. Information that should guide an agent repeatedly should not have to be typed into every prompt. Persistent instruction artefacts externalise stable working rules and make them inspectable and versionable.

## **Global CLAUDE.md**

Claude Code supports persistent instructions at several scopes. User level instructions can be stored in `~/.claude/CLAUDE.md` and apply across projects, while organisation managed policies and local variants provide additional layers.[^49]

A global or user level instruction file should contain information that is genuinely stable across projects, such as preferred working practices, communication conventions or general completion criteria. Project specific facts should remain in the project environment rather than being duplicated globally.

This is not a hard security mechanism. Claude Code documentation explicitly distinguishes behavioural guidance in `CLAUDE.md` from permissions and hooks, which can enforce technical boundaries independently of model compliance.[^49]

## **Project Specific CLAUDE.md**

A project specific `CLAUDE.md` can be stored at the repository root or in `.claude/CLAUDE.md`. It provides persistent project context such as architecture, build and test commands, conventions and workflows.[^49]

A compact project instruction file might contain a role and working mode, implementation principles, explicit completion criteria and references to more detailed project knowledge. For example, it can require that verification be run before a task is reported as complete and that any unavailable verification is stated explicitly.

Claude Code treats these files as context, not as infallible configuration. Project instructions therefore need to remain concise, specific and internally consistent. Procedural content that is only relevant for particular tasks may be better represented as a Skill rather than loaded in every session.[^49]

## **Agent Skill**

An **Agent Skill** is a reusable folder containing a `SKILL.md` file and, optionally, scripts, references and assets for a particular capability or workflow.[^50] Skills are procedural artefacts rather than merely descriptive knowledge documents.

The Agent Skills specification uses **progressive disclosure**. At session start, the agent can receive only the name and description of available skills. The full instructions are loaded when the skill becomes relevant, and additional resources can be loaded later as required.[^50]

This design helps control context consumption. A system can maintain many specialised capabilities without injecting all instructions into every task. Examples include skills for producing a PowerPoint presentation, reviewing a legal document or applying a project specific data transformation procedure.

*Source: `full-lecture-notes-en.md`, "Model Routing" and "Subagents and Epistemic Infrastructure".*

## **Model Routing**

Agentic workflows can route different phases of work to different models. Planning, implementation and review do not necessarily require the same model or the same inference budget.

One useful pattern is:

`research → specification → implementation → review → revision`

Planning and review can be assigned to a model selected for stronger reasoning, while implementation can be assigned to a model that offers a favourable balance of coding capability, latency and cost. The resulting specification remains contextualised by project knowledge rather than becoming an isolated prompt.

Model routing should be treated as an engineering decision that can change as models evolve. The important abstraction is the separation of functions and evaluation criteria, not any particular provider combination.

## **Subagents and Epistemic Infrastructure**

A multi agent workflow becomes methodologically interesting when specialised agents operate against an explicit **epistemic infrastructure**. For example, one agent may coordinate several independent reviewers that inspect TEI XML using project knowledge, schemas and deterministic Python scripts.

The additional agents do not create truth by voting. Independent review can expose disagreements, locate suspicious cases and distribute inspection across different contexts. The evidence returned by schemas, tests, source comparisons and domain specific knowledge remains more important than model agreement by itself.

The purpose of multi agent orchestration is therefore to create structured trajectories of independent work and feedback, not merely to multiply model calls.


## Unit M12 — Promptotyping and Scholar-Centred Design

*Source: `full-lecture-notes-de.md`, sections 7.1 through 7.6.*

## 7.1 Definition und Grundprinzip

Promptotyping ist eine iterative, dokumentenbasierte Methode zur Entwicklung projektspezifischer digitaler Forschungsartefakte mit LLM-basierten AI Agents.

Der Begriff bezeichnet nicht lediglich das Erzeugen eines Prototyps durch Prompts. Im Mittelpunkt steht die gemeinsame Entwicklung von:

- dokumentiertem Projektverständnis,  
- digitalem Forschungsartefakt,  
- Prüfverfahren,  
- begrenzten Gründen der Akzeptanz.

Der grundlegende Zyklus lautet:

**Abbildung 11: Promptotyping als geschlossener Entwicklungszyklus.**  
*Projektwissen wird für eine Aufgabe in einen Working Context überführt und durch einen Agenten in ein digitales Forschungsartefakt operationalisiert. Verification und Validation erzeugen Evidenz und neue Erkenntnisse. Write-back führt diese Erkenntnisse in Wissensdokumente, Anforderungen und Modelle zurück.*

> **Projektwissen → Working Context → agentische Implementation → digitales Forschungsartefakt → Prüfung → Revision des Projektwissens**

Das Artefakt und das dokumentierte Projektverständnis entwickeln sich gemeinsam weiter.

## 7.2 Preparation

Preparation macht Daten, Quellen, Standards und Forschungskontext zugänglich.

Für die digitale Edition umfasst dies:

- Seitenbilder beschaffen und eindeutig benennen;  
- Provenienz dokumentieren;  
- vorhandene Transkriptionen sichern;  
- Richtlinien und Schema-Versionen sammeln;  
- Ausgangsdateien vor Veränderungen schützen;  
- Projektstruktur anlegen.

Preparation ist mehr als Dateiverwaltung. Sie schafft einen nachvollziehbaren Ausgangszustand.

## 7.3 Exploration

Exploration untersucht, was die Daten und Quellen ermöglichen und begrenzen.

Im Editionsprojekt kann sie zeigen:

- welche Seitentypen vorliegen;  
- welche Schriften und Layouts auftreten;  
- welche wiederkehrenden editorischen Phänomene vorhanden sind;  
- wo die Rohtranskription unsicher ist;  
- welche Anforderungen das Frontend an das Modell stellt.

Exploration erzeugt noch keine endgültige Spezifikation. Sie macht sichtbar, welche Fragen geklärt und welche Entscheidungen dokumentiert werden müssen.

## 7.4 Distillation

Distillation überführt das entwickelte Verständnis in gepflegte Dokumente:

- `source-description.md`  
- `transcription-rules.md`  
- `tei-model.md`  
- `requirements.md`  
- `design.md`  
- `verification.md`

Diese Dokumente bilden die Grundlage weiterer agentischer Arbeit. Sie bleiben revidierbar, weil neue Erkenntnisse aus der Implementation frühere Annahmen verändern können.

## 7.5 Requirements Engineering und Scholar-Centred Design

Requirements Engineering macht explizit, was ein Artefakt leisten soll. In einem wissenschaftlichen Projekt reicht es nicht, „eine schöne digitale Edition“ zu verlangen.

Anforderungen können lauten:

- Faksimile und Transkription müssen eindeutig zugeordnet sein.  
- Diplomatische und normalisierte Lesung müssen unterscheidbar bleiben.  
- Unsichere Lesungen dürfen nicht wie sicherer Text erscheinen.  
- Editorische Eingriffe müssen nachvollziehbar sein.  
- Quelldaten dürfen nicht stillschweigend verändert werden.  
- Das Artefakt muss lokal und ohne proprietären Dienst ausführbar sein.

**Scholar-Centred Design** richtet die Entwicklung an den Forschungspraktiken, Interpretationsaufgaben und Verantwortlichkeiten der beteiligten Wissenschaftler:innen aus. Es fragt nicht nur, ob eine Oberfläche benutzbar ist, sondern welche wissenschaftlichen Unterscheidungen sie sichtbar oder unsichtbar macht.

## 7.6 Implementation

Implementation macht die Wissensbasis handlungsfähig. Der Agent übersetzt dokumentierte Anforderungen in:

- TEI-Dateien,  
- Transformationsskripte,  
- Stylesheets,  
- Tests,  
- ein lokales Frontend,  
- Dokumentation.

Implementation ist keine neutrale Ausführung einer vollständig bestimmten Spezifikation. Erst durch das funktionierende Artefakt kann sichtbar werden, dass eine Regel fehlt oder eine Modellierung zu grob ist.

Ein Beispiel: Im TEI-Modell werden alle unsicheren Lesungen gleich behandelt. Im Frontend zeigt sich jedoch, dass zwischen „teilweise lesbar“, „editorisch ergänzt“ und „vollständig unleserlich“ unterschieden werden muss. Diese Erkenntnis gehört nicht nur in den Code, sondern zurück in das Wissensdokument und gegebenenfalls in das Datenmodell.

*Source: `full-lecture-notes-de.md`, sections 7.9 and 7.10.*

## 7.9 Write-back

Implementation und Prüfung erzeugen neues Wissen. Dieses Wissen muss in die zuständigen Dokumente zurückgeschrieben werden.

Mögliche Write-backs:

- Transkriptionsregel präzisieren;  
- neuen Unsicherheitstyp ergänzen;  
- Datenmodell revidieren;  
- Designentscheidung begründen;  
- bekannte Einschränkung dokumentieren;  
- Verifikationskriterium erweitern.

Write-back verhindert, dass relevantes Wissen nur im Chat, im Code oder im Gedächtnis einzelner Personen verbleibt.

## 7.10 Der Promptotype

Ein **Promptotype** ist der dokumentierte und referenzierbare Zustand einer Iteration. Er umfasst:

- den relevanten Stand der Project Knowledge Base,  
- das digitale Forschungsartefakt,  
- den referenzierten Datenzustand,  
- dokumentierte Prüfungen,  
- offene Fragen,  
- die begrenzten Gründe der Acceptance.

Ein Promptotype ist kein endgültiges Produkt. Er ist ein hinreichend bestimmter Zustand, von dem weitere Arbeit ausgehen kann.

*Source: `full-lecture-notes-en.md`, "As a ... I Want to".*

## **As a … I Want to**

User stories provide a compact requirements engineering format for expressing how a person should be able to work with an artefact:

```text
As a ...
I want to ...
so that I can ...
```

The format makes three questions explicit. Who is acting? What capability is required? Why does the capability matter? In research software, this connects implementation requirements directly to scholarly practice.[^42]

A liturgy scholar may want to compare the structure of an office across several *Libri Ordinarii* to identify regional differences. A social historian may want to compare network change across several decades to investigate changing economic relationships. The data model alone does not determine these operations. Requirements arise from the relation among data, research questions and scholarly practices.

*Source: `full-lecture-notes-en.md`, "Mapping Mobile Musicians".*

## **Mapping Mobile Musicians**

*Mapping Mobile Musicians* provides an example of how maintained knowledge and project specific artefacts can support several distinct scholarly activities. The project can be understood through four operations: **capture**, **curate**, **understand** and **explore**.

These operations require different representations and different working contexts. Capturing source information requires attention to provenance and extraction. Curation requires decisions about entities, relations and uncertainty. Understanding requires domain context and interpretation. Exploration requires interfaces and analytical operations that reflect scholarly questions.

The example therefore illustrates why an AI supported knowledge environment cannot be reduced to a single prompt or one static database. Different phases of work require different combinations of data, knowledge, tools and validation.

*Source: `full-lecture-notes-en.md`, "Spec Driven Development".*

## **Spec Driven Development**

**Spec Driven Development** places an explicit specification between exploratory discussion and implementation. Instead of asking an agent to “build something useful”, the workflow develops a structured account of requirements, user stories, data constraints, interfaces and verification criteria before substantial implementation begins.

The specification should be contextualised by the maintained knowledge environment rather than treated as a detached document. Data descriptions, research knowledge, design decisions and validation rules can remain in dedicated knowledge documents while the specification references the parts relevant to the implementation task.

This reduces the amount of tacit interpretation delegated to the agent and creates a clearer object for review before code or other artefacts are produced.


## Notes

*Footnote identifiers and definitions are reproduced unchanged from their source lecture notes.*

### Notes carried from the German Full Lecture Notes

[^3]: Produktbezeichnungen und konkrete Funktionen agentischer Arbeitsumgebungen verändern sich schnell. Die im Skriptum genannten Systeme dienen als Beispiele; Funktionsumfang und Terminologie sollten vor einer Publikation gegen die jeweils aktuelle Dokumentation geprüft werden.

[^5]: MCP bezeichnet eine technische Spezifikation für die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Die konkrete Sicherheits- und Berechtigungsarchitektur hängt von der jeweiligen Implementation ab.

### Notes carried from the English Full Lecture Notes

[^12]: Hailin Zhong and Shengxin Zhu, “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents,” 2026, https://doi.org/10.48550/arXiv.2605.13357.

[^42]: Christopher Pollin, *Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example*, Graz, 2025, https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602.

[^45]: Michael Wooldridge and Nicholas R. Jennings, “Intelligent Agents: Theory and Practice,” *The Knowledge Engineering Review* 10, no. 2, 1995, https://doi.org/10.1017/S0269888900008122.

[^46]: Guanzhi Wang et al., “Voyager: An Open Ended Embodied Agent with Large Language Models,” 2023, https://arxiv.org/abs/2305.16291.

[^47]: For the individual concepts see the official documentation referenced in footnotes 48 to 52.

[^48]: AGENTS.md, https://agents.md.

[^49]: Anthropic, “How Claude Remembers Your Project,” Claude Code Docs, https://code.claude.com/docs/en/memory.

[^50]: Agent Skills, https://agentskills.io and https://agentskills.io/specification.
