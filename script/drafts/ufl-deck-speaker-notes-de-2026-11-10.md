# Sprechernotizen für das Deck UFL-Agentic Engineering-Workshop-26, Folien 13 bis 78

Stand 2026-11-10. Geprüfte Entwürfe, noch nicht im Deck. Die Notizen der Folien 1 bis 8 und 10 bis 12 stehen bereits im Deck.
Die Dateien `batch-*.json` im selben Ordner enthalten dieselben Texte als fertige Schreibaufträge für Google Slides.

## Folie 13. Session 2

Klasse: trenner (Abschnittstrenner ohne Text im Body.)

Abschnittstrenner, keine Notiz.

## Folie 14. Aufbauendes Beispiel und Ablauf

Klasse: fertig

In dieser Einheit beginnt das Beispiel, das uns bis zum Ende des Workshops begleitet. Wir bauen Schritt für Schritt eine Wissensbasis zu Agentic Engineering und Governance auf, und am Ende bekommt sie eine Oberfläche im Browser. An jedem Schritt lernen Sie einen Aspekt des Agentic Engineering praktisch kennen.

Sie kopieren die Prompts von den Folien in Ihren eigenen AI Harness und arbeiten parallel mit. Während die Agents arbeiten, bespreche ich die Konzepte dahinter. Behalten Sie dabei Ihren Harness im Blick, denn der Agent ruft Werkzeuge auf, stellt Rückfragen und wartet auf Freigaben.

Achten Sie auf Ihre Usage. Die teuersten Modelle verbrauchen das Nutzungskontingent rasch und sind für die Übungen nicht nötig. Für die Daten gilt eine einfache Regel. Arbeiten Sie mit öffentlichen oder synthetischen Beispieldaten. Eigene Daten nehmen Sie nur dazu, wenn Ihre Organisation die Verarbeitung im gewählten Cloud-Dienst erlaubt.

- Befund: Die Folie sagt „Wir arbeiten mit einem AI Harness in der Cloud“, Folie 16 lässt dagegen „lokal als Ordner oder in der Cloud“ arbeiten, und Folie 19, 28 und 30 setzen Claude Code lokal voraus.

## Folie 15. AI Harnesses in der Cloud

Klasse: fertig

Wer keinen Harness auf dem eigenen Rechner installieren kann oder will, arbeitet mit einem AI Harness in der Cloud. Harness und Werkzeuge laufen dann auf Servern des Anbieters. Sie arbeiten im Browser und stellen Dateien durch Hochladen oder über verbundene Dienste bereit.

Auf der Folie stehen drei Angebote mit den jeweils nötigen Schritten. Bei Antigravity legen Sie ein Remote-Projekt an und starten die Aufgabe. Claude Code im Web und Codex Cloud arbeiten mit einem GitHub-Repository, das Sie zuerst verbinden. Für ein neues Projekt legen Sie also vorher ein Repository auf GitHub an. Alle drei setzen ein passendes Konto beim Anbieter voraus, die Voraussetzungen stehen jeweils dabei.

Ein Satz auf der Folie ist mir besonders wichtig. Verwenden Sie nur Daten, deren Verarbeitung im gewählten Dienst nach den Vorgaben Ihrer Organisation erlaubt ist. Wenn die Einrichtung hakt, helfen die verlinkten Dokumentationen der drei Anbieter.

- Befund: Tippfehler im ersten Satz, „auf einem Servern des Anbieters“.
- Befund: Zeitgebundene Produktaussagen (bei Antigravity „Derzeit keine Geschäftskonten“, Abo-Voraussetzungen) veralten bei Wiederverwendung des Decks und sind vor jedem Durchgang zu prüfen.
- Befund: Für diese Folie gibt es im UFL-Skriptum keinen eigenen Abschnitt, die Notiz stützt sich nur auf den Folientext.

## Folie 16. Hands-on 1: Webrecherche und Wissensdokumente

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die vorhandene Notiz ist kein Sprechtext, sie enthält nur eine alternative Promptfassung mit dem Vorspann „Prompt, damit vorhandenes Wissen am Rechner nicht genutzt wird“.
- Befund: Die Promptfassung in der Notiz weicht vom Folienprompt ab („Beantworte mir dann diese Fragen“ statt „Warte auf meine Antworten. Beantworte dann …“, Subagents mit „Sonnet 5.5“).
- Befund: Das Skriptum fragt im dritten Punkt „Wie destillierst du das Wissen, und welche Dokumente entstehen in knowledge/?“, die Folie „Wie organisierst du die Quellen und das Quellenverzeichnis?“.

## Folie 17. Hands-on 1: Eigene Wissensbasis schärfen

Klasse: fertig

Während die Recherche läuft, nutzen wir die Zeit für Ihre eigene Arbeit. Nehmen Sie sich fünf bis zehn Minuten und beantworten Sie für sich die vier Fragen auf der Folie. Bei welcher konkreten Aufgabe soll die Wissensbasis helfen, welche eigenen Quellen sollen hinein, welche zentrale Frage soll sie beantworten und woran erkennen Sie eine brauchbare Antwort?

Aus Ihren Antworten formulieren Sie einen Auftrag an Ihren Agenten und geben ihn in die laufende Konversation ein. Der Agent soll offene Punkte mit Ihnen klären und Ihr Projektprofil in knowledge/project.md aktualisieren.

Die zentrale Frage trägt alles Weitere. Im nächsten Hands-on destilliert der Agent die Quellen entlang dieser Leitfrage, und später beantworten wir sie mit einem Bericht und einer Präsentation. Je konkreter Sie die Frage fassen, desto besser lässt sich prüfen, ob die Ergebnisse taugen.

- Befund: Die Folie setzt knowledge/project.md voraus, der Prompt von Folie 16 nennt diesen Dateinamen nicht und verlangt das Projektprofil nur „in geeigneten Markdown-Dokumenten“.
- Befund: Im UFL-Skriptum gibt es keinen Abschnitt zu dieser Folie, die Notiz stützt sich auf den Folientext und auf Folie 26 und 36.

## Folie 18. AI Harnesses

Klasse: fertig

Sie haben jetzt eine Weile mit einem AI Harness gearbeitet, und die Folie gibt dafür die Definition. Ein AI Harness ist die Softwareumgebung eines AI Agents. Er führt die Agentenschleife aus, stellt Kontext und Werkzeuge bereit und kontrolliert, worauf der Agent zugreifen und was er tun darf. Das LLM liefert die Sprachfähigkeit, der Harness entscheidet, was der Agent sehen und tun darf. Deshalb unterscheiden sich zwei Harnesses mit demselben Modell im Ergebnis spürbar.

Die Folie nennt außerdem den Personal AI Agent. Er behält Kontext über einzelne Gespräche hinweg, betreut längerfristig Aufgaben einer Person und wird innerhalb vereinbarter Befugnisse selbstständig tätig. Auch seine Arbeitsumgebung ist ein Harness. Dazu stehen auf der Folie Beispiele, kommerzielle Angebote ebenso wie Open-Source-Projekte.

- Befund: Der Begriff „Personal AI Agent“ steht nicht im Glossar, das für dauerhaft laufende Agenten den Begriff „Always-On Agent“ (Dauerhaft laufender Agent) führt. Begriffsdrift prüfen.
- Befund: Die Folie definiert AI Harness etwas anders als Folie 19 („kontrolliert Zugriffs- und Handlungsrechte“ gegenüber „setzt Grenzen durch“).
- Befund: Das Skriptum nennt als Beispiel „Windsurf“, die Folie „Devin Desktop (vormals Windsurf)“. Die Produktangabe ist vor Wiederverwendung zu prüfen.

## Folie 19. Claude Code in der Claude Desktop App

Klasse: fertig

Diese Folie zeigt die Oberfläche, in der viele von Ihnen arbeiten, und verbindet sie mit zwei Begriffen. Der AI Harness ist die Software um das LLM. Ein AI Agent ist ein System, in dem ein LLM die nächsten Schritte plant und Werkzeuge nutzt, um ein vorgegebenes Ziel mit einem gewissen Maß an Autonomie zu verfolgen.

Die Einstellungen auf der Folie gehe ich kurz durch. Jeder Werkzeugaufruf erscheint im Verlauf, so wird Tool Use sichtbar. Slash Commands sind Befehle an den Harness selbst, etwa /context. Über MCP, Connectors und Plugins binden Sie externe Dienste an. Für den Workshop stellen Sie das Modell auf Sonnet 5.5, Effort auf low oder medium und den Permission Mode auf Auto. Usage und Context Window zeigen, wie viel Kontingent und Kontext Sie verbraucht haben, und Ihre Subscription bestimmt das Kontingent.

Prüfen Sie diese Einstellungen jetzt in Ihrem eigenen Harness.

- Befund: Die Folie steht nach dem Start von Hands-on 1 (Folie 16), die Einstellungen Modell, Effort und Permission Mode sollten laut Skriptum aber vor dem ersten Hands-on geprüft werden.

## Folie 20. Markdown ist eine leichtgewichtige Auszeichnungssprache …

Klasse: fertig

Der Agent hat Ihre Wissensdokumente als Markdown-Dateien angelegt, und diese Folie erklärt, warum. Markdown ist eine leichtgewichtige Auszeichnungssprache, die Dokumentstruktur in Klartext ausdrückt. Eine Raute markiert eine Überschrift, Sternchen markieren eine Hervorhebung, ein Bindestrich einen Listenpunkt. Auf der Folie sehen Sie dieselbe Überschrift einmal in Markdown und einmal so, wie Word sie intern als XML speichert. Für ein LLM kostet die Markdown-Fassung deutlich weniger Tokens.

