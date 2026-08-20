---
title: Knowledge and Context Engineering
module: 3
source-language: [de, en]
status: draft
created: 2026-08-20
units: [M8, M9]
canonical: false
canonical-gate: operator confirmation of the module cut
source-lecture-notes: [script/full-lecture-notes-de.md, script/full-lecture-notes-en.md]
---

# Module 3 — Knowledge and Context Engineering

> Draft cut of the full corpus. Every passage below is reproduced verbatim from the Full
> Lecture Notes; only the module heading, the unit headings and the provenance lines are added.
> The Full Lecture Notes stay authoritative until the operator confirms the cut. Coverage, discarded
> parallel versions and open questions are recorded in `script/COVERAGE.md`.


## Unit M8 — Context Engineering

*Source: `full-lecture-notes-de.md`, sections 4.1 through 4.6.*

## 4.1 Vom Prompt zum Informationszustand einer Aufgabe

Ein Agent soll für eine Seite einer digitalen Edition einen TEI-Entwurf erzeugen. Im Projektordner liegen jedoch weit mehr Informationen, als er für diesen Arbeitsschritt unmittelbar benötigt: mehrere hundert Seitenbilder, allgemeine Editionsrichtlinien, verschiedene Versionen des Schemas, Protokolle, Testberichte, frühere Fehlversuche und bereits erzeugte TEI-Dateien.

Der vollständige Projektbestand ist für das Projekt relevant, aber nicht alles daraus muss gleichzeitig im Modellkontext liegen. Für die konkrete Seite benötigt der Agent vor allem:

- das Seitenbild,  
- die Transkription,  
- die geltenden Transkriptionsregeln,  
- den einschlägigen Teil des TEI-Modells,  
- einige geprüfte Beispiele,  
- die aktuelle Aufgabe und ihre Prüfkriterien.

Weitere Ressourcen können im Projektbestand verbleiben und bei Bedarf über Werkzeuge gelesen oder abgefragt werden.

**Context Engineering** bezeichnet die systematische Auswahl, Organisation, Pflege und Bereitstellung dieses aufgabenspezifischen Informationszustands (Mei et al. 2025). Es bestimmt nicht nur, welche Informationen ein Modell erhält, sondern auch, in welcher Form und Reihenfolge sie vorliegen, wann weitere Informationen nachgeladen werden und was bewusst außerhalb des aktuellen Kontextes bleibt.

## 4.2 Context Window und Context Rot

Ein Modell kann nicht gleichzeitig auf alle Dateien, Notizen und Daten eines Projekts zugreifen. Es verarbeitet nur jene Informationen, die innerhalb eines aktuellen Laufs tatsächlich bereitgestellt werden. Dazu gehören je nach System:

- System- und Projektinstruktionen,  
- die aktuelle Nutzereingabe,  
- der bisherige Gesprächs- oder Arbeitsverlauf,  
- bereitgestellte Dokumentauszüge,  
- Werkzeugbeschreibungen,  
- Tool-Ausgaben,  
- Zwischenergebnisse,  
- die erzeugte Antwort.

Dieser technisch begrenzte Verarbeitungsraum wird als **Context Window** bezeichnet. Seine nominelle Größe gibt an, wie viele Tokens ein System grundsätzlich verarbeiten kann. Sie sagt jedoch nicht, dass alle enthaltenen Informationen gleich zuverlässig genutzt werden.

Untersuchungen zu langen Kontexten zeigen, dass Position, Ablenkung und Umfang der bereitgestellten Information die Leistung beeinflussen können. Relevante Information kann in langen Eingaben schwerer auffindbar sein, insbesondere wenn sie zwischen ähnlichen oder widersprüchlichen Inhalten steht.[^4]

Der Ausdruck **Context Rot** bezeichnet beobachtete Leistungsabfälle bei wachsender Kontextlänge. Er ist kein einzelner, abschließend geklärter technischer Mechanismus. Für agentische Arbeit ist der Begriff dennoch hilfreich: Während längerer Läufe sammeln sich Werkzeugausgaben, Fehlversuche, überholte Planungen und Zwischenstände an. Sie beanspruchen Tokens und können mit aktuell relevanter Information konkurrieren.

