# Full Slide Deck

Slide-text export of the Google deck of the teaching line, state of 2026-08-20. Everything below this header is the export as produced and carries no editorial changes.

Knowledge, Context and Agentic Engineering for Knowledge Work

Full Slidedeck. September 2026.


Dr. Christopher Pollin MA MA
Digital Humanities Craft OGwww.dhcraft.org | office@dhcraft.org 
Slides were generated AI-assisted. Images are partly AI-generated.
Knowledge Engineering, Context Engineering und Agentic Engineering bezeichnen drei miteinander verbundene Ebenen der Arbeit mit LLM-basierten AI Agents.

Knowledge Engineering betrifft den Aufbau und die Pflege expliziten, revidierbaren Projektwissens. Dazu gehören Forschungsdaten, Dokumentationen, Anforderungen, Designentscheidungen und Prozesswissen ebenso wie Wissen, das zunächst nur implizit bei einzelnen Expert:innen oder innerhalb einer Organisation vorhanden ist. Dieses Wissen wird in einer Form festgehalten, in der es gelesen, überprüft, ergänzt und korrigiert werden kann. Im Promptotyping bildet eine fortschreibbare und versionierte Wissensbasis aus Markdown-Dokumenten die zentrale Struktur, die Forschungsdaten, Domänenwissen, Anforderungen, Implementierung und Verifikation miteinander verbindet.

Context Engineering betrifft nicht den gesamten Wissensbestand, sondern den Informationszustand einer konkreten Aufgabe. Es bestimmt, welche Informationen, Anweisungen, Werkzeuge und Beispiele zu einem bestimmten Zeitpunkt im Kontextfenster eines Modells verfügbar sind, in welcher Reihenfolge sie bereitgestellt werden und was bewusst nicht geladen wird. Prompt Engineering konzentriert sich demgegenüber enger auf die Gestaltung einer einzelnen Eingabesequenz. Context Engineering organisiert den aufgabenrelevanten Ausschnitt aus einem größeren Wissensbestand über einen längeren Arbeitsverlauf.

Agentic Engineering betrifft die Organisation und Kontrolle mehrschrittiger Arbeit, in der LLM-basierte Agents nicht nur Text erzeugen, sondern innerhalb einer Projektumgebung auf Wissens- und Softwareartefakte einwirken. Sie können Dateien lesen und bearbeiten, Datenbeschreibungen und Anforderungen auswerten, Code erzeugen, Programme ausführen, Ergebnisse prüfen und ihre Arbeit auf Grundlage von Rückmeldungen überarbeiten. Der Begriff ist deshalb weiter als agentische Softwareentwicklung: Die Arbeit richtet sich nicht nur auf Code, sondern auch auf Datenbeschreibungen, Spezifikationen, Mappings, Designentscheidungen, Prozessdokumente und Verifikationskonzepte.

Die drei Ebenen erfüllen unterschiedliche Funktionen. Knowledge Engineering organisiert den verfügbaren Wissensbestand. Context Engineering stellt daraus den für eine Aufgabe relevanten Ausschnitt bereit. Agentic Engineering organisiert, wie ein Agent mit diesem Kontext innerhalb einer technischen Umgebung handelt. Ein AI Harness stellt dafür den Zugriff auf Dateien, Werkzeuge und Ausführungsumgebungen sowie die Verwaltung von Zustand, Zugriffsrechten und Rückmeldungen bereit. Das Harness entscheidet jedoch nicht selbst, welches Projektwissen relevant oder wissenschaftlich angemessen ist.

Im Promptotyping werden diese Ebenen in einem iterativen Arbeitsprozess verbunden. Der Agent arbeitet aus einer gepflegten Projektwissensbasis, erzeugt oder verändert digitale Forschungsartefakte und schreibt Erkenntnisse aus Exploration, Implementierung und Prüfung in den Wissensbestand zurück. Dadurch entwickeln sich das dokumentierte Projektverständnis und das daraus erzeugte Artefakt gemeinsam weiter.

Diese Struktur automatisiert keine neutrale Übersetzung von Forschungsdaten in Software. Sie macht vielmehr jenen Teil der Übersetzung explizit, der formuliert, dokumentiert und geprüft werden kann. Die Verantwortung für die Interpretation der Daten, die fachliche Angemessenheit der Modellierung und die Akzeptanz eines digitalen Forschungsartefakts verbleibt bei den für die Forschung verantwortlichen Personen.


Prompt Engineering 
Prompt Engineering is the iterative design and evaluation of instructions for a specific model and task.
Shift in focus: Prompt → Context Engineering
Prompting Strategies: There Is No Prompt to Rule Them All
What prompting really is !?Finding Coordinates in a Latent Program Space
Schulhoff et al. The Prompt Report: A Systematic Survey of Prompting Techniques. 2024.
https://doi.org/10.48550/arXiv.2406.06608 

Knowledge & Context Engineering 
A defintion knowledge 
A definition context engineer
 → 
→
literatur


https://www.youtube.com/watch?v=FgaBdwSvOGM 

Skriptum:  https://docs.google.com/document/d/1yYEGgC2R8CDnkqqh8z6ApKfQYSETsYyez2vxwPHK8_k/edit?usp=sharing 

Computer- und datenbasierte Forschungsarbeit wird durch Frontier-LLMs asymmetrisch amplifiziert
“The big goal that we are working towards is automating research”	- Jakub Pachocki (OpenAI’s chief scientist)“Geniuses in a data center” 	- Dario Amodei (CEO Anthropic)
Benchmarks
https://simple-bench.com
https://arcprize.org/leaderboard
https://lastexam.ai
https://epoch.ai/frontiermath
… 
https://metr.org/time-horizons

Lernziele
Die Grundlagen und Möglichkeiten des Context- und Agentic Engineering verstehen und nutzen.
Wissen für die Arbeit mit LLMs und AI Agents aufbereiten und nutzbar machen.
Agentenunterstützte Workflows gestalten, umsetzen und evaluieren.
Ablauf
todo

Zentrale Begriffe für die Arbeit mit AI Agents
AI AgentLLM-basiertes System für mehrschrittige, werkzeuggestützte Aufgabenausführung
Agentic EngineeringOrganisation und Kontrolle mehrschrittiger agentischer Arbeit
AI HarnessTechnische Umgebung, in der AI Agents Kontext erhalten, Werkzeuge nutzen, Aufgaben ausführen und Rückmeldung verarbeiten

Knowledge EngineeringAufbau und Pflege expliziten, revidierbaren Projektwissens
Prompt EngineeringIterative Gestaltung und Optimierung von Prompts
Context EngineeringAuswahl, Organisation und Bereitstellung aufgabenrelevanter Informationen im Kontextfenster eines LLMs

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, Chenglei Si, Yinheng Li et al. 2024. “The Prompt Report: A Systematic Survey of Prompting Techniques.”
https://doi.org/10.48550/arXiv.2406.06608 
Mei, Lingrui et al. 2025. “A Survey of Context Engineering for Large Language Models.”
https://doi.org/10.48550/arXiv.2507.13334 
Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. 2026. “AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications, and Challenges.” Information Fusion 126: 103599.
https://doi.org/10.1016/j.inffus.2025.103599 
Zhong, Hailin, and Shengxin Zhu. 2026. “AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents.”
https://doi.org/10.48550/arXiv.2605.13357 
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. 

AI Harness
Technische Software-Schicht, über die ein LLM-basierter AI Agent Kontext erhält, Werkzeuge aufruft, Aktionen in einer Arbeitsumgebung ausführt und Rückmeldung verarbeitet. Das Harness verwaltet dabei Zustand, Zugriffsrechte und Kontrollfluss. 
Beispiele sind Claude Code, Codex, Cursor oder Pi) 
Zhong, Hailin, and Shengxin Zhu. 2026. “AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents.”
https://doi.org/10.48550/arXiv.2605.13357 
Schematische Darstellung eines AI Harness. Erzeugt mit ChatGPT Images 2.0.

Claude Code

