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

### Direct snapshot

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

Common entrypoints:

| Skill | Use when |
| --- | --- |
| `pepeye` | Delegation or a bounded multi-stage workflow needs coordination |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `qp-setup` | A selected tool, host integration, or shared instruction surface needs setup or repair |
| `oro-fun-sigidi` | Agent-facing instructions, skills, prompts, routing, or workflow text needs writing/review |
| `oro-fun-eniyan` | Human-facing technical prose needs writing, editing, or pruning |

Use `alarina` for the complete installed inventory.

`ko-skill` remains a compatibility entrypoint for skill-writing requests and routes to `oro-fun-sigidi`. `oro-ologbon` remains a compatibility entrypoint and routes by audience.

## Optional user instructions

Skills work without a shared instruction block. Copy whichever lines below match how you want the assistant to work, or use all of them. Edit them to suit your workflow:

```text
Use `alarina` when the right skill is unclear.
Use `pepeye` when several independent results or dependent stages need coordination; keep simple work local.
Use `ro-wo` before accepting or rejecting a consequential premise or proposed approach.
Use `oro-fun-sigidi` when writing or changing agent-facing instructions, skills, or prompts.
Use `oro-fun-eniyan` when writing or refining human-facing technical prose.
Use `root-cause` when a failure's causal mechanism is unresolved before implementing a fix.
Use `atunwo` when an independent code review is requested or materially warranted by risk or uncertainty.
```

These lines guide skill use; they do not grant additional tool or publication permissions. `qp-setup` can help place only the lines you select in the appropriate instruction file.

Pepeye's model and reasoning preferences live separately in `~/.qp/settings.json`, under `providers.codex.actions` and `providers.claude.actions`. On first use, if the file is missing, Pepeye calls `qp-setup` to create it from the shipped [configuration template](skills/qp-setup/assets/settings.json). Setup previews the settings and preserves your choices. Without a matching preference—or if setup is declined or unavailable—Pepeye chooses sufficient capability at reasonable cost. The JSON contains no free-form behavioral instructions.

Setup copies only the active host's template section by default; choose “Both hosts” to configure Codex and Claude together. Adding another host later preserves existing action choices and unrelated settings.

## Update

From a checkout:

```bash
bash scripts/update.sh
```

The updater detects the existing QP installation manager and delegates to it. Use `--dry-run` to preview. For selective Skills CLI installs, `--sync` also offers currently missing QP skills; removals and additions that change the installed catalogue require confirmation.

## Uninstall

For a direct snapshot installation:

```bash
bash scripts/uninstall.sh
```

Do not install the package through multiple managers at once.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `oro-fun-sigidi` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.
