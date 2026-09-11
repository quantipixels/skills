# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use that skill directly when the owner is clear; use `alarina` when it is not, and `pepeye` when several QP results need to be coordinated into one outcome.

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
Use `alarina` to choose the right QP skill for this request:

[describe the outcome you need]
```

A few common entrypoints:

| Skill | Use when |
| --- | --- |
| `pepeye` | Several QP results or subagents need coordination into one bounded outcome |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `ko-skill` | An agent skill needs creation, improvement, validation, or bounded portfolio review |

Use `alarina` for the complete installed inventory.

## Recommended global instructions

QP works without extra global instructions. Add this block only when you want these defaults across projects:

```text
Use relevant QP skills when they materially improve the result. Use `alarina` when the next owner is unclear; otherwise use the owning skill directly.
Use `pepeye` when the user requests delegation or a bounded multi-stage outcome materially benefits from several QP result owners or subagents.
Use `ro-wo` before agreeing or disagreeing with a material premise.
Use `oro-ologbon` for technical communication and prose cleanup.
```

User-level instruction files:

- **Codex:** `$CODEX_HOME/AGENTS.md` (defaults to `~/.codex/AGENTS.md`)
- **Claude Code:** `~/.claude/CLAUDE.md`

For one repository, use its normal `AGENTS.md`, `CLAUDE.md`, or equivalent instruction surface instead.

For Codex, you can ask QP to apply the supported block safely:

```text
Use `qp-setup` to configure my user-level QP instructions. Preview the exact diff first and preserve my existing instructions.
```

`qp-setup` handles inspection, backup, preview, and approved user/repository-scope changes. You can remove any line from the recommended block if you do not want that default behavior.

## Update and uninstall

Rerun the Skills CLI or your chosen installer to update.

For a direct snapshot installation:

```bash
bash scripts/uninstall.sh
```

Do not install QP through multiple managers at once.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `ko-skill` for contribution and skill-authoring guidance. Change rationale and proof belong in PRs and CI.