RQ4: Are measured intelligence, self-estimated intelligence, and implicit theories of intelligence able to predict statistically significant variance in the acceptance of “active” or “passive” enhancement methods in addition to personality traits (Big Five, Dark Triad, vulnerable narcissism)?
Kontext
Daten
LLM-gestützte Exploration und Analyse von Forschungsdaten
Grinschgl, S., Berdnik, A. L., Stehling, E., Hofer, G., & Neubauer, A. C. (2023). Who Wants to Enhance Their Cognitive Abilities? Potential Predictors of the Acceptance of Cognitive Enhancement. Journal of Intelligence, 11(6), 109. https://doi.org/10.3390/jintelligence11060109

Aggregated test data and the codebook: https://osf.io/2s3ze 
Pre-registration at https://osf.io/urwxt 
Codebook
Paper
Forschungsfrage und Auftrag


Projekt vorbereiten: Quellen, Files und AI-Agent Loops 
Erstelle im aktuellen Verzeichnis ein Projekt mit dieser Struktur:

hands-on-01-forschungsdatenanalyse/
├── data/
├── context/
├── task/
├── scripts/
├── outputs/
└── report/

Recherchiere anschließend die folgenden Ressourcen:

 * Aggregated test data and the codebook: https://osf.io/2s3ze * Pre-registration: https://osf.io/urwxt 

Lade die relevanten Dateien herunter und lege sie passend unter `data/` beziehungsweise `context/` ab.

Erstelle außerdem `task/quellen.md` mit:
 * Titel und Funktion jeder Datei,
 * ursprünglicher URL,
 * Dateiformat,
 * kurzer Begründung der Zuordnung.

Verändere die heruntergeladenen Quelldateien nicht.
Zeige abschließend die angelegte Projektstruktur.
Tool Use
Loop
Files
└─────────── AI HARNESS ────────┘
1. Preparation
Diese erste Phase ist die Preparation. Bevor der Agent etwas analysiert oder implementiert, wird zunächst ein belastbarer Projektbestand hergestellt.
Im Prompt geben wir nicht jede einzelne Handlung vor. Wir formulieren ein Ziel: Der Agent soll eine Projektstruktur anlegen, die relevanten Quellen recherchieren, die Dateien herunterladen und sie sinnvoll einordnen. Dabei arbeitet er nicht nur im Chat, sondern innerhalb eines AI Harness – also einer technischen Umgebung, die ihm Zugriff auf Dateien, Webzugriff, Terminal und weitere Werkzeuge gibt.
Auf der rechten Seite sehen wir mehrere zentrale Elemente agentischer Arbeit. Über Files nimmt der Agent den bestehenden Projektzustand wahr und verändert ihn. Durch Tool Use greift er auf Webressourcen und die lokale Projektumgebung zu. Diese Schritte laufen nicht einmalig ab, sondern in einem AI-Agent Loop: Der Agent prüft den aktuellen Zustand, wählt eine Handlung, führt ein Werkzeug aus, verarbeitet das Ergebnis und entscheidet über den nächsten Schritt.
Das Ergebnis dieser Phase ist daher nicht bloß eine Antwort im Chat. Es entsteht ein persistenter und nachvollziehbarer Projektbestand: Forschungsdaten, Codebook und Präregistrierung liegen strukturiert vor, ihre Herkunft wird dokumentiert, und die Quelldateien bleiben unverändert.
Methodisch ist das wichtig, weil die spätere Arbeit nicht bei null beginnt. Alle weiteren Schritte bauen auf diesem vorbereiteten Bestand auf. Preparation bedeutet hier also: Quellen und Arbeitsumgebung so einzurichten, dass der Agent kontrolliert, nachvollziehbar und wiederholbar weiterarbeiten kann.


Vorgehen planen: Daten verstehen und Möglichkeiten abwägen 
2. Planning
Untersuche die Forschungsdaten und die zugehörigen Kontextquellen.

Entwickle zunächst ein konzeptionelles Vorgehen für ein lokales, statisches Webtool zur sicheren Exploration der ursprünglichen Daten.

Erstelle das Tool, führe es lokal im Browser aus und prüfe die zentralen Funktionen. Verändere die Quelldateien nicht.

Erstelle einen sehr kompakten Plan. Erkläre alles in einfacher Sprache, ohne Komplexität zu verlieren.

hands-on-01-forschungsdatenanalyse/├── context/│   ├── Enhancement_Analyses_Syntax_shareable.sps   (13.374 Bytes)│   ├── Enhancement_Codebook.pdf                    (261.011 Bytes)│   └── Preregistration_urwxt_OSF-API.json          (33.385 Bytes)├── data/│   ├── Enhancement_Data_SPSS_shareable.sav         (58.316 Bytes)│   └── Enhancement_Data_SPSS_shareable.xlsx        (72.063 Bytes)├── outputs/                                        (leer)├── report/                                         (leer)├── scripts/                                        (leer)└── task/    └── quellen.md
Konzeption vor Implementierung 
Lokales, statisches Webtool im Browser 
Kompakter Plan in einfacher Sprache 

Zielbild präzisieren: Rückfragen, Feedback und iterative Überarbeitung 
Lies den Projektbestand und deinen bisherigen Plan.

Stelle mir gezielte Rückfragen, damit du das gewünschte Endergebnis, die Nutzungssituation und die fachlichen Anforderungen möglichst genau verstehst.

Frage nach allem, was sich nicht zuverlässig aus den vorhandenen Dateien ableiten lässt. **Triff keine stillen Annahmen.**

Nutze mein Feedback, um die Anforderungen und den Plan schrittweise zu überarbeiten.

Fasse nach jeder Runde kurz zusammen, was du verstanden und geändert hast.
3. Feedback & Self Revision

Webtool umsetzen: Plan ausführen und ein funktionierendes Artefakt erzeugen 
Setze den überarbeiteten Plan um.

Erstelle ein lokales, statisches Webtool zur Exploration der Forschungsdaten.

Nutze die vorhandenen Daten und Kontextquellen, verändere die Quelldateien nicht und dokumentiere wichtige technische Entscheidungen.

Öffne das Tool im Browser und behebe auftretende Fehler.
4. Implementation

Ergebnis prüfen: Funktionen, Datenverarbeitung und Übereinstimmung mit den Anforderungen
Prüfe das erzeugte Webtool systematisch.

Kontrolliere:
- ob es lokal im Browser funktioniert,
- ob die Daten korrekt eingelesen und dargestellt werden,
- ob die vereinbarten Anforderungen umgesetzt sind,
- ob die Quelldateien unverändert geblieben sind.

Dokumentiere gefundene Fehler, behebe technische Probleme und fasse die Prüfergebnisse kompakt zusammen.
5. Verification

Context Engineering 
Context Engineering umfasst die systematische Auswahl, Organisation, Pflege und Bereitstellung der Informationen, die ein LLM-basiertes System für seine Arbeit benötigt.

Context Engineering

Model Context Window = 8K
A context window, in the context of large language models (LLMs), refers to the portion of text that the model can consider at once when generating or analyzing language.[...]
Model Context Window = 8K
A context window, in the context of large language models (LLMs), refers to the portion of text that the model can consider at once when generating or analyzing language. It is essentially the window through which the model "sees" and processes text, helping it understand the current context to make predictions, generate coherent sentences, or provide relevant responses.[...]
6000 Token
Input Token
Output Token
Lorem ipsum … 
Lorem ipsum … 
1500 Token
Context Window = 6000 + 1500 < 8000
Context Window = 10000 + 1500 > 80003500 tokens are not in the context window!
What is a Context Window? Unlocking LLM Secrets. https://youtu.be/-QVoIxEpFkMAttention Is All You Need (2017). https://arxiv.org/abs/1706.03762 
Hong, Kelly, Anton Troynikov, and Jeff Huber. Context Rot: How Increasing Input Tokens Impacts LLM Performance. Chroma, 2025. https://research.trychroma.com/context-rot. 
The Context Window is the model’s finite working space, containing the input and previously generated tokens available at each generation step. Through self-attention, the model uses these tokens to predict the next token. 
Context Rot describes how the model’s ability to retrieve and use relevant information can decline as the number of tokens in the context window grows.
Context engineering begins with the information available to the model at each generation step. A large language model generates one token at a time. Its current context consists of the input and all tokens generated so far, while self-attention relates the tokens within this bounded sequence to predict the next token. Both examples show an 8,000-token context window. In the first example, 6,000 input tokens leave room for 2,000 output tokens. After 1,500 tokens have been generated, the complete sequence contains 7,500 tokens, all of which remain formally available to the model. In the second example, 10,000 input tokens combined with 1,500 output tokens would produce a sequence of 11,500 tokens, exceeding the limit by 3,500. The system must shorten the sequence through truncation or compaction, or reject the request. The red tokens represent information excluded from the resulting context and therefore unable to influence the next prediction. The formal context limit determines which tokens can be available. Context rot concerns how reliably the model uses them. As the sequence grows, relevant information can become harder to retrieve and apply, causing task performance to decline even before the formal limit is reached. The chart reports results from a controlled repeated-words task and should be understood as task-specific evidence. The pattern varies across models and tasks. Context engineering curates the active sequence so that relevant information retains priority within the finite context budget.

