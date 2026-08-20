---
title: Projekt-Charter
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
related: [specification.md, governance.md, plan.md]
---

# Projekt-Charter

Das Repo ist der kanonische Masterbestand der Lehrlinie *Knowledge, Context and Agentic Engineering for Knowledge Work* und trägt die Plattform, die diesen Bestand und seine Workshop-Ableitungen öffentlich zeigt.

## Master-Profil-Modell

Der Master enthält das vollständige Material, domänenneutral: LLM-Grundlagen, die vier Engineering-Ebenen, Promptotyping, Verifikation. Er ist intern zweigeteilt in einen generischen Kern und austauschbare Fallstudien-Module (aktuell Hersch und Zweig für Forschungsdaten und Editionen). Ein Workshop-Profil ist eine dokumentierte Spezialisierung: Es wählt aus dem Master Kern-Abschnitte, Fallstudien und Tiefe für eine konkrete Zielgruppe. Drei Profile sind angelegt, KUG/M3GIM (kompakt, ohne Vorwissen), CLARIAH-AT (Forschungsdaten und Editionen, DH-Studierende), Uni for Life (ausführlich, Firmen und andere Disziplinen).

## Bestandskarte

| Bestand | Ort | Status |
| --- | --- | --- |
| Master-Skriptum (deutsch) | `skriptum/`, Überführung aus dem Vault offen | geplant |
| Lecture Notes CLARIAH-AT (englisch) | `skriptum/`, Volltext gesichert | geplant |
| Master-Folientexte mit Speaker Notes | `slides/`, Überführung aus dem Vault offen | geplant |
| Workshop-Profile | `workshops/<id>/` | geplant |
| Folien-Exporte (PPTX je Stand) und Titelbilder (PNG) | `workshops/<id>/` bzw. `docs/assets/covers/` | geplant |
| Live-Decks | Google Slides, verlinkt im Register `docs/data/workshops.json` | laufend |
| ausführbares Hands-on-Paket CLARIAH | Repo `chpollin/zbz-ocr-tei`, `workshops/clariah-at-2026/` | extern, verlinkt |
| Projektkoordination und thematische Wissensbasis | Obsidian-Vault des Autors | extern |

## Zielgruppenmodell

Drei Zielgruppen strukturieren die Profile: DH-Studierende mit Vorwissen (akademisch, englisch- oder deutschsprachig), Teilnehmende ohne LLM- und Programmiervorwissen (kompakte Einstiege), Professionals aus Firmen und anderen Disziplinen (Wissensarbeit jenseits der Forschung). Jedes Profil benennt Zielgruppe und Vorwissen explizit.