Ein Token ist die Einheit, in die ein LLM Text zerlegt, meist ein Wort oder Wortteil. Kosten und Context Window werden in Tokens gemessen. Ein Tokenizer zerlegt Text in Tokens und ordnet ihnen Zahlen zu, und welcher Tokenizer verwendet wird, hängt vom Modell ab. Probieren Sie den Tokenizer, der auf der Folie verlinkt ist, mit einem eigenen Satz aus. Die Markdown-Syntax erklärt der ebenfalls verlinkte Markdown Guide.

- Befund: Im Titelfeld steht der ganze Definitionstext zu Markdown und Tokens statt eines kurzen Titels. Das Skriptum führt die Folie als „Markdown und Tokens“.

## Folie 21. Tokenkosten und Subscriptions

Klasse: fertig

Nach den Tokens geht es um das, was sie kosten. Es gibt zwei Abrechnungswege. Eine Subscription gibt Ihnen Zugang zu den Anwendungen und ein Nutzungskontingent. Höhere Tarife unterscheiden sich durch Nutzungslimits, verfügbare LLMs und Zusatzfunktionen. Die API-Nutzung wird nach Verbrauch abgerechnet, getrennt nach Input-Tokens für übergebene Inhalte und Output-Tokens für erzeugte Ausgaben.

Das Rechenbeispiel auf der Folie zeigt, dass ein einzelner Aufruf wenig kostet. Agents brauchen aber viele LLM-Aufrufe. Lange Kontexte, Subagents und erneute Versuche erhöhen den Verbrauch, und wiederverwendete Eingaben können durch Caching günstiger werden. Ein Abo bedeutet deshalb keine unbegrenzte Nutzung, und aus diesem Grund habe ich Sie gebeten, auf Ihre Usage zu achten.

Die Preise auf der Folie tragen einen Stand und ändern sich laufend. Prüfen Sie die aktuellen Preise und die regionalen Endpreise bei Ihrem Anbieter.

- Befund: Die Folie trägt Preise und den Vermerk „Stand 10. November 2026“. Bei Wiederverwendung sind Preise und Datum zu aktualisieren.
- Befund: Das Rechenbeispiel ist arithmetisch korrekt (20.000 Input-Tokens zu 2 USD und 5.000 Output-Tokens zu 10 USD pro Million ergeben 0,04 plus 0,05 gleich 0,09 USD).
- Befund: Für diese Folie gibt es im UFL-Skriptum keinen Abschnitt, die Notiz stützt sich auf den Folientext.

## Folie 22. AI Agent & Tool Use

Klasse: fertig

Was Sie in Ihrem Harness als Tool-Aufrufe sehen, ist der Kern eines AI Agents. Ein LLM-basierter AI Agent wählt für ein vorgegebenes Ziel Schritt für Schritt die nächste Aktion. Bei Tool Use formuliert das LLM einen Werkzeugaufruf, etwa für eine Websuche oder das Lesen einer Datei. Der Harness führt den Aufruf aus und gibt das Ergebnis an das LLM zurück, das es bei der nächsten Entscheidung berücksichtigt.

Das Beispiel auf der Folie zeigt diese Schleife. Auf den Prompt, das Projekt zusammenzufassen, listet der Agent mit ls den Projektordner auf und findet den Ordner knowledge. Mit cd wechselt er hinein, listet ihn erneut auf und liest mit cat die Datei project.md. Daraus schreibt er die Zusammenfassung. Jeden Befehl hat der Agent selbst gewählt, auf Grundlage des letzten Ergebnisses.

Sehen Sie in Ihrem eigenen Verlauf nach, welche Befehle Ihr Agent bei der Recherche verwendet hat.

## Folie 23. Subagents

Klasse: fertig

Im ersten Hands-on haben Sie die Recherche auf zwei Subagents aufgeteilt. Ein Subagent ist ein AI Agent, dem ein anderer Agent eine abgegrenzte Aufgabe überträgt. Er arbeitet in einem eigenen Context Window ohne den bisherigen Verlauf und gibt nur sein Ergebnis an den beauftragenden Agenten zurück. Der Hauptverlauf bleibt dadurch entlastet.

Auf der Folie stehen die Punkte, auf die es beim Einsatz ankommt. Geben Sie dem Subagenten gezielt Kontext mit, etwa Auftrag, Quellen und Prüfkriterien. Lagern Sie Recherche, Analyse oder Review aus, lassen Sie abgrenzbare Teilaufgaben parallel laufen und stimmen Sie Anweisungen, Werkzeuge und LLM auf die Aufgabe ab. Die Ergebnisse führt der Hauptagent zusammen, und Sie prüfen sie.

Weil ein Subagent den Verlauf nicht kennt, eignet er sich für ein Review ohne Vorwissen. Das Beispiel auf der Folie lässt einen Entwurf mit den Quellen abgleichen, ohne ihn zu ändern. Auch ein solches Review garantiert keine Richtigkeit.

- Befund: Der Beispielprompt prüft den „Governance-Entwurf“, der erst in Hands-on 3 (Folie 29) entsteht. An dieser Stelle von Session 2 existiert er bei den Teilnehmenden noch nicht.

## Folie 24. Hands-on 1: Ergebnis eines Durchgangs

Klasse: fertig

So sieht das Ergebnis eines Durchgangs von Hands-on 1 aus. Ihre Ergebnisse sehen anders aus, ähneln ihm aber. Vorgegeben waren die Ordner knowledge, sources und scripts. Der Agent hat von sich aus ein Python-Skript scripts/check_kb.py angelegt, das die Wissensbasis prüft, und dazu die Markdown-Dokumente INDEX.md und journal.md. Vergleichen Sie das mit Ihrem eigenen Projektordner.

Zwei Fragen auf der Folie führen weiter. Warum ist PDF für LLMs ein schwieriges Format? Ein PDF hält fest, wo Zeichen auf einer Seite stehen, und kaum, wie ein Text gegliedert ist. Überschriften, Lesereihenfolge und Tabellen muss ein Programm erst wieder erschließen. Und was ist ein Word- oder Excel-Dokument eigentlich? Beide sind gepackte Ordner mit XML-Dateien, deren Inhalt zwischen vielen Formatierungsangaben steht. Deshalb arbeiten wir inhaltlich in Markdown und lassen PDF oder Word erst am Ende mit Code erzeugen.

- Befund: Die Folie steht nach den Konzeptfolien zu Markdown und Word-XML (Folie 20). Ihre Leitfragen zu PDF und Word führen laut Skriptum zu diesem Abschnitt hin, die Reihenfolge ist damit umgekehrt.

## Folie 25. Ein Projekt mit AI Agents bearbeiten

Klasse: fertig

Die Folie teilt die Arbeit an einem Projekt mit AI Agents in drei Phasen. Im Aufbau der Wissensbasis tragen Sie eigenes Wissen, Kontext, Anforderungen und vorhandene Materialien zusammen und ergänzen sie durch gezielte Recherche. Das haben Sie in Hands-on 1 getan.

In der Destillation und Kuration arbeiten Sie das für Ihre Fragestellung relevante Wissen heraus, prüfen es und halten es kompakt mit nachvollziehbaren Belegen fest. Darum geht es im nächsten Hands-on.

In der Umsetzung nutzen Sie das erarbeitete Wissen, um eine konkrete Aufgabe zu lösen oder ein Artefakt zu entwickeln, im Workshop etwa einen Bericht, eine Präsentation oder ein Dashboard. Was ein Agent in der Umsetzung leistet, hängt von der Qualität des Wissens ab, auf das er zugreift, und deshalb kommt die Destillation vor der Umsetzung.

- Befund: Für diese Folie gibt es im UFL-Skriptum keinen Abschnitt, die Notiz stützt sich auf den Folientext und die Abfolge der Hands-ons.
- Befund: Der dritte Punkt der Folie endet ohne Punkt („… ein Artefakt zu entwickeln“), die beiden anderen mit Punkt.

## Folie 26. Hands-On 2: Wissen in Wissensdokumente destillieren

Klasse: fertig

Im zweiten Hands-on destillieren Sie Ihre Quellen. Ein Wissensdokument ist strukturiertes, externalisiertes Wissen, destilliert aus Quellen, Daten oder Erfahrung zur Wiederverwendung durch Menschen und AI Agents. Ein gutes Wissensdokument ist für Menschen und KI lesbar, kompakt, durch Markdown übertragbar und kuratierbar, also prüfbar, korrigierbar und erweiterbar.

Kopieren Sie den Prompt in Ihre laufende Konversation. Der Agent liest Ihr Projektprofil mit der Leitfrage und lässt Subagents jede Quelle in sources/ in eine eigene Markdown-Datei in knowledge/ destillieren, mit Quellenverweis und Seitenangabe. Die Originale bleiben unverändert. Danach schlägt er vor, wie er knowledge/ überarbeitet, und wartet auf Ihr OK. Prüfen Sie den Vorschlag, bevor Sie freigeben.

Die Follow-up-Prompts auf der Folie prüfen das Ergebnis auf Fehler und Redundanzen. Schauen Sie danach mit /context nach, wie voll Ihr Context Window ist. Darum geht es auf der nächsten Folie.