Wissen auswählen, strukturieren und verdichten 
Context Compression kann zunächst allgemein als Verringerung der Informationsmenge verstanden werden, die in einen Arbeitskontext aufgenommen werden soll. Dazu gehören etwa:
Auswahl relevanter Abschnitte,
Zusammenfassung,
Entfernung von Wiederholungen,
Aggregation von Daten,
Reduktion auf relevante Beispiele.
Der Begriff bezeichnet jedoch zunächst nur die Verringerung des Umfangs. Für Context Engineering genügt das nicht.
Distillation
Das Paper verwendet deshalb den stärkeren Begriff Distillation. Distillation reduziert nicht nur die Tokenmenge, sondern überführt ein vorhandenes Verständnis in eine selektive, strukturierte und prüfbare Repräsentation.
Erhalten bleiben sollen insbesondere:
relevante Begriffe und Unterscheidungen,
Beziehungen und Abhängigkeiten,
Bedingungen und Einschränkungen,
Unsicherheiten und offene Fragen,
Begründungen und Entscheidungszusammenhänge.
Das gleiche Ausgangsmaterial kann unterschiedlich destilliert werden, wenn sich Zweck oder Aufgabe verändern. Eine Zusammenfassung für eine allgemeine Einführung unterscheidet sich von einer Darstellung, die einen Agenten bei der Implementierung oder Verifikation anleiten soll.
Das Paper grenzt Distillation daher ausdrücklich von blosser Zusammenfassung und Context Compression ab. Sie erzeugt eine inspizierbare Repräsentation, die für weitere Arbeit hinreichend sein soll.

Wissensdokumente und ihre Serialisierung in Markdown 
Wissensdokumente
Hier würde die verbesserte Definition stehen:
Ein Wissensdokument ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus umfangreicherem Material destilliert und von Menschen geprüft sowie von LLM-basierten Systemen als Kontext genutzt werden kann.
Danach die zentralen Eigenschaften:
Begrenztheit Ein Wissensdokument bildet nicht den gesamten Wissensbestand ab, sondern einen abgegrenzten Gegenstand oder Zweck.
Strukturierung Begriffe, Zusammenhänge, Regeln, Bedingungen und Unsicherheiten werden explizit organisiert.
Revidierbarkeit Das Dokument bleibt lesbar, kritisierbar, ergänzbar und korrigierbar.
Duale Nutzbarkeit Menschen können es prüfen und bearbeiten; LLM-basierte Systeme können es als Kontext verwenden.
Zweckmässige Verdichtung Das Dokument ist kompakt, ohne die für seinen Zweck erforderlichen Differenzierungen zu verlieren.
Das Paper beschreibt solche Dokumente als begrenzte Repräsentationen, die aus umfangreicherem Material destilliert, für menschliche Prüfung gepflegt und für die Aufnahme in aufgabenspezifische Working Contexts verfügbar gemacht werden.
Markdown als Serialisierung
Das Wissensdokument ist das konzeptionelle Artefakt. Markdown ist eine mögliche technische Repräsentation dieses Artefakts.
Markdown eignet sich dafür, weil es:
als Plain Text offen und langfristig lesbar ist,
einfache Strukturen wie Überschriften, Listen, Links, Tabellen und Codeblöcke unterstützt,
mit unterschiedlichen Editoren bearbeitet werden kann,
leicht versioniert und verglichen werden kann,
durch Menschen direkt lesbar ist,
durch LLMs ohne aufwendige Konvertierung verarbeitet werden kann.

Wissensbasis und Working Context 
Dieser Abschnitt schliesst das Kapitel ab und verbindet die Einzelkonzepte.
Wissensdokumente liegen persistent in einer Wissensbasis oder Projektumgebung. Sie müssen nicht bei jeder Aufgabe vollständig in das Context Window geladen werden.
Das Paper unterscheidet deshalb:
Project Knowledge Base Der persistente, inspizierbare und revidierbare Bestand des dokumentierten Projektwissens.
Working Context Die für eine konkrete Aufgabe bereitgestellten Informationen, Dokumente, Datenzugriffe, Instruktionen und Werkzeuge.
Der Working Context kann enthalten:
die Aufgabenstellung,
relevante Wissensdokumente oder einzelne Abschnitte,
ausgewählte Daten und Beispiele,
Agenteninstruktionen,
Werkzeugbeschreibungen und Zugriffsrechte,
aktuelle Ergebnisse und Rückmeldungen.
Nicht jedes relevante Objekt muss vollständig im Context Window liegen. Ein Agent kann über Werkzeuge auf vollständige Datenbestände zugreifen, während nur Beschreibungen, Abfrageergebnisse oder ausgewählte Beispiele als Tokens in den Kontext aufgenommen werden.
Die zentrale Unterscheidung lautet:
Die Wissensbasis bewahrt verfügbares Wissen. Context Engineering stellt daraus den für eine konkrete Aufgabe geeigneten Working Context zusammen.
Diese Trennung ist für das Paper zentral: Die persistente Wissensbasis und der aufgabenspezifische Working Context erfüllen unterschiedliche Funktionen und dürfen nicht gleichgesetzt werden.

AgenticEngineering 
Agentic Engineering umfasst die systematische Organisation mehrschrittiger agentischer Arbeit, insbesondere die Zerlegung und Koordination von Aufgaben, den Einsatz von Werkzeugen, die Reaktion auf Zwischenergebnisse, die erforderlichen menschlichen Eingriffe sowie die Prüfung und Fortführung der Arbeit. 

Warum mehrschrittige Arbeit organisiert werden muss 
Agentische Arbeit
Ein AI Agent verfolgt ein Ziel über mehrere Modell- und Werkzeugaufrufe.
Er liest und verändert Dateien, führt Programme aus und verarbeitet Zwischenergebnisse.
Seine nächsten Schritte hängen von Ergebnissen, Fehlern und Rückmeldungen aus der Arbeitsumgebung ab.
Organisation und Kontrolle
Aufgaben müssen begrenzt, zerlegt und koordiniert werden.
Werkzeuge, Zugriffsrechte und Abbruchbedingungen müssen festgelegt werden.
Zwischenergebnisse müssen geprüft und bei Bedarf an Menschen eskaliert werden.
Der Projektzustand muss über mehrere Schritte hinweg nachvollziehbar bleiben.
Kernaussage:
Agentic Engineering organisiert, wie ein AI Agent über mehrere Schritte handelt, auf Ergebnisse reagiert und seine Arbeit prüfbar fortführt.

Knowledge Engineering 
Knowledge Engineering umfasst den Aufbau und die Pflege expliziten, revidierbaren Projektwissens, das die aktuelle Auffassung eines Projekts von seinen Daten, seinem Zweck und den für die Umsetzung relevanten Entscheidungen festhält. 

“I know things”
https://media.tenor.com/39mLNuMFLCsAAAAe/thats-what-i-do-i-drink-and-i-know-things.png 
Wissen kann vorhanden sein, ohne explizit dokumentiert, geteilt oder für einen Agenten nutzbar zu sein. 

