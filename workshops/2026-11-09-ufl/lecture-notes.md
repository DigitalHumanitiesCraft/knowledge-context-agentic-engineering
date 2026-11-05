---
title: "Lecture Notes (Uni for Life 2026)"
workshop: 2026-11-09-ufl
created: 2026-08-20
updated: 2026-11-05
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

Zur Vorbereitung gehören Claude Desktop (https://claude.com/de/download) und der englischsprachige Foliensatz *Technical Preparation for Context, Knowledge and Agentic Engineering* (https://docs.google.com/presentation/d/19zybf1mABP3qM65GXv0xEGVososbhM03P9_INInYPj8/edit), der die Einrichtung im Detail beschreibt.

Die Lehrlinie *Knowledge, Context and Agentic Engineering* wird laufend gepflegt und erweitert.

- Website mit allen Materialien: https://dhcraft.org/knowledge-context-agentic-engineering
- Skriptum Deutsch: https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit
- Glossar: https://dhcraft.org/knowledge-context-agentic-engineering/glossary.de.html
- Video-Playlist: https://www.youtube.com/playlist?list=PLXY4kw40KBaY

Von Digital Humanities Craft kommen der YouTube-Kanal (https://www.youtube.com/@DigitalHumanitiesCraft), Folien früherer Veranstaltungen (https://chpollin.github.io/GM-DH), der Blog (https://dhcraft.org/excellence/blog), die öffentliche Zotero-Gruppenbibliothek mit der zitierten Literatur (https://www.zotero.org/groups/5319178/agki-dh) und Patreon (https://www.patreon.com/c/DigitalHumanitiesCraft).

### Lernziele und Ablauf

Der Workshop umfasst drei Sessions zu je zwei Stunden, online über Zoom. Session 1 findet am Montag, 9.11.2026, von 14 bis 16 Uhr statt, Session 2 am Dienstag, 10.11.2026, von 10 bis 12 Uhr und Session 3 am selben Tag von 14 bis 16 Uhr. Die Themen gehen über die Sessions hinweg ineinander über.

Den Rahmen bilden fünf Begriffe, die einem Video von IBM Technology folgen (*Agentic Engineering: 5 Terms Every AI Developer Should Know*, 2026, https://youtu.be/SIZsFGvtClM).

Agentic Engineering
: AI Agents arbeiten lassen. Menschen bestimmen Ziel, Grenzen und Abnahme.

Prompt Engineering
: Dem Agenten Ziel, Vorgaben und Zwischenschritte mitgeben.

Context Engineering
: Entscheiden, was der Agent bei jedem Schritt vor sich hat, weder zu wenig noch zu viel.

Knowledge Engineering
: Projektwissen in Dokumenten festhalten, die Mensch und Agent lesen, prüfen und weiterführen.

Harness Engineering
: Festlegen, welche Werkzeuge der Agent hat, was er ohne Freigabe darf und wie seine Arbeit geprüft wird.

### Aufbauendes Beispiel und Ablauf

Über alle drei Sessions entsteht Schritt für Schritt eine Wissensbasis zu Agentic Engineering und Governance, mit einer Oberfläche im Browser. Jeder Schritt vertieft einen Aspekt des Agentic Engineering. Die Teilnehmenden kopieren die Prompts von den Folien in ihren AI Harness und arbeiten parallel mit. Während die Agents arbeiten, bespricht die Gruppe weitere Konzepte, deshalb lohnt es sich, den eigenen Harness dabei im Blick zu behalten.

Zwei Vorgaben gelten für den ganzen Workshop. Die teuersten Modelle (GPT-6 Astra, Claude Fable) verbrauchen das Nutzungskontingent rasch und sind für die Übungen nicht nötig. Opus reicht für den Hauptagenten, Subagents laufen auf Sonnet 5.5 oder GPT-6.1 Terra. Beim Datenschutz ist Vorsicht geboten, sobald personenbezogene oder sensible Daten im Spiel sind, die unter die Datenschutz-Grundverordnung (DSGVO) fallen, oder Anwendungen, die der EU AI Act regelt, etwa Entscheidungen über Personal. Dasselbe gilt für Daten, die für die eigene Person oder das eigene Unternehmen wichtig sind.

## Session 1

### „Few-shotted for Breakfast“

Die Folie stellt Beiträge von Andrej Karpathy an den Anfang, die zeigen, wie schnell sich die Arbeit mit LLMs verändert hat (https://x.com/karpathy/status/2116957135661945283, https://x.com/karpathy/status/2004607146781278521). Daneben stehen zwei Sammlungen selbst gebauter Anwendungen (https://getartcraft.com/apps, https://hackertube.org). Wenn ein AI Agent Software nach Beschreibung baut, verschiebt sich eine alte Abwägung. Statt Lizenzen für Standardsoftware zu bezahlen oder sich an deren Grenzen zu reiben, lässt sich ein kleines Werkzeug genau für die eigenen Anforderungen bauen. Ob sich das im Einzelfall lohnt, hängt davon ab, wer das Werkzeug danach pflegt und prüft, und genau darum geht es im Rest des Workshops. Wer die technische Grundlage nachholen möchte, findet sie in Karpathys Vortrag *Deep Dive into LLMs like ChatGPT* (https://youtu.be/7xTGNNLPyMI).

### fancy (research) tools & workflows

Fancy (research) tools & workflows sind kleine Forschungswerkzeuge und Arbeitsabläufe, die Coding Agents aus einer gepflegten Wissensbasis bauen, meist als statische Anwendungen, die ohne Server im Browser laufen (https://dhcraft.org/fancy-research-tools). Die Folie nennt Beispiele aus der eigenen Arbeit.

- coOCR/HTR, Transkription von Handschriften und Drucken mit Prüfung durch Fachleute (https://dhcraft.org/co-ocr-htr/)
- teiCrafter, Auszeichnung von Transkriptionen in TEI-XML (https://dhcraft.org/teiCrafter/editor.html)
- CorrespExplorer, Briefdaten als Karte, Zeitleiste und Netzwerk (https://dhcraft.org/CorrespExplorer/)
- SZD OCR/HTR Pipeline (https://chpollin.github.io/szd-htr-ocr-pipeline/)
- Stefan-Zweig-Bibliographie (https://chpollin.github.io/klawiter-rescue/)

Zum Agentic Knowledge Engineering gehören Promptotyping (https://dhcraft.org/Promptotyping/), Grounded Vault (https://dhcraft.org/grounded-vault/) und die Agentic Edition Pipeline (https://github.com/DigitalHumanitiesCraft/agentic-edition-pipeline).

### LLMs bzw. AI Agents als „Jagged Alien Intelligences“

Die Fähigkeiten von LLMs sind gezackt verteilt (jaggedness). Ein Modell löst manche schwierige Aufgaben souverän und scheitert an scheinbar leichten. Eine Feldstudie mit Wissensarbeitenden zeigt diese „gezackte Grenze“ empirisch (Dell’Acqua et al., 2026), und Gans (2026) modelliert sie formal.

Auf der Seite der Modelleigenschaften stehen vier Punkte. LLMs arbeiten probabilistisch, sie können konfabulieren, also plausibel klingende, aber falsche Aussagen erzeugen, sie tragen Bias aus ihren Trainingsdaten und bleiben in ihrem Inneren schwer einsehbar. Ob ein LLM „rechnen“ kann, ist dafür ein gutes Prüfbeispiel. Die Interpretierbarkeitsforschung zeigt, dass ein Modell Additionen über andere interne Wege löst, als es auf Nachfrage selbst beschreibt (Lindsey et al., 2025). Sycophancy bezeichnet die Neigung, Nutzenden nach dem Mund zu reden. Schließlich bilden LLMs eine eigene Art von „Weltmodell“, das sich mit menschlichem Weltwissen nur teilweise deckt (Summerfield, 2025).

Auf der Seite der Interaktion stehen die Eigenschaften, die für die Arbeit mit Agents zählen. LLMs nutzen Werkzeuge (Tool Use), etwa Websuche oder das Ausführen von Code. Das Context Window wirkt wie eine Aufmerksamkeitsspanne, die später im Workshop genauer behandelt wird. Das Wissen des Modells endet am Knowledge Cut-off, und das Modell lernt im Gebrauch nicht kontinuierlich dazu. „Reasoning“ bedeutet bei aktuellen Modellen, dass sie vor der Antwort zusätzliche „Thinking“-Tokens erzeugen.

### Claude Code in der Claude Desktop App

Ein AI Harness ist die Software um ein LLM, die die Agentenschleife ausführt, Kontext und Werkzeuge bereitstellt und Grenzen durchsetzt. Zhong und Zhu (2026) beschreiben den Harness als eigene Laufzeitschicht für Agents, eine praxisnahe Anatomie liefert https://www.langchain.com/blog/the-anatomy-of-an-agent-harness. Beispiele sind Claude Code, OpenAI Codex, Cursor, Windsurf, OpenCode, Antigravity CLI, Qwen Code, Cline und GitHub Copilot. Das Modell liefert die Sprachfähigkeit, der Harness entscheidet, was der Agent sehen und tun darf. Deshalb unterscheiden sich zwei Harnesses mit demselben Modell im Ergebnis spürbar.

Die Folie zeigt die Oberfläche, mit der der Workshop arbeitet, und die Einstellungen, die vor dem ersten Hands-on geprüft werden.

- AI Agents und Tool Use sind sichtbar, weil jeder Werkzeugaufruf im Verlauf erscheint.
- Slash Commands sind Befehle an den Harness selbst, etwa `/context`.
- MCP, Connectors und Plugins binden externe Dienste und Erweiterungen an.
- Die Modellwahl steht für den Workshop auf Sonnet 5.5.
- Effort bzw. Reasoning steht auf low oder medium.
- Der Mode wird auf Auto gestellt.
- Usage und Context Window zeigen, wie viel Kontingent und Kontext verbraucht sind.

### Prompt Engineering ist so 2025!

Die Folie zerlegt den Prompt aus Hands-on 1 in seine Bausteine. Der erste Absatz definiert den Task und legt mit dem Hinweis auf den Live-Workshop Zielgruppe und Stil fest. Die Bitte um drei Fragen baut Kontext in einem Frage-Antwort-Spiel auf. Die Fragen zur Aufteilung der Recherche, zu den Qualitätskriterien und zur Destillation steuern den Prozess, weil der Agent erst nach dem OK weiterarbeitet. Die Regeln für die Webrecherche sind Vorgaben (Constraints).

Die Form eines Prompts ist bei aktuellen Modellen weitgehend egal. Entscheidend sind das Ziel, das nötige Wissen und die Erfolgskriterien. Die Qualität entsteht zunehmend außerhalb des Prompts, im Kontext (Context Engineering) und in der Umgebung, die die Arbeit steuert und prüft (Harness Engineering). Der Rest des Workshops behandelt genau diese beiden Ebenen.

### Hands-on 1: Webrecherche und Wissensdokumente

Das erste Hands-on beginnt mit einem neuen, leeren Ordner, etwa `wissensbasis`. Im AI Harness startet eine neue Session mit Zugriff auf genau diesen Ordner. Dann wird der folgende Prompt kopiert und abgeschickt. Auf die Rückfragen des Agenten darf man frei antworten, auch in eigenen Worten statt mit einer der angebotenen Optionen.

> Ich möchte eine Wissensbasis zu „Agentic Engineering und Governance“ aufbauen, zugeschnitten auf meine Arbeit und meine Organisation. Wir sind in einem Live-Workshop: Antworte kompakt, sachlich und ohne technische Vorkenntnisse verständlich.
>
> 1. Stell mir drei Fragen zu meiner Rolle, meiner Organisation und dazu, wofür ich AI Agents einsetzen will.
> 2. Beantworte mir dann diese Fragen und warte auf mein OK:
>    - Wie teilst du die Recherche auf 2 Subagents (Sonnet 5.5; max 8 Quellen pro Agent) auf?
>    - Mit welchen drei Kriterien prüfst du die Qualität einer Quelle, und welche Kategorien schlägst du vor?
>    - Wie destillierst du das Wissen, und welche Dokumente entstehen in knowledge/?
> 3. Nach meinem OK recherchierst du im Web. Dabei gilt:
>    - Nur Quellen, die 2026 veröffentlicht wurden, Datum an der Quelle geprüft.
>    - Je Quelle das Original in sources/ (PDF oder Webseite als Text), benannt nach Herausgeber, Datum und Kurztitel.
>    - Das destillierte Wissen liegt als Markdown-Dokumente in knowledge/. Jede Aussage verweist auf ihre Datei in sources/ mit Fundstelle. Eine Quellenliste in knowledge/ nennt Titel, Herausgeber, Datum, Link und Kategorie.

Die Leitfrage während der Ausführung lautet, was alles passiert. Die Gruppe beobachtet, welche Werkzeuge der Agent aufruft, wann er nachfragt und wann er anhält. Danach folgen zwei Follow-up-Prompts.

> Können wir noch etwas optimieren? Liste und Begründungen. Definiere unser Ziel in einem Satz.

> Übernimm die Verbesserungen und leg los!

Die Prüfung des Datums an der Quelle kostet Zeit, und sie ist nötig. Im Probelauf übernahm der Hauptagent sonst falsche Datumsangaben aus den Berichten der Subagents. Die Konzepte dieses Hands-on sind Markdown, Wissensdokumente, AI Agent und Tool Use sowie Subagents.

### Hands-on 1: Ergebnis eines Durchgangs

Die Ergebnisse sehen bei jeder Person etwas anders aus, ähneln einander aber. Vorgegeben waren die Ordner `knowledge/`, `sources/` und `scripts/`. Der Agent hat von sich aus ein Python-Skript `scripts/check_kb.py` angelegt, das die Wissensbasis prüft, sowie die Markdown-Dokumente `INDEX.md` und `journal.md`.

Zwei Fragen führen zum nächsten Abschnitt. Warum ist PDF für LLMs ein schwieriges Format, und was ist ein Word- oder Excel-Dokument eigentlich? Ein PDF hält fest, wo Zeichen auf einer Seite stehen, und nicht, wie ein Text gegliedert ist. Überschriften, Lesereihenfolge und Tabellen muss ein Programm erst wieder erschließen. Word- und Excel-Dateien sind gepackte Ordner mit XML-Dateien, deren Inhalt zwischen viel Formatierungsangaben steht.

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

### AI Agent & Tool Use

Ein AI Agent ist ein System, in dem ein LLM für ein festgelegtes Ziel Schritt für Schritt die nächste Aktion wählt, darunter Tool Use. Das Modell formuliert einen Werkzeugaufruf, etwa eine Websuche oder das Lesen einer Datei, den eine Software außerhalb des Modells ausführt. Das Ergebnis fließt in die nächste Entscheidung ein. Die Definition folgt den Übersichten von Sapkota, Roumeliotis und Karkee (2025) sowie Xu et al. (2025).

Ein Beispiel zeigt die Schleife. Auf den Prompt „Fass mir zusammen, worum es in diesem Projekt geht.“ entscheidet der Agent selbst über die Schritte. `ls` zeigt, was im Projektordner liegt, und dort gibt es einen Ordner `knowledge`. `cd .\knowledge\` wechselt in diesen Ordner, `ls` zeigt dort `project.md`, und `cat .\project.md` öffnet den Text, aus dem der Agent die Zusammenfassung schreibt. Tool Use heißt, dass der Agent selbst entscheidet, welches Werkzeug er als Nächstes einsetzt. Jedes Ergebnis bestimmt den nächsten Schritt.

### Subagents

Ein Subagent ist ein AI Agent, dem ein anderer Agent eine abgegrenzte Aufgabe übergibt. Er arbeitet mit eigenem Context Window, ohne den bisherigen Verlauf, mit eigenen Anweisungen, Werkzeugen und Modell, und gibt nur das Ergebnis zurück. Im Hauptverlauf landet nur dieses Ergebnis.

Ein Reviewer ohne Vorwissen kann so als LLM-as-a-Judge urteilen, weil er den Verlauf nicht kennt, der zum Ergebnis geführt hat. Teilaufgaben laufen gleichzeitig, und das Modell lässt sich der Schwierigkeit der Aufgabe anpassen. Subagents lohnen sich für umfangreiche, abgegrenzte Aufgaben wie eine Webrecherche. Für Kleinigkeiten lohnen sie sich nicht, ebenso wenig dort, wo alle Agents denselben Kontext brauchen. Die Dokumentation steht unter https://code.claude.com/docs/en/sub-agents.

### Hands-on 2: Wissensdokumente destillieren

Ein Wissensdokument ist eine strukturierte Aufzeichnung externalisierten Wissens, destilliert aus Quellen, Daten oder Erfahrung zur Wiederverwendung durch Menschen und KI-Agenten. Vier Eigenschaften machen ein gutes Wissensdokument aus. Es ist für Menschen und KI lesbar, kompakt, in offenen Formaten wie Markdown übertragbar und kuratierbar, also prüfbar, korrigierbar und erweiterbar.

Das zweite Hands-on schärft die Wissensbasis mit einer Leitfrage. Der Prompt hat drei Teile.

> Schlag mir aus meinen Antworten drei Leitfragen vor, die unsere Wissensbasis beantworten soll, und halte meine Wahl mit meinem Profil in knowledge/project.md fest.
>
> Destilliere dann mit Subagents (Sonnet 5.5) jede Quelle in sources/ in einer Markdown-Datei zusammen: was sie zur Leitfrage sagt, mit Seitenangabe. Die PDFs bleiben liegen.
>
> Überarbeite danach knowledge/ aus diesen Dateien im Hinblick auf die Leitfrage und sag mir vorher, was du ändern willst.

Das erste Wissensdokument ist `knowledge/project.md`.

```markdown
# Projekt
Wissensbasis zu Agentic Engineering
und Governance für meine Organisation.

## Leitfrage
Welche Regeln brauchen wir, bevor AI
Agents mit internen Daten arbeiten?
```

Ein Follow-up-Prompt prüft das Ergebnis.

> Ist alles korrekt? Gibt es Redundanzen? Können wir die gleiche Information ohne Informationsverlust kompakter schreiben? Liste und begründe! Setze das dann alle um!

Danach lohnt der Blick darauf, wie voll das Context Window ist. `/context` zeigt es, `/compact` schafft Platz.

### Context Window managen

Ein Context Window bezeichnet den Textausschnitt, den ein LLM bei der Verarbeitung oder Erzeugung von Sprache auf einmal berücksichtigen kann. Eingabe und Ausgabe teilen sich diesen Raum. Bei einem Context Window von 8000 Tokens passen 6000 Tokens Eingabe und 1500 Tokens Ausgabe hinein. Bei 10000 Tokens Eingabe ist das Fenster überschritten, und ältere Teile fallen heraus oder müssen gekürzt werden.

Context Rot beschreibt, dass die Leistung eines Modells mit wachsender Eingabelänge nachlässt, lange bevor das Fenster voll ist (Chroma, 2025, https://research.trychroma.com/context-rot). Ein voller Verlauf ist deshalb auch dann ein Problem, wenn er technisch noch hineinpasst. Zwei Videos vertiefen das Thema, *What is a Context Window? Unlocking LLM Secrets* (https://youtu.be/-QVoIxEpFkM) und *Context Engineering for AI Agents: 4 Failure Modes to Avoid* (https://www.youtube.com/watch?v=BwXremQ-i6I).

Zwei Slash Commands machen das Context Window in Claude Code handhabbar. `/context` zeigt, wie voll das Context Window ist und womit. `/compact` ersetzt den Verlauf durch eine Zusammenfassung, danach werden CLAUDE.md und die zuletzt bearbeiteten Dateien neu geladen. Was nur im Gespräch stand und nicht in einer Datei, kann dabei verloren gehen, und genau deshalb gehört dauerhaftes Wissen in Wissensdokumente.

### AGENTS.md / CLAUDE.md

AGENTS.md und CLAUDE.md sind Markdown-Dateien mit dauerhaften Anweisungen für einen AI Agent, also Projektzweck, Arbeitsregeln und Verweise auf Wissen. Der Harness lädt sie bei jeder Session und nach `/compact`. AGENTS.md ist das offene Format, das viele Harnesses lesen (https://agents.md), CLAUDE.md die Entsprechung in Claude Code (https://code.claude.com/docs/en/memory). `/init` untersucht das Projekt und legt die CLAUDE.md an, und der Befehl wird im Workshop gleich an dieser Stelle ausgeführt.

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
- index.html per Doppelklick öffnen

## Regeln
- Nur Quellen aus 2026
- Quellen nur in sources/
- knowledge/ wird nie veröffentlicht
```

### Hands-on 3: Wissensbasis nutzen

Das dritte Hands-on fragt die Wissensbasis ab und erzeugt daraus ein Ergebnis. Zwei Beobachtungen begleiten es.

Suchen (Retrieval)
: AI Agents suchen über das Terminal, mit Volltextsuche und regulären Ausdrücken, also Suchmustern für Text. Sprechende Dateinamen wie `AEPD_2026-02_agentic-artificial-intelligence` werden eher gefunden. Es lohnt sich zu beobachten, mit welchen Befehlen der eigene Agent sucht.

Erzeugen
: Inhaltlich wird immer in Markdown gearbeitet. PDF und Word erzeugt der Agent mit Code, das dauert länger.

Der Prompt fragt nach Governance für die eigene Organisation.

> Wie können wir mit dem Wissen aus unserer Wissensbasis Governance für AI Agents in meiner Organisation entwickeln? Stell mir vorher drei Fragen zu meiner Organisation und zu den Daten, mit denen wir arbeiten.
>
> Antworte nur aus knowledge/ und sources/ und nenne zu jeder Aussage die Datei. Wo die Wissensbasis nichts hergibt, sag es und schlag mir eine Websuche mit Subagents vor. Neue Quellen kommen wie die bisherigen nach sources/ und in die Wissensdokumente.
>
> Führe das Ergebnis in knowledge/governance-entwurf.md zusammen.

Danach entsteht aus dem Entwurf ein Dokument zum Weitergeben.

> Erzeuge ein ansprechendes PDF mit der ausformulierten Governance.

Wer die Fragen zur eigenen Organisation zu persönlich findet, kann sie für eine Musterfirma beantworten. Im Probelauf trug das ebenso gut.

### KI-Governance auf zwei Ebenen

Governance für KI-Agenten hat zwei Gegenstände, die Daten und den Agenten selbst. Fünf Fragen gelten für beide Ebenen.

Sichtbarkeit
: Wo liegen sensible Daten, und wohin fließen sie? Welche Tools, Konnektoren und Modelle nutzt der Agent?

Klassifikation
: Wie sensibel sind die Daten? Welche Inhalte und Erweiterungen sind vertrauenswürdig?

Rechtsraum
: Wo werden Daten verarbeitet, und welches Recht gilt? Wo läuft das Modell, und lässt sich der Anbieter wechseln?

Zugriff
: Wer darf auf welche Daten zugreifen? Was darf der Agent ohne Freigabe tun?

Nachweis
: Sind die Datenflüsse protokolliert? Werden Tool-Calls und Freigaben aufbewahrt?

Die Datenebene vertieft ein Video von IBM Technology (*Can Your AI Use Sensitive Data Safely? 5 Capabilities You Need*, 2026, https://www.youtube.com/watch?v=jnP9AgtX0qo).

### Permission Modes und Autonomie

Claude Code arbeitet mit den Rechten der Person, die es startet, auf ihrem Rechner. Der Permission Mode legt fest, was der Agent ohne Rückfrage tun darf, also wie viel Autonomie man ihm gibt. Die fünf Modi reichen von wenig zu viel Autonomie.

| Mode | Verhalten | Wann |
| --- | --- | --- |
| Plan | erkundet und plant, ändert nichts | für die Spezifikation, bevor etwas gebaut wird |
| Manual | fragt bei allem außer Lesen | wenn man jeden Schritt selbst freigeben will |
| Accept edits | bearbeitet Dateien ohne Rückfrage | wenn der Plan steht und Git jede Änderung rückgängig machen kann |
| Auto | Lesen und Bearbeiten im Projekt frei, alles andere prüft ein Klassifikator | für die tägliche Arbeit, eine Garantie ist das nicht |
| Bypass | alles ohne Prüfung | nur in einer abgeschotteten Testumgebung (Sandbox) |

Im Modus Auto prüft ein Klassifikator jede Aktion, und er kann sich irren. Eine feste Grenze setzt erst eine Regel in den Einstellungen. Einige Bereiche ändert der Agent nie ohne Rückfrage, etwa den Versionsverlauf des Projekts und seine eigenen Einstellungen. Die Dokumentation steht unter https://code.claude.com/docs/en/permission-modes.

### Autonomie und Zugriff

Die Folie ordnet Agenten danach, wie selbstständig sie handeln und worauf sie zugreifen dürfen. Je mehr von beidem zusammenkommt, desto mehr Absicherung braucht der Einsatz. Die Einordnung folgt dem Technologiebericht der United Nations University zum Agent Harness (Liu, 2026).

### AI Slop & De-Slopification

AI Slop sind KI-erzeugte Inhalte von geringer Qualität. Merriam-Webster hat „Slop“ zum Wort des Jahres 2025 gewählt, und Willison (2024) hat den Begriff für unerwünschte KI-Inhalte geprägt. Auch ein gutes Ergebnis trägt oft Spuren davon, etwa zu viele Ebenen, Farben und Markierungen, wenn es ungeprüft übernommen wird. Im Beispiel der Folie stehen orange Linien, farbige Marken, graue Quellen, Punkte und eine Legende in einem einzigen Absatz. Wenn alles markiert ist, ist nichts markiert.

De-Slopification heißt, diese Spuren zu erkennen und zu entfernen, bevor das Ergebnis weitergegeben wird. Für das PDF aus Hands-on 3 lautet der Prompt so.

> Ist dieses PDF wirklich gut lesbar? Sieh dir jede Seite als Bild an und liste auf, was überladen wirkt oder nach AI Slop aussieht, mit Begründung. Setz die Verbesserungen dann um, erzeuge das PDF neu und zeig mir eine Seite.

Das Video *How to Deslopify Your AI* (https://youtu.be/QSZKZHeGZr4) vertieft das Thema.

### Skills: ein PDF-Skill

Ein Skill ist gespeichertes Anwendungswissen, ein Arbeitsablauf, den man einmal durchgearbeitet hat, als Markdown-Datei mit `name` und `description` im Kopf und der Anleitung darunter. Er liegt in `.claude/skills/<name>/SKILL.md`, optional mit Skripten und Vorlagen. Der Harness lädt zunächst nur die description und die Anleitung erst, wenn die Aufgabe passt. Darin liegt der Unterschied zu CLAUDE.md, die in jeder Session gilt. Aufgerufen wird ein Skill automatisch über seine description oder direkt, hier mit `/governance-pdf`.

Der Prompt macht aus dem Weg von der Recherche bis zum PDF einen Skill.

> Analysiere, wie wir in dieser Konversation von der Recherche bis zum PDF vorgegangen sind, und mach daraus einen Skill unter .claude/skills/ in diesem Repository. Sag mir am Ende, wie man ihn aufruft.

```markdown
---
name: governance-pdf
description: Gut lesbares PDF aus Markdown.
---
# PDF erstellen
1. Inhalt in Markdown fertigstellen.
2. PDF mit einem Skript erzeugen.
3. Seiten als Bild prüfen.
## Design
- Nur Überschriften, Fließtext, Fußnoten.
- Pflicht, Empfehlung: eigene Abschnitte.
- Eine Akzentfarbe, keine Linien.
```

Der Agent leitet den Skill aus dem erprobten Ablauf ab. Er ist damit ein Agentenprodukt und wird wie jede CLAUDE.md geprüft, bevor man sich auf ihn verlässt. Die Dokumentation steht unter https://code.claude.com/docs/en/skills.

### Zwischenfazit

Drei Fragen schließen Session 1 ab. Wo in der eigenen Arbeit wäre eine solche Wissensbasis nützlich, und welche Daten dürften dort nicht hinein? War noch nachvollziehbar, was der Agent gerade tut, oder wurde es irgendwann zu viel? Was fehlt noch, um das ab morgen allein zu machen?

Die Begriffe der Session ordnen sich so.

- LLM als Jagged Alien Intelligence
- Agent und Harness mit Tool Use, Subagent, LLM-as-a-Judge, Permission Modes und Skills
- Prompt Engineering
- Knowledge Engineering mit Wissensdokument, Markdown und Destillieren
- Context Engineering mit Context Window, Context Rot, `/context` und `/compact`
- Governance

## Session 2

### Hands-on 4: Wissensdashboard

Das vierte Hands-on baut eine Oberfläche über die Wissensbasis. Es beginnt in einer neuen Session im Ordner `wissensbasis` oder mit `/clear`. `/compact` würde dagegen eine Zusammenfassung des alten Chats behalten. Der erste Prompt verschafft dem Agenten einen Überblick.

> Worum geht es in diesem Ordner? Verschaff dir einen Überblick über alle Dateien und fasse kurz zusammen, was wir wissen, was wo liegt und was noch offen ist. Antworte kompakt und ohne technische Vorkenntnisse verständlich. Ändere nichts.

Dann wird der Plan-Modus eingeschaltet und der zweite Prompt abgeschickt. Die Rückfragen werden beantwortet, der Plan geprüft und freigegeben.

> Plane ein Dashboard, mit dem ich unsere Wissensbasis durchsuchen kann, und erstelle dafür einen Implementierungsplan mit Meilensteinen:
>
> - Single-Page-Application mit HTML, CSS und JavaScript, die sich per Doppelklick auf index.html öffnet, ohne Server.
> - Links eine Sidebar mit Suche und Filtern nach Kategorie, Herausgeber, Datum und Art (Quelle oder Wissensdokument).
> - Rechts die Trefferliste, ein Klick zeigt das Dokument lesbar an, mit Link zum Original.
> - Ein Skript liest knowledge/ und sources/ und erzeugt daraus die Daten für das Dashboard.
> - Ein helles, sachliches Arbeitswerkzeug ohne AI Slop.
>
> Stell mir Fragen, wo etwas unklar ist.

Zum Schluss wird das Dashboard im Browser geöffnet und ausprobiert.

### Die erste Iteration des Dashboards

Die Webseite besteht aus vier einfachen Bausteinen. HTML legt die Struktur fest, CSS das Design und JavaScript das Verhalten, etwa Suchen und Filtern. Die Daten erzeugt ein Skript aus `knowledge/` und `sources/`.

Ein Doppelklick auf `index.html` öffnet die Seite. Das Skript legt die Daten dafür als JavaScript-Datei neben die Seite, weil der Browser JSON-Dateien ohne Server nicht lädt. Die Seite läuft nur auf dem eigenen Rechner. Einen lokalen Server und eine Portnummer braucht es so nicht, und gerade diese beiden waren im Probelauf die erste Hürde für Menschen ohne technischen Hintergrund.

Kleinere Werkzeuge und Skripte, deren Ergebnisse man selbst prüfen kann, darf man vibe coden, also den Code nicht lesen und nur das Ergebnis testen, auf eigene Verantwortung. Mit mehr Erfahrung in Softwareentwicklung kommt man weiter. Der Workshop setzt bewusst auf einfache Technologien, weil gerade wer nicht Software entwickelt von kleinen Werkzeugen profitiert, die sich lesen und prüfen lassen.

### Hands-on 4: Follow-Up Prompts

Die erste Iteration ist selten fertig. Die Folie bündelt fünf Wege, die weiterführen.

Feedback geben
: Man beschreibt in Text, was stört, und hängt einen Screenshot an.

> Hier ist mein Feedback zum Screenshot:
> - Helleres, ruhigeres UI ohne AI Slop.
> - …

Self-Verification und Self-Refine
: Das Modell prüft das eigene Ergebnis gegen den Plan und verbessert es auf Grundlage dieser Prüfung.

> Ist alles umgesetzt, was im Plan stand? Liste Abweichungen auf und begründe sie.

Subagent als LLM-as-a-Judge
: Ein Subagent prüft unabhängig, ohne den Verlauf zu kennen. Im Probelauf fand diese Prüfung Fehler, die die eigenen Tests des Agenten übersehen hatten.

> Lass einen Subagenten das Dashboard kritisch prüfen und konkrete Verbesserungen vorschlagen. Ändere noch nichts, wir besprechen seine Befunde.

Refactoring
: Dieselbe Prüfung lässt sich auf den Code anwenden.

> Was sollten wir am Code refactoren? Liste und begründe, ändere noch nichts.

Wissen kuratieren
: LLMs erzeugen immer Rauschen, und man muss immer wieder aufräumen. Kuratieren heißt auswählen, prüfen, ordnen und erschließen, kontextualisieren, korrigieren, ergänzen, aussortieren und erhalten.

> Was muss jemand wissen, um das Projekt weiterzuführen? Bring knowledge/ auf den aktuellen Stand, ohne Belege und offene Fragen zu verlieren. Sag mir vorher, was du ändern willst.

### Wissensdashboard: ein Beispiel zum Ausprobieren

Die Folie zeigt das Ergebnis eines Durchgangs mit dem Prompt aus Hands-on 4. Der Link zum Ausprobieren folgt nach dem Probelauf.

### Vibe Coding & Agentic (Knowledge and Research) Engineering

Vibe Coding
: Software durch natürlichsprachliche Aufträge und Ausprobieren entwickeln. Der erzeugte Code wird weitgehend ungeprüft übernommen (Karpathy, 2025).

Agentic Coding und Agentic Engineering
: Agentengestützte Softwareentwicklung gestalten. Agents schreiben, testen und überarbeiten Code. Menschen bestimmen Anforderungen und Handlungsspielräume und prüfen Umsetzung und Ergebnisse (Willison, 2026a).

Agentic (Knowledge and Research) Engineering
: Vorgeschlagener Arbeitsbegriff für die Gestaltung und Prüfung agentengestützter Forschungsabläufe. Menschen und AI Agents nutzen dokumentiertes Projektwissen, um Quellen und Forschungsdaten zu bearbeiten und Werkzeuge zu entwickeln. Geprüfte Ergebnisse und bestätigte Entscheidungen ergänzen die Wissensbasis. Den Hintergrund bilden Allen, Stork und Groth (2023) und der Blogbeitrag „Haters gonna hate“ (https://dhcraft.org/excellence/blog/Vibe-Coding).

### Knowledge Engineering

Drei etablierte Felder tragen zum Knowledge Engineering bei.

Personal Information Management
: Der Umgang mit eigener Information über Formate und Orte hinweg. Das Kernproblem ist Fragmentierung. Die Tätigkeiten sind Behalten, Finden und Wiederfinden sowie Pflegen und Organisieren (Jones et al., 2017).

Projektmanagement
: Die systematische Planung, Steuerung und Kontrolle von Vorhaben innerhalb definierter Rahmenbedingungen, in den Phasen Initiierung, Planung, Durchführung, Überwachung und Steuerung sowie Abschluss (Kuster et al., 2022).

Wissensmodellierung
: Die Konstruktion einer Wissensbasis, in der die Konzepte einer Domäne identifiziert, formal repräsentiert und abfragbar gemacht werden. Der Weg führt von den Fragen über Wissenserwerb, Vokabular, Kodierung und Instanzen bis zu Abfragen, Inferenz und Evaluation (Russell & Norvig, 2020).

Knowledge Engineering verbindet die drei Felder. Es baut Wissen so auf und pflegt es so, dass Menschen und AI Agents damit arbeiten können. Wer eine Domäne versteht und ihre Begriffe, Regeln und Entscheidungen formal festhält, kann sie dem Agenten als genaue Anforderungen übergeben.

### Obsidian

Obsidian ist ein Wissensmanagementsystem, das Notizen als Markdown-Dateien in einem lokalen Ordner speichert. Dieser Ordner heißt Vault. Die Daten bleiben auf dem eigenen Computer, das Dateiformat ist offen, und ein Cloud-Konto ist nicht nötig (https://obsidian.md).

Ein Vault kann auf drei Ebenen arbeiten. Auf der ersten dient er der persönlichen Information, also Ablage und Wiederfinden im Sinne des Personal Information Management. Auf der zweiten trägt er Projekt und Arbeit, etwa laufende Vorhaben, Workshop- und Publikationsplanung. Auf der dritten bildet er Wissensstruktur ab, von informeller Strukturierung mit Links, Tags und Maps of Content bis zu formaler Modellierung mit Dokumenttypen, Relationen und Schemata.

### Hands-on 5: Wissens-Vault bauen

Die These hinter diesem Hands-on lautet, dass ein Projekt umso mehr Wissensstruktur braucht, je komplexer es ist, so wie größere Vorhaben mehr Projektmanagement brauchen. Zuerst wird Obsidian installiert (https://obsidian.md/download). Dann startet eine neue Session, und in Obsidian wird über Manage vaults und Open folder as vault genau der Ordner `wissensbasis` geöffnet. Wer einen übergeordneten Ordner öffnet, bekommt einen zweiten Vault im ersten, im Probelauf entstand so ein Ordner `.obsidian/.obsidian/`. Ein erster Blick gilt dem Graphen. Dann folgen drei Prompts.

Prompt 1 plant. Der Agent klärt den Zweck und schlägt eine Struktur vor.

> Wir machen aus diesem Ordner einen Obsidian-Vault. Frag mich zuerst, wofür ich ihn brauche: für ein Projekt, für mein persönliches Wissen oder für beides. Schlag mir danach vor: einen Frontmatter-Kopf für jedes Dokument in knowledge/, eine kleine Tag-Taxonomie, Wikilinks zwischen verwandten Dokumenten (nur unter Related), eine HOME.md als Map of Content und eine ACTIVE-WORK.md mit dem, was läuft, den nächsten Schritten und den offenen Fragen. Ändere noch nichts.

Prompt 2 baut. Der Agent setzt die Struktur um, hält die Regeln in CLAUDE.md fest und prüft. Die Bitte, nach jedem Schritt zu zeigen, was sich geändert hat, setzt dem Umbau eine Grenze. Ohne sie führte „Setz um“ im Probelauf zu großen Umbauten auf einmal.

> Setz den Vorschlag Schritt für Schritt um, mit einem Commit je Schritt, und zeig mir nach jedem Schritt, was sich geändert hat. Halte in CLAUDE.md fest, wofür der Vault da ist, was wo liegt und welche Regeln gelten. Lass .obsidian/ unverändert. Prüf am Ende auf tote Links, Dokumente ohne Verbindung und Tags außerhalb der Taxonomie, und ob das Dashboard noch funktioniert.

Prompt 3 kuratiert. Der Agent schlägt Verbesserungen vor, und man gibt sie frei. Strukturelle Kuration ändert Frontmatter, Tags, Links und MOCs, ihre Prüfungen sind eindeutig und die Änderungen leicht rückgängig zu machen. Inhaltliche Kuration ändert Text, ihre Prüfungen sind Urteile, und Änderungen lassen sich schwer zurücknehmen. Deshalb trennt der Prompt beide.

> Kuratiere den Vault. Prüf die Struktur auf Dubletten, unpassende Status-Felder und fehlende MOC-Einträge und den Inhalt auf Redundanzen. Trenn die Befunde nach Struktur und Inhalt, schlag pro Fund Zusammenführen, Trennen, Kürzen oder Belassen vor, begründe und sortiere nach Wirkung. Setz erst nach meiner Freigabe um. Lösche nichts, im Zweifel belassen.

### Das Wissensdokument im Vault

Im Vault bekommt das Wissensdokument einen Kopf, Tags und Relationen.

```markdown
---
type: knowledge
created: 2026-11-10
status: draft
tags: [agents, concepts, papers]
---
# Agent Governance
## Summary
Permission Modes regeln …
## Kernpunkte
## Synthese
## Sources
## Related
- [[Permission Modes]]
- [[Hooks]]
```

Kopf
: Frontmatter in YAML, einem Format aus Schlüssel und Wert. Typ, Datum, Status und Tags machen den Vault abfragbar.

Tags
: Je ein Tag aus Thema, Funktion und Quelle. Das Thema sagt, worum es geht (`agents`, `policies`, `risks`), die Funktion, welche Art Dokument vorliegt (`concepts`, `mocs`, `workflows`), und die Quelle, woher das Wissen stammt (`papers`, `websites`, `originals`). Neue Tags entstehen nur in diesen Kategorien, festgelegt in `TAG-TAXONOMY.md`. Ohne eine solche Taxonomie entstehen Synonyme, Tippfehler und uneinheitliche Granularität. Der Reifegrad steht im Feld `status` und gehört nicht in die Tags.

Körper
: Ein Konzept pro Datei mit sprechendem Titel, in sich verständlich, mit Summary, Kernpunkten, Synthese und Sources.

Relationen
: Wikilinks stehen nur unter Related, damit Prüfskripte und Dashboard den Fließtext sauber lesen. Obsidian zeigt auch, welche Dokumente auf ein Dokument verweisen.

### Aufbau des Vaults

Vier Dateien im Root tragen die Ordnung des Vaults.

```
vault/
├── HOME.md          Map of Content, verlinkt alle Bereiche
├── ACTIVE-WORK.md   was läuft, was als Nächstes kommt
├── TAG-TAXONOMY.md  kontrolliertes Vokabular
├── CLAUDE.md        Zweck, Topografie und Regeln
└── knowledge/       Wissensdokumente
```

Eine Map of Content (MOC) ist ein Einstiegspunkt, der Links auf verwandte Dokumente mit je einer Zeile Erläuterung versammelt. `HOME.md` verweist auf Themen-MOCs, diese auf Wissensdokumente. Für Agents sind MOCs Navigationsinfrastruktur. Das Context Window fasst einen größeren Vault nicht vollständig, deshalb startet der Agent an einem Einstiegspunkt und folgt den Links.

CLAUDE.md enthält die Topografie des Vaults, also welcher Ordner welchem Zweck dient. Weil der Harness CLAUDE.md bei jedem Sitzungsbeginn lädt, kennt der Agent den Vault vom ersten Satz an. `ACTIVE-WORK.md` bündelt die laufenden Vorhaben mit Status und nächstem Schritt, sodass eine neue Session dort beginnt und weiß, woran gerade gearbeitet wird. Dasselbe Muster beschreibt Karpathy (2026) für eine vom LLM gepflegte Wissensbasis aus unveränderlichen Quellen, einem vom LLM geschriebenen Wiki und einem Schema-Dokument wie CLAUDE.md oder AGENTS.md.

Obsidian und Claude Code arbeiten auf denselben Dateien. Obsidian zeigt den Vault, Claude Code schreibt. Den Ordner `.obsidian/` mit den Einstellungen fasst der Agent nicht an. Wikilinks versteht Obsidian, viele andere Programme nicht.

### How Steph Ango uses Obsidian

Steph Ango ist CEO von Obsidian und beschreibt sein eigenes System als einen möglichen Stil (https://stephango.com/vault). Er arbeitet mit einem einzigen Vault, kaum Ordnern, durchgehend Markdown, Kategorien und Tags im Plural, Datumsangaben im Format JJJJ-MM-TT und vielen internen Links. Er rät, eigene Regeln zu wählen, aufzuschreiben und bei Bedarf zu ändern, weil ein konsistenter Stil viele kleine Entscheidungen erspart. Die Prinzipien sind Ausgangspunkte für eigene Entscheidungen und kein Standard.

### Mit dem Vault arbeiten

Ein Vault trägt mehr als die Ablage. Die Folie nennt sieben Arten, mit ihm zu arbeiten.

- Wiederfinden, also Notizen, Gedanken und Wissen über Suche, Tags und Links finden.
- Verknüpfen, also Projekte mit ihrem Wissen und untereinander verbinden.
- Einarbeiten, etwa ein Transkript übergeben, aus dem der Agent eine Notiz nach Vorlage am richtigen Ort ablegt.
- Fragen stellen, etwa „Was wissen wir über Datenschutz?“, mit einer Antwort, die auf die Dokumente verweist.
- Verbindungen finden, etwa „Welche Projekte nutzen dieselbe Quelle?“.
- Weiterarbeiten, etwa „Was ist offen?“, wobei der Agent bei `ACTIVE-WORK.md` ansetzt.
- Kuratieren, also Dubletten, tote Links und veraltete Aussagen finden.

## Session 3

### Frontier-LLMs amplifizieren computergestützte Wissensarbeit

Benchmarks sind standardisierte Tests für KI-Modelle. Sie zeigen, wie gut ein Modell bestimmte Aufgaben löst und wo es Fehler macht, und automatisch prüfbare Ergebnisse helfen beim Training und bei der Bewertung. Die Folie nennt METR Time Horizons, SimpleBench, ARC-AGI-3, Terminal-Bench und SWE-bench.

Forschungsresultate und Sicherheitsvorfälle zeigen Fähigkeiten und Kontrollprobleme unter konkreten Bedingungen, ihre Übertragbarkeit bleibt aber zu prüfen. Die Folie führt dazu Ergebnisse von OpenAI in der Mathematik und zu den Navier-Stokes-Gleichungen sowie einen Vorfall zwischen OpenAI und Hugging Face im Zusammenhang mit Agent Swarms an.

Recursive Self-Improvement bedeutet, dass KI hilft, leistungsfähigere KI zu entwickeln, die wiederum die weitere Entwicklung vorantreibt. Die Folie hält das für sehr wahrscheinlich und stellt dazu Positionen gegenüber, von Naam (2026) über AI 2027 bis zu den AGI-Zeitleisten von 80,000 Hours, ergänzt um Interviews und Videos zu KI-Fortschritt und Risiken. Weitere Videos enthält die kuratierte Playlist der Lehrlinie.

### Agentic Engineering: was das Modell umgibt

Die Folie ordnet die Bausteine, die ein Modell zu einem arbeitsfähigen Agenten machen, nach drei Disziplinen. Jeder Baustein beantwortet eine Frage.

| Disziplin | Baustein | Frage, die er beantwortet | Beispiel |
| --- | --- | --- | --- |
| Context Engineering | Projektdateien (.md) | Was weiß der Agent? | CLAUDE.md, knowledge/ |
| | Skills (.md, Skripte) | Wie erledigt er Arbeit? | PDF-Skill, Protokoll |
| Harness Engineering | Harness | Wo arbeitet der Agent? | Claude Code, Codex |
| | Werkzeuge | Was kann er tun? | Terminal, lesen, schreiben |
| | Konnektoren (MCP) | Was erreicht er anderswo? | Drive, Mail, Kalender |
| | Subagenten (.md) | Wem gibt er Arbeit? | Recherche, Reviewer |
| | Hooks (Skripte) | Was läuft bei Ereignissen? | sperren, erinnern, loggen |
| Loop Engineering | Loops, Schwärme | Was läuft autonom? | Wochenaudit, Reviewer |

Ein Plugin ist ein Paket aus Skills, Hooks und Konnektoren, das man installiert und weitergibt.

### Context Engineering

Context Engineering gestaltet, was im Context Window steht. Dazu gehören Instruktionen, Wissen, Tools, Memory und die Anfrage selbst, ausgewählt und verdichtet, damit das LLM mit begrenztem Platz zuverlässig arbeitet. Die Ordnung folgt der Übersicht von Mei et al. (2025), der Inhalt den Methoden, die in den Sessions bereits angewandt wurden.

Beschaffen
: Prompt Engineering mit Rückfragen, Beispielen und Meilensteinen aus Hands-on 1 und 2. Retrieval, bei dem der Agent Dateien selbst sucht und liest. Claude Code verwendet dafür keine Vektordatenbank, sondern Suchwerkzeuge und Lesezugriffe.

Verarbeiten
: Strukturierte Information in Markdown, Frontmatter und Relationen von Wissensdokumenten. Destillieren, also Quellen zu Wissensdokumenten verdichten, wie in Hands-on 1 und 2.

Verwalten
: Memory in CLAUDE.md und in Notizen, die der Agent selbst schreibt. Context Compression mit `/compact`, das den Verlauf durch eine Zusammenfassung ersetzt.

Anwenden
: Tool Use über MCP-Server und Skills, die erst bei Bedarf geladen werden. Multi-Agent-Arbeit mit Subagents, die je ein eigenes Context Window haben.

### Hands-on 6: Eine Anfrage mit Excel-Daten

Das sechste Hands-on bringt den Vault mit einer echten Arbeitssituation zusammen. Eine Anfrage mit vier Excel-Dateien kommt per Mail. Das Material liegt in [`data/`](data/README.md), vier Excel-Dateien aus der Northwind-Beispieldatenbank mit Bestellungen, Produkten, Kunden und Mitarbeitenden. In einer neuen Session im Vault werden die vier Dateien in einen Ordner `eingang/` gelegt.

Prompt 1 führt in den Vault. Der Agent liest Regeln, Einstieg und laufende Arbeit.

> Lies CLAUDE.md, HOME.md und ACTIVE-WORK.md. Fass in wenigen Sätzen zusammen, was in diesem Vault steht und was offen ist. Ändere nichts.

Prompt 2 bringt die Anfrage. Der Agent prüft sie gegen die eigene Governance und schlägt nächste Schritte vor.

> ```
> Betreff: Anfrage Workshop Agentic Engineering und Governance
> Anhänge: bestellungen.xlsx, produkte.xlsx, kunden.xlsx, mitarbeitende.xlsx
>
> Sehr geehrte Damen und Herren,
> ich leite den Vertrieb bei Northwind Traders, einem Großhandel für Feinkost und Getränke. Unsere Leute arbeiten fast ausschließlich mit Excel-Listen, und mehrere kopieren inzwischen Kundendaten in Chatbots. Wir wünschen uns:
> - einen eintägigen Workshop für unser Team
> - Folien, die wir intern weitergeben dürfen
> - eine kleine Webseite mit den wichtigsten Begriffen und Regeln
> - einen ersten Vorschlag für interne Regeln zum Einsatz von KI im Vertrieb
> Angehängt sind Exporte aus unserem Warenwirtschaftssystem von 1996 bis 1998. Mich interessiert besonders, welche Produkte und Länder am meisten Umsatz bringen.
> Mit freundlichen Grüßen
> Andrew Fuller, Vertrieb, Northwind Traders
> ```
> Diese Anfrage ist gerade gekommen, die Anhänge liegen in eingang/. Prüf sie gegen unseren Governance-Entwurf, sag mir, welches Wissen im Vault dafür schon da ist, und schlag mir die nächsten Schritte vor. Ändere noch nichts.

Die Mail im Prompt ist gekürzt. Die vollständige Fassung in [`data/kundenanfrage.txt`](data/kundenanfrage.txt) enthält zusätzlich Telefonnummer, Adresse und Bemerkungen zu Pension und Elternzeit im Team. Warum diese Angaben fehlen, ist die Frage an die Gruppe. Sie gehören zu den Daten, die nicht in einen Cloud-Dienst gehen, und dieselbe Frage stellt sich bei `mitarbeitende.xlsx` mit Geburtsdaten und Adressen. Für die Umsatzfrage reichen Bestellungen, Produkte und Kunden.

### Hands-on 6: Die Daten im Dashboard

Die Prüfung aus Prompt 2 legt fest, welche Dateien der Agent nutzen darf. In derselben Session geht es weiter. Fragt der Agent, ob er ein Python-Paket für Excel installieren darf, wird das bestätigt.

Prompt 3 ergänzt eine zweite Ansicht. Der Agent plant und baut eine Datenansicht im Wissensdashboard. Damit beantwortet das Dashboard beide Wünsche der Anfrage, die Übersicht über Begriffe und Regeln und die Frage, was ein Agent mit den Daten anfangen kann.

> Aktiviere den Plan-Modus. Ergänze das Wissensdashboard um eine zweite Ansicht „Daten“: Umsatz nach Produkt, Kategorie, Land und Monat, als Diagramme und Tabelle. Nutze nur die Dateien, die die Prüfung freigegeben hat. Alle Kennzahlen berechnet ein Skript aus den Excel-Dateien, nicht du selbst. Halte Daten und Anforderungen in knowledge/ fest.

Prompt 4 prüft. Der Agent rechnet jede Kennzahl gegen die Excel-Dateien nach.

> Prüfe jede Kennzahl der Ansicht gegen eine Referenz, die du direkt aus den Excel-Dateien berechnest. Liste und begründe Abweichungen. Ändere noch nichts.

Zum Schluss rechnet man eine Kennzahl selbst in Excel nach. Der dritte Prompt setzt die Regel aus dem Abschnitt zum Determinismus um, der vierte die unabhängige Prüfung.

### Subagents, Agent Teams und Dynamic Workflows

Ein Agent kann Arbeit auf drei Arten verteilen.

Subagents
: Ein Hauptagent gibt Teilaufgaben an Helfer ab und entscheidet nach jedem Ergebnis, was als Nächstes passiert. Die Helfer arbeiten mit eigenem Context Window und kennen nur ihren Auftrag. So verteilt Research Mission Control drei Experimente und prüft jeden Bericht an den Dateien nach.

Agent Teams
: Ein Team Lead verteilt die Arbeit an eigenständige Sessions, die sich über eine gemeinsame Aufgabenliste und direkte Nachrichten selbst abstimmen. Das eignet sich für Review aus mehreren Blickwinkeln und konkurrierende Hypothesen. Die Funktion ist experimentell (https://code.claude.com/docs/en/agent-teams).

Dynamic Workflows
: Claude schreibt ein Skript, das den Ablauf vorab festlegt und viele Subagents steuert. Unterwegs entscheidet kein Agent mehr. Mit dem Schalter Ultracode plant Claude für jede größere Aufgabe selbst einen Workflow.

### Research Mission Control: ein Hauptagent, drei Experimente

Die Folie zeigt einen Lauf aus der Vorbereitung dieses Workshops. Ein Hauptagent verteilte drei Experimente an Subagents, nämlich Mails anonymisieren, PDF zu Markdown und Sprache zu Text, und prüfte jeden Bericht am Ende an den Dateien.

```
Hauptagent
verteilt Aufträge, prüft Berichte
   │
   ├─▶ Subagent Mail anonymisieren
   ├─▶ Subagent PDF zu Markdown
   └─▶ Subagent Sprache zu Text
            │
            ▼
   Bericht an den Hauptagenten
            │
            ▼
   Gegencheck an den Dateien
```

Jeder Agent arbeitete mit eigenem Context Window in einem eigenen Ordner unter [`lokale-workflows/`](lokale-workflows/). Der Auftrag nannte Ziel, Schreibpfad und Grenzen, etwa nur lokale Modelle, kein Commit und kein Push. Ein Bericht gilt als ungeprüft, bis der Hauptagent ihn an den Dateien geprüft hat. Parallel kuratierten eigene Sessions die Repositories der Forschungswerkzeuge und meldeten ihre Commits zurück. Rollen und Übergaben für solche Arbeit beschreibt Research Mission Control (https://github.com/DigitalHumanitiesCraft/research-mission-control).

### MCP, RAG und Memory

Drei Wege geben einem Agenten Wissen und Fähigkeiten über sein Modell hinaus. Ein Video stellt sie zusammen mit Skills nebeneinander (*Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know*, https://youtu.be/X4FVEEegCbk).

Model Context Protocol (MCP)
: Ein offener Standard, über den ein LLM an andere Programme und Datenquellen angeschlossen wird, etwa Datenbanken, Dateien oder einen Kalender. Jedes angeschlossene Programm kann über einen MCP-Server Aktionen anbieten, die das Modell auslöst, etwa eine Berechnung (Tool), Inhalte zum Lesen wie eine Dokumentation (Resource) und Vorlagen mit Anweisungen, etwa Stilregeln für Code (Prompt). Eine Einführung bietet der MCP-Kurs von Hugging Face (https://huggingface.co/learn/mcp-course/unit1/introduction).

Retrieval-Augmented Generation (RAG)
: RAG gibt einem LLM Zugriff auf eigene Dokumente, etwa Word-, PowerPoint- oder Excel-Dateien, die einmal aufbereitet und in einem Suchspeicher abgelegt werden. Bei einer Frage findet das System passende Textabschnitte (Retrieval), ergänzt damit den Prompt (Augmentation), und das Modell erzeugt daraus die Antwort (Generation). Wie gut die Dokumente aufbereitet sind, bestimmt, wie gut die Antworten werden. Zwei Videos erklären Prinzip und Aufbau (https://youtu.be/u47GtXwePms, https://youtu.be/P8tOjiYEFqU).

Memory
: Memory gibt einem LLM ein Gedächtnis über einzelne Gespräche hinaus. Das System speichert selbst Notizen zu Vorlieben, Korrekturen und Vorhaben, laufend oder nach Gesprächsende. Zu Beginn lädt es ein Inhaltsverzeichnis, einzelne Notizen holt es bei Bedarf, und auf Wunsch durchsucht es frühere Gespräche. Die Notizen lassen sich einsehen, ändern und löschen. Memory wirkt als Kontext, sicher verhindern lässt sich etwas nur mit einem Hook (Anthropic, 2026b).

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

### Docling: Dokumente als Markdown

Docling ist ein Open-Source-Werkzeug, das Dokumente auf dem eigenen Rechner in strukturiertes Markdown oder JSON umwandelt. Es entstand bei IBM Research Zürich und gehört heute zur LF AI & Data Foundation (Auer et al., 2024, https://docling-project.github.io/docling/). Der Prozess zeigt konkret den Schritt „Wissen erwerben“ aus der Wissensmodellierung.

1. Ein Mensch wählt die Quelle aus, etwa ein PDF, eine Word- oder PowerPoint-Datei, eine Webseite oder einen Scan.
2. Docling analysiert lokal Layout, Lesereihenfolge und Tabellen und erkennt bei Scans den Text per OCR.
3. Das Ergebnis ist ein DoclingDocument, eine einheitliche Struktur aus Überschriften, Absätzen, Tabellen und Bildern.
4. Daraus exportiert Docling Markdown oder verlustfreies JSON.
5. Agent und Mensch arbeiten weiter. Der Agent liest das Markdown in `sources/` und destilliert daraus Wissensdokumente in `knowledge/`, die ein Mensch prüft.

Markdown erhält Überschriften, Lesereihenfolge und Tabellen, die bei einfacher Textextraktion verloren gehen. Weil Docling lokal läuft, verlassen sensible Dokumente den Rechner nicht. Ein Test in [`lokale-workflows/pdf-zu-markdown/`](lokale-workflows/pdf-zu-markdown/) zeigt beides. Docling übertrug Überschriften, Liste und Tabelle eines Test-PDFs vollständig, während einfache Textextraktion die Tabelle zerriss. Im zweispaltigen Teil rutschte allerdings eine Überschrift zwischen die Spalten, und gescannte deutsche Seiten las die Standard-OCR schwach. Im Workshop ist Docling kein Hands-on, weil die lokale Installation über Python in einer Zoom-Sitzung zu viel Einrichtung verlangt.

### Promptotyping Documents

Promptotyping Documents sind Wissensdokumente, unterschieden nach der Art des Wissens, das sie tragen (Pollin, 2026). Allen drei Typen sind die Teilnehmenden im Workshop schon begegnet.

Declarative Documents
: Sie halten Wissen über den Gegenstand fest, also über Daten, Domäne und Anforderungen, und erweitern, was das LLM über das Projekt weiß. Beispiele sind `project.md`, `data.md`, `specification.md` und `design.md`. In Hands-on 1 waren das `project.md` und `sources/`.

Process Documents
: Sie halten Wissen über den Arbeitsverlauf fest, also was geschehen ist, was offen ist und was als Nächstes kommt. Zusammen mit Git bilden `journal.md`, `handoff.md` und `plan.md` das Gedächtnis des Projekts. Im Workshop übernahmen Commits und Meilensteine diese Rolle.

Action Documents
: Sie halten Wissen über das Handeln fest, also was Agents im Projekt tun dürfen und wie, und steuern damit das Verhalten des Agenten. Beispiele sind CLAUDE.md und AGENTS.md, `governance.md`, `rules.md` und Skills wie der PDF-Skill aus Session 1.

### Loop Engineering

Loop Engineering gestaltet das System, das den Agenten anstößt und prüft, statt ihn jedes Mal von Hand zu prompten. Im Beispiel läuft die Datenansicht aus Hands-on 6 als wiederkehrender Ablauf.

```
Auslöser                      Agent
neue Excel-Datei     ──────▶  liest knowledge/,
liegt im Ordner               aktualisiert die Datenansicht
     ▲                              │      ▲
     │                              ▼      ┆ Abweichung,
Freigabe                      Prüfskript   ┆ neuer Versuch
Mensch nimmt ab      ◀──────  Kennzahlen gegen
oder gibt zurück              Excel-Summen
```

Ein Auslöser, etwa eine neue Datei, ein Zeitpunkt oder ein Ereignis, startet den Agenten. Ein fest verdrahtetes Prüfskript läuft danach, und der Agent kann es nicht überspringen. Findet es eine Abweichung, beginnt eine innere Schleife mit einem neuen Versuch. Erst das geprüfte Ergebnis geht zur Freigabe an einen Menschen. Jeder Auslöser vervielfacht Anfragen und Tokens, deshalb gehören Abbruchbedingungen und Grenzen zur Gestaltung. Den Begriff erläutert das Video von IBM Technology aus dem Abschnitt zu Lernzielen und Ablauf.

### Subagents und Workflows

Ein Agent kann Teilaufgaben an weitere Agents abgeben. Anthropic unterscheidet dabei Workflows, die LLMs und Werkzeuge über vorab festgelegte Codepfade orchestrieren, von Agents, die Ablauf und Werkzeugnutzung selbst bestimmen (Anthropic, 2024). Drei Formen kommen in der Praxis vor.

Subagent
: Ein Agent mit eigenem Context Window erledigt eine abgegrenzte Aufgabe und liefert nur das Ergebnis zurück. Claude Code bringt Explore und Plan mit, eigene Agents liegen in `.claude/agents/`. Codex kennt die Rollen `explorer` und `worker`, eigene Agents liegen in `.codex/agents/` (OpenAI, 2026).

Dynamic Workflow
: Claude schreibt ein Skript, verteilt Teilaufgaben auf viele parallele Subagents und lässt die Befunde gegenprüfen, bis sie übereinstimmen. Ausgelöst wird ein Workflow durch die ausdrückliche Bitte darum oder durch die Einstellung Ultracode (Anthropic, 2026a).

Parallele Sessions
: Eigenständige Sessions mit eigenem Ordner schicken einander Nachrichten. Auf diese Weise ist die Vorbereitung dieses Workshops entstanden.

Mehr Agents kosten mehr. Multi-Agent-Systeme verbrauchen laut Anthropic etwa fünfzehnmal so viele Tokens wie ein Chat (Anthropic, 2025). Sie lohnen sich für Recherche, Prüfung und Lesen. Bei parallelem Schreiben kollidieren Agents leicht.

### Determinismus so weit wie möglich ausreizen

Manche Aufgaben haben genau eine richtige Antwort, andere verlangen ein Urteil. Die Unterscheidung entscheidet, ob ein LLM die Aufgabe selbst lösen sollte.

Deterministisch
: Code, Formeln und Skripte liefern bei gleicher Eingabe die gleiche Ausgabe. Dazu gehören Summen, Budgets, Datumsangaben und Zählungen, Prüfungen wie die, ob jedes Feld ausgefüllt ist und die Summe stimmt, sowie das Umwandeln von Formaten.

Probabilistisch
: Das Urteil einer KI oder eines Menschen kann bei gleicher Eingabe unterschiedlich ausfallen. Dazu gehören Zusammenfassen, Formulieren und Tonalität, Klassifizieren, Abwägen und Entscheiden sowie die Frage, ob ein Ergebnis plausibel ist.

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

### Test Driven Development (TDD)

Beim Test Driven Development entsteht der Test vor dem Code. Zuerst scheitert der Test (rot), dann besteht er mit der Umsetzung (grün).

Für Coding Agents verhindern Tests zwei typische Fehler, Code, der nicht funktioniert, und Code, den niemand braucht. Ein Test, der schon vor der Umsetzung besteht, prüft nichts. Im Prompt genügt „Arbeite mit Red/Green-TDD.“ Leistungsfähige Modelle verstehen das als Anweisung, zuerst Tests zu schreiben, ihr Scheitern zu zeigen und dann umzusetzen (Willison, 2026b). In Hands-on 6 übernimmt das Prüfskript diese Rolle für die Kennzahlen.

### Open Models: das Modell im eigenen Haus

Open-Weight-Modelle sind frei herunterladbar und laufen auf eigener Hardware, etwa mit Ollama. Trainingsdaten und Code bleiben meist verschlossen, deshalb ist Open Weights nicht dasselbe wie Open Source.

- Privat, weil die Daten den Rechner nicht verlassen.
- Anpassbar, weil sich ein Modell auf eine Aufgabe und eigenes Wissen zuschneiden lässt.
- Unabhängig, weil kein Anbieter Preis, Modell oder Bedingungen über Nacht ändert.
- Begrenzt, weil sie schwächer sind als die stärksten geschlossenen Modelle und Hardware und Betrieb ebenfalls kosten.

Den Grundsatz dahinter nennt van Strien (2026) Boring AI. Gemeint ist das kleinste Werkzeug, das die Aufgabe löst, und oft reicht dafür ein Skript oder ein kleines Modell. Die These, dass offene Modelle als private und anpassbare Intelligenz Boden gewinnen, vertritt der Vortrag *How Open Models Win Against OpenAI and Anthropic* (https://youtu.be/zsO5RktNB7k). Seine Marktzahlen sind Angaben des Vortragenden und hier nicht übernommen.

Drei lokale Workflows aus der Vorbereitung des Workshops liegen in [`lokale-workflows/`](lokale-workflows/), jeweils mit Skript, Prüfung und README. Sie anonymisieren eine Mail mit einem Skript und einem lokalen LLM, wandeln ein PDF mit Docling in Markdown um und transkribieren eine Besprechung mit Whisper.

## Anhang

### Commands in Claude Code (Auswahl)

Slash Commands sind Befehle an den Harness selbst (https://code.claude.com/docs/en/overview).

- `/init` erzeugt eine CLAUDE.md mit Projektstruktur und Konventionen.
- `/compact` komprimiert die Konversation, behält Kontext und spart Tokens.
- `/clear` löscht die gesamte Konversationshistorie. Dateiänderungen bleiben.
- `/effort` setzt das Reasoning-Level (low, medium, high, max).
- `/model` wechselt das Modell.
- `/plan` schaltet den Plan-Modus ein. Claude plant, führt aber nichts ohne Zustimmung aus.
- `/context` zeigt die Auslastung des Context Window.
- `/help` listet alle verfügbaren Befehle.
- `/diff` zeigt alle Änderungen der Session.
- `/rewind` setzt Code und Konversation zurück. Es ersetzt Git nicht und erfasst reine Bash-Änderungen nicht.

Zwei Sonderzeichen und zwei Tastenkürzel ergänzen die Befehle. `@` referenziert Dateien oder Verzeichnisse im Prompt, `!` führt einen Shell-Befehl direkt aus, und Befehl und Ausgabe landen im Kontext. Shift+Tab wechselt zwischen Normal-Modus, Auto-Accept und Plan-Modus, zweimal Esc öffnet das Rewind-Menü.

### AI Watermarking

Ein Wasserzeichen soll erkennbar machen, ob ein Text oder ein Bild von einer KI stammt. Bei Text und Bild funktioniert das grundverschieden.

Beim Text-Watermarking wirkt das Wasserzeichen schon beim Schreiben. Ein LLM berechnet für jedes mögliche nächste Token eine Wahrscheinlichkeit und zieht daraus eines. Beim Watermarking erzeugt ein geheimer Schlüssel zusammen mit dem vorangehenden Text bei jedem Schritt einen Zufallswert, der die Auswahl leicht in eine bestimmte Richtung lenkt. Der Text bleibt gut lesbar, trägt aber ein statistisches Muster in der Wortwahl. Wer den Schlüssel hat, berechnet für einen Text einen Wert und vergleicht ihn mit einer Schwelle. Je länger der Text, desto verlässlicher das Ergebnis, und Umschreiben oder Übersetzen schwächt das Muster (Dathathri et al., 2024, Fig. 1, CC BY 4.0).

Beim Bild-Watermarking wird das fertige Bild markiert. Ein Encoder legt eine kurze Bitfolge unsichtbar ins Pixelmuster, ein Decoder liest sie wieder aus, schon bei einem einzelnen Bild. JPEG-Kompression und Zuschnitt übersteht das Wasserzeichen, gezielte Angriffe können es entfernen (Bui et al., 2023). Signierte Metadaten nach dem Standard C2PA sind ein zweiter Weg, die jeder prüfen kann, solange sie nicht entfernt wurden. Das Video *How Image Watermarking Works* von Computerphile (2026, https://youtu.be/h6j_ixGnpiY) erklärt den Bildteil.

Ein Wasserzeichen ist ein Hinweis und kein Beweis. Fehlt es, folgt daraus nicht, dass ein Mensch den Inhalt erstellt hat. Seit 2. August 2026 verlangt Art. 50 des AI Act von Anbietern, synthetische Inhalte maschinenlesbar zu kennzeichnen, und Watermarks sind dafür ein Baustein.

### Agentic Search: suchen wie im Terminal

Für eine Wissensbasis in Markdown braucht ein Coding Agent meist keine Vektordatenbank. Er sucht mit grep nach Wörtern und Mustern, liest die gefundenen Dateien ganz und sucht nach, wenn etwas fehlt. Jede Suche steht als Befehl im Verlauf und lässt sich nachvollziehen, und der Agent liest ganze Dokumente statt einzelner Passagen. Das setzt sprechende Dateinamen, Markdown und Frontmatter voraus, wie in Hands-on 3. Synonyme und sehr große Bestände bleiben ein Fall für semantische Suche. Ein Video von IBM Technology diskutiert die Frage (*Are Vector Databases Still Needed? RAG, AI Agents & Search*, https://youtu.be/rXFV1ivDe6c).

## Literatur

- Allen, B. P., Stork, L., & Groth, P. (2023). Knowledge Engineering Using Large Language Models. *Transactions on Graph Data and Knowledge*, 1(1), 3. https://doi.org/10.4230/TGDK.1.1.3
- Anthropic (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents
- Anthropic (2025). How we built our multi-agent research system. https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic (2026a). Introducing dynamic workflows in Claude Code. https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- Anthropic (2026b). How Claude remembers your project. https://code.claude.com/docs/en/memory
- Anthropic (2026c). Orchestrate teams of Claude Code sessions. https://code.claude.com/docs/en/agent-teams
- Auer, C., et al. (2024). Docling Technical Report. arXiv:2408.09869. https://arxiv.org/abs/2408.09869
- Bui, T., et al. (2023). TrustMark: Universal Watermarking for Arbitrary Resolution Images. arXiv:2311.18297. https://arxiv.org/abs/2311.18297
- Dathathri, S., et al. (2024). Scalable watermarking for identifying large language model outputs. *Nature*. https://doi.org/10.1038/s41586-024-08025-4
- Dell’Acqua, F., et al. (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*, 37(2), 403–423. https://doi.org/10.1287/orsc.2025.21838
- Gans, J. (2026). A Model of Artificial Jagged Intelligence. arXiv:2601.07573. https://doi.org/10.48550/arXiv.2601.07573
- Hugging Face (2026). Introduction to Model Context Protocol (MCP). https://huggingface.co/learn/mcp-course/unit1/introduction
- Jones, W., et al. (2017). Personal Information Management. In *Encyclopedia of Library and Information Sciences* (4. Aufl.). https://doi.org/10.1081/E-ELIS4-120053695
- Karpathy, A. (2025). Vibe Coding. Beitrag auf X, 2. Februar 2025. https://x.com/karpathy/status/1886192184808149383
- Karpathy, A. (2026). LLM Wiki. GitHub Gist, 4. April 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Kuster, J., et al. (2022). *Handbuch Projektmanagement* (5. Aufl.). https://doi.org/10.1007/978-3-662-65473-6
- Lindsey, J., et al. (2025). On the Biology of a Large Language Model. *Transformer Circuits*. https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- Liu (2026). Engineering and Governing the Agent Harness. UNU Macau Technology Report 1. https://unu.edu/publication/engineering-and-governing-agent-harness-technology-and-policy-framework-runtime-layer
- Mei, L., Yao, J., Ge, Y., et al. (2025). A Survey of Context Engineering for Large Language Models. arXiv:2507.13334. https://doi.org/10.48550/arXiv.2507.13334
- Merriam-Webster (2025). Word of the Year 2025: Slop. https://www.merriam-webster.com/wordplay/word-of-the-year
- OpenAI (2026). Subagents. https://learn.chatgpt.com/docs/agent-configuration/subagents
- Pollin, C. (2026). Promptotyping. Translating Research Data into Research Artefacts with Context and Agentic Engineering. https://docs.google.com/document/d/1_Q6kLFxvnvLMRizN2F_uTkpwsaJ-Cp0uBw4REKfhDlM/edit
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4. Aufl.). Pearson. https://aima.cs.berkeley.edu
- Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges. *Information Fusion*, 126, 103599. https://doi.org/10.1016/j.inffus.2025.103599
- Summerfield, C. (2025). *These Strange New Minds: How AI Learned to Talk and What It Means*. Viking.
- van Strien, D. (2026). AI Design Patterns for Information Professionals. https://danielvanstrien.xyz/ai-patterns-for-glam/
- Willison, S. (2024). Slop is the new name for unwanted AI-generated content. https://simonwillison.net/2024/May/8/slop/
- Willison, S. (2026a). What is agentic engineering? Agentic Engineering Patterns. https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/
- Willison, S. (2026b). Red/green TDD. Agentic Engineering Patterns. https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/
- Xu, W., Huang, C., Gao, S., & Shang, S. (2025). LLM-Based Agents for Tool Learning: A Survey. *Data Science and Engineering*, 10, 533–563. https://link.springer.com/article/10.1007/s41019-025-00296-9
- Zhong, H., & Zhu, S. (2026). AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents. arXiv:2605.13357. https://doi.org/10.48550/arXiv.2605.13357
