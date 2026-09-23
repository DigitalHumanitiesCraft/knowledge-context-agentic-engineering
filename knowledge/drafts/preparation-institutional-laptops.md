# Preparation on Institutional Laptops (Draft)

Draft additions to `docs/preparation.html` and `docs/preparation.de.html`. Nothing here is decided and no file under `docs/` was touched. The draft was written for Christian Steiner on 2026-09-23 because an upcoming hackathon for early-career researchers from several European research and technology organizations raised four questions the current Preparation page does not answer: how to install without administrator rights, which harness works with an organizational Mistral licence, which routes cost nothing, and how far each harness stays inside the practice folder.

Conventions follow `preparation-page.md`: paste-ready text stands in blockquotes, English first and German second; `[TBD: ...]` marks a fact no checked source states; spelling is American. No amounts appear, per the repository rule; access routes name plan types and link the pricing page.

**Verification.** Every product claim below was checked on 2026-09-23 by fetching the page source over HTTP and matching the quoted sentence verbatim, not through a summarizing tool. Section 4 lists each source with the sentence it carries. One statement that a research pass had attributed to OpenAI, that Codex in `workspace-write` reads files anywhere, is not in the checked source and is therefore left out.

## 1. What the current page covers and what it lacks

The page already carries the load-bearing idea: a disposable `ai-workspace` folder, "Keep confidential and irreplaceable files outside the practice folder", Manual or Plan mode for the first harness conversation, and a read-only first check. It names Claude Code, Codex, Pi and OpenCode, and it notes the move from Gemini CLI to Antigravity CLI.

A search of `docs/preparation.html` on 2026-09-23 found no occurrence of `administrator`, `admin rights`, `Mistral`, `subscription` or `licen`, and one of `Antigravity` (the Gemini CLI notice). Four additions follow from that.

| Addition | Where on the page | Section |
| --- | --- | --- |
| Installing without administrator rights | "Before you begin", as a third paragraph after "Only when selected" | 2.1 |
| Mistral Vibe as a harness option | Step 5 card list, and a new Option D after Option C | 2.2 |
| Access routes without amounts | Step 5, directly after the card list | 2.3 |
| How far each harness stays in the folder | Step 5, after the access routes, before Option A | 2.4 |

## 2. Drafted page content

### 2.1 Installing without administrator rights

> **On an institutional laptop.** Many organizations do not grant administrator rights. The core path still works, because every tool it needs offers an installation for your own user account. Choose that variant where one exists. If your IT policy forbids installing software at all, even for your own account, clarify this before the session; you can then work on the browser path and pair with someone whose laptop runs a harness.
>
> - Visual Studio Code: choose the **User setup**. It installs under your own profile and needs no administrator permission.
> - Python on Windows: use the **Python install manager** from python.org or the Microsoft Store. It installs Python for your user account only.
> - Claude Code: the native installer runs without administrator rights. Git for Windows is optional.
> - Antigravity CLI: the installer places `agy` in your own user directory.
> - Git on Windows, only when selected: if the standard installer asks for administrator rights, use the **Portable** edition from the same download page.

> **Auf einem Dienstlaptop.** Viele Einrichtungen vergeben keine Administratorrechte. Der Kernpfad funktioniert trotzdem, denn jedes Werkzeug darin lässt sich für das eigene Benutzerkonto installieren. Wähle diese Variante, wo es sie gibt. Verbietet deine IT jede Installation, auch im eigenen Konto, kläre das vor dem Termin; du arbeitest dann im Browserpfad und schließt dich jemandem an, auf dessen Laptop ein Harness läuft.
>
> - Visual Studio Code: das **User Setup** wählen. Es installiert ins eigene Profil und braucht keine Administratorrechte.
> - Python unter Windows: den **Python install manager** von python.org oder aus dem Microsoft Store verwenden. Er installiert Python nur für das eigene Benutzerkonto.
> - Claude Code: der native Installer läuft ohne Administratorrechte. Git for Windows ist optional.
> - Antigravity CLI: der Installer legt `agy` im eigenen Benutzerverzeichnis ab.
> - Git unter Windows, nur wenn gewählt: verlangt der normale Installer Administratorrechte, die **Portable**-Ausgabe von derselben Downloadseite nehmen.

