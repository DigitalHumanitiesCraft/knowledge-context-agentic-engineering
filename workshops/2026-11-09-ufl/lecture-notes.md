---
title: "Lecture Notes (Uni for Life 2026)"
workshop: 2026-11-09-ufl
created: 2026-08-20
updated: 2026-11-04
language: de
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Opus 5.5)
status: draft
related: [profile.md, slide-deck.md, data/README.md, ../../script/full-lecture-notes-de.md]
---

# Intermediate Prompting Agentic Engineering

Uni for Life, Universität Graz, 9. und 10. November 2026

Dr. Christopher Pollin, Digital Humanities Craft OG

Dieses Skriptum folgt dem Foliensatz des Workshops Folie für Folie. Jeder Abschnitt trägt den Titel einer Folie und formuliert aus, was die Folie in Stichworten zeigt. Prompts stehen im Wortlaut, damit sie sich direkt in den eigenen AI Harness kopieren lassen.

## Einstieg

### Vorstellungsrunde

Die Runde klärt, mit welchen Voraussetzungen die Gruppe arbeitet. Gefragt wird nach dem Arbeitsbereich, nach den bisher genutzten KI-Modellen und Werkzeugen, nach Programmiervorkenntnissen etwa in Python oder JavaScript und danach, ob die Begriffe Context Window und Reasoning-Modell vertraut sind. Die letzte Frage ist praktisch. Für die Hands-ons braucht jede Person Zugang zu einem Frontier-LLM, etwa über ein Pro- oder Max-Abo, über Mistral oder lokal, und dazu einen laufenden AI Harness wie Claude Desktop, Codex oder Antigravity.

### Materialien

Die Materialfolie sammelt alle Links in drei Gruppen.

