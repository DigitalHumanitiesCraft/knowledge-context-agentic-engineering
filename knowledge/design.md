---
title: Design der Plattform
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
created: 2026-08-20
updated: 2026-08-20
language: de
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Fable 5)
related: [specification.md]
---

# Design der Plattform

Designhaltung, Motiv und Systemwerte für `docs/`. Die Plattform adressiert ein professionelles, internationales Publikum aus Wissenschaft und Firmenkontexten; sie muss ruhig, präzise und hochwertig wirken und die realen Foliendecks als visuelle Anker zeigen statt eigener Illustrationswelten.

## Motiv (Vorschlag, Operator-Entscheidung offen)

Leitmotiv ist der Weg von der Quelle zum geprüften Artefakt: Quelle, Wissensdokumente, Working Context, agentische Schleife, Prüfung, Artefakt. Dieses Motiv existiert bereits als weiße Workflow-Hauptvisualisierung der CLARIAH-Titelgrafik und wird zur visuellen Sprache der Plattform weitergeführt, als Linienführung im Header und als wiederkehrendes Diagrammvokabular. Es passt zum Thema, weil die Plattform genau das zeigt, was das Motiv behauptet, einen kuratierten Bestand und seine geprüften Ableitungen.

## Systemwerte

- **Grund**: Papierweiß, nahezu schwarze Typografie, großzügiger Weißraum; dunkles Theme nachrangig.
- **Akzent**: Türkis als einzige Signalfarbe, aus dem CLARIAH-Material übernommen, wo es Segment, Evidenz und Prüfpunkte markiert; hier für Links, aktive Zustände und das Motiv.
- **Marke**: DHCraft-Watercolor-Logo (Standardvariante aus `DigitalHumanitiesCraft/brand-assets`), sparsam gesetzt.
- **Typografie**: eine gut lesbare Grotesk über Google Fonts mit System-Fallback; Monospace für Prompts und Code, in Anlehnung an die Consolas-Promptrahmen der Decks.
- **Bildmaterial**: ausschließlich die Titelfolien-PNGs der Workshops und die Workflow-Visualisierung; keine Stockbilder, keine generischen KI-Illustrationen.
- **Karten**: Workshop-Einträge als Karten mit Titelbild, Datum, Veranstaltung, Zielgruppe und Links; Reihenfolge chronologisch.

## Offene Designentscheidungen

- Freigabe des Leitmotivs durch den Operator.
- Fontwahl (Vorschlag folgt mit dem ersten Plattform-Entwurf).
- Umgang mit dem dunklen Theme (mitliefern oder bewusst hell halten).
