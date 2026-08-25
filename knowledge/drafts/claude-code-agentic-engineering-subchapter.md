# Claude Code as a Case Study in Agentic Engineering

Editorial proposal for the Full Slide Deck. The canonical slide export and both Full Lecture Notes remain unchanged. The intended format is a compact talk sequence with one claim and one visual object per slide.

## Editorial conclusion

The source set supports a coherent subchapter on Claude Code inside Agentic Engineering. Its didactic value lies in making the complete system observable. Claude Code connects a model with persistent instructions, selected project context, tools, an executable environment, feedback and intervention mechanisms.

The subchapter should apply concepts that the deck already defines. It should show how Prompt Engineering, Knowledge Engineering, Context Engineering and Agentic Engineering meet inside one harness. Installation belongs at the transition into the practical setup path. Product surfaces, model versions and command inventories belong in reference material because they change faster than the conceptual argument.

## Source assessment

| Source | Contribution | Limitation | Editorial use |
| --- | --- | --- | --- |
| `Wissensdokument_ AI Harness, Context, Knowledge und Agentic Engineering.md` | Clear system model connecting instructions, knowledge, context, tools, feedback, validation and verification | Substantial overlap with the Full Lecture Notes | Organising frame and terminology check |
| `25 Aug at 16_32.md` | Feature discovery from an official introductory webinar, including `CLAUDE.md`, context management, Plan Mode, screenshots and runtime intervention | Automatic transcript with recognition errors, duplicated passages and imprecise product claims | Discovery source whose product claims require verification |
| `25 Aug at 17_08.md` | Further feature discovery on MCP, Skills, Plugins, context strategies, parallel sessions, Subagents and Remote Control | Automatic transcript with systematic product-name errors and several claims marked as uncertain by the speaker | Discovery source for the tutorial and optional reference slides; commands verified independently |
| `UI-SPECIFICATION.md` | Project example that separates invariants, decision points and acceptance checks for one bounded UI task | Represents an earlier design state and conflicts with several accepted project decisions | Example of task-scoped instructions and drift control, not a new project authority |
| Five slide montages supplied with the transcript | Evidence of the source presentation's sequence and interface examples | Several claims per montage, repeated Plan Mode and `CLAUDE.md`, small screenshots, volatile versions and external visual rights | Composition critique and screenshot brief only |
| Further supplied screenshots on MCP, Skills, Plugins and context strategies | Product vocabulary and a compact comparison of extension mechanisms | Cropped source slides, volatile commands and external visual rights | Topic discovery and terminology check only |
| Full Slide Deck export | Existing conceptual line and current placeholders for Claude Code | Export state whose header excludes editorial changes below it | Placement and redundancy check |
| Full Lecture Notes | Maintained definitions of Agentic Engineering, AI Harness, instruction files, tools, permissions and human control | Claude Code remains an example among several harnesses | Conceptual authority for the new slide sequence |
| Official Claude Code documentation, checked 2026-08-25 | Current installation, instruction hierarchy, context behaviour, permission modes, controls and data handling | Product details remain versioned and require rechecking before publication | Authority for all product-specific claims |

## Montage analysis

| Supplied montage | Useful material | Editorial decision |
| --- | --- | --- |
| `(2)` agent definitions, evolution and agentic coding frontier | General distinction between an LLM feature, a workflow and an agentic loop | Keep in the existing Agentic Engineering introduction. Omit the product forecast from the Claude Code subchapter. |
| `(3)` introduction, software lifecycle and execution surfaces | Claude Code as a harness that can inspect a project and act across a task lifecycle | Retain one opening case-study slide. Remove the software lifecycle matrix from the general knowledge-work route and move the surface comparison to an optional reference. |
| `(4)` IDE integration and `CLAUDE.md` | Persistent project instructions and the relationship between editor, terminal and project files | Build one conceptual `CLAUDE.md` slide. Correct the hierarchy model and keep IDE setup on the Preparation page. |
| `(5)` model selection, context and Plan Mode | Context inspection, compaction and planning before modification | Give Context Management and Plan Mode one slide each. Move model selection to the model-routing appendix. Remove the duplicate Plan Mode composition. |
| `(6)` screenshots, shell mode, interrupt and rewind | Visual evidence, runtime steering and reversibility | Keep visual feedback and intervention in the conceptual sequence. Move shell mode to a command reference. |

