---
title: Google Docs state of the German lecture notes, 2026-11-10
status: snapshot
created: 2026-11-10
language: de
source: https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit
source-modified: 2026-11-10T08:15:16Z
retrieved: 2026-11-10
canonical: false
related: [../full-lecture-notes-de.md, ../../workshops/2026-11-09-ufl/lecture-notes.md]
---

<!-- Unchanged text of the Google Doc as returned by the Drive connector on 2026-11-10. It secures passages that
     exist only in the Doc before the Markdown source is revised. It is not a maintained holding. -->

# **Knowledge, Context and Agentic Engineering**

## *Konzepte, Methoden und Workflows für die kontrollierte Arbeit mit LLM-basierten AI Agents*

**Dr. Christopher Pollin, MA MA**

Digital Humanities Craft OG

[www.dhcraft.or](https://www.dhcraft.org)g |[ office@dhcraft.or](mailto:office@dhcraft.org)g

Workshopskriptum, Arbeitsfassung, November 2026

**Foliensatz:** *Knowledge, Context and Agentic Engineering*

**Begleitmaterialien:** Workshopunterlagen und Hands-on-Dateien

# Abstract

LLM-basierte AI Agents können computer- und datenbasierte Forschungsarbeit über einzelne Modellantworten hinaus unterstützen. Sie können Dateien untersuchen, Werkzeuge aufrufen, Programme ausführen, Zwischenergebnisse verarbeiten und digitale Forschungsartefakte über mehrere Schritte hinweg entwickeln. Ihre produktive Nutzung hängt jedoch nicht allein von der Leistungsfähigkeit eines Modells oder der Formulierung einzelner Prompts ab. Sie setzt voraus, dass relevantes Projektwissen explizit dokumentiert, für konkrete Aufgaben gezielt bereitgestellt und die daraus entstehende agentische Arbeit innerhalb einer technischen Umgebung organisiert, begrenzt und geprüft wird.

Prompt Engineering formuliert Aufgaben und Vorgaben. Knowledge Engineering dokumentiert, strukturiert und pflegt relevantes Wissen. Context Engineering stellt Anweisungen, Wissen, Arbeitsstand und Ergebnisse aus Tool Use für den jeweiligen LLM-Aufruf zusammen und passt sie im Arbeitsverlauf an. Agentic Engineering gestaltet den Einsatz von AI Agents für mehrschrittige Wissensarbeit. Harness Engineering gestaltet ihre technische Arbeitsumgebung mit Werkzeugen, Befugnissen und Prüfverfahren. Diese Aufgaben greifen ineinander.

Diese Ebenen werden im **Promptotyping** als iterativer, dokumentenbasierter Forschungsworkflow verbunden. Eine fortschreibbare Project Knowledge Base hält den gegenwärtigen Stand des Projektwissens fest. Für einzelne Aufgaben werden daraus geeignete Working Contexts zusammengestellt. AI Agents erzeugen oder verändern auf dieser Grundlage digitale Forschungsartefakte. Erkenntnisse aus Exploration, Implementation und Prüfung werden anschließend in den dokumentierten Projektstand zurückgeführt.

Im Workshop entsteht schrittweise eine Wissensbasis zu Agentic Engineering und Governance für die eigene Arbeit und Organisation. Die Teilnehmenden recherchieren Quellen, destillieren Wissen in Wissensdokumente und entwickeln daraus einen Governance-Entwurf für einen eigenen Anwendungsfall. Anschließend untersuchen sie Autonomie und Zugriff im eigenen Setup. Die digitale Edition dient ergänzend als fachliches Beispiel für Forschungsdaten, Modellierung und wissenschaftliche Prüfung.

# Zu diesem Skriptum

Das Skriptum erläutert die Begriffe und Arbeitsweisen des Workshops und dokumentiert die Übungen. Der Workshop-Pfad führt durch Recherche, Destillation, Nutzung der Wissensbasis und die Prüfung des eigenen Setups. Die Kapitel ordnen die Begriffe systematisch, ergänzende Editionsbeispiele vertiefen ihre Anwendung in der Forschung. Quellen stehen als Kurzbelege im Text und mit vollständigen Angaben im Literaturverzeichnis. Die technischen Hinweise beziehen sich auf die verlinkte Produktdokumentation.

# Inhaltsverzeichnis

[**1. Einführung**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.q317t7idtco6)

[1.1 Ausgangslage](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.5eeivwh9ilsw)

[1.2 Prompts und organisierte Arbeitsumgebungen](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.v3skr2onkcvf)

[1.3 Zentrale These](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.1svzl9wakkjb)

[1.4 Ergänzendes Beispiel: eine digitale Edition](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ovafnnyikct8)

[1.5 Lernziele und Aufbau](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.vbdaw97h8k4v)

[1.6 Workshop-Praxis und Materialien](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.v5hxh9gu89il)

[**2. Grundlagen: LLM, Assistant, AI Agent und AI Harness**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.3oukd7kymfrd)

[2.1 LLMs als probabilistische Textsysteme](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.3kgsuoyhsu6m)

[2.2 Pre-Training, Post-Training und Assistant-Verhalten](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.37x2vhb6uamr)

[2.3 LLM-basierte AI Agents](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.lmxxf6ndqqge)

[2.4 Das AI Harness](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.6rzfri3ve1xq)

[2.5 Personal AI Agents](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.4df081u24q0q)

[**3. Prompt Engineering**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.sbna5qwgmqd5)

[3.1 Prompt und Prompt Engineering](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.w7k2d973n8ua)

[3.2 Der Prompt als begrenzte Spezifikation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.wqv8nlvwa359)

[3.3 Rollen- und Persona-Prompting](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.xc12bd53596d)

[3.4 Iteration, Self-Revision und strukturierte Ausgaben](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.uq1nrtobjqs5)

[3.5 Warum Promptwirkungen schwer zu evaluieren sind](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.14bkbconpcdw)

[3.6 Mechanistische Perspektive](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.inpyhsv0h1m)

[3.7 Grenzen des Prompt Engineering](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.wz2j8lc8k337)

[3.8 Hands-on 1: Webrecherche und Wissensdokumente](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.msa7zrcttm0s)

[**4. Context Engineering**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.n735e0d7gkl6)

[4.1 Kontext als Informationszustand einer Aufgabe](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.f84j6hvvgq6i)

[4.2 Context Window und Context Rot](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.57i6kbr4onkz)

[4.3 Wie Informationen in den Modellkontext gelangen](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.gki9px46uqfs)

[4.4 Context Compression und Distillation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.rwmw0cgkazb)

[4.5 Project Knowledge Base, Working Context und Context Window](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ydrsnjm0r9iu)

[4.6 Ergänzende Übung: Working Context für eine TEI-Aufgabe](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.qwzpdtv1sk4p)

[**5. Knowledge Engineering**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.9zt1ujsvotqp)

[5.1 Warum Projektwissen explizit werden muss](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.8l8skm2qf8t)

[5.2 Knowledge Acquisition](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.xq7flzjloym7)

[5.3 Project Knowledge Base](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.qpz6i8n94k73)

[5.4 Wissensdokumente](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.rb8xpw4ix27s)

[5.5 Markdown als technische Repräsentation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.dmtx0cr66ym5)

[5.6 Instruktionsdateien und Agent Skills](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.l485vq2a5ssl)

[5.7 Governance und Kuration](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.bpj2ff2rlah9)

[5.8 Hands-on 2: Wissen in Wissensdokumente destillieren](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ogqb3oqtgofz)

[**6. Agentic Engineering**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.g36dnp74et5j)

[6.1 Warum mehrschrittige Arbeit organisiert werden muss](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.6ew7juig66rx)

[6.2 Agentische Ausführungsschleife](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.qayxkyy2an2)

[6.3 Planung, Ausführung und Feedback](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.tcucet2xsks5)

[6.4 Werkzeuge, Berechtigungen und Reversibilität](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.e4neezw5n6va)

[6.5 MCP, Subagents und Agent-to-Agent-Kommunikation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.x68l9cma5lme)

[6.6 Versionierte Zwischenstände und menschliche Intervention](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.uadrd0kje19k)

[6.7 Ergänzende Übung: TEI erzeugen und ein Frontend implementieren](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.en7nrs9f2j4e)

[6.8 KI-Governance](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.mnu3252w07e3)

[6.9 Hands-on 3: Governance für den eigenen Anwendungsfall entwickeln](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.tgcjqkhjrquq)

[6.10 Autonomie und Systemzugriff](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.bgpj5tnokcq1)

[6.11 Hands-on: Autonomie und Zugriff im eigenen Setup prüfen](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.asumj4il2szj)

[6.12 Zwischenfazit](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.o1fvrhcdboeo)

[**7. Promptotyping**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ydcffnh7dfr8)

[7.1 Definition und Grundprinzip](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.xwsmkca1fpxb)

[7.2 Preparation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.rzyf38tkd0w0)

[7.3 Exploration](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.y6vm4bcxprtg)

[7.4 Distillation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.gyu2xr7dw6ro)

[7.5 Requirements Engineering und Scholar-Centred Design](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.opurbptkye90)

[7.6 Implementation](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.6b9589b09j5o)

[7.7 Verification, Validation und Acceptance](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.is73tazid66)

[7.8 Critical Expert](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.pav69m4m47a2)

[7.9 Write-back](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.8k0fvltm7wxv)

[7.10 Der Promptotype](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ifaz3woa5a13)

[7.11 Hands-on: Write-back und Acceptance dokumentieren](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.4q1ovos7x0pl)

[**8. Zusammenfassung und Begriffsübersicht**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.n90ugle3nlq3)

[**9. Literaturverzeichnis**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.8nzih42yx0z2)

[**10. Anhang: Vorlagen**](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit#heading=h.ndi2kwpfue4y)

# Abbildungsverzeichnis

  - Wissensbestand, Working Context und agentische Ausführung
  - Die digitale Edition als durchgehender Arbeitszusammenhang
  - Sprachmodell und Assistentenfigur
  - Konkurrierende Deutungen des Prompt Engineering
  - Modell-, aufgaben- und sprachabhängige Promptwirkungen
  - Warum Prompt Engineering schwer zu evaluieren ist
  - Didaktisches Modell der Promptwirkung
  - Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung
  - Project Knowledge Base, Working Context und Context Window
  - Agentische Ausführungsschleife
  - Promptotyping als geschlossener Entwicklungszyklus
  - Prüfung, Evidenz und verantwortliche Acceptance

# 1\. Einführung

## **1.1 Ausgangslage**

Large Language Models werden zunehmend nicht nur als Systeme für einzelne Frage-Antwort-Interaktionen eingesetzt. In Verbindung mit Dateien, Werkzeugen und Ausführungsumgebungen können sie Aufgaben über mehrere Schritte hinweg bearbeiten. Ein LLM-basierter AI Agent kann Projektressourcen untersuchen, Informationen aus unterschiedlichen Quellen zusammenführen, Code erzeugen und ausführen, Fehlermeldungen verarbeiten und sein weiteres Vorgehen an den beobachteten Projektzustand anpassen.

Diese Entwicklung erweitert die Möglichkeiten computer- und datenbasierter Forschung. Eine Historikerin kann beispielsweise aus einer kleinen Sammlung von Quellenbildern einen ersten Transkriptionsentwurf erzeugen lassen. Ein Editionsprojekt kann TEI-Dateien gegen ein Schema prüfen, Varianten eines Frontends erzeugen und die Darstellung editorischer Unsicherheit vergleichen. Ein Forschungsteam kann Datenprofile, Transformationen und Visualisierungen erstellen, ohne jeden technischen Schritt vollständig von Grund auf programmieren zu müssen.

Die Fähigkeit, ein Artefakt zu erzeugen, ist jedoch nicht mit der Fähigkeit gleichzusetzen, dessen technische Korrektheit oder wissenschaftliche Angemessenheit zuverlässig zu beurteilen. Eine TEI-Datei kann wohlgeformt und schema-valide sein, obwohl eine unsichere Lesung editorisch unangemessen als sicherer Text ausgezeichnet wurde. Ein Interface kann technisch funktionieren und trotzdem den Eindruck erwecken, eine normalisierte Form sei die einzig richtige Lesart. Ein Datenmodell kann konsistent sein und zugleich Unterschiede ausblenden, die für die Forschungsfrage entscheidend sind.

Die zentrale Herausforderung liegt deshalb nicht allein in der Erzeugung von Ergebnissen. Sie liegt in der Organisation der Bedingungen, unter denen diese Ergebnisse entstehen, geprüft, revidiert und für einen benannten Zweck verwendet werden können.

## **1.2 Prompts und organisierte Arbeitsumgebungen**

Bei einer einfachen und klar abgegrenzten Aufgabe kann eine präzise formulierte Anweisung ausreichen. Ein Prompt kann etwa verlangen, aus einer Tabelle alle Datumsangaben zu extrahieren und als JSON auszugeben. Sobald eine Aufgabe jedoch mehrere Dateien, Werkzeuge und Entscheidungen umfasst, reicht die Betrachtung eines einzelnen Prompts nicht mehr aus.

Nehmen wir an, ein Agent soll für eine digitale Edition eine historische Seite transkribieren, als TEI modellieren und anschließend in einem Frontend darstellen. Dafür muss geklärt werden:

  - Welche Transkriptionsrichtlinien gelten?
  - Welche Version des TEI-Modells ist maßgeblich?
  - Wie werden unleserliche Stellen, Ergänzungen und Streichungen repräsentiert?
  - Darf der Agent die Ausgangsdatei verändern?
  - Welche Tests müssen ausgeführt werden?
  - Was geschieht, wenn eine editorische Entscheidung nicht aus den Quellen oder Richtlinien hervorgeht?
  - Welche Erkenntnisse aus der Implementation müssen in die Projektdokumentation zurückgeschrieben werden?

Diese Fragen betreffen unterschiedliche Ebenen. Ein Teil gehört zur Gestaltung der aktuellen Aufgabe, ein Teil zum persistenten Projektwissen, ein Teil zur Auswahl des aufgabenspezifischen Kontextes und ein Teil zur Kontrolle der mehrschrittigen Ausführung.

## **1.3 Zentrale These**

Die zentrale These dieses Skriptums lautet:

**Abbildung 1: Wissensbestand, Working Context und agentische Ausführung.**

Die Übersicht verbindet Aufgabe, Wissensbestand, aktuellen Kontext und agentische Ausführung. Harness Engineering betrifft die technische Umgebung, in der dieser Ablauf stattfindet. Rückmeldungen aus der Arbeit und ihrer Prüfung können Änderungen an den Anforderungen, den Wissensdokumenten, dem Kontext und der Konfiguration des Harness erforderlich machen.

*Produktive und nachvollziehbare Arbeit mit LLM-basierten AI Agents entsteht nicht allein durch bessere Modelle oder besser formulierte Prompts. Sie setzt das Zusammenspiel von organisiertem Projektwissen, aufgabenspezifischem Kontext, kontrollierter agentischer Ausführung und verantwortlicher Prüfung voraus.*

Die Engineering-Begriffe bezeichnen unterschiedliche Gestaltungsaufgaben:

  - **Prompt Engineering** gestaltet die aktuelle Eingabesequenz.
  - **Knowledge Engineering** baut und pflegt den verfügbaren Wissensbestand.
  - **Context Engineering** stellt den für eine konkrete Aufgabe erforderlichen Informationszustand zusammen.
  - **Agentic Engineering** organisiert die mehrschrittige Ausführung innerhalb einer technischen Umgebung.

<!-- end list -->

  - Harness Engineering gestaltet die technische Arbeitsumgebung mit ihren Werkzeugen, Befugnissen und Prüfverfahren.

Das **AI Harness** vermittelt zwischen diesen Ebenen. Es stellt Werkzeuge und Zugriffe bereit, verwaltet den Zustand einer Arbeit und gibt Ergebnisse an das Modell zurück. Es entscheidet jedoch nicht, welche editorische Lesung angemessen ist oder ob ein Artefakt für eine Publikation akzeptiert werden kann.

## **1.4 Ergänzendes Beispiel: eine digitale Edition**

Die digitale Edition dient als ergänzendes Forschungsbeispiel. Ausgangspunkt sind historische Seitenbilder, eine Rohtranskription, editorische Richtlinien und ein begrenztes TEI-Ausgangsmodell. Ziel ist ein lokaler Demonstrator, der Faksimile, diplomatische Transkription, normalisierte Lesung und editorische Unsicherheiten sichtbar macht.

Das Beispiel verbindet drei Arbeitsbereiche:

**Abbildung 2: Die digitale Edition als durchgehender Arbeitszusammenhang.**

*Die Abbildung verbindet Quellenbilder und Datenerzeugung mit TEI-basierter Datenmodellierung, Transformation und Frontend-Darstellung. Die Pfeile verlaufen nicht nur in Richtung des Interfaces: Probleme, die erst in der Darstellung sichtbar werden, führen zurück zu Transkription, Modellierungsregeln und Anforderungen.*

  - **Datenerzeugung:** Transkription, Annotation, Normalisierung und Provenienz.
  - **Datenmodellierung:** TEI-Strukturen, Entitäten, Relationen, Varianten und Unsicherheiten.
  - **Frontend-Darstellung:** synoptische Ansichten, Umschaltung von Textschichten, Hervorhebung von Annotationen und Darstellung editorischer Eingriffe.

Die Bereiche sind nicht voneinander unabhängig. Erst in der Frontend-Darstellung kann sichtbar werden, dass eine Modellierungsregel unzureichend ist. Eine als einfaches Attribut modellierte Unsicherheit kann sich beispielsweise nicht differenziert genug darstellen lassen. Umgekehrt kann eine elegante Oberfläche eine editorisch problematische Vereinfachung verdecken. Die Implementation ist daher nicht nur Ausführung, sondern auch eine Form der Untersuchung des Projektwissens.

## **1.5 Lernziele und Aufbau**

Nach dem Workshop können die Teilnehmenden:

  - AI Agents für Wissensarbeit einsetzen und durch klare Ziele und Vorgaben steuern (Agentic Engineering).
  - Wissen so dokumentieren, strukturieren und pflegen, dass Menschen und AI Agents es nachvollziehen, prüfen und weiterentwickeln können (Knowledge Engineering).
  - Anweisungen, relevantes Wissen, den Arbeitsstand und Ergebnisse aus Tool Use für den jeweiligen LLM-Aufruf zusammenstellen und im Arbeitsverlauf anpassen (Context Engineering).
  - Die technische Arbeitsumgebung eines AI Agents mit ihren Werkzeugen, Befugnissen und Prüfverfahren erklären und nutzen (Harness Engineering).

## **1.6 Workshop-Praxis und Materialien**

Im Workshop untersuchen wir, wie AI Agents auf Basis von Frontier-LLMs Wissensarbeit amplifizieren können. Mit Zugang und den erforderlichen Kompetenzen lassen sich auch spezialisierte Werkzeuge für eigene Arbeitsprozesse entwickeln und anpassen. Die schnelle technologische Entwicklung verlangt laufende Orientierung, die Arbeit mit AI Agents erfordert fachliche und technische Entscheidungen.

Digital Humanities Craft entwickelt Werkzeuge und Workflows mit einem Schwerpunkt auf angewandter generativer KI zur Forschungsunterstützung. Gemeinsam mit Forschenden entstehen iterativ spezialisierte Forschungswerkzeuge und Workflows. AI Agents im AI Harness unterstützen die Umsetzung, häufig als statische Anwendungen im Browser. Dabei bestimmen die Forschenden die Anforderungen und prüfen die fachliche Eignung.

Die Vorstellungsrunde klärt Rolle und Arbeitsbereich, bisherige LLM- und Agentennutzung, Programmiervorkenntnisse sowie das Verständnis von Context Window und Reasoning-Modellen. Außerdem wird erfragt, welcher AI Harness einsatzbereit ist und ob lokal betriebene LLMs oder andere Anbieter genutzt werden. Erwartungen an den Workshop und die persönliche Wahrnehmung der KI-Entwicklung ergänzen diese Orientierung.

Für die Übungen wird ein leerer Projektordner angelegt und eine Session mit Zugriff auf diesen Ordner gestartet. Die Übungen bis zum Zwischenfazit bleiben in derselben Konversation. Während Agents arbeiten, werden Konzepte besprochen. Rückfragen, Freigabeanfragen und Tool-Aufrufe bleiben dabei im Blick.

LLM, Anbieter und Harness werden getrennt ausgewählt. Modellwahl, Reasoning beziehungsweise Effort und Usage beeinflussen den Arbeitsablauf. Subagents verbrauchen ebenfalls Ressourcen. Ein lokaler Harness kann ein extern betriebenes LLM verwenden. Wo die Oberfläche läuft, beantwortet deshalb noch nicht, wo die Daten verarbeitet werden.

Eigene Daten können einbezogen werden. Vorab ist zu klären, welche personenbezogenen oder vertraulichen Inhalte enthalten sind, wohin sie übertragen werden und welche Vorgaben der Organisation gelten. Die technische Möglichkeit eines Uploads stellt keine organisatorische Freigabe dar.

### **Materialien**

Website mit Materialien: <https://dhcraft.org/knowledge-context-agentic-engineering>

Glossar: <https://dhcraft.org/knowledge-context-agentic-engineering/glossary.de.html>

Beispiele für Forschungswerkzeuge: <https://dhcraft.org/fancy-research-tools>

Technische Vorbereitung: <https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit>

# 2\. Grundlagen: LLM, Assistant, AI Agent und AI Harness

## **2.1 LLMs als probabilistische Textsysteme**

Ein Large Language Model erzeugt Text, indem es auf Grundlage der bisherigen Eingabesequenz Wahrscheinlichkeiten für das nächste Token berechnet. Das ausgewählte Token wird Teil des Kontextes für die nächste Vorhersage. Dieser autoregressive Vorgang wird wiederholt, bis eine Ausgabe abgeschlossen ist.\[1\]

Die Beschreibung als *Next Token Prediction* klingt einfacher, als das beobachtete Verhalten vermuten lässt. Durch umfangreiches Pre-Training können Modelle sprachliche, fachliche und formale Muster reproduzieren, Texte transformieren, Code erzeugen und komplexe Aufgaben bearbeiten. Dennoch bleibt die Ausgabe probabilistisch. Derselbe Prompt kann bei mehreren Durchläufen unterschiedliche Ergebnisse erzeugen. Eine plausible Formulierung ist daher nicht automatisch eine rekonstruierte Tatsache, und eine kohärente Begründung ist nicht automatisch ein Nachweis ihrer Richtigkeit.

Für die digitale Edition bedeutet dies: Ein Modell kann eine sehr überzeugende Transkription erzeugen, obwohl einzelne Zeichen falsch gelesen wurden. Es kann eine TEI-Struktur ausgeben, die formal plausibel aussieht, obwohl sie nicht den projektspezifischen Richtlinien entspricht. Die sprachliche Qualität einer Antwort darf deshalb nicht mit ihrer fachlichen Verlässlichkeit verwechselt werden.

### **Tokens und Tokenizer**

Ein Token ist eine Einheit, in die ein LLM Text zerlegt, häufig ein Wort oder Wortteil. Ein Tokenizer zerlegt den Text in solche Einheiten und ordnet ihnen numerische Kennungen zu. Die Tokenisierung hängt vom jeweiligen LLM ab. Kontextgrenzen und die verbrauchsabhängige Abrechnung vieler Angebote werden in Tokens angegeben.

### **Reasoning und Effort**

Reasoning bezeichnet hier die zusätzliche Verarbeitung eines LLM für Schlussfolgerungsaufgaben. Bei vielen Reasoning-LLMs entstehen dabei weitere Tokens, die nicht vollständig als Antwort sichtbar werden. Eine Einstellung wie Effort steuert je nach System den vorgesehenen Verarbeitungsaufwand. Sie garantiert keine korrekten Ergebnisse. Die konkrete Wirkung und die verfügbaren Stufen sind produktabhängig.

### **Gezackte Fähigkeitenprofile**

Frontier-LLMs bezeichnet im Workshop die jeweils leistungsfähigsten allgemein einsetzbaren LLMs. Welche Systeme dazu zählen, hängt vom Zeitpunkt und den betrachteten Aufgaben ab. Die Bezeichnung garantiert keine verlässliche Leistung für einen konkreten Arbeitsprozess. Als Blackbox wird die begrenzte Einsicht in die internen Berechnungen beschrieben. Eine ausgegebene Begründung ist keine vollständige Rekonstruktion dieser Berechnungen.

Die Formulierung „Jagged Alien Intelligences“ beschreibt im Workshop ein ungewohntes, ungleichmäßiges Fähigkeitenprofil. Eine überzeugende Leistung bei einer schwierigen Aufgabe erlaubt keine sichere Aussage über eine andere, scheinbar einfachere Aufgabe. Die Metapher bezeichnet weder eine einheitliche wissenschaftliche Intelligenzklasse noch menschliches Denken.

Für die Arbeit sind insbesondere Konfabulationen, also plausibel formulierte erfundene Inhalte, Verzerrungen (Bias) und Sycophancy relevant. Sycophancy bezeichnet eine übermäßige Anpassung an die Annahmen oder Erwartungen der fragenden Person. Gegenmaßnahmen im Workshop sind belegte Aussagen, ausdrückliche Prüfkriterien und kritische Gegenperspektiven.

Der Knowledge Cut-off bezeichnet den angegebenen zeitlichen Stand des Trainingswissens und garantiert keine vollständige Kenntnis aller früheren Ereignisse. Neue Informationen im Gespräch verändern den aktuellen Kontext. Daraus folgt keine laufende Aktualisierung der LLM-Gewichte. Websuche und Dateizugriff können aktuellere Informationen bereitstellen. Rechenaufgaben lassen sich an ausführbaren Code übergeben und am Ergebnis prüfen.

## **2.2 Pre-Training, Post-Training und Assistant-Verhalten**

Im Pre-Training werden umfangreiche Text- und andere Datenbestände verwendet, um statistische Repräsentationen sprachlicher und fachlicher Muster zu lernen. Vereinfacht kann man sagen, dass dabei modellintern nutzbare Zusammenhänge entstehen. Diese sind jedoch nicht wie Einträge in einer Datenbank adressierbar. Das Modell besitzt kein verlässliches Seiten- oder Quellenregister und kann seltene oder editionsspezifische Informationen falsch rekonstruieren.

Post-Training richtet das Modell stärker auf bestimmte Aufgaben-, Interaktions- und Verhaltensformen aus. Dazu gehören Instruction Tuning, Reinforcement Learning from Human Feedback und verwandte Verfahren. Ein Basismodell wird dadurch zu einem System, das typischerweise als hilfreicher Assistent antwortet, Anweisungen befolgt und bestimmte Sicherheits- oder Stilregeln berücksichtigt.

Die in einer Interaktion erscheinende Assistentenfigur ist nicht mit einem menschlichen Gegenüber gleichzusetzen.

Folie zur Unterscheidung zwischen Sprachmodell und Assistentenfigur

**Abbildung 3: Sprachmodell und Assistentenfigur.**

*Die Folie unterscheidet das zugrunde liegende Modell von dem durch Post-Training, Systeminstruktionen und aktuellen Kontext stabilisierten Assistentenverhalten. Die anthropomorphe Form der Interaktion ist praktisch nützlich, darf aber nicht als Nachweis menschlicher Intentionalität oder fachlicher Autorität verstanden werden.* Sie ist ein durch Training, Systeminstruktionen und aktuellen Kontext stabilisiertes Verhaltensmuster. Das erklärt, warum sachliche, strukturierte Kommunikation häufig produktiv ist: Das Modell ist auf menschliche Kommunikationsformen ausgerichtet. Es erklärt zugleich, warum soziale Kohärenz nicht mit menschlicher Intentionalität oder fachlicher Autorität verwechselt werden darf.\[2\]

## **2.3 LLM-basierte AI Agents**

Ein LLM-basierter AI Agent ist ein System, das für ein vorgegebenes Ziel schrittweise die nächsten Aktionen auswählt. Bei Tool Use formuliert das LLM einen Werkzeugaufruf, etwa für eine Websuche oder das Lesen einer Datei. Der AI Harness führt den Aufruf aus und gibt das Ergebnis an das LLM zurück. Dieses berücksichtigt es bei der nächsten Entscheidung.

Tool Use verbindet die Textgenerierung des LLM mit ausführbaren Funktionen. Welche Werkzeuge verfügbar sind und ob ihre Ausführung erlaubt ist, regelt die Umgebung. Ein Werkzeugaufruf kann Daten lesen, etwas berechnen oder einen Zustand verändern. Die folgenden Schritte zeigen eine mögliche agentische Nutzung des Terminals.

### **Beispiel einer Projektzusammenfassung**

Fass mir zusammen, worum es in diesem Projekt geht.

1.  ls listet den Projektordner auf. Darin findet der Agent den Ordner knowledge.
2.  cd .\\knowledge wechselt in diesen Ordner.
3.  ls listet dessen Inhalt auf. Darin liegt project.md.
4.  cat .\\project.md liest den Dateiinhalt. Daraus erstellt der Agent die Zusammenfassung.

Hier wählt der Agent die Schritte selbst. Tool Use kann auch Teil eines vorgegebenen Ablaufs sein. Das gelesene Ergebnis beeinflusst die nächste Entscheidung, es legt sie nicht zwingend fest. Die Befehle dienen als Beispiel für eine PowerShell-Session. Ein anderer Harness kann dieselbe Aufgabe mit einem Dateilesewerkzeug erledigen.

Dokumentation zur Agentenschleife und Werkzeugausführung: Anthropic, How Claude Code works.

## **2.4 Das AI Harness**

Ein AI Harness ist die Softwareumgebung eines AI Agents. Er führt die Agentenschleife aus, stellt Kontext und Werkzeuge bereit und kontrolliert Zugriffs- und Handlungsrechte. Das LLM, die Oberfläche und die Ausführungsumgebung erfüllen unterschiedliche Funktionen. Die Definition verdichtet die von Zhong und Zhu (2026) beschriebenen Aufgaben einer Laufzeitumgebung für Software-Agents.\[3\]

Das Harness kann beispielsweise festlegen:

  - welche Ordner gelesen oder verändert werden dürfen;
  - welche Befehle ohne Bestätigung ausgeführt werden können;
  - wie Werkzeugausgaben in den Modellkontext zurückgelangen;
  - wie lange ein Lauf fortgesetzt wird;
  - wann ein Mensch einbezogen werden muss;
  - wie Zwischenergebnisse gespeichert werden.

Das Harness stellt technische Kontrollmöglichkeiten bereit. Es entscheidet jedoch nicht, ob eine editorische Modellierung wissenschaftlich angemessen ist. Ein XML-Validator kann feststellen, dass \<unclear\> an einer bestimmten Stelle zulässig ist. Er kann nicht entscheiden, ob die Quelle tatsächlich unleserlich ist oder ob eine alternative Lesung wahrscheinlicher wäre.

Harness Engineering gestaltet diese Umgebung. Dazu gehören die Auswahl und Anbindung von Werkzeugen, der Zugriff auf Dateien und Dienste, Freigaben, Protokollierung und Prüfverfahren. Ein leistungsfähiges LLM erhält dadurch keine pauschale Handlungsbefugnis. Der erlaubte Zugriff muss zum jeweiligen Auftrag passen.

### Beispiele für AI Harnesses

  - Claude Code: <https://claude.ai/code>
  - Codex: <https://chatgpt.com/codex>
  - Antigravity: <https://antigravity.google.com>
  - Cursor: <https://cursor.com/>
  - Devin Desktop (vormals Windsurf): <https://devin.ai/desktop>
  - Pi (Open Source): <https://pi.dev/>
  - OpenCode (Open Source): <https://opencode.ai/>
  - Manus: <https://manus.im/>

Die Beispiele sind nach ihrem Anwendungsschwerpunkt eingeordnet. Open Source bezeichnet die Software des Harness. Die verwendeten LLMs können über externe Dienste laufen. Betriebsort, LLM-Wahl und Befugnisse hängen von der Einrichtung ab.

## 2.5 Personal AI Agents

Ein Personal AI Agent behält über einzelne Gespräche hinweg Kontext und betreut längerfristig Aufgaben einer Person. Innerhalb vereinbarter Befugnisse wird er selbstständig tätig. Seine technische Arbeitsumgebung ist ein AI Harness. Diese Arbeitsdefinition greift die Vision dauerhafter persönlicher Agents bei Wu et al. (2026) auf.

Die Begriffe beschreiben unterschiedliche Ebenen. Der Harness stellt die technische Ausführung und Kontrolle bereit. Personal AI Agent bezeichnet die längerfristige Betreuung einer Person und ihrer Aufgaben. Ein System kann beide Funktionen verbinden.

### Beispiele für Personal AI Agents

  - OpenAI dots: <https://learn.chatgpt.com/docs/dots>
  - Grok Bot: <https://x.ai/bot>
  - Claude Duet: <https://claude.com/product/claude-duet>
  - Hermes Agent (Open Source): <https://hermes-agent.nousresearch.com/>
  - OpenClaw (Open Source): <https://openclaw.ai/>

### Dauerhafte Delegation und menschliche Kontrolle

Das Paper Avatar Intelligence beschreibt eine Vision dauerhafter persönlicher AI Agents, die Ziele, Präferenzen und Einschränkungen einer Person über Aufgaben und Gespräche hinweg berücksichtigen. Entscheidend ist die Delegation von Entscheidungen innerhalb vereinbarter Befugnisse. Die Person behält das Recht, Ziele zu ändern, einzugreifen und Befugnisse zu widerrufen. Ein gemeinsamer Kern aus Nutzermodell und Gedächtnis soll spezialisierte Agenten für unterschiedliche Aufgaben verbinden (Wu et al., 2026).

Fortschritt bemisst sich dabei auch an der menschlichen Arbeit, die für ein verlässliches Ergebnis nötig bleibt. Zielklärung, Rückfragen, Koordination und Prüfung kosten Zeit. Der vorgeschlagene Agentic Oversight Index berücksichtigt deshalb den gelieferten Nutzen, die technischen Betriebskosten und den menschlichen Betreuungsaufwand. Er ist ein konzeptioneller Bewertungsvorschlag, noch kein empirisch validiertes Maß (Wu et al., 2026).

Die Roadmap reicht von eng angeleiteter Ausführung über Delegation mit gezielten Kontrollpunkten bis zu selbstständigem Handeln in abgegrenzten Bereichen. Ein Agent kann je nach Aufgabe unterschiedlich autonom arbeiten. Mehr Autonomie ist deshalb keine pauschale Eigenschaft des gesamten Systems (Wu et al., 2026).

### Forschungsaufgaben bei dauerhaften persönlichen Agents

  - Personalisierung soll auch Entscheidungspräferenzen berücksichtigen.
  - Rehearsal Engineering soll Agents ermöglichen, repräsentative Situationen zu erproben und aus kontrolliertem Feedback zu lernen.
  - Sicherheit und Verantwortlichkeit sollen durch begrenzte Zugriffsrechte, Freigaben, Protokolle und Korrekturmöglichkeiten gesichert werden.

Diese Forschungsaufgaben stehen im Mittelpunkt des Papers. Versicherungen werden ergänzend als Möglichkeit diskutiert, verbleibende finanzielle Schäden abzusichern (Wu et al., 2026).

Für den Workshop lässt sich daraus ableiten, dass ein Personal AI Agent Kontinuität, klare Befugnisse und angemessene Kontrolle braucht. Der AI Harness stellt dafür die technische Ausführung und Kontrolle bereit. Die weitergehende Vorstellung des Papers, eine „kognitive Identität“ der Person modellieren zu können, bleibt ein Forschungsanspruch. Für unsere Arbeitsdefinition genügt, dass der Agent autorisierte Ziele und Präferenzen verlässlich berücksichtigt.

# 3\. Prompt Engineering

## **3.1 Prompt und Prompt Engineering**

Ein Prompt ist mehr als eine Frage. Er ist die für einen Modellaufruf bereitgestellte Eingabesequenz. Sie kann eine Aufgabe, Ausgangsmaterialien, Kontextinformationen, Anforderungen, Einschränkungen, Beispiele, Verfahrenshinweise und Vorgaben für die erwartete Ausgabe enthalten.

Prompt Engineering bezeichnet die Entwicklung und Überarbeitung von Prompts anhand der Anforderungen und der beobachteten Ergebnisse. Inhalt und Struktur werden so angepasst, dass die Aufgabe verständlich, widerspruchsfrei und prüfbar ist (Schulhoff et al. 2024).

Folie mit konkurrierenden öffentlichen Vorstellungen von Prompt Engineering

**Abbildung 4: Konkurrierende Deutungen des Prompt Engineering.**

*Die Folie kontrastiert Prompting als vermeintliche Beschwörungskunst, als vermarktetes Versprechen perfekter Formeln und als Verstärkung vorhandener Expertise. Die Gegenüberstellung motiviert eine engere Arbeitsdefinition: Prompt Engineering gestaltet eine konkrete Eingabesequenz, ohne fehlendes Fachwissen oder Projektkontext ersetzen zu können.* (Schulhoff et al. 2024). Der Begriff ist bewusst enger als Context Engineering. Er richtet sich auf eine konkrete Eingabesequenz, nicht auf die gesamte Informationsumgebung einer längeren Arbeitstrajektorie.

Ein einfacher Prompt kann lauten:

*Transkribiere diese Seite.*

Eine begrenztere und prüfbarere Fassung wäre:

*Transkribiere die bereitgestellte Seite diplomatisch. Erhalte Zeilenumbrüche, markiere unleserliche Stellen als* *\[unleserlich\]**, normalisiere keine Schreibweisen und ergänze keine Wörter, die nicht sichtbar sind. Gib zuerst die Transkription und anschließend eine Liste unsicherer Lesungen mit Zeilenreferenz aus.*

Die zweite Fassung macht sichtbar, welche Eigenschaften des Ergebnisses erwartet werden. Sie garantiert noch keine korrekte Transkription, reduziert aber die Zahl stiller Annahmen.

## **3.2 Der Prompt als begrenzte Spezifikation**

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

### **Beispiel: TEI-Erzeugung**

Erzeuge für \\page-001.txt\\ eine TEI-Datei.

Verwende:

\\- \\knowledge/transcription-rules.md\\

\\- \\knowledge/tei-model.md\\

\\- \\knowledge/uncertainty.md\\

Anforderungen:

\\- Erhalte Seiten- und Zeilenwechsel.

\\- Verändere den Transkriptionstext nicht stillschweigend.

\\- Markiere unsichere Lesungen nach den dokumentierten Regeln.

\\- Verwende nur Elemente und Attribute, die im Projektmodell vorgesehen sind.

\\- Validere die Datei gegen \\schema/edition.rng\\.

Abschluss:

\\- Speichere die Datei unter \\tei/page-001.xml\\.

\\- Führe die Validierung aus.

\\- Berichte über verbleibende fachliche Unsicherheiten getrennt von technischen Fehlern.

Der Prompt enthält keine vollständige Erklärung der editorischen Regeln. Er verweist auf den persistenten Wissensbestand. Dadurch bleibt er kompakt und auf die aktuelle Aufgabe begrenzt.

### **Prompts für aktuelle Frontier-LLMs**

  - Prompts an die Fähigkeiten aktueller Frontier-LLMs anpassen.
  - Klare, widerspruchsfreie Aufgaben statt pauschaler Denkanweisungen formulieren.
  - Erfolgskriterien festlegen und die Wirkung des Prompts an den Ergebnissen prüfen.
  - Relevanten Kontext bereitstellen, Ergebnisse überprüfen lassen und kritische Perspektiven einholen.

Die zugespitzte Folienüberschrift „Prompt Engineering ist so 2025\!“ richtet sich gegen die unveränderte Übernahme älterer Promptrezepte. Für eine konkrete Aufgabe wird geprüft, welche Anweisungen und Beispiele helfen. Der gewünschte Prozess lässt sich durch Rückfragen, Quellenvorgaben, Freigaben und überprüfbare Ausgaben steuern.

Beim Rechercheprompt des Workshops lassen sich fünf Funktionen unterscheiden. Das Ziel ist eine organisationsbezogene Wissensbasis. Zielgruppe und Stil bestimmen die verständliche, kompakte Antwort. Rückfragen bauen Kontext auf. Planung und ausdrückliches OK steuern den Ablauf. Quellenjahr, Ablage und Fundstellen legen Vorgaben und Nachweise fest.

## **3.3 Rollen- und Persona-Prompting**

Eine verbreitete Form des Promptings weist dem Modell eine Rolle zu:

*Du bist eine erfahrene Editionswissenschaftlerin.*

Eine solche Formulierung kann Terminologie, Stil, Perspektive und Detaillierungsgrad beeinflussen. Sie fügt dem Modell jedoch kein neues Fachwissen hinzu. Die Rolle kann höchstens gelernte Muster fachsprachlicher Kommunikation wahrscheinlicher machen.

**Role Prompting** bezeichnet eine knappe funktionale Zuweisung. **Persona Prompting** beschreibt eine ausgearbeitete Perspektive mit Hintergrund, Erfahrung, Zielen, Einschränkungen und Nutzungssituation. Beide sollten gemeinsam betrachtet, aber nicht gleichgesetzt werden.

Beispiel einer Persona:

Du repräsentierst eine Teilnehmerin des Workshops.

Hintergrund:

\\- Literaturwissenschaftlerin

\\- Erfahrung mit digitalen Editionen

\\- regelmäßige Arbeit mit Word und Excel

\\- keine Erfahrung mit Terminal, Git oder VS Code

\\- grundsätzlich interessiert, aber vorsichtig bei Installationen

\\- arbeitet mit Windows

Prüfe die folgende Anleitung aus dieser Perspektive.

Identifiziere:

1\\. unklare Begriffe,

2\\. fehlende Zwischenschritte,

3\\. stillschweigend vorausgesetztes Wissen,

4\\. Stellen, an denen du wahrscheinlich Unterstützung benötigst.

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

## **3.4 Iteration, Self-Revision und strukturierte Ausgaben**

Prompts entstehen häufig nicht in einem Schritt. Eine produktive Interaktion kann aus mehreren begrenzten Durchgängen bestehen:

*erzeugen → prüfen → korrigieren → verdichten*

Ein erster Prompt kann einen Entwurf erzeugen. Ein zweiter fordert eine kriteriengeleitete Prüfung. Ein dritter überarbeitet nur die tatsächlich identifizierten Probleme.

Beispiel:

Prüfe die TEI-Datei auf:

1\\. Abweichungen von \\transcription-rules.md\\,

2\\. unzulässige oder nicht definierte Elemente,

3\\. stillschweigende Normalisierungen,

4\\. unmarkierte Unsicherheiten.

Liste zuerst die Befunde mit Zeilenreferenz.

Verändere die Datei noch nicht.

Danach:

Überarbeite ausschließlich die bestätigten Befunde.

Bewahre alle nicht betroffenen Strukturen.

Führe anschließend die Schema-Validierung erneut aus.

Diese Form der **Self-Revision** kann Fehler sichtbar machen, ist aber keine unabhängige Verifikation. Dasselbe Modell kann seine eigenen Fehlannahmen übersehen oder nachträglich plausibel begründen. Self-Revision wird verlässlicher, wenn explizite Kriterien, externe Tests und überprüfbare Referenzen vorliegen.

Kontext lässt sich durch Rückfragen, bereitgestellte Dokumente, Beispiele, Dateisuche oder die Auswertung bisheriger Ergebnisse aufbauen. Kritische Perspektiven können Annahmen und Gegenargumente sichtbar machen. Eine Aufforderung zur Selbstprüfung liefert mögliche Befunde, deren Tragfähigkeit am Material geprüft werden muss. Diese Verfahren werden nach ihrem Beitrag zur Aufgabe eingesetzt.

Strukturierte Ausgabeformate reduzieren Mehrdeutigkeit. Ein Prompt kann eine Markdown-Tabelle, JSON, XML oder eine definierte Dateistruktur verlangen. Dabei sind unterschiedliche Ebenen zu unterscheiden:

  - syntaktische Konformität,
  - strukturelle Vollständigkeit,
  - semantische Richtigkeit,
  - wissenschaftliche Angemessenheit.

Gültiges JSON beweist nur, dass die Syntax stimmt. Schema-valide TEI beweist nur, dass die formalen Regeln eingehalten wurden. Ob die Quelle angemessen repräsentiert ist, bleibt eine fachliche Frage.

## **3.5 Warum Promptwirkungen schwer zu evaluieren sind**

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

  - Ziel und Metrik festlegen.
  - Eine Baseline definieren.
  - Möglichst nur einen relevanten Bestandteil verändern.
  - Mehrere Beispiele und Wiederholungen verwenden.
  - Auf neuen Fällen prüfen.
  - Modell und Version dokumentieren.
  - Fachliche Qualität getrennt von Stil und Format bewerten.

## **3.6 Mechanistische Perspektive**

Sprachliche Eingaben werden in hochdimensionale numerische Repräsentationen überführt. Unterschiedliche Formulierungen verändern die internen Aktivierungen, aus denen die Wahrscheinlichkeitsverteilung möglicher Ausgaben entsteht. Semantische und funktionale Beziehungen können sich in diesen Repräsentationen widerspiegeln.

Der Ausdruck Latent Program Space dient hier als Metapher für gelernte Verarbeitungsroutinen.

Didaktisches Modell von Prompt, Aktivierungspfad und Latent Program Space

**Abbildung 7: Didaktisches Modell der Promptwirkung.**

*Die Darstellung veranschaulicht, dass eine Eingabe interne Repräsentationen und Verarbeitungspfade beeinflusst. Der Ausdruck „Latent Program Space“ bezeichnet hier keine klar abgegrenzte Sammlung klassischer Programme. Übersetzen, Zusammenfassen, Klassifizieren oder Erklären sind wiederkehrende Verhaltensmuster, die aus den Gewichten des LLM und dem aktuellen Verarbeitungsverlauf entstehen.*

Mechanistische Interpretierbarkeitsverfahren versuchen, Teile solcher internen Berechnungen zu rekonstruieren.

Folie mit Attribution Graph und Steuerung interner Aktivierungsrichtungen

**Abbildung 8: Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung.**

*Links wird ein Attribution Graph als partielle Rekonstruktion einer internen Berechnung gezeigt. Rechts verändert die Verstärkung bestimmter Aktivierungsrichtungen das beobachtete Verhalten. Die Beispiele stützen die Annahme systematischer interner Verarbeitung, liefern aber keine vollständige Erklärung natürlicher Promptwirkungen.* Attribution Graphs und verwandte Verfahren zeigen, dass bestimmte interne Strukturen und Aktivierungsrichtungen mit beobachtbarem Verhalten zusammenhängen können (Lindsey et al. 2025). Diese Befunde machen plausibel, dass unterschiedliche Prompts unterschiedliche Verarbeitungsverläufe begünstigen. Sie liefern jedoch noch keine vollständige Theorie, mit der sich natürliche Promptwirkungen zuverlässig vorhersagen lassen.

## **3.7 Grenzen des Prompt Engineering**

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

## **3.8 Hands-on 1: Webrecherche und Wissensdokumente**

### **Arbeitsauftrag**

Legen Sie einen neuen, leeren Ordner an, etwa wissensbasis. Starten Sie darin eine Session mit Zugriff auf diesen Ordner. Übernehmen Sie den folgenden Prompt. Beantworten Sie die Rückfragen mit Blick auf Ihre eigene Arbeit und prüfen Sie den Recherchevorschlag, bevor Sie ihn freigeben.

Ich möchte eine Wissensbasis zu „Agentic Engineering und Governance“ aufbauen, zugeschnitten auf meine Arbeit und meine Organisation. Wir sind in einem Live-Workshop. Antworte kompakt, sachlich und ohne technische Vorkenntnisse verständlich.

1\. Stell mir drei Fragen zu meiner Rolle, meiner Organisation und dazu, wofür ich AI Agents einsetzen will.

2\. Beantworte mir dann die folgenden Fragen und warte auf mein OK:

Wie teilst du die Recherche auf 2 Subagents (Sonnet 5.5, max. 8 Quellen pro Agent) auf?

Mit welchen drei Kriterien prüfst du die Qualität einer Quelle, und welche Kategorien schlägst du vor?

Wie destillierst du das Wissen, und welche Dokumente entstehen in knowledge/?

3\. Nach meinem OK recherchierst du im Web. Dabei gilt:

Nur Quellen, die 2026 veröffentlicht wurden, Datum an der Quelle geprüft.

Je Quelle das Original in sources/ (PDF oder Webseite als Text), benannt nach Herausgeber, Datum und Kurztitel.

Das destillierte Wissen liegt als Markdown-Dokumente in knowledge/. Jede Aussage verweist auf ihre Datei in sources/ mit Fundstelle. Eine Quellenliste in knowledge/ nennt Titel, Herausgeber, Datum, Link und Kategorie.

Die Modellangabe und die Jahresgrenze sind Vorgaben dieses Workshop-Prompts. Prüfen Sie die Modellverfügbarkeit im verwendeten Harness. Fehlt das genannte Modell oder die Subagent-Funktion, muss die Durchführung angepasst werden. Das Quellenjahr beschränkt diese Übung, es ist kein allgemeines Qualitätskriterium für Forschungsliteratur.

Als Ausgangspunkt für die Qualitätsprüfung eignen sich die fachliche Zuständigkeit des Herausgebers, die Nachvollziehbarkeit von Methode und Belegen sowie die Relevanz für die Leitfrage. Als Kategorien kommen Forschungsbeitrag, technische Dokumentation und institutionelle Orientierung infrage. Veröffentlichungsdatum und Fassung werden zusätzlich erfasst. Rechtliche Fragen erfordern die jeweils einschlägigen Primärquellen.

### **Follow-up-Prompts**

Können wir noch etwas optimieren? Liste und begründe\! Definiere unser Ziel in einem Satz. Hast du noch konzeptuelle Fragen?

Übernimm die Verbesserungen und leg los\!

### **Ergebnis und Beobachtung**

Beobachten Sie die Rückfragen, die Verteilung der Recherche und die Tool-Aufrufe. Prüfen Sie beispielhaft, ob das Datum an der Quelle und die angegebene Fundstelle stimmen. Der Agent kann Hilfsdateien oder Prüfskripte ergänzen. Welche Dateien tatsächlich entstanden sind, wird am Projektordner geprüft.

### **Eigene Wissensbasis schärfen**

Nehmen Sie sich 5–10 Minuten Zeit und überlegen Sie zunächst selbst:

  - Bei welcher konkreten Aufgabe soll Ihnen die Wissensbasis helfen?
  - Welche eigenen Quellen oder Dokumente möchten Sie einbeziehen?
  - Welche Frage soll die Wissensbasis beantworten?
  - Woran würden Sie erkennen, dass die Antwort für Ihre Arbeit brauchbar ist?
  - Wie würden Sie diese Anforderungen Ihrem AI Agent mitteilen?

Kopieren Sie die Fragen mit Ihren Antworten in die laufende Konversation. Besprechen Sie offene Punkte und lassen Sie das Projektprofil in knowledge/project.md aktualisieren.

# 4\. Context Engineering

## **4.1 Kontext als Informationszustand einer Aufgabe**

Context Engineering stellt Anweisungen, relevantes Wissen, den Arbeitsstand und Ergebnisse aus Tool Use für den jeweiligen LLM-Aufruf zusammen und passt sie im Arbeitsverlauf an. Die Auswahl wird im Verlauf einer agentischen Aufgabe wiederholt überprüft (Anthropic 2025, Effective context engineering for AI agents).

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

## **4.2 Context Window und Context Rot**

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

Untersuchungen zu langen Kontexten zeigen, dass Position, Ablenkung und Umfang der bereitgestellten Information die Leistung beeinflussen können. Relevante Information kann in langen Eingaben schwerer auffindbar sein, insbesondere wenn sie zwischen ähnlichen oder widersprüchlichen Inhalten steht.\[4\]

Der Ausdruck **Context Rot** bezeichnet beobachtete Leistungsabfälle bei wachsender Kontextlänge. Er ist kein einzelner, abschließend geklärter technischer Mechanismus. Für agentische Arbeit ist der Begriff dennoch hilfreich: Während längerer Läufe sammeln sich Werkzeugausgaben, Fehlversuche, überholte Planungen und Zwischenstände an. Sie beanspruchen Tokens und können mit aktuell relevanter Information konkurrieren.

Daraus folgt nicht, dass Kontext immer möglichst kurz sein sollte. Zu starke Reduktion kann Bedingungen, Unsicherheiten und Provenienz entfernen. Die Zielgröße ist ein **dichter und hinreichender Kontext**: so begrenzt wie möglich, aber so vollständig und differenziert wie für die Aufgabe erforderlich.

Für ein vereinfachtes Context Window mit 8.000 Tokens passen 6.000 Input-Tokens und 1.500 Output-Tokens gemeinsam in das Budget. 10.000 Input-Tokens und 1.500 Output-Tokens überschreiten es. Reale Systeme haben zusätzliche Regeln für Ausgabegrenzen, Reasoning und Kontextverwaltung. Die maximale Ausgabe wird deshalb bei der Planung berücksichtigt.

## **4.3 Wie Informationen in den Modellkontext gelangen**

Eine Datei im Projektordner ist nicht automatisch Teil des Context Window. Damit ihr Inhalt für das Modell verfügbar wird, muss das System sie lesen, extrahieren, transformieren oder durch ein Werkzeug untersuchen.

Der Weg lässt sich schematisch darstellen:

***Datei oder Datenbestand → Werkzeug, Parser oder Skript → bereitgestellte Repräsentation → Tokenisierung → Context Window***

Unterschiedliche Formate erfordern unterschiedliche Zugriffe:

  - Markdown und Quellcode können meist direkt gelesen werden.
  - CSV-Dateien können selektiv profiliert oder abgefragt werden.
  - Word-Dateien müssen strukturiert ausgelesen werden.
  - PDFs können Text, Layout und Bilder kombinieren.
  - Bilder werden multimodal verarbeitet oder in strukturierte Beschreibungen überführt.
  - Datenbanken werden über Abfragen genutzt, ohne vollständig in den Kontext geladen zu werden.

Im Editionsprojekt kann der Agent ein Bild öffnen, ohne dessen Binärdaten als Tokens zu „lesen“. Ein multimodales System verarbeitet das Bild und erzeugt interne Repräsentationen. Ein Skript kann aus hundert TEI-Dateien nur jene Elemente zählen, die für eine aktuelle Modellierungsfrage relevant sind. In den Modellkontext gelangt dann die Ausgabe des Skripts, nicht zwingend der gesamte Datenbestand.

Die methodisch relevante Einheit ist daher nicht die Datei als solche, sondern ihre **für das Modell bereitgestellte Repräsentation**.

## **4.4 Context Compression und Distillation**

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

  - **Auswahl:** Was ist für den Gegenstand relevant?
  - **Strukturierung:** Welche Begriffe, Regeln und Beziehungen müssen explizit werden?
  - **Verdichtung:** Welche Redundanz kann entfernt werden, ohne notwendige Differenzierungen zu verlieren?

Das Gegenrisiko ist **Überdestillation**. Sie liegt vor, wenn Provenienz, Unsicherheiten oder handlungsnotwendige Details verloren gehen.

### **Context Management im Workshop**

/context

In Claude Code zeigt /context die Belegung und die Bestandteile des Context Window. Damit lässt sich prüfen, wie viel Platz unter anderem Verlauf, Dateien und Werkzeugdefinitionen beanspruchen.

/compact

Mit /compact lässt sich der Verlauf kompaktieren. Eine Zusammenfassung tritt an die Stelle großer Teile des bisherigen Gesprächs. Dauerhafte Projektanweisungen werden wieder bereitgestellt. Details aus früheren Nachrichten können verloren gehen. Benötigte Dateien werden bei Bedarf erneut gelesen. Der genaue Ablauf hängt von der Produktversion ab (Anthropic, How Claude Code works und How Claude remembers your project).

Halten Sie die Leitfrage, bestätigte Entscheidungen und den Arbeitsstand in Projektdateien fest. Prüfen Sie nach einer Kompaktierung, ob die Aufgabe und ihre Grenzen erhalten geblieben sind. Dieselbe Konversation kann fortgesetzt werden, ohne dass ihr vollständiger Wortlaut ständig im aktiven Kontext liegt.

## **4.5 Project Knowledge Base, Working Context und Context Window**

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

*Knowledge Engineering baut und pflegt den Wissensbestand; Context Engineering stellt daraus und aus weiteren Ressourcen den für eine konkrete Aufgabe erforderlichen Kontext zusammen.*

## **4.6 Ergänzende Übung: Working Context für eine TEI-Aufgabe**

### **Aufgabe**

Wählen Sie aus einem bereitgestellten Projektbestand jene Ressourcen aus, die ein Agent benötigt, um eine Seite korrekt als TEI zu modellieren.

### **Kategorien**

Ordnen Sie jede Ressource einer Kategorie zu:

  - unmittelbar laden,
  - bei Bedarf nachladen,
  - nur über ein Werkzeug abfragen,
  - für diese Aufgabe nicht verwenden.

### **Beispielmatrix**

|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*Ressource\*\* | \*\*Unmittelbar\*\* | \*\*Bei Bedarf\*\* | \*\*Tool-Zugriff\*\* | \*\*Nicht verwenden\*\* | \*\*Begründung\*\* |
| page-017.jpg | Yes |   |   |   | Primärquelle |
| transcription-rules.md | Yes |   |   |   | verbindliche Regeln |
| vollständiges Projektprotokoll |   |   |   | Yes | zu breit und teilweise überholt |
| edition.rng |   |   | Yes |   | durch Validator verwenden |
| zwei geprüfte TEI-Beispiele | Yes |   |   |   | konkretisieren Grenzfälle |
| alte Schema-Version |   |   |   | Yes | nicht maßgeblich |

### **Reflexion**

  - Welche Ressource ist wichtig, muss aber nicht vollständig in den Kontext?
  - Welche Information fehlt im Bestand?
  - Welche Auswahlentscheidung ist fachlich und nicht nur technisch?

# 5\. Knowledge Engineering

## **5.1 Warum Projektwissen explizit werden muss**

In einem Editionsprojekt ist Wissen häufig verteilt. Ein Teil steht in Richtlinien, ein Teil in E-Mails, ein Teil in TEI-Beispielen und ein Teil nur im Erfahrungswissen einzelner Editor:innen. Menschen, die lange am Projekt arbeiten, ergänzen fehlende Zusammenhänge oft unbewusst. Eine neue Person oder eine neue Agenteninstanz besitzt diesen Hintergrund nicht.

Ein Agent kann zwar alle Dateien durchsuchen, aber daraus entsteht nicht automatisch ein konsistentes Projektverständnis. Er kann eine alte Regel mit einer neuen vermischen oder aus einem einzelnen Beispiel eine allgemeine Konvention ableiten.

**Knowledge Engineering** betrifft den Aufbau und die Pflege expliziten, inspizierbaren und revidierbaren Projektwissens. Es macht relevante Begriffe, Regeln, Entscheidungen, Einschränkungen und Unsicherheiten so sichtbar, dass sie gelesen, kritisiert und fortgeschrieben werden können.

Ziel ist keine vollständige Repräsentation aller verfügbaren Informationen. Eine Wissensbasis ist zweckgebunden. Sie hält jenen Teil des Wissens fest, der für bestimmte Formen der Arbeit, Entscheidung und Prüfung erforderlich ist.

## **5.2 Knowledge Acquisition**

Projektwissen stammt aus zwei grundlegenden Quellen:

  - bereits vorhandenen Dokumenten und Daten;
  - implizitem Wissen von Personen und Organisationen.

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

Im Editionsprojekt könnte ein Interview ergeben, dass \<supplied\> nur verwendet werden darf, wenn eine Ergänzung mit hoher Sicherheit aus dem unmittelbaren Kontext erschlossen werden kann. Diese Regel steht vielleicht nicht in der alten Richtlinie, wird aber seit Jahren praktiziert. Knowledge Acquisition macht sie sichtbar; Distillation überführt sie anschließend in eine überprüfbare Form.

## **5.3 Project Knowledge Base**

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

Im Governance-Beispiel enthält sources/ die erhaltenen Originalquellen. knowledge/ enthält das Projektprofil, Quellenverzeichnis und die daraus destillierten Wissensdokumente. scripts/ kann vom Agenten erzeugte Prüf- oder Verarbeitungsskripte aufnehmen. Eine Quellenliste dokumentiert Titel, Herausgeber, Datum, Link und Kategorie. Jede belegpflichtige Aussage nennt außerdem die relevante Fundstelle.

Die Wissensbasis ersetzt Quellen und Forschungsdaten nicht. Sie beschreibt und kontextualisiert deren Verwendung. source-description.md ist nicht die Quelle. tei-model.md ist nicht die TEI-Datei. Beide dokumentieren jedoch, wie mit den Quellen und Daten gearbeitet werden soll.

## **5.4 Wissensdokumente**

Ein Editionsprojekt kann seine Regeln in einer langen Richtlinie, mehreren E-Mails und mündlich weitergegebenem Erfahrungswissen verteilen. Für eine konkrete Aufgabe ist ein solcher Bestand schwer nutzbar. Ein Agent müsste die relevanten Aussagen jedes Mal neu suchen und könnte widersprüchliche Fassungen miteinander vermischen.

Ein Wissensdokument führt die für einen abgegrenzten Gegenstand relevanten Aussagen in einer überprüfbaren Form zusammen. Es kann beispielsweise festhalten, wie unsichere Lesungen markiert werden, welche Ausnahmen gelten und wie diese Unsicherheit im Frontend sichtbar werden soll.

Ein Wissensdokument ist strukturiertes, externalisiertes Wissen, destilliert aus Quellen, Daten oder Erfahrung zur Wiederverwendung durch Menschen und AI Agents. Es macht relevante Aussagen und ihre Herkunft prüfbar. Die Bezeichnung allein sagt noch nichts darüber aus, ob sein Inhalt bereits überprüft wurde.

Wissensdokumente sollen folgende Eigenschaften besitzen.

  - Für Menschen und KI lesbar, mit einer nachvollziehbaren Struktur und geklärten Begriffen.
  - Kompakt, unter Erhalt relevanter Begründungen, Ausnahmen und Unsicherheiten.
  - Übertragbar, im Workshop durch textbasiertes Markdown.
  - Kuratierbar, also prüfbar, korrigierbar und erweiterbar.

Quellenverweise mit Fundstellen verbinden die destillierten Aussagen mit den Originalen. Erfahrung und organisatorische Entscheidungen werden als solche kenntlich gemacht.

Beispiel:

\\---

document\_type: knowledge

status: reviewed

topic: uncertain readings

sources:

\\- editorial-guidelines-v2.pdf

\\- workshop-2026-04-12.md

\\---

\\\<a id="unsichere-lesungen"\\\>\\\</a\\\>

\# Unsichere Lesungen

\\\<a id="grundregel"\\\>\\\</a\\\>

\#\# Grundregel

Eine lesbare, aber nicht sicher identifizierbare Zeichenfolge wird mit

\\\\\<unclear\\\>\\ ausgezeichnet.

\\\<a id="unleserliche-stellen"\\\>\\\</a\\\>

\#\# Unleserliche Stellen

Ist keine belastbare Zeichenfolge erkennbar, wird keine hypothetische

Lesung als regulärer Text eingetragen.

\\\<a id="erganzungen"\\\>\\\</a\\\>

\#\# Ergänzungen

\\\\\<supplied\\\>\\ wird nur verwendet, wenn eine Ergänzung durch den unmittelbaren

Kontext begründet ist. Die Begründung muss nachvollziehbar bleiben.

\\\<a id="darstellung-im-frontend"\\\>\\\</a\\\>

\#\# Darstellung im Frontend

Unsichere Lesungen werden visuell markiert. Die Benutzeroberfläche darf

sie nicht wie sicheren Text darstellen.

\\\<a id="offene-frage"\\\>\\\</a\\\>

\#\# Offene Frage

Für teilweise lesbare Eigennamen ist noch zu klären, ob Zeichen- oder

Wortebene ausgezeichnet wird.

## **5.5 Markdown als technische Repräsentation**

Das Wissensdokument ist ein konzeptionelles Artefakt und nicht an ein bestimmtes Dateiformat gebunden. Im hier beschriebenen Workflow wird Markdown verwendet, weil es offen, textbasiert und sowohl für Menschen als auch für LLM-basierte Systeme gut lesbar ist.

Markdown trennt Struktur und Inhalt durch einfache Zeichen:

  - \# für Überschriften,
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

### **Markdown, Word und PDF**

Markdown stellt Dokumentstruktur in Klartext dar. Überschriften, Listen und Verweise benötigen wenig zusätzliche Syntax. Ein Markdown-Text ist bei vergleichbarem Inhalt meist kompakter als das vollständige XML einer Word-Datei. Wie viele Tokens benötigt werden, hängt von der konkreten Repräsentation und dem Tokenizer ab.

Word- und Excel-Dateien in den Formaten DOCX und XLSX enthalten strukturierte Daten in einem Dateicontainer. Zum Lesen werden Text, Tabellen oder andere benötigte Bestandteile extrahiert. PDFs beschreiben vor allem die Seitendarstellung. Lesereihenfolge, Tabellenstruktur und Text aus Scans müssen gegebenenfalls rekonstruiert werden. Extraktionsergebnisse werden deshalb am Original geprüft.

Inhaltlich arbeiten wir im Workshop in Markdown. PDF und Word dienen bei Bedarf als Ausgabeformate. Der Agent kann sie mit Code erzeugen, was zusätzliche Ausführungs- und Prüfschritte erfordert. Ein gut gestaltetes PDF macht seine Aussagen nicht verlässlicher als die zugrunde liegenden Wissensdokumente.

## **5.6 Instruktionsdateien und Agent Skills**

Ein Wissensdokument beschreibt einen Gegenstand. Eine Instruktionsdatei enthält dauerhafte Anweisungen für die Arbeit des Agents. Ein Prompt formuliert den aktuellen Auftrag. Ein Skill bündelt ein wiederverwendbares Verfahren und gegebenenfalls Skripte oder Ressourcen.

### **AGENTS.md und CLAUDE.md**

Diese Markdown-Dateien können Projektzweck, Arbeitsregeln und Verweise auf relevantes Wissen festhalten. Welche Datei ein Harness automatisch lädt und welche Geltungsbereiche er unterstützt, ist produktabhängig. In Claude Code können Anweisungen unter anderem global in \~/.claude/CLAUDE.md oder projektbezogen in einer CLAUDE.md liegen. Die dokumentierten Regeln bestimmen, wann Dateien geladen werden (Anthropic, How Claude remembers your project).

### **Beispiel globaler Anweisungen**

\# Arbeitsweise

\- Antworte kompakt und sachlich.

\- Frag nach, bevor du Dateien löschst.

\- Übertrage personenbezogene Daten nur nach ausdrücklicher Freigabe an einen dafür freigegebenen Dienst.

\- Zitiere nur, was du gelesen hast.

### **Beispiel projektbezogener Anweisungen**

\#\# Projekt

Wissensbasis zu Agentic Engineering und Governance für meine Organisation.

  

\#\# Regeln

\- Für diese Recherche nur Quellen aus 2026 verwenden.

\- Originalquellen in sources/ ablegen und unverändert erhalten.

\- Destilliertes Wissen in knowledge/ mit Fundstellen dokumentieren.

\- knowledge/ wird nicht veröffentlicht.

Die Jahresgrenze und das Veröffentlichungsverbot sind Projektentscheidungen dieses Beispiels. Die Datenregel muss an die tatsächlich geltenden Vorgaben der Organisation angepasst werden.

/init

In Claude Code kann /init den Projektbestand untersuchen und einen Ausgangspunkt für die CLAUDE.md erzeugen beziehungsweise Verbesserungen vorschlagen. Prüfen Sie den Entwurf auf zutreffende Angaben und ergänzen Sie Regeln, die sich aus den Dateien nicht erschließen lassen.

Instruktionsdateien beeinflussen das Verhalten des LLM. Technische Zugriffsbeschränkungen werden über Berechtigungen, passende Hooks oder Isolation durchgesetzt. Eine Regel in CLAUDE.md ersetzt diese Kontrollen nicht.

### **Agent Skills**

Ein Skill beschreibt ein wiederkehrendes Verfahren. Die Arbeit mit Skills wird im weiteren Workshop praktisch vertieft. Für die bisherigen Übungen genügt die Unterscheidung zwischen aktuellem Prompt, dauerhaftem Projektwissen und wiederkehrenden Arbeitsanweisungen.

## **5.7 Governance und Kuration**

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

## **5.8 Hands-on 2: Wissen in Wissensdokumente destillieren**

Arbeiten Sie mit der angelegten Wissensbasis in derselben Konversation weiter. Die Quellen liegen in sources/, das eigene Profil und die gewählte Leitfrage werden in knowledge/project.md festgehalten.

### **Prompt**

Schlag mir aus meinen Antworten drei Leitfragen vor. Halte meine Wahl und mein Profil in knowledge/project.md fest.

Destilliere mit Subagents (Sonnet 5.5) das für die Leitfrage relevante Wissen aus jeder Quelle in sources/ in je eine Markdown-Datei, mit Quellenverweis und Seitenangabe beziehungsweise Abschnitt. Die Originalquellen bleiben unverändert.

Schlage vor, wie du knowledge/ daraus überarbeitest. Warte vor der Umsetzung auf mein OK.

Je Quelle entsteht zunächst ein nachvollziehbares Destillat. Benennen Sie im Gespräch den Ablageort, falls der Agent ihn nicht eindeutig festlegt. Daraus werden die thematischen Wissensdokumente überarbeitet. Quellenbezogene Zusammenfassung und thematische Zusammenführung erfüllen unterschiedliche Aufgaben, ihre Herkunft muss nachvollziehbar bleiben.

### **Beispiel für knowledge/project.md**

\# Projekt

Wissensbasis zu Agentic Engineering und Governance für meine Organisation.

  

\#\# Leitfrage

Welche Regeln brauchen wir, bevor AI Agents mit internen Daten arbeiten?

### **Follow-up-Prompt**

Ist alles korrekt? Gibt es Redundanzen? Geht es kompakter, ohne Informationsverlust? Liste und begründe\! Setze dann alles um\!

Die Formulierung verbindet die Benennung möglicher Probleme mit ihrer Überarbeitung. Soll vor Änderungen eine Prüfung durch Sie erfolgen, geben Sie zunächst nur die Liste in Auftrag und lassen Sie die Umsetzung anschließend freigeben. Prüfen Sie exemplarisch, ob Seitenangaben, Ausnahmen und offene Fragen erhalten sind. Eine LLM-Selbstprüfung genügt für den Nachweis der Richtigkeit nicht.

Rufen Sie /context auf und prüfen Sie die Belegung. Halten Sie den bestätigten Stand in den Dateien fest, bevor Sie bei Bedarf /compact verwenden.

# 6\. Agentic Engineering

## **6.1 Warum mehrschrittige Arbeit organisiert werden muss**

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

## **6.2 Agentische Ausführungsschleife**

Eine vereinfachte Ausführungsschleife lautet:

**Abbildung 10: Agentische Ausführungsschleife.**

*Der Agent erfasst den aktuellen Projektzustand, plant einen begrenzten nächsten Schritt, verwendet ein Werkzeug, beobachtet dessen Ergebnis und aktualisiert sein Vorgehen. Der Zyklus bleibt an dokumentierte Anforderungen, Berechtigungen, Abbruchbedingungen und menschliche Interventionspunkte gebunden.*

***Zustand erfassen → nächsten Schritt planen → Werkzeug oder Aktion ausführen → Ergebnis beobachten → Vorgehen aktualisieren***

Im Editionsprojekt:

  - Agent liest Aufgabe und relevante Wissensdokumente.
  - Agent untersucht die vorhandene Transkription.
  - Agent erzeugt TEI.
  - Agent führt Schema-Validierung aus.
  - Agent liest Fehlermeldungen.
  - Agent korrigiert technische Fehler.
  - Agent dokumentiert verbleibende fachliche Unsicherheiten.
  - Agent transformiert TEI in HTML.
  - Agent prüft die Darstellung.
  - Agent schlägt Write-back vor.

Autonomie bezeichnet dabei den Umfang der Arbeit zwischen zwei menschlichen Eingriffen. Sie bedeutet nicht Abwesenheit menschlicher Kontrolle.

## **6.3 Planung, Ausführung und Feedback**

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

## **6.4 Werkzeuge, Berechtigungen und Reversibilität**

Der Permission Mode legt fest, welche Aktionen ein AI Agent ohne Ihre Freigabe ausführen darf. Systemzugriff und Freigaben werden getrennt betrachtet. Der Agent kann weitreichende Leserechte besitzen, auch wenn er vor Änderungen nachfragt.

### **Permission Modes in Claude Code**

### **Plan**

Erkundet das Projekt und plant die Umsetzung, bevor Änderungen erfolgen.

### **Manual**

Fragt vor Aktionen, die noch nicht freigegeben sind.

### **Accept edits**

Erlaubt Dateiänderungen und bestimmte Dateisystembefehle ohne Rückfrage.

### **Auto**

Genehmigt viele Aktionen automatisch. Ein Klassifikator prüft weitere Aktionen und kann sie blockieren. Seine Prüfung kann Fehler übersehen.

### **Bypass**

Überspringt die meisten Freigabeprüfungen. Nur in einer isolierten Umgebung verwenden. Der Modus setzt nicht sämtliche Schutzmechanismen außer Kraft.

Die Bezeichnungen und Einzelheiten sind produktabhängig. Diese Kurzfassungen orientieren sich an Anthropic, Choose a permission mode. Weniger manuelle Freigaben bedeuten weder bessere Ergebnisse noch eine umfassendere Isolation.

### **Deny-Regeln, Hooks und Sandbox**

Deny-Regeln und geeignete Hooks können bestimmte Aktionen unabhängig vom gewählten Modus blockieren. Ein Hook ist ein Programm, das der Harness bei einem festgelegten Ereignis ausführt. Seine Schutzwirkung hängt davon ab, welche Werkzeuge und Ausführungswege er tatsächlich erfasst.

Eine Sandbox begrenzt die Datei- und Netzwerkzugriffe von Shell-Befehlen. Die eingebaute Sandbox von Claude Code läuft unter macOS, Linux und WSL2, unter nativem Windows ist sie nicht verfügbar. Dateiwerkzeuge, MCP-Server und Hooks liegen außerhalb dieser Shell-Sandbox (Anthropic, Configure the sandboxed Bash tool).

Begrenzen Sie Zugriffe auf die für den Auftrag erforderlichen Ressourcen. Bereiten Sie die Rücknahme relevanter Änderungen vor. Versionierung hilft bei erfassten Dateiständen, sie macht bereits versandte Informationen oder externe Aktionen nicht rückgängig.

## **6.5 MCP, Subagents und Agent-to-Agent-Kommunikation**

Das **Model Context Protocol (MCP)** standardisiert die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Ein MCP-Server kann beispielsweise Zugriff auf ein Repository, eine Datenbank oder einen Validator bereitstellen.\[5\]

Ein Konnektor ist eine Anbindung an einen Dienst oder Datenbestand. Ein Plugin erweitert einen Harness um gebündelte Funktionen, etwa Werkzeuge oder Arbeitsanweisungen. MCP, Konnektor und Plugin bezeichnen unterschiedliche Aspekte solcher Erweiterungen. Die konkrete Benennung und der Funktionsumfang hängen vom Produkt ab.

MCP löst ein technisches Integrationsproblem. Es entscheidet nicht, ob ein Werkzeug für die Aufgabe geeignet ist oder wie seine Ergebnisse fachlich interpretiert werden.

Ein Subagent ist ein AI Agent, dem ein anderer Agent eine abgegrenzte Aufgabe überträgt. Er arbeitet in einem eigenen Context Window und gibt sein Ergebnis an den beauftragenden Agenten zurück.

  - Kontext gezielt mitgeben, etwa Auftrag, Quellen und Prüfkriterien.
  - Recherche, Analyse oder Review auslagern und den Hauptverlauf entlasten.
  - Abgrenzbare Teilaufgaben bei Bedarf parallel bearbeiten lassen.
  - Anweisungen, Werkzeuge und LLM auf die Aufgabe abstimmen.
  - Ergebnisse zusammenführen und am Material prüfen.

Subagents eignen sich besonders für umfangreiche, klar abgrenzbare Teilaufgaben. Bei Kleinigkeiten oder eng voneinander abhängigen Schritten kann der Aufwand für Übergabe und Zusammenführung den Nutzen überwiegen.

Welche Anweisungen oder Verlaufsanteile ein Subagent übernimmt, hängt vom Harness und seiner Konfiguration ab. Ein eigener Kontext bedeutet nicht zwingend, dass überhaupt kein bisheriger Kontext übernommen wird. Claude Code unterscheidet beispielsweise frische Subagents und Forks der Konversation (Anthropic, Create custom subagents).

### **LLM-as-a-Judge**

Bei LLM-as-a-Judge beurteilt ein LLM ein Ergebnis anhand vorgegebener Kriterien. Ein Subagent kann diese Rolle übernehmen, etwa beim Abgleich eines Governance-Entwurfs mit Quellen. Ein eigener Kontext reduziert die Übernahme bisheriger Gesprächsannahmen, begründet aber keine verlässliche Unabhängigkeit oder Richtigkeit.

Lass einen Subagenten den Governance-Entwurf mit den Quellen in sources/ abgleichen. Er soll unbelegte oder widersprüchliche Aussagen mit Fundstelle im Entwurf und Begründung auflisten. Den Entwurf soll er nicht verändern.

Ein Review-Auftrag sollte die zu prüfende Fassung, den Quellenbestand, die Kriterien und das Rückgabeformat nennen. Die Befunde werden anschließend anhand des Entwurfs und der Quellen nachgeprüft.

Agent-to-Agent-Protokolle verbinden eigenständige Agents. Die methodischen Fragen bleiben:

  - Welche Zuständigkeit besitzt jeder Agent?
  - Welche Informationen werden übergeben?
  - Wie werden Konflikte sichtbar?
  - Wer entscheidet bei widersprüchlichen Ergebnissen?

## **6.6 Versionierte Zwischenstände und menschliche Intervention**

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

## **6.7 Ergänzende Übung: TEI erzeugen und ein Frontend implementieren**

### **Teil A: TEI erzeugen**

Der Agent erhält:

  - Seitenbild,
  - Rohtranskription,
  - Wissensdokumente,
  - Schema,
  - zwei geprüfte Beispiele.

Auftrag:

  - TEI erzeugen,
  - Schema validieren,
  - technische Fehler korrigieren,
  - fachliche Unsicherheiten separat dokumentieren.

### **Teil B: Frontend implementieren**

Das lokale Frontend soll zeigen:

  - Faksimile,
  - diplomatische Transkription,
  - normalisierte Ansicht,
  - Unsicherheiten,
  - Annotationen.

### **Teil C: Rückkopplung prüfen**

Fragen:

  - Sind Seiten- und Zeilenwechsel sichtbar?
  - Werden Unsicherheiten als Unsicherheiten dargestellt?
  - Erzeugt die Oberfläche falsche Eindeutigkeit?
  - Welche Modellierungsprobleme werden erst im Interface sichtbar?
  - Welche Wissensdokumente müssen revidiert werden?

## **6.8 KI-Governance**

KI-Governance legt fest, wer über den Einsatz von KI entscheidet, welche Regeln gelten und wie ihre Einhaltung überprüft wird. Dazu gehören Zuständigkeiten, nachvollziehbare Entscheidungen und Verfahren für Kontrolle und den Umgang mit Problemen (IEEE Standards Association 2026).

Die Governance-Fragen des Workshops betrachten sowohl Daten als auch den Agenten. Die Gegenüberstellung dient als eigene didaktische Struktur für die Fallarbeit.

### **Sichtbarkeit**

Wo liegen sensible Daten und wohin werden sie übertragen? Welche Tools, Konnektoren und LLMs nutzt der Agent? Ein lokales Programm kann Inhalte an einen externen Dienst senden.

### **Einstufung und Vertrauen**

Wie sensibel sind die verwendeten Daten? Welche Inhalte und Erweiterungen sind vertrauenswürdig? Ein gelesener Inhalt kann Anweisungen enthalten, die dem eigentlichen Auftrag widersprechen. Herkunft und erlaubte Verwendung werden deshalb geprüft.

### **Rechtsraum**

Wo werden die Daten verarbeitet und welcher rechtliche sowie vertragliche Rahmen gilt? Wo laufen Agent und LLM, wer betreibt sie? Die Antworten werden für das tatsächlich verwendete Angebot und die konkrete Organisation ermittelt.

### **Zugriff**

Wer darf auf welche Daten zugreifen? Welche Aktionen darf der Agent ohne Freigabe ausführen? Lesezugriff, Schreibzugriff und externe Aktionen werden getrennt betrachtet.

### **Nachweis**

Sind Datenübertragungen, Tool-Aufrufe, Freigaben und Ergebnisse dokumentiert? Ein Protokoll muss erkennen lassen, was tatsächlich ausgeführt wurde. Welche Inhalte protokolliert und wie lange sie aufbewahrt werden, wird für den Anwendungsfall festgelegt.

Ein Governance-Entwurf aus einer Wissensbasis hält Vorschläge und offene Fragen fest. Die organisatorische Entscheidung über geltende Regeln wird dadurch vorbereitet. Fehlende Rechts- oder Organisationskenntnis muss sichtbar bleiben.

## **6.9 Hands-on 3: Governance für den eigenen Anwendungsfall entwickeln**

Beschreiben Sie einen Fall aus Ihrer Arbeit. Welche Aufgabe soll ein AI Agent übernehmen, mit welchen Daten soll er arbeiten und in welchem System soll er eingesetzt werden? Bleiben Sie in der laufenden Konversation.

### **Prompt**

Unser Fall: {{Ihre Fallbeschreibung}}

  

Welche Governance-Regeln brauchen wir für diesen Einsatz? Stell mir vorher bis zu drei Rückfragen, falls wichtige Angaben fehlen.

  

Antworte nur aus knowledge/ und sources/. Belege deine Aussagen mit Datei und Fundstelle. Benenne offene Fragen. Schlage bei Wissenslücken eine gezielte Webrecherche mit Subagents vor und warte auf mein OK. Neue Quellen werden wie bisher abgelegt und in die Wissensdokumente eingearbeitet.

  

Halte das Ergebnis in knowledge/governance-entwurf.md fest.

Beobachten Sie, wie der Agent relevante Inhalte findet. Dafür kann er Dateinamen durchsuchen, Volltextsuche oder reguläre Ausdrücke verwenden, also Suchmuster für Text. Ein sprechender Dateiname erleichtert die Orientierung. Welche Aussagen er findet, hängt zusätzlich vom Dateiinhalt und der Suchstrategie ab.

Prüfen Sie beispielhaft, ob die Aussagen durch die genannten Fundstellen gedeckt sind. Unterscheiden Sie Quellenbefunde, eigene organisatorische Festlegungen und offene Fragen. Der Entwurf bleibt zunächst in Markdown.

### **Follow-up-Prompt**

Erzeuge aus knowledge/governance-entwurf.md ein übersichtliches PDF mit Quellenverweisen und offenen Fragen.

Kontrollieren Sie im PDF die Lesbarkeit, Quellenverweise und offenen Fragen. Die inhaltliche Grundlage bleibt die Markdown-Datei.

## **6.10 Autonomie und Systemzugriff**

Autonomie beschreibt den Handlungsspielraum eines Agents zwischen menschlichen Eingriffen. Systemzugriff beschreibt die Dateien, Dienste und Rechte, die ihm zur Verfügung stehen. Die Matrix der Folie betrachtet beide Dimensionen getrennt. Ihre Farben sind eine didaktische Orientierung, keine validierte Risikoskala. Das konkrete Risiko hängt von Aufgabe, Daten und Schutzmaßnahmen ab.

Für die Auslegung der Matrix sind die Begrenzung von Berechtigungen, risikobezogene menschliche Freigaben und nachvollziehbare Aktionen maßgeblich. NIST formuliert diese Gesichtspunkte als Entwurfsprinzipien für agentische Identitäts- und Zugriffssysteme. Der Beitrag ist eine fachliche Orientierung, kein Nachweis, dass ein konkreter Harness alle Kontrollen bereits umsetzt (NIST 2026).

### **Kein direkter Systemzugriff**

Der Agent erhält nur die übergebenen Inhalte. Beim Beraten bleibt das unmittelbare Aktionsrisiko geringer, die Vertraulichkeit der Eingaben und die Qualität der Antworten werden dennoch geprüft. Werden Vorschläge ausgeführt, übernimmt der Mensch die Schritte selbst. Autonome Bearbeitung ist auf die bereitgestellten Inhalte begrenzt, Aktionen in anderen Systemen stehen nicht zur Verfügung.

### **Begrenzter Zugriff**

Der Agent kann auf einen Projektordner oder auf Dienste mit ausdrücklich begrenzten Rechten zugreifen. Schon die Leserechte müssen passen, weil auch vertrauliche Inhalte gelesen werden können. Bei assistiertem Handeln bezieht sich die Freigabe auf die konkrete Handlung und die betroffenen Daten. Änderungen werden geprüft und ihre Rücknahme vorbereitet. Autonomes Handeln erfordert begrenzte Befugnisse und nachvollziehbare Aktionen.

### **Weitreichender Zugriff**

Der Agent erreicht Dateien, E-Mail oder Dienste mit umfangreichen Rechten. Bereits das Lesen kann sensible Informationen offenlegen. Zugriff wird deshalb auf die für den Auftrag erforderlichen Inhalte reduziert. Einzelfreigaben allein reichen als Schutz nicht aus. Vor einer weitergehenden Freigabe werden Systemzugriff und Handlungsspielraum begrenzt.

Welche Aktionen eine ausdrückliche Freigabe erfordern, wird für den Anwendungsfall festgelegt. Veröffentlichen, Löschen oder E-Mails senden sind Beispiele, die in der Übung bewusst besprochen werden. Die Vereinbarung wird anschließend mit den tatsächlich wirksamen technischen Kontrollen abgeglichen.

## **6.11 Hands-on: Autonomie und Zugriff im eigenen Setup prüfen**

Bleiben Sie in Ihrer laufenden Konversation. Beantworten Sie die Leitfragen und ergänzen Sie sie im Prompt.

  - Auf welchem Gerät und in welchem AI Harness arbeiten Sie?
  - Welche Daten möchten Sie verwenden?
  - Auf welche Dateien und Dienste kann Ihr Agent zugreifen?
  - Welche Aktionen darf er ohne Ihre Freigabe ausführen?
  - Welche Aktionen möchten Sie ausdrücklich selbst freigeben?

Wählen Sie eine geeignete Projektdatei aus. Beobachten Sie beim Zusammenfassen die Tool-Aufrufe und Freigabeanfragen. Ordnen Sie den Fall anschließend anhand von Handlungsspielraum und Systemzugriff in die Matrix ein.

### **Prompt**

Wir prüfen Autonomie und Zugriff für unseren bisherigen Anwendungsfall.

  

Meine Antworten auf die Leitfragen:

{{Ihre Antworten auf die Leitfragen}}

  

Kläre fehlende Angaben mit mir. Prüfe die für dich einsehbaren Zugriffsrechte und Freigabeeinstellungen. Trenne meine Angaben, überprüfte Einstellungen und offene Fragen. Ändere keine Einstellungen.

  

Lies die Datei \[Dateipfad\] und fasse sie kurz zusammen. Verändere keine Dateien. Nenne anschließend die verwendeten Tools und Zugriffe.

  

Welche Schutzmaßnahmen passen zu unserem Fall? Begründe sie aus knowledge/ und sources/ mit Datei und Fundstelle. Benenne Wissenslücken.

Der Agent kann nur einsehbare Einstellungen und tatsächlich ausgeführte Zugriffe beurteilen. Eine gelungene Zusammenfassung belegt keine allgemeine Absicherung des Systems. Vergleichen Sie die beobachteten Schritte mit Ihrer Einordnung und halten Sie ungeklärte Rechte oder Ausführungswege fest.

## **6.12 Zwischenfazit**

  - Wo in Ihrer Arbeit wäre eine solche Wissensbasis hilfreich? Welche Daten würden Sie unter welchen Bedingungen einbeziehen?
  - Konnten Sie nachvollziehen, was Ihr Agent gerade tut? Wann wurde es unübersichtlich?
  - Was fehlt Ihnen noch, um ab morgen selbstständig damit zu arbeiten?

### **Begriffe bis zum Zwischenfazit**

### **LLMs**

Frontier-LLMs, „Jagged Alien Intelligences“, Reasoning und Effort, Tokens und Tokenizer.

### **AI Agent und AI Harness**

Tool Use, Subagents, LLM-as-a-Judge.

### **Agentic Engineering**

Ziele, Vorgaben und mehrschrittige agentische Wissensarbeit.

### **Prompt Engineering**

Ziele, Vorgaben und Erfolgskriterien.

### **Knowledge Engineering**

Wissensbasis, Wissensdokumente, Markdown, Destillieren, Quellenverweise und Fundstellen.

### **Context Engineering**

Context Window, Context Rot, /context und /compact, AGENTS.md und CLAUDE.md.

### **Harness Engineering**

Permission Modes und Freigaben, Deny-Regeln, Hooks und Sandbox.

### **KI-Governance**

Autonomie und Systemzugriff, Zuständigkeiten und nachvollziehbare Entscheidungen.

# 7\. Promptotyping

## **7.1 Definition und Grundprinzip**

Promptotyping ist eine iterative, dokumentenbasierte Methode zur Entwicklung projektspezifischer digitaler Forschungsartefakte mit LLM-basierten AI Agents.

Der Begriff bezeichnet nicht lediglich das Erzeugen eines Prototyps durch Prompts. Im Mittelpunkt steht die gemeinsame Entwicklung von:

  - dokumentiertem Projektverständnis,
  - digitalem Forschungsartefakt,
  - Prüfverfahren,
  - begrenzten Gründen der Akzeptanz.

Der grundlegende Zyklus lautet:

**Abbildung 11: Promptotyping als geschlossener Entwicklungszyklus.**

*Projektwissen wird für eine Aufgabe in einen Working Context überführt und durch einen Agenten in ein digitales Forschungsartefakt operationalisiert. Verification und Validation erzeugen Evidenz und neue Erkenntnisse. Write-back führt diese Erkenntnisse in Wissensdokumente, Anforderungen und Modelle zurück.*

***Projektwissen → Working Context → agentische Implementation → digitales Forschungsartefakt → Prüfung → Revision des Projektwissens***

Das Artefakt und das dokumentierte Projektverständnis entwickeln sich gemeinsam weiter.

## **7.2 Preparation**

Preparation macht Daten, Quellen, Standards und Forschungskontext zugänglich.

Für die digitale Edition umfasst dies:

  - Seitenbilder beschaffen und eindeutig benennen;
  - Provenienz dokumentieren;
  - vorhandene Transkriptionen sichern;
  - Richtlinien und Schema-Versionen sammeln;
  - Ausgangsdateien vor Veränderungen schützen;
  - Projektstruktur anlegen.

Preparation ist mehr als Dateiverwaltung. Sie schafft einen nachvollziehbaren Ausgangszustand.

## **7.3 Exploration**

Exploration untersucht, was die Daten und Quellen ermöglichen und begrenzen.

Im Editionsprojekt kann sie zeigen:

  - welche Seitentypen vorliegen;
  - welche Schriften und Layouts auftreten;
  - welche wiederkehrenden editorischen Phänomene vorhanden sind;
  - wo die Rohtranskription unsicher ist;
  - welche Anforderungen das Frontend an das Modell stellt.

Exploration erzeugt noch keine endgültige Spezifikation. Sie macht sichtbar, welche Fragen geklärt und welche Entscheidungen dokumentiert werden müssen.

## **7.4 Distillation**

Distillation überführt das entwickelte Verständnis in gepflegte Dokumente:

  - source-description.md
  - transcription-rules.md
  - tei-model.md
  - requirements.md
  - design.md
  - verification.md

Diese Dokumente bilden die Grundlage weiterer agentischer Arbeit. Sie bleiben revidierbar, weil neue Erkenntnisse aus der Implementation frühere Annahmen verändern können.

## **7.5 Requirements Engineering und Scholar-Centred Design**

Requirements Engineering macht explizit, was ein Artefakt leisten soll. In einem wissenschaftlichen Projekt reicht es nicht, „eine schöne digitale Edition“ zu verlangen.

Anforderungen können lauten:

  - Faksimile und Transkription müssen eindeutig zugeordnet sein.
  - Diplomatische und normalisierte Lesung müssen unterscheidbar bleiben.
  - Unsichere Lesungen dürfen nicht wie sicherer Text erscheinen.
  - Editorische Eingriffe müssen nachvollziehbar sein.
  - Quelldaten dürfen nicht stillschweigend verändert werden.
  - Das Artefakt muss lokal und ohne proprietären Dienst ausführbar sein.

**Scholar-Centred Design** richtet die Entwicklung an den Forschungspraktiken, Interpretationsaufgaben und Verantwortlichkeiten der beteiligten Wissenschaftler:innen aus. Es fragt nicht nur, ob eine Oberfläche benutzbar ist, sondern welche wissenschaftlichen Unterscheidungen sie sichtbar oder unsichtbar macht.

## **7.6 Implementation**

Implementation macht die Wissensbasis handlungsfähig. Der Agent übersetzt dokumentierte Anforderungen in:

  - TEI-Dateien,
  - Transformationsskripte,
  - Stylesheets,
  - Tests,
  - ein lokales Frontend,
  - Dokumentation.

Implementation ist keine neutrale Ausführung einer vollständig bestimmten Spezifikation. Erst durch das funktionierende Artefakt kann sichtbar werden, dass eine Regel fehlt oder eine Modellierung zu grob ist.

Ein Beispiel: Im TEI-Modell werden alle unsicheren Lesungen gleich behandelt. Im Frontend zeigt sich jedoch, dass zwischen „teilweise lesbar“, „editorisch ergänzt“ und „vollständig unleserlich“ unterschieden werden muss. Diese Erkenntnis gehört nicht nur in den Code, sondern zurück in das Wissensdokument und gegebenenfalls in das Datenmodell.

## **7.7 Verification, Validation und Acceptance**

Drei Ebenen müssen unterschieden werden.

**Abbildung 12: Prüfung, Evidenz und verantwortliche Acceptance.**

*Deterministische Validation und agentisches Review liefern überprüfbare Evidenz. Die fachliche und wissenschaftliche Beurteilung verbleibt beim Critical Expert. Erst diese verantwortliche Prüfung kann zu einer zweckgebundenen Acceptance führen; technische Konformität allein autorisiert kein Forschungsartefakt.*

### **Technische Verifikation**

Prüft Konformität mit formalisierten Anforderungen:

  - XML ist wohlgeformt;
  - TEI entspricht dem Schema;
  - Tests laufen erfolgreich;
  - Transformationen erzeugen die erwarteten Dateien;
  - Quelldateien wurden nicht verändert.

### **Fachliche und wissenschaftliche Validierung**

Prüft, ob Repräsentation und Artefakt für den vorgesehenen Forschungszweck angemessen sind:

  - Entspricht die Transkription der Quelle?
  - Sind editorische Unsicherheiten angemessen repräsentiert?
  - Unterstützt das Interface die vorgesehenen Interpretationshandlungen?
  - Werden Modellierungsentscheidungen sichtbar oder irreführend naturalisiert?

### **Acceptance**

Bezeichnet die verantwortliche Entscheidung, einen identifizierbaren Projektzustand für einen benannten Zweck anzunehmen.

Ein technisch verifiziertes Artefakt kann wissenschaftlich ungeeignet sein. Umgekehrt kann ein wissenschaftlich interessanter Demonstrator technisch noch nicht publikationsreif sein. Acceptance muss deshalb zweckgebunden formuliert werden.

## **7.8 Critical Expert**

Der **Critical Expert** trägt die Verantwortung dort, wo Prüfung Quellenkenntnis, Interpretation oder Designurteil verlangt.

Agents und Validatoren können:

  - Fehler lokalisieren,
  - Kriterien anwenden,
  - Unterschiede berichten,
  - Evidenz zusammenstellen.

Der Critical Expert entscheidet:

  - welche Lesung vertretbar ist;
  - ob eine Modellierung der Quelle angemessen entspricht;
  - ob die Oberfläche wissenschaftliche Differenzierungen erhält;
  - ob der Zustand für den benannten Zweck akzeptiert wird.

Die Rolle ist nicht auf eine einzelne Person beschränkt. Sie bezeichnet die verantwortliche fachliche Autorität im Projekt.

## **7.9 Write-back**

Implementation und Prüfung erzeugen neues Wissen. Dieses Wissen muss in die zuständigen Dokumente zurückgeschrieben werden.

Mögliche Write-backs:

  - Transkriptionsregel präzisieren;
  - neuen Unsicherheitstyp ergänzen;
  - Datenmodell revidieren;
  - Designentscheidung begründen;
  - bekannte Einschränkung dokumentieren;
  - Verifikationskriterium erweitern.

Write-back verhindert, dass relevantes Wissen nur im Chat, im Code oder im Gedächtnis einzelner Personen verbleibt.

## **7.10 Der Promptotype**

Ein **Promptotype** ist der dokumentierte und referenzierbare Zustand einer Iteration. Er umfasst:

  - den relevanten Stand der Project Knowledge Base,
  - das digitale Forschungsartefakt,
  - den referenzierten Datenzustand,
  - dokumentierte Prüfungen,
  - offene Fragen,
  - die begrenzten Gründe der Acceptance.

Ein Promptotype ist kein endgültiges Produkt. Er ist ein hinreichend bestimmter Zustand, von dem weitere Arbeit ausgehen kann.

## **7.11 Hands-on: Write-back und Acceptance dokumentieren**

### **Write-back**

Analysieren Sie die Implementation und dokumentieren Sie:

  - neue Erkenntnisse über die Quelle,
  - neue Anforderungen,
  - unzureichende Regeln,
  - offene fachliche Fragen,
  - notwendige Änderungen an Datenmodell oder Frontend.

### **Acceptance Statement**

\\\<a id="acceptance-statement-2"\\\>\\\</a\\\>

\# Acceptance Statement

\\\<a id="identifizierter-zustand"\\\>\\\</a\\\>

\#\# Identifizierter Zustand

\\- Knowledge Base: Commit \\abc123\\

\\- TEI-Daten: Version \\0.3\\

\\- Frontend: Build \\2026-08-01\\

\\- Schema: \\edition.rng\\, Version \\1.2\\

\\\<a id="accepted-for"\\\>\\\</a\\\>

\#\# Accepted for

Interner Demonstrator zur Prüfung des TEI-Modells und der synoptischen

Darstellung von Faksimile, diplomatischer Transkription und Normalisierung.

\\\<a id="technisch-verifiziert"\\\>\\\</a\\\>

\#\# Technisch verifiziert

\\- XML-Wohlgeformtheit

\\- Schema-Konformität

\\- erfolgreiche lokale Transformation

\\- unveränderte Quelldateien

\\- Navigation zwischen den Beispielseiten

\\\<a id="fachlich-gepruft"\\\>\\\</a\\\>

\#\# Fachlich geprüft

\\- Zuordnung von Faksimile und Transkription

\\- Darstellung der markierten Unsicherheiten

\\- Nachvollziehbarkeit editorischer Eingriffe

\\\<a id="nicht-nachgewiesen"\\\>\\\</a\\\>

\#\# Nicht nachgewiesen

\\- vollständige philologische Verifikation des Korpus

\\- Eignung für eine öffentliche oder zitierfähige Edition

\\- Barrierefreiheit und produktive Langzeitverfügbarkeit

\\\<a id="offene-fragen"\\\>\\\</a\\\>

\#\# Offene Fragen

\\- Unterscheidung zwischen teilweise lesbaren und ergänzten Eigennamen

\\- Darstellung konkurrierender Normalisierungen

# 8\. Zusammenfassung und Begriffsübersicht

Die Engineering-Begriffe bezeichnen unterschiedliche Gegenstände. Die Übersicht zeigt die Aufgabenformulierung, den Wissensbestand, den aktuellen Kontext und die mehrschrittige Ausführung. Harness Engineering ergänzt die Gestaltung der technischen Arbeitsumgebung.

|  |  |  |
| :-: | :-: | :-: |
| \*\*Ebene\*\* | \*\*Gegenstand\*\* | \*\*Leitfrage\*\* |
| Prompt Engineering | aktuelle Eingabesequenz | Wie wird die Aufgabe formuliert? |
| Knowledge Engineering | persistenter Wissensbestand | Was muss explizit dokumentiert und gepflegt werden? |
| Context Engineering | Informationszustand einer Aufgabe | Welche Informationen benötigt der Agent jetzt? |
| Agentic Engineering | mehrschrittige Ausführung | Wie wird die Arbeit organisiert, begrenzt und geprüft? |
| Harness Engineering | Werkzeuge, Befugnisse und Prüfverfahren | Wie wird die technische Arbeitsumgebung gestaltet? |

Harness Engineering gestaltet Werkzeuge, Befugnisse und Prüfverfahren der technischen Umgebung. KI-Governance bestimmt, wer den Einsatz verantwortet, welche Regeln gelten und wie ihre Einhaltung überprüft wird. Die Anwendung auf den aktuellen Workshop-Fall und die Begriffe bis Folie 25 stehen in den Abschnitten 6.8–6.12.

Promptotyping verbindet diese Ebenen in einem iterativen Forschungsworkflow.

Die zentrale Formel lautet:

***Prompt Engineering gestaltet die aktuelle Eingabesequenz.***

***Context Engineering organisiert den Informationszustand einer Aufgabe.***

***Knowledge Engineering baut und pflegt den dafür verfügbaren Wissensbestand.***

***Agentic Engineering organisiert die mehrschrittige Ausführung.***

***Promptotyping verbindet diese Ebenen in der iterativen Entwicklung und verantwortlichen Prüfung digitaler Forschungsartefakte.***

Die digitale Edition zeigt, warum diese Verbindung notwendig ist. Quelle, Transkription, Datenmodell, Transformation und Frontend bilden keinen neutralen technischen Ablauf. Jede Stufe enthält Entscheidungen darüber, welche Unterschiede sichtbar, bearbeitbar und interpretierbar werden. AI Agents können diese Arbeit erheblich unterstützen. Sie können jedoch die fachliche Verantwortung für Repräsentation, Validierung und Acceptance nicht übernehmen.

# 9\. Literaturverzeichnis

Anthropic. 2025\\. “Claude’s Character.” Anthropic Research.

Anthropic. 2026\\. “Claude’s Constitution.” Anthropic.

Battle, Rick, and Teja Gollapudi. 2024\\. “The Unreasonable Effectiveness of Eccentric Automatic Prompts.” arXiv:2402.10949.

Hong, Kelly, Anton Troynikov, and Jeff Huber. 2025\\. “Context Rot: How Increasing Input Tokens Impacts LLM Performance.” Chroma Research.

Hu, Tiancheng, and Nigel Collier. 2024\\. “Quantifying the Persona Effect in LLM Simulations.” arXiv:2402.10811.

Li, Cheng, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, and Xing Xie. 2023\\. “Large Language Models Understand and Can Be Enhanced by Emotional Stimuli.” arXiv:2307.11760.

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. 2025\\. “On the Biology of a Large Language Model.” Transformer Circuits.

Mei, et al. 2025\\. “Context Engineering for Large Language Models.” arXiv:2507.13334.

Pollin, Christopher. 2026\\. “Asymmetric Amplification.” Digital Humanities Craft.

Pollin, Christopher. 2026\\. “Promptotyping.” Manuskript in Vorbereitung.

Rajeev, Meghana, Rajkumar Ramamurthy, Prapti Trivedi, et al. 2025\\. “Cats Confuse Reasoning LLM: Query Agnostic Adversarial Triggers for Reasoning Models.” arXiv:2503.01781.

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. 2024\\. “The Prompt Report: A Systematic Survey of Prompting Techniques.” arXiv:2406.06608.

Yin, Ziqi, Hao Wang, Kaito Horio, Daisuke Kawahara, and Satoshi Sekine. 2024\\. “Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance.” arXiv:2402.14531.

Anthropic. 2025. Effective context engineering for AI agents. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

Anthropic. How Claude Code works. Claude Code Docs. <https://code.claude.com/docs/en/how-claude-code-works>

Anthropic. Choose a permission mode. Claude Code Docs. <https://code.claude.com/docs/en/permission-modes>

Anthropic. Configure the sandboxed Bash tool. Claude Code Docs. <https://code.claude.com/docs/en/sandboxing>

Anthropic. Create custom subagents. Claude Code Docs. <https://code.claude.com/docs/en/sub-agents>

Anthropic. How Claude remembers your project. Claude Code Docs. <https://code.claude.com/docs/en/memory>

IEEE Standards Association. 2026. AI Ethics vs. AI Governance: What’s the Difference? 5. Juni. <https://standards.ieee.org/beyond-standards/ai-ethics-vs-ai-governance-whats-the-difference/>

National Institute of Standards and Technology (NIST). 2026. Design Tenets for Agent Identity Management Systems. 27. Oktober. <https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems>

Wu, Zheng, et al. Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents. 2. November 2026. <https://arxiv.org/abs/2611.03092>

Zhong, Hailin, und Shengxin Zhu. AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents. 13. Mai 2026. <https://doi.org/10.48550/arXiv.2605.13357>

# 10\. Anhang: Vorlagen

## **A. Vorlage für ein Wissensdokument**

\\---

document\_type: knowledge

status: draft

owner:

sources:

last\_reviewed:

\\---

\\\<a id="gegenstand"\\\>\\\</a\\\>

\# Gegenstand

\\\<a id="zweck"\\\>\\\</a\\\>

\#\# Zweck

\\\<a id="begriffe-und-unterscheidungen"\\\>\\\</a\\\>

\#\# Begriffe und Unterscheidungen

\\\<a id="regeln"\\\>\\\</a\\\>

\#\# Regeln

\\\<a id="einschrankungen-und-ausnahmen"\\\>\\\</a\\\>

\#\# Einschränkungen und Ausnahmen

\\\<a id="unsicherheiten"\\\>\\\</a\\\>

\#\# Unsicherheiten

\\\<a id="offene-fragen-2"\\\>\\\</a\\\>

\#\# Offene Fragen

\\\<a id="quellen"\\\>\\\</a\\\>

\#\# Quellen

## **B. Vorlage für eine Instruktionsdatei**

\\\<a id="rolle-und-arbeitsmodus"\\\>\\\</a\\\>

\# Rolle und Arbeitsmodus

\\\<a id="projektstruktur"\\\>\\\</a\\\>

\# Projektstruktur

\\\<a id="verbindliche-arbeitsregeln"\\\>\\\</a\\\>

\# Verbindliche Arbeitsregeln

\\\<a id="werkzeuge-und-befehle"\\\>\\\</a\\\>

\# Werkzeuge und Befehle

\\\<a id="regeln-fur-ruckfragen-und-eskalation"\\\>\\\</a\\\>

\# Regeln für Rückfragen und Eskalation

\\\<a id="abschlusskriterien"\\\>\\\</a\\\>

\# Abschlusskriterien

\\\<a id="verweise-auf-wissensdokumente"\\\>\\\</a\\\>

\# Verweise auf Wissensdokumente

## **C. Vorlage für einen Working Context**

\\\<a id="aufgabe-2"\\\>\\\</a\\\>

\# Aufgabe

\\\<a id="relevante-anforderungen"\\\>\\\</a\\\>

\# Relevante Anforderungen

\\\<a id="bereitgestellte-wissensdokumente"\\\>\\\</a\\\>

\# Bereitgestellte Wissensdokumente

\\\<a id="ausgangsdateien-und-daten"\\\>\\\</a\\\>

\# Ausgangsdateien und Daten

\\\<a id="verfugbare-werkzeuge"\\\>\\\</a\\\>

\# Verfügbare Werkzeuge

\\\<a id="aktueller-projektzustand"\\\>\\\</a\\\>

\# Aktueller Projektzustand

\\\<a id="prufkriterien-2"\\\>\\\</a\\\>

\# Prüfkriterien

\\\<a id="bekannte-unsicherheiten"\\\>\\\</a\\\>

\# Bekannte Unsicherheiten

\\\<a id="bewusst-nicht-geladene-ressourcen"\\\>\\\</a\\\>

\# Bewusst nicht geladene Ressourcen

## **D. Vorlage für einen Verification Report**

\\\<a id="verification-report"\\\>\\\</a\\\>

\# Verification Report

\\\<a id="identifizierter-zustand-2"\\\>\\\</a\\\>

\#\# Identifizierter Zustand

\\\<a id="ausgefuhrte-technische-prufungen"\\\>\\\</a\\\>

\#\# Ausgeführte technische Prüfungen

\\\<a id="ergebnisse"\\\>\\\</a\\\>

\#\# Ergebnisse

\\\<a id="abweichungen"\\\>\\\</a\\\>

\#\# Abweichungen

\\\<a id="nicht-geprufte-aspekte"\\\>\\\</a\\\>

\#\# Nicht geprüfte Aspekte

\\\<a id="fachliche-fragen"\\\>\\\</a\\\>

\#\# Fachliche Fragen

\\\<a id="empfohlene-nachste-schritte"\\\>\\\</a\\\>

\#\# Empfohlene nächste Schritte

## **E. Vorlage für ein Acceptance Statement**

\\\<a id="acceptance-statement-3"\\\>\\\</a\\\>

\# Acceptance Statement

\\\<a id="identifizierter-zustand-3"\\\>\\\</a\\\>

\#\# Identifizierter Zustand

\\\<a id="accepted-for-2"\\\>\\\</a\\\>

\#\# Accepted for

\\\<a id="technisch-verifiziert-2"\\\>\\\</a\\\>

\#\# Technisch verifiziert

\\\<a id="fachlich-gepruft-2"\\\>\\\</a\\\>

\#\# Fachlich geprüft

\\\<a id="nicht-nachgewiesen-2"\\\>\\\</a\\\>

\#\# Nicht nachgewiesen

\\\<a id="offene-fragen-3"\\\>\\\</a\\\>

\#\# Offene Fragen

\\\<a id="verantwortliche-entscheidung"\\\>\\\</a\\\>

\#\# Verantwortliche Entscheidung

# Anmerkungen

  - Die Beschreibung als Next Token Prediction ist eine funktionale Vereinfachung. Sie erklärt den unmittelbaren Generationsmechanismus, nicht die gesamte interne Verarbeitung eines Transformer-Modells.
  - Für die Unterscheidung zwischen zugrunde liegendem Modell, Assistant-Verhalten und trainiertem Charakter sind insbesondere die Veröffentlichungen von Anthropic zu Claude’s Character und zur Constitution relevant. Die ontologische Interpretation dieser Begriffe bleibt jedoch umstritten.
  - Produktbezeichnungen und konkrete Funktionen agentischer Arbeitsumgebungen verändern sich schnell. Die im Skriptum genannten Systeme dienen als Beispiele; Funktionsumfang und Terminologie sollten vor einer Publikation gegen die jeweils aktuelle Dokumentation geprüft werden.
  - Die nominelle Kontextgröße ist nicht mit einer garantierten effektiven Nutzung aller enthaltenen Information gleichzusetzen. Forschung zu Long-Context-Systemen untersucht unter anderem Positions-, Distraktor- und Retrievaleffekte.
  - MCP bezeichnet eine technische Spezifikation für die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Die konkrete Sicherheits- und Berechtigungsarchitektur hängt von der jeweiligen Implementation ab.