- Befund: Schreibweise „Hands-On 2“ weicht von „Hands-on“ auf den übrigen Hands-on-Folien ab.
- Befund: Der Follow-up-Prompt „Erzeuge ein AGENTS.md!“ steht hier, erklärt wird AGENTS.md erst auf Folie 28, die für Claude Code /init und CLAUDE.md zeigt.

## Folie 27. Context Window managen

Klasse: fertig

Nach zwei Hands-ons ist Ihr Verlauf lang geworden, deshalb jetzt das Context Window. Es bezeichnet den Textausschnitt, den ein LLM auf einmal berücksichtigen kann, und Eingabe und Ausgabe teilen sich diesen Raum. Das Beispiel auf der Folie rechnet mit einem Fenster von 8000 Tokens. Eingabe mit 6000 und Ausgabe mit 1500 Tokens passen hinein. Bei 10000 Tokens Eingabe ist das Fenster überschritten, und ältere Teile fallen heraus oder müssen gekürzt werden.

Context Rot beschreibt, dass die Leistung eines Modells mit wachsender Eingabelänge nachlässt, lange bevor das Fenster voll ist. Ein langer Verlauf ist also auch dann ein Problem, wenn er technisch noch hineinpasst.

In Claude Code zeigt /context, wie voll das Context Window ist und womit. /compact fasst den Verlauf zusammen, die Projektanweisungen bleiben erhalten, und benötigte Dateien liest der Agent bei Bedarf erneut. Was nur im Gespräch stand und in keiner Datei, kann dabei verloren gehen. Deshalb gehört dauerhaftes Wissen in Wissensdokumente.

## Folie 28. AGENTS.md / CLAUDE.md

Klasse: fertig

Dauerhaftes Wissen liegt in Wissensdokumenten, dauerhafte Anweisungen liegen in eigenen Dateien. AGENTS.md und CLAUDE.md sind Markdown-Dateien mit Anweisungen für einen AI Agent, also Projektzweck, Arbeitsregeln und Verweise auf Wissen. AGENTS.md ist ein offenes Format, das viele Harnesses lesen, CLAUDE.md die Entsprechung in Claude Code. Welche Datei wann geladen wird, hängt vom Harness ab.

Die Anweisungen liegen auf zwei Ebenen. Die globale Datei gilt für alle Projekte und hält die Arbeitsweise fest, etwa kompakt zu antworten, vor dem Löschen nachzufragen und nur zu zitieren, was gelesen wurde. Die Projektdatei gilt nur in diesem Projekt und nennt Zweck, Start und Regeln, etwa dass nur Quellen aus 2026 aufgenommen werden.

In Claude Code untersucht /init das Projekt und erzeugt einen Entwurf der CLAUDE.md. Lesen und korrigieren Sie diesen Entwurf, bevor Sie sich darauf verlassen, denn der Agent richtet sich in jeder Session nach dieser Datei.

- Befund: Das Beispiel der Projektdatei nennt ein „Wissensdashboard“ und „index.html per Doppelklick öffnen“, das Dashboard entsteht aber erst in Hands-on 5 (Folie 40).

## Folie 29. Hands-on 3: Governance für den eigenen Anwendungsfall entwickeln

Klasse: fertig

Im dritten Hands-on nutzen Sie die Wissensbasis für Ihren eigenen Fall. Beschreiben Sie zuerst eine Aufgabe aus Ihrer Arbeit, die ein AI Agent übernehmen soll, mit welchen Daten er arbeiten soll und in welchem System er eingesetzt wird. Diese Beschreibung setzen Sie im Prompt an die Stelle in den doppelten geschweiften Klammern.

Der Prompt fragt, welche Governance-Regeln dieser Einsatz braucht. Der Agent darf vorher bis zu drei Rückfragen stellen und antwortet nur aus knowledge/ und sources/, mit Datei und Fundstelle. Bei Wissenslücken schlägt er eine Webrecherche mit Subagents vor und wartet auf Ihr OK. Das Ergebnis hält er in knowledge/governance-entwurf.md fest.

Beobachten Sie dabei, wie der Agent relevante Inhalte findet. Er sucht über das Terminal, mit Volltextsuche und Suchmustern, und sprechende Dateinamen helfen ihm dabei. Prüfen Sie, ob seine Aussagen durch die angegebenen Quellen gedeckt sind, und notieren Sie, welche Fragen offen bleiben.

- Befund: Die Folie kündigt an „Das PDF bereiten wir anschließend daraus auf“, das nächste PDF entsteht aber in Hands-on 4 (Folie 36) als Bericht zur Leitfrage und nicht aus dem Governance-Entwurf.
- Befund: Das Skriptum führt dieses Hands-on als „Hands-on 3: Wissensbasis nutzen“ mit drei Fragen zur Organisation, die Folie mit eigener Fallbeschreibung und bis zu drei Rückfragen.

## Folie 30. Permission Modes und Autonomie in Claude Code

Klasse: fertig

Sie haben Ihrem Agenten in den letzten Hands-ons Zugriff auf Dateien und das Web gegeben. Der Permission Mode legt fest, welche Aktionen er ohne Ihre Freigabe ausführen darf, und damit, wie viel Autonomie Sie ihm geben. Die Folie ordnet die Modi danach, wie viele manuelle Freigaben sie verlangen.

Plan erkundet das Projekt und plant, bevor etwas geändert wird. Manual fragt vor jeder Aktion, die noch nicht freigegeben ist. Accept edits erlaubt Dateiänderungen und bestimmte Dateisystembefehle ohne Rückfrage. Auto genehmigt viele Aktionen automatisch, weitere prüft ein Klassifikator und kann sie blockieren. Dieser Klassifikator kann sich irren. Bypass überspringt die meisten Prüfungen und gehört nur in eine isolierte Umgebung.

Feste Grenzen setzen Deny-Regeln und geeignete Hooks, die bestimmte Aktionen unabhängig vom Modus blockieren. Eine Sandbox begrenzt zusätzlich die Datei- und Netzwerkzugriffe von Shell-Befehlen. Unter nativem Windows steht die eingebaute Sandbox von Claude Code nicht zur Verfügung.

- Befund: Die Folie beschreibt Manual als „fragt vor Aktionen, die noch nicht freigegeben sind“, das Skriptum als „fragt bei allem außer Lesen“. Beide Fassungen sind abzugleichen.

## Folie 31. Autonomie und Zugriff

Klasse: fertig

Die Permission Modes regeln einen einzelnen Harness. Diese Übersicht ordnet AI Agents allgemeiner nach zwei Fragen, wie selbstständig sie handeln und worauf sie zugreifen dürfen. In den Spalten steht die Autonomie, vom Beraten über das assistierte Handeln mit Freigaben bis zum autonomen Handeln im vereinbarten Rahmen. In den Zeilen steht der Systemzugriff, von keinem direkten Zugriff über begrenzte Rechte auf einen Projektordner bis zu weitreichendem Zugriff auf Dateien, E-Mail und Dienste mit Ihren Rechten.

Je mehr von beidem zusammenkommt, desto mehr Absicherung braucht der Einsatz. Bei weitreichendem Zugriff ist schon das Lesen sensibel, und Einzelfreigaben reichen als Schutz allein nicht aus. Dort begrenzen Sie zuerst Zugriff und Handlungsspielraum.

Die Einordnung ist eine eigene didaktische Fassung nach Quellen der United Nations University und des NIST. Das konkrete Risiko hängt von Aufgabe, Daten und Schutzmaßnahmen ab. Im Workshop gilt, dass Veröffentlichen, Löschen und E-Mails senden eine ausdrückliche Freigabe brauchen.

- Befund: Das Skriptum nennt als Grundlage nur Liu (2026, United Nations University), die Folie zusätzlich NIST (2026). Das Skriptum ist entsprechend zu ergänzen.

## Folie 32. Session 3

Klasse: trenner (Abschnittstrenner ohne Text im Body.)

Abschnittstrenner, keine Notiz.

## Folie 33. “Few-shotted for Breakfast”

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die vorhandene Notiz ist kein Sprechtext, sie enthält nur den englischen Text der beiden Screenshots mit dem Vorspann „text auf sceenshot“ (Tippfehler).
- Befund: Die Folie eröffnet im Skriptum Session 1, im Deck steht sie am Beginn von Session 3. Verweise der Notizen auf andere Sessions sind daraufhin zu prüfen.

## Folie 34. fancy (research) tools & workflows

Klasse: fertig

Wie das in der Praxis aussieht, zeigt diese Folie an Beispielen aus der Arbeit von Digital Humanities Craft. Gemeinsam mit Forschenden entwickeln wir iterativ spezialisierte Forschungswerkzeuge und Workflows. AI Agents im AI Harness setzen sie schnell um, meist als statische Anwendungen, die ohne Server im Browser laufen.

teiCrafter unterstützt die Auszeichnung von Transkriptionen in TEI-XML. Der CorrespExplorer zeigt Briefdaten als Karte, Zeitleiste und Netzwerk. Dazu kommen die SZD OCR/HTR Pipeline und die Stefan-Zweig-Bibliographie.

Unter Agentic Knowledge Engineering stehen Promptotyping, Grounded Vault und die Agentic Edition Pipeline. Promptotyping und Grounded Vault begegnen Ihnen später in dieser Einheit wieder. Die Übersicht mit allen Links finden Sie unter der Adresse auf der Folie.