Note. Each bullet is carried by a checked sentence in section 4. `[TBD: macOS]`. No checked source states whether Visual Studio Code, Python from python.org or `xcode-select --install` need administrator rights on macOS. The draft therefore makes no macOS claim; an operator test on a standard macOS account would settle it.

Note. `[TBD: Git for Windows]`. The installer script declares that it can run without elevation, but its default target is Program Files and no Git for Windows documentation describes a non-administrator install. The Portable route is offered on the official download page; that it avoids elevation is an inference from its form, not a documented statement.

Note. The advice to clarify IT policy first comes from the planning conversation of 2026-09-23, where participants from several organizations reported that installation often needs pre-approval. It is not a product claim.

### 2.2 Mistral Vibe as Option D

Card for the Step 5 list, in the form of the existing cards:

> **Mistral · open CLI**
> **Mistral Vibe** VS Code extension and open-source terminal harness. Mistral plan or Mistral API key. Documentation · Setup step

> **Mistral · offene CLI**
> **Mistral Vibe** VS-Code-Erweiterung und quelloffenes Terminal-Harness. Mistral-Plan oder Mistral-API-Key. Dokumentation · Setup-Schritt

Note. The label follows the Codex card ("OpenAI · open CLI"). The CLI repository `mistralai/mistral-vibe` carries the Apache-2.0 licence (GitHub API, 2026-09-23); the licence of the extension was not checked.

Option D, after Option C:

> **Option D · Start Mistral Vibe in Visual Studio Code**
> Use this route if your organization provides a Mistral licence. Install the Mistral Vibe extension from the publisher Mistral AI; it requires Visual Studio Code 1.94 or later. Sign in with your Mistral plan or add an API key you manage yourself, as the extension's setup describes. Send the same read-only request: List the files in this folder. Do not create, edit, move or delete anything, and do not run commands. For the terminal interface, follow the official CLI installation page; on macOS and Linux it offers a one-line installer, and a manual route uses `uv tool install mistral-vibe` with Python 3.12 or later. Mistral states that Vibe works on Windows but officially targets UNIX environments.
> Check: Mistral Vibe names the practice files without changing them.

> **Option D · Mistral Vibe in Visual Studio Code starten**
> Diesen Weg nehmen, wenn deine Einrichtung eine Mistral-Lizenz stellt. Die Erweiterung Mistral Vibe vom Herausgeber Mistral AI installieren; sie verlangt Visual Studio Code 1.94 oder neuer. Mit dem Mistral-Plan anmelden oder einen selbst verwalteten API-Key eintragen, wie es die Einrichtung der Erweiterung beschreibt. Dieselbe Leseanfrage schicken: List the files in this folder. Do not create, edit, move or delete anything, and do not run commands. Für die Terminal-Oberfläche der offiziellen Installationsseite folgen; unter macOS und Linux gibt es einen Einzeiler, der manuelle Weg ist `uv tool install mistral-vibe` mit Python 3.12 oder neuer. Mistral schreibt, dass Vibe unter Windows läuft, offiziell aber auf UNIX-Umgebungen ausgerichtet ist.
> Prüfen: Mistral Vibe nennt die Übungsdateien, ohne sie zu ändern.

Note. `[TBD: publisher string]`. The checked install page names the extension and its prerequisites; the exact publisher label shown in the Extensions view was not checked. Before publication, confirm it in Visual Studio Code, as Option A does for Anthropic.

Note. Whether Mistral Vibe becomes a full Option D with its own tutorial, or a documentation card like OpenCode, is an operator decision. The draft proposes Option D because organizational Mistral licences are the concrete case that triggered it; a full tutorial in `docs/tutorials/` would follow the shared eight-step order and is not drafted here.

### 2.3 Access routes

To follow the card list in Step 5. Plan names only, no amounts; the pricing link carries the figure.