Daraus folgt nicht, dass Kontext immer möglichst kurz sein sollte. Zu starke Reduktion kann Bedingungen, Unsicherheiten und Provenienz entfernen. Die Zielgröße ist ein **dichter und hinreichender Kontext**: so begrenzt wie möglich, aber so vollständig und differenziert wie für die Aufgabe erforderlich.

## 4.3 Wie Informationen in den Modellkontext gelangen

Eine Datei im Projektordner ist nicht automatisch Teil des Context Window. Damit ihr Inhalt für das Modell verfügbar wird, muss das System sie lesen, extrahieren, transformieren oder durch ein Werkzeug untersuchen.

Der Weg lässt sich schematisch darstellen:

> **Datei oder Datenbestand → Werkzeug, Parser oder Skript → bereitgestellte Repräsentation → Tokenisierung → Context Window**

Unterschiedliche Formate erfordern unterschiedliche Zugriffe:

- Markdown und Quellcode können meist direkt gelesen werden.  
- CSV-Dateien können selektiv profiliert oder abgefragt werden.  
- Word-Dateien müssen strukturiert ausgelesen werden.  
- PDFs können Text, Layout und Bilder kombinieren.  
- Bilder werden multimodal verarbeitet oder in strukturierte Beschreibungen überführt.  
- Datenbanken werden über Abfragen genutzt, ohne vollständig in den Kontext geladen zu werden.

Im Editionsprojekt kann der Agent ein Bild öffnen, ohne dessen Binärdaten als Tokens zu „lesen“. Ein multimodales System verarbeitet das Bild und erzeugt interne Repräsentationen. Ein Skript kann aus hundert TEI-Dateien nur jene Elemente zählen, die für eine aktuelle Modellierungsfrage relevant sind. In den Modellkontext gelangt dann die Ausgabe des Skripts, nicht zwingend der gesamte Datenbestand.

Die methodisch relevante Einheit ist daher nicht die Datei als solche, sondern ihre **für das Modell bereitgestellte Repräsentation**.

## 4.4 Context Compression und Distillation

Umfangreiche Informationsbestände enthalten häufig mehr Material, als für eine einzelne Aufgabe benötigt wird. Sie können Wiederholungen, alte Fassungen, implizite Voraussetzungen und widersprüchliche Aussagen enthalten.

**Context Compression** reduziert die Menge des unmittelbar bereitgestellten Kontextes. Dazu gehören:

- Auswahl relevanter Abschnitte,  
- Zusammenfassung,  
- Entfernung von Wiederholungen,  
- Aggregation von Daten,  
- Auswahl repräsentativer Beispiele,  
- Kompaktierung eines bisherigen Arbeitsverlaufs.

Eine kürzere Fassung ist jedoch nicht automatisch besser. Eine Zusammenfassung kann Unsicherheit glätten, Begründungen entfernen oder mehrere alternative Aussagen in eine scheinbar eindeutige Regel verwandeln.

**Distillation** geht deshalb über bloße Kompression hinaus. Sie überführt verfügbares Verständnis in eine selektive, strukturierte, inspizierbare und revidierbare Repräsentation. Für die digitale Edition kann eine Destillation beispielsweise festhalten:

- welche Arten von Unsicherheit unterschieden werden;  
- wie sie in TEI repräsentiert werden;  
- welche Begründung hinter der Regel steht;  
- welche Ausnahmen bekannt sind;  
- wie Unsicherheit im Frontend sichtbar werden soll;  
- welche Fragen noch offen sind.

Distillation umfasst drei Operationen:

1. **Auswahl:** Was ist für den Gegenstand relevant?  
2. **Strukturierung:** Welche Begriffe, Regeln und Beziehungen müssen explizit werden?  
3. **Verdichtung:** Welche Redundanz kann entfernt werden, ohne notwendige Differenzierungen zu verlieren?

Das Gegenrisiko ist **Überdestillation**. Sie liegt vor, wenn Provenienz, Unsicherheiten oder handlungsnotwendige Details verloren gehen.

## 4.5 Project Knowledge Base, Working Context und Context Window

Zwischen drei Ebenen ist zu unterscheiden:

**Abbildung 9: Project Knowledge Base, Working Context und Context Window.**  
*Die Project Knowledge Base enthält den persistenten Projektbestand. Der Working Context ist eine aufgabenspezifische Auswahl aus Wissensdokumenten, Daten, Instruktionen, Werkzeugbeschreibungen und aktuellen Rückmeldungen. Nur die tatsächlich bereitgestellte Repräsentation gelangt in das technisch begrenzte Context Window.*

