---
title: Critical Perspectives and Governance
module: 5
source-language: [de, en]
status: draft
created: 2026-08-20
units: [M13, M18, M19]
canonical: false
canonical-gate: operator confirmation of the module cut
source-masters: [script/master-script-de.md, script/master-script-en.md]
---

# Module 5 — Critical Perspectives and Governance

> Draft cut of the master corpus. Every passage below is reproduced verbatim from a master
> script; only the module heading, the unit headings and the provenance lines are added.
> The masters stay authoritative until the operator confirms the cut. Coverage, discarded
> parallel versions and open questions are recorded in `script/COVERAGE.md`.


## Unit M13 — Verification, Validation and the Critical Expert

*Source: `master-script-de.md`, sections 7.7 and 7.8.*

## 7.7 Verification, Validation und Acceptance

Drei Ebenen müssen unterschieden werden.

**Abbildung 12: Prüfung, Evidenz und verantwortliche Acceptance.**  
*Deterministische Validation und agentisches Review liefern überprüfbare Evidenz. Die fachliche und wissenschaftliche Beurteilung verbleibt beim Critical Expert. Erst diese verantwortliche Prüfung kann zu einer zweckgebundenen Acceptance führen; technische Konformität allein autorisiert kein Forschungsartefakt.*

### Technische Verifikation

Prüft Konformität mit formalisierten Anforderungen:

- XML ist wohlgeformt;  
- TEI entspricht dem Schema;  
- Tests laufen erfolgreich;  
- Transformationen erzeugen die erwarteten Dateien;  
- Quelldateien wurden nicht verändert.

### Fachliche und wissenschaftliche Validierung

Prüft, ob Repräsentation und Artefakt für den vorgesehenen Forschungszweck angemessen sind:

- Entspricht die Transkription der Quelle?  
- Sind editorische Unsicherheiten angemessen repräsentiert?  
- Unterstützt das Interface die vorgesehenen Interpretationshandlungen?  
- Werden Modellierungsentscheidungen sichtbar oder irreführend naturalisiert?

### Acceptance

Bezeichnet die verantwortliche Entscheidung, einen identifizierbaren Projektzustand für einen benannten Zweck anzunehmen.

Ein technisch verifiziertes Artefakt kann wissenschaftlich ungeeignet sein. Umgekehrt kann ein wissenschaftlich interessanter Demonstrator technisch noch nicht publikationsreif sein. Acceptance muss deshalb zweckgebunden formuliert werden.

## 7.8 Critical Expert

Der **Critical Expert** trägt die Verantwortung dort, wo Prüfung Quellenkenntnis, Interpretation oder Designurteil verlangt.

Agents und Validatoren können:

- Fehler lokalisieren,  
- Kriterien anwenden,  
- Unterschiede berichten,  
- Evidenz zusammenstellen.

Der Critical Expert entscheidet:

- welche Lesung vertretbar ist;  
- ob eine Modellierung der Quelle angemessen entspricht;  
- ob die Oberfläche wissenschaftliche Differenzierungen erhält;  
- ob der Zustand für den benannten Zweck akzeptiert wird.

Die Rolle ist nicht auf eine einzelne Person beschränkt. Sie bezeichnet die verantwortliche fachliche Autorität im Projekt.

*Source: `master-script-de.md`, section 7.11.*

## 7.11 Hands-on: Write-back und Acceptance dokumentieren

### Write-back

Analysieren Sie die Implementation und dokumentieren Sie:

- neue Erkenntnisse über die Quelle,  
- neue Anforderungen,  
- unzureichende Regeln,  
- offene fachliche Fragen,  
- notwendige Änderungen an Datenmodell oder Frontend.

### Acceptance Statement

\<a id="acceptance-statement-2"\>\</a\>

\# Acceptance Statement

\<a id="identifizierter-zustand"\>\</a\>

\#\# Identifizierter Zustand

