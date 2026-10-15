---
title: Verification, Validation und Acceptance
status: draft
created: 2026-10-15
updated: 2026-10-15
language: de
related: [../../knowledge/terms.md, ../full-lecture-notes-de.md, ../../slides/full-slide-deck.md]
---

# Verification, Validation und Acceptance

## Lernziel

Die Lernenden können an einem Editionsbeispiel unterscheiden, was ein technischer Prüfbefund zeigt, welche fachliche Frage offenbleibt und für welchen Zweck ein Projektzustand angenommen werden kann.

## Lehrtext

Ein AI Agent erzeugt aus einer Transkription eine TEI-Datei und daraus eine Editionsansicht. Der Schema-Check meldet keinen Fehler, und die Seite öffnet sich im Browser. Damit liegen technische Prüfergebnisse vor. Ob die Transkription die Quelle angemessen wiedergibt und die Oberfläche ihre Unsicherheiten erkennen lässt, muss gesondert untersucht werden.

Technical Verification prüft die Übereinstimmung mit festgelegten, überprüfbaren Anforderungen. Dazu gehören XML-Wohlgeformtheit, Schema-Konformität, auflösbare Referenzen und das Verhalten der Transformation. Ein Schema-Check untersucht die kodierten Strukturen anhand des verwendeten Schemas. Seine Aussage hängt davon ab, welche Anforderungen dieses Schema tatsächlich ausdrückt.

Validation bezeichnet in dieser Lehrlinie die fachliche Prüfung am Forschungszweck und an der Quelle. Bei einer digitalen Edition betrifft sie etwa die Angemessenheit einer Lesung, die Unterscheidung zwischen Ergänzung und unleserlicher Stelle und die Darstellung editorischer Unsicherheit. Automatisierte Vergleiche und agentische Reviews können dafür Befunde liefern. Quellenkenntnis und die Begründung einer editorischen Entscheidung gehören zur fachlichen Verantwortung im Projekt.

Acceptance ist die verantwortliche Annahme eines bezeichneten Zustands für einen bestimmten Zweck. Ein Zustand kann beispielsweise für eine interne Besprechung der Editionsansicht angenommen werden, während die Transkription noch fachlich geprüft wird. Eine Publikationsfreigabe braucht die für diesen weitergehenden Zweck erforderlichen Nachweise und eine eigene Entscheidung.

Prüfverfahren, prüfende Rolle und Annahmeentscheidung erfüllen unterschiedliche Funktionen. Ein weiterer Agent kann eine zusätzliche Prüfung durchführen und übersehene Probleme benennen. Sein Bericht hält fest, welche Quellen und Kriterien er verwendet hat und was er tatsächlich geprüft hat. Die fachliche Verantwortung und die Acceptance richten sich weiterhin nach der vereinbarten Zuständigkeit.

Die Fachsprache verwendet das Wort Validation auch für formale Prüfungen, etwa bei XML Schema Validation. Im Kurs benennen wir deshalb immer den Gegenstand der Prüfung. Der Ausdruck Schema-Validierung bezeichnet hier eine technische Prüfung. Er legt keine fachliche oder wissenschaftliche Annahme nahe.

## Folienfolge

### Folie 1. Welche Aussage trägt der Test?

- Der Schema-Check prüft die TEI-Struktur gegen ein bestimmtes Schema.
- Der Browser zeigt, ob die Editionsansicht im geprüften Ablauf funktioniert.
- Die Übereinstimmung einer Lesung mit der Quelle braucht einen eigenen Nachweis.

### Folie 2. Fachliche Prüfung am Editionsfall

- Quelle und Transkription vergleichen.
- Ergänzungen, Unsicherheiten und unleserliche Stellen unterscheiden.
- Prüfen, ob die Editionsansicht diese Unterscheidungen erhält.

### Folie 3. Acceptance benennt Zustand und Zweck

- Welcher Daten-, Wissens- und Softwarestand wird angenommen?
- Wofür reichen die vorhandenen Nachweise?
- Welche Einschränkung gilt, und wer trägt die Entscheidung?

### Folie 4. Ein Prüfbericht mit begrenzter Aussage

Ein technischer Prüfbefund nennt Gegenstand, Kriterium, Ergebnis und Grenzen. Eine fachliche Entscheidung nennt Quelle und Begründung. Die Acceptance verbindet den bezeichneten Zustand mit dem angenommenen Verwendungszweck.

## Übung

