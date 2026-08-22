# Preparation Page (Draft)

Draft content for one Preparation subpage under `docs/`, the page that workshop subpages link to from their prerequisites block. Nothing here is decided and no file under `docs/` was touched. Sources are the two preparation decks of the museum workshop line and the standing setup page of the AI Coding Literacy site, the prerequisites block of the delivered ÖAW instance, the five workshop profiles in `workshops/`, `knowledge/drafts/google-artefacts.md`, `knowledge/drafts/page-copy.md` and `knowledge/design.md`, together with the author's research vault under `Teaching/Workshops/` and `Projects/VeTMedAI/`.

Two marking conventions follow `page-copy.md`. `[TBD: ...]` marks a fact that no source states, so a later pass either fills it from an operator answer or drops the sentence. A note beginning with "Inference" marks a claim derived from the sources rather than stated in them. Paste-ready text stands in blockquotes, everything outside a blockquote is a working note. Spelling is American, as in `page-copy.md`.

Access states in section 1 were verified on 2026-08-20 from an unauthenticated client, by requesting the PDF export endpoint of each deck, by following each Drive folder URL to its final address, and by requesting each web page and its data file. A redirect into `googleusercontent.com` means the file is readable by anyone with the link. Every readable artefact was identified by its document title rather than by the recorded link alone.

Link hygiene. No URL in this document carries an `ouid=` or `authuser=` parameter. The vault records the two preparation decks with a trailing `?usp=sharing`; this document keeps the canonical `/edit` form, which is the same target with the sharing hint removed. Nothing else needed cleaning, and the source forms are not reproduced here.

## 1. Inventory of existing preparation units

Three preparation surfaces exist, two of them taught live as their own session and one standing permanently on the web. All three are German, all three belong to the museum workshop line, and all three are publicly readable. The teaching line of this repository has no preparation surface of its own.

| Unit | Built for | Language | Date and format | URL | Access state |
| --- | --- | --- | --- | --- | --- |
| Preparation deck *Vorbereitungstreffen Programmieren 2.0: LLMs für Forschungsdaten im Museum 2026* | Programmieren 2.0, museum line, museum association of Austria | de | 2026-01-26, online session, 60 minutes | https://docs.google.com/presentation/d/1gvhQtVVRV7btvqd2b-YIPsRNQJk0umt6C8un3ONnnLY/edit | public, PDF export granted, title confirmed |
| Preparation deck *2026-04-13 1000 Vorbereitungstreffen Museumsbund NHM Wien (Promptotyping und Wissensmanagement mit LLMs)* | the double half-day workshop at the natural history museum, museum line | de | 2026-04-13, online briefing, 75 minutes | https://docs.google.com/presentation/d/1FI6EyAXHo0C4FKfftyyaM-PgVRQkCMQtYrHDqXJy_Nw/edit | public, PDF export granted, title confirmed |
| Standing setup page *Voraussetzungen & Setup* of the AI Coding Literacy site | Programmieren 2.0 and the AI Coding Literacy curriculum | de | permanent web page, no session | https://dhcraft.org/ai-coding-literacy/de/setup.html | public; the page renders from `data/content.json`, which is served publicly as well |
| Material folder *workshop-programmieren-2.0* on Drive | Programmieren 2.0 | de | permanent folder | https://drive.google.com/drive/folders/1m37hhcmlzqmB9evjgVvRK7_Dgu6JCobn | public folder, listing served without login, folder name confirmed |
| Preparation reading *llmdh* | Programmieren 2.0, named as `Vorbereitungslektüre` | de | permanent web page | https://chpollin.github.io/llmdh | public |
| Prerequisites block inside the ÖAW instance | ÖAW AI Winter School 2026, this teaching line | en, checklist in de | 2026-02-17, part of the taught material | recorded in the vault workshop document; the taught surfaces are the deck and the lecture notes listed in `google-artefacts.md` | the deck and notes are public; the checklist itself has no separate artefact |

### Scope of each unit

The preparation deck of 2026-01-26 holds twenty-one slides that take an audience without programming experience through the technical base once. It covers what LLM-assisted coding changes about the work, the tool landscape in three columns (chat interfaces, coding environment, coding agents), the four things that must be ready before the workshop, Visual Studio Code with its extensions, Python installation for Windows through the Microsoft Store and for macOS through python.org, the terminal with `python --version`, `cd` and `ls`, the four-step Python workflow, the three building blocks of a web page, Live Server and the reason a browser blocks local data, and a self-study exercise that runs one prepared script and edits its output in the browser. Claude Code appears only in the tool overview. The unit assumes chat access to a language model and does not install an agent.

