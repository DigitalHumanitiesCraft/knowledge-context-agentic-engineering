---
title: Governance
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
related: [project.md, plan.md]
---

# Governance

Entscheidungsautorität, Quellenstatus und Grenzen für Menschen und Agenten in diesem Repo. Master-Instanz der Governance-Funktion nach der Promptotyping-Konvention; die erste Instanz liegt im Methodik-Repo `DigitalHumanitiesCraft/Promptotyping`.

## Rollen und Autorität

- **Critical Expert (Operator)** entscheidet: kanonischen Begriffswortlaut, Titel und Motiv, Veröffentlichungsschritte (Pages-Aktivierung, Lizenz, Ankündigungen), Rechtefragen, Löschung oder Umzug kanonischer Bestände, alle Drift-Auflösungen gegen den Vault-Kanon.
- **Agenten** führen aus: Struktur, Überführung, Plattformbau, Registerpflege, Verifikation; sie bereiten Entscheidungen mit Empfehlung vor und führen `journal.md` nach.

## Quellenstatus

| Bestand | kanonischer Ort |
| --- | --- |
| Master-Skriptum, Lecture Notes, Folientexte | dieses Repo (`skriptum/`, `slides/`) |
| Begriffe (bis zur Befüllung von `begriffe.md`) | die Vault-Atome des Autors |
| Workshop-Register | `docs/data/workshops.json` |
| Live-Decks | Google Slides, als Ausspielung; abweichende Formulierungen werden als Delta geprüft |
| CLARIAH-Hands-on (Prompts, Schema, Läufe) | `chpollin/zbz-ocr-tei/workshops/clariah-at-2026/` |
| Projektkoordination | Vault des Autors (Project Overview, ACTIVE-WORK) |

## Write-back

Änderungen am kanonischen Text passieren hier und werden committet; Google-Artefakte werden danach nachgezogen. Begriffsentscheidungen fließen zuerst in `begriffe.md` und von dort in Skriptum, Folien und die Vault-Atome. Erkenntnisse aus Workshops (Durchführung, Feedback) gehen in das jeweilige Profil und in `journal.md`.

## Rechte und Datenschutz

Keine Faksimiles in diesem Repo; Bildrechte der Hersch- und Zweig-Materialien liegen bei den Quellprojekten, verlinkt wird auf deren Bestände. Keine personenbezogenen Daten Dritter; Teilnehmendendaten von Workshops werden hier nie geführt. Die Lizenz des Repos ist eine offene Operator-Entscheidung; bis dahin gilt Standard-Copyright.

## Eskalation

Bei Widerspruch zwischen Repo, Vault und Google-Artefakten wird nicht still harmonisiert; der Widerspruch geht als benanntes Delta an den Operator.
