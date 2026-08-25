---
title: Harness Route Icon System
project:
  name: knowledge-context-agentic-engineering
  repository: https://github.com/DigitalHumanitiesCraft/knowledge-context-agentic-engineering
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: proposal
created: 2026-08-25
updated: 2026-08-25
language: en
related: [../design.md, module-icon-system.md, module-hub-architecture.md]
---

# Harness Route Icon System

This proposal defines four portable line icons for learning routes concerned with coding literacy and AI harnesses. The assets distinguish routes within the existing platform without extending the five-colour module taxonomy. Their geometry is original and brand-neutral. A route name remains the semantic and accessible source.

## Shared construction

- Every asset declares a 48 by 48 view box and the same 48 pixel intrinsic size.
- A two-unit `currentColor` contour with round caps and joins continues the module-icon grammar.
- The live drawing stays within a four-unit outer margin and remains legible at 24 to 32 pixels.
- The files contain no text element, font, raster image, script, external reference or embedded style block.
- The geometric `C` and pi forms are large route identifiers constructed from paths. They are neither font glyphs nor copied product marks.
- Each root SVG is decorative through `aria-hidden="true"` and `focusable="false"`. The surrounding route label supplies meaning and interaction state.

## Semantic matrix

| Route | Asset | Primary object | Didactic meaning |
| --- | --- | --- | --- |
| AI Coding Literacy | `ai-coding-literacy.svg` | Workspace divided into file rail, visible result and terminal | Coding literacy joins project orientation, an executable command and inspection of an observable result. The outlined circle marks the result to inspect and is not a decorative approval mark. |
| Claude Code | `claude-code.svg` | Port-bearing terminal harness with an open `C` contour | Claude Code is presented as a terminal-based harness that receives project context and connects to tools. The `C` distinguishes the route without reproducing a product logo. |
| Codex | `codex.svg` | Patch document beside a returning execution path | Codex applies an inspectable diff and continues through execution and re-checking. Added and removed rows make the patch explicit; the returning arrows encode the working loop. |
| Pi local | `pi-local.svg` | Local computer containing a pi contour and one connected model node | Pi is shown as a local harness surface whose model connection remains inside the user's computer boundary. The single node identifies the model endpoint without turning the icon into a generic network. |

## Accessible use

When an icon sits beside a visible route name, an HTML image reference uses `alt=""`; an inline SVG retains the supplied hidden and unfocusable attributes. The visible route name provides the accessible name of its link or section.

An icon-only control requires a language-matched accessible name on the enclosing interactive element, such as `aria-label="Open the Codex learning route"`, together with a visible tooltip or visually hidden text. The SVG itself remains hidden from assistive technology, so its constructed `C` or pi contour is never announced as a letter or mathematical expression. Focus, availability and external-destination status belong to the enclosing HTML and cannot be communicated by icon colour alone.

External SVG files loaded through `img` do not inherit the host element's CSS colour. A coloured implementation therefore uses an inline copy or the platform's existing mask technique. In both cases `currentColor` allows one asset to follow the route component's neutral or contextual colour without producing asset variants.

## Acceptance checks

The package is structurally ready when all four files parse as XML, expose `viewBox="0 0 48 48"`, declare 48 pixel intrinsic dimensions, use `currentColor`, contain no raster or text elements and preserve the shared stroke grammar. Visual acceptance requires inspection at 48, 32 and 24 pixels. The text label remains required at every public route location.