The preparation deck of 2026-04-13 holds fourteen main slides plus an appendix that reuses the January deck as self-study material, and it is the unit that carries agentic setup. It covers the method framing, Obsidian as a local markdown vault, AI coding agents as a category with Claude Code as the harness used by the instructor, the same four-point readiness list as January, Visual Studio Code, Claude Code with both access routes and the platform-specific install commands, GitHub Desktop with the three terms repository, commit and push, Obsidian installation with vault creation and the warning against a cloud-synced folder, what participants bring to each of the two workshops, a seven-point next-steps list, and a three-step troubleshooting path. Its methodological point is stated in the vault: the tool slides are ordered so that participants derive their own preparation sequence from them, which is why the main part carries no separate checklist.

The standing setup page is a permanently maintained web surface with five setup items (Python, Visual Studio Code, LLM access, terminal, pip), each with a download link, tutorial links, a check command and notes; a quick-check list of five items; a first-script walkthrough with expected output; four troubleshooting entries covering PATH on Windows, `python3` against `python`, interpreter selection in Visual Studio Code and `python -m pip`; and a resource list for humanities audiences. The content lives in `data/content.json` of the public repository `DigitalHumanitiesCraft/ai-coding-literacy`, so the page is editable as data rather than as markup. It carries no Claude Code section.

The Drive folder holds the workshop data, the prepared scripts and a documentation template. The reading is an LLM-fundamentals site used as the conceptual entry ticket for Programmieren 2.0. Neither is a setup instruction, and both are listed because the museum line's preparation logic points at them.

The ÖAW prerequisites block is the only preparation material inside this teaching line. It lists terminal access, Node.js, `npm install -g @anthropic-ai/claude-code`, and an Anthropic API key or a Claude Pro subscription, and it marks all four as optional because participants could follow the demonstration instead. The install route it names is superseded by the native installer that the April deck uses, which is the clearest single piece of evidence for the maintenance rule in section 4.

## 2. Drafted page content

### 2.1 Lead

> Every workshop in this line works on a real machine. The preparation below makes sure the session can start at the first substantive prompt instead of at an installation, so bring a laptop you are allowed to install software on, a browser, and access to a frontier language model. Which of the following sections apply to you depends on the workshop you booked; the table at the end of this page states it per instance, and the workshop page you came from names its own level.

> Work through it in this order. Set up the accounts first, because an installed tool without an account gets you nowhere. Install second. Run the check third, and do it on the laptop you will actually bring.

Note. The commissioned section order puts the tools before the accounts, and the lead therefore states the working order separately. Both preparation decks put the readiness list before the tool slides for the same reason.

### 2.2 Claude Code

> Claude Code is a terminal-based coding agent from Anthropic. It reads and writes files in the folder you start it in, runs commands, searches the web, and takes instructions in ordinary language. The difference to the Claude web interface is that it works directly in your file system rather than through copy and paste.

> Claude Code is not part of the free Claude tier. You need either a paid plan or an API key with billing before the installation is of any use, so settle that first in section 2.5.

Steps.

> 1. Open a terminal. On Windows use PowerShell, on macOS or Linux use the Terminal app. If Visual Studio Code is already installed, its built-in terminal does the same job (Terminal, then New Terminal).
> 2. Run the install command for your system.
>    - macOS, Linux or Windows Subsystem for Linux: `curl -fsSL https://claude.ai/install.sh | bash`
>    - Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
>    - macOS with Homebrew: `brew install --cask claude-code`
>    - Windows with WinGet: `winget install Anthropic.ClaudeCode`
> 3. On Windows, install Git for Windows as well. Claude Code expects it.
> 4. Create an empty folder for the workshop somewhere you will find it again, without spaces or special characters in the path.
> 5. In the terminal, move into that folder with `cd` and the folder name, then type `claude` and press Enter. The login opens in your browser. Sign in with the account that holds your plan.
> 6. First run check. Ask it something harmless about the folder, for example to list the files it can see. An answer that names your folder means the installation, the login and the file access all work.

> The official installation page is the authority on all of this and is updated when the commands change: https://code.claude.com/docs/en/setup

Note. Steps 1 to 5 are taken from slide 11 of the 2026-04-13 deck, which carries all four install commands, the Git for Windows requirement and the browser login. Step 4 follows the vault reading of the same workshop, where the empty working folder is the starting point. Step 6 is `[TBD: what the page names as the first-run check; no source states one, and inventing a specific command or expected output here would be a guess]`.

Note. An older route through Node.js and `npm install -g @anthropic-ai/claude-code` appears in the ÖAW material of 2026-02 and is superseded by the native installer above. `[TBD: whether the page mentions the npm route at all]`. The recommendation is to leave it out, because a preparation page with two competing install routes produces support cases.

