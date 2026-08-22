---
title: Understanding Large Language Models
module: 1
source-language: [de, en]
status: draft
created: 2026-08-20
units: [M1, M2, M3, M4, M5, M6]
canonical: false
canonical-gate: operator confirmation of the module cut
source-lecture-notes: [script/full-lecture-notes-de.md, script/full-lecture-notes-en.md]
---

# Module 1 — Understanding Large Language Models

> Draft cut of the Full Lecture Notes. Every passage below is reproduced verbatim from the Full
> Lecture Notes; only the module heading, the unit headings and the provenance lines are added.
> The Full Lecture Notes stay authoritative until the operator confirms the cut. Coverage, discarded
> parallel versions and open questions are recorded in `script/COVERAGE.md`.


## Unit M1 — Applied Generative AI in Research Data Workflows

*Source: `full-lecture-notes-de.md`, Abstract and "Zu diesem Skriptum".*

## Abstract

LLM-basierte AI Agents können computer- und datenbasierte Forschungsarbeit über einzelne Modellantworten hinaus unterstützen. Sie können Dateien untersuchen, Werkzeuge aufrufen, Programme ausführen, Zwischenergebnisse verarbeiten und digitale Forschungsartefakte über mehrere Schritte hinweg entwickeln. Ihre produktive Nutzung hängt jedoch nicht allein von der Leistungsfähigkeit eines Modells oder der Formulierung einzelner Prompts ab. Sie setzt voraus, dass relevantes Projektwissen explizit dokumentiert, für konkrete Aufgaben gezielt bereitgestellt und die daraus entstehende agentische Arbeit innerhalb einer technischen Umgebung organisiert, begrenzt und geprüft wird.

Das Skriptum unterscheidet dafür vier miteinander verbundene Arbeitsebenen. **Prompt Engineering** gestaltet die aktuelle Eingabesequenz. **Knowledge Engineering** baut und pflegt einen expliziten, inspizierbaren und revidierbaren Bestand von Projektwissen. **Context Engineering** stellt daraus und aus weiteren Ressourcen den Informationszustand zusammen, den ein Modell oder Agent für eine konkrete Aufgabe benötigt. **Agentic Engineering** organisiert die mehrschrittige Ausführung, in der ein Agent Dateien und Daten untersucht, Werkzeuge verwendet, Ergebnisse verarbeitet und auf dieser Grundlage weitere Handlungen auswählt. Ein **AI Harness** stellt dafür den technischen Zugriff auf Dateien, Werkzeuge und Ausführungsumgebungen sowie die Verwaltung von Zustand, Zugriffsrechten und Rückmeldungen bereit.

Diese Ebenen werden im **Promptotyping** als iterativer, dokumentenbasierter Forschungsworkflow verbunden. Eine fortschreibbare Project Knowledge Base hält den gegenwärtigen Stand des Projektwissens fest. Für einzelne Aufgaben werden daraus geeignete Working Contexts zusammengestellt. AI Agents erzeugen oder verändern auf dieser Grundlage digitale Forschungsartefakte. Erkenntnisse aus Exploration, Implementation und Prüfung werden anschließend in den dokumentierten Projektstand zurückgeführt.

Als durchgehendes Beispiel dient die Entwicklung eines kleinen Demonstrators für eine digitale Edition. Der Fall verbindet Datenerzeugung, Datenmodellierung, Transformation, Frontend-Darstellung, technische Verifikation und fachliche Validierung. Dadurch wird sichtbar, dass eine digitale Edition nicht allein aus einem Interface besteht. Sie umfasst die nachvollziehbare Verbindung von Quelle, erzeugten Daten, Datenmodell, Transformation, Darstellung und den Gründen ihrer zweckgebundenen Akzeptanz.

## Zu diesem Skriptum