> **Access routes.** A harness needs model access. Check first whether your organization already provides one; an organizational licence usually decides the route.
>
> | Harness | Free route | Paid or organizational route |
> | --- | --- | --- |
> | Claude Code | none; the free Claude plan does not include Claude Code | Pro, Max, Team, Enterprise or Console account, or a supported cloud provider |
> | Codex | included in the ChatGPT Free plan | further ChatGPT plans, business and education plans |
> | Mistral Vibe | limited coding sessions in the free plan | Mistral plans, or an API key |
> | Antigravity | free individual plan with rate limits | [TBD: paid plan names] |
>
> Free routes are limited and change often. For a full day of agentic work, a paid or organizational route is considerably more reliable.

> **Zugangswege.** Ein Harness braucht Modellzugang. Prüfe zuerst, ob deine Einrichtung schon einen stellt; eine Lizenz der Einrichtung entscheidet meist den Weg.
>
> | Harness | Kostenloser Weg | Bezahlter Weg oder Weg über die Einrichtung |
> | --- | --- | --- |
> | Claude Code | keiner; der kostenlose Claude-Plan enthält Claude Code nicht | Pro, Max, Team, Enterprise oder Console, oder ein unterstützter Cloud-Anbieter |
> | Codex | im ChatGPT-Free-Plan enthalten | weitere ChatGPT-Pläne, Business- und Education-Pläne |
> | Mistral Vibe | begrenzte Coding-Sessions im kostenlosen Plan | Mistral-Pläne oder API-Key |
> | Antigravity | kostenloser Einzelplan mit Nutzungsgrenzen | [TBD: Namen der bezahlten Pläne] |
>
> Kostenlose Wege sind begrenzt und ändern sich oft. Für einen ganzen Tag agentischer Arbeit ist ein bezahlter Weg oder einer über die Einrichtung deutlich verlässlicher.

Note. The Antigravity row rests on the research pass, which read `antigravity.google/pricing` through a summarizing tool; it was not re-checked verbatim and stays marked until it is. The closing sentence on reliability is the planning conversation's experience, not a product claim.

Note. GitHub Copilot is left out. Two reads of its plan documentation disagreed on whether the free plan includes agent mode, and the question was not settled.

### 2.4 How far a harness stays in the folder

> **The folder boundary.** Each harness decides differently what it may read and change outside `ai-workspace`, and the boundary is weakest for terminal commands on Windows. The disposable folder therefore remains the actual protection: keep confidential data off the practice folder and start with a mode that asks before every change.
>
> - Claude Code works in the folder you start it in. Further folders need `--add-dir`, and reads outside can be blocked in the settings. Its sandbox for commands runs on macOS, Linux and WSL2, not on native Windows.
> - Codex in its default local mode edits within the workspace and asks before going beyond it.
> - The built-in agent tools of Visual Studio Code read and write only in the open workspace, but terminal commands run with your user privileges.
> - Antigravity limits the agent to your project folders by default.
> - Mistral Vibe asks before reading or writing outside its working directory.

> **Die Ordnergrenze.** Jedes Harness regelt anders, was es außerhalb von `ai-workspace` lesen und ändern darf, und am schwächsten ist die Grenze bei Terminalbefehlen unter Windows. Der eigentliche Schutz bleibt deshalb der Übungsordner: keine vertraulichen Daten hinein, und mit einem Modus beginnen, der vor jeder Änderung fragt.
>
> - Claude Code arbeitet in dem Ordner, in dem es gestartet wird. Weitere Ordner brauchen `--add-dir`, Lesezugriffe außerhalb lassen sich in den Einstellungen sperren. Seine Sandbox für Befehle läuft unter macOS, Linux und WSL2, nicht unter nativem Windows.
> - Codex bearbeitet im lokalen Standardmodus nur den Workspace und fragt, bevor es darüber hinausgeht.
> - Die eingebauten Agentenwerkzeuge von Visual Studio Code lesen und schreiben nur im geöffneten Workspace, Terminalbefehle laufen aber mit deinen Benutzerrechten.
> - Antigravity beschränkt den Agenten standardmäßig auf die Projektordner.
> - Mistral Vibe fragt, bevor es außerhalb seines Arbeitsverzeichnisses liest oder schreibt.