## Corrections required before reuse

1. **`CLAUDE.md` and auto memory are separate mechanisms.** `CLAUDE.md` contains persistent instructions written and maintained by people. Auto memory stores notes that Claude Code creates for later sessions. Calling `CLAUDE.md` a memory file obscures this distinction.
2. **Instruction files are concatenated into context.** Files closer to the working directory are read later. The system does not implement a general mechanical override rule. Conflicts still require clear and consistent instructions.
3. **Plan Mode is a permission mode.** Claude Code may inspect files and run exploratory commands while source edits remain blocked. An approved plan changes the permission mode for subsequent implementation.
4. **Compaction summarises session history.** Project-root `CLAUDE.md` instructions and unscoped rules are re-injected from disk. Nested and path-scoped instructions return when the corresponding files are read again.
5. **The webinar's data-retention statement is too broad.** Local execution still sends prompts and selected content to the configured model provider. Server retention depends on account type and privacy settings. Claude Code also stores local plaintext transcripts by default. A security slide must use the current data-usage documentation.
6. **Model names, version numbers and interface chrome are volatile.** They should remain outside the conceptual core. A model-selection example belongs in a model-routing appendix after its learning purpose is defined.
7. **Subagents and parallel sessions solve different coordination problems.** A Subagent works inside one main assignment and returns a result from its isolated context. A parallel session is an independent top-level run. Concurrent writing sessions require separate worktrees or disjoint file areas before their results are reconciled.
8. **MCP tools can read and change external systems.** The protocol connection does not establish one uniform risk level. Each server, tool, credential and read or write effect requires its own scope and verification.
9. **Remote Control keeps execution on the local host.** The supported entry routes are currently `claude remote-control`, `claude --remote-control` and `/remote-control`. Availability and account requirements remain volatile because the feature is a research preview.

## Placement in the Full Slide Deck

The subchapter belongs after the generic definitions of Agentic Engineering, AI Harness and the agentic execution loop. It should establish one complete system before mapping the extension mechanisms and delegated contexts that support it. Detailed configuration belongs in the tutorial and reference material.

The existing Claude Code fragments should be consolidated in the later editorial pass.

- The generic agent history and evolution material remains in the Agentic Engineering introduction.
- The software development lifecycle matrix is omitted from the general knowledge-work deck.
- IDE, desktop, web and mobile surfaces move to an optional reference slide.
- The two Plan Mode examples become one slide about permission and planning.
- The repeated `CLAUDE.md` material becomes one conceptual slide plus one optional hierarchy reference.
- Model selection and shell mode move to the appendix.
- Screenshot input and runtime interruption remain because they demonstrate feedback and control.

## Proposed talk sequence

### 1. Claude Code als Fallstudie für Agentic Engineering

**Visible copy**

> Claude Code verbindet ein Modell mit Projektkontext, Werkzeugen, Ausführung und Feedback.

> `Modell + Harness + Umgebung → agentische Arbeit`

**Visual**

One cropped terminal state inside a violet Agentic Engineering frame. The screenshot shows a neutral project folder and a read-only request. Account names, personal paths, model versions and token counters remain outside the crop.

**Speaker note**

Claude Code dient als konkretes Beispiel für die zuvor eingeführte Systemebene. Die Fähigkeit entsteht aus dem Zusammenspiel von Modell, Harness und Projektumgebung. Der einzelne Prompt setzt ein Ziel. Das Harness stellt den Raum bereit, in dem daraus eine Folge beobachtbarer Handlungen wird.

### 2. Ein AI Harness organisiert eine Arbeitstrajektorie

**Visible copy**

> `beobachten → planen → handeln → prüfen → fortführen`

The visual labels the surrounding system with `Instructions`, `Context`, `Tools`, `Runtime`, `Permissions` and `Feedback`.

**Visual**

A single loop diagram. The project folder occupies the centre. Tool results return to the next model call as feedback. One human control point sits between inspection and continuation.

**Speaker note**