Dieses Skriptum begleitet den gleichnamigen Foliensatz und folgt grundsätzlich dessen Dramaturgie. Die Folien verdichten Begriffe, Prozesse, Beispiele und Arbeitsaufträge visuell; die zugehörigen Kapitel erläutern die Argumentation, definieren zentrale Konzepte und dokumentieren die Hands-on-Übungen. Begriffe werden zunächst orientierend eingeführt und später an einer maßgeblichen Stelle vollständig ausgearbeitet. Wiederholungen erscheinen nur dort, wo sie für das Verständnis einer neuen Anwendung erforderlich sind. Quellen werden im Text durch Kurzbelege referenziert; vollständige Angaben stehen im Literaturverzeichnis. Ergänzende technische oder begriffliche Hinweise erscheinen in Fußnoten.

*Source: `full-lecture-notes-en.md`, "Applied Generative AI for Research Data Workflows".*

## **Applied Generative AI for Research Data Workflows**

**Applied Generative AI** refers here to the application and adaptation of generative AI methods and systems to domain specific problems, following the broader tradition of applied computer science. The focus is not primarily on developing new foundation models, but on integrating generative AI into existing knowledge practices and examining the methodological consequences of doing so.[^4]

Research data workflows provide a demanding field of application. Generative models can interpret and structure research material, transform data between representations, generate code for deterministic operations and operate inside AI harnesses that provide access to project files, tools and executable environments. Frontier models are particularly relevant because multimodality, reasoning, coding, tool use and agentic capabilities are increasingly combined within the same systems. This does not imply that frontier models are appropriate for every task. Smaller, specialised, local or open weight models may be more efficient, controllable or reproducible for particular purposes.

*Source: `full-lecture-notes-de.md`, sections 1.1 and 1.2.*

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

*Source: `full-lecture-notes-de.md`, sections 1.4 and 1.5.*

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


## Unit M2 — Research Data, Representation and Provenance

*Source: `full-lecture-notes-en.md`, "Humanities Research Data Are Constructed through Scholarly Workflows".*

## **Humanities Research Data Are Constructed through Scholarly Workflows**

**Research data** are analogue or digital representations of research objects, sources, observations or processes that are selected, collected, constructed or produced through scholarly work. They are shaped by research decisions and require sufficient documentation, context and preservation to support scholarly claims, critical assessment, reproducibility and reuse.[^5] In the humanities, this constructed character is especially visible because transcription, annotation, modelling and encoding make particular aspects of a source explicit while leaving others implicit.

A facsimile, a transcription and a TEI representation of the same historical document are therefore not interchangeable. Each is a different representation with different affordances and different forms of uncertainty. The Stefan Zweig notebook *Clarissa* illustrates how facsimile, descriptive metadata, collection context and later modelling together make the object computationally and scholarly usable.

**AI ready data** are data structured and documented for effective use in AI and machine learning workflows. This includes machine readable formats and metadata, clear provenance and usage conditions, and transparent information about quality, uncertainty and potential biases.[^6] AI readiness complements broader research data principles such as FAIR rather than replacing them.[^7]

*Source: `full-lecture-notes-en.md`, "Two AI Supported Research Data Workflows & Epistemic Infrastructures".*

## **Two AI Supported Research Data Workflows & Epistemic Infrastructures**

Two workflows provide recurring examples. The first processes multilingual printed sources associated with the writings of Jeanne Hersch. Scanned pages are transformed through OCR and layout analysis into structured representations, converted to TEI XML and enriched with information such as named entities and authority data. The second processes handwritten and typed material from the Stefan Zweig collection with multimodal foundation models for transcription and subsequent editorial curation.[^13]

Both workflows combine **probabilistic operations** with **deterministic operations**. A model may propose a transcription, classification or structured representation. Deterministic software can transform data, validate XML, execute tests or check numerical relations. Researchers can compare generated representations with sources, correct them and determine their editorial status.

The surrounding project environment is therefore an **epistemic infrastructure**. Files, project knowledge, schemas, tests, provenance information, model outputs and editorial decisions together establish the conditions under which a generated representation can be inspected, criticised, validated and accepted for a particular purpose.[^3]


