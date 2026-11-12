# Local workflows

Three pipelines that run on one's own computer without a cloud service. An agent builds each pipeline, a local tool or open model does the work, a fixed script checks the result, and a person releases it. They belong to the teaching on open models and own pipelines in module 04 Agentic Engineering and were built and measured on 2026-11-05 for the Uni for Life workshop of 9 and 10 November 2026. Each folder is also an installable skill: its `SKILL.md` explains what the pipeline does and what it would install before anything is set up.

| Folder | Pipeline |
| --- | --- |
| [`mail-anonymisieren/`](mail-anonymisieren/README.md) | Redacts a mail with an Excel attachment before a cloud agent sees it, with rules, a local LLM and a check script |
| [`pdf-zu-markdown/`](pdf-zu-markdown/README.md) | Converts PDF, DOCX and scans to Markdown with Docling and checks the result against a known test document |
| [`sprache-zu-text/`](sprache-zu-text/README.md) | Transcribes a recording with faster-whisper, summarises it through Ollama and measures the word error rate |

The folder and skill names and the READMEs are German, because the workflows were written for a German-speaking workshop.

## Test data

`data/` holds the test input of the mail redaction, the synthetic customer mail `kundenanfrage.txt` and the employee table `mitarbeitende.xlsx`. The table is converted from Microsoft's Northwind sample database, `samples/databases/northwind-pubs/instnwnd.sql` in [microsoft/sql-server-samples](https://github.com/microsoft/sql-server-samples), retrieved 2026-11-03, under the MIT License, whose notice is kept in `data/LICENSE-northwind.txt`. All persons and companies in the mail and the table are fictional. The conversion script and the other three Northwind tables stay with the workshop material for which they were made.

One's own mails, recordings and documents are never placed in this folder. Each `SKILL.md` describes in its section Eigene Daten how to run a pipeline on them in one's own terminal and outside the repository.