Die relevante Einheit ist die Arbeitstrajektorie über mehrere Modellaufrufe und Werkzeughandlungen. Dateien, Befehlsausgaben und Tests verändern den Zustand, auf den der nächste Schritt reagiert. Agentic Engineering bestimmt Aufgabenrahmen, Zugriffe, Prüfungen und Abbruchbedingungen für diese Trajektorie.

### 3. `CLAUDE.md` macht projektbezogene Arbeitsregeln persistent

**Visible copy**

> `CLAUDE.md` beschreibt, wie der Agent im Projekt arbeitet.

Four compact fields show `Scope`, `Project routes`, `Working rules` and `Completion checks`.

**Visual**

A small document beside the project folder. Arrows point from the instruction file to the session context and from the project knowledge base to task-specific file reads. The two artefact classes remain visually distinct.

**Speaker note**

Die Instruktionsdatei hält wiederkehrende Regeln und verweist auf den Wissensbestand. Sie ersetzt keine Project Knowledge Base. Ihr Inhalt wird als Kontext geladen und bleibt deshalb verhaltenssteuernde Instruktion. Technische Grenzen entstehen zusätzlich durch Berechtigungen, Hooks und die zugängliche Umgebung.

### 4. Skills, MCP und Plugins erfüllen unterschiedliche Funktionen

**Visible copy**

| Mechanismus | Funktion |
| --- | --- |
| Skill | Lädt ein wiederverwendbares Verfahren für eine Aufgabenklasse. |
| MCP | Verbindet das Harness mit externen Werkzeugen und Datenquellen. |
| Plugin | Bündelt Erweiterungen als installierbares Paket. |

> `Skill = Verfahren · MCP = Verbindung · Plugin = Paket`

**Visual**

One compact system map. The Skill points toward the working context, MCP crosses the boundary toward an external system and the Plugin encloses several extension components. `CLAUDE.md` remains beside the map as persistent project instruction and is not presented as a fourth package type.

**Speaker note**

Die drei Mechanismen bilden keine Hierarchie. Ein Skill stellt prozedurales Wissen und die dafür erforderlichen Ressourcen bei Bedarf bereit. Ein erprobter wiederkehrender Workflow kann in einen Skill überführt werden, sobald Trigger und Abschlussprüfung stabil sind. MCP standardisiert den Werkzeugzugriff auf externe Systeme. Ein Plugin verpackt Skills, Subagents, Hooks und MCP-Server für Installation, Versionierung und Verteilung. Die Auswahl beginnt beim konkreten Bedarf im Arbeitsprozess.

### 5. Context wird für den aktuellen Schritt kuratiert

**Visible copy**

> `Instructions + Files + Tool Outputs + History → Working Context`

> `/context` zeigt die Belegung. `/compact` fasst den Verlauf zusammen.

**Visual**

A finite context frame receives selected items from a larger project knowledge base. A small live `/context` crop may sit beside the diagram if it remains readable at presentation distance.

**Speaker note**

Das Context Window enthält nur den aktuellen Informationszustand. Projektwissen bleibt außerhalb verfügbar und wird bei Bedarf gelesen. Die beiden Befehle machen Context Management sichtbar. Der erste zeigt die Belegung, der zweite erzeugt eine verdichtete Fortsetzung des bisherigen Verlaufs.

### 6. Subagents arbeiten in abgegrenzten Kontexten

**Visible copy**

> Subagents bearbeiten klar begrenzte Recherchefragen in einem eigenen frischen Context Window.

> `Teilfrage + Quellenrahmen + Rückgabeformat → Recherche → Befund + Evidenz + Unsicherheit`

**Visual**

A fork-join diagram. The main agent delegates two distinct questions. Each branch enters its own fresh context and returns findings, evidence and uncertainty. The branches reunite at the main agent, whose three actions are `abgleichen`, `integrieren` and `prüfen`.

**Speaker note**