### 2.3 Visual Studio Code

> Visual Studio Code is a free code editor from Microsoft. It runs on Windows, macOS and Linux, it can be extended, and it has a terminal built in, which is where you will run things during the workshop.

Steps.

> 1. Download it from https://code.visualstudio.com and run the installer. On macOS, drag the app into the Applications folder.
> 2. Open the Extensions view with the icon in the left bar, or with `Ctrl+Shift+X` (`Cmd+Shift+X` on macOS).
> 3. Search for "Python" and install the extension published by Microsoft. Install "Pylance" the same way.
> 4. If your workshop builds a web page, install "Live Server" as well. It starts a small local web server, which a browser needs before it will let a page load data files from your own machine.
> 5. Open the built-in terminal through the menu, Terminal and then New Terminal. On Windows this is PowerShell, on macOS and Linux it is zsh or bash. For everything on this page the difference does not matter.

Note. Steps 1 to 3 and 5 come from the two preparation decks and the standing setup page, which agree on them. Step 4 is grounded twice, in the January deck's Live Server slide and in the KUG map demo recorded in the vault, which runs through Live Server or `python -m http.server` because the browser otherwise refuses to load the CSV.

### 2.4 Python

> You do not need to learn Python. You need it installed, because during the workshop the model writes scripts and you run them. What you actually do is run a file, read the message when it fails, and hand that message back to the model.

Steps.

> 1. Install Python. On Windows, open the Microsoft Store, search for Python and install the version published by the Python Software Foundation. On macOS and Linux, download it from https://www.python.org/downloads
> 2. If you install on Windows from python.org instead of the Store, tick "Add Python to PATH" on the first installer screen. Skipping it is the single most common reason the workshop machine later reports that `python` is not recognized.
> 3. Check it. In the terminal, type `python --version`. A version number as the answer means it works. On macOS, try `python3 --version` if `python` produces nothing.
> 4. Tell the editor which Python to use. In Visual Studio Code press `Ctrl+Shift+P`, type "Python: Select Interpreter", and choose the version you just installed.
> 5. Run one script before you arrive. Create a file called `test.py` in your workshop folder, put one line in it, for example `print("ready")`, save with `Ctrl+S`, and run `python test.py` in the terminal. Seeing your own word printed back is the whole test.
> 6. When a script asks for something you do not have, the terminal says `ModuleNotFoundError`. The fix is one command, for example `pip install pandas`. Nothing needs to be installed in advance.

Note. Steps 1 to 6 are grounded in the April deck (Microsoft Store route, Python extension), the standing setup page (check commands, interpreter selection, the `python3` and PATH troubleshooting entries, the first-script walkthrough) and the ÖAW lecture notes, which name `ModuleNotFoundError` and the `pip install` fix as the typical failure of that step.

Note. `[TBD: which Python version the page names]`. The museum-line source of 2026-04 names 3.12 and advises against 3.13, which was current advice at that date and is exactly the kind of statement section 4 says a preparation page should not freeze. The recommendation is to name no version and let the Store or python.org default stand.

### 2.5 Accounts and access

> Claude account. Create it at https://claude.com. For workshops that only use the chat interface the free tier is enough. For workshops that run Claude Code you need a paid plan (Pro or Max), and the usage limit is shared between Claude and Claude Code. The alternative is an account at https://console.anthropic.com with a payment method and an API key, which bills per use instead of per month. Current prices are on https://claude.com/pricing
> If you prefer a different provider, the concepts transfer and you can follow everything in the chat-based parts with the model of your choice. The agentic parts assume Claude Code.

> Google account. Some instances keep their material in a Drive folder, and some hands-on units run in Google Colab, which is a Python environment in the browser. If your workshop page links either, sign in once beforehand and confirm you can open the link.

> GitHub account. Not required to download workshop material, because public repositories download without an account. You need one only if your workshop puts your own work under version control, in which case install GitHub Desktop from https://desktop.github.com and connect it to your account.

Note. The paid-plan requirement, the shared limit and the two access routes come from slide 11 of the April deck. No amount is reproduced here, per the repository rule; the pricing link carries the current figure. The recommendation in the source to work with Sonnet by default on the API route is a cost argument that ages with the model lineup, so it is left out.

Note. Colab is grounded in the ÖAW hands-on, which has participants copy a notebook into their own Drive. Drive folders as material carriers are grounded in `google-artefacts.md`, which records the KUG and Uni for Life folders as login-gated.

Note. `[TBD: whether any registered instance actually requires an API key rather than a plan]`, and `[TBD: whether participants bring their own data]`. The museum line asked for a dataset and a one-page concept; none of the five profiles in `workshops/` states a data requirement.