Der folgende Fall ist ein didaktisches Szenario, kein Bericht über einen ausgeführten Prüflauf. Eine TEI-Datei besteht den Schema-Check. In der Editionsansicht erscheint eine unsichere Lesung als gewöhnlicher Text. Ein weiterer Agent hält die Transkription für plausibel. Für eine interne Besprechung soll die Ansicht gezeigt werden.

1. Welche technische Aussage ist durch den beschriebenen Check gedeckt?
2. Welche fachliche Prüfung fehlt?
3. Was müsste vor einer Annahme zur internen Besprechung ausdrücklich sichtbar und dokumentiert werden?

## Besprechung der Übung

Der Schema-Check belegt Konformität mit dem verwendeten Schema. Ob die Lesung der Quelle entspricht, bleibt offen. Für die Editionsansicht ist außerdem zu prüfen, ob die Kodierung der Unsicherheit fehlt oder bei der Transformation verloren geht. Der zustimmende Agentenbericht ergänzt die Evidenz nur insoweit, wie sein tatsächlicher Quellenzugriff und Prüfumfang nachvollziehbar sind.

Für eine interne Besprechung kann die verantwortliche Person die Ansicht nach Prüfung ihres konkreten Zustands mit der Einschränkung annehmen, dass sie der Diskussion der Darstellung dient und die fragliche Lesung sichtbar ungeprüft bleibt. Aus dem beschriebenen Fall folgt noch keine erfolgte Acceptance.

## Redaktion und Quellenabgleich

Der Vorschlag baut auf den deutschen Full Lecture Notes, Abschnitte 7.7 bis 7.9 und 7.11, dem englischen Abschnitt Evaluation, Verification, Validation and Acceptance sowie dem Prüfbegriffsabschnitt in knowledge/terms.md auf. Der Fall konkretisiert die dort vorhandenen Kriterien und den Unsicherheitsfall aus Abschnitt 7.6. Er führt keine neue historische Quelle und keinen empirischen Prüfbefund ein.

Am 15. Oktober 2026 wurden die aktuelle deutsche Google-Docs-Fassung und der native Full Slide Deck lesend abgerufen. Die Begriffszuordnung von Abschnitt 7.7 entspricht dem lokalen deutschen Text. Die Bildunterschrift zu Abbildung 12 verwendet jedoch Deterministische Validation, während Technical Verification im Glossar die formale Prüfung bezeichnet. Der Entwurf löst diese Stelle durch Benennung des jeweiligen Prüfgegenstands auf. Das ist ein Vorschlag zur Autorenabnahme.

Die ältere CLARIAH-Fassung nennt die formale Prüfung Validation und die fachliche Prüfung Scholarly verification. Das Glossar dokumentiert diese Zuordnung bereits als veranstaltungsspezifische Variante. Der Vorschlag verwendet die Begriffe der Full Lecture Notes. Der native Foliensatz enthält unter anderem die Folien 5. Verification und die TEI-Prüfung durch Subagents, aber keine entsprechende zusammenhängende Begriffsfolge. Die hier formulierte Folge ist ein Textentwurf für ihre Ergänzung.

Die internen Definitionen und ihre Wiedergaben wurden verglichen. Eine neue externe Literaturprüfung oder empirische Evaluation der Prüfverfahren wurde nicht durchgeführt. Die fachliche Abnahme, die Übernahme in die gepflegten Lecture Notes und die native Gestaltung der Folien stehen aus.

- [Deutsche Full Lecture Notes](../full-lecture-notes-de.md), Abschnitte 7.6 bis 7.11.
- [Englische Full Lecture Notes](../full-lecture-notes-en.md), Evaluation, Verification, Validation and Acceptance.
- [Begriffsvertrag](../../knowledge/terms.md), Prüfbegriffe und CLARIAH-Zuordnung.
- [Lokaler Foliensatz](../../slides/full-slide-deck.md), Verification und TEI-Prüfung.
- [CLARIAH-Lecture-Notes](../../workshops/2026-09-25-clariah-at/lecture-notes.md), Evaluation, Validation and Scholarly Verification.
- [Aktuelle deutsche Google-Fassung](https://docs.google.com/document/d/1rJRraAfBfnkrb_3ik4savYuboLPhZ-zAFvlj4CmmMcE/edit).
- [Nativer Full Slide Deck](https://docs.google.com/presentation/d/1FtJpBn8l49I6B-r6b8bdIsbTngLQ9-LdP5BeylXD3M4/edit).
