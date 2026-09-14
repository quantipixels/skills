# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use that skill directly when the owner is clear; use `pepeye` when it is not.

Browse the public docs at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

Choose the native plugin for your host, or Skills CLI for editable skill copies. Use one installation method per host to avoid duplicate skills.

### Codex plugin

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex, then use `$qp-skills:pepeye` with your requested outcome. The plugin installs all QP skills. You control the model and reasoning.

In the Codex app, add `quantipixels/skills` as a custom marketplace in Plugins, install `qp-skills`, and restart.

### Skills CLI

Install all skills for Codex in the current project:

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

Add `--global` for a personal installation, or replace `'*'` with a skill name for a selective install. Pepeye's complete operating experience requires all QP skills; individual skills remain independently usable.

For Claude Code, replace `--agent codex` with `--agent claude-code`. Skills CLI installs skills; use the Claude plugin to include Pepeye as a native agent.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code or run `/reload-plugins`. The plugin provides all QP skills and the `qp-skills:pepeye` agent, which preloads Pepeye. Use `/qp-skills:pepeye` directly, ask Claude to delegate to `qp-skills:pepeye`, or start a session with:

```bash
claude --agent qp-skills:pepeye
```

Model, reasoning, and permissions remain under your control. Claude discovers the shared `skills/` and `agents/` directories natively; no setup script or separate agent configuration is needed.

## Start

### Work with Pepeye

After installing all QP skills, paste this at the start of your Codex or Claude Code conversation:

```text
Read and follow the installed `qp-skills:pepeye` skill throughout this session.
```

For Skills CLI installations, replace `qp-skills:pepeye` with `pepeye`. Then describe your work normally. Repeat the instruction in a new conversation; it does not change your saved configuration, model, or reasoning settings.

This uses Pepeye's operating method without creating or maintaining a [Pepeye](agents/pepeye.md) agent configuration. The plugin bundles Pepeye's definition, but Codex does not automatically register bundled Markdown definitions as custom agents.

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
| `oro` | Agent-facing instructions or human-facing technical prose needs writing, review, editing, or pruning |
| `adanwo` | A bounded exploratory or measured experiment must settle uncertainty |
| `pepeye` | The starting owner or useful route is unclear, or delegated work needs coordination |

Pepeye uses installed skill definitions as the dynamic inventory.

### 4.2 identity migration

This minor release keeps the methods while removing retired entrypoint directories. Update explicit invocations and saved paths:

| Previous name | Canonical route |
| --- | --- |
| `alarina` | `pepeye` |
| `hitl` | `pepeye` coordination/user-involvement policy |
| `ro-wo` | `pepeye` premise check |
| `se-triage` | `alaga` issue-intake mode |
| `root-cause` | `alaga` diagnosis mode |
| `seda-spec` | `atona` behavior-contract mode |
| `seda-ticket` | `atona` decomposition mode |
| `seda-pr` | `wo-pr` publication mode |
| `yoruba-glossary` | `amose` Yorùbá terminology branch |
| `oro-fun-sigidi`, `oro-fun-eniyan`, `oro-ologbon` | `oro` with the appropriate audience branch |
| `salaye` | `oro` visual-explanation branch |
| `prototype` | `adanwo` exploration mode |
| `optimize` | `adanwo` measured-experiment mode |


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

Use [`AGENTS.md`](AGENTS.md) and `oro` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.