## Unit M3 — The Current LLM Capability Landscape

*Source: `full-lecture-notes-en.md`, "Which Frontier Models and AI Technologies Do You Use?".*

## **Which Frontier Models and AI Technologies Do You Use?**

The contemporary LLM landscape contains several overlapping ecosystems. Hosted frontier systems are provided by companies such as Anthropic, OpenAI, Google and xAI. Other important model families include Mistral, Llama, DeepSeek, Qwen and Kimi. Open weight systems can additionally be executed on locally controlled infrastructure with environments such as Ollama or LM Studio. Because relative capabilities, speed and cost change rapidly, continuously updated comparative resources such as Artificial Analysis are useful for locating the current frontier.[^14]

Model choice should not be reduced to benchmark performance. Systems differ in capability, modalities, inference cost, latency, openness, deployment options, context capacity, tool use and the AI harnesses through which they can operate. Hosted proprietary services, open weight models and locally executed systems therefore represent different technical and governance arrangements.

AI harnesses form another layer of this landscape. Claude Code, Codex, Gemini CLI, Mistral Vibe, Qwen Code, Kimi Code, Pi and Cursor connect models with files, tools, state and executable environments. The effective AI system is increasingly a compound system rather than a model considered in isolation.[^12]


## Unit M4 — Asymmetric Amplification and the Capability Frontier

*Source: `full-lecture-notes-en.md`, "Frontier LLMs Asymmetrically Amplify Computational Research".*

## **Frontier LLMs Asymmetrically Amplify Computational Research**

Frontier AI companies increasingly describe research automation as a strategic objective. Jakub Pachocki has publicly described automating research as a major goal at OpenAI, while Dario Amodei has used the image of “geniuses in a data center”. Such statements are not evidence that research has been automated. They indicate, however, the direction in which leading laboratories are attempting to extend model capability.[^15]

Several heterogeneous evaluations show substantial progress in capabilities relevant to computational research. METR measures the duration of software tasks that agents can complete at specified levels of reliability. ARC AGI probes adaptation to unfamiliar tasks. FrontierMath and formal theorem proving examine mathematical reasoning in settings where at least parts of an output can be checked externally. Cyber evaluations probe software understanding, exploration, planning and tool use in executable environments. These evaluations measure different things and should not be collapsed into one scale of intelligence.[^16]

I describe the practical effect as **asymmetric amplification**. Frontier LLMs particularly amplify work where relevant information is digitally represented, actions can be executed through software and the environment can return useful feedback. Coding, data transformation, formal modelling and many computational research workflows have these properties. The effect is asymmetric because it depends on existing expertise, accessible data, technical infrastructure and the ability to assess outputs. The same model can therefore amplify an experienced developer or computational researcher much more strongly than someone working without structured knowledge, tools or evaluative criteria.[^17]


## Unit M5 — What an LLM Is: Jagged Capability, Latent Program Space, Assistant Character

*Source: `full-lecture-notes-en.md`, "LLMs as Jagged Alien Intelligences" through "Embeddings and Contextual Representations".*

## **LLMs as Jagged Alien “Intelligences”**

The metaphor of **jagged alien intelligence** describes an unfamiliar capability profile rather than consciousness or human like understanding. Frontier LLMs can perform extremely difficult tasks while failing on neighbouring tasks that appear simple to human observers. Their competence is therefore powerful, uneven and difficult to extrapolate.[^18]

Several model properties contribute to this profile. Outputs are probabilistic and can contain plausible but unsupported claims. Models can reproduce biases and display **sycophancy**, a tendency to align an answer with the user’s expressed belief even when this reduces factual reliability. Their internal computations are only partially understood. At the same time, contemporary systems can use tools, work with large contexts, generate and execute code and allocate additional inference time computation to difficult tasks.