Warum Wissen explizit festgehalten werden muss
Implizites und fragmentiertes Wissen
Wissen liegt verteilt in Dokumenten, Daten, Notizen, Arbeitspraktiken und bei einzelnen Personen.
Vorhandene lokale Ordnung ergibt noch keine gemeinsame, systemweit nutzbare Wissensbasis.
Informationen können widersprüchlich, unvollständig, veraltet oder nur aus ihrem Entstehungskontext verständlich sein.
Persistentes und revidierbares Projektwissen
Relevantes Wissen wird explizit repräsentiert und strukturiert.
Menschen und LLM-basierte Systeme können denselben dokumentierten Stand lesen und verwenden.
Aussagen, Entscheidungen und Unsicherheiten bleiben prüfbar, ergänzbar und korrigierbar.
Kernaussage:
Knowledge Engineering macht relevantes Wissen explizit, inspizierbar und revidierbar.

Wissensmodellierung
Konstruktion einer Wissensbasis: Konzepte einer Domäne identifizieren, formal repräsentieren, abfragbar machen.
Personal Information Management
Umgang mit eigener Information über Formate und Orte hinweg, im Dienst von Zielen und Rollen.
Projektmanagement
Systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen.
Fragen identifizieren
Wissen erwerben
Vokabular festlegen
Wissen kodieren
Instanzen beschreiben
Abfragen und Inferenz
Evaluieren
Erwerben und erstellen
Speichern und organisieren
Pflegen und wiederfinden
Nutzen und verteilen
Kernproblem: Fragmentierung
Kernkonzept: Personal Information Collection
Initiierung
Planung
Durchführung
Überwachung und Steuerung
Abschluss
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. 
Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez-Quiñones. Personal Information Management. 2017. https://doi.org/10.1081/E-ELIS4-120053695. 
„Handbuch Projektmanagement von Jürg Kuster | ISBN 978-3-662-65472-9 | Fachbuch online kaufen - Lehmanns.de“. o. J. Zugegriffen 15. September 2024. https://www.lehmanns.de/shop/wirtschaft/59031377-9783662654729-handbuch-projektmanagement. 

Wissensdokumente 
Definition
Ein Wissensdokument ist eine begrenzte, strukturierte und revidierbare Repräsentation relevanten Wissens, die aus einem umfangreicheren Bestand destilliert und von Menschen geprüft sowie von LLM-basierten Systemen als Kontext genutzt werden kann.
Eigenschaften
Begrenzt Behandelt einen klar umrissenen Gegenstand oder erfüllt eine bestimmte Funktion.
Strukturiert Organisiert relevante Begriffe, Zusammenhänge, Regeln, Bedingungen und Unsicherheiten.
Revidierbar Kann gelesen, geprüft, ergänzt und korrigiert werden.
Dual nutzbar Für Menschen verständlich und prüfbar; für LLMs als Kontext verwendbar.
Kompakt, aber hinreichend Reduziert Umfang und Redundanz, ohne notwendige Differenzierungen zu verlieren.
Technische Form
Im Workshop werden Wissensdokumente als Markdown-Dateien gespeichert.
Markdown eignet sich dafür, weil es:
offener Plain Text ist,
einfache Strukturen unterstützt,
versionierbar und verlinkbar ist,
von Menschen und LLMs direkt gelesen werden kann.
Die begriffliche Pointe lautet:
Das Wissensdokument ist das Konzept; Markdown ist seine technische Repräsentation.

Persona Engineering: “You are a …”
Du repräsentierst eine typische Teilnehmerin meines Workshops.
Hintergrund:
- 48 Jahre alt
- Literaturwissenschaftlerin
- arbeitet regelmäßig mit Word, Excel und digitalen Editionen
- keine Erfahrung mit Terminal, Git oder VS Code
- nutzt ChatGPT gelegentlich
- ist motiviert, aber vorsichtig bei technischen Installationen
- verwendet Windows

Aufgabe:
Lies die folgende Workshop-Anleitung aus dieser Perspektive.

Identifiziere:
1. Stellen, die du nicht sicher verstehen würdest,
2. Begriffe, die nicht erklärt sind,
3. Schritte, bei denen du wahrscheinlich Unterstützung benötigst,
4. Fragen, die du während des Workshops stellen würdest.

Erfinde keine technischen Fehler. Beurteile nur, was sich aus der Anleitung ergibt.
Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai. https://youtu.be/YnNF55QV0zs?si=GfKc9ZmXyD_UtqYs  

Mapping Mobile Musicians Mobilität und Musiktheaterwissen im Graz der Nachkriegszeit am Beispiel der Sängerin Ira Malaniuk
Erfassen 

Kuratieren 

Verstehen

 Explorieren
(lokal zeigen)

AI Agents gibt es schon länger als LLMs
Titelblatt von Wieners 1948 erschienenem Werk Cybernetics or Control and Communication in the Animal and the Machine. https://de.wikipedia.org/wiki/Norbert_Wiener 
Autonomie: handelt ohne ständige äußere Steuerung
Reaktivität: antwortet auf Veränderungen seiner Umgebung
Proaktivität: verfolgt von sich aus Ziele
“soziale” Fähigkeit: interagiert mit anderen Agenten
Ernst Peter Fischer: Norbert Wieners Kybernetik in 90 Sekunden. https://youtu.be/PKTgbBPMzeg
Wooldridge, Michael, and Nicholas R. Jennings. ‘Intelligent Agents: Theory and Practice’. The Knowledge Engineering Review 10, no. 2 (1995): 115–52. https://doi.org/10.1017/S0269888900008122.   
Multi-Agent Hide and Seek. OpenAI 2017. https://www.youtube.com/watch?v=kopoLzvh5jY 
AlphaGo - The Movie | Full award-winning documentary. 2016. https://youtu.be/WXuK6gekU1Y
Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, und Anima Anandkumar. “Voyager: An Open-Ended Embodied Agent with Large Language Models“, 25. Mai 2023. https://arxiv.org/abs/2305.16291v2. 

LLMs als Jagged Alien ‘Intelligences’
Eigenschaften des Modells 
Probabilistisch / Konfabulationen / Bias / Black-Box
“Memorieren” Arithmetik, Buchstabieren
Sycophancy als Tendenz von LLMs Nutzer:innen zuzustimmen
Andersartiges Weltmodell “Every cat is smarter than an LLM”  (LeCun)
Interaktionen
Tool-Use (Websuche, Coding, … )
Context Window als “Aufmerksamkeitsspanne”
Knowledge Cut-Off und kein Continual Learning
“Reasoning” als “Thinking” Token
Lindsey, Authors Jack, Wes Gurnee*, Emmanuel Ameisen*, u. a. „On the Biology of a Large Language Model“. Transformer Circuits, o. J. Zugegriffen 25. Mai 2025. https://transformer-circuits.pub/2025/attribution-graphs/biology.html. 
Fabrizio Dell’Acqua et al., ‘Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality’, Organization Science 37, no. 2 (2026): 403–23, https://doi.org/10.1287/orsc.2025.21838. 

Summerfield, Christopher. These Strange New Minds: How AI Learned to Talk and What It Means. Viking, 2025.

Joshua Gans, ‘A Model of Artificial Jagged Intelligence’, arXiv:2601.07573, preprint, arXiv, 12 January 2026, https://doi.org/10.48550/arXiv.2601.07573.  


Fable 5 beauftragt 3 Opus Subagents um die TEI XML zu verifizieren und validieren 
Die Opus Subagents bedienen sich der “epistemischen Infrastruktur” aus Wissensdokumenten (pipeline.md) und Tools (Schema, Python Scripts, etc.)

https://www.youtube.com/watch?v=OWPRU_Pc4Ng


MCP vs Skills: Which Is Right for Your AI Agent and LLMs?. https://www.youtube.com/watch?v=goU9VIXA8II 

Modelling Routing
Planning vs. Execution (writing code)
Planning (best possible model) mit Fable oder Opus
Execution mit Opus oder Sonnet
Research → write spec → write code → PR → review → edit 
Spec = Specification = User Stories
Specification ist kontextualisiert im knowledge ordner (daten, research, design etc.)
Review pr wieder bei Fable
Matthew Berman. https://youtu.be/1KKB_UiW6ls?si=QRBVjLB9C24DOzhC 


