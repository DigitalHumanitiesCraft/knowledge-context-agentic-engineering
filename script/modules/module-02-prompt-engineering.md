---
title: Prompt Engineering
module: 2
source-language: [de, en]
status: draft
created: 2026-08-20
units: [M7, M11, M14, M16]
canonical: false
canonical-gate: operator confirmation of the module cut
source-masters: [script/master-script-de.md, script/master-script-en.md]
---

# Module 2 — Prompt Engineering

> Draft cut of the master corpus. Every passage below is reproduced verbatim from a master
> script; only the module heading, the unit headings and the provenance lines are added.
> The masters stay authoritative until the operator confirms the cut. Coverage, discarded
> parallel versions and open questions are recorded in `script/COVERAGE.md`.


## Unit M7 — Prompt Engineering

*Source: `master-script-de.md`, sections 3.1 through 3.5.*

## 3.1 Prompt und Prompt Engineering

Ein Prompt ist mehr als eine Frage. Er ist die für einen Modellaufruf bereitgestellte Eingabesequenz. Sie kann eine Aufgabe, Ausgangsmaterialien, Kontextinformationen, Anforderungen, Einschränkungen, Beispiele, Verfahrenshinweise und Vorgaben für die erwartete Ausgabe enthalten.

**Prompt Engineering** bezeichnet die iterative Entwicklung einzelner Prompts durch Veränderungen ihres Inhalts, ihrer Struktur oder der auf sie angewandten Prompting-Techniken

Folie mit konkurrierenden öffentlichen Vorstellungen von Prompt Engineering

**Abbildung 4: Konkurrierende Deutungen des Prompt Engineering.**  
*Die Folie kontrastiert Prompting als vermeintliche Beschwörungskunst, als vermarktetes Versprechen perfekter Formeln und als Verstärkung vorhandener Expertise. Die Gegenüberstellung motiviert eine engere Arbeitsdefinition: Prompt Engineering gestaltet eine konkrete Eingabesequenz, ohne fehlendes Fachwissen oder Projektkontext ersetzen zu können.* (Schulhoff et al. 2024). Der Begriff ist bewusst enger als Context Engineering. Er richtet sich auf eine konkrete Eingabesequenz, nicht auf die gesamte Informationsumgebung einer längeren Arbeitstrajektorie.

Ein einfacher Prompt kann lauten:

> Transkribiere diese Seite.

Eine begrenztere und prüfbarere Fassung wäre:

> Transkribiere die bereitgestellte Seite diplomatisch. Erhalte Zeilenumbrüche, markiere unleserliche Stellen als `[unleserlich]`, normalisiere keine Schreibweisen und ergänze keine Wörter, die nicht sichtbar sind. Gib zuerst die Transkription und anschließend eine Liste unsicherer Lesungen mit Zeilenreferenz aus.

Die zweite Fassung macht sichtbar, welche Eigenschaften des Ergebnisses erwartet werden. Sie garantiert noch keine korrekte Transkription, reduziert aber die Zahl stiller Annahmen.

## 3.2 Der Prompt als begrenzte Spezifikation

Ein guter Prompt ist weniger eine rhetorische Formel als eine **begrenzte Spezifikation**. Er beschreibt eine aktuelle Aufgabe innerhalb eines bereits vorhandenen Wissens- und Arbeitskontextes.

Typische Bestandteile sind:

- **Ziel:** Was soll erzeugt oder verändert werden?  
- **Ausgangslage:** Welche Dateien, Daten oder bisherigen Ergebnisse sind relevant?  
- **Anforderungen:** Welche Eigenschaften muss das Ergebnis besitzen?  
- **Einschränkungen:** Was darf nicht verändert oder angenommen werden?  
- **Vorgehen:** Welche Schritte oder Prüfungen sind erforderlich?  
- **Ausgabeform:** In welchem Format soll das Ergebnis vorliegen?  
- **Abschlusskriterium:** Woran ist erkennbar, dass die Aufgabe hinreichend bearbeitet wurde?

