---
name: qp-setup
description: Configure a coding-agent baseline through communication instructions and companion-tool choices. Focus on preserving existing instructions, safe managed-block changes, approved setup, and supported integrations.
---

# QP Setup

Guide one coding-agent baseline setup: configure communication instructions, then help choose companion tools and supported integrations when requested.

Use QP Setup when the user requests a coding-agent baseline that includes communication instructions and companion-tool choices or supported integrations. An explicit instruction-only request remains in scope, but end after the instruction result unless the user also asks to continue with companion tools. Do not use QP Setup for standalone named-tool, MCP, plugin, or integration setup. For a standalone named tool, use its explicit owner when one exists; otherwise state that no QP owner is available.

Apply the communication behavior in the managed block below to live setup updates. Keep the exact target, authority, action, and result in text.

## 1. Select the instruction scope

Use a global or repository instruction scope that the user already selected explicitly. Otherwise, ask:

> Where should I configure the communication instructions: globally or in this repository?

Do not select repository scope from the current working directory. Treat global and repository targets as separate actions when the user requests both.

Keep instruction changes and tool proposals as separate results.

## 2. Resolve one instruction target

Configure one instruction target at a time. Keep each change previewable and verifiable.

Identify the active coding agent from direct current-session runtime evidence. Use an explicit user selection next. Use repository markers, installed commands, and configuration only as fallback evidence.

Resolve the supported global or repository `AGENTS.md`, `CLAUDE.md`, or equivalent instruction target. Ask one focused question when the active coding agent or target remains ambiguous. Do not invent an instruction path for an unsupported coding agent.

## 3. Inspect and preview

Inspect the target for:

- equivalent communication and emoji guidance;
- `<!-- qp:asd-ste100:start -->` and `<!-- qp:asd-ste100:end -->` markers;
- an existing `<!-- qp:start -->` policy block;
- missing, duplicate, nested, overlapping, or reversed managed markers;
- complete equivalent unmanaged guidance;
- instructions that conflict with the requested guidance.

Use this exact managed block:

```markdown
<!-- qp:start -->
- Lead with the requested result, decision, or next action.
- In a progress update, lead with the newest user-relevant fact or state. If no result exists yet, lead with the immediate action. Put the next action after the result.
- Report internal process only when it changes scope, safety, authority, proof, or expected wait. Keep a required skill notice concise and state its user-visible effect.
- Use short, direct sentences. Give one instruction or main idea in each sentence. Combine instructions only when the actions must occur at the same time.
- Write an instruction as a direct command.
- Prefer active voice and concrete verbs. Name the actor when omission can cause ambiguity.
- Use common, precise words with one clear meaning for general language. Use technical terms when they are more accurate or useful.
- Use the same term for the same item, action, state, or concept.
- Give technical terms enough context for the reader to understand and learn them. When necessary, add a concise explanation or companion example.
- Replace an ambiguous pronoun or reference with the specific item, action, or result.
- Present procedure steps in execution order. Number the steps when their order matters.
- State a prerequisite condition before the instruction or result that depends on it. Keep other conditions and exceptions next to the text that they control.
- Use headings and lists when they make actions, conditions, results, or exceptions easier to find.
- Preserve exact code, commands, identifiers, paths, API names, quotations, errors, and required domain terms.
- Separate observed facts, inferences, confirmed decisions, recommendations, and next actions when mixing them can mislead.
- Do not turn an inference or optional improvement into a requirement. If it changes scope, requirements, or authority, label it and get approval.
- State uncertainty, evidence limits, and incomplete proof directly.

Do not reduce technical accuracy, bury the main point, hide a condition, or change exact technical content to make the language simpler.

- Use emoji naturally in live user communication when they improve clarity, tone, warmth, or personality.
- Choose emoji that fit the message. Place them beside the text they support. Keep repeated state meanings consistent.
- State every status, result, warning, and decision in words. Emoji must not replace text.
- Do not add emoji to exact content such as code, commands, paths, quotations, or errors.
- Keep formal results and recommendations emoji-free unless the user asks otherwise.
<!-- qp:end -->
```

Treat unmanaged current guidance as equivalent only when it contains every rule from the exact current payload with the same required meaning and has no material conflict.

Apply these rules in order:

1. Validate the markers. Stop without writing when a legacy marker appears or when the current marker pair is partial, duplicate, nested, overlapping, or reversed.
2. Classify managed content. Treat all content inside one valid `qp:start` block as QP-managed. Leave an exact current block unchanged. Otherwise, replace the complete managed block with the current block while preserving its location and all outside content.
3. Classify unmanaged content only when no managed block exists. Leave complete equivalent current guidance unchanged. Append the current block with suitable Markdown spacing when no related guidance exists. Stop without writing for semantic-only, partial, stale, mixed, or conflicting guidance.
4. Check outside instructions and authority. Stop without writing for a material conflict. Capture the original content, preview the exact result, and preserve all unrelated content. Apply an authorized managed-block change only.

