# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use that skill directly when the owner is clear; use `alarina` when it is not, and `pepeye` when several results need coordinating into one outcome.

Browse the public docs at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

Global install:

```bash
npx skills add quantipixels/skills --global
```

Install one skill with `--skill <name>`.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

### Direct snapshot install

For macOS/Linux with Git and Python 3.10+:

```bash
git clone https://github.com/quantipixels/skills.git
cd skills
bash scripts/install.sh --codex --dry-run
bash scripts/install.sh --codex
```

Use `--claude` instead, or both flags, for the direct skill-only path. See [compatibility](docs/compatibility.md) for currently proved host paths.

## Start

If you know the skill you need, use it directly. Otherwise:

```text
Use `alarina` to choose the right skill for this request:

[describe the outcome you need]
```

A few common entrypoints:

| Skill | Use when |
| --- | --- |
| `pepeye` | Delegation or a bounded multi-stage workflow needs coordination |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `oro-fun-sigidi` | Agent-facing instructions, skills, prompts, routing, or workflow text needs writing/review |
| `oro-fun-eniyan` | Human-facing technical prose needs writing, editing, or pruning |

Use `alarina` for the complete installed inventory.

`ko-skill` remains a compatibility entrypoint for skill-writing requests and routes to `oro-fun-sigidi`. `oro-ologbon` remains a compatibility entrypoint and routes by audience.

### Optional integrated agent experience

`pepeye` works with the host's native agents without extra setup. It uses seven Yorùbá work postures when staffing delegated work: **Àṣàwárí**, **Olùtúpalẹ̀**, **Akọ̀wé**, **Olùṣe**, **Olùdánilójú**, **Olùwádìí**, and **Olùyẹ̀wò**.

These are staffing concepts, not seven required files. `qp-setup` audits the selected Codex/Claude environment and prefers adequate native agents or existing user definitions. It proposes a QP-managed agent definition only when that definition adds durable value beyond what already exists, then shows the exact change before asking for permission to apply it.

### Host instructions

QP does not install a default global instruction block. Skills should be discoverable and useful through their own descriptions and the host's normal capabilities.

When useful, `qp-setup` can ask permission to audit the user's global `AGENTS.md` / `CLAUDE.md`. It preserves useful existing policy and proposes only durable changes that materially improve behavior; no change is a valid audit result.

## Update

From a checkout, run:

```bash
bash scripts/update.sh
```

The updater detects the existing QP installation manager and delegates to it: the QP direct installer, the Skills CLI, or the Claude Code plugin manager. It does not create a second installation registry.

For Skills CLI installations, current installed QP skills are updated in place. Deprecated installed skills are presented before removal. Use `--sync` if you also want the updater to offer currently missing QP skills for installation.

For a dry run:

```bash
bash scripts/update.sh --dry-run
```

## Uninstall

For a direct snapshot installation:

```bash
bash scripts/uninstall.sh
```

Do not install the package through multiple managers at once.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `oro-fun-sigidi` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.