Nicht jede Aufgabe benötigt alle Bestandteile in gleicher Ausführlichkeit. Eine einfache Formatumwandlung kann durch einen kurzen Prompt eindeutig beschrieben werden. Eine editorisch folgenreiche Transformation benötigt dagegen eine genauere Spezifikation.

Die Präzision eines Prompts hängt nicht von seiner Länge ab. Ein sehr langer Prompt kann widersprüchlich oder schwer priorisierbar sein. Ein kurzer Prompt kann ausreichen, wenn die relevanten Regeln bereits in Wissensdokumenten und Instruktionsdateien vorliegen.

### Beispiel: TEI-Erzeugung

Erzeuge für \`page-001.txt\` eine TEI-Datei.

Verwende:

\- \`knowledge/transcription-rules.md\`

\- \`knowledge/tei-model.md\`

\- \`knowledge/uncertainty.md\`

Anforderungen:

\- Erhalte Seiten- und Zeilenwechsel.

\- Verändere den Transkriptionstext nicht stillschweigend.

\- Markiere unsichere Lesungen nach den dokumentierten Regeln.

\- Verwende nur Elemente und Attribute, die im Projektmodell vorgesehen sind.

\- Validere die Datei gegen \`schema/edition.rng\`.

Abschluss:

\- Speichere die Datei unter \`tei/page-001.xml\`.

\- Führe die Validierung aus.

\- Berichte über verbleibende fachliche Unsicherheiten getrennt von technischen Fehlern.

Der Prompt enthält keine vollständige Erklärung der editorischen Regeln. Er verweist auf den persistenten Wissensbestand. Dadurch bleibt er kompakt und auf die aktuelle Aufgabe begrenzt.

## 3.3 Rollen- und Persona-Prompting

Eine verbreitete Form des Promptings weist dem Modell eine Rolle zu:

> Du bist eine erfahrene Editionswissenschaftlerin.

Eine solche Formulierung kann Terminologie, Stil, Perspektive und Detaillierungsgrad beeinflussen. Sie fügt dem Modell jedoch kein neues Fachwissen hinzu. Die Rolle kann höchstens gelernte Muster fachsprachlicher Kommunikation wahrscheinlicher machen.

**Role Prompting** bezeichnet eine knappe funktionale Zuweisung. **Persona Prompting** beschreibt eine ausgearbeitete Perspektive mit Hintergrund, Erfahrung, Zielen, Einschränkungen und Nutzungssituation. Beide sollten gemeinsam betrachtet, aber nicht gleichgesetzt werden.

Beispiel einer Persona:

Du repräsentierst eine Teilnehmerin des Workshops.

Hintergrund:

\- Literaturwissenschaftlerin

\- Erfahrung mit digitalen Editionen

\- regelmäßige Arbeit mit Word und Excel

\- keine Erfahrung mit Terminal, Git oder VS Code

\- grundsätzlich interessiert, aber vorsichtig bei Installationen

\- arbeitet mit Windows

Prüfe die folgende Anleitung aus dieser Perspektive.

Identifiziere:

1\. unklare Begriffe,

2\. fehlende Zwischenschritte,

3\. stillschweigend vorausgesetztes Wissen,

4\. Stellen, an denen du wahrscheinlich Unterstützung benötigst.

Eine synthetische Persona kann mögliche Probleme sichtbar machen. Sie erzeugt jedoch keine empirischen Nutzerdaten. Ihre Antworten sind Hypothesen, die mit realen Personen, Beobachtungen oder vorhandener Nutzerforschung geprüft werden müssen.

Rollen- und Persona-Prompting eignen sich besonders für:

- Stilvariation,  
- Perspektivwechsel,  
- frühe Interface- und Materialkritik,  
- Vorbereitung von Interviews,  
- Identifikation möglicher Rückfragen.

Sie ersetzen nicht:

- Fachwissen,  
- reale Stakeholder,  
- empirische Nutzerforschung,  
- fachliche Validierung.

## 3.4 Iteration, Self-Revision und strukturierte Ausgaben

Prompts entstehen häufig nicht in einem Schritt. Eine produktive Interaktion kann aus mehreren begrenzten Durchgängen bestehen:

> erzeugen → prüfen → korrigieren → verdichten

Ein erster Prompt kann einen Entwurf erzeugen. Ein zweiter fordert eine kriteriengeleitete Prüfung. Ein dritter überarbeitet nur die tatsächlich identifizierten Probleme.

Beispiel:

Prüfe die TEI-Datei auf:

1\. Abweichungen von \`transcription-rules.md\`,

2\. unzulässige oder nicht definierte Elemente,

3\. stillschweigende Normalisierungen,

4\. unmarkierte Unsicherheiten.

Liste zuerst die Befunde mit Zeilenreferenz.

Verändere die Datei noch nicht.

Danach:

Überarbeite ausschließlich die bestätigten Befunde.

Bewahre alle nicht betroffenen Strukturen.

Führe anschließend die Schema-Validierung erneut aus.

Diese Form der **Self-Revision** kann Fehler sichtbar machen, ist aber keine unabhängige Verifikation. Dasselbe Modell kann seine eigenen Fehlannahmen übersehen oder nachträglich plausibel begründen. Self-Revision wird verlässlicher, wenn explizite Kriterien, externe Tests und überprüfbare Referenzen vorliegen.

Strukturierte Ausgabeformate reduzieren Mehrdeutigkeit. Ein Prompt kann eine Markdown-Tabelle, JSON, XML oder eine definierte Dateistruktur verlangen. Dabei sind unterschiedliche Ebenen zu unterscheiden:

- syntaktische Konformität,  
- strukturelle Vollständigkeit,  
- semantische Richtigkeit,  
- wissenschaftliche Angemessenheit.

Gültiges JSON beweist nur, dass die Syntax stimmt. Schema-valide TEI beweist nur, dass die formalen Regeln eingehalten wurden. Ob die Quelle angemessen repräsentiert ist, bleibt eine fachliche Frage.

## 3.5 Warum Promptwirkungen schwer zu evaluieren sind

Prompting kann überraschend empfindlich auf Formulierungen reagieren.

Folie mit empirischen Beispielen ungewöhnlicher Promptwirkungen

**Abbildung 5: Modell-, aufgaben- und sprachabhängige Promptwirkungen.**  
*Die Beispiele zeigen, dass emotionale Zusätze, Höflichkeit, Formalität und kleine sprachliche Veränderungen messbare, aber heterogene Effekte erzeugen können. Die Folie dient nicht als Sammlung empfohlener Tricks, sondern als Evidenz dafür, dass beobachtete Promptwirkungen lokal und schwer zu verallgemeinern sind.* Frühere Studien berichteten Effekte emotionaler Zusätze, von Höflichkeit oder ungewöhnlichen automatisch erzeugten Prompts. Andere Untersuchungen zeigen, dass irrelevante Zusätze die Leistung verschlechtern oder dass Effekte auf neueren Modellen nicht stabil repliziert werden (Li et al. 2023; Yin et al. 2024; Battle und Gollapudi 2024; Rajeev et al. 2025).

Daraus folgt nicht, dass Prompt Engineering wirkungslos ist. Es folgt vielmehr, dass Promptwirkungen häufig lokal sind. Sie hängen ab von:

- Modell und Modellversion,  
- Aufgabe und Datensatz,  
- Sprache,  
- Position und Struktur der Information,  
- Evaluationsmetrik,  
- Zufallsvariation.

Eine veränderte Leistung nach einer Promptvariation beweist außerdem nicht, dass die Formulierung aus dem vermuteten Grund wirkt. Ein Star-Trek-Präfix kann in einem Benchmark die Leistung verbessern. Daraus folgt nicht automatisch, dass „analytische Präzision“ mechanistisch als Star-Trek-Konzept aktiviert wurde. Solche Erklärungen sind Hypothesen, solange keine direkte mechanistische Evidenz vorliegt.

Promptvarianten sollten deshalb wie experimentelle Interventionen behandelt werden:

Folie zur schwierigen Evaluation von Prompt Engineering

**Abbildung 6: Warum Prompt Engineering schwer zu evaluieren ist.**  
*Die Abbildung verbindet drei Probleme: irrelevante Zusätze können Reasoning stören, ungewöhnliche automatisch erzeugte Prompts können unerwartet gut abschneiden, und Rollenformulierungen verbessern nicht zuverlässig Faktentreue oder Schlussfolgerungsleistung. Einzelne erfolgreiche Prompts sind daher keine hinreichende Grundlage für allgemeine Best Practices.*

1. Ziel und Metrik festlegen.  
2. Eine Baseline definieren.  
3. Möglichst nur einen relevanten Bestandteil verändern.  
4. Mehrere Beispiele und Wiederholungen verwenden.  
5. Auf neuen Fällen prüfen.  
6. Modell und Version dokumentieren.  
7. Fachliche Qualität getrennt von Stil und Format bewerten.

*Source: `master-script-de.md`, sections 3.7 and 3.8.*

## 3.7 Grenzen des Prompt Engineering

Prompt Engineering kann eine aktuelle Aufgabe präzisieren. Es kann jedoch grundlegende Probleme der Wissens- und Arbeitsorganisation nicht allein lösen.

Ein guter Prompt ersetzt nicht:

- fehlendes oder unzugängliches Projektwissen;  
- widersprüchliche Richtlinien;  
- ungeklärte Anforderungen;  
- einen überladenen oder irrelevanten Kontext;  
- persistente Dokumentation;  
- Werkzeug- und Berechtigungsmanagement;  
- technische Tests;  
- fachliche Validierung;  
- die Organisation längerer Arbeitstrajektorien.

Je länger und ressourcenreicher eine Aufgabe wird, desto weniger lässt sie sich als Optimierung einer einzelnen Eingabesequenz beschreiben. Dann verschiebt sich der Gegenstand von der Formulierung des Prompts zur Organisation des Informationszustands, in dem der Agent arbeitet.

## 3.8 Hands-on: Eine Editionsaufgabe als begrenzte Spezifikation

### Ziel

Aus einer vagen Aufgabe wird ein begrenzter und prüfbarer Prompt.

### Ausgangsformulierung

> Erstelle eine digitale Edition dieser Seite.

### Arbeitsauftrag

Präzisieren Sie:

- Zielartefakt,  
- Ausgangsdateien,  
- editorische Regeln,  
- unveränderliche Ressourcen,  
- erwartete Ausgabe,  
- technische Prüfungen,  
- offene fachliche Entscheidungen.

### Musterlösung

Untersuche \`sources/page-001.jpg\` und \`transcription/page-001.txt\`.

Erzeuge einen ersten TEI-Entwurf unter \`tei/page-001.xml\`.

Verwende:

\- \`knowledge/transcription-rules.md\`

\- \`knowledge/tei-model.md\`

\- \`knowledge/uncertainty.md\`

Regeln:

\- Verändere die Quelldateien nicht.

\- Erhalte Seiten- und Zeilengrenzen.

\- Normalisiere keine Schreibweise, sofern dies nicht ausdrücklich vorgesehen ist.

\- Markiere unsichere Lesungen und unleserliche Stellen.

\- Erfinde keine fehlenden Inhalte.

Prüfung:

\- Validiere gegen \`schema/edition.rng\`.

\- Trenne technische Fehler von fachlichen Unsicherheiten.

\- Benenne Annahmen, die nicht aus den Quellen oder Wissensdokumenten hervorgehen.

### Reflexion

- Welche Informationen gehören in den Prompt?  
- Welche Informationen sollten persistent in Wissensdokumenten stehen?  
- Welche Entscheidungen kann der Agent ausführen, aber nicht autorisieren?

*Source: `master-script-en.md`, "Prompting Strategies: There Is No Prompt to Rule Them All".*

## **Prompting Strategies: There Is No Prompt to Rule Them All**

No single prompting strategy performs optimally across all models, tasks and evaluation settings. Effective prompting is better understood as a combination of several practices rather than the discovery of one universal prompt.[^8]

* **Organize the Context**: provide relevant information at the right time and in a usable form.
* **Structure the Prompt**: separate task, source context, rules and output contract.
* **Iterate and Evaluate**: compare variants on fixed examples and explicit criteria.
* **Use Reasoning Selectively**: match inference time reasoning to the complexity and evaluability of the task.[^36]
* **Counter Sycophancy**: require evidence, alternatives or independent critical review where agreement with the user could bias the result.
* **Generate, Compare and Reconcile**: produce independent candidates, inspect their differences and adjudicate the result.

Effective prompting therefore combines **context selection, instruction design, inference strategy and evaluation**. This already moves beyond the prompt itself and leads directly to Knowledge and Context Engineering.


## Unit M11 — Working Environment, API Access and Structured Output

*Source: `master-script-en.md`, "Prepare the Working Environment before the First Prompt".*

## **Prepare the Working Environment before the First Prompt**

Agentic work begins before the first substantive prompt. The first decision is therefore not necessarily how to phrase an instruction, but **where the model is going to work**. An AI harness such as Claude Code, Codex, Gemini CLI or Cursor can provide controlled access to files, a terminal and project specific tools.[^12]

A project workspace should contain relevant source material, project documentation, expected outputs and the context needed to understand the task. Access should remain limited to the intended working boundary. Original sources should remain unchanged, while generated artefacts should be stored separately and connected to sufficient provenance.

Preparing the workspace determines which files, tools, knowledge and forms of feedback later become available to the model or agent. The environment is therefore part of the methodological design rather than neutral technical plumbing.

*Source: `master-script-en.md`, ".txt to JSON to CSV".*

## **.txt → JSON → CSV**

Generative models can be combined with deterministic processing rather than replacing it. The Islington public health example starts with extracted text and tables, transforms relevant information into structured JSON and CSV, and then applies deterministic consistency checks.

This distinction is methodologically important. Recognising a table, interpreting its layout or extracting values from noisy source material may require probabilistic model behaviour. Once values have been represented explicitly, arithmetic relations can be recomputed deterministically.

A recurring workflow pattern is therefore:

`probabilistic interpretation → structured representation → deterministic checking`

Row totals, column totals and other invariants can provide strong feedback. Such checks do not prove that the original source was interpreted correctly, but they can expose internal inconsistencies and focus subsequent human inspection.


## Unit M14 — From Facsimile to a Research Data Package

*Source: `master-script-en.md`, "Multimodality & Vision Language Models".*

## **Multimodality & Vision Language Models**

A **Vision Language Model (VLM)** processes visual and linguistic information within the same task. A general purpose multimodal foundation model can therefore receive a facsimile together with an instruction and generate a transcription without being a dedicated OCR or HTR system.[^30]

```text
FACSIMILE                      INSTRUCTION
visual information             task and rules
          \                       /
           \                     /
            VISION LANGUAGE MODEL
                      |
                      v
               TRANSCRIPTION