Subagents sind sinnvoll, sobald der Hauptagent die fachliche Richtung und eine prüfbare Teilfrage formulieren kann. Dazu gehören Untersuchungen mit umfangreicher Dateilektüre, deren Zwischenschritte den Hauptkontext nicht belegen sollen. Jeder Subagent beginnt mit einem eigenen Context Window und erhält den erforderlichen Quellenrahmen. Das Ergebnis kommt als kompakter Befund mit Evidenz und offenen Unsicherheiten zurück. Der Hauptagent gleicht widersprüchliche Befunde ab, integriert tragfähige Ergebnisse in den Projektkontext und führt die abschließenden Prüfungen aus. Eine parallele Sitzung bildet dagegen einen unabhängigen Arbeitsstrang. Schreibende Sitzungen benötigen getrennte Worktrees oder disjunkte Dateibereiche.

### 7. Permission Mode begrenzt den Handlungsraum

**Visible copy**

| Modus | Zulässige Arbeit |
| --- | --- |
| Plan | lesen, untersuchen, Plan vorlegen |
| Ask before edits | Änderungen einzeln freigeben |
| Accept edits | Änderungen ausführen und anschließend prüfen |

**Visual**

One mode selector with three didactically selected states. Plan Mode receives the violet emphasis. A narrow boundary separates inspection from modification.

**Speaker note**

Plan Mode ist ein kontrollierter Lesemodus für Exploration und Planung. Die Freigabe eines Plans wechselt in einen Modus, der Änderungen erlaubt. Die Wahl des Modus gehört zur Aufgabenspezifikation, weil sie den Handlungsspielraum des Agenten festlegt.

### 8. Eingriffe verändern den laufenden Agentic Loop

**Visible copy**

> `Esc` unterbricht und erlaubt eine neue Richtung.

> `Esc Esc` öffnet Checkpoints für Code und Conversation.

> Berechtigungen halten sensible Aktionen an.

**Visual**

A horizontal execution trace with one interrupt point, one checkpoint and one permission gate. The diagram carries the message. A terminal screenshot provides secondary evidence.

**Speaker note**

Kontrolle findet während der Ausführung statt. Eine Unterbrechung bewahrt den bisherigen Arbeitsstand und ermöglicht zusätzliche Information. Checkpoints unterstützen reversible Korrekturen. Berechtigungen verlangen eine Entscheidung, bevor der Lauf seine technische Wirkung erweitert.

### 9. Visuelles Feedback wird Teil der Prüfschleife

**Visible copy**

> `Screenshot → Plan → Änderung → Render → Vergleich`

**Visual**

Use one locally produced before-and-after interface example. The screenshot is attached to a bounded request. The resulting render is compared with the original observation and one explicit acceptance criterion.

**Speaker note**

Ein Screenshot liefert eine Beobachtung aus der Umgebung. Der Agent muss daraus eine prüfbare Änderung ableiten, die Seite erneut rendern und das Ergebnis vergleichen. Der visuelle Input ersetzt weder den Plan noch die Abnahme. Er erweitert die verfügbare Evidenz für den nächsten Schritt.

### 10. Die Installation endet mit einer beobachtbaren Prüfung

**Visible copy**

> 1. Offizielle Installationsroute verwenden
> 2. Kontrollierten Arbeitsordner öffnen
> 3. `claude` starten
> 4. Einen lesenden Datei-Check ausführen

> Vollständige Anleitung in Preparation

**Visual**

A four-state setup strip connects installation, project folder, terminal start and read-only evidence. The final state can reuse the planned anonymised `prep-03-harness-scope.webp` capture when it is available.

**Speaker note**

Die Folie definiert das Abschlusskriterium der Einrichtung. Der Teilnehmer weist nach, dass Programmstart, Anmeldung und Ordnerzugriff funktionieren. Betriebssystemspezifische Befehle bleiben auf der gepflegten Preparation-Seite, damit der Foliensatz bei Änderungen der Installation stabil bleibt.

### 11. Fachliche Akzeptanz bleibt ein menschlicher Kontrollpunkt

**Visible copy**

> Tests prüfen formale Bedingungen.

> Quellenprüfung bewertet fachliche Evidenz.

> Verantwortliche Personen entscheiden über Akzeptanz.

**Visual**

The agentic loop terminates at two separate objects. One is a machine-readable assessment result. The other is a human scholarly decision. A green governance line links the decision back to maintained project knowledge.

**Speaker note**