Mechanistic interpretability research indicates that model behaviour can depend on structured internal computational pathways that differ substantially from familiar human procedures.[^19] This motivates a theoretical perspective developed later in these notes. LLMs can be understood not only as next token predictors, but also as systems in which training has produced a repertoire of learned transformations or **vector programs**.

## **How Large Language Models Work**

For a more extensive visual introduction, see *Wie LLMs funktionieren*.[^20]

A **large language model** is a neural network trained on very large collections of tokenised data to predict how a sequence continues. In an autoregressive language model, the model estimates a probability distribution over possible next tokens conditioned on the tokens already available in its context. A selected token becomes part of the sequence and therefore influences the next prediction.[^21]

The crucial distinction is that the **training objective is not identical to the capabilities acquired during training**. Next token prediction describes the optimisation problem used in autoregressive language modelling. To perform that objective well across heterogeneous data, the model learns representations and transformations associated with syntax, concepts, relations, styles, code and recurring patterns of reasoning. These structures can subsequently support generation, translation, classification, coding, analysis and reasoning without a separate manually written program for every task.[^21]

The basic objective also does not directly ask whether a proposition is true. It asks which continuation is probable given the available context. Yoshua Bengio uses this distinction to contrast ordinary autoregressive language modelling with his proposed *Scientist AI*, which would explicitly estimate probabilities for hypotheses about the world.[^22] Human generated language contains extensive information about the world, so language modelling can still produce broad world representations. The narrower point is that truth is not identical to the next token objective.

## **Transformer Architecture**

Most contemporary LLMs are based on the **Transformer architecture**. A Transformer processes token representations through repeated layers in which attention mechanisms allow information at different positions in the sequence to influence one another.[^23]

A simple next token diagram such as `cat sat on a → mat` illustrates the output objective, but the probability assigned to `mat` results from transformations across many layers and high dimensional representations. **Self attention** allows the model to construct context dependent representations rather than treating every token independently.

This connection matters for the later engineering chapters. Prompts and context alter the token sequence supplied to the model. That sequence conditions the distributed computation through which the model produces subsequent tokens. Prompting is therefore an intervention on the model’s current computation, not merely a textual wrapper around an otherwise fixed answer.

## **Pretraining and Posttraining**

During **pretraining**, a model learns statistical structure from large and heterogeneous corpora. This process creates broad linguistic, conceptual and procedural representations and can support many capabilities that were not separately programmed.[^21] It is sometimes useful to describe pretraining as building a broad repertoire of knowledge and capabilities, but this remains a simplification because knowledge and capability are entangled throughout model training.

**Posttraining** shapes how that repertoire is expressed in an assistant. Instruction tuning, demonstrations, preference learning, reinforcement learning and related methods can stabilise instruction following, behavioural tendencies and interface specific capabilities.[^24] Contemporary development pipelines may also include intermediate stages between broad pretraining and later alignment training. The boundaries and terminology differ across laboratories and papers.

A useful high level distinction is therefore:

`training → changes model parameters`

`inference → uses the trained parameters for a current interaction`

Ordinary inference does not normally update the model weights. The model can nevertheless adapt strongly to examples, instructions and information supplied in its current context.

## **The Shape of a Wikipedia Article About Zebras**

An LLM does not normally retrieve an addressable copy of a training document when it answers a question. Training changes model parameters so that statistical structure from training data influences later generation. Andrej Karpathy has described this metaphorically as a form of lossy compression. What remains is not the original document but a learned statistical structure that can contribute to later outputs.[^25]

This distinction is important for **parametric knowledge**. A model may produce an accurate description of zebras because its parameters encode patterns learned from relevant material. It cannot thereby provide direct provenance for every generated claim or reconstruct the exact source from which a statement was learned.

Tool use changes the situation. Web search, retrieval systems, files and databases can obtain external information and make selected representations of it available during inference. Three information layers should therefore be distinguished:

`model parameters → learned representations`

`external resources → retrievable information`

