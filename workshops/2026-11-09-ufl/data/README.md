---
title: "Example Data (Uni for Life 2026)"
workshop: 2026-11-09-ufl
created: 2026-08-20
updated: 2026-11-04
language: en
authors: [Christopher Pollin]
generated-with: Claude Code (Claude Opus 5.5)
status: draft
related: [../profile.md]
---

# Example Data (Uni for Life 2026)

This folder holds the material for session 3, in which participants handle a customer request with the knowledge base they built in sessions 1 and 2, and the hook shown in session 2.

`kundenanfrage.txt` is a synthetic German e-mail from a fictional sales director of Northwind Traders. It asks for a workshop on agentic engineering and governance, slides, a small reference website and draft rules for AI use, and it carries the four Excel files as attachments. The mail deliberately contains personal data, such as remarks on colleagues' leave and retirement, a home address and a private phone number in the signature, so that participants practise copying only the parts a language model needs.

The four Excel files are converted from Microsoft's Northwind sample database, a fictional food wholesaler with orders from 1996 to 1998.

| File | Sheets |
| --- | --- |
| `bestellungen.xlsx` | Orders, Order Details |
| `produkte.xlsx` | Products, Categories, Suppliers |
| `kunden.xlsx` | Customers, Shippers |
| `mitarbeitende.xlsx` | Employees, with fictional birth dates, home addresses and home phone numbers |

The column names and values are unchanged from the source. Photos and picture blobs are dropped. `northwind_to_xlsx.py` reproduces the files from the source script:

```
python northwind_to_xlsx.py instnwnd.sql .
```

## Project-folder hook

`hooks/schutz.py` is a Claude Code `PreToolUse` hook that blocks `Edit` and `Write` calls whose target lies outside the project folder, including paths on another drive. Participants copy it to `.claude/hooks/schutz.py` in their project and register it in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "python .claude/hooks/schutz.py" }]
      }
    ]
  }
}
```

The hook covers file tools only. Shell commands run by the agent are outside its reach and remain governed by the permission mode.

## Provenance and licence

Source: `samples/databases/northwind-pubs/instnwnd.sql` in [microsoft/sql-server-samples](https://github.com/microsoft/sql-server-samples), retrieved 2026-11-03. The repository is licensed under the MIT License, Copyright (c) Microsoft Corporation, and its notice is retained in `LICENSE-northwind.txt`. All persons and companies in the data and in the mail are fictional.
