# QP Skills

Focused expertise and methods for reasoning, engineering, design, and delivery. Use skills directly or combine them as needed. QP has no mandatory router or universal task lifecycle.

Each skill lives in [`skills/<name>/SKILL.md`](skills) and loads its own supporting resources.

## Install

### Claude Code

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
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

Common entrypoints are `atona` for planning, `alaga` for code delivery, `atunwo` for independent code review, `arojinle` for consequential choices, `amose` for domain modelling, and `html-artifact` for browser projections. Use [`alarina`](skills/alarina/SKILL.md) when you want the QP inventory or help choosing the next skill.

Use [`pepeye`](skills/pepeye/SKILL.md) for optional subagent coordination. It uses native delegation tools and the existing specialist skills, without installing a main-agent identity, worker files, or host settings. Install it with `npx skills add quantipixels/skills --skill pepeye -g`, or use the package installation above. No separate Pepeye plugin or setup is required. Host support determines which worker model and reasoning controls are available.

Use [`irinse`](skills/irinse/SKILL.md) to discover, select, and use high-leverage companion engineering tools whose useful interfaces or evidence semantics are easy to miss. Irinṣẹ is a small tool router and usage-knowledge home; it does not own installation or configuration.

Use [`qp-setup`](skills/qp-setup/SKILL.md) when a selected engineering/agent tool must be installed, configured, updated, verified, or removed, or for optional QP/Codex host configuration. Its Codex branch still supports general instructions, a Pepeye binding, main-session defaults, and Context Notes at user or repository scope with preview, permission, and backups. Install the skill with `npx skills add quantipixels/skills --skill qp-setup -g`; omit `-g` for a repository skill installation. Choose the configuration scope separately when running setup.

For explanations use `salaye`; for technical authoring or prose cleanup/pruning use `oro-ologbon`. Use `alaga` for accepted code delivery; standalone scope discussion belongs to the planning, specification, or decision owner for the unresolved question. Explicit legacy `alaga scope-only` remains compatibility-only for this minor release.

## Project

[Compatibility](docs/compatibility.md) records what the package currently proves. Use [`AGENTS.md`](AGENTS.md) and `ko-skill` for contribution and skill-authoring guidance. Change evidence belongs in PRs and CI rather than new repository reports.
