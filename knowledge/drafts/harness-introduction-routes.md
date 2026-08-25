---
title: AI Harness Introduction Routes
status: draft
created: 2026-08-25
updated: 2026-08-25
language: en
related: [module-hub-architecture.md, claude-code-agentic-engineering-subchapter.md, curated-agent-skills-library.md]
---

# AI Harness Introduction Routes

Content and route contract for three product-specific introductions beneath Module 04. The shared teaching object is the AI Harness as the environment that connects a model with project files, instructions, tools, permissions, execution feedback and persistent state.

## Relation to Module 00

AI Coding Literacy belongs to Module 00. It develops the human capability to describe a task, inspect files and outputs, read errors, control permissions and verify a result. It therefore uses a neutral workspace-and-verification symbol.

The product introductions belong to Module 04. They show how the same capabilities are realised in different harnesses. Claude Code, Codex and Pi are sibling routes. None defines the general AI Coding Literacy curriculum.

## Shared tutorial sequence

Every harness introduction uses the same learning sequence so that readers can compare products without treating their interfaces as equivalent.

1. State the learning goal and identify the harness, its execution surface and its maintained primary source.
2. Check the prerequisites, including the workspace, Git state and required account or local model service.
3. Install or open the harness through the current official route and verify its version.
4. Start it in one bounded workspace and identify the active model or provider.
5. Read the repository instruction layer and identify its scope.
6. Inspect tools, permissions and safety boundaries before allowing changes.
7. Locate Skills, external connections and parallel-work mechanisms where the product supports them.
8. Run one reversible read-only task, inspect the result and confirm with `git status --short` that the workspace is unchanged.

Product-specific commands remain linked to current primary documentation and carry a last-checked date. The conceptual sequence stays stable when a command or interface changes.

## Claude Code

- Public route: `docs/tutorials/claude-code.html` and `docs/tutorials/claude-code.de.html`.
- Status: available.
- Teaching emphasis: terminal and editor integration, `CLAUDE.md`, context management, plan and execution modes, Skills, Model Context Protocol connections, Subagents and delegated work.
- Project instructions: `CLAUDE.md` or `.claude/CLAUDE.md`, with personal additions in `CLAUDE.local.md` where appropriate.
- Safety boundary: permissions and operating-system sandboxing are separate controls. The first exercise starts explicitly with `claude --permission-mode plan`.
- Extensions: Skills, Model Context Protocol connections, plugins and Subagents are built-in concepts; isolated parallel changes can use worktrees.
- First check: inspect one workspace, name the instruction sources and existing checks, then confirm outside the harness with `git status --short` that no file changed.
- Primary sources checked 2026-08-25: [Quickstart](https://code.claude.com/docs/en/quickstart), [permission modes](https://code.claude.com/docs/en/permission-modes), [memory and project instructions](https://code.claude.com/docs/en/memory), [Subagents](https://code.claude.com/docs/en/sub-agents).

## Codex

- Public route: `docs/tutorials/codex.html` and `docs/tutorials/codex.de.html`.
- Status: to be implemented from current official OpenAI documentation and the maintained OpenAI Academy bootcamp source.
- Teaching emphasis: local and app workspaces, repository instructions, tool-mediated changes, permissions, Skills, Model Context Protocol connections, Subagents, browser-supported verification and inspectable diffs.
- Project instructions: hierarchical `AGENTS.md` files are combined from the repository root towards the current working directory; `/init` creates a starting file.
- Safety boundary: sandbox and approval policy are separate controls. The first exercise starts explicitly with `codex --sandbox read-only` and inspects the current state with `/permissions`.
- Extensions: Skills, Model Context Protocol connections, Subagents and worktrees are maintained product concepts.
- Local models: the open-source CLI exposes version-sensitive OSS-provider routes for Ollama and LM Studio. They are an optional extension of the Codex route, not its default prerequisite.
- First check: inspect one workspace, name the applicable instructions and existing checks, then confirm outside the harness with `git status --short` that no file changed.
- Primary sources checked 2026-08-25: [Codex CLI](https://developers.openai.com/codex/cli/), [`AGENTS.md`](https://developers.openai.com/codex/guides/agents-md/), [Skills](https://developers.openai.com/codex/skills/), [MCP](https://developers.openai.com/codex/mcp/), [Subagents](https://developers.openai.com/codex/subagents/), [worktrees](https://developers.openai.com/codex/app/worktrees/) and [Codex bootcamp 101](https://academy.openai.com/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31).

## Pi with a local model

- Public route: `docs/tutorials/pi.html` and `docs/tutorials/pi.de.html`.
- Status: to be implemented from the official Pi repository and maintained documentation.
- Teaching emphasis: an inspectable MIT-licensed harness, explicit model-provider configuration, local-model connection, extensions and Skills, and the relation between a small harness core and user-controlled adaptation.
- Installation reference: `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`; the package and repository namespace are checked immediately before publication because both changed during 2026.
- Project instructions: Pi reads hierarchical `AGENTS.md` files and can also read `CLAUDE.md`; an `AGENTS.override.md` can replace the file on the same level.
- Safety boundary: Pi runs with the operating-system rights of the user who starts it. Project trust controls the loading of project resources; it is not a sandbox and does not restrict tool actions.
- Product boundary: Pi intentionally omits built-in permission prompts, Plan Mode, MCP and Subagents. Those capabilities require tool allowlists, containers, extensions, packages or separate processes.
- Local model reference: Pi documents a local llama.cpp router bound to `127.0.0.1` and GGUF models; Ollama provides an additional integration route. Model licence, hardware requirements, context length and tool-calling quality are assessed separately.
- First check: start with `pi --tools read,grep,find,ls -p "Summarize this repository and explain how its checks are run."`, then confirm outside the harness with `git status --short` that no file changed.
- Primary sources checked 2026-08-25: [Pi documentation](https://pi.dev/docs/latest), [usage and product boundaries](https://pi.dev/docs/latest/usage), [security](https://pi.dev/docs/latest/security), [official repository](https://github.com/earendil-works/pi), [llama.cpp integration](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/llama-cpp.md) and [Ollama integration](https://docs.ollama.com/integrations/pi).

The page must distinguish an open-source harness from the model that it calls. Local execution of the harness does not by itself establish that model inference stays on the local machine.

## Comparative learning outcome

The three routes use the same success definition: the learner can start the harness in a bounded repository, identify the applicable project instructions, explain the active tool and permission boundary, complete a read-only orientation task and demonstrate that the Git working tree stayed unchanged. Product-specific commands remain secondary to this observable capability.

Screenshots support orientation but do not carry volatile commands or security claims. Installation commands, package names, permission labels and provider integrations are maintained as dated source-backed text.

## Route presentation

The landing-page learning-routes section uses three groups.

- Foundation contains AI Coding Literacy.
- AI Harness introductions contains Claude Code, Codex and Pi with a local model.
- Research workflow contains Research Data and Knowledge Work.

Each route has a distinct, original line icon. Product names remain text labels. The interface does not reproduce third-party logos or imply endorsement.

## Acceptance boundary

The common tutorial component is accepted once. Product pages receive separate source and function checks because installation commands, supported extensions and permission models can change independently. The Research Director assesses the didactic comparison and the accuracy of the Pi local-model boundary.
