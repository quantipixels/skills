# Agent experience

Use when the user wants provider-native worker profiles for a more integrated delegation experience. This branch installs/configures runtime posture; `pepeye` still owns coordination and remains usable without it.

## Keep the layers separate

Provider profiles describe **work posture + runtime defaults**, not semantic expertise or workflow stages.

The shipped postures are defined once in [roles](../assets/agent-experience/roles.json):

- `explorer` — read-only investigation and mapping;
- `analyst` — bounded deep reasoning and consequential technical judgment;
- `writer` — human-facing technical artifacts;
- `implementer` — bounded source/configuration mutation;
- `verifier` — reproduction, testing, and falsification;
- `researcher` — current external/primary-source evidence;
- `reviewer` — fresh independent judgment of a fixed candidate.

Do not preload or hardcode semantic skills into these profiles. An assignment may name an already-selected skill when that materially improves the work; otherwise leave normal skill discovery/use to the host/model. Do not add generic “discover skills” boilerplate merely to restate model-native behavior.

Model and reasoning choices are **defaults**, not role identity. `pepeye` may request a different model/effort for a particular assignment when the host exposes that capability.

## Inspect the actual host

Resolve the host(s), version, scope, current agent/profile support, model choices, effort/reasoning controls, and any existing files from the installed host and current official documentation. Cached model IDs are not authoritative.

Current target conventions are:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/agents/` (default `~/.codex/agents/`) | `<repo>/.codex/agents/` |
| Claude Code | `~/.claude/agents/` | `<repo>/.claude/agents/` |

If the installed host uses a different supported location or schema, follow the host and report the difference instead of forcing the cached convention.

Inspect all target role files before proposing a write. Also inspect only the host configuration needed to determine whether native subagents/profile selection are enabled and usable. Do not enable experimental team/runtime features merely because the host offers them.

## Ask once, then show the real proposal

Use the host's structured question UI when available. Prefer one compact setup interview over a serial chain of confirmations.

Resolve these choices:

1. **Host** — Codex, Claude Code, or both when both are available.
2. **Scope** — current repository or user/global.
3. **Optimization** — `Balanced` (default), `Efficient`, `Quality`, or `Custom`.
4. **Role overrides** — ask only when `Custom` is selected or the detected host/account cannot satisfy the proposed mapping.
5. **Main/root model** — preserve the existing setting by default. Treat changing it as a separate optional choice, not part of installing worker profiles.

Defaults inside the interview may be accepted normally. **The final mutation confirmation must default to No.**

### Resolve presets from current capability

The role catalogue records a baseline model class (`efficient | balanced | strong`) and effort. Map those classes to concrete models actually available in the selected host/account and show the resolved mapping before applying it.

- **Balanced** — use the catalogue baseline.
- **Efficient** — move `strong → balanced` and `balanced → efficient`; keep already-efficient roles efficient. Reduce effort where the current task-independent default would otherwise be needlessly deep, but do not go below a host-supported level that makes the posture unreliable.
- **Quality** — move `efficient → balanced` and `balanced → strong`; keep strong roles strong. Prefer deeper supported effort for `analyst`, `implementer`, and `reviewer`, with proportional defaults for the remaining roles.
- **Custom** — use the user's per-role model/effort choices.

If the available models do not form three meaningful classes, collapse classes rather than inventing distinctions. If support is uncertain, ask the smallest question needed to resolve it.

These are startup defaults only. Do not encode “reviewer must always use the strongest model” or similar semantic rules into the profile.

## Preview before mutation

Prepare the native profiles in a temporary directory with [render-agent-profiles.py](../scripts/render-agent-profiles.py). Feed it a temporary JSON mapping of role names to the resolved concrete `model` and `effort` values; do not create persistent package state merely to drive rendering.

Show a compact preview that includes:

- host + scope;
- every role with concrete model and effort;
- read-only vs write-capable posture;
- exact files to add/update;
- any required host-config key that would change;
- existing profile files that would be replaced; and
- backup location.

Then ask one final confirmation equivalent to:

```text
Apply these agent-experience changes? [y/N]
```

A blank answer means **No**. If the proposal changes after that preview, show the changed proposal and ask again.

## Apply without taking over the harness

Render/install only the selected profiles. Preserve unrelated profiles, instructions, permissions, providers, MCP configuration, and host settings.

For Codex, merge only a currently supported setting that is genuinely required to make native subagents/profile selection usable. Do not configure Code Mode, join/wait behavior, scheduling, retry policy, or model-selection algorithms: those belong to the harness.

For Claude Code, install native subagent definitions only. Do not preload semantic skills into `skills:` fields. Do not enable agent teams merely to make these profiles work; teams are a separate host capability that `pepeye` may use when already available and valuable.

Before replacing an existing profile or config file, save a byte-for-byte backup under the host's own configuration area:

- Codex user → `$CODEX_HOME/backups/skill-setup/agent-experience/`;
- Codex repository → `<repo>/.codex/backups/skill-setup/agent-experience/`;
- Claude user → `~/.claude/backups/skill-setup/agent-experience/`;
- Claude repository → `<repo>/.claude/backups/skill-setup/agent-experience/`.

Use unique backup names and never overwrite earlier backups. Dry-run/inspection creates no files.

Refresh each destination immediately before writing. If it changed after preview in a way that affects the edit, reconcile and obtain confirmation for the revised proposal.

## Verify and return

Read every installed profile back. Confirm:

- all seven selected role definitions are present exactly once;
- model/effort values match the accepted preview;
- read/write posture matches the role catalogue as far as the host can enforce it;
- no semantic skill was preloaded or hardcoded into a profile;
- unrelated host configuration is unchanged; and
- the host can discover the profile location, noting when a new session is required.

Return the host/scope, installed roles, resolved model/effort defaults, changed files, verification, backup/rollback path, and any host capability limitation.
