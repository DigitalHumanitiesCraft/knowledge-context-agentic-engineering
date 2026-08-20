# Knowledge, Context and Agentic Engineering

## Konzepte, Methoden und Workflows für die kontrollierte Arbeit mit LLM-basierten AI Agents

**Dr. Christopher Pollin, MA MA**  
Digital Humanities Craft OG  
[www.dhcraft.org](https://www.dhcraft.org) · [office@dhcraft.org](mailto:office@dhcraft.org)

**Workshopskriptum · Arbeitsfassung · Juli 2026**

**Foliensatz:** *Knowledge, Context and Agentic Engineering*  
**Begleitmaterialien:** Workshopunterlagen und Hands-on-Dateien

## Abstract

LLM-basierte AI Agents können computer- und datenbasierte Forschungsarbeit über einzelne Modellantworten hinaus unterstützen. Sie können Dateien untersuchen, Werkzeuge aufrufen, Programme ausführen, Zwischenergebnisse verarbeiten und digitale Forschungsartefakte über mehrere Schritte hinweg entwickeln. Ihre produktive Nutzung hängt jedoch nicht allein von der Leistungsfähigkeit eines Modells oder der Formulierung einzelner Prompts ab. Sie setzt voraus, dass relevantes Projektwissen explizit dokumentiert, für konkrete Aufgaben gezielt bereitgestellt und die daraus entstehende agentische Arbeit innerhalb einer technischen Umgebung organisiert, begrenzt und geprüft wird.

Das Skriptum unterscheidet dafür vier miteinander verbundene Arbeitsebenen. **Prompt Engineering** gestaltet die aktuelle Eingabesequenz. **Knowledge Engineering** baut und pflegt einen expliziten, inspizierbaren und revidierbaren Bestand von Projektwissen. **Context Engineering** stellt daraus und aus weiteren Ressourcen den Informationszustand zusammen, den ein Modell oder Agent für eine konkrete Aufgabe benötigt. **Agentic Engineering** organisiert die mehrschrittige Ausführung, in der ein Agent Dateien und Daten untersucht, Werkzeuge verwendet, Ergebnisse verarbeitet und auf dieser Grundlage weitere Handlungen auswählt. Ein **AI Harness** stellt dafür den technischen Zugriff auf Dateien, Werkzeuge und Ausführungsumgebungen sowie die Verwaltung von Zustand, Zugriffsrechten und Rückmeldungen bereit.

Diese Ebenen werden im **Promptotyping** als iterativer, dokumentenbasierter Forschungsworkflow verbunden. Eine fortschreibbare Project Knowledge Base hält den gegenwärtigen Stand des Projektwissens fest. Für einzelne Aufgaben werden daraus geeignete Working Contexts zusammengestellt. AI Agents erzeugen oder verändern auf dieser Grundlage digitale Forschungsartefakte. Erkenntnisse aus Exploration, Implementation und Prüfung werden anschließend in den dokumentierten Projektstand zurückgeführt.

Als durchgehendes Beispiel dient die Entwicklung eines kleinen Demonstrators für eine digitale Edition. Der Fall verbindet Datenerzeugung, Datenmodellierung, Transformation, Frontend-Darstellung, technische Verifikation und fachliche Validierung. Dadurch wird sichtbar, dass eine digitale Edition nicht allein aus einem Interface besteht. Sie umfasst die nachvollziehbare Verbindung von Quelle, erzeugten Daten, Datenmodell, Transformation, Darstellung und den Gründen ihrer zweckgebundenen Akzeptanz.

## Zu diesem Skriptum

Dieses Skriptum begleitet den gleichnamigen Foliensatz und folgt grundsätzlich dessen Dramaturgie. Die Folien verdichten Begriffe, Prozesse, Beispiele und Arbeitsaufträge visuell; die zugehörigen Kapitel erläutern die Argumentation, definieren zentrale Konzepte und dokumentieren die Hands-on-Übungen. Begriffe werden zunächst orientierend eingeführt und später an einer maßgeblichen Stelle vollständig ausgearbeitet. Wiederholungen erscheinen nur dort, wo sie für das Verständnis einer neuen Anwendung erforderlich sind. Quellen werden im Text durch Kurzbelege referenziert; vollständige Angaben stehen im Literaturverzeichnis. Ergänzende technische oder begriffliche Hinweise erscheinen in Fußnoten.

## Inhaltsverzeichnis

- [1\. Einführung](#1-einfuhrung)  
  - [1.1 Ausgangslage](#1-1-ausgangslage)  
  - [1.2 Vom einzelnen Prompt zur organisierten Arbeitsumgebung](#1-2-vom-einzelnen-prompt-zur-organisierten-arbeitsumgebung)  
  - [1.3 Zentrale These](#1-3-zentrale-these)  
  - [1.4 Durchgehendes Beispiel: eine digitale Edition](#1-4-durchgehendes-beispiel-eine-digitale-edition)  
  - [1.5 Lernziele und Aufbau](#1-5-lernziele-und-aufbau)  
- [2\. Grundlagen: LLM, Assistant, AI Agent und AI Harness](#2-grundlagen-llm-assistant-ai-agent-und-ai-harness)  
  - [2.1 LLMs als probabilistische Textsysteme](#2-1-llms-als-probabilistische-textsysteme)  
  - [2.2 Pre-Training, Post-Training und Assistant-Verhalten](#2-2-pre-training-post-training-und-assistant-verhalten)  
  - [2.3 Vom Modell zum Agenten](#2-3-vom-modell-zum-agenten)  
  - [2.4 Das AI Harness](#2-4-das-ai-harness)  
- [3\. Prompt Engineering](#3-prompt-engineering)  
  - [3.1 Prompt und Prompt Engineering](#3-1-prompt-und-prompt-engineering)  
  - [3.2 Der Prompt als begrenzte Spezifikation](#3-2-der-prompt-als-begrenzte-spezifikation)  
  - [3.3 Rollen- und Persona-Prompting](#3-3-rollen-und-persona-prompting)  
  - [3.4 Iteration, Self-Revision und strukturierte Ausgaben](#3-4-iteration-self-revision-und-strukturierte-ausgaben)  
  - [3.5 Warum Promptwirkungen schwer zu evaluieren sind](#3-5-warum-promptwirkungen-schwer-zu-evaluieren-sind)  
  - [3.6 Mechanistische Perspektive](#3-6-mechanistische-perspektive)  
  - [3.7 Grenzen des Prompt Engineering](#3-7-grenzen-des-prompt-engineering)  
  - [3.8 Hands-on: Eine Editionsaufgabe als begrenzte Spezifikation](#3-8-hands-on-eine-editionsaufgabe-als-begrenzte-spezifikation)  
- [4\. Context Engineering](#4-context-engineering)  
  - [4.1 Vom Prompt zum Informationszustand einer Aufgabe](#4-1-vom-prompt-zum-informationszustand-einer-aufgabe)  
  - [4.2 Context Window und Context Rot](#4-2-context-window-und-context-rot)  
  - [4.3 Wie Informationen in den Modellkontext gelangen](#4-3-wie-informationen-in-den-modellkontext-gelangen)  
  - [4.4 Context Compression und Distillation](#4-4-context-compression-und-distillation)  
  - [4.5 Project Knowledge Base, Working Context und Context Window](#4-5-project-knowledge-base-working-context-und-context-window)  
  - [4.6 Hands-on: Einen Working Context für eine TEI-Aufgabe zusammenstellen](#4-6-hands-on-einen-working-context-fur-eine-tei-aufgabe-zusammenstellen)  
- [5\. Knowledge Engineering](#5-knowledge-engineering)  
  - [5.1 Warum Projektwissen explizit werden muss](#5-1-warum-projektwissen-explizit-werden-muss)  
  - [5.2 Knowledge Acquisition](#5-2-knowledge-acquisition)  
  - [5.3 Project Knowledge Base](#5-3-project-knowledge-base)  
  - [5.4 Wissensdokumente](#5-4-wissensdokumente)  
  - [5.5 Markdown als technische Repräsentation](#5-5-markdown-als-technische-reprasentation)  
  - [5.6 Instruktionsdateien und Agent Skills](#5-6-instruktionsdateien-und-agent-skills)  
  - [5.7 Governance und Kuration](#5-7-governance-und-kuration)  
  - [5.8 Hands-on: Ein Wissensdokument zu editorischer Unsicherheit destillieren](#5-8-hands-on-ein-wissensdokument-zu-editorischer-unsicherheit-destillieren)  
- [6\. Agentic Engineering](#6-agentic-engineering)  
  - [6.1 Warum mehrschrittige Arbeit organisiert werden muss](#6-1-warum-mehrschrittige-arbeit-organisiert-werden-muss)  
  - [6.2 Agentische Ausführungsschleife](#6-2-agentische-ausfuhrungsschleife)  
  - [6.3 Planung, Ausführung und Feedback](#6-3-planung-ausfuhrung-und-feedback)  
  - [6.4 Werkzeuge, Berechtigungen und Reversibilität](#6-4-werkzeuge-berechtigungen-und-reversibilitat)  
  - [6.5 MCP, Subagents und Agent-to-Agent-Kommunikation](#6-5-mcp-subagents-und-agent-to-agent-kommunikation)  
  - [6.6 Versionierte Zwischenstände und menschliche Intervention](#6-6-versionierte-zwischenstande-und-menschliche-intervention)  
  - [6.7 Hands-on: TEI erzeugen, validieren und ein Frontend implementieren](#6-7-hands-on-tei-erzeugen-validieren-und-ein-frontend-implementieren)  
- [7\. Promptotyping](#7-promptotyping)  
  - [7.1 Definition und Grundprinzip](#7-1-definition-und-grundprinzip)  
  - [7.2 Preparation](#7-2-preparation)  
  - [7.3 Exploration](#7-3-exploration)  
  - [7.4 Distillation](#7-4-distillation)  
  - [7.5 Requirements Engineering und Scholar-Centred Design](#7-5-requirements-engineering-und-scholar-centred-design)  
  - [7.6 Implementation](#7-6-implementation)  
  - [7.7 Verification, Validation und Acceptance](#7-7-verification-validation-und-acceptance)  
  - [7.8 Critical Expert](#7-8-critical-expert)  
  - [7.9 Write-back](#7-9-write-back)  
  - [7.10 Der Promptotype](#7-10-der-promptotype)  
  - [7.11 Hands-on: Write-back und Acceptance dokumentieren](#7-11-hands-on-write-back-und-acceptance-dokumentieren)  
- [8\. Zusammenfassung und Begriffsübersicht](#8-zusammenfassung-und-begriffsubersicht)  
- [9\. Literaturverzeichnis](#9-literaturverzeichnis)  
- [10\. Anhang: Vorlagen](#10-anhang-vorlagen)

## Abbildungsverzeichnis

1. Wissensbestand, Working Context und agentische Ausführung  
2. Die digitale Edition als durchgehender Arbeitszusammenhang  
3. Sprachmodell und Assistentenfigur  
4. Konkurrierende Deutungen des Prompt Engineering  
5. Modell-, aufgaben- und sprachabhängige Promptwirkungen  
6. Warum Prompt Engineering schwer zu evaluieren ist  
7. Didaktisches Modell der Promptwirkung  
8. Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung  
9. Project Knowledge Base, Working Context und Context Window  
10. Agentische Ausführungsschleife  
11. Promptotyping als geschlossener Entwicklungszyklus  
12. Prüfung, Evidenz und verantwortliche Acceptance

# 1\. Einführung

## 1.1 Ausgangslage

Large Language Models werden zunehmend nicht nur als Systeme für einzelne Frage-Antwort-Interaktionen eingesetzt. In Verbindung mit Dateien, Werkzeugen und Ausführungsumgebungen können sie Aufgaben über mehrere Schritte hinweg bearbeiten. Ein LLM-basierter AI Agent kann Projektressourcen untersuchen, Informationen aus unterschiedlichen Quellen zusammenführen, Code erzeugen und ausführen, Fehlermeldungen verarbeiten und sein weiteres Vorgehen an den beobachteten Projektzustand anpassen.

Diese Entwicklung erweitert die Möglichkeiten computer- und datenbasierter Forschung. Eine Historikerin kann beispielsweise aus einer kleinen Sammlung von Quellenbildern einen ersten Transkriptionsentwurf erzeugen lassen. Ein Editionsprojekt kann TEI-Dateien gegen ein Schema prüfen, Varianten eines Frontends erzeugen und die Darstellung editorischer Unsicherheit vergleichen. Ein Forschungsteam kann Datenprofile, Transformationen und Visualisierungen erstellen, ohne jeden technischen Schritt vollständig von Grund auf programmieren zu müssen.

Die Fähigkeit, ein Artefakt zu erzeugen, ist jedoch nicht mit der Fähigkeit gleichzusetzen, dessen technische Korrektheit oder wissenschaftliche Angemessenheit zuverlässig zu beurteilen. Eine TEI-Datei kann wohlgeformt und schema-valide sein, obwohl eine unsichere Lesung editorisch unangemessen als sicherer Text ausgezeichnet wurde. Ein Interface kann technisch funktionieren und trotzdem den Eindruck erwecken, eine normalisierte Form sei die einzig richtige Lesart. Ein Datenmodell kann konsistent sein und zugleich Unterschiede ausblenden, die für die Forschungsfrage entscheidend sind.

Die zentrale Herausforderung liegt deshalb nicht allein in der Erzeugung von Ergebnissen. Sie liegt in der Organisation der Bedingungen, unter denen diese Ergebnisse entstehen, geprüft, revidiert und für einen benannten Zweck verwendet werden können.

## 1.2 Vom einzelnen Prompt zur organisierten Arbeitsumgebung

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

## 1.3 Zentrale These

Die zentrale These dieses Skriptums lautet:

**Abbildung 1: Wissensbestand, Working Context und agentische Ausführung.**  
*Die schematische Übersicht zeigt die vier Ebenen des Skriptums. Prompt Engineering formuliert die aktuelle Aufgabe. Knowledge Engineering pflegt den persistenten Projektbestand. Context Engineering wählt daraus und aus weiteren Ressourcen den Working Context. Agentic Engineering organisiert die Ausführung im AI Harness. Rückmeldungen aus Implementation und Prüfung können Änderungen an allen vier Ebenen auslösen.*

> Produktive und nachvollziehbare Arbeit mit LLM-basierten AI Agents entsteht nicht allein durch bessere Modelle oder besser formulierte Prompts. Sie setzt das Zusammenspiel von organisiertem Projektwissen, aufgabenspezifischem Kontext, kontrollierter agentischer Ausführung und verantwortlicher Prüfung voraus.

Vier Begriffe strukturieren diesen Zusammenhang:

- **Prompt Engineering** gestaltet die aktuelle Eingabesequenz.  
- **Knowledge Engineering** baut und pflegt den verfügbaren Wissensbestand.  
- **Context Engineering** stellt den für eine konkrete Aufgabe erforderlichen Informationszustand zusammen.  
- **Agentic Engineering** organisiert die mehrschrittige Ausführung innerhalb einer technischen Umgebung.

Das **AI Harness** vermittelt zwischen diesen Ebenen. Es stellt Werkzeuge und Zugriffe bereit, verwaltet den Zustand einer Arbeit und gibt Ergebnisse an das Modell zurück. Es entscheidet jedoch nicht, welche editorische Lesung angemessen ist oder ob ein Artefakt für eine Publikation akzeptiert werden kann.

## 1.4 Durchgehendes Beispiel: eine digitale Edition

Das Skriptum verwendet eine kleine digitale Edition als durchgehendes Beispiel. Ausgangspunkt sind drei bis fünf historische Seitenbilder, eine Rohtranskription, editorische Richtlinien und ein begrenztes TEI-Ausgangsmodell. Ziel ist ein lokaler Demonstrator, der Faksimile, diplomatische Transkription, normalisierte Lesung und editorische Unsicherheiten sichtbar macht.

Das Beispiel verbindet drei Arbeitsbereiche:

**Abbildung 2: Die digitale Edition als durchgehender Arbeitszusammenhang.**  
*Die Abbildung verbindet Quellenbilder und Datenerzeugung mit TEI-basierter Datenmodellierung, Transformation und Frontend-Darstellung. Die Pfeile verlaufen nicht nur in Richtung des Interfaces: Probleme, die erst in der Darstellung sichtbar werden, führen zurück zu Transkription, Modellierungsregeln und Anforderungen.*

1. **Datenerzeugung:** Transkription, Annotation, Normalisierung und Provenienz.  
2. **Datenmodellierung:** TEI-Strukturen, Entitäten, Relationen, Varianten und Unsicherheiten.  
3. **Frontend-Darstellung:** synoptische Ansichten, Umschaltung von Textschichten, Hervorhebung von Annotationen und Darstellung editorischer Eingriffe.

Die Bereiche sind nicht voneinander unabhängig. Erst in der Frontend-Darstellung kann sichtbar werden, dass eine Modellierungsregel unzureichend ist. Eine als einfaches Attribut modellierte Unsicherheit kann sich beispielsweise nicht differenziert genug darstellen lassen. Umgekehrt kann eine elegante Oberfläche eine editorisch problematische Vereinfachung verdecken. Die Implementation ist daher nicht nur Ausführung, sondern auch eine Form der Untersuchung des Projektwissens.

## 1.5 Lernziele und Aufbau

Nach der Bearbeitung des Skriptums und der zugehörigen Übungen sollen die Teilnehmenden:

- Prompt, Knowledge, Context und Agentic Engineering unterscheiden können;  
- die Rolle eines AI Harness erklären können;  
- Prompts als begrenzte Spezifikationen formulieren können;  
- zwischen Project Knowledge Base, Working Context und Context Window unterscheiden können;  
- Wissensdokumente aus heterogenen Quellen destillieren können;  
- mehrschrittige agentische Aufgaben planen, begrenzen und prüfen können;  
- technische Verifikation von fachlicher und wissenschaftlicher Validierung unterscheiden können;  
- Erkenntnisse aus Implementation und Prüfung in den dokumentierten Projektstand zurückführen können;  
- die Grenzen agentischer Autonomie und die Notwendigkeit verantwortlicher menschlicher Entscheidungen erkennen.

Die Kapitel folgen einer einfachen Bewegung: vom einzelnen Prompt über den aktiven Kontext und den persistenten Wissensbestand zur agentischen Ausführung und schließlich zum Promptotyping als integrierter Methode.

# 2\. Grundlagen: LLM, Assistant, AI Agent und AI Harness

## 2.1 LLMs als probabilistische Textsysteme

Ein Large Language Model erzeugt Text, indem es auf Grundlage der bisherigen Eingabesequenz Wahrscheinlichkeiten für das nächste Token berechnet. Das ausgewählte Token wird Teil des Kontextes für die nächste Vorhersage. Dieser autoregressive Vorgang wird wiederholt, bis eine Ausgabe abgeschlossen ist.[^1]

Die Beschreibung als *Next Token Prediction* klingt einfacher, als das beobachtete Verhalten vermuten lässt. Durch umfangreiches Pre-Training können Modelle sprachliche, fachliche und formale Muster reproduzieren, Texte transformieren, Code erzeugen und komplexe Aufgaben bearbeiten. Dennoch bleibt die Ausgabe probabilistisch. Derselbe Prompt kann bei mehreren Durchläufen unterschiedliche Ergebnisse erzeugen. Eine plausible Formulierung ist daher nicht automatisch eine rekonstruierte Tatsache, und eine kohärente Begründung ist nicht automatisch ein Nachweis ihrer Richtigkeit.

Für die digitale Edition bedeutet dies: Ein Modell kann eine sehr überzeugende Transkription erzeugen, obwohl einzelne Zeichen falsch gelesen wurden. Es kann eine TEI-Struktur ausgeben, die formal plausibel aussieht, obwohl sie nicht den projektspezifischen Richtlinien entspricht. Die sprachliche Qualität einer Antwort darf deshalb nicht mit ihrer fachlichen Verlässlichkeit verwechselt werden.

## 2.2 Pre-Training, Post-Training und Assistant-Verhalten

Im Pre-Training werden umfangreiche Text- und andere Datenbestände verwendet, um statistische Repräsentationen sprachlicher und fachlicher Muster zu lernen. Vereinfacht kann man sagen, dass dabei modellintern nutzbare Zusammenhänge entstehen. Diese sind jedoch nicht wie Einträge in einer Datenbank adressierbar. Das Modell besitzt kein verlässliches Seiten- oder Quellenregister und kann seltene oder editionsspezifische Informationen falsch rekonstruieren.

Post-Training richtet das Modell stärker auf bestimmte Aufgaben-, Interaktions- und Verhaltensformen aus. Dazu gehören Instruction Tuning, Reinforcement Learning from Human Feedback und verwandte Verfahren. Ein Basismodell wird dadurch zu einem System, das typischerweise als hilfreicher Assistent antwortet, Anweisungen befolgt und bestimmte Sicherheits- oder Stilregeln berücksichtigt.

Die in einer Interaktion erscheinende Assistentenfigur ist nicht mit einem menschlichen Gegenüber gleichzusetzen.

Folie zur Unterscheidung zwischen Sprachmodell und Assistentenfigur

**Abbildung 3: Sprachmodell und Assistentenfigur.**  
*Die Folie unterscheidet das zugrunde liegende Modell von dem durch Post-Training, Systeminstruktionen und aktuellen Kontext stabilisierten Assistentenverhalten. Die anthropomorphe Form der Interaktion ist praktisch nützlich, darf aber nicht als Nachweis menschlicher Intentionalität oder fachlicher Autorität verstanden werden.* Sie ist ein durch Training, Systeminstruktionen und aktuellen Kontext stabilisiertes Verhaltensmuster. Das erklärt, warum sachliche, strukturierte Kommunikation häufig produktiv ist: Das Modell ist auf menschliche Kommunikationsformen ausgerichtet. Es erklärt zugleich, warum soziale Kohärenz nicht mit menschlicher Intentionalität oder fachlicher Autorität verwechselt werden darf.[^2]

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

# 3\. Prompt Engineering

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

## 3.6 Mechanistische Perspektive

Sprachliche Eingaben werden in hochdimensionale numerische Repräsentationen überführt. Unterschiedliche Formulierungen verändern die internen Aktivierungen, aus denen die Wahrscheinlichkeitsverteilung möglicher Ausgaben entsteht. Semantische und funktionale Beziehungen können sich in diesen Repräsentationen widerspiegeln.

Der Ausdruck *Latent Program Space* kann als Metapher

Didaktisches Modell von Prompt, Aktivierungspfad und Latent Program Space

**Abbildung 7: Didaktisches Modell der Promptwirkung.**  
*Die Darstellung veranschaulicht, dass eine Eingabe interne Repräsentationen und Verarbeitungspfade beeinflusst. Der „Latent Program Space“ ist dabei als konzeptionelle Metapher für gelernte Verarbeitungsroutinen zu lesen, nicht als klar abgegrenzter Speicher klassischer Programme.* für die Menge gelernter Verarbeitungsroutinen verstanden werden, die ein Modell abhängig von Eingabe und Kontext unterschiedlich aktiviert. Übersetzen, Zusammenfassen, Klassifizieren oder Erklären sind keine klar getrennten Programme im klassischen Sinn. Sie sind wiederkehrende Verhaltensmuster, die aus den Gewichten und dem aktuellen Aktivierungsverlauf entstehen.

Mechanistische Interpretierbarkeitsverfahren versuchen, Teile solcher internen Berechnungen zu rekonstruieren.

Folie mit Attribution Graph und Steuerung interner Aktivierungsrichtungen

**Abbildung 8: Partielle Rekonstruktion und experimentelle Steuerung interner Verarbeitung.**  
*Links wird ein Attribution Graph als partielle Rekonstruktion einer internen Berechnung gezeigt. Rechts verändert die Verstärkung bestimmter Aktivierungsrichtungen das beobachtete Verhalten. Die Beispiele stützen die Annahme systematischer interner Verarbeitung, liefern aber keine vollständige Erklärung natürlicher Promptwirkungen.* Attribution Graphs und verwandte Verfahren zeigen, dass bestimmte interne Strukturen und Aktivierungsrichtungen mit beobachtbarem Verhalten zusammenhängen können (Lindsey et al. 2025). Diese Befunde machen plausibel, dass unterschiedliche Prompts unterschiedliche Verarbeitungsverläufe begünstigen. Sie liefern jedoch noch keine vollständige Theorie, mit der sich natürliche Promptwirkungen zuverlässig vorhersagen lassen.

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

# 4\. Context Engineering

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

# 5\. Knowledge Engineering

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

# 6\. Agentic Engineering

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

# 7\. Promptotyping

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

## 7.7 Verification, Validation und Acceptance

Drei Ebenen müssen unterschieden werden.

**Abbildung 12: Prüfung, Evidenz und verantwortliche Acceptance.**  
*Deterministische Validation und agentisches Review liefern überprüfbare Evidenz. Die fachliche und wissenschaftliche Beurteilung verbleibt beim Critical Expert. Erst diese verantwortliche Prüfung kann zu einer zweckgebundenen Acceptance führen; technische Konformität allein autorisiert kein Forschungsartefakt.*

### Technische Verifikation

Prüft Konformität mit formalisierten Anforderungen:

- XML ist wohlgeformt;  
- TEI entspricht dem Schema;  
- Tests laufen erfolgreich;  
- Transformationen erzeugen die erwarteten Dateien;  
- Quelldateien wurden nicht verändert.

### Fachliche und wissenschaftliche Validierung

Prüft, ob Repräsentation und Artefakt für den vorgesehenen Forschungszweck angemessen sind:

- Entspricht die Transkription der Quelle?  
- Sind editorische Unsicherheiten angemessen repräsentiert?  
- Unterstützt das Interface die vorgesehenen Interpretationshandlungen?  
- Werden Modellierungsentscheidungen sichtbar oder irreführend naturalisiert?

### Acceptance

Bezeichnet die verantwortliche Entscheidung, einen identifizierbaren Projektzustand für einen benannten Zweck anzunehmen.

Ein technisch verifiziertes Artefakt kann wissenschaftlich ungeeignet sein. Umgekehrt kann ein wissenschaftlich interessanter Demonstrator technisch noch nicht publikationsreif sein. Acceptance muss deshalb zweckgebunden formuliert werden.

## 7.8 Critical Expert

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

## 7.11 Hands-on: Write-back und Acceptance dokumentieren

### Write-back

Analysieren Sie die Implementation und dokumentieren Sie:

- neue Erkenntnisse über die Quelle,  
- neue Anforderungen,  
- unzureichende Regeln,  
- offene fachliche Fragen,  
- notwendige Änderungen an Datenmodell oder Frontend.

### Acceptance Statement

\<a id="acceptance-statement-2"\>\</a\>

\# Acceptance Statement

\<a id="identifizierter-zustand"\>\</a\>

\#\# Identifizierter Zustand

\- Knowledge Base: Commit \`abc123\`

\- TEI-Daten: Version \`0.3\`

\- Frontend: Build \`2026-08-01\`

\- Schema: \`edition.rng\`, Version \`1.2\`

\<a id="accepted-for"\>\</a\>

\#\# Accepted for

Interner Demonstrator zur Prüfung des TEI-Modells und der synoptischen

Darstellung von Faksimile, diplomatischer Transkription und Normalisierung.

\<a id="technisch-verifiziert"\>\</a\>

\#\# Technisch verifiziert

\- XML-Wohlgeformtheit

\- Schema-Konformität

\- erfolgreiche lokale Transformation

\- unveränderte Quelldateien

\- Navigation zwischen den Beispielseiten

\<a id="fachlich-gepruft"\>\</a\>

\#\# Fachlich geprüft

\- Zuordnung von Faksimile und Transkription

\- Darstellung der markierten Unsicherheiten

\- Nachvollziehbarkeit editorischer Eingriffe

\<a id="nicht-nachgewiesen"\>\</a\>

\#\# Nicht nachgewiesen

\- vollständige philologische Verifikation des Korpus

\- Eignung für eine öffentliche oder zitierfähige Edition

\- Barrierefreiheit und produktive Langzeitverfügbarkeit

\<a id="offene-fragen"\>\</a\>

\#\# Offene Fragen

\- Unterscheidung zwischen teilweise lesbaren und ergänzten Eigennamen

\- Darstellung konkurrierender Normalisierungen

# 8\. Zusammenfassung und Begriffsübersicht

Die vier Engineering-Ebenen erfüllen unterschiedliche Funktionen:

| Ebene | Gegenstand | Leitfrage |
| :---- | :---- | :---- |
| Prompt Engineering | aktuelle Eingabesequenz | Wie wird die Aufgabe formuliert? |
| Knowledge Engineering | persistenter Wissensbestand | Was muss explizit dokumentiert und gepflegt werden? |
| Context Engineering | Informationszustand einer Aufgabe | Welche Informationen benötigt der Agent jetzt? |
| Agentic Engineering | mehrschrittige Ausführung | Wie wird die Arbeit organisiert, begrenzt und geprüft? |

Promptotyping verbindet diese Ebenen in einem iterativen Forschungsworkflow.

Die zentrale Formel lautet:

> **Prompt Engineering gestaltet die aktuelle Eingabesequenz.**  
> **Context Engineering organisiert den Informationszustand einer Aufgabe.**  
> **Knowledge Engineering baut und pflegt den dafür verfügbaren Wissensbestand.**  
> **Agentic Engineering organisiert die mehrschrittige Ausführung.**  
> **Promptotyping verbindet diese Ebenen in der iterativen Entwicklung und verantwortlichen Prüfung digitaler Forschungsartefakte.**

Die digitale Edition zeigt, warum diese Verbindung notwendig ist. Quelle, Transkription, Datenmodell, Transformation und Frontend bilden keinen neutralen technischen Ablauf. Jede Stufe enthält Entscheidungen darüber, welche Unterschiede sichtbar, bearbeitbar und interpretierbar werden. AI Agents können diese Arbeit erheblich unterstützen. Sie können jedoch die fachliche Verantwortung für Repräsentation, Validierung und Acceptance nicht übernehmen.

# 9\. Literaturverzeichnis

Anthropic. 2025\. “Claude’s Character.” Anthropic Research.

Anthropic. 2026\. “Claude’s Constitution.” Anthropic.

Battle, Rick, and Teja Gollapudi. 2024\. “The Unreasonable Effectiveness of Eccentric Automatic Prompts.” arXiv:2402.10949.

Hong, Kelly, Anton Troynikov, and Jeff Huber. 2025\. “Context Rot: How Increasing Input Tokens Impacts LLM Performance.” Chroma Research.

Hu, Tiancheng, and Nigel Collier. 2024\. “Quantifying the Persona Effect in LLM Simulations.” arXiv:2402.10811.

Li, Cheng, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, and Xing Xie. 2023\. “Large Language Models Understand and Can Be Enhanced by Emotional Stimuli.” arXiv:2307.11760.

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. 2025\. “On the Biology of a Large Language Model.” Transformer Circuits.

Mei, et al. 2025\. “Context Engineering for Large Language Models.” arXiv:2507.13334.

Pollin, Christopher. 2026\. “Asymmetric Amplification.” Digital Humanities Craft.

Pollin, Christopher. 2026\. “Promptotyping.” Manuskript in Vorbereitung.

Rajeev, Meghana, Rajkumar Ramamurthy, Prapti Trivedi, et al. 2025\. “Cats Confuse Reasoning LLM: Query Agnostic Adversarial Triggers for Reasoning Models.” arXiv:2503.01781.

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. 2024\. “The Prompt Report: A Systematic Survey of Prompting Techniques.” arXiv:2406.06608.

Yin, Ziqi, Hao Wang, Kaito Horio, Daisuke Kawahara, and Satoshi Sekine. 2024\. “Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance.” arXiv:2402.14531.

# 10\. Anhang: Vorlagen

## A. Vorlage für ein Wissensdokument

\---

document\_type: knowledge

status: draft

owner:

sources:

last\_reviewed:

\---

\<a id="gegenstand"\>\</a\>

\# Gegenstand

\<a id="zweck"\>\</a\>

\#\# Zweck

\<a id="begriffe-und-unterscheidungen"\>\</a\>

\#\# Begriffe und Unterscheidungen

\<a id="regeln"\>\</a\>

\#\# Regeln

\<a id="einschrankungen-und-ausnahmen"\>\</a\>

\#\# Einschränkungen und Ausnahmen

\<a id="unsicherheiten"\>\</a\>

\#\# Unsicherheiten

\<a id="offene-fragen-2"\>\</a\>

\#\# Offene Fragen

\<a id="quellen"\>\</a\>

\#\# Quellen

## B. Vorlage für eine Instruktionsdatei

\<a id="rolle-und-arbeitsmodus"\>\</a\>

\# Rolle und Arbeitsmodus

\<a id="projektstruktur"\>\</a\>

\# Projektstruktur

\<a id="verbindliche-arbeitsregeln"\>\</a\>

\# Verbindliche Arbeitsregeln

\<a id="werkzeuge-und-befehle"\>\</a\>

\# Werkzeuge und Befehle

\<a id="regeln-fur-ruckfragen-und-eskalation"\>\</a\>

\# Regeln für Rückfragen und Eskalation

\<a id="abschlusskriterien"\>\</a\>

\# Abschlusskriterien

\<a id="verweise-auf-wissensdokumente"\>\</a\>

\# Verweise auf Wissensdokumente

## C. Vorlage für einen Working Context

\<a id="aufgabe-2"\>\</a\>

\# Aufgabe

\<a id="relevante-anforderungen"\>\</a\>

\# Relevante Anforderungen

\<a id="bereitgestellte-wissensdokumente"\>\</a\>

\# Bereitgestellte Wissensdokumente

\<a id="ausgangsdateien-und-daten"\>\</a\>

\# Ausgangsdateien und Daten

\<a id="verfugbare-werkzeuge"\>\</a\>

\# Verfügbare Werkzeuge

\<a id="aktueller-projektzustand"\>\</a\>

\# Aktueller Projektzustand

\<a id="prufkriterien-2"\>\</a\>

\# Prüfkriterien

\<a id="bekannte-unsicherheiten"\>\</a\>

\# Bekannte Unsicherheiten

\<a id="bewusst-nicht-geladene-ressourcen"\>\</a\>

\# Bewusst nicht geladene Ressourcen

## D. Vorlage für einen Verification Report

\<a id="verification-report"\>\</a\>

\# Verification Report

\<a id="identifizierter-zustand-2"\>\</a\>

\#\# Identifizierter Zustand

\<a id="ausgefuhrte-technische-prufungen"\>\</a\>

\#\# Ausgeführte technische Prüfungen

\<a id="ergebnisse"\>\</a\>

\#\# Ergebnisse

\<a id="abweichungen"\>\</a\>

\#\# Abweichungen

\<a id="nicht-geprufte-aspekte"\>\</a\>

\#\# Nicht geprüfte Aspekte

\<a id="fachliche-fragen"\>\</a\>

\#\# Fachliche Fragen

\<a id="empfohlene-nachste-schritte"\>\</a\>

\#\# Empfohlene nächste Schritte

## E. Vorlage für ein Acceptance Statement

\<a id="acceptance-statement-3"\>\</a\>

\# Acceptance Statement

\<a id="identifizierter-zustand-3"\>\</a\>

\#\# Identifizierter Zustand

\<a id="accepted-for-2"\>\</a\>

\#\# Accepted for

\<a id="technisch-verifiziert-2"\>\</a\>

\#\# Technisch verifiziert

\<a id="fachlich-gepruft-2"\>\</a\>

\#\# Fachlich geprüft

\<a id="nicht-nachgewiesen-2"\>\</a\>

\#\# Nicht nachgewiesen

\<a id="offene-fragen-3"\>\</a\>

\#\# Offene Fragen

\<a id="verantwortliche-entscheidung"\>\</a\>

\#\# Verantwortliche Entscheidung  


[^1]: Die Beschreibung als Next Token Prediction ist eine funktionale Vereinfachung. Sie erklärt den unmittelbaren Generationsmechanismus, nicht die gesamte interne Verarbeitung eines Transformer-Modells.

[^2]: Für die Unterscheidung zwischen zugrunde liegendem Modell, Assistant-Verhalten und trainiertem Charakter sind insbesondere die Veröffentlichungen von Anthropic zu Claude’s Character und zur Constitution relevant. Die ontologische Interpretation dieser Begriffe bleibt jedoch umstritten.

[^3]: Produktbezeichnungen und konkrete Funktionen agentischer Arbeitsumgebungen verändern sich schnell. Die im Skriptum genannten Systeme dienen als Beispiele; Funktionsumfang und Terminologie sollten vor einer Publikation gegen die jeweils aktuelle Dokumentation geprüft werden.

[^4]: Die nominelle Kontextgröße ist nicht mit einer garantierten effektiven Nutzung aller enthaltenen Information gleichzusetzen. Forschung zu Long-Context-Systemen untersucht unter anderem Positions-, Distraktor- und Retrievaleffekte.

[^5]: MCP bezeichnet eine technische Spezifikation für die Verbindung von LLM-Anwendungen mit Werkzeugen und Datenquellen. Die konkrete Sicherheits- und Berechtigungsarchitektur hängt von der jeweiligen Implementation ab.