Knowledge und Context Engineering 
Knowledge Engineering organisiert den Bestand. Vorhandene Dokumente und Daten aufbereiten und nach Konventionen strukturieren; implizites Wissen von Expert:innen und Organisationen erheben und in dieselbe Form bringen.
Context Engineering stellt daraus den für eine Aufgabe relevanten Ausschnitt im Kontextfenster des Agenten bereit.
Die zweite Tätigkeit setzt die erste voraus. Das Wissenssystem ist kein Archiv, sondern ein Produktionssystem für Zielartefakte.

Knowledge Engineering hat zwei Quellen. Die erste sind vorhandene Dokumente und Daten, die aufbereitet werden, PDF-Bestände in maschinenlesbare Formate überführt (etwa mit Docling), tabellarische Daten in Snapshot-Dokumente, Texte in destillierte Wissensdokumente. Die zweite Quelle ist Wissen, das noch in keinem Dokument steht, sondern implizit bei Expert:innen, in einer Institution oder einem Projekt liegt; es wird über Interviews, Deep Dives und Anforderungserhebung gehoben und in dieselbe strukturierte Form gebracht. Der Begriff stammt aus der Expertensystem-Tradition; die Verschiebung gegenüber der klassischen Fassung liegt im Formalisierungsziel, nicht mehr Logik und Ontologie, sondern strukturierte natürliche Sprache mit leichtem Metadaten-Anteil, weil das Sprachmodell das Sprachverstehen beisteuert.
Context Engineering ist die Gestaltung dessen, was zu jedem Zeitpunkt eines Laufs im Kontextfenster liegt, Auswahl, Reihenfolge und Zeitpunkt des Ladens von Information, Werkzeugen und Anweisungen, einschließlich der Entscheidung, was bewusst nicht geladen wird. Die Abgrenzung gegen Prompting liegt im Gegenstand; Prompting optimiert eine einzelne Anweisung, Context Engineering verwaltet den Informationszustand einer ganzen Arbeitstrajektorie. Es setzt Knowledge Engineering voraus, weil nur ein strukturierter Bestand selektives Laden erlaubt; darin liegt die Abgrenzung gegen den Kurzschluss, Context Engineering sei besseres Prompting.
Der Zweck des Ganzen ist die Produktion. Das Wissenssystem dient nicht der Ablage, sondern der Ableitung von Zielartefakten, eines Konzepts, eines Antrags, einer Spezifikation, eines Datenmodells. Kuratierte, verdichtete Wissensdokumente dienen als Eingabe eines LLM-Schritts, der das Artefakt erzeugt. Die User Story bildet die Brücke zwischen beiden Tätigkeiten, sie fasst eine fachliche Anforderung in eine Form, die für Menschen verständlich und für den Agenten als Kontext verwertbar ist.


Vorbereitung

Obsidian und der Vault als Arbeitsumgebung
Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem lokalen Ordner speichert. Dieser Ordner heißt Vault. 
Die Daten bleiben auf dem eigenen Computer, das Dateiformat ist offen, kein Cloud-Konto ist erforderlich. 
Der Vault ist ein Second Brain, ein externes Gedächtnis, das 
individuelles oder institutionelles Wissen organisiert 
operative Arbeit und Projekte steuert 
Wissensstrukturen und Domänen modelliert und repräsentiert 
https://obsidian.md
Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem gewöhnlichen lokalen Ordner speichert, und dieser Ordner heißt Vault. Es gibt keinen Server, keine Datenbank im Hintergrund, kein Cloud-Konto. Die Daten liegen auf dem eigenen Rechner, das Format ist offener Plain Text, und auf dieser Eigenschaft baut alles Weitere in diesem Workshop auf.
Links sehen Sie meinen eigenen Vault, den Ordnerbaum und daneben die Graphansicht, in der jede Notiz ein Punkt ist und jeder Link eine Kante. Er ist über Jahre gewachsen, Projekte, Lehrmaterial, Begriffe, Literatur. Ein solcher Vault ist ein Second Brain, ein externes Gedächtnis. Er organisiert Wissen, individuelles wie institutionelles, also Ablage und Wiederauffinden. Er steuert operative Arbeit und Projekte, was ansteht, was geplant ist, in welchem Zustand ein Vorhaben ist. Und er modelliert und repräsentiert Wissensstrukturen, von informellen Links und Tags bis zu Dokumenttypen und Relationen. Auf dieser dritten Ebene arbeiten wir in diesem Workshop hauptsächlich, die zweite nehmen wir mit.
Ein externes Gedächtnis ist genau das, was ein AI Agent braucht. Sein Kontextfenster ist ein begrenztes, flüchtiges Arbeitsgedächtnis, der Vault der Langzeitspeicher dazu. Weil der Vault ein Ordner mit offenen Textdateien ist, liest und schreibt der Agent dieselben Dateien wie ich. Obsidian ist eine Sicht auf diesen Ordner, das Terminal eine andere, der Agent eine dritte. Dieses geteilte Gedächtnis ist die Arbeitsgrundlage des Workshops, und deshalb richten wir es jetzt gemeinsam ein.

Claude Code als AI Harness

Obsidian installieren

Claude Code einrichten

Demo: Obsidian und Claude Code

AI Agents

Latent Programm Space

AI Agent Begriffe
Tools Use
AI Harness
AGENTS.md | CLAUDE.md
Agent Skill
Model Context Protocol (MCP)
Agent2Agent (A2A)
Subagents
5 AI Agent Terms You Need to Know. https://youtu.be/k5jYwyhDMxA 

Tools Use

AGENTS.md | CLAUDE.md
Eine Markdown-Datei im Wurzelverzeichnis eines Projekts, die der Agent zu Beginn jeder Sitzung automatisch in seinen Kontext lädt. Sie beschreibt, wie dieses konkrete Projekt funktioniert, also Build- und Testbefehle, Code-Konventionen, Commit-Format und relevante Pfade. Mehrere solcher Dateien sind verschachtelbar, wobei eine Datei näher am Arbeitsverzeichnis die Regeln übergeordneter Dateien überschreibt. Enthält die Datei etwa die Vorgabe, vor jedem Commit pnpm test auszuführen, dann tut der Agent genau das bei jedem Commit in diesem Projekt, ohne dass du es erneut anweist. (Von OpenAI eingeführt.)

Agent Skill
Ein Ordner mit einer SKILL.md und optional Skripten und Ressourcen für eine bestimmte Aufgabe
Name und Beschreibung jedes eingerichteten Skills lädt der Agent bei Sitzungsbeginn, die ganze Skill erst bei passender Anfrage
Dauerhaft präsent bleibt allein die Beschreibung, das hält das Context Window bei themenfremden Aufgaben frei
Beispiel: PowerPoint oder Word erzeugen
Agent Skills. https://agentskills.io
5 AI Agent Terms You Need to Know. https://youtu.be/k5jYwyhDMxA
Skill-Aufruf bei claude.ai

MCP
Ein offenes Protokoll, das LLM-Anwendungen über eine einheitliche Schnittstelle mit externen Tools, Datenquellen und Workflows verbindet. Ein Tool oder eine Datenquelle wird in einen MCP-Server verpackt, und jeder Agent, der MCP spricht, kann diesen Server nutzen, ohne einen eigenen Konnektor dafür zu bauen. Das löst das M-mal-N-Problem, da sonst M Agenten und N Tools M×N maßgeschneiderte Verbindungen bräuchten. Braucht ein Agent etwa Daten aus Notion, spricht er MCP mit einem Notion-MCP-Server, und dieser Server kümmert sich um die eigentliche Notion-API; einen Stripe-Server spricht derselbe Agent auf dieselbe Weise an. (Von Anthropic.) 

A2A (Agent to Agent)
A2A (Agent2Agent) ist ein offener Standard für die Kommunikation zwischen autonomen KI-Agenten. Er definiert eine gemeinsame Sprache, mit der Agenten aus unterschiedlichen Frameworks und von verschiedenen Anbietern zusammenarbeiten, ohne interne Logik, Tools oder Speicher preiszugeben.
Opakheit: Interaktion ohne Offenlegung von Speicher, Tools oder proprietärer Logik.
Erweiterbarkeit: formale Extensions mit gestuftem Promotionsverfahren, das den Kern stabil hält.
Verhältnis zu MCP: komplementär, MCP regelt Agent-zu-Tool, A2A Agent-zu-Agent.
Abgrenzung: kein Development-Kit, kein Tool-Call-Protokoll, kein MCP-Ersatz, keine Messaging-App.