Report the detected state and result for every branch. For a stop, name the conflict and required decision. For unchanged unmanaged guidance, report that QP does not own it.

## 4. Apply and verify

Create a timestamped backup beside an existing global or unversioned target unless the user explicitly declined the backup. For a tracked repository target, rely on the verified diff and source control unless the user requests an adjacent backup. Apply only the previewed change.

Re-read the target after writing. Verify that one valid `qp:start` block matches the exact current payload and that content outside the previewed range did not change. For an unchanged target with equivalent unmanaged guidance, verify that the complete target is unchanged.

Report the action, runtime or repository evidence, target, preview result, any backup path, change, and verification result.

## 5. Select and set up companion tools

Run this stage only when the user requested the combined coding-agent baseline or, after instruction setup, explicitly asks to continue with companion tools. Do not inspect the companion-tool catalog for an instruction-only request. Stop when the user selects `none`. Do not continue to Stage 6 for a tool when the user declines its proposed setup or that tool is unsupported.

Inspect every tool in this catalog before recommending an action:

| No. | Tool | Use case | Official documentation |
| --- | --- | --- | --- |
| 1 | IntelliJ MCP | Use IntelliJ IDEA code insight, project navigation, run configurations, terminal actions, and debugger tools from an MCP-compatible coding agent. | [IntelliJ IDEA MCP Server](https://www.jetbrains.com/help/idea/mcp-server.html) |
| 2 | tldr-code | Use for a compact repository map with call flow, data flow, impact, quality, and security signals before deep reading. | [tldr-code](https://github.com/parcadei/tldr-code) |
| 3 | ast-grep | Use for syntax-aware searches and repeatable structural rewrites across code. | [ast-grep](https://astgrep.com/) |
| 4 | Semgrep | Use for repeatable bug, security, and architecture rules in local checks or continuous integration. | [Semgrep](https://docs.semgrep.dev/) |
| 5 | ripgrep | Use for fast literal or regular-expression searches through repository content. | [ripgrep](https://github.com/BurntSushi/ripgrep) |
| 6 | fd | Use for fast file and directory discovery by name, path, or type. | [fd](https://github.com/sharkdp/fd) |

Use current official documentation to verify platform support and the configuration required for the intended use. Check installed commands or applications, versions, prerequisite applications or runtimes, tool configuration, supported MCP, plugin, skill, hook, or other integrations, integration server state, active coding-agent client configuration, and one proportionate usability signal. Do not read or report credentials. Command presence alone does not prove that a tool is ready.

For an installed tool, use `Needs setup` when the suggested use depends on a supported integration and a required prerequisite, server, registration, client entry, or other configuration is missing, stale, or unverified. Name the exact gap without exposing secret values.

Classify each tool and give it one suggested action:

| State | Meaning | Suggested action |
| --- | --- | --- |
| `Ready` | The supported tool and required configuration are present and usable. | `Use` when it adds relevant value; otherwise `Skip`. |
| `Needs setup` | The tool exists, but required configuration, integration, or verification is incomplete or stale. | `Complete setup` when the tool adds relevant value; otherwise `Skip`. |
| `Missing` | The supported tool is not installed. | `Install` only when it adds distinct value; otherwise `Skip`. |
| `Unsupported` | The current platform or required integration does not support the tool. | `Skip`. |

Present one numbered table with the tool, observed state, evidence, suggested action, reason, use case, and official documentation. Base each suggestion on the user's work, current tools, overlap, platform support, and setup cost. Do not recommend every missing tool. Add `All suggested actions` only when two or more compatible actions remain. Add `None`.

Ask:

> Which companion tools should I help you use or set up? Choose one or more numbers or tool names, `all` for all suggested actions, or `none` to stop.

Refresh each selected tool's state before a mutation. For `Needs setup` or `Missing`, propose the exact configuration or installation, permissions, and verification. Apply only accepted actions, then verify the resulting state. For IntelliJ MCP, install or verify IntelliJ IDEA before Stage 6. Authority for one tool does not authorize another.

## 6. Offer supported platform integrations

Use the integration assessment from Stage 5. For each selected tool, refresh stale documentation or state, then present supported MCP, plugin, skill, hook, or other integration options that are not already active. For IntelliJ MCP, include the IDE version, MCP Server plugin, server state, and client configuration.

Present supported integrations as numbered options. Include `Both` for two compatible options, `All` for three or more compatible options or selected platforms, and `Skip integration`. Do not combine conflicting or duplicate options.

Installation does not authorize integration. State each option's target, change, permissions, and verification. Configure only accepted options, verify them from the target platform, and report installation and integration separately.