\- Knowledge Base: Commit \`abc123\`

\- TEI-Daten: Version \`0.3\`

\- Frontend: Build \`2026-08-01\`

\- Schema: \`edition.rng\`, Version \`1.2\`

\<a id="accepted-for"\>\</a\>

\#\# Accepted for

Interner Demonstrator zur Prüfung des TEI-Modells und der synoptischen

Darstellung von Faksimile, diplomatischer Transkription und Normalisierung.

\<a id="technisch-verifiziert"\>\</a\>

\#\# Technisch verifiziert

\- XML-Wohlgeformtheit

\- Schema-Konformität

\- erfolgreiche lokale Transformation

\- unveränderte Quelldateien

\- Navigation zwischen den Beispielseiten

\<a id="fachlich-gepruft"\>\</a\>

\#\# Fachlich geprüft

\- Zuordnung von Faksimile und Transkription

\- Darstellung der markierten Unsicherheiten

\- Nachvollziehbarkeit editorischer Eingriffe

\<a id="nicht-nachgewiesen"\>\</a\>

\#\# Nicht nachgewiesen

\- vollständige philologische Verifikation des Korpus

\- Eignung für eine öffentliche oder zitierfähige Edition

\- Barrierefreiheit und produktive Langzeitverfügbarkeit

\<a id="offene-fragen"\>\</a\>

\#\# Offene Fragen

\- Unterscheidung zwischen teilweise lesbaren und ergänzten Eigennamen

\- Darstellung konkurrierender Normalisierungen


## Unit M18 — Project Governance and Research Mission Control

No text in either master covers this unit. The nearest adjacent material is carried
elsewhere: knowledge-base governance and curation in module 3 (DE section 5.7),
least-privilege permissions in module 4 (DE section 6.4) and human intervention points
in module 4 (DE section 6.6). See `script/COVERAGE.md`.


## Unit M19 — Limits, Glossary and Apparatus

*Source: `master-script-de.md`, chapter 8, summary and glossary of the four layers.*

# 8\. Zusammenfassung und Begriffsübersicht

Die vier Engineering-Ebenen erfüllen unterschiedliche Funktionen:

| Ebene | Gegenstand | Leitfrage |
| :---- | :---- | :---- |
| Prompt Engineering | aktuelle Eingabesequenz | Wie wird die Aufgabe formuliert? |
| Knowledge Engineering | persistenter Wissensbestand | Was muss explizit dokumentiert und gepflegt werden? |
| Context Engineering | Informationszustand einer Aufgabe | Welche Informationen benötigt der Agent jetzt? |
| Agentic Engineering | mehrschrittige Ausführung | Wie wird die Arbeit organisiert, begrenzt und geprüft? |

Promptotyping verbindet diese Ebenen in einem iterativen Forschungsworkflow.

Die zentrale Formel lautet:

> **Prompt Engineering gestaltet die aktuelle Eingabesequenz.**  
> **Context Engineering organisiert den Informationszustand einer Aufgabe.**  
> **Knowledge Engineering baut und pflegt den dafür verfügbaren Wissensbestand.**  
> **Agentic Engineering organisiert die mehrschrittige Ausführung.**  
> **Promptotyping verbindet diese Ebenen in der iterativen Entwicklung und verantwortlichen Prüfung digitaler Forschungsartefakte.**

Die digitale Edition zeigt, warum diese Verbindung notwendig ist. Quelle, Transkription, Datenmodell, Transformation und Frontend bilden keinen neutralen technischen Ablauf. Jede Stufe enthält Entscheidungen darüber, welche Unterschiede sichtbar, bearbeitbar und interpretierbar werden. AI Agents können diese Arbeit erheblich unterstützen. Sie können jedoch die fachliche Verantwortung für Repräsentation, Validierung und Acceptance nicht übernehmen.

*Source: `master-script-de.md`, chapter 9, bibliography.*

# 9\. Literaturverzeichnis

Anthropic. 2025\. “Claude’s Character.” Anthropic Research.

Anthropic. 2026\. “Claude’s Constitution.” Anthropic.

Battle, Rick, and Teja Gollapudi. 2024\. “The Unreasonable Effectiveness of Eccentric Automatic Prompts.” arXiv:2402.10949.

Hong, Kelly, Anton Troynikov, and Jeff Huber. 2025\. “Context Rot: How Increasing Input Tokens Impacts LLM Performance.” Chroma Research.

Hu, Tiancheng, and Nigel Collier. 2024\. “Quantifying the Persona Effect in LLM Simulations.” arXiv:2402.10811.

Li, Cheng, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, and Xing Xie. 2023\. “Large Language Models Understand and Can Be Enhanced by Emotional Stimuli.” arXiv:2307.11760.

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. 2025\. “On the Biology of a Large Language Model.” Transformer Circuits.

Mei, et al. 2025\. “Context Engineering for Large Language Models.” arXiv:2507.13334.

Pollin, Christopher. 2026\. “Asymmetric Amplification.” Digital Humanities Craft.

Pollin, Christopher. 2026\. “Promptotyping.” Manuskript in Vorbereitung.

Rajeev, Meghana, Rajkumar Ramamurthy, Prapti Trivedi, et al. 2025\. “Cats Confuse Reasoning LLM: Query Agnostic Adversarial Triggers for Reasoning Models.” arXiv:2503.01781.

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. 2024\. “The Prompt Report: A Systematic Survey of Prompting Techniques.” arXiv:2406.06608.

Yin, Ziqi, Hao Wang, Kaito Horio, Daisuke Kawahara, and Satoshi Sekine. 2024\. “Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance.” arXiv:2402.14531.

*Source: `master-script-en.md`, "References".*

## **References**

Allen, Bradley P., et al. “Knowledge Engineering Using Large Language Models.” *Transactions on Graph Data and Knowledge* 1, no. 1, 2023. https://doi.org/10.4230/TGDK.1.1.3.

Anthropic. “Claude’s Character.” https://www.anthropic.com/research/claude-character.

Anthropic. “Claude’s Constitution.” 2026. https://www.anthropic.com/constitution.

Anthropic. “Claude’s New Constitution.” 2026. https://www.anthropic.com/research/claude-new-constitution.

Anthropic. “Effective Context Engineering for AI Agents.” 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents.

Bengio, Yoshua. “Godfather of AI: How To Make Safe Superintelligent AI.” Interview with Rob Wiblin. *80,000 Hours*, 2026. https://youtu.be/PZqDFs2sbiY.

Brown, Tom B., et al. “Language Models are Few Shot Learners.” 2020. https://arxiv.org/abs/2005.14165.

Chollet, François. “How I Think About LLM Prompt Engineering.” 2023. https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering.

Dell’Acqua, Fabrizio, et al. “Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality.” *Organization Science* 37, no. 2, 2026, 403 to 423. https://doi.org/10.1287/orsc.2025.21838.

Gans, Joshua. “A Model of Artificial Jagged Intelligence.” 2026. https://doi.org/10.48550/arXiv.2601.07573.

Geiger, Philipp. “Daten / Forschungsdaten.” 2024. https://doi.org/10.17175/wp_2023_003_v2.

Hong, Kelly, Anton Troynikov, and Jeff Huber. *Context Rot: How Increasing Input Tokens Impacts LLM Performance*. Chroma, 2025. https://research.trychroma.com/context-rot.

Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez Quiñones. “Personal Information Management.” 2017. https://doi.org/10.1081/E-ELIS4-120053695.

Li, Chloe, Nevan Wichers, Sara Price, Samuel Marks, and Jon Kutasov. “Model Spec Midtraining: Improving How Alignment Training Generalizes.” 2026. https://arxiv.org/abs/2605.02087.

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. “On the Biology of a Large Language Model.” Transformer Circuits, 2025. https://transformer-circuits.pub/2025/attribution-graphs/biology.html.

Majithia, A., et al. “An Actionable Framework for AI Ready Data.” 2026. https://doi.org/10.1002/aaai.70054.

Mei, Lingrui, Jiayu Yao, Yuyao Ge, et al. “A Survey of Context Engineering for Large Language Models.” 2025. https://doi.org/10.48550/arXiv.2507.13334.

Ouyang, Long, et al. “Training Language Models to Follow Instructions with Human Feedback.” 2022. https://arxiv.org/abs/2203.02155.

Pollin, Christopher. *Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example*. Graz, 2025. https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602.

Pollin, Christopher. “Asymmetric Amplification. Why AI Does Not Automate Research, But Disruptively Amplifies Computer Based Research Work.” Digital Humanities Craft, 2026. https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

Pollin, Christopher. *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*. Review draft 0.9, 2026.

Russell, Stuart J., and Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th ed. Pearson, 2020. https://aima.cs.berkeley.edu.

Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. “AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges.” *Information Fusion* 126, 2025, 103599. https://doi.org/10.1016/j.inffus.2025.103599.

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. “The Prompt Report: A Systematic Survey of Prompting Techniques.” 2024. https://doi.org/10.48550/arXiv.2406.06608.

Sofroniew, Nicholas, Isaac Kauvar, William Saunders, et al. “Emotion Concepts and Their Function in a Large Language Model.” 2026. https://transformer-circuits.pub/2026/emotions/index.html.

Summerfield, Christopher. *These Strange New Minds: How AI Learned to Talk and What It Means*. Viking, 2025.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. “Attention Is All You Need.” *Advances in Neural Information Processing Systems* 30, 2017. https://arxiv.org/abs/1706.03762.

Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, et al. “Voyager: An Open Ended Embodied Agent with Large Language Models.” 2023. https://arxiv.org/abs/2305.16291.

Wilkinson, Mark D., et al. “The FAIR Guiding Principles for Scientific Data Management and Stewardship.” *Scientific Data* 3, 2016. https://doi.org/10.1038/sdata.2016.18.

Wooldridge, Michael, and Nicholas R. Jennings. “Intelligent Agents: Theory and Practice.” *The Knowledge Engineering Review* 10, no. 2, 1995, 115 to 152. https://doi.org/10.1017/S0269888900008122.

Zhong, Hailin, and Shengxin Zhu. “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents.” 2026. https://doi.org/10.48550/arXiv.2605.13357.

*Source: `master-script-de.md`, chapter 10, templates A through E.*

# 10\. Anhang: Vorlagen

## A. Vorlage für ein Wissensdokument

\---

document\_type: knowledge

status: draft

owner:

sources:

last\_reviewed:

\---

\<a id="gegenstand"\>\</a\>

\# Gegenstand

\<a id="zweck"\>\</a\>

\#\# Zweck

\<a id="begriffe-und-unterscheidungen"\>\</a\>

\#\# Begriffe und Unterscheidungen

\<a id="regeln"\>\</a\>

\#\# Regeln

\<a id="einschrankungen-und-ausnahmen"\>\</a\>

\#\# Einschränkungen und Ausnahmen

\<a id="unsicherheiten"\>\</a\>

\#\# Unsicherheiten

\<a id="offene-fragen-2"\>\</a\>

\#\# Offene Fragen

\<a id="quellen"\>\</a\>

\#\# Quellen

## B. Vorlage für eine Instruktionsdatei

\<a id="rolle-und-arbeitsmodus"\>\</a\>

\# Rolle und Arbeitsmodus

\<a id="projektstruktur"\>\</a\>

\# Projektstruktur

\<a id="verbindliche-arbeitsregeln"\>\</a\>

\# Verbindliche Arbeitsregeln

\<a id="werkzeuge-und-befehle"\>\</a\>

\# Werkzeuge und Befehle

\<a id="regeln-fur-ruckfragen-und-eskalation"\>\</a\>

\# Regeln für Rückfragen und Eskalation

\<a id="abschlusskriterien"\>\</a\>

\# Abschlusskriterien

\<a id="verweise-auf-wissensdokumente"\>\</a\>

\# Verweise auf Wissensdokumente

## C. Vorlage für einen Working Context

\<a id="aufgabe-2"\>\</a\>

\# Aufgabe

\<a id="relevante-anforderungen"\>\</a\>

\# Relevante Anforderungen

\<a id="bereitgestellte-wissensdokumente"\>\</a\>

\# Bereitgestellte Wissensdokumente

\<a id="ausgangsdateien-und-daten"\>\</a\>

\# Ausgangsdateien und Daten

\<a id="verfugbare-werkzeuge"\>\</a\>

\# Verfügbare Werkzeuge

\<a id="aktueller-projektzustand"\>\</a\>

\# Aktueller Projektzustand

\<a id="prufkriterien-2"\>\</a\>

\# Prüfkriterien

\<a id="bekannte-unsicherheiten"\>\</a\>

\# Bekannte Unsicherheiten

\<a id="bewusst-nicht-geladene-ressourcen"\>\</a\>

\# Bewusst nicht geladene Ressourcen

## D. Vorlage für einen Verification Report

\<a id="verification-report"\>\</a\>

\# Verification Report

\<a id="identifizierter-zustand-2"\>\</a\>

\#\# Identifizierter Zustand

\<a id="ausgefuhrte-technische-prufungen"\>\</a\>

\#\# Ausgeführte technische Prüfungen

\<a id="ergebnisse"\>\</a\>

\#\# Ergebnisse

\<a id="abweichungen"\>\</a\>

\#\# Abweichungen

\<a id="nicht-geprufte-aspekte"\>\</a\>

\#\# Nicht geprüfte Aspekte

\<a id="fachliche-fragen"\>\</a\>

\#\# Fachliche Fragen

\<a id="empfohlene-nachste-schritte"\>\</a\>

\#\# Empfohlene nächste Schritte

## E. Vorlage für ein Acceptance Statement

\<a id="acceptance-statement-3"\>\</a\>

\# Acceptance Statement

\<a id="identifizierter-zustand-3"\>\</a\>

\#\# Identifizierter Zustand

\<a id="accepted-for-2"\>\</a\>

\#\# Accepted for

\<a id="technisch-verifiziert-2"\>\</a\>

\#\# Technisch verifiziert

\<a id="fachlich-gepruft-2"\>\</a\>

\#\# Fachlich geprüft

\<a id="nicht-nachgewiesen-2"\>\</a\>

\#\# Nicht nachgewiesen

\<a id="offene-fragen-3"\>\</a\>

\#\# Offene Fragen

\<a id="verantwortliche-entscheidung"\>\</a\>

\#\# Verantwortliche Entscheidung  

*Source: `master-script-en.md`, appendix templates.*

## **Appendix: Knowledge Document Template**

```markdown
# Subject

## Purpose

## Concepts and Distinctions

## Relevant Evidence and Sources

## Rules and Constraints

## Relationships and Dependencies

## Uncertainties

## Open Questions

## Decisions

## Provenance
```

## **Appendix: Agent Instruction Template**

```markdown
# Role and Working Mode

# Project Structure

# Binding Working Rules

# Tools and Commands

# Permissions and Boundaries

# Rules for Questions and Escalation

# Completion Criteria

# References to Knowledge Documents
```

## **Appendix: Working Context Template**

```markdown
# Task

# Relevant Requirements

# Provided Knowledge

# Data and Resource Access

# Instructions

# Tools

# Current State

# Verification Criteria

# Escalation Conditions
```

## **Appendix: Verification Report**

```markdown
# Object

# Version or State

# Verification Criteria

# Checks Performed

# Results

# Failures and Warnings

# Unverified Properties

# Evidence
```

## **Appendix: Validation and Acceptance Record**

```markdown
# Object

# Intended Purpose

# Relevant Sources and Evidence

# Domain Validation

# Remaining Uncertainty

# Acceptance Decision

# Responsible Person or Role

# Date and Version
```
