# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result; use the owner directly, or use `pepeye` when several QP results need to be coordinated into one outcome.

Browse the public docs at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

The simplest global install is:

```bash
npx skills add quantipixels/skills --global
```

Install a named skill with `--skill <name>`.

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

If you know the result you need, invoke that skill directly. If you do not, start with Alárinà:

```text
Use `alarina` to choose the right QP skill for this request:

[describe the outcome you need]
```

Common entrypoints:

| Skill | Use when |
| --- | --- |
| `alarina` | The next QP owner is unclear |
| `pepeye` | A bounded multi-stage outcome needs several QP result owners or native subagents |
| `ro-wo` | A material premise needs testing before agreement or disagreement |
| `arojinle` | A consequential choice needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `architect` | Software/module structure, ownership, seams, state, or architecture sufficiency needs design or review |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate, codebase snapshot, or refactor parity claim needs independent judgment |
| `wo-pr` | An existing PR/MR needs to become reviewable and mergeable |
| `seda-pr` | Requested work needs commit/push and PR/MR publication |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `ayewo-igba-ise` | Finished or materially paused work needs an evidence-backed postmortem |
| `ko-skill` | A skill needs creation, revision, validation, or a bounded portfolio audit |
| `oro-ologbon` | Technical communication or supplied prose needs clearer, tighter wording |

Use `alarina` for the full installed inventory rather than treating this table as the catalogue.

## Global agent instructions

QP works without extra global instructions. Add only the defaults you want the agent to apply across projects.

User-level instruction files:

- **Codex:** `$CODEX_HOME/AGENTS.md` (defaults to `~/.codex/AGENTS.md`)
- **Claude Code:** `~/.claude/CLAUDE.md`

For one repository, use its normal `AGENTS.md`, `CLAUDE.md`, or equivalent instruction surface instead.

### QP routing

```text
Use relevant QP skills when they materially improve the result. Use `alarina` when the next owner is unclear; otherwise use the owning skill directly.
```

### Workflow orchestration

```text
Use `pepeye` when the user requests delegation or a bounded multi-stage outcome materially benefits from several QP result owners or native subagents. Use specialist QP skills directly for their methods.
```

### Critical judgment

```text
Use `ro-wo` before agreeing or disagreeing with a material premise.
```

### Communication

```text
Use `oro-ologbon` for technical communication and prose cleanup.
```

For Codex, `qp-setup` can inspect, preview, back up, and apply approved QP instructions at user or repository scope instead of editing the instruction file blindly.

## Update and uninstall

Rerun the Skills CLI or your chosen installer to update.

For a direct snapshot installation:

```bash
bash scripts/uninstall.sh
```

Do not install QP through multiple managers at once.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `ko-skill` for contribution and skill-authoring guidance. Change rationale and proof belong in PRs and CI rather than turning the README into project architecture documentation.
