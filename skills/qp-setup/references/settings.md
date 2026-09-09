# QP settings and native agents

QP preferences are data, not a replacement host configuration. Supported files are:

- user: `~/.qp/setting.json`
- repository: `<git-root>/.qp/setting.json`

Repository discovery uses `git rev-parse --show-toplevel`, so subdirectories, nested repositories, and linked worktrees use the correct checkout. An explicit `--repo PATH` is available for non-Git projects. QP does not walk parent directories looking for `.qp` files.

## Precedence

Resolve each field independently:

1. built-in default;
2. user host default;
3. user agent override;
4. repository host default;
5. repository agent override.

Scope wins over specificity. This lets a repository set `model: adaptive` and reset all user-level model pins while preserving a user reasoning preference it does not mention. `adaptive` means Pepeye chooses an available model/effort for the job and leaves the native agent unpinned. `inherit` also leaves the native field unset but asks Pepeye not to choose an override. Neither value proves what a host actually ran.

Pepeye itself remains the host-selected main agent and is not configurable through the worker `agents` map. Keep startup model/session selection in the host.

## Communication

`communication` supports:

- `default` — add no QP communication instruction; native agent/host/project configuration remains in control.
- `adaptive` — match the user's current language, register, and detail level.
- `yoruba` — use Yoruba for user-facing prose, with appropriate diacritics.

Explicit task language and output contracts override the preference. Code, identifiers, commands, paths, quotations, and machine-readable output stay exact. The helper returns the resolved instruction but deliberately does not bake communication into generated agents: runtime workers receive the coordinator's current policy, so changing communication does not require regenerating agents.

## Model and reasoning example

```json
{
  "$schema": "https://raw.githubusercontent.com/quantipixels/skills/ori/skills/qp-setup/assets/setting.schema.json",
  "version": 1,
  "communication": "adaptive",
  "codex": {
    "reasoning": "high",
    "agents": {
      "atona": { "model": "gpt-5.6-sol", "reasoning": "xhigh" },
      "alaga": { "model": "adaptive", "reasoning": "adaptive" }
    }
  },
  "claude": {
    "model": "adaptive",
    "agents": {
      "atunwo": { "model": "opus", "reasoning": "high" }
    }
  }
}
```

Model identifiers are host-owned strings. The schema intentionally does not maintain a volatile model catalogue. Reasoning values are constrained to the host surfaces QP can render; unsupported future values must be added deliberately rather than silently ignored.

## Inspect

From an installed `qp-setup` skill:

```bash
python3 scripts/configure.py inspect
python3 scripts/configure.py inspect --global
python3 scripts/configure.py inspect --repo /path/to/project
```

Output is resolved policy plus source paths and origins. It is not a runtime observation.

## Native agent setup

Claude plugin installation already exposes packaged `pepeye`, `atona`, `alaga`, `atunwo`, `iwadi`, `architect`, and `ko-skill` agents. Those packaged adapters use adaptive defaults and cannot read local `.qp` preferences during plugin installation. Use native sync only when you need user/repository pins or a direct skills installation.

Preview first:

```bash
python3 scripts/configure.py sync --host all --scope user --dry-run
python3 scripts/configure.py sync --host codex --scope repo --dry-run
```

Then run the same command without `--dry-run`. For a direct Claude skills installation, native agents preload bare skill names. If Claude skills come from the QP plugin but you want separately generated user/repository agents, add `--plugin-skills` so the generated workers preload `qp-skills:<skill>`.

User sync reads only user preferences; it cannot accidentally bake repository settings into global agents. Repository sync reads both scopes. The helper writes only QP-owned files in the selected native `agents/` directory and its ownership/lock metadata. It does not modify `settings.json`, `config.toml`, permissions, startup defaults, installed skills, or `.qp/setting.json`. Existing unowned files and edited QP files are collisions and are preserved.

Remove only owned native agents with:

```bash
python3 scripts/configure.py remove --host all --scope user --dry-run
python3 scripts/configure.py remove --host all --scope user
```

Removal is intentionally independent of settings validity. A stale `.qp-setup.lock` after interruption requires confirming no setup process is active before manual lock removal and retry.

## Roles

Pepeye remains the coordinator and final synthesizer. Native workers are focused execution contexts rather than aliases for every skill:

- `atona`: planning and premortem readiness;
- `alaga`: bounded implementation and proof;
- `atunwo`: independent read-only review;
- `iwadi`: substantial evidence-backed research;
- `architect`: consequential architecture analysis;
- `ko-skill`: skill authoring/validation.

Premise testing (`ro-wo`) and communication cleanup (`oro-ologbon`) stay shared capabilities inside these workers instead of becoming extra agent identities. This keeps the roster job-shaped and lets Pepeye compose expertise without a fixed pipeline.

Claude read-only workers receive an allowlist of read/search/web tools. Codex read-only workers use `sandbox_mode = "read-only"`. Mutable workers are instructed not to delegate further; host permission configuration remains authoritative. No adapter grants provider-write, commit, push, installation, or publication authority.