- Die **Project Knowledge Base** bewahrt den persistenten, inspizierbaren und revidierbaren Wissensbestand.  
- Der **Working Context** ist der für eine konkrete Aufgabe zusammengestellte Informationszustand.  
- Das **Context Window** ist der technische Verarbeitungsraum, in dem dieser Kontext vom Modell genutzt wird.

Für die Aufgabe „TEI für Seite 17 erzeugen“ könnte der Working Context enthalten:

Aktuelle Aufgabe

├── page-017.jpg

├── page-017.txt

├── transcription-rules.md

├── uncertainty.md

├── relevanter Abschnitt aus tei-model.md

├── zwei geprüfte Beispiele

├── Schema- und Validierungsbefehl

└── aktuelles Feedback des Validators

Nicht enthalten sein müssen:

- allgemeine Projektberichte,  
- Richtlinien zu anderen Quellentypen,  
- vollständige Protokolle,  
- alte Schema-Versionen,  
- nicht mehr relevante Fehlversuche.

Die zentrale Unterscheidung lautet:

> Knowledge Engineering baut und pflegt den Wissensbestand; Context Engineering stellt daraus und aus weiteren Ressourcen den für eine konkrete Aufgabe erforderlichen Kontext zusammen.

## 4.6 Hands-on: Einen Working Context für eine TEI-Aufgabe zusammenstellen

### Aufgabe

Wählen Sie aus einem bereitgestellten Projektbestand jene Ressourcen aus, die ein Agent benötigt, um eine Seite korrekt als TEI zu modellieren.

### Kategorien

Ordnen Sie jede Ressource einer Kategorie zu:

1. unmittelbar laden,  
2. bei Bedarf nachladen,  
3. nur über ein Werkzeug abfragen,  
4. für diese Aufgabe nicht verwenden.

### Beispielmatrix

| Ressource | Unmittelbar | Bei Bedarf | Tool-Zugriff | Nicht verwenden | Begründung |
| :---- | ----: | ----: | ----: | ----: | :---- |
| `page-017.jpg` | ✓ |  |  |  | Primärquelle |
| `transcription-rules.md` | ✓ |  |  |  | verbindliche Regeln |
| vollständiges Projektprotokoll |  |  |  | ✓ | zu breit und teilweise überholt |
| `edition.rng` |  |  | ✓ |  | durch Validator verwenden |
| zwei geprüfte TEI-Beispiele | ✓ |  |  |  | konkretisieren Grenzfälle |
| alte Schema-Version |  |  |  | ✓ | nicht maßgeblich |

### Reflexion

- Welche Ressource ist wichtig, muss aber nicht vollständig in den Kontext?  
- Welche Information fehlt im Bestand?  
- Welche Auswahlentscheidung ist fachlich und nicht nur technisch?


## Unit M9 — Knowledge Engineering and Knowledge Documents

*Source: `full-lecture-notes-en.md`, "Knowledge & Context Engineering", the three-way distinction between the two layers and the prompt.*

## **Knowledge & Context Engineering**

Complex knowledge work contains more relevant information than should be placed into a single prompt. Project goals, documents, data, policies, requirements, examples, design decisions, previous findings, unresolved questions and validation criteria may all matter, but they do not all matter at the same time.

**Knowledge Engineering** organises the persistent informational basis. It makes relevant knowledge explicit, inspectable and revisable so that people and AI systems can work from a maintained state rather than from undocumented assumptions.[^9] **Context Engineering** constructs the task specific information state from that broader environment.[^10]

The distinction can be expressed through three questions:

`Knowledge Engineering → What does the project or organisation know?`

`Context Engineering → What does the model or agent need now?`

`Prompt Engineering → What should the model or agent do now?`

Knowledge work therefore becomes an engineering problem of maintaining available knowledge and providing the right subset of that knowledge for a particular action.

*Source: `full-lecture-notes-de.md`, sections 5.1 through 5.8.*

## 5.1 Warum Projektwissen explizit werden muss