https://a2a-protocol.org/latest/topics/a2a-and-mcp/#why-different-protocols 
https://github.com/a2aproject/A2A 

Subagents
Ein Subagent ist ein Kindagent, den der Hauptagent für eine abgegrenzte Teilaufgabe erzeugt. Jeder läuft in seinem eigenen frischen Kontextfenster, erledigt seine Arbeit und gibt nur ein Ergebnis zurück, was das Kontextfenster des Elternagenten sauber hält und Parallelität ermöglicht. Anders als die vier anderen Begriffe gibt es dafür keinen formalen Standard, sondern ein Muster, das in praktisch allen Agentensystemen nahezu identisch auftaucht. Im ersten typischen Fall ist eine Aufgabe zu groß für ein einzelnes Kontextfenster, etwa das Sichten von 500 Dateien; der Hauptagent erzeugt einen Subagenten, der die Dateien liest und eine Zusammenfassung zurückgibt, sodass er selbst nie alle 500 laden muss. Im zweiten Fall ist die Arbeit parallelisierbar, etwa zwanzig unabhängige Prüfungen, die zwanzig Subagenten gleichzeitig statt nacheinander erledigen. Dein Forschungsleitstellen-Muster mit parallel orchestrierten Claude-Instanzen ist eine konkrete Ausprägung davon.

Knowledge und Context Engineering

Warum AI Agents Context brauchen 
Mit wachsender Autonomie verschiebt sich der Engpass vom Modell zum Kontext.
Das Kontextfenster ist begrenzt; die Leistung fällt deutlich unterhalb der Fenstergrenze ab (Context Rot).
Lange autonome Läufe akkumulieren Rauschen; Reasoning-Budget fließt in Navigation statt in die Aufgabe.
Zielgröße ist nicht kurz, sondern dicht und hinreichend.

Der Befund lässt sich reproduzieren. Erhält ein Agent einen unstrukturierten Bestand und den Auftrag, daraus ein Zieldokument zu erzeugen, fällt das Ergebnis schwach aus oder der Kontext läuft über. Drei Mechanismen erklären das. Erstens degradiert die Modellleistung mit wachsender Kontextlänge deutlich unterhalb der nominellen Fenstergrenze; die Chroma-Untersuchung von 2025 zeigt das über 18 Modelle hinweg (Angaben auf der Verifikationsliste). Zweitens akkumuliert ein langer autonomer Lauf Rauschen, jedes gelesene irrelevante Dokument, jede Fehlausgabe bleibt im Fenster und verwässert die relevante Information. Drittens ist das Reasoning-Budget endlich; was das Modell auf die Navigation durch ungeordnetes Material verwendet, fehlt am eigentlichen Problem.
Die Gegenposition gehört dazu. Für kurze Einzelabfragen sind starke Modelle robust gegen unordentlichen Kontext; das Problem kippt beim langhorizontigen Delegieren, wenn der Agent über viele Schritte selbständig mit dem Material arbeitet. Daraus folgt die Kernthese, mit wachsender Autonomie verschiebt sich der Engpass vom Modell zum Kontext. Ein besseres Modell behebt das nicht, ein besser organisierter Bestand schon.
Die Konsequenz ist keine Kürzungsregel. Radikal verknappter Kontext verliert Provenienz und Begründung, das Ergebnis wird nicht besser, sondern anders schlecht. Die Zielgröße ist dicht und hinreichend, jede Aussage trägt Information, und ein frischer Kontext wird mit dem Material allein handlungsfähig. Die architektonische Antwort ist eine geschichtete Basis, ein minimaler Kern bleibt permanent geladen, die Tiefe wird bedarfsgesteuert nachgeladen. Wie diese Architektur gebaut wird, ist Gegenstand von Phase 2.
Ref. Chroma, Context Rot, 2025.


Wissensmanagment mit LLMs
Obsidianhttps://obsidian.md
Claude Codehttps://code.claude.com/docs/de/overview 


Screencast der heutigen Einheit zum Nachschauen
Wissens- und Projektmanagement mit Obsidian und Claude Code. Einführung. https://youtu.be/31Y6uRLnkQA 

Wissensmodellierung
Konstruktion einer Wissensbasis: Konzepte einer Domäne identifizieren, formal repräsentieren, abfragbar machen.
Personal Information Management
Umgang mit eigener Information über Formate und Orte hinweg, im Dienst von Zielen und Rollen.
Projektmanagement
Systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen.
Fragen identifizieren
Wissen erwerben
Vokabular festlegen
Wissen kodieren
Instanzen beschreiben
Abfragen und Inferenz
Evaluieren
Erwerben und erstellen
Speichern und organisieren
Pflegen und wiederfinden
Nutzen und verteilen
Kernproblem: Fragmentierung
Kernkonzept: Personal Information Collection
Initiierung
Planung
Durchführung
Überwachung und Steuerung
Abschluss
Russell, Stuart J., and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th edn. Pearson Series in Artificial Intelligence. Pearson, 2020. https://aima.cs.berkeley.edu. 
Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez-Quiñones. Personal Information Management. 2017. https://doi.org/10.1081/E-ELIS4-120053695. 
„Handbuch Projektmanagement von Jürg Kuster | ISBN 978-3-662-65472-9 | Fachbuch online kaufen - Lehmanns.de“. o. J. Zugegriffen 15. September 2024. https://www.lehmanns.de/shop/wirtschaft/59031377-9783662654729-handbuch-projektmanagement. 

CLAUDE.md
CLAUDE.md-Dateien sind Markdown-Dokumente, die einem Agenten persistente Instruktionen für ein Projekt oder einen Workflow geben. Sie werden als Klartext geschrieben und zu Beginn jeder Session in das Context Window geladen. Was dort steht, gilt in jeder Session und muss nicht mehr im Chat wiederholt werden.
Es gibt ein globales und ein projektspezifisches CLAUDE.md.
Der Agent macht denselben Fehler ein zweites Mal.
Ein Review findet etwas, das der Agent über diese Codebasis hätte wissen müssen.
Dieselbe Korrektur wird im Chat getippt wie in der letzten Session.
Ein neues Teammitglied bräuchte denselben Kontext, um produktiv zu sein.
Speaker Notes: Die rechte Spalte hält die vier Aufnahmesignale, jedes beschreibt eine Wiederholungssituation, die ein Eintrag beendet. Daneben existiert ein zweiter Entstehungsweg, vorab gesetzte Policy wie ein Abschlusskriterium, die keinem konkreten Fehler folgt. Real gibt es weitere Ebenen, CLAUDE.local.md für persönliche, nicht versionierte Ergänzungen und eine Organisationsebene in Claude Code; die Zwei-Ebenen-Darstellung ist eine didaktische Vereinfachung.


Globale CLAUDE.md
todo
Das globale CLAUDE.md liegt im Home-Verzeichnis der Person und wird in jeder Session geladen, unabhängig vom Projekt. Es hält personengebundene Policy, also Rolle und Arbeitsmodus, Arbeitsweise und Abschlusskriterien. Das Auswahlkriterium lautet dauerhaft und projektunabhängig; alles, was nur ein Projekt betrifft, wandert eine Ebene tiefer. 
Das Beispiel demonstriert nebenbei, wie Instruktionen für ein Modell geschrieben werden, ausformulierte Sätze statt Stichwortlisten, direkte Anrede, überprüfbare Regeln. Der Abschnitt Detailwissen praktiziert selbst Context Engineering, das Dokument bleibt klein und verweist auf Skills und Projektwissen, statt Details zu inlinen. Das Abschlusskriterium entspricht der Definition of Done aus Scrum und verhindert den häufigsten Agentenfehler, das vorzeitige Fertigmelden. 

Projektspezifisches CLAUDE.md
## Rolle und Arbeitsmodus

