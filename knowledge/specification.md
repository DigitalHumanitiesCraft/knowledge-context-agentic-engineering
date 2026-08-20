---
title: Spezifikation Plattform und Repo-Struktur
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
related: [project.md, design.md]
---

# Spezifikation Plattform und Repo-Struktur

Anforderungen an die öffentliche Plattform (`docs/`, GitHub Pages) und die tragende Repo-Struktur.

## Anforderungen

1. Die Startseite zeigt den Masterbestand (Titel, Kurzbeschreibung, Zugänge zu Skriptum und Folientexten) und darunter das Register aller Workshop-Instanzen.
2. Jede Workshop-Zeile zeigt Datum, Titel, Veranstaltung, Zielgruppe, Schwerpunkt, Sprache und Status sowie die Links auf das Google-Slides-Live-Deck, das Skriptum und die PPTX-Exporte.
3. Jeder Workshop hat einen visuellen Anker, das Titelfolien-PNG unter `docs/assets/covers/<id>.png`; die Karte auf der Plattform zeigt es.
4. Das Register lebt als eine Datei, `docs/data/workshops.json`; ein neuer Workshop ist genau ein Eintrag dort plus ein Profilordner.
5. Unterricht läuft immer über Google Slides; die Plattform verlinkt die Live-Decks und hält PPTX-Exporte als versionierte Stände unter `workshops/<id>/`. Ein eingebetteter Viewer ist optional und nachrangig gegenüber Link plus Titelbild.
6. Die Site ist statisch ohne Build-Schritt (HTML, CSS, Vanilla JS), englischsprachig, responsiv, und lädt außer Google Fonts keine externen Ressourcen.

## Akzeptanzkriterien

- Das Register rendert vollständig aus `workshops.json`; ein Testeintrag erscheint ohne Änderung am HTML.
- Alle Links des Registers lösen auf; fehlende Artefakte (`null`) erzeugen keinen toten Link, sondern entfallen sichtbar.
- Die Seite ist ohne JavaScript lesbar (Basisinhalt), mit JavaScript vollständig.
- Titelbilder haben Alt-Texte mit Workshop-Titel und Datum.

## Entscheidungen

- Registry als eine JSON-Datei statt Frontmatter-Sammlung, weil die Plattform ohne Build-Schritt rendert und ein Eintrag pro Workshop die kleinste Pflegeeinheit ist (2026-08-20).
- Titelbilder als PNG-Export der ersten Folie, vom Operator geliefert, weil sie die realen Deck-Varianten zeigen (2026-08-20).