- Befund: Das Skriptum nennt zusätzlich coOCR/HTR als Beispiel, die Folie nicht.
- Befund: Das Skriptum sagt „Session 3 stellt sie genauer vor“, was im Deck nun die laufende Einheit ist.

## Folie 35. Leistung, Geschwindigkeit und Kosten von Modellen

Klasse: fertig

Bei der Modellwahl hilft ein unabhängiger Vergleich. Artificial Analysis vergleicht proprietäre LLMs und LLMs mit offenen Gewichten anhand von Benchmark-Ergebnissen, Geschwindigkeit und Kosten pro Benchmark-Aufgabe. LLMs mit offenen Gewichten lassen sich auch gesondert vergleichen.

Für die Arbeit mit Agents zählen alle drei Größen. Ein Agent ruft das LLM viele Male auf, deshalb summieren sich Kosten und Wartezeit über einen ganzen Lauf. Das teuerste Modell ist für die Übungen in diesem Workshop nicht nötig, und für Subagents mit abgegrenzten Aufgaben reicht oft ein günstigeres. Schauen Sie sich die Seite nach dem Workshop an und vergleichen Sie die Modelle, die in Ihrem Harness zur Wahl stehen.

- Befund: Für diese Folie gibt es im UFL-Skriptum keinen Abschnitt, die Notiz stützt sich auf den Folientext, Folie 21 und die Modellvorgaben im Abschnitt „Aufbauendes Beispiel und Ablauf“.

## Folie 36. Hands-on 4: Die eigene Leitfrage beantworten

Klasse: fertig

Mit dem vierten Hands-on kommen wir zur Umsetzung. Sie beantworten die Leitfrage aus Ihrem Projektprofil und machen daraus zwei Ergebnisse zum Weitergeben. Formulieren Sie vorher für sich, welche Frage aus Ihrem Arbeitsalltag beantwortet werden soll und für wen.

Kopieren Sie den Prompt. Der Agent liest project.md und die Wissensdokumente, präzisiert mit Ihnen die Leitfrage und klärt Zielgruppe und Verwendungszweck. Dann erarbeitet er eine kompakte Antwort mit Quellen und Fundstellen und kennzeichnet Schlussfolgerungen, Widersprüche und Wissenslücken. Hier hält er an. Prüfen Sie die Antwort und ihre Belege, bevor Sie mit OK freigeben.

Danach beauftragt der Agent zwei Subagents parallel. Der eine erstellt einen PDF-Bericht, der andere eine bearbeitbare PowerPoint mit genau fünf Folien. Verfolgen Sie im Verlauf, wie beide gleichzeitig arbeiten. Hält der Agent zwischendurch an, schicken Sie continue. Am Ende prüfen Sie, ob beide Ergebnisse die Frage beantworten, mit den Belegen übereinstimmen und gut lesbar sind.

- Befund: Im UFL-Skriptum ist Hands-on 4 noch das Wissensdashboard. Ein Abschnitt zu diesem neuen Hands-on fehlt, die Notiz stützt sich auf den Folientext.
- Befund: Im Prompt bricht „Kläre fehlende Angaben“ ohne Punkt in die nächste Zeile um.

## Folie 37. Hands-on 4: PDF und PowerPoint prüfen und überarbeiten

Klasse: fertig

Die erste Fassung ist selten fertig. AI Slop bezeichnet KI-erzeugte Inhalte von geringer Qualität. In einem Bericht oder einer Präsentation zeigt er sich etwa durch austauschbare Aussagen, Wiederholungen oder überladene Gestaltung. Auch ein gutes Ergebnis trägt oft solche Spuren, wenn es ungeprüft übernommen wird. De-Slopification heißt, diese Schwächen am Ergebnis zu erkennen und gezielt zu beheben.

Die Folie hat zwei Prompts. Der erste prüft den Inhalt gegen Leitfrage, abgestimmte Antwort und Quellen und ändert noch nichts, damit Sie die Befunde lesen können, bevor etwas geändert wird. Der zweite lässt den Agenten jede PDF-Seite und jede Folie als Bild ansehen, Schwächen benennen und beheben, ohne belegte Inhalte zu verlieren. Am Ende zeigt er Ihnen eine Seite und eine Folie vor und nach der Überarbeitung.

Vergleichen Sie die überarbeiteten Dateien danach selbst mit den ersten Fassungen.

- Befund: Das Skriptum wendet De-Slopification auf das Governance-PDF aus Hands-on 3 an, die Folie auf PDF und PowerPoint aus Hands-on 4.

## Folie 38. Skills für PDF und PowerPoint

Klasse: fertig

Den Weg zu PDF und PowerPoint haben Sie einmal durchgearbeitet, und ein Skill hält ihn fest. Ein Skill ist gespeichertes Anwendungswissen, ein wiederverwendbarer Arbeitsablauf als Markdown-Datei mit name und description im YAML-Header und der Anleitung darunter. Er liegt im Projekt in einem eigenen Ordner unter .claude/skills, optional mit Skripten und Vorlagen.

Zunächst sind nur Name und Beschreibung verfügbar. Die Anleitung lädt der Harness erst, wenn der Skill verwendet wird. Die projektweite CLAUDE.md wird dagegen in jeder Session geladen.

Der Prompt auf der Folie lässt den Agenten aus Ihrer Erstellung und Überarbeitung zwei Skills ableiten, report-pdf und presentation-pptx. Beide sollen ohne diesen Chat verständlich sein, und Zielgruppe, Thema und Umfang werden je Auftrag festgelegt. In Claude Code rufen Sie sie danach direkt mit Schrägstrich und Namen auf. Lesen Sie die erzeugten Skills, bevor Sie sich auf sie verlassen, denn sie sind ein Agentenprodukt wie jede CLAUDE.md.

- Befund: Das Skriptum beschreibt einen einzelnen Skill governance-pdf aus dem Governance-PDF, die Folie zwei Skills report-pdf und presentation-pptx.

## Folie 39. Skills

Klasse: fertig

Skills rufen Sie in der Claude Desktop App über den Schrägstrich auf. Im Menü auf der Folie sehen Sie unter Skills zwei Einträge, einen für PDF-Berichte und einen für PowerPoint-Präsentationen, jeweils mit ihrer Beschreibung. Diese Beschreibung ist das, was der Harness von einem Skill zunächst kennt.

Der zweite Punkt ist ebenso wichtig. Auch der Agent kann einen Skill nutzen, wenn eine Aufgabe zur Beschreibung passt, ohne dass Sie ihn eigens aufrufen. Probieren Sie beides aus, einmal mit dem Schrägstrich und einmal mit einem Auftrag, der zum Skill passt.

## Folie 40. Hands-on 5: Wissensdashboard

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die vorhandene Notiz ist kein Sprechtext, sie enthält nur eine abweichende Promptfassung mit dem Vorspann „Prompt für Christopher“.
- Befund: Die Nummer Hands-on 5 ist doppelt vergeben, auch Folie 51 heißt „Hands-on 5: Wissens-Vault bauen“.
- Befund: Das Skriptum führt das Wissensdashboard noch als Hands-on 4.

## Folie 41. Die erste Iteration des Dashboards

Klasse: fertig

Ihr Dashboard besteht aus vier einfachen Bausteinen. HTML legt die Struktur fest, CSS das Design und JavaScript das Verhalten, etwa Suchen und Filtern. Die Daten erzeugt ein Skript aus knowledge/ und sources/.

Das Skript stellt die Daten als JavaScript-Datei bereit, weil der Browser JSON-Dateien ohne Server nicht lädt. Lokal öffnet ein Doppelklick auf index.html die Seite, einen lokalen Server und eine Portnummer brauchen Sie dafür nicht. Arbeiten Sie in der Cloud, nutzen Sie die Vorschau oder laden das Projekt herunter.

Kleinere Werkzeuge und Skripte, deren Ergebnisse Sie selbst prüfen können, dürfen Sie vibe coden. Sie lesen dann den Code nicht und testen nur das Ergebnis, auf eigene Verantwortung. Mit mehr Erfahrung in Softwareentwicklung kommen Sie weiter. Der Workshop setzt bewusst auf einfache Technologien, weil gerade wer keine Software entwickelt von kleinen Werkzeugen profitiert, die sich lesen und prüfen lassen. Öffnen Sie jetzt Ihr Dashboard und probieren Sie Suche und Filter aus.

## Folie 42. Hands-on 5: Follow-Up Prompts

Klasse: fertig

Die erste Iteration ist selten fertig, und die Folie zeigt mehrere Wege, wie Sie weiterarbeiten. Sie können Feedback geben, in Text und mit einem Screenshot, und beschreiben, was stört. Mit Self-Verification und Self-Refine prüft der Agent sein Ergebnis gegen den Plan und listet Abweichungen auf. Diese Prüfung bleibt beim selben Agenten.

Unabhängiger prüft ein Subagent als LLM-as-a-Judge. Er kennt den Verlauf nicht und sieht sich das Dashboard ohne Vorwissen an. Lassen Sie ihn zuerst nur Befunde liefern, die wir besprechen, bevor etwas geändert wird. Dieselbe Prüfung lässt sich auf den Code anwenden, mit der Frage nach Refactoring und danach, wie sich die Software sauber testen lässt.

