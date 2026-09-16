# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use `alarina` to coordinate the work, or invoke a specialist directly for a focused result.

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

### Give the agent a working brief

After installing the skills, copy this block into your personal or project `AGENTS.md` / `CLAUDE.md`, or paste it into a conversation for that session. Merge it with existing instructions. Keep, adapt or omit the final paragraph to fit your preferred personality; it is yours to choose.

```text
Use the installed `alarina` skill as the governing working method for carrying my requests through authorized completion. Load it, then select and apply relevant installed skills and playbooks as the work evolves. Read their instructions and applicable references; use their methods, not just their names. Keep settled work direct and preserve accepted decisions when resuming.

Choose available tools by the evidence the task needs. Use `irinse` when source structure, measurement semantics, effective use or readiness needs guidance; do not wait for a poor result before choosing a suitable capability. Keep routine work direct and report material capability or coverage gaps.

When work needs planning, use `atona` to guide it and `html-artifact` for the human-readable plan. Keep the same document current through delivery, showing the direction, decisions, progress, evidence and remaining choices clearly enough for someone new to the work to follow. Keep me involved when my judgment is needed and carry on with work already authorized.

Be a steady workmate: warm, direct, resourceful and candid. Have a view and reconsider when evidence warrants it. Care about craft, follow through and keep me oriented. Match my language and tone; let humour arise naturally.
```

Then describe your work normally. Saved instructions apply when your host loads that file; a conversation paste applies to that session. This brief does not install tools, change permissions, select a model or create a worker. Personality stays in user-owned instructions, not in the skills.

The plugin bundles an [Alárinà agent definition](agents/alarina.md), but using its skill as a working method does not require creating a separate agent configuration. Codex does not automatically register bundled Markdown definitions as custom agents.

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
| `irinse` | Tool selection, difficult source retrieval, effective use, or environment readiness needs guidance |
| `yoruba-glossary` | Yorùbá language guidance, lessons, word formation, or glossary maintenance is needed |
| `oro` | Agent-facing instructions or human-facing technical prose needs writing, review, editing, or pruning |
| `adanwo` | A bounded exploratory or measured experiment must settle uncertainty |
| `alarina` | Select or use an engineering playbook, compose or resume work across owners, or find the starting owner |
| `human-view` | Supplied content needs a clear default visual presentation without a full design engagement |

Alárinà uses installed skill definitions as the dynamic inventory.

See [a worked engineering example](docs/engineering-example.md) for how identity, recovery, architecture and tests fit together in a retry fix.

With `alarina` active, describe the engineering outcome or name a playbook; it selects the path and coordinates the relevant skills. The [engineering playbooks guide](docs/engineering-playbooks.md) shows supported paths, direct invocation examples and expected evidence. Settled single-owner work can still use its specialist directly.

## Update

Explicitly invoke `qp-update` to identify the active installation and update QP through its existing manager. It preserves installation scope and local changes, and distinguishes installed updates from a session that still needs reloading. It does not run automatically.

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

To verify a checkout through both native plugin managers without changing your normal host configuration, run:

```bash
python3 scripts/plugins/verify_native_install.py
```

The verifier uses temporary Codex and Claude configuration directories, installs the local checkout, checks the reported component inventory, and compares representative installed files with their sources. Pass `--host codex` or `--host claude` to exercise one manager. A successful run proves manager discovery and installed-content agreement; start a fresh host session to verify runtime skill invocation.

Use the opt-in [engineering evaluations](evals/README.md) to compare actual repairs with and without skill guidance. The kit checks executable contracts and regression detection; your native host runs the models.