Zur Vorbereitung gehören Claude Desktop (https://claude.com/de/download) und der englischsprachige Foliensatz *Technical Preparation for Context, Knowledge and Agentic Engineering* (https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit), der die Einrichtung im Detail beschreibt.

Die Lehrlinie *Knowledge, Context and Agentic Engineering* wird laufend gepflegt und erweitert.

- Website mit allen Materialien: https://dhcraft.org/knowledge-context-agentic-engineering
- Full Slide Deck: https://docs.google.com/presentation/d/1FtJpBn8l49I6B-r6b8bdIsbTngLQ9-LdP5BeylXD3M4/edit
- Skriptum Deutsch: https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit
- Skriptum Englisch: https://docs.google.com/document/d/1eaGx86RFr4Xywnxmf4Krdy4GKMYMcnW8pAYPXVH-Lr8/edit
- Video-Playlist: https://www.youtube.com/playlist?list=PLXY4kw40KBaY
- Repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering

Von Digital Humanities Craft kommen der YouTube-Kanal (https://www.youtube.com/@DigitalHumanitiesCraft), Folien früherer Veranstaltungen (https://chpollin.github.io/GM-DH), der Blog (https://dhcraft.org/excellence/blog), die öffentliche Zotero-Gruppenbibliothek mit der zitierten Literatur (https://www.zotero.org/groups/5319178/agki-dh) und Patreon (https://www.patreon.com/c/DigitalHumanitiesCraft).

### Lernziele und Ablauf

Der Workshop umfasst drei Sessions zu je zwei Stunden, online über Zoom. Jede Session gehört zu einem Bereich des Agentic Engineering und löst ein Lernziel ein.

Session 1: Prompt und Context Engineering
: Montag, 9.11.2026, 14:00–16:00. Die Teilnehmenden erklären, wie LLM, AI Agent und AI Harness zusammenwirken, und steuern den Agenten über Prompts, CLAUDE.md und Skills. Die Konzepte sind Tool Use, Subagents, Context Window, Memory, Skills und MCP. Dazu gehören Hands-on 1 und 2 mit Wissensdashboard, Pitch und Skill.

Session 2: Knowledge Engineering
: Dienstag, 10.11.2026, 10:00–12:00. Die Teilnehmenden bauen Projektwissen so auf und pflegen es, dass ein AI Agent damit verlässlich arbeitet. Die Konzepte sind Governance, Permission Modes, Promptotyping Documents, Wissensdokument, Tags, Maps of Content und Vault-Governance. Dazu gehört Hands-on 3, in dem die Wissensbasis zu einem Obsidian-Vault wird.

Session 3: Agentic Engineering
: Dienstag, 10.11.2026, 14:00–16:00. Die Teilnehmenden planen agentische Arbeitsabläufe, prüfen ihre Ergebnisse und übertragen sie auf eigene Vorhaben. Die Konzepte sind Promptotyping, Loop Engineering, Determinismus und Qualitätssicherung. Dazu gehört Hands-on 4, ein Analysewerkzeug aus Excel-Daten.

### Begriffe im Workshop

Die Begriffe des Workshops ordnen sich in vier Bereiche. Das LLM ist die Grundlage aller Bereiche, Governance zieht sich quer durch alle.

Prompt Engineering
: Rückfragen, Beispiele und Meilensteine im Prompt.

Context Engineering
: Context Window, CLAUDE.md und AGENTS.md, Memory, Skill und MCP, also alles, was dem Agenten mitgeteilt wird.

Knowledge Engineering
: Wissensdokument, Promptotyping Documents, Docling, der Obsidian-Vault mit Frontmatter, Wikilinks, Tag-Taxonomie und Maps of Content sowie das Kuratieren, also das Wissen, das Menschen erarbeiten und ordnen.

Agentic Engineering
: AI Agent, AI Harness, Tool Use, Subagents und Workflows, Permission Modes, Hook, Rule of Two, Promptotyping, Fancy Research Tools, Loop Engineering, LLM-as-a-Judge, deterministisch und probabilistisch sowie Qualität sichern.

### Aufbauendes Beispiel und Ablauf

Über alle drei Sessions entsteht Schritt für Schritt eine Wissensbasis zu Agentic Engineering und Governance, mit einer Oberfläche im Browser. Jeder Schritt vertieft einen Aspekt des Agentic Engineering. Die Teilnehmenden kopieren die Prompts von den Folien in ihren AI Harness und arbeiten parallel mit. Während die Agents arbeiten, bespricht die Gruppe weitere Konzepte, deshalb lohnt es sich, den eigenen Harness dabei im Blick zu behalten.

Zwei Vorgaben gelten für den ganzen Workshop. Die teuersten Modelle (GPT-6 Astra, Claude Fable) verbrauchen das Nutzungskontingent rasch und sind für die Übungen nicht nötig. Opus reicht für den Hauptagenten, Subagents laufen auf Sonnet 5.5 oder GPT-6.1 Terra. Beim Datenschutz ist Vorsicht geboten, sobald personenbezogene oder sensible Daten im Spiel sind, die unter die Datenschutz-Grundverordnung (DSGVO) fallen, oder Anwendungen, die der EU AI Act regelt, etwa Entscheidungen über Personal.

## Session 1: Prompt und Context Engineering

### „Few-shotted for Breakfast“

Die Folie stellt Beiträge von Andrej Karpathy an den Anfang, die zeigen, wie schnell sich die Arbeit mit LLMs verändert hat. Wer die technische Grundlage nachholen möchte, findet sie in seinem Vortrag *Deep Dive into LLMs like ChatGPT* (https://youtu.be/7xTGNNLPyMI).

### Software … für alle!?

Wenn ein AI Agent Software nach Beschreibung baut, verschiebt sich eine alte Abwägung. Statt Lizenzen für Standardsoftware zu bezahlen oder sich an deren Grenzen zu reiben, lässt sich ein kleines Werkzeug genau für die eigenen Anforderungen bauen. Die Folie zeigt dazu eine Sammlung solcher selbst gebauter Anwendungen (https://getartcraft.com/apps). Ob sich das im Einzelfall lohnt, hängt davon ab, wer das Werkzeug danach pflegt und prüft, und genau darum geht es im Rest des Workshops.

### LLMs bzw. AI Agents als „Jagged Alien Intelligences“

Die Fähigkeiten von LLMs sind gezackt verteilt (jaggedness). Ein Modell löst manche schwierige Aufgaben souverän und scheitert an scheinbar leichten. Eine Feldstudie mit Wissensarbeitenden zeigt diese „gezackte Grenze“ empirisch (Dell’Acqua et al., 2026), und Gans (2026) modelliert sie formal.

Auf der Seite der Modelleigenschaften stehen vier Punkte. LLMs arbeiten probabilistisch, sie können konfabulieren, also plausibel klingende, aber falsche Aussagen erzeugen, sie tragen Bias aus ihren Trainingsdaten und bleiben in ihrem Inneren schwer einsehbar. Ob ein LLM „rechnen“ kann, ist dafür ein gutes Prüfbeispiel. Die Interpretierbarkeitsforschung zeigt, dass ein Modell Additionen über andere interne Wege löst, als es auf Nachfrage selbst beschreibt (Lindsey et al., 2025). Sycophancy bezeichnet die Neigung, Nutzenden nach dem Mund zu reden. Schließlich bilden LLMs eine eigene Art von „Weltmodell“, das sich mit menschlichem Weltwissen nur teilweise deckt (Summerfield, 2025).

Auf der Seite der Interaktion stehen die Eigenschaften, die für die Arbeit mit Agents zählen. LLMs nutzen Werkzeuge (Tool Use), etwa Websuche oder das Ausführen von Code. Das Context Window wirkt wie eine Aufmerksamkeitsspanne, die später im Workshop genauer behandelt wird. Das Wissen des Modells endet am Knowledge Cut-off, und das Modell lernt im Gebrauch nicht kontinuierlich dazu. „Reasoning“ bedeutet bei aktuellen Modellen, dass sie vor der Antwort zusätzliche „Thinking“-Tokens erzeugen.

### LLM-basierte AI Agents

Ein AI Agent ist ein System, das ein Sprachmodell nutzt, um Aktionen zu planen und auszuwählen, darunter Werkzeugaufrufe (Tool Use). So verfolgt der Agent ein festgelegtes Ziel. Rückmeldungen aus der Ausführung fließen in die nächsten Schritte ein, und seine Autonomie ist begrenzt. Die Definition folgt den Übersichten von Sapkota, Roumeliotis und Karkee (2025) sowie Xu et al. (2025).

### AI Harness

Ein AI Harness ist die Softwareschicht, die die Agentenschleife um ein Modell herum ausführt. Er verwaltet Kontext und Arbeitsstand, koordiniert Modellaufrufe und Werkzeugausführung und gibt die Ergebnisse an das Modell zurück. Dabei setzt er Berechtigungen und Abbruchbedingungen durch. Zhong und Zhu (2026) beschreiben den Harness als eigene Laufzeitschicht für Agents, eine praxisnahe Anatomie liefert https://www.langchain.com/blog/the-anatomy-of-an-agent-harness.

Beispiele sind Claude Code, OpenAI Codex, Cursor, Windsurf, OpenCode, Pi, Antigravity CLI, Qwen Code, Cline, GitHub Copilot und Manus. Das Modell liefert die Sprachfähigkeit, der Harness entscheidet, was der Agent sehen und tun darf. Deshalb unterscheiden sich zwei Harnesses mit demselben Modell im Ergebnis spürbar.

### Claude Code in der Claude Desktop App

Die Folie zeigt die Oberfläche, mit der der Workshop arbeitet, und die Einstellungen, die vor dem ersten Hands-on geprüft werden.

- Tool Use ist sichtbar, weil jeder Werkzeugaufruf im Verlauf erscheint.
- Slash Commands sind Befehle an den Harness selbst, etwa `/context`.
- MCP, Connectors und Plugins binden externe Dienste und Erweiterungen an.
- Die Modellwahl steht für den Workshop auf Sonnet 5.5.
- Effort bzw. Reasoning steht auf low oder medium.
- Der Mode wird auf Auto gestellt.
- Usage und Context Window zeigen, wie viel Kontingent und Kontext verbraucht sind.

### Hands-on 1: Ein Projekt konfigurieren

Das erste Hands-on beginnt mit einem neuen, leeren Ordner, etwa `wissensbasis`. Im AI Harness startet eine neue Session mit Zugriff auf genau diesen Ordner. Dann wird der folgende Prompt kopiert und abgeschickt.

> Ich möchte ein Wissensdashboard zu „Agentic Engineering und Governance“ aufbauen, das zu meiner Arbeit und meiner Organisation passt. Grundlage ist eine kurze Webrecherche (verwende nur einen Subagent), die nur Quellen aus 2026 aufnimmt: Papers, Literatur, PDFs, Präsentationen, Best Practices und Webseiten. Das Dashboard zeigt alle gefundenen Quellen nach Kategorien geordnet, mit Suche, Filtern und Sortierung, und verlinkt jeweils auf das Original.
>
> Das Dashboard ist eine Single-Page-Application mit HTML, CSS und JavaScript.
> Das destillierte Wissen liegt als Markdown-Dokumente im Ordner knowledge/.
> Die Liste der gefundenen Quellen liegt im Ordner sources/.
> Das Projekt bekommt eine sinnvolle Ordnerstruktur.
>
> Setze noch nichts um. Stell mir zuerst drei Fragen zu meinem beruflichen Kontext, etwa zu meiner Rolle, meiner Organisation und dazu, wofür ich AI Agents einsetzen möchte.
>
> Wir arbeiten danach in Meilensteinen. Schlag mir die Meilensteine vor und halte nach jedem an, bis ich das Ergebnis geprüft und freigegeben habe.
>
> Erkläre so, dass es auch ohne technische Vorbildung verständlich ist. Antworte kompakt und sachlich, wir arbeiten in einem Live-Workshop.

Der Prompt ist konstruiert. Er bündelt die Konzepte und Strategien des Workshops, damit alle zu einem brauchbaren Ergebnis kommen, und sieht in der eigenen Arbeit anders aus. Die Leitfrage während der Ausführung lautet, was alles passiert. Die Gruppe beobachtet, welche Werkzeuge der Agent aufruft, wann er nachfragt und wann er anhält.

### Prompt Engineering ist so 2025!

Dieselbe Folie zerlegt den Prompt in seine Bausteine. Der erste Absatz definiert den Task. Die vier Zeilen zu Single-Page-Application, `knowledge/`, `sources/` und Ordnerstruktur sind Vorgaben (Constraints). Die Anweisung, zuerst drei Fragen zu stellen, baut Kontext in einem Frage-Antwort-Spiel auf. Die Meilensteine mit Halt nach jedem Schritt steuern den Prozess. Der letzte Absatz legt Zielgruppe und Stil fest.

Die Form eines Prompts ist bei aktuellen Modellen weitgehend egal. Entscheidend sind das Ziel, das nötige Wissen und die Erfolgskriterien. Die Qualität entsteht zunehmend außerhalb des Prompts, im Kontext (Context Engineering) und in der Umgebung, die die Arbeit steuert und prüft (Harness Engineering). Der Rest des Workshops behandelt genau diese beiden Ebenen.

### Markdown und Tokens

Markdown ist eine leichtgewichtige Auszeichnungssprache, die Dokumentstruktur in Klartext ausdrückt. Hierarchie und Elemente werden mit wenigen Zeichen explizit, was für LLMs deutlich weniger Tokens kostet als etwa Word-XML. Die Folie stellt dieselbe Überschrift in beiden Formen nebeneinander.

```markdown
# Die Antwort
## Kapitel 1
Die Antwort ist **42**.
- Punkt 1
  - Punkt 1.1
```

```xml
<w:p>
  <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
  <w:r><w:t>Die Antwort</w:t></w:r>
</w:p>
```

Ein Token ist die Einheit, in die ein LLM Text zerlegt, meist ein Wort oder Wortteil. Kosten und Context Window werden in Tokens gemessen. Ein Tokenizer zerlegt Text in Tokens und ordnet ihnen Zahlen zu, und welcher Tokenizer verwendet wird, hängt vom Modell ab. Unter https://platform.openai.com/tokenizer lässt sich das selbst ausprobieren, die Syntax erklärt https://www.markdownguide.org.

### Wissensdokument (Context Engineering)

Ein Wissensdokument ist eine strukturierte Aufzeichnung externalisierten Wissens, destilliert aus Quellen, Daten oder Erfahrung zur Wiederverwendung durch Menschen und KI-Agenten. Seine Aussagen bleiben auf Belege rückführbar, Annahmen und Unsicherheiten werden explizit gemacht.

Vier Eigenschaften machen ein gutes Wissensdokument aus. Es ist für Menschen und KI lesbar, kompakt mit dem Wesentlichen und seinen Belegen, in offenen Formaten wie Markdown übertragbar und kuratierbar, also prüfbar, korrigierbar und erweiterbar. Im Hands-on entsteht als erstes Wissensdokument `knowledge/project.md`.

```markdown
# Projekt
Wissensdashboard zu Agentic Engineering
und Governance für meine Organisation.
## Zielgruppe
Leitung und Fachabteilungen ohne
Technikhintergrund.
## Offene Fragen
- Welche Kategorien brauchen wir?
```

Mit dem folgenden Prompt wird das Dokument aus dem bisherigen Gespräch geschärft.

> Präzisiere knowledge/project.md aus unserem Gespräch: Ziel, Zielgruppe, Anforderungen, Abgrenzung und offene Fragen. Trenne Belegtes von Annahmen und frag mich, wo etwas unklar ist.

### Tool Use: So bedient ein KI-Agent den Rechner

Auf den Prompt „Fass mir zusammen, worum es in diesem Projekt geht.“ entscheidet der Agent selbst über die Schritte. `ls` zeigt, was im Projektordner liegt, und dort gibt es einen Ordner `knowledge`. `cd .\knowledge\` wechselt in diesen Ordner, `ls` zeigt dort `project.md`, und `cat .\project.md` öffnet den Text, aus dem der Agent die Zusammenfassung schreibt.

Tool Use heißt, dass der Agent selbst entscheidet, welches Werkzeug er als Nächstes einsetzt. Jedes Ergebnis bestimmt den nächsten Schritt. Diese Schleife aus Entscheidung, Werkzeugaufruf und Rückmeldung ist das, was einen Agent von einem Chat unterscheidet.

### Die erste Iteration des Dashboards

Das Dashboard besteht aus vier einfachen Bausteinen. HTML legt die Struktur fest, CSS das Design und JavaScript das Verhalten. JSON enthält die Daten in strukturierter Form, und der Agent hat die gefundenen Quellen dort direkt eingetragen. Eine Adresse wie `http://127.0.0.1:8765` verweist auf einen lokalen Server auf dem eigenen Computer und wird im Browser geöffnet. Die Portnummer ist bei jeder Person anders, und die Seite läuft nur lokal.

AI Agents können Software für genau die Aufgaben bauen, die man braucht. Der Workshop setzt dafür bewusst auf einfache Technologien, weil gerade wer nicht Software entwickelt von kleinen, einfachen Werkzeugen profitiert, die sich lesen und prüfen lassen.

Auf dem Screenshot sind generische Oberflächenelemente gelb markiert, die LLMs ungefragt erzeugen, etwa dekorative Kennzahlen, Verlaufsflächen oder Werbesprache (AI Slop). Diese Elemente zu entfernen (De-Slopification) gehört zu jeder Iteration, bei Oberflächen ebenso wie bei Texten.

### Hands-on 1: Follow-Up Prompts zum Feedback

Die erste Iteration ist selten fertig. Zwei Wege führen weiter. Beim Feedback beschreibt man in Text, was stört, und hängt einen Screenshot an.

> Ist alles perfekt umgesetzt? Liste und begründe!

> Hier ist mein Feedback:
> * Mach ein helles, klares UI, ohne AI-Slop
> * Mach ein echtes Arbeitstool mit einer Sidebar links zum Filtern und Sortieren.
> * …

Die erste Frage nutzt Self-Verification und Self-Refine. Das Modell prüft das eigene Ergebnis und verbessert es auf Grundlage dieser Prüfung. Der zweite Weg holt eine unabhängige Prüfung ein, indem ein Subagent als Gutachter auftritt (LLM-as-a-Judge).

> Beauftrage einen Subagenten, um kritisch-konstruktiv zu reviewen, was wir hier gemacht haben, und er soll konkrete Empfehlungen machen, wie wir es besser machen können. Lass uns seine Ergebnisse gemeinsam diskutieren.

### Subagents: ein Reviewer Agent

Subagents sind eigenständige Agenteninstanzen mit eigenem Context Window, eigenen Anweisungen und Werkzeugen. Der Hauptagent delegiert eine Aufgabe und erhält nur das Ergebnis zurück. Das lohnt sich, wenn eine Aufgabe viel Ausgabe erzeugt, die der Hauptverlauf nicht braucht, etwa eine Webrecherche, wenn sie in sich abgeschlossen ist oder wenn sie eine unabhängige Prüfung braucht. Claude Code bringt die Subagents Explore, Plan und General-purpose bereits mit.

Ein eigener Subagent ist eine Markdown-Datei mit einem kurzen Kopf. Der folgende Reviewer darf nur lesen und läuft auf einem günstigeren Modell.

```markdown
---
name: reviewer
description: Prüft das Projekt.
tools: Read, Glob, Grep
model: sonnet
---

Prüfe Dashboard und knowledge/ gegen
CLAUDE.md. Belege jeden Befund mit
Datei und Stelle. Ändere nichts.
```

Die Datei liegt unter `.claude/agents/reviewer.md`. Claude Code wählt den Subagent über seine description oder auf Zuruf, etwa mit „Lass den reviewer das Dashboard prüfen.“ Die Dokumentation steht unter https://code.claude.com/docs/en/sub-agents.

### Hands-on 1: Follow-Up Prompts zu Refactoring und Kuratieren

Self-Verification und Self-Refine lassen sich auch auf den Code anwenden.

> Was können wir alles refactoren? Erstelle eine Liste und begründe, wie wir das umsetzen können.

Dasselbe gilt für das Wissen. LLMs erzeugen immer Rauschen, und man muss immer wieder aufräumen. Kuratieren heißt auswählen, prüfen, ordnen und erschließen, kontextualisieren, korrigieren, ergänzen, aussortieren und erhalten.

> Wie können wir all unsere Wissensdokumente kuratieren und somit verbessern? Gibt es irgendwo Redundanzen? Können wir sie kompakter und präziser formulieren und damit auch besser machen? Was betrifft das alles?

Weil bei jeder Änderung etwas schiefgehen kann, gehört eine Versionierung mit Git und GitHub dazu. Jeder Stand lässt sich dann zurückholen.

> Lass uns für jeden Task und Meilenstein saubere Commits in unserem GitHub-Repository anlegen.

### Context Window managen

Ein Context Window bezeichnet den Textausschnitt, den ein LLM bei der Verarbeitung oder Erzeugung von Sprache auf einmal berücksichtigen kann. Eingabe und Ausgabe teilen sich diesen Raum. Bei einem Context Window von 8000 Tokens passen 6000 Tokens Eingabe und 1500 Tokens Ausgabe hinein. Bei 10000 Tokens Eingabe ist das Fenster überschritten, und ältere Teile fallen heraus oder müssen gekürzt werden.

Context Rot beschreibt, dass die Leistung eines Modells mit wachsender Eingabelänge nachlässt, lange bevor das Fenster voll ist (Chroma, 2025, https://research.trychroma.com/context-rot). Ein voller Verlauf ist deshalb auch dann ein Problem, wenn er technisch noch hineinpasst. Zwei Videos vertiefen das Thema, *What is a Context Window? Unlocking LLM Secrets* (https://youtu.be/-QVoIxEpFkM) und *Context Engineering for AI Agents: 4 Failure Modes to Avoid* (https://www.youtube.com/watch?v=BwXremQ-i6I).

Zwei Slash Commands machen das Context Window in Claude Code handhabbar. `/context` zeigt, wie voll das Context Window ist und womit. `/compact` ersetzt den Verlauf durch eine Zusammenfassung, danach werden CLAUDE.md und die zuletzt bearbeiteten Dateien neu geladen. Was nur im Gespräch stand und nicht in einer Datei, kann dabei verloren gehen, und genau deshalb gehört dauerhaftes Wissen in Wissensdokumente.

### AGENTS.md / CLAUDE.md

AGENTS.md und CLAUDE.md sind Markdown-Dateien mit dauerhaften Anweisungen für einen AI Agent, also Projektzweck, Arbeitsregeln und Verweise auf Wissen. Der Harness lädt sie bei jeder Session und nach `/compact`. AGENTS.md ist das offene Format, das viele Harnesses lesen (https://agents.md), CLAUDE.md die Entsprechung in Claude Code (https://code.claude.com/docs/en/memory). `/init` untersucht das Projekt und legt die CLAUDE.md an.

Die Anweisungen liegen auf zwei Ebenen. Die globale Datei `~/.claude/CLAUDE.md` gilt für alle Projekte.

```markdown
# Arbeitsweise
- Antworte kompakt und sachlich
- Frag nach, bevor du Dateien löschst
- Keine personenbezogenen Daten an externe Dienste
- Zitiere nur, was du gelesen hast
```

Die Projektdatei `wissensbasis/CLAUDE.md` gilt nur in diesem Projekt.

```markdown
## Projekt
Wissensdashboard zu Agentic Engineering
und Governance für meine Organisation

## Starten
- python -m http.server 8765

## Regeln
- Nur Quellen aus 2026
- Quellen nur in sources/
- knowledge/ wird nie veröffentlicht
```

### Memory

Memory sind Notizen, die der Agent selbst aus der Arbeit ableitet und in späteren Sessions wieder lädt. Anders als CLAUDE.md und AGENTS.md schreiben nicht die Nutzenden sie, sondern der Agent.

| | Claude Code, Auto Memory | Codex, Memories |
| --- | --- | --- |
| Was | schreibt während der Arbeit mit, etwa Vorlieben, Korrekturen, laufende Vorhaben und Hinweise auf Quellen | fasst abgeschlossene Chats im Hintergrund zusammen |
| Wo | lokal unter `~/.claude/projects/…/memory/` | lokal unter `~/.codex/memories/` |
| Standard | an, steuerbar mit `/memory` | aus, steuerbar mit `/memories` |

Verbindliche Regeln gehören in CLAUDE.md bzw. AGENTS.md. Memory ist eine Erinnerungshilfe, die der Agent selbst pflegt, und eignet sich deshalb nicht als Ort für Regeln. Die Quellen sind https://code.claude.com/docs/en/memory und https://learn.chatgpt.com/docs/customization/memories?surface=app.

### Hands-on 2: Vom Wissen zum Pitch und zum Skill

Das zweite Hands-on überträgt das gesammelte Wissen auf die eigene Organisation und macht daraus einen kurzen Pitch. Es läuft in vier Schritten.

Im ersten Schritt entsteht in einem kurzen Interview die Leitfrage.

> Übertrage das Wissen in knowledge/ und sources/ auf meine Organisation. Schlag mir aus dieser Perspektive vor, wo Agentic Engineering und Governance für uns wichtig sind, und stell mir höchstens drei Fragen. Überarbeite nach meinen Antworten einmal und leite drei Leitfragen für einen kurzen Pitch ab.

Im zweiten Schritt wird der Inhalt im Chat ausgearbeitet, bevor eine Datei entsteht. Die PowerPoint-Datei braucht Code und damit mehr Tokens und Zeit, deshalb lohnt sich die Freigabe des Inhalts vorher.

> Arbeite zur gewählten Leitfrage zuerst nur im Chat eine Gliederung für höchstens fünf Folien aus, jede Aussage mit Quelle aus sources/. Erst wenn ich den Inhalt freigebe, erzeugst du die PowerPoint-Datei.

Im dritten Schritt wird das Design mit Text und Screenshot verbessert.

> Hier ist mein Feedback zum Design:
> * …
> Überarbeite die Folien.

Im vierten Schritt wird der erprobte Ablauf als Skill gesichert.

> Halte den Ablauf vom Wissen über die Leitfrage bis zum Design als Skill in .claude/skills/pitch/SKILL.md fest.

### Skills: ein Pitch-Skill

Ein Skill ist gespeichertes Anwendungswissen, ein Arbeitsablauf, den man einmal durchgearbeitet hat, abgelegt als `SKILL.md` und optional ergänzt um Skripte und Vorlagen. Der Harness lädt zunächst nur die description und die vollständige Anleitung erst, wenn die Aufgabe passt. Darin liegt der Unterschied zu CLAUDE.md, die in jeder Session gilt. Aufgerufen wird ein Skill automatisch über seine description oder direkt, hier mit `/pitch`.

```markdown
---
name: pitch
description: Pitch mit max. 5 Folien.
---
# Pitch erstellen
1. Leitfrage mit mir klären.
2. Inhalt im Chat ausarbeiten.
3. Nach Freigabe .pptx erzeugen.
## Design
- Corporate Design der Organisation.
- Eine Botschaft pro Folie.
- Jede Aussage mit Quelle.
```

Der Agent leitet den Skill aus dem freigegebenen Pitch ab. Er ist damit ein Agentenprodukt und wird wie jede CLAUDE.md geprüft, bevor man sich auf ihn verlässt. Die Dokumentation steht unter https://code.claude.com/docs/en/skills.

### MCP, RAG und Memory

Ein Video stellt die vier Wege nebeneinander, auf denen ein Agent über sein Modell hinaus Wissen und Fähigkeiten erhält, nämlich Skills, das Model Context Protocol (MCP) für die Anbindung externer Dienste, Retrieval-Augmented Generation (RAG) und Memory (*Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know*, https://youtu.be/X4FVEEegCbk).

### Context Engineering

Context Engineering gestaltet, was im Context Window steht. Dazu gehören Instruktionen, Wissen, Tools, Memory und die Anfrage selbst, ausgewählt und verdichtet, damit das LLM mit begrenztem Platz zuverlässig arbeitet. Die Ordnung folgt der Übersicht von Mei et al. (2025), der Inhalt den Methoden, die in Session 1 bereits angewandt wurden.

Beschaffen
: Prompt Engineering mit Rückfragen, Beispielen und Meilensteinen aus Hands-on 1 und 2. Retrieval, bei dem der Agent Dateien selbst sucht und liest. Claude Code verwendet dafür keine Vektordatenbank, sondern Suchwerkzeuge und Lesezugriffe.

Verarbeiten
: Strukturierte Information in Markdown, Frontmatter und Relationen von Wissensdokumenten. Destillieren, also Quellen zu Wissensdokumenten verdichten, wie in Hands-on 1.

Verwalten
: Memory in CLAUDE.md und in Notizen, die der Agent selbst schreibt. Context Compression mit `/compact`, das den Verlauf durch eine Zusammenfassung ersetzt.

Anwenden
: Tool Use über MCP-Server und Skills, die erst bei Bedarf geladen werden. Multi-Agent-Arbeit mit Subagents, die je ein eigenes Context Window haben.

## Session 2: Knowledge Engineering

### Agentic Engineering im Überblick

Die Folie eröffnet Session 2 und wiederholt die Begriffe, die der Workshop verwendet. Sie folgt einem Video von IBM Technology (*Agentic Engineering: 5 Terms Every AI Developer Should Know*, 2026, https://youtu.be/SIZsFGvtClM), das fünf Ebenen unterscheidet.

Prompt
: Prompting-Strategien kennen, anwenden und iterativ verbessern.

Knowledge und Context
: Fach- und Projektwissen erschließen und strukturieren, für den jeweiligen LLM-Aufruf auswählen und aufbereiten.

Harness
: Die Arbeitsumgebung mit Werkzeugen, Wissen, Berechtigungen und Steuerung gestalten und prüfen.

Loop
: Aufgaben in Handlungs- und Prüfzyklen bearbeiten, mit klaren Zielen, Abbruchbedingungen und menschlicher Kontrolle.

Factory
: Abläufe weitgehend automatisieren, mit festen Prüfpunkten.

Session 1 hat Prompt und Context behandelt, Session 2 vertieft Knowledge und Harness, Session 3 führt zu Loop.

### KI-Governance auf zwei Ebenen

Governance für KI-Agenten hat zwei Gegenstände, die Daten und den Agenten selbst. Fünf Fragen gelten für beide Ebenen.

Sichtbarkeit
: Wo liegen sensible Daten, und wohin fließen sie? Welche Tools, Konnektoren und Modelle nutzt der Agent?

Klassifikation
: Wie sensibel sind die Daten? Welche Inhalte und Erweiterungen sind vertrauenswürdig, welche fremd?

Rechtsraum
: Wo werden Daten gespeichert und verarbeitet, und welches Recht gilt? Wo läuft das Modell, und lässt sich der Anbieter wechseln?

Zugriff
: Wer darf auf welche Daten zugreifen? Was darf der Agent ohne Freigabe tun, was nur mit?

Nachweis
: Sind die Datenflüsse lückenlos protokolliert? Werden Tool-Calls, Freigaben und Abbrüche aufbewahrt?

Die Kernregel ist die Rule of Two (Meta AI, 2025). Ein Agent hat pro Session höchstens zwei von drei Eigenschaften, nämlich fremde Inhalte verarbeiten, auf eigene Daten zugreifen und Zustand ändern oder nach außen kommunizieren. Braucht eine Aufgabe alle drei, entscheidet ein Mensch. Die Datenebene vertieft ein Video von IBM Technology (*Can Your AI Use Sensitive Data Safely? 5 Capabilities You Need*, 2026, https://www.youtube.com/watch?v=jnP9AgtX0qo), die Agentenebene ein Technologiebericht der United Nations University (Liu, 2026).

### Permission Modes und Autonomie

Claude Code arbeitet mit den Rechten der Person, die es startet. Der Permission Mode legt fest, was ohne Rückfrage geschieht. Die Modi beantworten die Governance-Frage aus dem vorigen Abschnitt, was der Agent ohne Freigabe tun darf. Entscheidend ist, wie viel Autonomie man ihm geben will. Die fünf Modi reichen von wenig zu viel Autonomie.

| Mode | Verhalten | Wann |
| --- | --- | --- |
| Plan | erkundet und plant, ändert nichts | für mehrere Runden an der Spezifikation, bevor etwas gebaut wird |
| Manual | fragt bei allem außer Lesen | wenn man jeden Schritt selbst kontrollieren will |
| Accept edits | bearbeitet Dateien ohne Rückfrage | wenn der Plan steht und Git jede Änderung rückgängig macht |
| Auto | Lesen und Bearbeiten im Projekt frei, alles andere prüft ein Klassifikator | Empfehlung für die tägliche Arbeit, Probleme sind nach der Erfahrung im Workshop selten |
| Bypass | alles ohne Prüfung | nur in isolierten Umgebungen wie einer Sandbox |

Im Auto-Modus beurteilt ein Klassifikator, ob eine Aktion riskant ist. Durchgesetzt wird eine Grenze dagegen durch eine deny-Regel oder einen Hook. Bestimmte Pfade ändert Claude Code nie automatisch, darunter `.git`, `.claude`, `.bashrc` und weitere geschützte Pfade. Die Dokumentation steht unter https://code.claude.com/docs/en/permission-modes.

### Hook: nur im Projektordner arbeiten

Ein Hook ist ein Skript, das der Harness bei einem Ereignis ausführt, hier vor jedem Datei-Werkzeug (PreToolUse). Endet es mit Exit-Code 2, wird der Aufruf blockiert, und der Agent erhält die Begründung. Eine Regel in CLAUDE.md liest der Agent und kann sie übersehen. Einen Hook setzt der Harness durch.

Der Hook wird in `.claude/settings.json` eingetragen.

```json
{"hooks": {"PreToolUse": [{
  "matcher": "Edit|Write",
  "hooks": [{
    "type": "command",
    "command": "python .claude/hooks/schutz.py"
  }]
}]}}
```

`schutz.py` liest den Zielpfad. Liegt er außerhalb des Projektordners, endet das Skript mit Exit-Code 2. Das Skript liegt in diesem Repository unter [`data/hooks/schutz.py`](data/hooks/schutz.py). Der Hook hat Grenzen. Shell-Befehle umgehen ihn, weil er nur die Datei-Werkzeuge prüft, und vollständigen Schutz bietet erst eine Sandbox. Die Dokumentation steht unter https://code.claude.com/docs/en/hooks.

### Knowledge Engineering

Knowledge Engineering umfasst den Aufbau und die Pflege expliziten, revidierbaren Projektwissens. Dieses Wissen hält die aktuelle Auffassung eines Projekts von seinen Daten, seinem Zweck und den für die Umsetzung relevanten Entscheidungen fest. Ein Frontier-LLM setzt nur so genau um, wie die Spezifikation es vorgibt. Wer eine Domäne versteht und ihre Begriffe, Regeln und Entscheidungen festhält, kann sie dem Agenten als genaue Anforderungen übergeben.

Drei etablierte Felder tragen dazu bei.

Personal Information Management
: Der Umgang mit eigener Information über Formate und Orte hinweg, im Dienst von Zielen und Rollen. Das Kernproblem ist Fragmentierung, das Kernkonzept die Personal Information Collection. Die Tätigkeiten reichen vom Erwerben und Erstellen über Speichern, Organisieren, Pflegen und Wiederfinden bis zum Nutzen und Verteilen (Jones et al., 2017).

Projektmanagement
: Die systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen, in den Phasen Initiierung, Planung, Durchführung, Überwachung und Steuerung sowie Abschluss (Kuster et al., 2022).

Wissensmodellierung
: Die Konstruktion einer Wissensbasis, in der die Konzepte einer Domäne identifiziert, formal repräsentiert und abfragbar gemacht werden. Der Weg führt von den Fragen über Wissenserwerb, Vokabular, Kodierung und Instanzen bis zu Abfragen, Inferenz und Evaluation (Russell & Norvig, 2020).

### Docling: Vom PDF zum Wissensdokument

Docling ist ein Open-Source-Werkzeug, das Dokumente auf dem eigenen Rechner in strukturiertes Markdown oder JSON umwandelt. Es entstand bei IBM Research Zürich und gehört heute zur LF AI & Data Foundation (Auer et al., 2024, https://docling-project.github.io/docling/). Der Prozess zeigt konkret den Schritt „Wissen erwerben“ aus der Wissensmodellierung.

1. Ein Mensch wählt die Quelle aus, etwa ein PDF, eine Word- oder PowerPoint-Datei, eine Webseite oder einen Scan.
2. Docling analysiert Layout, Lesereihenfolge und Tabellen und erkennt bei Scans den Text per OCR.
3. Das Ergebnis ist ein DoclingDocument, eine einheitliche Struktur aus Überschriften, Absätzen, Tabellen und Bildern.
4. Daraus exportiert Docling Markdown oder verlustfreies JSON.
5. Der Agent liest das Markdown in `sources/` und destilliert daraus Wissensdokumente in `knowledge/`, die ein Mensch prüft.

Markdown erhält Überschriften, Lesereihenfolge und Tabellen, die bei einfacher Textextraktion verloren gehen. Weil Docling lokal läuft, verlassen sensible Dokumente den Rechner nicht. Über einen MCP-Server lässt sich Docling auch direkt an einen Agenten anbinden. Im Workshop ist Docling kein Hands-on, weil die lokale Installation über Python in einer Zoom-Sitzung zu viel Einrichtung verlangt.

### Promptotyping Documents

Promptotyping Documents sind Wissensdokumente, unterschieden nach der Art des Wissens, das sie tragen (Pollin, 2026). Allen drei Typen sind die Teilnehmenden in Session 1 schon begegnet.

Declarative Documents
: Sie halten Wissen über den Gegenstand fest, also über Daten, Domäne und Anforderungen, und erweitern, was das LLM über das Projekt weiß. Beispiele sind `project.md`, `data.md`, `specification.md` und `design.md`. In Hands-on 1 waren das `project.md` und `sources/`.

Process Documents
: Sie halten Wissen über den Arbeitsverlauf fest, also was geschehen ist, was offen ist und was als Nächstes kommt. Zusammen mit Git bilden `journal.md`, `handoff.md` und `plan.md` das Gedächtnis des Projekts. In Hands-on 1 übernahmen Commits und Meilensteine diese Rolle.

Action Documents
: Sie halten Wissen über das Handeln fest, also was Agents im Projekt tun dürfen und wie, und steuern damit das Verhalten des Agenten. Beispiele sind CLAUDE.md und AGENTS.md, `governance.md`, `rules.md` und Skills wie der Pitch-Skill aus Hands-on 2.

### Obsidian

Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem lokalen Ordner speichert. Dieser Ordner heißt Vault. Die Daten bleiben auf dem eigenen Computer, das Dateiformat ist offen, und ein Cloud-Konto ist nicht nötig (https://obsidian.md).

Ein Vault kann auf drei Ebenen arbeiten. Auf der ersten dient er der persönlichen Information, also Ablage und Wiederfinden im Sinne des Personal Information Management. Auf der zweiten trägt er Projekt und Arbeit, etwa laufende Vorhaben, Workshop- und Publikationsplanung. Auf der dritten bildet er Wissensstruktur ab, von informeller Strukturierung mit Links, Tags und Maps of Content bis zu formaler Modellierung mit Dokumenttypen, Relationen und Schemata.

### How Steph Ango uses Obsidian

Steph Ango ist CEO von Obsidian und beschreibt sein eigenes System als einen möglichen Stil (https://stephango.com/vault). Er arbeitet mit einem einzigen Vault, kaum Ordnern, durchgehend Markdown, Kategorien und Tags im Plural, Datumsangaben im Format JJJJ-MM-TT und vielen internen Links. Er rät, eigene Regeln zu wählen, aufzuschreiben und bei Bedarf zu ändern, weil ein konsistenter Stil viele kleine Entscheidungen erspart. Die Prinzipien sind Ausgangspunkte für eigene Entscheidungen und kein Standard.

### Das Wissensdokument im Vault

In Session 1 war ein Wissensdokument eine Markdown-Datei mit Überschriften. Im Vault kommen ein Kopf und Relationen dazu.

```markdown
---
type: knowledge
created: 2026-11-10
status: draft
tags: [policies, agents]
---
# Agent Governance
## Summary
Die [[Rule of Two]] begrenzt …
## Kernpunkte
## Synthese
## Sources
## Related
- [[Permission Modes]]
- [[Hooks]]
```

Kopf
: Der Frontmatter in YAML, einem Format aus Schlüssel und Wert. Typ, Datum, Status und Tags machen den Vault abfragbar.

Körper
: Ein Konzept pro Datei, in sich verständlich, mit Summary, Kernpunkten, Synthese und Sources.

Relationen
: Wikilinks im Text und unter Related. Obsidian zeigt auch, welche Dokumente auf ein Dokument verweisen.

### Tags und Tag-Taxonomie

Tags sind Attribute quer zu Ordnern und lassen sich kombinieren. Links verbinden einzelne Konzepte, Tags benennen breite Kategorien. Eine Tag-Taxonomie ist ein kontrolliertes Vokabular mit Kategorien, die sich nicht überlappen, und neue Tags entstehen nur innerhalb dieser Kategorien. Ohne Taxonomie entstehen Synonyme, Tippfehler und uneinheitliche Granularität.

Das Beispiel auf der Folie arbeitet mit drei Kategorien. Das Thema sagt, worum es geht (`agents`, `policies`, `risks`), die Funktion, welche Art Dokument vorliegt (`concepts`, `mocs`, `workflows`), und die Quelle, woher das Wissen stammt (`papers`, `websites`, `originals`). Ein Dokument trägt dann etwa `tags: [agents, concepts, papers]`. Der Reifegrad steht im Feld `status` und gehört nicht in die Tags.

### Maps of Content

Eine Map of Content (MOC) ist ein kuratierter Einstiegspunkt in einen Themenbereich. Sie versammelt Links auf verwandte Dokumente mit je einer Zeile Erläuterung. MOCs können verschachtelt sein, eine `HOME.md` im Root verweist auf Themen-MOCs, diese auf Unter-MOCs oder Wissensdokumente.

```
HOME.md
├── Governance MOC
│   ├── [[Rule of Two]]
│   ├── [[Permission Modes]]
│   └── [[Hooks]]
├── Agents MOC
│   ├── [[Subagents]]
│   └── [[Skills]]
└── Quellen MOC
```

Für Agents sind MOCs Navigationsinfrastruktur. Das Context Window fasst einen größeren Vault nicht vollständig, deshalb startet der Agent an einem Einstiegspunkt und folgt den Links.

### Hands-on 3: Die Wissensbasis wird ein Obsidian-Vault

Zuerst wird Obsidian installiert (https://obsidian.md/download) und der Ordner `wissensbasis` über Manage Vaults und Open folder as vault als Vault geöffnet. Ein erster Blick gilt den Dateien, der Graph-Ansicht und den Eigenschaften. Dann folgen drei Prompts im AI Harness, und jedes Ergebnis wird geprüft, bevor der nächste Prompt folgt.

Bestand analysieren:

> Wir machen aus diesem Projektordner einen Obsidian-Vault. Analysiere knowledge/ und sources/: Welche Dokumenttypen gibt es, welche Konzepte kommen mehrfach vor, wo fehlen Verbindungen? Schlage ein Frontmatter-Schema, eine kleine Tag-Taxonomie und Wikilinks vor. Ändere noch nichts.

Vault anlegen:

> Setze den Vorschlag mit meinen Anmerkungen um: Frontmatter in jedem Dokument, darunter Summary, Kernpunkte, Synthese, Sources und Related, Wikilinks im Text und unter Related, eine TAG-TAXONOMY.md und eine HOME.md als Einstieg. Halte die neuen Regeln in CLAUDE.md fest. Lege für jeden Schritt einen Commit an.

Vault prüfen:

> Prüfe den Vault auf tote Wikilinks, Dokumente ohne Verbindung und Tags außerhalb der Taxonomie. Liste und begründe die Befunde und schlage Korrekturen vor. Ändere noch nichts.

Zum Schluss wird der Vault erneut in Obsidian angesehen, mit der Leitfrage, was die Graph-Ansicht jetzt zeigt.

### Kuratieren: Struktur und Inhalt

Kuratieren ist die laufende Pflege des Vaults, also verdichten, präzisieren, verknüpfen, bereinigen und archivieren. Ohne Kuration wächst der Vault und verliert an Nutzbarkeit. Zwei Arten unterscheiden sich darin, wie sicher sich prüfen und rückgängig machen lässt, was der Agent ändert.

Strukturelle Kuration
: Sie ändert Frontmatter, Tags, Links und MOCs. Die Prüfungen sind eindeutig, Änderungen leicht rückgängig zu machen.

> Aktiviere den Plan-Modus. Analysiere den Vault auf verwaiste Dokumente, tote Wikilinks, Dubletten, Tags außerhalb von TAG-TAXONOMY.md, unpassende Status-Felder und fehlende MOC-Einträge. Gib einen Plan nach Wirkung sortiert aus. Führe erst nach Bestätigung aus. Nie löschen, immer archivieren.

Inhaltliche Kuration
: Sie ändert Text, also Formulierungen, Dubletten, Widersprüche und veraltete Aussagen. Die Prüfungen sind Urteile, Änderungen schwer rückgängig zu machen.

> Analysiere die Wissensdokumente auf inhaltliche Redundanzen. Schlage pro Fund Zusammenführen, Trennen, Kürzen oder Belassen vor und begründe. Führe nichts aus. Regel: Keine Information geht verloren, im Zweifel belassen.

Beide Prompts sind Beispiele, die für den eigenen Vault angepasst werden.

### Vault-Governance

Vault-Governance macht die Regeln des Vaults explizit, in Dateien, die Mensch und Agent gleichermaßen lesen. Harness Governance regelt, was der Agent tun darf, Vault-Governance, wie das Wissen geordnet ist, mit dem er arbeitet. Vier Systemdokumente im Root tragen diese Regeln.

```
vault/
├── HOME.md          Einstieg, verlinkt alle Bereiche
├── TAG-TAXONOMY.md  kontrolliertes Vokabular
├── CLAUDE.md        Topografie und Regeln
└── ACTIVE-WORK.md   laufende Vorhaben, Status, nächster Schritt
```

CLAUDE.md enthält die Topografie des Vaults, also welcher Ordner welchem Zweck dient. Diese Struktur denkt der Mensch, ausgehend davon, wie er arbeitet und was er braucht, etwa Projekte, Fachwissen, Anträge, Verwaltung und Aufgaben. Weil der Harness CLAUDE.md bei jedem Sitzungsbeginn lädt, kennt der Agent den Vault vom ersten Satz an. Details stehen in Konventionen und MOCs, die er bei Bedarf nachlädt. Im Wissensdashboard aus Hands-on 1 bilden `knowledge/` und `sources/` die einfachste Form einer solchen Topografie.

Dasselbe Muster beschreibt Karpathy (2026) für eine vom LLM gepflegte Wissensbasis. Unveränderliche Quellen, ein vom LLM geschriebenes Wiki und ein Schema-Dokument wie CLAUDE.md oder AGENTS.md, das Struktur, Konventionen und Arbeitsabläufe festlegt und von Mensch und LLM gemeinsam weiterentwickelt wird. ACTIVE-WORK.md bündelt die laufenden Vorhaben mit Status und nächstem Schritt, sodass eine neue Session dort beginnt und weiß, woran gerade gearbeitet wird.

## Session 3: Agentic Engineering

### Fancy Research Tools

Fancy (research) tools sind kleine Forschungswerkzeuge, die Coding Agents aus einer gepflegten Wissensbasis bauen, meist als statische Anwendungen, die ohne Server im Browser laufen (https://dhcraft.org/fancy-research-tools/). Der Weg dorthin hat fünf Schritte, und bei jedem ist geklärt, wer ihn trägt.

1. Frage und Daten klären, also was das Werkzeug leisten soll und mit welchem Material. Das entscheidet der Mensch.
2. Wissen ordnen, also Projekt, Daten und Anforderungen in `knowledge/` festhalten. Das leisten Mensch und Agent gemeinsam.
3. In Meilensteinen bauen. Der Agent setzt um, der Mensch gibt frei.
4. Am Material prüfen, mit Tests, Review-Agent und fachlicher Sichtung durch den Menschen.
5. Nutzen und pflegen. Das Werkzeug läuft im Browser, und die Wissensbasis wächst mit.

Ein Befund aus der Prüfung ändert zuerst die Wissensbasis und erst danach den Code. Professionell wird ein solches Werkzeug durch Prüfung, Pflege und Weitergabe, was sich im Team lernen oder als Dienstleistung beauftragen lässt.

### Loop Engineering

Loop Engineering gestaltet das System, das den Agenten anstößt und prüft, statt ihn jedes Mal von Hand zu prompten. Das Beispiel ist das Analysewerkzeug aus Hands-on 4 als wiederkehrender Ablauf.

```
Auslöser                      Agent
neue Excel-Datei     ──────▶  liest knowledge/,
liegt im Ordner               aktualisiert den Bericht
     ▲                              │      ▲
     │                              ▼      ┆ Abweichung,
Freigabe                      Prüfskript   ┆ neuer Versuch
Mensch nimmt ab      ◀──────  Kennzahlen gegen
oder gibt zurück              Excel-Summen
```

Ein Auslöser, etwa eine neue Datei, ein Zeitpunkt oder ein Ereignis, startet den Agenten. Ein fest verdrahtetes Prüfskript läuft danach, und der Agent kann es nicht überspringen. Findet es eine Abweichung, beginnt eine innere Schleife mit einem neuen Versuch. Erst das geprüfte Ergebnis geht zur Freigabe an einen Menschen. Jeder Auslöser vervielfacht Anfragen und Tokens, deshalb gehören Abbruchbedingungen und Grenzen zur Gestaltung. Den Begriff erläutert das Video von IBM Technology aus Session 2.

### Subagents und Workflows

Ein Agent kann Teilaufgaben an weitere Agents abgeben. Anthropic unterscheidet dabei Workflows, die LLMs und Werkzeuge über vorab festgelegte Codepfade orchestrieren, von Agents, die Ablauf und Werkzeugnutzung selbst bestimmen (Anthropic, 2024). Drei Formen kommen in der Praxis vor.

Subagent
: Ein Agent mit eigenem Context Window erledigt eine abgegrenzte Aufgabe und liefert nur das Ergebnis zurück. Claude Code bringt Explore und Plan mit, eigene Agents liegen in `.claude/agents/`. Codex kennt die Rollen `explorer` und `worker`, eigene Agents liegen in `.codex/agents/` (OpenAI, 2026).

Dynamic Workflow
: Claude schreibt ein Orchestrierungsskript, verteilt Teilaufgaben auf viele parallele Subagents und lässt die Befunde von anderen Agents gegenprüfen, bis die Ergebnisse übereinstimmen. Ausgelöst wird ein Workflow durch die ausdrückliche Bitte darum oder durch die Einstellung ultracode, die Claude selbst entscheiden lässt, wann sich ein Workflow lohnt (Anthropic, 2026).

Parallele Sessions
: Eigenständige Sessions mit eigenem Ordner schicken einander Nachrichten und melden sich zurück, wenn sie fertig sind. Auf diese Weise ist die Vorbereitung dieses Workshops entstanden.

Mehr Agents kosten mehr. In Anthropics Multi-Agent-Research-System verbrauchten Agents etwa viermal, Multi-Agent-Systeme etwa fünfzehnmal so viele Tokens wie ein Chat, dafür lag das System auf einer internen Recherche-Evaluation deutlich über einem einzelnen Agenten (Anthropic, 2025). Ungeeignet ist der Ansatz, wenn alle Agents denselben Kontext brauchen oder die Aufgabe kaum parallelisierbar ist. OpenAI empfiehlt parallele Agents vor allem für lesende Aufgaben, weil gleichzeitig schreibende Agents leicht kollidieren.

### Determinismus so weit wie möglich ausreizen

Manche Aufgaben haben genau eine richtige Antwort, andere verlangen ein Urteil. Die Unterscheidung entscheidet, ob ein LLM die Aufgabe selbst lösen sollte.

Deterministisch
: Code, Formeln und Skripte liefern bei gleicher Eingabe die gleiche Ausgabe. Dazu gehören Summen, Budgets, Datumsangaben und Zählungen, Prüfungen wie die, ob jedes Feld ausgefüllt ist und die Summe stimmt, sowie das Umwandeln von Formaten.

Probabilistisch
: Das Urteil eines LLM oder eines Menschen kann bei gleicher Eingabe unterschiedlich ausfallen. Dazu gehören Zusammenfassen, Formulieren und Tonalität, Klassifizieren, Abwägen und Entscheiden sowie die Frage, ob ein Ergebnis plausibel ist.

Was ein Skript erledigen kann, soll ein Skript erledigen. Das LLM schreibt das Skript und rechnet nicht selbst.

### Qualität sichern

Qualität entsteht durch passende Prüfungen, unabhängiges Review und menschliche Abnahme. Vier Mechanismen tragen dazu bei.

Unabhängiges Review
: Ein zweiter Agent prüft mit frischem Kontext, als LLM-as-a-Judge nach festgelegten Kriterien. Seine Befunde werden am Material geprüft.

Mensch im Prozess
: Automatische Tests erfassen nicht alles. In einem Projekt waren alle Tests bestanden, doch Markierungen erschienen grau statt olivgrün, und erst die visuelle Prüfung fand den Fehler.

Fehler in Mechanismen überführen
: Ein gefundener Fehler wird zu einer dauerhaften Prüfung. Als in der Handy-Ansicht der Text unter dem ersten Bildschirm begann, kam ein Test dazu, der seitdem seine Position prüft.

Rechte und Freigaben
: Push, Versand und Veröffentlichung bleiben beim Menschen.

### Hands-on 4: Ein Analysewerkzeug aus Excel-Daten

Das Material liegt in [`data/`](data/README.md), vier Excel-Dateien aus der Northwind-Beispieldatenbank mit Bestellungen, Produkten, Kunden und Mitarbeitenden. In einem neuen Ordner `analyse` werden die Excel-Dateien abgelegt, dann startet eine neue Session im AI Harness mit Zugriff auf diesen Ordner. Die drei Prompts werden nacheinander ausgeführt, und jedes Ergebnis wird geprüft, bevor der nächste Prompt folgt.

Daten verstehen:

> Analysiere die Excel-Dateien in diesem Ordner: Welche Tabellen, Spalten und Beziehungen gibt es, welche Fragen lassen sich damit beantworten? Halte das in knowledge/data.md fest. Stell mir drei Fragen zu meinem Ziel. Ändere sonst noch nichts.

Werkzeug bauen:

> Baue ein Analysewerkzeug als Single-Page-Application im Browser. Alle Kennzahlen berechnet ein Skript aus den Excel-Dateien, nicht du selbst. Halte die Anforderungen in knowledge/requirements.md fest und arbeite in Meilensteinen.

Ergebnisse prüfen:

> Prüfe jede Kennzahl im Werkzeug gegen eine Referenz, die du direkt aus den Excel-Dateien berechnest. Liste und begründe Abweichungen. Ändere noch nichts.

Zum Schluss werden die Kennzahlen im Werkzeug mit eigenen Summen in Excel verglichen. Der zweite Prompt setzt die Regel aus der Determinismus-Folie um, der dritte die unabhängige Prüfung.

### Ausblick: Vorlagen für die eigene Arbeit

Vier Vorlagen aus laufender Arbeit zeigen, wie die Konzepte des Workshops in größeren Systemen aussehen. Es sind Research Previews, und ob sie für den produktiven Einsatz taugen, ist im eigenen Projekt zu prüfen.

Second Brain Vault
: Vorlage eines persönlichen Arbeitssystems mit synthetischen Beispielen (https://github.com/chpollin/second-brain-vault).

Grounded Vault
: Belegpflichtige Wissensbasis mit prüfbaren Quellenankern (https://github.com/DigitalHumanitiesCraft/grounded-vault).

Research Mission Control
: Rollen und Übergaben für mehrere Agenten und Arbeitsstränge (https://github.com/DigitalHumanitiesCraft/research-mission-control).

Promptotyping
: Methode, Skills und Vorlagen für Wissensdokumente (https://github.com/DigitalHumanitiesCraft/Promptotyping).

## Anhang

### Vibe Coding und Agentic (Knowledge and Research) Engineering

Vibe Coding
: Software durch natürlichsprachliche Aufträge und Ausprobieren entwickeln. Der erzeugte Code wird weitgehend ungeprüft übernommen (Karpathy, 2025).

Agentic Engineering
: Agentengestützte Softwareentwicklung gestalten. Agents schreiben, testen und überarbeiten Code. Menschen bestimmen Anforderungen und Handlungsspielräume und prüfen Umsetzung und Ergebnisse (Willison, 2026).

Agentic (Knowledge and Research) Engineering
: Vorgeschlagener Arbeitsbegriff für die Gestaltung und Prüfung agentengestützter Forschungsabläufe. Menschen und AI Agents nutzen dokumentiertes Projektwissen, um Quellen und Forschungsdaten zu bearbeiten und Werkzeuge zu entwickeln. Geprüfte Ergebnisse und bestätigte Entscheidungen ergänzen die Wissensbasis. Den Hintergrund bilden Allen, Stork und Groth (2023) und der Blogbeitrag „Haters gonna hate“ (https://dhcraft.org/excellence/blog/Vibe-Coding).

### Frontier-LLMs amplifizieren computergestützte Wissensarbeit

Benchmarks sind standardisierte Tests für KI-Modelle. Sie zeigen, wie gut ein Modell bestimmte Aufgaben löst und wo es Fehler macht, und automatisch prüfbare Ergebnisse helfen beim Training und bei der Bewertung. Die Folie nennt METR Time Horizons, SimpleBench, ARC-AGI-3, Terminal-Bench und SWE-bench.

Forschungsresultate und Sicherheitsvorfälle zeigen Fähigkeiten und Kontrollprobleme unter konkreten Bedingungen, ihre Übertragbarkeit bleibt aber zu prüfen. Die Folie führt dazu Ergebnisse von OpenAI in der Mathematik und zu den Navier-Stokes-Gleichungen sowie einen Vorfall zwischen OpenAI und Hugging Face im Zusammenhang mit Agent Swarms an.

Recursive Self-Improvement bedeutet, dass KI hilft, leistungsfähigere KI zu entwickeln, die wiederum die weitere Entwicklung vorantreibt. Die Folie hält das für sehr wahrscheinlich und stellt dazu Positionen gegenüber, von Naam (2026) über AI 2027 bis zu den AGI-Zeitleisten von 80,000 Hours, ergänzt um Interviews und Videos zu KI-Fortschritt und Risiken. Weitere Videos enthält die kuratierte Playlist der Lehrlinie.

### AI Watermarking

Ein Wasserzeichen soll erkennbar machen, ob ein Text oder ein Bild von einer KI stammt. Bei Text und Bild funktioniert das grundverschieden.

Beim Text-Watermarking wirkt das Wasserzeichen schon beim Schreiben. Ein LLM berechnet für jedes mögliche nächste Token eine Wahrscheinlichkeit und zieht daraus eines. Beim Watermarking erzeugt ein geheimer Schlüssel zusammen mit dem vorangehenden Text bei jedem Schritt einen Zufallswert, der die Auswahl leicht in eine bestimmte Richtung lenkt. Der Text bleibt gut lesbar, trägt aber ein statistisches Muster in der Wortwahl. Wer den Schlüssel hat, berechnet für einen Text einen Wert und vergleicht ihn mit einer Schwelle. Je länger der Text, desto verlässlicher das Ergebnis, und Umschreiben oder Übersetzen schwächt das Muster (Dathathri et al., 2024, Fig. 1, CC BY 4.0).

Beim Bild-Watermarking wird das fertige Bild markiert. Ein Encoder legt eine kurze Bitfolge unsichtbar ins Pixelmuster, ein Decoder liest sie wieder aus, schon bei einem einzelnen Bild. JPEG-Kompression und Zuschnitt übersteht das Wasserzeichen, gezielte Angriffe können es entfernen (Bui et al., 2023). Signierte Metadaten nach dem Standard C2PA sind ein zweiter Weg, die jeder prüfen kann, solange sie nicht entfernt wurden. Das Video *How Image Watermarking Works* von Computerphile (2026, https://youtu.be/h6j_ixGnpiY) erklärt den Bildteil.

Ein Wasserzeichen ist ein Hinweis und kein Beweis. Fehlt es, folgt daraus nicht, dass ein Mensch den Inhalt erstellt hat. Seit 2. August 2026 verlangt Art. 50 des AI Act von Anbietern, synthetische Inhalte maschinenlesbar zu kennzeichnen, und Watermarks sind dafür ein Baustein.

## Literatur

- Allen, B. P., Stork, L., & Groth, P. (2023). Knowledge Engineering Using Large Language Models.
- Anthropic (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents
- Anthropic (2025). How we built our multi-agent research system. https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic (2026). Introducing dynamic workflows in Claude Code. https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- Auer, C., et al. (2024). Docling Technical Report. arXiv:2408.09869. https://arxiv.org/abs/2408.09869
- Bui, T., et al. (2023). TrustMark: Universal Watermarking for Arbitrary Resolution Images. arXiv:2311.18297. https://arxiv.org/abs/2311.18297
- Dathathri, S., et al. (2024). Scalable watermarking for identifying large language model outputs. *Nature*. https://doi.org/10.1038/s41586-024-08025-4
- Dell’Acqua, F., et al. (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*, 37(2), 403–423. https://doi.org/10.1287/orsc.2025.21838
- Gans, J. (2026). A Model of Artificial Jagged Intelligence. arXiv:2601.07573. https://doi.org/10.48550/arXiv.2601.07573
- Jones, W., et al. (2017). Personal Information Management. In *Encyclopedia of Library and Information Sciences* (4. Aufl.). https://doi.org/10.1081/E-ELIS4-120053695
- Karpathy, A. (2025). Vibe Coding. Beitrag auf X, 2. Februar 2025.
- Karpathy, A. (2026). LLM Wiki. GitHub Gist, 4. April 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Kuster, J., et al. (2022). *Handbuch Projektmanagement* (5. Aufl.). https://doi.org/10.1007/978-3-662-65473-6
- Lindsey, J., et al. (2025). On the Biology of a Large Language Model. *Transformer Circuits*. https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- Liu (2026). Engineering and Governing the Agent Harness. UNU Macau Technology Report 1. https://unu.edu/publication/engineering-and-governing-agent-harness-technology-and-policy-framework-runtime-layer
- Mei, L., Yao, J., Ge, Y., et al. (2025). A Survey of Context Engineering for Large Language Models. arXiv:2507.13334. https://doi.org/10.48550/arXiv.2507.13334
- Meta AI (2025). Agents Rule of Two: A Practical Approach to AI Agent Security. https://ai.meta.com/blog/practical-ai-agent-security/
- OpenAI (2026). Subagents. https://learn.chatgpt.com/docs/agent-configuration/subagents
- Pollin, C. (2026). Promptotyping. Translating Research Data into Research Artefacts with Context and Agentic Engineering. https://docs.google.com/document/d/1_Q6kLFxvnvLMRizN2F_uTkpwsaJ-Cp0uBw4REKfhDlM/edit
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4. Aufl.). Pearson. https://aima.cs.berkeley.edu
- Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges. *Information Fusion*, 126, 103599. https://doi.org/10.1016/j.inffus.2025.103599
- Summerfield, C. (2025). *These Strange New Minds: How AI Learned to Talk and What It Means*. Viking.
- Willison, S. (2026). What is agentic engineering?
- Xu, W., Huang, C., Gao, S., & Shang, S. (2025). LLM-Based Agents for Tool Learning: A Survey. *Data Science and Engineering*, 10, 533–563. https://link.springer.com/article/10.1007/s41019-025-00296-9
- Zhong, H., & Zhu, S. (2026). AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents. arXiv:2605.13357. https://doi.org/10.48550/arXiv.2605.13357