Der letzte Weg betrifft das Wissen. LLMs erzeugen immer Rauschen, und man muss immer wieder aufräumen. Kuratieren heißt auswählen, prüfen, ordnen und erschließen, kontextualisieren, korrigieren, ergänzen, aussortieren und erhalten. Wählen Sie einen dieser Prompts und schicken Sie ihn ab.

- Befund: Laut Skriptum heißt die Prüfung durch einen selbst suchenden Subagenten im Promptotyping-Paper Agentic Review und wird vom LLM-as-a-Judge im engeren Sinn abgegrenzt. Die Folie verwendet nur „Subagent als LLM-as-a-Judge“.
- Befund: „Test Driven Development“ steht als Stichwort auf der Folie ohne Erklärung. Das Glossar definiert es.

## Folie 43. Agentic Governance Workspace

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

## Folie 44. Computational Thinking

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

## Folie 45. Vibe Coding, Agentic Engineering und Promptotyping

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die vorhandene Notiz nennt „Die erste Fassung Ihres Dashboards in Hands-on 4“, im Deck ist das Dashboard Hands-on 5 (Folie 40).
- Befund: Die Notiz verweist zweimal auf „Session 3“ als spätere Einheit („in Session 3 sehen Sie den ganzen Ablauf noch einmal“), die Folie steht aber selbst in Session 3.

## Folie 46. Wissensmodellierung

Klasse: fertig

Mit dieser Folie wechseln wir von der Software zum Wissen, das in der dritten Spalte der vorigen Folie steht. Drei etablierte Felder helfen dabei, Projektwissen so aufzubauen und zu pflegen, dass Menschen und AI Agents damit arbeiten können.

Wissensmodellierung konstruiert eine Wissensbasis. Die Konzepte einer Domäne werden identifiziert, formal repräsentiert und abfragbar gemacht, und der Weg führt von den Fragen über Wissenserwerb, Vokabular und Kodierung bis zu Abfragen und Evaluation. Das persönliche Informationssystem betrifft den Umgang mit der eigenen Information über Formate und Orte hinweg. Sein Kernproblem ist die Fragmentierung. Projektmanagement plant, steuert und kontrolliert Vorhaben in Phasen von der Initiierung bis zum Abschluss.

Wer eine Domäne versteht und ihre Begriffe, Regeln und Entscheidungen festhält, kann sie dem Agenten als genaue Anforderungen übergeben. Wie viel Struktur das Projektwissen braucht, hängt von der Komplexität des Projekts ab.

- Befund: Der Beleg zum Projektmanagement verweist auf eine Shop-Seite von Lehmanns mit Zugriffsdatum 2024, das Skriptum zitiert dagegen Kuster et al. (2022).

## Folie 47. 

Klasse: bild (Folie ohne Titel und Text, nur ein Bild. Inhalt aus dem Export nicht beurteilbar.)

Keine Notiz. Die Folie zeigt nur einen Screenshot eines Prompts in der Claude Desktop App, ihr Zweck im Ablauf ist aus dem Deck nicht zu erkennen.

## Folie 48. 

Klasse: bild (Folie ohne Titel und Text, nur ein Bild. Inhalt aus dem Export nicht beurteilbar.)

Das ist die Graphansicht meines eigenen Vaults in Obsidian. Jeder Punkt ist eine Notiz, jede Linie ein Link zwischen zwei Notizen. In der Mitte steht die Notiz Promptotyping, und Sie sehen, mit wie vielen anderen Notizen sie verbunden ist. Am Rand sehen Sie die Ordnerstruktur.

Der Graph zeigt, was ein Vault gegenüber einer Ablage in Ordnern hinzufügt, die Beziehungen zwischen den Dokumenten. Für einen Agenten sind diese Links Wege, denen er beim Suchen folgen kann.

## Folie 49. Agentisches Wissensmanagement

Klasse: fertig

Die drei Felder der vorigen Folie lassen sich mit einem Werkzeug bedienen. Obsidian ist eine Notiz- und Wissensmanagement-Anwendung, die Notizen als Markdown-Dateien in einem lokalen Ordner speichert, dem Vault. Weil die Daten als einfache Textdateien auf dem eigenen Computer liegen, kann Claude Code sie direkt lesen und bearbeiten. Das Dateiformat ist offen, und ein Cloud-Konto brauchen Sie nicht.

Für die Wissensmodellierung bilden Links, Tags und Ordnerhierarchien Relationen, die sich an das eigene Fachgebiet anpassen lassen und die der Agent beim Arbeiten nutzt. Als persönliches Informationssystem organisiert der Vault die eigenen Notizen und die eigene Forschung. Für das Projektmanagement dient er strategisch der Organisation von Projekten und operativ der Planung laufender Arbeit.

Das Bild auf der Folie zeigt die Ordner- und die Graphansicht meines eigenen Vaults. Eine ausführlichere Einführung gibt das verlinkte Video.

## Folie 50. How Steph Ango uses Obsidian

Klasse: fertig

Bevor Sie selbst einen Vault bauen, sehen wir uns an, wie ein erfahrener Nutzer seinen Vault ordnet. Die Empfehlungen auf der Folie stammen vom CEO von Obsidian, der sein eigenes System als einen möglichen Stil beschreibt. Er arbeitet mit einem einzigen Vault und kaum Ordnern, mit Standard-Markdown, mit Kategorien und Tags im Plural, mit Datumsangaben in der Reihenfolge Jahr, Monat, Tag und mit vielen internen Links. Dazu kommen eine Bewertungsskala mit sieben Stufen und eine einzige Aufgabenliste pro Woche.

Er rät, eigene Regeln zu wählen, aufzuschreiben und bei Bedarf zu ändern, weil ein konsistenter Stil viele kleine Entscheidungen erspart. So lesen wir auch diese Liste. Sie beschreibt einen minimalistischen, linkbasierten Ansatz und ist ein Ausgangspunkt für Ihre eigenen Entscheidungen. Im nächsten Hands-on legen Sie solche Regeln für Ihren Vault fest und lassen sie in der CLAUDE.md festhalten.

## Folie 51. Hands-on 5: Wissens-Vault bauen

Klasse: fertig

In diesem Hands-on machen Sie aus Ihrem Projektordner einen Obsidian-Vault. Dahinter steht die These auf der Folie, dass ein Projekt umso mehr Wissensstruktur braucht, je komplexer es ist, so wie größere Vorhaben mehr Projektmanagement brauchen.

Starten Sie eine neue Session und öffnen Sie in Obsidian über Open folder as vault genau den Ordner wissensbasis. Wer einen übergeordneten Ordner öffnet, bekommt einen zweiten Vault im ersten. Sehen Sie sich zuerst den Graphen an. Der Agent legt einen Commit je Schritt an, dafür muss Git installiert sein.

Prompt 1 plant. Der Agent fragt nach dem Zweck des Vaults und schlägt Frontmatter, Tags, Links, eine HOME.md und eine ACTIVE-WORK.md vor, ohne etwas zu ändern. Prompt 2 baut und zeigt nach jedem Schritt, was sich geändert hat. Achten Sie darauf, dass der Agent wirklich kleinschrittig vorgeht, im Probelauf führte ein bloßes „Setz um“ zu großen Umbauten auf einmal. Prompt 3 kuratiert und trennt die Befunde nach Struktur und Inhalt. Am Ende haben Sie einen Vault, dessen Regeln in der CLAUDE.md stehen, und ein Dashboard, das weiter funktioniert.

- Befund: Die Folie trägt die Nummer Hands-on 5, dieselbe wie das Wissensdashboard auf den Folien 40 und 42. Im Skriptum ist das Dashboard Hands-on 4 und der Vault Hands-on 5.
- Befund: Prompt 2 verlangt einen Commit je Schritt und setzt damit Git voraus. Die Folie nennt das nicht, das Skriptum verweist im Abschnitt „Git und GitHub“ auf die Installation, und eine entsprechende Folie fehlt im Deck.

## Folie 52. Das Wissensdokument im Vault

Klasse: fertig

Die Folie zeigt, wie ein einzelnes Wissensdokument nach dem Umbau aussieht. Im Vault bekommt es einen Kopf, Tags und Relationen.

Der Kopf ist Frontmatter in YAML, einem Format aus Schlüssel und Wert. Typ, Datum, Status und Tags machen den Vault abfragbar. Bei den Tags vergeben wir je einen aus Thema, Funktion und Quelle, also worum es geht, welche Art Dokument vorliegt und woher das Wissen stammt. Neue Tags entstehen nur in diesen Kategorien, festgelegt in der TAG-TAXONOMY.md. Ohne eine solche Taxonomie entstehen Synonyme, Tippfehler und uneinheitliche Granularität. Der Reifegrad gehört in das Feld status.

Der Körper folgt dem Grundsatz ein Konzept, eine Datei, mit sprechendem Titel, Summary, Kernpunkten, Synthese und Sources. Wikilinks stehen nur unter Related. So lesen Prüfskripte und das Dashboard den Fließtext sauber, und Obsidian zeigt trotzdem an, welche Dokumente auf ein Dokument verweisen.

- Befund: Das Beispiel-Frontmatter trägt das feste Datum created: 2026-11-10, das bei Wiederverwendung des Decks als Datum dieses Durchgangs gelesen werden kann.

## Folie 53. Aufbau des Vaults

Klasse: fertig