Note. The Mistral Vibe bullet is an inference: the checked README says reads and writes in directories added with `--add-dir` "don't require the \"outside workdir\" prompt", which implies that prompt for everything else, but the prompt itself was not observed.

Note. The Visual Studio Code bullet concerns its built-in agent tools, which is the surface GitHub Copilot uses in Visual Studio Code; it is kept although Copilot is not an option, because participants may meet it on managed machines.

## 3. Open points for the operator

1. Whether the four additions enter the public page, and in which form.
2. Mistral Vibe as Option D or as a documentation card (2.2).
3. macOS without administrator rights, to be tested on a standard account (2.1).
4. Git for Windows without administrator rights (2.1).
5. Antigravity paid plan names and a verbatim check of its pricing page (2.3).
6. The `Last verified` date on the page, if the additions are installed.

## 4. Sources

All checked on 2026-09-23 by HTTP fetch of the page source and verbatim match.

| Claim | Source | Sentence found |
| --- | --- | --- |
| VS Code user setup without admin | https://code.visualstudio.com/docs/setup/windows | "This setup does not require administrator permissions. It installs under %LOCALAPPDATA%\Programs\Microsoft VS Code" |
| Python install manager per user | https://docs.python.org/3/using/windows.html | "The Python install manager does not support installing runtimes per-machine." and "are all per-user only" |
| Classic Python installer deprecated | same | "This installer is deprecated since 3.14 and will not be produced for Python 3.16 or later." |
| Claude Code without admin | https://code.claude.com/docs/en/setup | "You do not need to run as Administrator. Installing Git for Windows is optional." |
| Claude Code plans | same | "Claude Code requires a Pro, Max, Team, Enterprise, or Console account. The free claude.ai plan does not include Claude Code access." |
| Claude Code working directory | https://code.claude.com/docs/en/permissions | "By default, Claude has access to files in the directory where you launched it." |
| Claude Code outside reads | same | `permissions.blockReadsOutsideWorkingDirectories` |
| Claude Code sandbox platforms | https://code.claude.com/docs/en/sandboxing | "The sandbox is built into Claude Code and runs on macOS, Linux, and WSL2. Native Windows is not supported." |
| Antigravity CLI user directory | https://antigravity.google/docs/cli/install | "The installation script registers the agy binary to your local user directory: C:\Users\<username>\AppData\Local\agy\bin" |
| Antigravity folder default | https://antigravity.google/docs/agent-settings | "By default, the agent only has access to the folders inside your Project and the application's local app data directory" |
| Git Portable | https://git-scm.com/install/windows | "Portable ("thumbdrive edition")" |
| Mistral Vibe CLI | https://docs.mistral.ai/vibe/code/cli/install-setup | "Python 3.12 or later for manual installation." and `uv tool install mistral-vibe` |
| Mistral Vibe on Windows | https://github.com/mistralai/mistral-vibe | "Mistral Vibe works on Windows, but we officially support and target UNIX environments." |
| Mistral Vibe folder boundary | same | reads and writes in added directories "don't require the \"outside workdir\" prompt" |
| Mistral Vibe extension | https://docs.mistral.ai/vibe/code/vs-code-extension/install-authenticate | "VS Code Version 1.94.0 or later." and "A Mistral plan or an API key you manage yourself." |
| Mistral free plan | https://mistral.ai/pricing | "Limited coding sessions." |
| Codex default sandbox | https://developers.openai.com/codex/concepts/sandboxing (redirects to learn.chatgpt.com) | "workspace-write: The agent can read files, edit within the workspace, and run routine local commands inside that boundary. This is the default low-friction mode for local work." |
| Codex boundary | same | "It asks before using the internet or going beyond the workspace boundary." |
| Codex plans | https://developers.openai.com/codex/pricing (redirects to learn.chatgpt.com) | "ChatGPT Work and Codex are included in your ChatGPT Free, Go, Plus, Pro, Business, Edu, or Enterprise plan" |
| VS Code agent tools | https://code.visualstudio.com/docs/agents/security (redirects to /docs/agents/run/security) | "Built-in agent tools can only read and write files within the current workspace folder." and "The agent can execute terminal commands and shell scripts with your user privileges" |
