# Repository guidance

For repository work, use this checkout's [Alárinà skill](skills/alarina/SKILL.md); the installed plugin can lag. Use `oro-sigidi` for agent instructions and `oro-eniyan` for human prose.

## Edit the owner

- `skills/alarina/` is canonical: `commands/` own results, `references/` share expertise by use case, and `playbooks/` compose workflows. Keep one discoverable `SKILL.md`; preserve command invocation permissions, including explicit-only `pese` and `qp-update`.
- [routes.yaml](skills/alarina/routes.yaml) owns inventory and the `SKILL.md` menu. Update both together: the compiler rejects menu drift but does not rewrite it.
- [agents/alarina.md](agents/alarina.md) delegates to the skill; [providers.yaml](scripts/plugins/providers.yaml) records the four native host entry points. Keep operating methods out of agent profiles.
- The repository root is the shared native package for Codex, Claude Code, OpenCode and Pi. Build outputs are only the root plugin manifests and small native agent declarations; do not copy or rewrite the skill tree per host.

## Build and verify

The npm build wrappers use `python3` and [requirements-dev.txt](requirements-dev.txt), even for Markdown-only skill changes. Install dependencies in a virtual environment when needed.

After changing shipped sources, run from the repository root and include regenerated declarations in the change:

```sh
npm run build:plugins
npm run check:plugins
python3 scripts/skills/check_package.py
```

For compiler or installer changes, add `npm run test:plugins`. [Package CI](.github/workflows/checks.yml) lists other mechanical checks; [build guidance](scripts/plugins/README.md) covers native installation. Verify activation and model behavior separately when claimed. Keep model evals optional; do not recreate deliberately retired checks.

Before pushing substantive changes, apply Alárinà's [local readiness contract](skills/alarina/references/engineering/delivery/local-readiness.md) to the complete source and generated candidate. CI is the backstop for locally available review and checks.

## Keep changes cohesive

Consult [ARCHITECTURE.md](ARCHITECTURE.md) for ownership and build flows, and [.nongoals](.nongoals) before expanding responsibilities. Reconcile structural changes through `architect-document` and update affected reader instructions; routine wording changes need no architecture churn.

Add scripts for valuable deterministic results. Shared runtime scripts belong in `skills/alarina/scripts/`, package validators in `scripts/skills/`, and optional comparisons in `evals/`. Existing `.qp/` is ignored working state; new records follow the skill's [persistence policy](skills/alarina/references/productivity/records.md). Remove stale callers and evidence claims when retiring scripts or workflows. Preserve attribution and licences.

Use Changesets for release versioning; generated plugin versions come from `package.json`.
