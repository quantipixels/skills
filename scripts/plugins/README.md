# Alárinà native plugin build and evidence

The repository owns one canonical Alárinà skill. Native plugins compile its complete reference tree:

```text
skills/alarina/SKILL.md               canonical operating entrypoint
skills/alarina/commands/   focused command methods
skills/alarina/references/<domain>/   shared depth, tools and assets
skills/alarina/routes.yaml            command and playbook topology
plugins/codex/qp-skills/              generated Codex plugin
plugins/claude/qp-skills/             generated Claude plugin
.agents/plugins/marketplace.json      Codex marketplace → generated Codex plugin
.claude-plugin/marketplace.json       Claude marketplace → generated Claude plugin
```

Each generated plugin contains exactly one discoverable `skills/alarina/SKILL.md`. Commands contain their actual methods rather than snapshots of separately installed skills. The source command table is generated from `routes.yaml`; the compiler rejects menu drift, missing resources and invalid policies. Provider-qualified invocation text and implicit-selection metadata are added at build time. Paths inside references remain relative to the installed skill tree, independent of the user's project directory.

## Build and check

Builds stage and validate a complete candidate before publishing it. Existing output is preserved unless `--replace` is given. Replacement keeps the old bundle until the candidate is ready and restores it if publication fails.

```bash
python3 scripts/plugins/build_alarina_bundle.py \
  --provider codex --output plugins/codex/qp-skills --replace
python3 scripts/plugins/build_alarina_bundle.py \
  --provider claude --output plugins/claude/qp-skills --replace

python3 scripts/plugins/build_alarina_bundle.py \
  --provider codex --output plugins/codex/qp-skills --check
python3 scripts/plugins/build_alarina_bundle.py \
  --provider claude --output plugins/claude/qp-skills --check
```

`--check` rebuilds in isolation and compares every file and mode. `bundle-manifest.json` records the provider, route digest, stable source-input digest, qualified invocation, commands, and per-file provenance. It deliberately does not claim model selection or successful runtime command loading.

The provider registry is [providers.yaml](providers.yaml). Codex and Claude are the only release providers. Add another provider only after its discovery rules, namespaces, implicit invocation controls, manifest, native validation, install/update behavior, and activation boundary are established with the current manager.

## Native installation evidence

The verifier installs from this repository's marketplace into disposable manager state and compares the installed plugin with the matching generated source artifact:

```bash
python3 scripts/plugins/verify_native_install.py --host codex
python3 scripts/plugins/verify_native_install.py --host claude
python3 scripts/plugins/test_verify_native_install.py
```

Fresh installation establishes manager registration, enabled state, the one-skill inventory, provider-specific agent inventory, and installed bytes. It does not invoke a model or prove implicit selection in an existing session.

## Check a real A → B update

Keep manager execution, installed content, and session activation as separate evidence. Use disposable user/project state, the installed manager's supported update commands, and no personal installation or credentials.

1. Prepare two complete generated plugin versions. Save a byte copy of the installed A plugin root.
2. Advance the same marketplace source to B and run the provider's supported update through the same registration. Do not replace this step with uninstall plus fresh install.
3. Resolve the installed B root from manager state and compare it with the current generated source:

```bash
python3 scripts/plugins/verify_native_install.py --host codex \
  --before-root "$before_snapshot" --installed-root "$installed_plugin_root"
```

Use `--host claude` for Claude. Snapshot mode reports versions and added, removed, and changed paths while explicitly leaving `manager_transition` and `session_activation` as `not_observed`; pair it with the recorded manager command and a fresh or reloaded consumer session.

## Behavioral evaluation boundary

The focused prompts under `evals/alarina/` are optional behavioral probes with private expectations, not a CI gate or a model runner. Native manager checks establish packaging and discovery. A model run is required to claim selection, routing, command loading or completion quality; package checks do not establish those outcomes.

## Agent adapters

`agents/alarina.md` supplies only the portable identity, description and delegation to the skill. The compiler renders `agents/alarina.md` for Claude with `skills: [qp-skills:alarina]` and a plugin-root fallback, and `agents/alarina.toml` for Codex with `developer_instructions` naming `$qp-skills:alarina`. Model and permission settings inherit from the host.

Codex 0.156.1 loads custom agents from project/user configuration directories, not plugin contents. Its bundle therefore ships a standalone-format profile for separate placement in `.codex/agents/` or `~/.codex/agents/`; no unsupported manifest key or automatic config mutation is added. The native installer check still expects zero auto-registered Codex agents. Claude registers its one agent through the plugin. See [Codex agent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [Claude subagents](https://code.claude.com/docs/en/sub-agents).