`current context → information available for this inference`

The boundary of the model is therefore not the boundary of the complete AI system.

## **Tokenization**

LLMs do not directly process text as semantic words. A **tokenizer** converts character sequences into discrete units called **tokens**. Depending on the tokenizer, one token may correspond to a word, part of a word, punctuation or another recurring sequence. Each token is mapped to a numerical identifier before it enters the neural network.[^26]

Tokenisation is partly an engineering decision. A useful tokenizer balances vocabulary size, sequence length and the ability to represent previously unseen strings. The boundaries it creates are not necessarily linguistically intuitive. A long word may consist of several tokens while a short, frequent sequence may be represented by one token.

The practical consequence is that context windows, input costs and output lengths are measured in tokens rather than words or characters. Tokenisation therefore determines the discrete sequence over which model computation and context limits operate.

## **Embeddings and Contextual Representations**

Tokens are converted from discrete identifiers into continuous numerical representations. **Embeddings** provide the initial mapping into a high dimensional vector space. During training, systematic relations can emerge among representations associated with recurring linguistic and conceptual patterns.[^23]

The familiar illustration in which `dog` and `cat` appear closer than `dog` and `stone` provides a useful first intuition, but it is not a complete account of meaning. Initial embeddings are transformed repeatedly across the network, producing **contextual representations** that depend on surrounding tokens and the current task.

A sentence written in Shakespearean English and a semantically similar sentence written in contemporary English can therefore condition different internal representations and activation patterns. This helps explain why wording matters without assuming that the model stores one fixed meaning for each token. Prompting provides a structured pattern of tokens that participates in selecting and combining learned computations.

*Source: `full-lecture-notes-en.md`, "Prompt Engineering: Finding Coordinates in a Latent Program Space" and the mechanistic-interpretability excursus.*

## **Prompt Engineering: Finding Coordinates in a Latent Program Space**

These lecture notes adopt a theoretical model inspired particularly by François Chollet’s account of LLM prompting.[^27] The central claim is that an LLM can be understood as containing a large repertoire of **learned computational transformations**, and that prompts act partly as signals that select and combine these transformations.

The terminology used here is:

* **Vector Program**: a learned transformation that realises a capability or behaviour
* **Latent Program Space**: the space of possible learned transformations
* **Program Query**: an address or search signal within that space
* **Prompt Engineering**: external search for an effective address
* **Reasoning / Test Time Compute**: internal search for an effective computation

A Vector Program is not a conventional symbolic program stored as a discrete object inside the model. It is a distributed transformation implemented through high dimensional representations and model parameters. The thesis is nevertheless stronger than a purely rhetorical metaphor. It proposes that useful model behaviours correspond to learned computational structures that can be differentially elicited through prompts and context.

For the transcription example, a Program Query may condition and combine transformations associated with visual recognition, historical language, layout, reading order, document structure and diplomatic transcription policy. Iterative Prompt Engineering is then an external search process in which the user varies the query and evaluates the resulting behaviour.

## **Excursus: Mechanistic Interpretability and Activation Paths**

**Mechanistic interpretability** investigates the internal computations through which neural networks produce behaviour. Attribution graph research has reconstructed partial internal pathways associated with multi step computations, including arithmetic and linguistic processing.[^19]

Related work by Sofroniew and colleagues identifies internal representations associated with concepts described as emotional states. Intervening on vectors associated with concepts such as *desperate* or *calm* can causally alter subsequent model behaviour.[^31]

These findings do not provide a complete empirical map of a Latent Program Space. They do, however, support several elements of the theoretical account. Internal computation is structured rather than undifferentiated, different pathways can contribute to different behaviours, and interventions on representations can change outputs systematically. The Latent Program Space thesis generalises from such findings to an account of how learned computational possibilities may be addressed through prompts and context.

*Source: `full-lecture-notes-en.md`, "Training Builds and Shapes the Latent Program Space" through the assistant-character sections.*

