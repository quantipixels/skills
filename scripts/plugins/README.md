# Native package build and evidence

The repository root is the package for Codex, Claude Code, OpenCode and Pi. [`skills/alarina/`](../../skills/alarina/) is the one canonical method tree. [`agents/alarina.md`](../../agents/alarina.md) is the portable, thin agent profile. No host gets a copied skill tree or rewritten `SKILL.md`.

`npm run build:plugins` validates the source skill and generates the root Codex and Claude plugin manifests plus small Codex, Claude and OpenCode agent declarations. `npm run check:plugins` checks them for drift. [`providers.yaml`](providers.yaml) records the four supported native entry points. [`scripts/skills/check_package.py`](../skills/check_package.py) also checks routes, active links, marketplaces and the single discovery entry.

Codex and Claude marketplaces both source `./`. Codex registers its native TOML agent separately in a project or user agent directory. Claude registers the generated Markdown agent through the plugin, with `qp-skills:alarina` preload and a plugin-root skill fallback. OpenCode loads `./skills` from [`opencode.json`](../../opencode.json) and its project agent from `.opencode/agents/alarina.md`. Pi loads `./skills` from `package.json`; the portable agent profile can be applied through `--append-system-prompt`, and Pi has no package named-agent declaration.

## Native install check

Run `python3 scripts/plugins/verify_native_install.py --host codex` or `--host claude` to install into disposable manager state and compare the installed canonical skill and declarations with a clean staged package. The stage exports only the runtime skill, native declarations, manifests, marketplaces, package metadata and licence. This excludes ignored `.qp/`, `node_modules/` and development files; Codex's local marketplace copier can otherwise include ignored working files from a live checkout. The check does not change the user's installation.

For a local Codex refresh, run `python3 scripts/plugins/verify_native_install.py --export /new/stable/package/path` after `npm run check:plugins`. Point only the install command at that clean source:

```bash
codex -c 'marketplaces.qp-skills.source="/new/stable/package/path"' plugin add qp-skills@qp-skills --json
```

The source override leaves the persisted marketplace registration unchanged. The export path must be new and outside this checkout. Native installation was checked with Codex 0.157.1; resolve the installed path and compare its runtime files before claiming the update complete.

For a saved update comparison, supply one host and the before and installed package roots:

```bash
python3 scripts/plugins/verify_native_install.py --host codex \
  --before-root "$before_snapshot" --installed-root "$installed_plugin_root"
```

Snapshot mode verifies installed package content and reports added, changed and removed files. It does not prove that a manager performed the transition or that a session reloaded. Native manager checks prove registration and bytes; model selection, command loading and task completion need separate runtime evidence. The focused prompts under `evals/alarina/` are optional behavioral probes, not a CI gate.
