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

### Materialien und Kanäle

Begleitend zum Workshop gibt es Videos auf dem YouTube-Kanal von Digital Humanities Craft (https://www.youtube.com/@DigitalHumanitiesCraft), Folien zu früheren Veranstaltungen (https://chpollin.github.io/GM-DH), den Blog (https://dhcraft.org/excellence/blog) und eine öffentliche Zotero-Gruppenbibliothek mit der zitierten Literatur (https://www.zotero.org/groups/5319178/agki-dh). Alle Materialien dieser Lehrlinie, die laufend gepflegt und erweitert werden, liegen unter https://dhcraft.org/knowledge-context-agentic-engineering.

### Vorstellungsrunde

Die Runde klärt, mit welchen Voraussetzungen die Gruppe arbeitet. Gefragt wird nach dem Arbeitsbereich, nach den bisher genutzten KI-Modellen und Werkzeugen, nach Programmiervorkenntnissen etwa in Python oder JavaScript und danach, ob die Begriffe Context Window und Reasoning-Modell vertraut sind. Die letzte Frage ist praktisch. Für die Hands-ons braucht jede Person Zugang zu einem Frontier-LLM, etwa über ein Pro- oder Max-Abo, über Mistral oder lokal, und dazu einen laufenden AI Harness wie Claude Desktop, Codex oder Antigravity.

### Technische Vorbereitung

Claude Desktop lässt sich unter https://claude.com/de/download installieren. Die Einrichtung im Detail beschreibt der englischsprachige Foliensatz *Technical Preparation for Context, Knowledge and Agentic Engineering* (https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit).

### Lernziele und Ablauf

Nach dem Workshop können die Teilnehmenden

1. erklären, wie LLM, AI Agent und AI Harness zusammenwirken,
2. Projektwissen und Kontext so aufbauen und pflegen, dass ein AI Agent damit verlässlich arbeitet (Knowledge und Context Engineering),
3. agentische Arbeitsabläufe planen, ihre Ergebnisse prüfen und auf eigene Vorhaben übertragen (Agentic Engineering).

Der Workshop umfasst drei Sessions zu je zwei Stunden, online über Zoom.

| Session | Termin |
| --- | --- |
| 1 | Montag, 9.11.2026, 14:00–16:00 |
| 2 | Dienstag, 10.11.2026, 10:00–12:00 |
| 3 | Dienstag, 10.11.2026, 14:00–16:00 |

### Aufbauendes Beispiel und Ablauf

Über alle drei Sessions entsteht Schritt für Schritt eine Wissensbasis zu Agentic Engineering und Governance, mit einer Oberfläche im Browser. Jeder Schritt vertieft einen Aspekt des Agentic Engineering. Die Teilnehmenden kopieren die Prompts von den Folien in ihren AI Harness und arbeiten parallel mit. Während die Agents arbeiten, bespricht die Gruppe weitere Konzepte, deshalb lohnt es sich, den eigenen Harness dabei im Blick zu behalten.

Zwei Vorgaben gelten für den ganzen Workshop. Die teuersten Modelle (GPT-6 Astra, Claude Fable) verbrauchen das Nutzungskontingent rasch und sind für die Übungen nicht nötig. Opus reicht für den Hauptagenten, Subagents laufen auf Sonnet 5.5 oder GPT-6.1 Terra. Beim Datenschutz ist Vorsicht geboten, sobald personenbezogene oder sensible Daten im Spiel sind, die unter die Datenschutz-Grundverordnung (DSGVO) fallen, oder Anwendungen, die der EU AI Act regelt, etwa Entscheidungen über Personal.

## Session 1: LLMs, AI Agents und das erste Projekt

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

## Session 2: Kontext, Wissen und Steuerung

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

### Zugriff und Auto-Modus

Claude Code arbeitet mit den Rechten der Person, die es startet. Der Permission Mode legt fest, was ohne Rückfrage geschieht. Die fünf Modi reichen von wenig zu viel Autonomie.

| Mode | Verhalten |
| --- | --- |
| Plan | erkundet und plant, ändert nichts |
| Manual | fragt bei allem außer Lesen |
| Accept edits | bearbeitet Dateien ohne Rückfrage |
| Auto | ein Klassifikator prüft jede Aktion im Hintergrund |
| Bypass | alles ohne Prüfung, nur in isolierten Umgebungen |

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

## Session 3: Eine Kundenanfrage abwickeln

Für Session 3 gibt es noch keine Folien. Das Material liegt in [`data/`](data/README.md), eine synthetische Kundenanfrage per Mail mit vier Excel-Dateien aus der Northwind-Beispieldatenbank. Die Anfrage verlangt einen Workshop, Folien, eine kleine Referenz-Website und Entwürfe für Regeln zur KI-Nutzung und enthält bewusst personenbezogene Daten. Dieser Teil des Skriptums wird geschrieben, sobald die Folien stehen.

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

## Literatur

- Allen, B. P., Stork, L., & Groth, P. (2023). Knowledge Engineering Using Large Language Models.
- Dell’Acqua, F., et al. (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*, 37(2), 403–423. https://doi.org/10.1287/orsc.2025.21838
- Gans, J. (2026). A Model of Artificial Jagged Intelligence. arXiv:2601.07573. https://doi.org/10.48550/arXiv.2601.07573
- Karpathy, A. (2025). Vibe Coding. Beitrag auf X, 2. Februar 2025.
- Lindsey, J., et al. (2025). On the Biology of a Large Language Model. *Transformer Circuits*. https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges. *Information Fusion*, 126, 103599. https://doi.org/10.1016/j.inffus.2025.103599
- Summerfield, C. (2025). *These Strange New Minds: How AI Learned to Talk and What It Means*. Viking.
- Willison, S. (2026). What is agentic engineering?
- Xu, W., Huang, C., Gao, S., & Shang, S. (2025). LLM-Based Agents for Tool Learning: A Survey. *Data Science and Engineering*, 10, 533–563. https://link.springer.com/article/10.1007/s41019-025-00296-9
- Zhong, H., & Zhu, S. (2026). AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents. arXiv:2605.13357. https://doi.org/10.48550/arXiv.2605.13357