## **Training Builds and Shapes the Latent Program Space**

The Latent Program Space is not explicitly hand designed. It develops through several stages of training.

**Pretraining** establishes a broad repertoire of representations, capabilities and behavioural patterns from language, knowledge, code and other training material.[^21] **Model Spec Midtraining** is a recently proposed technique in which, after broad pretraining but before later alignment training, a model is trained on synthetic documents that discuss a Model Spec or Constitution. The objective is to influence how subsequent alignment training generalises.[^32] Midtraining is therefore a useful category here, but it is not a universally standardised phase across all model providers.

**Posttraining** shapes how the learned repertoire is expressed in an assistant. Demonstrations, preference learning, reinforcement learning and related methods can stabilise instruction following, behavioural tendencies and interface specific capabilities such as tool calling.[^24]

At **inference** time, prompts and context condition and combine parts of the trained repertoire for a particular task. An **AI Harness** extends the effective system by providing tools, state, feedback, permissions and control for agentic work.[^12]

## **The Assistant Is a Character Generated by the Model**

The **Assistant** encountered in a conversational interface should not simply be equated with the underlying neural network. Providers shape assistant behaviour through training, runtime instructions, policy layers and product design. Anthropic provides an unusually explicit example because it describes Claude in terms of a cultivated **character** and publishes a Constitution that states intended values and behavioural dispositions.[^33]

These notes use the distinction as an ontological and practical working model. The model can represent and generate many possible styles and behavioural patterns. “Claude” refers to a particular assistant character that Anthropic attempts to strengthen and stabilise through training and system design. This formulation follows Anthropic’s own public account, while remaining neutral about stronger claims concerning consciousness or subjective experience.[^33]

Models are extensively trained on human communication and can therefore generate convincing social behaviour. Clear and constructive communication can improve interaction, but social fluency, confidence and empathy are not evidence that the system is a human interlocutor or that its claims are correct.

## **How Anthropic Shapes Claude’s Assistant Character**

Anthropic’s **Claude Constitution** is a public description of the values and behaviour the company aims to cultivate in Claude. It is not simply a runtime system prompt. Anthropic states that the Constitution is used at various stages of training and can be used to construct synthetic data, responses and rankings for future training.[^34]

This distinction separates three layers. **Training artefacts**, such as a Constitution or Model Spec, can shape what is learned during model development. **Character training and posttraining** can stabilise behavioural tendencies and assistant dispositions. **System prompts** operate at runtime and provide instructions within a particular deployment context.[^35]

Claude’s behaviour is therefore produced by the interaction between trained model parameters and current runtime context. The Constitution, character training and system prompt are related, but they are not technically the same thing.


## Unit M6 — The Four Engineering Layers

*Source: `full-lecture-notes-de.md`, section 1.3.*

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


## Notes

*Footnote identifiers and definitions are reproduced unchanged from their source lecture notes.*

### Notes carried from the English Full Lecture Notes

[^3]: Christopher Pollin, *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*, review draft 0.9, 2026.

[^4]: The term *Applied Generative AI* is used here for domain specific application and adaptation of generative AI, following the framing developed in teaching and AGKI DH activities by Christopher Pollin.

[^5]: Philipp Geiger, “Daten / Forschungsdaten,” 2024, https://doi.org/10.17175/wp_2023_003_v2. See also Johanna Drucker, “Humanities Approaches to Graphical Display,” *Digital Humanities Quarterly* 5, no. 1, 2011.

[^6]: Majithia et al., “An Actionable Framework for AI Ready Data,” 2026, https://doi.org/10.1002/aaai.70054.

[^7]: Mark D. Wilkinson et al., “The FAIR Guiding Principles for Scientific Data Management and Stewardship,” *Scientific Data* 3, 2016, https://doi.org/10.1038/sdata.2016.18.

[^12]: Hailin Zhong and Shengxin Zhu, “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents,” 2026, https://doi.org/10.48550/arXiv.2605.13357.

