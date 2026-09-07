# QP Skills

Focused expertise and methods for reasoning, engineering, design, and delivery. Use skills directly or combine them as needed. **Pepeye** is the optional general agent for ordinary work and supervised delegation.

Each skill lives in [`skills/<name>/SKILL.md`](skills) and loads its own supporting resources. QP has no mandatory router or universal task lifecycle.

## Install

### Claude Code

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Select Pepeye for a session when useful:

```bash
claude --agent qp-skills:pepeye
```

### Codex or skill-only installation

For macOS/Linux with Git and Python 3.10+:

```bash
git clone https://github.com/quantipixels/skills.git
cd skills
bash scripts/install.sh --codex --dry-run
bash scripts/install.sh --codex
```

Use `--claude` instead, or both flags, for the direct skill-only path. Run `bash scripts/install.sh --help` for the supported options. Do not install QP through multiple managers at once.

Rerun the installer to update. Remove a direct installation with:

```bash
bash scripts/uninstall.sh
```

The repository also includes a native Codex plugin manifest. See [compatibility](docs/compatibility.md) for the currently proved host paths.

## Use

Common entrypoints are `atona` for planning, `alaga` for implementation, `atunwo` for review, `arojinle` for consequential choices, `amose` for domain modelling, and `html-artifact` for browser projections. Use [`alarina`](skills/alarina/SKILL.md) when you want the QP inventory or help choosing the next skill.

Use `pepeye` for delegated staffing, supervision, worker reuse, and integration when that coordination is useful.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `ko-skill` for contribution and skill-authoring guidance. Change evidence belongs in PRs and CI rather than new repository reports.
