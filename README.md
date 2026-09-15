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

Restart Codex, then ask it to use `alarina` with your requested outcome. The plugin installs all QP skills. You control the model and reasoning.

In the Codex app, add `quantipixels/skills` as a custom marketplace in Plugins, install `qp-skills`, and restart.

### Skills CLI

Install all skills for Codex in the current project:

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

Add `--global` for a personal installation, or replace `'*'` with a skill name for a selective install. Alárinà's complete operating experience requires all QP skills. Individual skills can be used without Alárinà; include any companion required by the selected branch. For initiative planning with `atona`, also install `html-artifact`.

For Claude Code, replace `--agent codex` with `--agent claude-code`. Skills CLI installs skills; use the Claude plugin to include Alárinà as a native agent.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code or run `/reload-plugins`. The plugin provides all QP skills and the Alárinà agent. Ask Claude to use `alarina` for your requested outcome.

Model, reasoning, and permissions remain under your control. Claude discovers the shared `skills/` and `agents/` directories natively; no setup script or separate agent configuration is needed.

## Start

### Work with Alárinà

After installing all QP skills, paste this at the start of your Codex or Claude Code conversation:

```text
Read and follow the installed `alarina` skill throughout this session.
```

Then describe your work normally. Repeat the instruction in a new conversation; it does not change your saved configuration, model, or reasoning settings.

This uses Alárinà's operating method without creating or maintaining an [Alárinà](agents/alarina.md) agent configuration. The plugin bundles Alárinà's definition, but Codex does not automatically register bundled Markdown definitions as custom agents.

### Make it your own

Personality belongs in your user instructions. Copy and adapt this optional example into your personal `AGENTS.md` or `CLAUDE.md`:

```text
Be a steady workmate: warm, direct, resourceful, and candid. Have a view
and reconsider when evidence warrants it. Care about craft, follow through,
and keep me oriented. Match my language and tone; let humour arise naturally.

Read and follow the installed `alarina` skill throughout this session.
Use `html-artifact` for plans and keep the same human-readable document
current through delivery.
```

Choose your own name, voice and language preferences. The example takes effect only when you adopt it; installing Alárinà does not set a persona or change your user instructions.

### Use a skill directly

If you know the skill you need, use it directly.

Common entrypoints:

| Skill | Use when |
| --- | --- |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `architect` | Technical structure, interfaces or technology choices need survey, design or review |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `irinse` | A selected tool, host integration, or shared instruction surface needs setup or repair |
| `yoruba-glossary` | Yorùbá language guidance, lessons, word formation, or glossary maintenance is needed |
| `oro` | Agent-facing instructions or human-facing technical prose needs writing, review, editing, or pruning |
| `adanwo` | A bounded exploratory or measured experiment must settle uncertainty |
| `alarina` | The starting owner or useful route is unclear, or delegated work needs coordination |
| `human-view` | Supplied content needs a clear default visual presentation without a full design engagement |

Alárinà uses installed skill definitions as the dynamic inventory.

See [a worked engineering example](docs/engineering-example.md) for how identity, recovery, architecture and tests fit together in a retry fix.

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

## Project

Use [`AGENTS.md`](AGENTS.md) and `oro` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.

Use the opt-in [engineering evaluations](evals/README.md) to compare actual repairs with and without skill guidance. The kit checks executable contracts and regression detection; your native host runs the models.
