# Local native migration observation — 2026-09-24

Historical observation of the earlier owner-snapshot candidate. Its 112-file counts and fourteen hidden-owner layout do not describe the later 38-command source consolidation. Current-candidate verification must be reported separately.

This bounded check used disposable manager state and a local marketplace fixture. Version 4.2.0 exposed two standalone skills (`alarina` and `alaga`) from the marketplace root. Version 4.3.0 moved the same `qp-skills` identity to the provider subdirectory and exposed one Alárinà skill with hidden owner snapshots.

| Host | Manager | Observed transition | Installed result |
| --- | --- | --- | --- |
| Codex | `codex-cli 0.156.1` | `codex plugin add qp-skills@qp-skills-migration --json` advanced 4.2.0 → 4.3.0 after the local marketplace changed | enabled 4.3.0 package from `plugins/codex/qp-skills`; one `SKILL.md` and fourteen `OWNER.md` files |
| Claude Code | `2.1.263` | `claude plugin marketplace update` followed by `claude plugin update ... --scope user --yes` reported 4.2.0 → 4.3.0 | enabled 4.3.0 package; `plugin details` reported one skill and one agent |

The active registered package on each host points at the new version and contains no standalone specialist `SKILL.md`. The snapshot verifier matched all 112 installed files to the final provider artifact on each host and observed the inventory change from `alaga, alarina` to `alarina`. Claude reported that restart is required to activate the update. Codex local marketplaces do not support `marketplace upgrade`; the subsequent `plugin add` read the changed local source and installed 4.3.0.

This establishes the local manager transition and resulting inventory for the fixture. It does not establish Git-backed marketplace refresh, same-version refresh, rollback after interruption, preservation of unrelated packages, uninstall ownership, model selection, owner-file loading, or activation in an already-running session.