[^13]: Jeanne Hersch workflow, https://chpollin.github.io/zbz-ocr-tei and https://github.com/chpollin/zbz-ocr-tei. Stefan Zweig workflow, https://chpollin.github.io/szd-htr-ocr-pipeline and https://github.com/chpollin/szd-htr-ocr-pipeline.

[^14]: Artificial Analysis, https://artificialanalysis.ai.

[^15]: See the sources collected on the corresponding lecture slide and Pollin, “Asymmetric Amplification,” 2026, https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

[^16]: METR, https://metr.org/time-horizons; ARC Prize, https://arcprize.org/leaderboard; SimpleBench, https://simple-bench.com; Humanity’s Last Exam, https://lastexam.ai; Epoch AI FrontierMath, https://epoch.ai/frontiermath.

[^17]: Christopher Pollin, “Asymmetric Amplification,” 2026, https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

[^18]: Fabrizio Dell’Acqua et al., “Navigating the Jagged Technological Frontier,” *Organization Science* 37, no. 2, 2026, https://doi.org/10.1287/orsc.2025.21838; Joshua Gans, “A Model of Artificial Jagged Intelligence,” 2026, https://doi.org/10.48550/arXiv.2601.07573; Christopher Summerfield, *These Strange New Minds*, 2025.

[^19]: Jack Lindsey et al., “On the Biology of a Large Language Model,” Transformer Circuits, 2025, https://transformer-circuits.pub/2025/attribution-graphs/biology.html.

[^20]: Christopher Pollin, *Wie LLMs funktionieren*, YouTube, 2026, https://youtu.be/u4RRxi5tgTA.

[^21]: Tom B. Brown et al., “Language Models are Few Shot Learners,” 2020, https://arxiv.org/abs/2005.14165. For the Transformer architecture see Vaswani et al. 2017.

[^22]: Yoshua Bengio, “Godfather of AI: How To Make Safe Superintelligent AI,” interview with Rob Wiblin, *80,000 Hours*, 2026, https://youtu.be/PZqDFs2sbiY.

[^23]: Ashish Vaswani et al., “Attention Is All You Need,” 2017, https://arxiv.org/abs/1706.03762.

[^24]: Long Ouyang et al., “Training Language Models to Follow Instructions with Human Feedback,” 2022, https://arxiv.org/abs/2203.02155. See also Anthropic’s work on Constitutional AI and Claude’s Character.

[^25]: Andrej Karpathy, *Intro to Large Language Models*, 2023, https://www.youtube.com/watch?v=zjkBMFhNj_g. The compression language is a didactic analogy, not a literal model of parameter storage.

[^26]: For subword tokenisation see Rico Sennrich, Barry Haddow, and Alexandra Birch, “Neural Machine Translation of Rare Words with Subword Units,” 2016, https://arxiv.org/abs/1508.07909.

[^27]: François Chollet, “How I Think About LLM Prompt Engineering,” 2023, https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering.

[^31]: Nicholas Sofroniew et al., “Emotion Concepts and Their Function in a Large Language Model,” 2026, https://transformer-circuits.pub/2026/emotions/index.html.

[^32]: Chloe Li, Nevan Wichers, Sara Price, Samuel Marks, and Jon Kutasov, “Model Spec Midtraining: Improving How Alignment Training Generalizes,” 2026, https://arxiv.org/abs/2605.02087.

[^33]: Anthropic, “Claude’s Character,” https://www.anthropic.com/research/claude-character; Anthropic, “Claude’s Constitution,” 2026, https://www.anthropic.com/constitution.

[^34]: Anthropic, “Claude’s New Constitution,” 2026, https://www.anthropic.com/research/claude-new-constitution.

[^35]: Anthropic, “System Prompts,” https://platform.claude.com/docs/en/release-notes/system-prompts; Anthropic, “Claude’s New Constitution,” 2026.