```

The distinction matters because a VLM does not merely recognise isolated characters. Visual patterns, layout, linguistic context and task instructions can jointly influence the generated output. This flexibility can help with heterogeneous documents, but it creates a characteristic failure mode. Errors may be **contextually plausible rather than locally obvious**.

The ability to transcribe previously unseen handwriting is therefore interesting as a possible emergent capability of large multimodal models. Whether it should technically be classified as emergent depends on the definition of emergence, model scale and the unknown composition of proprietary training data.


## Unit M16 — Case Study Zweig: Transcribing a Complex Facsimile

*Source: `master-script-en.md`, "Transcribe a Facsimile with Gemini 3.7 Flash" and the two hands-on sections.*

## **Transcribe a Facsimile with Gemini 3.7 Flash**

A Stefan Zweig order slip provides a compact example of a prompt treated as a **bounded specification**. The instruction separates the immediate task, source context, transcription rules and expected output.[^29]

```text
Create a diplomatic transcription of this facsimile

# Context

German order slip from May 1935
Printed form with pencil entries by Stefan Zweig

# Rules

* Transcribe printed and handwritten text
* Preserve spelling, abbreviations, line breaks and field order
* Mark uncertainty as word[?] and illegible text as [...]
* Mark deletions as ~~text~~ and insertions as {text}
* Ignore show through