In einem Editionsprojekt ist Wissen häufig verteilt. Ein Teil steht in Richtlinien, ein Teil in E-Mails, ein Teil in TEI-Beispielen und ein Teil nur im Erfahrungswissen einzelner Editor:innen. Menschen, die lange am Projekt arbeiten, ergänzen fehlende Zusammenhänge oft unbewusst. Eine neue Person oder eine neue Agenteninstanz besitzt diesen Hintergrund nicht.

Ein Agent kann zwar alle Dateien durchsuchen, aber daraus entsteht nicht automatisch ein konsistentes Projektverständnis. Er kann eine alte Regel mit einer neuen vermischen oder aus einem einzelnen Beispiel eine allgemeine Konvention ableiten.

**Knowledge Engineering** betrifft den Aufbau und die Pflege expliziten, inspizierbaren und revidierbaren Projektwissens. Es macht relevante Begriffe, Regeln, Entscheidungen, Einschränkungen und Unsicherheiten so sichtbar, dass sie gelesen, kritisiert und fortgeschrieben werden können.

Ziel ist keine vollständige Repräsentation aller verfügbaren Informationen. Eine Wissensbasis ist zweckgebunden. Sie hält jenen Teil des Wissens fest, der für bestimmte Formen der Arbeit, Entscheidung und Prüfung erforderlich ist.

## 5.2 Knowledge Acquisition

Projektwissen stammt aus zwei grundlegenden Quellen:

1. bereits vorhandenen Dokumenten und Daten;  
2. implizitem Wissen von Personen und Organisationen.

Vorhandene Materialien können sein:

- Forschungsdaten,  
- Publikationen,  
- editorische Richtlinien,  
- Datenmodelle,  
- Quellcode,  
- Protokolle,  
- frühere Artefakte.

Implizites Wissen umfasst beispielsweise:

- Gründe für frühere Entscheidungen,  
- bekannte Ausnahmen,  
- Erwartungen an das Zielartefakt,  
- Kriterien für Akzeptanz,  
- praktische Erfahrungen mit bestimmten Quellentypen.

**Knowledge Acquisition** bezeichnet die Erhebung und Explizierung dieses relevanten Wissens. Mögliche Verfahren sind Dokumentenanalyse, Interviews, Workshops, Beobachtung von Arbeitsabläufen, Fehleranalyse und gemeinsame Modellierungssitzungen.

Im Editionsprojekt könnte ein Interview ergeben, dass `<supplied>` nur verwendet werden darf, wenn eine Ergänzung mit hoher Sicherheit aus dem unmittelbaren Kontext erschlossen werden kann. Diese Regel steht vielleicht nicht in der alten Richtlinie, wird aber seit Jahren praktiziert. Knowledge Acquisition macht sie sichtbar; Distillation überführt sie anschließend in eine überprüfbare Form.

## 5.3 Project Knowledge Base

Eine Sammlung von Dateien ist noch keine Wissensbasis.

Eine **Project Knowledge Base** ist der persistente, inspizierbare und revidierbare Bestand des dokumentierten Projektwissens. Sie hält die gegenwärtige Auffassung des Projekts über seine Daten, seinen Zweck und die relevanten Entscheidungen fest.

Für eine digitale Edition kann sie enthalten:

knowledge/

├── research-context.md

├── source-description.md

├── transcription-rules.md

├── terminology.md

├── tei-model.md

├── entities.md

├── uncertainty.md

├── requirements.md

├── design.md

├── verification.md

└── decisions.md

Die Wissensbasis ersetzt Quellen und Forschungsdaten nicht. Sie beschreibt und kontextualisiert deren Verwendung. `source-description.md` ist nicht die Quelle. `tei-model.md` ist nicht die TEI-Datei. Beide dokumentieren jedoch, wie mit den Quellen und Daten gearbeitet werden soll.

## 5.4 Wissensdokumente

Ein Editionsprojekt kann seine Regeln in einer langen Richtlinie, mehreren E-Mails und mündlich weitergegebenem Erfahrungswissen verteilen. Für eine konkrete Aufgabe ist ein solcher Bestand schwer nutzbar. Ein Agent müsste die relevanten Aussagen jedes Mal neu suchen und könnte widersprüchliche Fassungen miteinander vermischen.

Ein Wissensdokument führt die für einen abgegrenzten Gegenstand relevanten Aussagen in einer überprüfbaren Form zusammen. Es kann beispielsweise festhalten, wie unsichere Lesungen markiert werden, welche Ausnahmen gelten und wie diese Unsicherheit im Frontend sichtbar werden soll.