Nach dem einzelnen Dokument sehen wir den ganzen Vault. Vier Dateien im Root tragen seine Ordnung. HOME.md ist die Map of Content und verlinkt alle Bereiche, ACTIVE-WORK.md hält fest, was läuft und was als Nächstes kommt, TAG-TAXONOMY.md ist das kontrollierte Vokabular, und CLAUDE.md beschreibt Zweck, Topografie und Regeln. Die Wissensdokumente liegen im Ordner knowledge.

Eine Map of Content ordnet Links auf verwandte Dokumente, im Vault mit je einer Zeile Erläuterung. Für Agenten ist sie Navigationsinfrastruktur. Das Context Window fasst einen größeren Vault nicht vollständig, deshalb startet der Agent an einem Einstiegspunkt und folgt den Links. Weil der Harness die CLAUDE.md bei jedem Sitzungsbeginn lädt, kennt der Agent den Vault vom ersten Satz an, und eine neue Session setzt bei ACTIVE-WORK.md an.

Obsidian und Claude Code arbeiten auf denselben Dateien. Obsidian zeigt den Vault, Claude Code schreibt, und den Ordner .obsidian mit den Einstellungen fasst der Agent nicht an.

## Folie 54. Mit dem Vault arbeiten

Klasse: fertig

Ein Vault trägt mehr als die Ablage. Auf der Folie stehen sieben Arten, mit ihm zu arbeiten, wie sie im Alltag vorkommen. Wiederfinden und Verknüpfen kennen Sie aus jeder Notizanwendung. Weiter reicht es, wenn der Agent mitarbeitet. Sie übergeben ihm ein Transkript, und er legt eine Notiz nach Vorlage am richtigen Ort ab. Sie fragen, was wir über Datenschutz wissen, und die Antwort verweist auf die Dokumente. Sie fragen, welche Projekte dieselbe Quelle nutzen oder was offen ist, und für die zweite Frage setzt der Agent bei ACTIVE-WORK.md an. Beim Kuratieren findet er Dubletten, tote Links und veraltete Aussagen.

Diese Fragen tragen, weil Ihr Vault aus dem Hands-on Frontmatter, Links und eine ACTIVE-WORK.md hat. Wer Obsidian noch nicht installiert hat, findet den Download-Link auf der Folie. Geöffnet wird der Vault über Manage vaults und Open folder as vault, und zwar genau der Ordner wissensbasis.

## Folie 55. Frontier-LLMs amplifizieren computergestützte Wissensarbeit

Klasse: fertig

Diese Folie hebt den Blick vom eigenen Vault auf die Entwicklung der Modelle. Sie sammelt Material in drei Gruppen.

Benchmarks sind standardisierte Tests für KI-Modelle. Sie zeigen, wie gut ein Modell bestimmte Aufgaben löst und wo es Fehler macht, und ihre automatisch prüfbaren Ergebnisse helfen beim Training und bei der Bewertung. Auf der Folie stehen unter anderem METR Time Horizons, ARC-AGI-3 und SWE-bench. Die zweite Gruppe sind Forschungsresultate und Sicherheitsvorfälle, etwa Ergebnisse in der Mathematik. Sie zeigen Fähigkeiten und Kontrollprobleme unter konkreten Bedingungen, ihre Übertragbarkeit bleibt aber zu prüfen.

Die dritte Gruppe betrifft Recursive Self-Improvement, also KI, die hilft, leistungsfähigere KI zu entwickeln, die wiederum die weitere Entwicklung vorantreibt. Ich halte das für sehr wahrscheinlich. Die Positionen auf der Folie gehen dabei weit auseinander, von der Frage, wo die intelligence explosion bleibt, bis zum Szenario AI 2027. Interviews und Videos zu Fortschritt und Risiken ergänzen sie, weitere Videos finden Sie in der Playlist.

- Befund: Das Titelfeld enthält neben dem Titel eine zweite Zeile „Recursive Self-Improvement ist sehr wahrscheinlich“, die als Teil des Titels exportiert wird.
- Befund: Die Links zu photocraft und rea.tools stehen ohne Erläuterung auf der Folie, und das Skriptum erwähnt sie nicht.

## Folie 56. Agentic Engineering: was das Modell umgibt und was es davon sieht

Klasse: fertig

Diese Folie ordnet die Bausteine, die Sie in den Hands-ons benutzt haben, nach drei Disziplinen. Context Engineering wählt aus, ordnet und stellt bereit, was der Agent für eine Aufgabe braucht, und den Kern bildet die Auswahl. Harness Engineering gestaltet die Umgebung, in der der Agent arbeitet. Loop Engineering gestaltet die Abläufe, die ihn ohne Prompt von Hand anstoßen.

Jede Zeile stellt eine Frage, etwa was der Agent weiß, was er sich gemerkt hat, was er tun kann oder wem er Arbeit gibt. Die letzte Spalte zeigt, was davon im Context Window landet. Die CLAUDE.md liegt ab dem Start darin, von Skills zunächst nur die Beschreibung, und ihr Inhalt kommt erst bei Bedarf dazu. Von Subagents sieht der Hauptagent nur das Ergebnis. Hooks laufen außerhalb und erscheinen nur mit ihrer Rückmeldung. An dieser Spalte lässt sich ablesen, warum ein Agent etwas weiß oder übersieht.

- Befund: Für Hooks nennt die Folie im Context Window „nur ihre Rückmeldung, sie laufen außerhalb“, das Skriptum „nichts, sie laufen außerhalb“. Das Glossar (Hook) stützt die Folie, das Skriptum ist veraltet.

## Folie 57. Model Context

Klasse: fertig

Drei Wege geben einem Agenten Wissen und Fähigkeiten über sein Modell hinaus, und die Folie stellt sie nebeneinander.

MCP ist ein offener Standard, über den ein LLM an andere Programme und Datenquellen angeschlossen wird, etwa Datenbanken, Dateien oder einen Kalender. Ein MCP-Server bietet Tools, die das Modell ausführt, Resources mit Inhalten und Prompts als Vorlagen an. In der Tabelle der vorigen Folie standen diese Anschlüsse als Konnektoren. RAG gibt einem LLM Zugriff auf eigene Dokumente, die einmal aufbereitet und in einem Suchspeicher abgelegt werden. Bei einer Frage holt das System passende Abschnitte, ergänzt damit den Prompt, und das Modell antwortet samt Quellen. Wie gut die Dokumente aufbereitet sind, bestimmt, wie gut die Antworten werden.

Memory gibt einem LLM ein Gedächtnis über einzelne Gespräche hinaus. Das System speichert selbst Notizen zu Vorlieben, Korrekturen und Vorhaben, die Sie einsehen, ändern und löschen können. Memory wirkt als Kontext, den der Agent liest. Sicher verhindern lässt sich etwas erst mit einem Hook.

- Befund: Der Folientitel nennt nur MCP, die Folie behandelt auch RAG und Memory. Der Abschnitt im Skriptum heißt „MCP, RAG und Memory“.

## Folie 58. Agentic Memory

Klasse: fertig

Diese Abbildung von Anthropic zeigt, wie ein Agent zwischen zwei Sessions ein Gedächtnis aufbaut. Aus einer Session bleiben Transkripte, ein durchsuchbares Protokoll der Ereignisse. Daraus schreibt das Modell Memory Notes, also Beobachtungen, die es für wichtig hält. Aus Transkripten und Notizen entstehen verdichtete Darstellungen, und ein Teil davon wird als Kontext in jede neue Session geladen. Die Abbildung nennt diese Verarbeitung zwischen den Sessions Dreaming.

Für uns zählt der Unterschied zur CLAUDE.md. Die CLAUDE.md schreiben Sie, Memory schreibt der Agent selbst. Sie können diese Notizen einsehen, ändern und löschen. Memory wirkt als Kontext und als Gedächtnisstütze. Verbindliche Regeln gehören in eine Instruktionsdatei.

- Befund: Das Skriptum hat keinen Abschnitt zu Agentic Memory, und die Folie trägt außer einem Link keinen Text, deshalb keine Notiz.

## Folie 59. Agentic Search: suchen wie im Terminal

Klasse: fertig

Nach RAG stellt sich die Frage, ob Sie für Ihre Wissensbasis eine Vektordatenbank brauchen. Für eine Wissensbasis in Markdown braucht ein Coding Agent meist keine.

Bei RAG werden die Dokumente vorab in Abschnitte zerlegt und in einer Vektordatenbank abgelegt, und eine Frage holt die Abschnitte mit der ähnlichsten Bedeutung. Das passt für sehr große Bestände, für Synonyme und für die Suche nach Bedeutung. Bei Agentic Search sucht der Agent mit grep nach Wörtern und Mustern, liest die gefundenen Dateien ganz und sucht nach, wenn etwas fehlt.

Das Beispiel auf der Folie stammt aus einem Probelauf mit der Frage, was unsere Wissensbasis zu Datenschutz sagt. Der Agent findet zehn Dateien, liest den Governance-Entwurf und sucht dann in den Quellen gezielt nach DSGVO. Das gelingt, weil die Wissensbasis sprechende Dateinamen und Frontmatter hat. Jede Suche steht nachvollziehbar im Verlauf, und Sie können sie dort mitlesen.

- Befund: Das Skriptum sagt, die Wissensbasen mit Frontmatter seien „in Hands-on 3 entstanden“. Frontmatter entsteht laut Folie 51 erst beim Vault-Bau in Hands-on 5.

