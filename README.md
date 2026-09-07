# QP Skills

Focused expertise and methods for reasoning, engineering, design, and delivery. Use a skill directly or combine useful skills. **Pepeye** is the optional general conversational agent; it handles ordinary requests directly and supervises delegated work when useful.

Each skill lives in [`skills/<name>/SKILL.md`](skills). Its resources load when needed. No mandatory router, one-agent-per-skill rule, or universal task lifecycle is required.

## Install

### Claude Code plugin

Use the native plugin manager when you want the skills and Pepeye agent:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Invoke a skill normally, or select Pepeye for a session:

```bash
claude --agent qp-skills:pepeye
```

Claude's [main-agent selection](https://code.claude.com/docs/en/sub-agents) replaces its built-in system prompt. `model: inherit` inherits the model, not that prompt. Ordinary skill invocation retains the native main agent. Installing the plugin changes no startup default.

### Direct Codex or Claude skill installation

For macOS/Linux with Git and Python 3.10+, clone and inspect the source, then run:

```bash
git clone https://github.com/quantipixels/skills.git
bash skills/scripts/install.sh --codex --dry-run
bash skills/scripts/install.sh --codex
```

Use `--claude` for the skill-only Claude path, or both flags. Do not install QP through both Claude paths. With no host flags, updates retain the installation's existing hosts; a new installation defaults to Codex.

The script installs an owned snapshot under `${XDG_DATA_HOME:-~/.local/share}/qp-skills` and exact links in `~/.agents/skills` or `${CLAUDE_CONFIG_DIR:-~/.claude}/skills`. Updates switch the snapshot atomically and retire only links recorded by this installation. Foreign paths, modified installed files, and existing Skills CLI ownership block replacement. Other hosts and startup settings are not changed.

`--source /path/to/checkout` installs local changes. `--ref <branch|tag|commit>` fetches a selected Git revision instead. A downloaded/piped script defaults to `ori`. Existing Skills CLI installs are not silently adopted: remove or migrate them through that manager first. Native `npx skills add .` remains an alternative, managed independently.

The snapshot's `agents/codex/pepeye.config.toml` is the optional [Codex profile](https://developers.openai.com/codex/config-advanced) for 0.134.0+. Copy it to `$CODEX_HOME/pepeye.config.toml` only after preserving/merging existing effective `developer_instructions`, then run `codex --profile pepeye`. Profiles replace instruction strings rather than append them. They do not define a spawned worker or change sandbox/tool permissions.

For a project/user startup default, make the corresponding host setting explicitly: Claude's `agent` setting, or guarded Codex primary-session instructions. Restore only that setting/instruction block to undo it. Installation, selection, and default configuration are separate operations.

## Update and uninstall

For the direct installation, rerun the installer from the desired checkout or `--ref`. Keep edits in your source checkout, not the immutable installed snapshot.

```bash
bash skills/scripts/uninstall.sh --dry-run
bash skills/scripts/uninstall.sh
```

Removal verifies recorded links and installed content before deleting anything. Re-running from a checkout recovers an interrupted transaction. An incomplete pre-publication staging directory may remain after a killed process; it is never adopted as an active installation or removed by guessing ownership. Native plugins, other managers' records, and user settings are separate. Use the native manager to uninstall its own package.

## Use

Use the skill that helps achieve the requested result. Common entrypoints are `alaga` for implementation, `atunwo` for review, `atona` for planning, `arojinle` for consequential choices, `amose` for domain modelling, and `html-artifact` for browser projections. `arojinle` uses `amose` naturally during its interview. Use [`alarina`](skills/alarina/SKILL.md) for QP entrypoints, useful skill combinations, and the next route from your current work.

The `pepeye` skill is independently usable for staffing, model/effort selection, supervision, worker reuse, and integration. It is a coordination method, not a second conversational identity. Native hosts own tools, permissions, and worker sessions; unavailable controls remain explicit limitations.

Keep one-session work in the conversation. Use an existing project destination for maintained knowledge. `akosile` supplies optional shared repository storage and safe concurrent publication when that workspace is actually selected; it is not a prerequisite for plans, reviews, or artifacts.

## Compatibility and contributing

[Compatibility](docs/compatibility.md) distinguishes package/install proof from authenticated model behavior. The [runtime checks](docs/verification.md) exercise actual host use without turning prose into a keyword test suite.

Use `ko-skill` for authoring and the repository's [contribution instructions](AGENTS.md). Retain expertise and independently necessary safeguards, compose by reference, and put change evidence in PRs and CI rather than another repository report. `metadata.maturity: experimental` records a candidate's maturity without changing its normal activation or permission gates.

The flat source layout replaces the old subject/maturity directories. Skill names and user invocations remain stable; old source-path bookmarks and scripts need their paths updated. `qp-skills:qp` was replaced by `qp-skills:pepeye`; package names and existing `.qp` workspaces are unchanged.