Du bist mein Co-Researcher. Wenn ich eine Frage stelle, gib eine Einschätzung und ändere nichts. Wenn ich eine Aufgabe stelle, setze sie direkt um, ohne Optionen aufzuzählen oder um Erlaubnis zu fragen.

## Arbeitsweise

Mache die Anforderung explizit, bevor Code entsteht. Baue die minimale Lösung, die funktioniert, und keine Abstraktion, die niemand verlangt hat.

## Abschlusskriterium

Melde nichts als fertig, bevor die Verifikation gelaufen ist, und benenne, was geprüft wurde. War keine Verifikation möglich, sage das und begründe es.

## Detailwissen

Stilregeln liegen in Skills, Projektwissen liegt im jeweiligen Projekt. Dieses Dokument hält nur die Verweise.

Das projektspezifische CLAUDE.md liegt im Root des Repositories und wird zusätzlich zum globalen geladen, sobald eine Session dort startet. Es hält projektgebundene Fakten, also Build- und Testkommandos, Konventionen, Projektstruktur und Domänenbegriffe, die der Agent in jeder Session dieses Projekts braucht. Bei Widerspruch gilt das spezifischere Dokument; das ist Konvention, keine Mechanik, denn technisch werden beide Ebenen nur konkateniert. 
Die vier Abschnitte decken die Standardfragen jeder Session ab, wie wird gebaut und getestet, welche Konventionen gelten, wo liegt was, welche Domänenbegriffe trägt das Projekt. Der Präzedenzsatz rechts trägt den Übergang zur nächsten Einheit, weil das System keine Konfliktauflösung kennt, muss die Rangfolge als Regel formuliert werden; hier schließen Skills und pfadgebundene Regeln an. 

Um was geht es hier?
Für fortgeschrittenes Arbeiten mit LLMs muss man Projektmanagement, Kontext-Engineering, AI Harness und Wissensmodellierung berücksichtigen. Das ist zumindest meine These! Das ist besonders für mythos-/abler-Tier-Modelle wichtig, da man so den Agenten ausreichend Kontext zur Verfügung stellt, damit sie produktiv autonom arbeiten können.


Promptotyping


Folie 7: Promptotyping (Konzeptuelle Einordnung)
Funktion: Übergang von der Demo zur Methode, Begriffe verankern Inhalt:
Grafik einer Kugel mit den Elementen:
Research Data
Research Domain & Expert in the Loop
Co-Intelligence (Mollick)
(Frontier-)LLM & Context Engineering
Research Artefacts (e.g. tools, workflows, models)
In der Mitte: Der naive Prompt als Ausgangspunkt


Spec Driven Development

Scholar-Centred Design und Requirements Engineering
Knowledge Acquisition
Deep Dives (Workshops) mit Expert:innen
Expert Interview
Literature Review…
Erstellung von Personas
Sozialhistoriker:in
Liturgiewissenschaftler:in …
User Stories & Epics
As a ...
I want to ...
So that I can …
liturgy scholar
compare the Office structure for a specific feast across multiple Libri Ordinarii (e.g. Salzburg, Passau, Regensburg)
identify regional differences in liturgical practice
liturgy scholar
match chant incipits against the Cantus Index API and retrieve genre, Cantus ID, and concordances
verify identifications without manual lookup in printed catalogues
liturgy scholar
filter rubrics by spatial references (altars, chapels, processional stations)
reconstruct ritual movement within a specific church building
social historian
see network changes between 1828-1859
track how community business relationships developed over time
social historian
compare business activities between different community groups
map economic cooperation and division in Norton
social historian
view how men and women participated differently in credit and trade networks
reveal gender patterns in Norton's economic life
Pollin, Christopher. ‘Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example’. Graz, 2025. https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602. 

Promptotyping: Exploring Vibe Coding before it was cool
Pollin, Christopher. ‘Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example’. 2025. http://unipub.uni-graz.at/obvugrhs/12127700. 
“There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.” 		— Andrej Karpathy, February 2025
“I 'Accept All' always” 
“I don't read the diffs anymore”
“it's not really coding — I just see stuff, say stuff, run stuff”
Andrej Karpathy. Vibe Coding. https://x.com/karpathy/status/1886192184808149383

Christopher Pollin. “Haters gonna hate”: Warum die Kritik an Vibe Coding berechtigt ist – und welche Proto-AGI-Potenziale sie übersieht. https://dhcraft.org/excellence/blog/Vibe-Coding  
https://chpollin.github.io/HistInfo/InfoVis/wheaton-network-vis/wheaton-network-vis.html 
Andrej Karpathy coined the term “Vibe Coding” in February 2025. “here's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.” The accompanying statements were deliberately provocative. “I 'Accept All' always.” “I don't read the diffs anymore.” “It's not really coding — I just see stuff, say stuff, run stuff.”
By the time Karpathy named the practice, I had been doing it for almost half a year. Starting in autumn 2023, documented in the workshop series “Angewandte Generative KI in den (digitalen) Geisteswissenschaften” (chpollin.github.io/GM-DH), I experimented with LLMs at almost every level of the research process during my dissertation on workflows for historical information (Pollin 2025). I used them to model ontologies, generate TEI-XML and RDF, write SPARQL queries, and produce code for data analysis and visualisation. The key discovery was that user stories functioned as a bridge between structured research data and visual outputs. Instead of starting from the code, I described what a researcher needed to see and why, and let the LLM generate the implementation. In the early experiments, this meant Python scripts producing matplotlib plots and simple statistical charts. The data, with its semantics encoded in RDF and domain-specific ontologies, provided the structure. The user stories provided the direction. The LLM mapped one onto the other. As models improved across generations, from GPT-4 through Claude Opus 4.5 to the current frontier, the outputs grew more ambitious. What began as Python plots evolved into interactive, browser-based HTML interfaces. Tasks that failed or required extensive manual correction in 2023 worked reliably by late 2025. The blog post "Haters gonna hate" (dhcraft.org) contextualises why the critique of Vibe Coding is justified and what proto-AGI potentials it nonetheless reveals.


Andrej Karpathy. Vibe Coding. https://x.com/karpathy/status/1886192184808149383
The AI Daily Brief. Rick Rubin on Art, Life, and Vibe Coding. https://youtu.be/6BDsFUvPqI0
Christopher Pollin. “Haters gonna hate”: Warum die Kritik an Vibe Coding berechtigt ist – und welche Proto-AGI-Potenziale sie übersieht. https://dhcraft.org/excellence/blog/Vibe-Coding  
 
 Vibe Coding      
99% Vibe Code with Claude Opus 4.1 in ~6hBased on real research data (8 Excel Files). 

Pollin, Christopher. ‘Promptotyping: Von der Idee zur Anwendung’. Digital Humanities Craft - Research Blogs, 24 April 2025. https://dhcraft.org/excellence/blog/Promptotyping 

Promptotyping
https://chpollin.github.io/strashun/web-prototype 

Anhang


AI Agents gibt es schon länger als LLMs
Norbert Wiener begründet 1948 die Kybernetik und beschreibt, wie ein System sich selbst steuert, indem es Information über die eigenen Wirkungen zurückführt	Regelkreis = Feedback Loop → Loop Engineering (?)
Wooldridge und Jennings (1995) bestimmen einen Agenten über vier Eigenschaften.
Autonomie: 		handelt ohne ständige äußere Steuerung
Reaktivität: 		antwortet auf Veränderungen seiner Umgebung
Proaktivität: 		verfolgt von sich aus Ziele
“soziale” Fähigkeit: 	interagiert mit anderen Agenten
Titelblatt von Wieners 1948 erschienenem Werk Cybernetics or Control and Communication in the Animal and the Machine. https://de.wikipedia.org/wiki/Norbert_Wiener 
Ernst Peter Fischer: Norbert Wieners Kybernetik in 90 Sekunden. https://youtu.be/PKTgbBPMzeg