## Folie 60. Hands-on 6: Eine Anfrage mit Excel-Daten

Klasse: fertig

Das sechste Hands-on bringt den Vault mit einer echten Arbeitssituation zusammen. Eine Anfrage mit vier Excel-Dateien kommt per Mail, die Daten stammen aus der Northwind-Beispieldatenbank.

Starten Sie eine neue Session im Vault, laden Sie die vier Excel-Dateien herunter und legen Sie sie in den Ordner eingang. Prompt 1 lässt den Agenten CLAUDE.md, HOME.md und ACTIVE-WORK.md lesen. Achten Sie darauf, ob er den Stand Ihres Vaults richtig zusammenfasst, daran sehen Sie, ob die Arbeit aus dem letzten Hands-on trägt. Prompt 2 enthält die Anfrage selbst. Der Agent prüft, ob alle vier Dateien da sind, gleicht sie mit Ihrem Governance-Entwurf ab, sagt, welches Wissen schon im Vault liegt, und schlägt nächste Schritte vor. Ändern soll er noch nichts.

Die Mail im Prompt ist gekürzt. Telefonnummer, Adresse und Bemerkungen zu Pension und Elternzeit fehlen, und über das Warum sprechen wir gleich. Dieselbe Frage stellt sich bei mitarbeitende.xlsx mit Geburtsdaten und Adressen.

- Befund: Die Folie sagt „die vier Excel-Dateien herunterladen“, nennt aber keine Quelle. Das Skriptum verweist auf den Ordner data/ im Workshop-Material.

## Folie 61. Hands-on 6: Die Daten im Dashboard

Klasse: fertig

Die Prüfung aus Prompt 2 legt fest, welche Dateien der Agent nutzen darf. Damit geht es in derselben Session weiter. Schalten Sie den Plan-Modus ein. Fragt der Agent, ob er ein Python-Paket für Excel installieren darf, bestätigen Sie das.

Prompt 3 ergänzt das Wissensdashboard um eine zweite Ansicht mit dem Umsatz nach Produkt, Kategorie, Land und Monat, nur als Summen ohne Personendaten. Achten Sie im Plan darauf, dass ein Skript die Kennzahlen berechnet und nur die freigegebenen Dateien liest. Damit beantwortet das Dashboard beide Wünsche der Anfrage, die Übersicht über Begriffe und Regeln und die Frage nach den umsatzstärksten Produkten und Ländern.

Prompt 4 prüft. Der Agent rechnet jede Kennzahl mit einem eigenen Skript direkt aus den Excel-Dateien nach und listet Abweichungen auf. Zum Schluss rechnen Sie eine Kennzahl selbst in Excel nach. Der dritte Prompt überträgt das Rechnen einem Skript, der vierte sorgt für eine unabhängige Prüfung. Beide Regeln vertiefen wir gleich auf der Folie zur Qualitätssicherung.

## Folie 62. Subagents

Klasse: fertig

Subagents kennen Sie aus den Hands-ons. Diese Folie zeigt drei Arten, wie ein Agent Arbeit verteilt. Bei Subagents gibt ein Hauptagent Teilaufgaben an Helfer ab und entscheidet nach jedem Ergebnis, was als Nächstes passiert. Die Helfer arbeiten mit eigenem Context Window und kennen nur ihren Auftrag.

Bei Agent Teams verteilt ein Team Lead die Arbeit an eigenständige Sessions, die sich über eine gemeinsame Aufgabenliste und direkte Nachrichten selbst abstimmen. Das eignet sich für Review aus mehreren Blickwinkeln und für konkurrierende Hypothesen. Die Funktion ist experimentell. Bei Dynamic Workflows schreibt Claude ein Skript, das den Ablauf vorab festlegt und viele Subagents steuert. Unterwegs entscheidet dann kein Agent mehr. Mit dem Schalter Ultracode plant Claude für jede größere Aufgabe selbst einen solchen Workflow.

Mehr Agents verbrauchen mehr Tokens. Sie lohnen sich für Recherche, Prüfung und Lesen, beim parallelen Schreiben kollidieren sie leicht.

- Befund: Der Titel Subagents wiederholt den Titel von Folie 23, und die Dokumentationslinks unterscheiden sich (docs/en/agents hier, docs/en/sub-agents auf Folie 23).

## Folie 63. Qualität sichern: Skript, wo möglich, Urteil, wo nötig

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die vorhandene Notiz ist Stichwortmaterial mit Label-Präfixen („Beispiele:“, „Zu Test Driven Development:“) und liest sich als Hinweis für Bearbeitende, kaum als gesprochener Text.
- Befund: „Abnahme“ steht hier für die Sichtprüfung durch den Menschen (Skriptum „Sichtprüfung“), auf Folie 72 und im Glossar (Acceptance) für die Entscheidung, einen geprüften Stand zu verwenden. Der Begriff hat damit zwei Bedeutungen.

## Folie 64. Hook: nur im Projektordner arbeiten

Klasse: fertig

Diese Folie zeigt, wie eine Regel durchgesetzt wird. Eine Regel in der CLAUDE.md liest der Agent, und er kann sie übersehen. Einen Hook setzt der Harness durch. Ein Hook ist ein Skript, das der Harness bei einem Ereignis ausführt, hier vor jedem Schreibwerkzeug. Endet das Skript mit Exit-Code 2, wird der Aufruf blockiert, und der Agent erhält die Begründung.

Das Beispiel auf der Folie trägt den Hook in die Datei settings.json ein. Das Skript schutz.py liest den Zielpfad, und liegt er außerhalb des Projektordners, blockiert es den Aufruf.

Ebenso wichtig sind die Grenzen. Der Hook prüft nur die Datei-Werkzeuge, Shell-Befehle umgehen ihn. In Hands-on 6 liest der Agent die Excel-Dateien per Python, ein Hook auf das Lesewerkzeug hätte mitarbeitende.xlsx dort also nicht geschützt. Eine Sandbox reicht weiter. Auch sie isoliert nicht vollständig und läuft unter nativem Windows nicht.

- Befund: Die Folie sagt, eine Sandbox „isoliert aber nicht vollständig“. Das Skriptum schreibt „Vollständigen Schutz bietet erst eine Sandbox“, und das Glossar (Sandbox) nennt sie „the complete protection“.

## Folie 65. Open Models: das Modell im eigenen Haus

Klasse: fertig

Bisher haben wir mit Frontier-LLMs in der Cloud gearbeitet. Diese Folie zeigt die Alternative im eigenen Haus. Open-Weight-Modelle sind frei herunterladbar und laufen auf eigener Hardware, etwa mit Ollama. Trainingsdaten und Code bleiben meist verschlossen, Open Weights ist deshalb etwas anderes als Open Source.

Auf der Folie stehen vier Eigenschaften. Open Models sind privat, weil die Daten den Rechner nicht verlassen. Sie sind anpassbar, weil sich ein Modell auf eine Aufgabe und eigenes Wissen zuschneiden lässt. Sie machen unabhängig, weil kein Anbieter Preis, Modell oder Bedingungen über Nacht ändert. Und sie sind begrenzt, schwächer als die stärksten geschlossenen Modelle, und auch Hardware und Betrieb kosten.

Der Grundsatz dahinter heißt Boring AI. Gemeint ist das kleinste Werkzeug, das die Aufgabe löst, und oft reicht dafür ein Skript oder ein kleines Modell. Die folgenden Folien zeigen drei solche Pipelines.

## Folie 66. Eigene Pipelines: der Agent baut, das lokale Modell arbeitet

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Prompt und GitHub-Link zeigen auf workshops/2026-11-09-ufl/lokale-workflows. Nach der Regel des Repositorys wird ein gehaltener Workshop-Ordner aus dem Arbeitsbaum entfernt, die Links brechen dann bei Wiederverwendung des Decks.

## Folie 67. Mails anonymisieren: der Code ersetzt, das LLM benennt

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Prompt und GitHub-Link zeigen auf workshops/2026-11-09-ufl/lokale-workflows. Nach der Regel des Repositorys wird ein gehaltener Workshop-Ordner aus dem Arbeitsbaum entfernt, die Links brechen dann bei Wiederverwendung des Decks.
- Befund: Die vorhandene Notiz beginnt mit der Regieanweisung „Live zeigen:“ und einem Befehl, der Rest ist sprechbar.

## Folie 68. PDF zu Markdown: Docling liest das Layout

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Prompt und GitHub-Link zeigen auf workshops/2026-11-09-ufl/lokale-workflows. Nach der Regel des Repositorys wird ein gehaltener Workshop-Ordner aus dem Arbeitsbaum entfernt, die Links brechen dann bei Wiederverwendung des Decks.
- Befund: Die vorhandene Notiz beginnt mit der Regieanweisung „Live zeigen:“ und Befehlszeilen, der Rest ist sprechbar.

## Folie 69. Sprache zu Text: Whisper transkribiert, eine Namensliste hilft

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Prompt und GitHub-Link zeigen auf workshops/2026-11-09-ufl/lokale-workflows. Nach der Regel des Repositorys wird ein gehaltener Workshop-Ordner aus dem Arbeitsbaum entfernt, die Links brechen dann bei Wiederverwendung des Decks.
- Befund: Die vorhandene Notiz beginnt mit der Regieanweisung „Live zeigen:“ und Aufrufparametern, der Rest ist sprechbar.