Ein **Wissensdokument** ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus einem umfangreicheren Bestand destilliert, von Menschen geprüft und von LLM-basierten Systemen als Kontext genutzt werden kann.

Wichtige Eigenschaften sind:

- klar abgegrenzter Gegenstand,  
- nachvollziehbare Struktur,  
- sichtbare Unsicherheiten,  
- dokumentierte Provenienz,  
- Revidierbarkeit,  
- duale Lesbarkeit für Menschen und LLM-basierte Systeme.

Beispiel:

\---

document\_type: knowledge

status: reviewed

topic: uncertain readings

sources:

  \- editorial-guidelines-v2.pdf

  \- workshop-2026-04-12.md

\---

\<a id="unsichere-lesungen"\>\</a\>

\# Unsichere Lesungen

\<a id="grundregel"\>\</a\>

\#\# Grundregel

Eine lesbare, aber nicht sicher identifizierbare Zeichenfolge wird mit

\`\<unclear\>\` ausgezeichnet.

\<a id="unleserliche-stellen"\>\</a\>

\#\# Unleserliche Stellen

Ist keine belastbare Zeichenfolge erkennbar, wird keine hypothetische

Lesung als regulärer Text eingetragen.

\<a id="erganzungen"\>\</a\>

\#\# Ergänzungen

\`\<supplied\>\` wird nur verwendet, wenn eine Ergänzung durch den unmittelbaren

Kontext begründet ist. Die Begründung muss nachvollziehbar bleiben.

\<a id="darstellung-im-frontend"\>\</a\>

\#\# Darstellung im Frontend

Unsichere Lesungen werden visuell markiert. Die Benutzeroberfläche darf

sie nicht wie sicheren Text darstellen.

\<a id="offene-frage"\>\</a\>

\#\# Offene Frage

Für teilweise lesbare Eigennamen ist noch zu klären, ob Zeichen- oder

Wortebene ausgezeichnet wird.

## 5.5 Markdown als technische Repräsentation

Das Wissensdokument ist ein konzeptionelles Artefakt und nicht an ein bestimmtes Dateiformat gebunden. Im hier beschriebenen Workflow wird Markdown verwendet, weil es offen, textbasiert und sowohl für Menschen als auch für LLM-basierte Systeme gut lesbar ist.

Markdown trennt Struktur und Inhalt durch einfache Zeichen:

- `#` für Überschriften,  
- Listenpunkte,  
- Links,  
- Tabellen,  
- Codeblöcke.

Vorteile:

- mit unterschiedlichen Editoren lesbar;  
- zeilenweise versionierbar;  
- einfach referenzierbar;  
- in Obsidian oder anderen Systemen verlinkbar;  
- gezielt in Working Contexts aufnehmbar.

Markdown macht Inhalte nicht automatisch korrekt. Es schafft lediglich eine Form, in der Menschen und Agents am selben dokumentierten Bestand arbeiten können.

## 5.6 Instruktionsdateien und Agent Skills

Nicht jede persistente Information ist ein Wissensdokument.

### Wissensdokument

Beschreibt, was über einen Gegenstand bekannt ist:

- `uncertainty.md`  
- `tei-model.md`  
- `requirements.md`

### Instruktionsdatei

Legt wiederkehrende Regeln für agentische Arbeit fest, etwa in `CLAUDE.md` oder `AGENTS.md`:

\<a id="arbeitsweise"\>\</a\>

\#\# Arbeitsweise

\- Verändere keine Quelldateien.

\- Lies vor jeder TEI-Änderung die relevanten Wissensdokumente.

\- Trenne technische Fehler von fachlichen Fragen.

\- Melde eine Aufgabe erst als abgeschlossen, nachdem die vorgesehenen

  Validatoren und Tests ausgeführt wurden.

### Agent Skill

Bündelt Instruktionen, Skripte und Ressourcen für eine wiederkehrende Aufgabenklasse. Ein Skill könnte beschreiben, wie:

- TEI-Dateien validiert werden,  
- ein Datenprofil erzeugt wird,  
- eine Editionsseite transformiert wird,  
- ein Acceptance Report erstellt wird.

Die Unterscheidung lautet:

> Ein Wissensdokument beschreibt den Gegenstand. Eine Instruktionsdatei regelt die wiederkehrende Arbeit. Ein Skill operationalisiert ein wiederverwendbares Verfahren. Ein Prompt formuliert die aktuelle Aufgabe.

## 5.7 Governance und Kuration

Wissensbasen verlieren ohne Pflege an Nutzbarkeit. Dokumente werden veraltet, Begriffe uneinheitlich und parallele Fassungen widersprüchlich.

**Governance** bestimmt Regeln für Aufbau, Änderung und Nutzung. **Kuration** wendet diese Regeln auf den konkreten Bestand an.

Strukturelle Kuration betrifft:

- Dateinamen,  
- Metadaten,  
- Links,  
- Dokumenttypen,  
- Versionsangaben,  
- Dubletten.

Inhaltliche Kuration betrifft:

- widersprüchliche Aussagen,  
- veraltete Regeln,  
- fehlende Einschränkungen,  
- unangemessene Verdichtungen,  
- Revision von Anforderungen.

Ein Agent kann Probleme lokalisieren und Vorschläge erzeugen. Inhaltlich folgenreiche Änderungen müssen jedoch geprüft und verantwortet werden.

## 5.8 Hands-on: Ein Wissensdokument zu editorischer Unsicherheit destillieren

### Ausgangsmaterial

- zwei Richtlinienauszüge,  
- drei E-Mails,  
- ein Protokoll,  
- zwei TEI-Beispiele,  
- eine mündlich ergänzte Projektregel.

### Auftrag

1. Identifizieren Sie relevante Aussagen.  
2. Markieren Sie Widersprüche.  
3. Trennen Sie verbindliche Regeln, Beispiele und offene Fragen.  
4. Erstellen Sie `uncertainty.md`.  
5. Dokumentieren Sie die Quellen.  
6. Prüfen Sie, welche Information bei der Verdichtung verloren gehen könnte.

### Prüfkriterien

- Sind Unsicherheiten sichtbar?  
- Wurden Ausnahmen erhalten?  
- Ist die Provenienz nachvollziehbar?  
- Ist das Dokument kompakt, aber hinreichend?  
- Kann es unmittelbar als Kontext für eine TEI-Aufgabe verwendet werden?

*Source: `full-lecture-notes-en.md`, "Knowledge Modelling, Personal Information Management and Project Management".*

## **Knowledge Modelling, Personal Information Management and Project Management**

The form of Knowledge Engineering developed here draws on several neighbouring traditions. Classical **knowledge modelling** identifies concepts in a domain, represents relations and supports querying or inference.[^9] **Personal Information Management** studies how people acquire, organise, maintain, retrieve, use and share information across formats and locations, with fragmentation as a recurring problem.[^38] **Project management** contributes procedures for initiating, planning, executing, monitoring and closing work within explicit constraints.[^39]

AI supported knowledge work combines concerns from all three. It needs domain representations, usable information collections and operational project state. A maintained knowledge environment may therefore contain conceptual definitions, source references, requirements, decisions, process descriptions, instructions, open questions and evaluation criteria.

The goal is not to collapse these traditions into one discipline. It is to recognise that advanced work with AI agents requires aspects of all three.


## Notes

*Footnote identifiers and definitions are reproduced unchanged from their source lecture notes.*

### Notes carried from the German Full Lecture Notes

[^4]: Die nominelle Kontextgröße ist nicht mit einer garantierten effektiven Nutzung aller enthaltenen Information gleichzusetzen. Forschung zu Long-Context-Systemen untersucht unter anderem Positions-, Distraktor- und Retrievaleffekte.

### Notes carried from the English Full Lecture Notes

[^9]: Bradley P. Allen et al., “Knowledge Engineering Using Large Language Models,” 2023, https://doi.org/10.4230/TGDK.1.1.3; Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., 2020, https://aima.cs.berkeley.edu.

[^10]: Lingrui Mei et al., “A Survey of Context Engineering for Large Language Models,” 2025, https://doi.org/10.48550/arXiv.2507.13334. The formulation used here follows Pollin, *Promptotyping*, review draft 0.9, 2026.

[^38]: William Jones, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez Quiñones, “Personal Information Management,” 2017, https://doi.org/10.1081/E-ELIS4-120053695.

[^39]: See Jürg Kuster et al., *Handbuch Projektmanagement*, Springer, and the project management literature referenced in the slide deck.