Wooldridge, Michael, and Nicholas R. Jennings. ‘Intelligent Agents: Theory and Practice’. The Knowledge Engineering Review 10, no. 2 (1995): 115–52. https://doi.org/10.1017/S0269888900008122.   
Wiener begründet 1948 die Kybernetik als Wissenschaft von Steuerung, Regelung und Kommunikation in Systemen. Der zentrale Mechanismus ist der Regelkreis, ein System steuert sich selbst, indem es Information über die eigenen Wirkungen zurückführt und sein Verhalten daran korrigiert. Der Thermostat genügt als Minimalbeispiel, messen, vergleichen, nachstellen. Die Verbindung zur Gegenwart liegt in der Struktur, die agentische Ausführungsschleife aus Handeln, Ergebnislesen und erneutem Handeln ist ein Regelkreis, dessen Feedback über Tool-Ausgaben statt über Sensoren läuft. Das Titelblatt rechts datiert den Gedanken auf siebzig Jahre vor Claude Code.
Wooldridge und Jennings bestimmen 1995 den Agenten über vier Eigenschaften, Autonomie, Reaktivität, Proaktivität und soziale Fähigkeit. Beim Durchgehen lohnt die Rückbindung an heutige Systeme. Autonomie entspricht dem Lauf ohne Rückfrage über viele Schritte, Reaktivität dem Verarbeiten von Tool-Ergebnissen und Fehlern, Proaktivität der Zielverfolgung über die Einzelanweisung hinaus, soziale Fähigkeit den Subagents und A2A. Die Definition ist dreißig Jahre alt und passt auf Claude Code. Die LLMs haben die Agentenidee nicht neu erfunden, sondern die fehlende Komponente nachgeliefert, ein Verhaltensmodul, das Sprache versteht und Handlungen planen kann. Die Frage, welche Komponente vorher fehlte und wie sie ersetzt werden sollte, leitet zur nächsten Folie über

Reinforcement Learning Agents und LLM-Agents
Multi-Agent Hide and Seek. OpenAI 2017. https://www.youtube.com/watch?v=kopoLzvh5jY 
AlphaGo - The Movie | Full award-winning documentary. 2016. https://youtu.be/WXuK6gekU1Y
Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, und Anima Anandkumar. “Voyager: An Open-Ended Embodied Agent with Large Language Models“, 25. Mai 2023. https://arxiv.org/abs/2305.16291v2. 

NVIDIAs new 'Foundation Agent' SHOCKS the Entire Industry! | Dr. Jim Fan and agents for any REALITY. https://www.youtube.com/watch?v=SBoen3q5AoQ 


AlphaGo schlägt 2016 Lee Sedol. Move 37 in der zweiten Partie hielten kommentierende Profis zunächst für einen Fehler, er erwies sich als spielentscheidend. AlphaGo hat den Zug nicht aus menschlichen Partien gelernt, sondern im Selbstspiel entwickelt, die Strategie liegt außerhalb des menschlichen Trainingsmaterials. Für die Dokumentation lohnt die Szene, in der Fan Hui den Zug einordnet.
Multi-Agent Hide and Seek, OpenAI 2019, erweitert den Befund um die Interaktionsdimension. Verstecker und Sucher entwickeln über Millionen Runden Strategie und Gegenstrategie, Verbarrikadieren, Rampennutzung, zuletzt das Box-Surfing, ein Physik-Exploit der Simulationsumgebung, den die Entwickler nicht kannten. Belohnt wurde nur Verstecken und Finden, alles Weitere ist emergent. Interaktion zwischen Agenten ist damit eine eigene Emergenzquelle, unabhängig von der Größe der beteiligten Modelle. Falls Video, dann der Box-Surfing-Ausschnitt, er belegt in dreißig Sekunden, was die Folie behauptet.
Voyager, Wang et al. 2023, unterscheidet sich strukturell von den beiden ersten Systemen. Diese sind Reinforcement-Learning-Agenten, für ihre Aufgabe trainiert. Voyager exploriert Minecraft mit GPT-4 als Steuerung ohne aufgabenspezifisches Training. Der Agent schreibt sich Fähigkeiten als Code, legt sie in einer Skill-Bibliothek ab und baut auf ihnen auf. Der Tech Tree zeigt den Fähigkeitszuwachs gegen die Baselines, der Abstand wächst mit der Zeit, weil erworbene Skills weitere ermöglichen. Die Skill-Bibliothek beiläufig markieren, das Prinzip kehrt als Agent Skills in Claude Code wieder, die Vertiefung erfolgt dort.

The Agent Vision (Semantic Web)
Berners-Lee, Tim, James Hendler, und Ora Lassila. „The Semantic Web“. Scientific American 284, Nr. 5 (2001): 34–43. https://www.jstor.org/stable/pdf/26059207.pdf?refreqid=excelsior%3A1d9c33aa1ea640d57940082b42df15e6
Berners-Lee, Tim. This Is for Everyone. Pan Macmillan UK, 2025.
Sechs Jahre nach Wooldridge und Jennings entwarfen Tim Berners-Lee, James Hendler und Ora Lassila 2001 im Scientific American eine konkrete Vision für das Web. Software-Agenten sollten von Seite zu Seite wandern und anspruchsvolle Aufgaben für ihre Nutzer erledigen. Das bekannte Szenario zeigt zwei Geschwister, die ihre Agenten Arzttermine und Fahrdienste koordinieren lassen.

Diese Vision wird oft missverstanden. Das Semantic Web zielte nicht darauf, dass Maschinen menschliche Sprache verstehen. Berners-Lee stellte schon 1998 klar: "The Semantic Web is not artificial intelligence." Maschinenverständliche Dokumente bedeuten nur, dass eine Maschine ein wohldefiniertes Problem auf wohldefinierten Daten löst. Nicht die Maschine versteht den Menschen, sondern der Mensch strukturiert seine Daten für die Maschine, über Ontologien, RDF und eindeutige Bezeichner.

Die heutigen Sprachmodelle lösen dieselbe Aufgabe auf dem umgekehrten Weg, sie verarbeiten unstrukturierten Text direkt, ohne die ontologische Infrastruktur, die das Semantic Web voraussetzte.


AI Agents und Agentic AI (Sapkota)
AI Agents sind modulare, LLM-gestützte Systeme, die über reine Textgenerierung hinausgehen und umrissene Aufgaben automatisieren. 
LLM als Kern
Tool Use (Codeausführung, Websuche, Dateizugriff, Terminal)
Memory
Plannen
Ein AI Agent führt umrissene Aufgaben weitgehend selbstständig aus, etwa Dokumente erstellen, Daten suchen, rechnen und Arbeitsabläufe koordinieren, statt nur auf Anfragen zu reagieren.
Agentic AI ist kein einzelner Agent, sondern ein orchestrierter Verbund mehrerer Agenten, gekennzeichnet durch Zusammenarbeit, dynamische Aufgabenzerlegung, persistentes Gedächtnis und koordinierte Autonomie.



Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. ‘AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges’. Information Fusion 126 (September 2025): 103599. https://doi.org/10.1016/j.inffus.2025.103599 .
Was Norbert Wiener wohl über Claude Code gesagt hätte? 
Die heutige Ausprägung des Agenten ist der LLM-gestützte AI Agent. Sapkota, Roumeliotis und Karkee unterscheiden 2025 zwei Stufen.

Ein AI Agent ist ein modulares, von einem Sprachmodell angetriebenes System für umrissene Aufgaben. Sein Kern ist das LLM, ergänzt um Werkzeugzugriff, also Codeausführung, Websuche, Dateizugriff und Terminal, sowie um Gedächtnis und Planung. Ein solcher Agent erstellt Dokumente, sucht Daten, rechnet und koordiniert Arbeitsabläufe, statt nur auf Anfragen zu antworten.

Agentic AI ist die nächste Stufe, aber nicht durch mehr Autonomie, sondern durch eine andere Architektur. Sie ist kein einzelner Agent, sondern ein orchestrierter Verbund mehrerer Agenten, gekennzeichnet durch Zusammenarbeit, dynamische Aufgabenzerlegung, persistentes Gedächtnis und koordinierte Autonomie.

Claude Code zeigt beide Stufen am selben Werkzeug. Im einfachen Lauf ist es ein AI Agent. Sobald es über Subagenten Teilaufgaben an mehrere koordinierte Instanzen delegiert, die parallel arbeiten, bewegt es sich zur Agentic AI. Die Unterscheidung ist also keine Schublade, sondern beschreibt zwei Betriebsarten.