## Folie 70. 

Klasse: fertig

Die Abbildung fasst Promptotyping in einem Bild. In die Arbeit gehen drei Dinge ein, die Daten, mit denen gearbeitet wird, die Fachdomäne mit einer Expertin oder einem Experten in the Loop und ein Frontier-LLM zusammen mit Context Engineering. Heraus kommen Artefakte, etwa Werkzeuge, Workflows oder Modelle. Der Begriff Co-Intelligence steht dort, wo Fachwissen und LLM zusammentreffen.

Die Abbildung stammt aus der Forschung, deshalb ist von Research Data und Research Artefacts die Rede. Für Ihre Arbeit lesen Sie das als Daten und Ergebnisse Ihres eigenen Bereichs. Was Sie in den Hands-ons gebaut haben, die Wissensbasis, das Dashboard und der Vault, sind solche Artefakte.

## Folie 71. https://dhcraft.org/Promptotyping

Klasse: fertig

Ab hier fassen wir zusammen, was Sie in den drei Einheiten gemacht haben. Promptotyping ist eine Arbeitspraxis, die Forschungsdaten und ihre Kontexte in Artefakte übersetzt, die zu Fragen und Arbeitsweisen der Forschenden passen. Eine kuratierte Wissensbasis zum Projekt gibt Menschen und Agents während der iterativen Entwicklung einen gemeinsamen Kontext. Promptotyping baut auf Agentic Engineering auf. Das Projektwissen wird an den Quellen geprüft, und ob das Ergebnis fachlich stimmt, entscheiden die Forschenden.

Die Arbeit verläuft in vier Arbeitsformen, Preparation, Exploration, Distillation und Implementation, und Knowledge Curation läuft durch alle vier. Auf der nächsten Folie ordnen wir Ihre Hands-ons diesen Arbeitsformen zu.

Auf der Folie finden Sie die Methodenseite, das Repository und zwei Einführungsvideos, das zweite als Live-Demo mit Claude Code. Die Videos zeigen den Stand ihres Aufnahmedatums, und Modelle und Werkzeuge ändern sich laufend.

- Befund: Das Titelfeld enthält zwei zusammengeschriebene URLs (Methodenseite und Repository) und keinen Titel. Auch im Folientext stehen beide URLs ohne Trennung.

## Folie 72. Was Sie gemacht haben: ein Durchlauf Promptotyping

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die Zeile Implementation nennt „3, 4, 6“ für PDF, Dashboard und Datenansicht. Im Deck ist das PDF Hands-on 4 (Folie 36) und das Dashboard Hands-on 5 (Folie 40).
- Befund: Die Zeile Verification nennt Hands-on 4 für den Subagenten als Reviewer, der Review-Prompt steht im Deck unter Hands-on 5 (Folie 42). Die vorhandene Notiz übernimmt „Subagent aus Hands-on 4“.
- Befund: Die Zeile Scholarly Validation nennt „3, 6“ für „PDF ansehen“, das PDF entsteht im Deck in Hands-on 4.
- Befund: Die Zeile Knowledge Curation nennt „3, 4, 5“ für Kuratieren, Vault bauen und Skill ableiten. Im Deck liegen Kuratieren und Vault in Hands-on 5 und das Ableiten der Skills nach Hands-on 4 (Folie 38).

## Folie 73. Engineering-Begriffe: was jeweils gestaltet wird

Klasse: unfertig (Sichtbarer Entwurfsvermerk im Folientext („Entwurf“).)

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Die Spalte Im Workshop nennt „Meilensteinplan in Hands-on 4“. Den Implementierungsplan mit Meilensteinen verlangt im Deck das Wissensdashboard in Hands-on 5 (Folie 40).
- Befund: Die vorhandene Notiz sagt „Die ersten vier kennen Sie aus Session 1“. Die Lernziele auf Folie 4 nennen Agentic, Knowledge, Context und Harness Engineering, die ersten vier Zeilen der Tabelle Prompt, Context, Knowledge und Harness Engineering.

## Folie 74. Research Mission Control

Klasse: fertig

Keine neue Notiz, im Deck steht bereits eine.

- Befund: Folientext und vorhandene Notiz nennen die LLM-Rollen „AI Operator“ und „Operatoren“. Nach dem Glossar (Research Mission Control) heißt die LLM-Rolle ein Agent mit Rollentitel, etwa koordinierender Agent oder Projekt-Agent.
- Befund: Die vorhandene Notiz spricht vom „Vault aus Hands-on 3 bis 6“. Der Vault entsteht im Deck in Hands-on 5 (Folie 51).

## Folie 75. Second Brain Vault

Klasse: unfertig (Angekündigte Abbildung fehlt („Abbildung folgt“).)

Second Brain Vault überträgt das, was Sie im Workshop gebaut haben, auf ein persönliches Arbeitssystem über viele Projekte hinweg. Ein gepflegter Obsidian-Vault hält Ideen, Quellenlektüren und Bezüge zwischen Projekten. Die Projekt-Repositories halten ihr Wissen jeweils in einem Ordner knowledge, und der Agent folgt ausdrücklichen Verweisen zwischen beiden.

Auf der Folie stehen drei Punkte. Die Vorlage enthält synthetische Beispielnotizen, Skills, Konventionen und Strukturprüfungen, Sie können das System also an Beispieldaten ansehen. Eine automatische Suche über die Repositories gibt es nicht. Der Bericht eines Agenten gilt als ungeprüft, bis er an den Dateien geprüft ist, und erst bestätigte Befunde fließen über eine autorisierte Pflege in ihre Dokumente zurück.

Methodenseite und Repository sind auf der Folie verlinkt.

- Befund: Die URLs von Methodenseite und Repository stehen im Export ohne Trennung hintereinander.

## Folie 76. Grounded Vault

Klasse: unfertig (Angekündigte Abbildung fehlt („Abbildung folgt“).)

Grounded Vault richtet sich an Wissensarbeit, in der jede Aussage belegt sein muss. Es ist eine Architektur für Wissensbasen, in der jede inhaltliche Aussage einen maschinenlesbaren Anker zu ihrer Quelle trägt, bis zur einzelnen Passage, Datenzeile oder Berechnung. Diese Rückverfolgbarkeit heißt Provenienz. Grounded Vault ist ein Promptotyping-Profil für belegpflichtige Wissensarbeit.

Eine Kette aus fünf Schichten führt von den Quellen über Markdown, Destillate und Aussagen bis zum Output, und jede Schicht ist für sich prüfbar. Ebenso wichtig ist die Grenze. Agents erzeugen die Struktur, ob der Inhalt stimmt, behauptet die Architektur nicht. Das Ergebnis ist ein Prüfobjekt, das Fachleute Passage für Passage durchgehen.

Methodenseite und Repository sind auf der Folie verlinkt.

- Befund: Die URLs von Methodenseite und Repository stehen im Export ohne Trennung hintereinander.

## Folie 77. Fazit

Klasse: fertig

Zum Abschluss möchte ich mit Ihnen auf drei Fragen schauen. Wo in Ihrer Arbeit wäre eine solche Wissensbasis hilfreich, und welche Daten würden Sie unter welchen Bedingungen einbeziehen? Konnten Sie nachvollziehen, was Ihr Agent gerade tut, und wann wurde es unübersichtlich? Und was fehlt Ihnen noch, um ab morgen selbstständig damit zu arbeiten?

Die Übersicht auf der Folie fasst die Begriffe der drei Einheiten zusammen, geordnet nach den Engineering-Begriffen. Unter LLMs stehen die Grundlagen von den Jagged Alien Intelligences bis zu AI Agent, Harness und Subagents. Prompt Engineering steht für Ziele, Vorgaben und Erfolgskriterien, Knowledge Engineering für Wissensbasis, Wissensdokumente und Quellenverweise. Context Engineering umfasst Context Window, Context Rot und die CLAUDE.md, Harness Engineering die Permission Modes, Hooks und die Sandbox. Unter KI-Governance stehen Autonomie und Systemzugriff, mit denen der Workshop begonnen hat. Alle Begriffe finden Sie im Glossar.

- Befund: Das Skriptum hat keinen Abschnitt Fazit, die Notiz folgt allein der Folie.

## Folie 78. Ressourcen

Klasse: fertig

Die letzte Folie sammelt Literatur zum Weiterlesen, je einen Titel zu den Feldern dieses Workshops. Für Prompt Engineering steht eine systematische Übersicht über Prompting-Techniken. Für Knowledge Engineering stehen ein Beitrag zu Knowledge Engineering mit Large Language Models und das Lehrbuch zur Künstlichen Intelligenz, aus dem die Schritte der Wissensmodellierung stammen. Für Context Engineering steht ein Survey zu Context Engineering für LLMs, für Harness Engineering ein Paper, das den Harness als Laufzeitumgebung für Software-Agents beschreibt. Den Abschluss bildet eine begriffliche Taxonomie, die AI Agents und Agentic AI unterscheidet.

Alle Titel sind mit DOI oder Link angegeben. Weitere Literatur und die Videos finden Sie auf der Website zum Workshop und in der Playlist. Vielen Dank für Ihre Mitarbeit in den drei Einheiten.

- Befund: Sapkota et al. steht hier mit dem Jahr 2026, auf Folie 22 mit 2025, beide mit dem DOI 10.1016/j.inffus.2025.103599.
