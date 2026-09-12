# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use that skill directly when the owner is clear; use `alarina` when it is not.

Browse the public docs at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

Choose the native plugin for your host, or Skills CLI for editable skill copies. Use one installation method per host to avoid duplicate skills.

### Codex plugin

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex, then use `$qp-skills:alarina` with your requested outcome. The plugin installs all QP skills. You control the model and reasoning.

In the Codex app, add `quantipixels/skills` as a custom marketplace in Plugins, install `qp-skills`, and restart.

### Skills CLI

Install all skills for Codex in the current project:

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

Add `--global` for a personal installation, or replace `'*'` with a skill name for a selective install. Alárinà's complete operating experience requires all QP skills; individual skills remain independently usable.

For Claude Code, replace `--agent codex` with `--agent claude-code`. Skills CLI installs skills; use the Claude plugin to include Pepeye as a native agent.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code or run `/reload-plugins`. The plugin provides all QP skills and the `qp-skills:pepeye` agent, which preloads Alárinà. Use `/qp-skills:alarina` directly, ask Claude to delegate to `qp-skills:pepeye`, or start a session with:

```bash
claude --agent qp-skills:pepeye
```

Model, reasoning, and permissions remain under your control. Claude discovers the shared `skills/` and `agents/` directories natively; no setup script or separate agent configuration is needed.

## Start

### Work with Alárinà

After installing all QP skills, paste this at the start of your Codex or Claude Code conversation:

```text
Read and follow the installed `qp-skills:alarina` skill throughout this session.
```

For Skills CLI installations, replace `qp-skills:alarina` with `alarina`. Then describe your work normally. Repeat the instruction in a new conversation; it does not change your saved configuration, model, or reasoning settings.

This uses Alárinà's operating method without creating or maintaining a [Pepeye](agents/pepeye.md) agent configuration. The plugin bundles Pepeye's definition, but Codex does not automatically register bundled Markdown definitions as custom agents.

### Use a skill directly

If you know the skill you need, use it directly.

Common entrypoints:

| Skill | Use when |
| --- | --- |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `irinse` | A selected tool, host integration, or shared instruction surface needs setup or repair |
| `oro-fun-sigidi` | Agent-facing instructions, skills, prompts, routing, or workflow text needs writing/review |
| `oro-fun-eniyan` | Human-facing technical prose needs writing, editing, or pruning |

Use `alarina` for the complete installed inventory.


## Optional user instructions

Skills work without a shared instruction block. Copy whichever lines below match how you want the assistant to work, or use all of them. Edit them to suit your workflow:

```text
Use `alarina` when the right skill is unclear.
Use `ro-wo` before accepting or rejecting a consequential premise or proposed approach.
Use `oro-fun-sigidi` when writing or changing agent-facing instructions, skills, or prompts.
Use `oro-fun-eniyan` when writing or refining human-facing technical prose.
Use `root-cause` when a failure's causal mechanism is unresolved before implementing a fix.
Use `atunwo` when an independent code review is requested or materially warranted by risk or uncertainty.
```

These lines guide skill use; they do not grant additional tool or publication permissions. `irinse` can help place only the lines you select in the appropriate instruction file.

## Update

For a Git-backed Codex plugin installation:

```bash
codex plugin marketplace upgrade qp-skills
codex plugin add qp-skills@qp-skills
```

Restart Codex afterward. For Skills CLI installations, use `npx skills update`. Reuse the installation manager that owns your skills.

For Claude Code:

```bash
claude plugin marketplace update qp-skills
claude plugin update qp-skills@qp-skills
```

Restart Claude Code or run `/reload-plugins` afterward.

Claude plugin updates follow Git commits. The manifest intentionally omits `version`, so there is no version to synchronize with `package.json` releases.

## Uninstall

For the Codex plugin:

```bash
codex plugin remove qp-skills@qp-skills
codex plugin marketplace remove qp-skills
```

For Claude Code:

```bash
claude plugin uninstall qp-skills@qp-skills
claude plugin marketplace remove qp-skills
```

For Skills CLI, use `npx skills remove` and select the QP skills. Do not install the package through multiple managers at once.

If migrating from the retired direct installer, preserve local edits and use its original uninstaller before switching managers.

## Project

Use [`AGENTS.md`](AGENTS.md) and `oro-fun-sigidi` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.