### 2.6 Final check before you arrive

> Do this on the laptop you are bringing, not on a second machine.
> 1. `python --version` in the terminal answers with a version number.
> 2. Visual Studio Code opens, and the Python extension is listed as installed.
> 3. You ran `test.py` once and saw its output.
> 4. You can sign in to your model account in the browser.
> 5. For agentic workshops, `claude` starts in your workshop folder and has completed its browser login once.
> 6. The workshop folder exists, and you know its path.

Note. Modeled on the quick-check list of the standing setup page and the next-steps list of the April deck, reduced to the items every level shares plus one agentic item.

### 2.7 If something breaks

> 1. Read the error message. It usually names the problem, and often the fix.
> 2. Paste the error message into a language model and ask what it means. You will work the same way during the workshop.
> 3. If it still fails, write to the contact address on your workshop page, with one sentence on what you tried, the error message, and a screenshot.

Note. All three steps are in the source material, in the April deck's closing slide and in the troubleshooting section of the Programmieren 2.0 documentation. `[TBD: which contact address the platform prints]`. The recommendation is to point at the workshop page instead of hard-coding an address on the preparation page, so one edit covers all instances.

## 3. Applicability per workshop

Three levels keep the page short enough that a participant reads only their own row.

- Level 1, browser only. Model access in a browser. Nothing is installed.
- Level 2, editor and Python. Level 1 plus Visual Studio Code, Python, the terminal, and a local server where a browser prototype is built.
- Level 3, harness. Level 2 plus Claude Code and a paid plan, plus a working folder the agent operates in.

| Workshop | Level | Basis |
| --- | --- | --- |
| KUG/M3GIM 2026-09-16/17 | 1, with 2 conditional | Stated. The register describes an audience without an LLM or programming background, and the first hands-on in the vault material says explicitly that the chat interface suffices and nothing is installed. Inference for the conditional part: the map demo runs through Live Server or `python -m http.server`, and whether participants run it themselves or watch it is not fixed. |
| CLARIAH-AT 2026-09-25 | 1, with 3 conditional | Inference. The profile and `page-copy.md` record that no artifact states prerequisites. Both hands-on units need access to a multimodal frontier model, which `page-copy.md` already marks as an inference. The executable hands-on package lives in an external repository, so anyone running it locally lands at level 3. |
| Uni for Life 2026-11-09/10 | 3 | Stated. The vault workshop document lists installation and setup of Claude Code, terminal work and permissions as content of day one, so participants operate a harness. |
| VetMed Winter School 2026-11-30 to 12-04 | 3 | Stated. The vault concept builds the first two days on the Programmieren 2.0 preparation pattern with Visual Studio Code, Python, terminal and Live Server, then moves through an AI harness and local models to an own project. |
| ÖAW AI Winter School 2026-02-17 (delivered) | 1, with 3 optional | Stated in its own prerequisites block, which marks the agentic setup as optional and offers following the demonstration instead. Historical record; the instance is taught. |
| VetMedAI workshop 1 2026-04-22 (delivered) | 1 | Inference from the profile module mapping. The instance is chat-based throughout, with the participant exercise in the governance block, and agentic engineering appears as a short closing definition without a harness demonstration. |

Note. Two of the four planned instances have their level from a source that is not in this repository, meaning the vault workshop documents. A sync pass should either confirm the level with the operator or restate it in the profile, because a preparation page that contradicts a profile is worse than one that says nothing.

Note. `[TBD: whether the page shows all six rows or only the future four]`. The delivered instances have their preparation in the past, and their rows serve the reader of the archive rather than a participant.

## 4. Maintenance

Install instructions age faster than any other content on the platform, and the material already carries proof. Between February and April 2026 the Claude Code installation moved from a Node.js and npm route to a native installer with four platform variants, and the documentation address named in the older material now redirects to a different host. A Python version recommended in April is a recommendation with a shelf life. Three rules follow.

1. The page carries one "last verified" date at the top, and that date is the only thing a maintenance pass has to move when nothing else changed. Proposed initial value 2026-08-20, the date of the source check behind this draft.
2. Every tool section ends at its official installation page rather than reproducing it. The four addresses are https://code.claude.com/docs/en/setup, https://code.visualstudio.com, https://www.python.org/downloads and https://desktop.github.com. All four resolved on 2026-08-20.
3. No version numbers in prose, no prices, no model names as a current recommendation. Prices live behind the pricing link, versions live behind the download link, and the model lineup changes on a schedule nobody on this page controls.

Four things stay on the page in full detail because they have survived every revision of the museum-line material so far, the order of work, the check commands, the first-run test and the troubleshooting path.