# Output

Return only the transcription as plain text in reading order
```

The categories can be changed independently. A different source changes the context. A different editorial policy changes the rules. A different downstream workflow may require JSON, XML or TEI rather than plain text. This is not a universal prompt template. It is a transparent way of separating parts of the specification so that they can be inspected and revised.

## **Hands on 1: Transcribe a Facsimile with Gemini 3.7 Flash**

The exercise applies the same structure to a more difficult page from Stefan Zweig’s *Radiovortrag über Newyork*. Participants receive a reusable prompt skeleton and add task relevant source context and at least one rule based on the characteristics of the material.

The exercise has two purposes. First, participants must decide which information is actually useful for the transcription. Second, they must formulate a rule that addresses a plausible failure mode rather than simply increasing prompt length.

A useful additional rule is:

```text
Do not reconstruct or complete words from linguistic context when the reading
is not visually supported by the facsimile. Mark uncertainty instead.
```

The instruction asks the model to preserve explicit uncertainty rather than resolve difficult readings through linguistic plausibility. Whether the rule works has to be assessed against the facsimile.

## **Hands on 1: Transcribe a Facsimile with Gemini 3.7 Flash (Example Result)**

The example prompt adds catalogue and material information about the manuscript, including title, date, language, hand, pagination, collection and shelfmark. It also makes the transcription policy more explicit.

The generated transcription can appear remarkably fluent while individual readings remain wrong. Fluency, grammaticality and internal coherence are therefore not evidence of source fidelity. A model may produce a word that fits the sentence even where the visual evidence supports another reading, or it may fail to express uncertainty where a human editor would hesitate.

The output should consequently be treated as a **candidate representation** that requires comparison with the source. This principle generalises beyond transcription. Model outputs can be valuable because they provide plausible structured candidates, but plausibility is not equivalent to validation.


## Notes

*Footnote identifiers and definitions are reproduced unchanged from their master.*

### Notes carried from the English master

[^8]: Sander Schulhoff et al., “The Prompt Report: A Systematic Survey of Prompting Techniques,” 2024, https://doi.org/10.48550/arXiv.2406.06608.

[^12]: Hailin Zhong and Shengxin Zhu, “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents,” 2026, https://doi.org/10.48550/arXiv.2605.13357.

[^29]: Google Gemini, “Prompt Design Strategies,” https://ai.google.dev/gemini-api/docs/prompting-strategies.

[^30]: Gemini Team, “Gemini: A Family of Highly Capable Multimodal Models,” 2023, https://arxiv.org/abs/2312.11805.

[^36]: For inference time scaling as a broader category see Charlie Snell et al., “Scaling LLM Test Time Compute Optimally Can Be More Effective Than Scaling Model Parameters,” 2024, https://arxiv.org/abs/2408.03314.