Claude Code kann Tests ausführen, Dateien vergleichen und Prüfberichte erzeugen. Die fachliche Bedeutung eines Befunds und die Akzeptanz eines Forschungsartefakts erfordern verantwortliche Personen. Diese Trennung verbindet die Produktdemonstration mit Verification, Governance und dem Critical Expert.

## Optional reference slides

The following material supports questions and hands-on work. It should stay outside the conceptual sequence.

1. Current installation routes for macOS, Linux, Windows PowerShell and WinGet.
2. Context choice matrix comparing `/compact`, `/clear`, Subagents and parallel sessions; the speaker note adds worktree isolation for concurrent file edits.
3. Platform comparison across terminal, Visual Studio Code, desktop, Claude Code on the web and Remote Control, with local and remote execution labelled explicitly.
4. Model selection after the model-routing concept has been introduced.
5. Shell mode with `!`, `/resume`, file mentions and selected interactive shortcuts.
6. Current data flow, local transcript storage and account-dependent retention.

## Visual production brief

- Replace every montage with one claim and one dominant visual object.
- Produce local screenshots from an anonymised `ai-workspace` or another disposable repository.
- Crop account names, personal paths, model versions, token counters and unrelated terminal history.
- Use a screenshot when the interface state is evidence. Use a diagram for system architecture and conceptual relations.
- Reuse the Full Slide Deck typography and paper ground. Use violet for the Agentic Engineering chapter identity, turquoise for context selection, blue for tool action and green for verification or human control.
- Keep screenshots large enough for the terminal text to remain legible from the back of a room.
- Treat the supplied webinar montages as research references. Their images and layouts are not publication assets for this deck.

## Relation to the Claude Code tutorial

The Preparation page carries the shared setup route. The paired pages `docs/tutorials/claude-code.html` and `docs/tutorials/claude-code.de.html` carry the Claude Code introduction, extension map, coordination patterns and focused deepening routes. The tutorial distinguishes Subagents from parallel sessions and explains Worktrees and Remote Control as optional advanced mechanisms. The subchapter should link to the relevant tutorial anchor instead of reproducing platform-specific commands. The same first-run criterion applies across these surfaces. Claude Code starts in a disposable folder and completes one read-only inspection before any modification is authorised.

The planned harness-scope screenshot can support both surfaces. The slide uses a tight crop that demonstrates the concept. The tutorial keeps the wider state and the step-by-step check.

## Official references checked on 2026-08-25

- Claude Code overview and installation, https://code.claude.com/docs and https://code.claude.com/docs/en/installation
- Project instructions and auto memory, https://code.claude.com/docs/en/memory
- Context window and compaction, https://code.claude.com/docs/en/context-window and https://code.claude.com/docs/en/how-claude-code-works
- Permission modes and Plan Mode, https://code.claude.com/docs/en/permission-modes
- Interactive controls and checkpoints, https://code.claude.com/docs/en/interactive-mode
- Image and screenshot workflows, https://code.claude.com/docs/en/common-workflows
- Extension mechanisms, https://code.claude.com/docs/en/features-overview
- Model Context Protocol, https://code.claude.com/docs/en/mcp
- Plugins, https://code.claude.com/docs/en/plugins and https://code.claude.com/docs/en/discover-plugins
- Subagents and parallel agent patterns, https://code.claude.com/docs/en/sub-agents and https://code.claude.com/docs/en/agents
- Sessions and isolated worktrees, https://code.claude.com/docs/en/sessions and https://code.claude.com/docs/en/worktrees
- Remote Control and Claude Code on the web, https://code.claude.com/docs/en/remote-control and https://code.claude.com/docs/en/claude-code-on-the-web
- Platforms and execution surfaces, https://code.claude.com/docs/en/platforms
- Data flow, retention and local transcripts, https://code.claude.com/docs/en/data-usage and https://code.claude.com/docs/en/claude-directory

## Editorial acceptance required

The operator decides whether the eleven-slide sequence enters the Full Slide Deck, whether slide 10 remains inside the conceptual chapter or moves to the practical appendix, and which locally produced screenshots become publication assets. After acceptance, the native slide deck should be edited first. The text export and the corresponding Full Lecture Notes sections should then be refreshed from that accepted state.
