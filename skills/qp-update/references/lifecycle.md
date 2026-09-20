# Lifecycle and activation

Use after the one-time procedure refresh. The manager owns mutation; this reference supplies lifecycle decisions and accepting evidence.

## Reconcile the update unit

Compare the complete source inventory with the installed, owned selection using discoverable `SKILL.md` identities, not directory counts. Distinguish revisions, retirements, available additions, same-identity moves, documented replacements and conflicts. Without a historical baseline, call an absent local skill *available*, not necessarily *new*.

| Installation | Update boundary |
| --- | --- |
| Native Codex or Claude plugin | Update the registered source and installed package. Ordinary internal additions/removals follow the bundle; narrower instructions or changed permissions still control. Preserve identity, scope, targets and enabled state. |
| Skills CLI | Update only the installed QP selection in its existing scope/placement. Check the installed CLI's filtering and side effects: a named update can still affect other host targets or source-wide retirement prompts. Resolve unsupported scope before running it. |
| Editable Git checkout or symlink | Establish upstream and active consumer before a non-destructive update. Preserve dirty, untracked and unpushed work. Updating a checkout does not create missing individual skill links; whole-directory discovery differs from individual symlinks. |
| Copies, mixed owners or unknown provenance | Establish ownership before mutation; do not reinstall over ambiguity or take over another manager's files. |

Honor evidenced future-all intent, but do not infer it from a past `--skill '*'`, matching names or counts. Otherwise retain the selection and surface additions. Use manager records and applicable user instructions, not a new installation-state database.

Confirm retirement from a complete inventory at the correct source/ref. Network failure, truncation, a missing path or ambiguous relocation is not retirement. Resolve same-identity moves first. Recognize replacements only from explicit upstream evidence, not name similarity.

For separate CLI copies, updating is not blanket deletion authority. Reuse an approved removal or obtain that decision; remove only an owned, unmodified copy through the manager. Noninteractive updates may skip retirement even with `--yes`: inspect the result and use a supported scoped removal when authorized. Preserve modified, foreign or ambiguous copies; skipped removal is not full reconciliation.

For authorized, separable replacements, install and verify the replacement before removing the old copy. On failure, retain the old skill and report partial work. Indivisible bundles use the manager's actual guarantees, not invented staged replacement or rollback. Report obsolete explicit references in user instructions; edit them only when authorized.

## Apply and recover

Refresh target and local-change evidence before mutation. Do not overwrite a modified updater to obtain fresh instructions. Check whether marketplace refresh also changes unrelated packages or disabled state; QP approval does not cover unrelated effects.

After interruption or an ambiguous result, inspect actual effects before retrying. Preserve successful work and unresolved conflicts in the existing task record. Use supported recovery within authority, never a blind reset, cache patch or custom transaction.

## Activate the actual consumer

Verify installed content and intended membership, including updater references and replacements. Confirm preserved pins, scope, placement, enabled state and local work. Detect stale copies in other discovery roots without deleting unrelated installations.

Prefer activation the host already performs. If discovery remains stale, use only a documented facility exposed by the installed client. A command requiring direct user input is a remaining action, not an executed reload.

| Surface | Activation boundary |
| --- | --- |
| Codex local skills | Use native detection. If already exposed by the active app server, `skills/list` with `forceReload: true` refreshes discovery; this is an API call, not a slash command. Restart if the supported refresh leaves discovery stale. |
| Codex plugin | Use the installed client's plugin activation path. Local-skill watching is not proof of package reload; give its restart instruction when no usable reload exists. |
| Claude plugin | Check whether already active. Otherwise use `/reload-plugins` in the actual session where supported, or report the required user action/restart. Respect surface/version limits and prompt-cache warnings; do not automatically use `--force`. |
| Claude local skills | Use supported watching and reread changed instructions/references. A file update does not replace existing conversation content; a fresh session may remain necessary. |

Check exact identities and resolved paths in that consumer. A successful command, equal counts or a second process does not prove original-session activation. Reread the installed updater and affected references without bootstrapping again; reconcile a material difference from the inspected procedure under the original authority. Never reinvoke the side-effecting updater just to test discovery. Report missing live-host evidence and concrete pending activation separately from verified files.

## Current interfaces

Resolve syntax and capabilities from installed help and current first-party guidance:

- [Skills CLI](https://github.com/vercel-labs/skills): selected updates and removal.
- [Codex skills](https://developers.openai.com/codex/skills), [app server](https://developers.openai.com/codex/app-server), and [plugin packaging](https://developers.openai.com/plugins/build/plugins): discovery and package refresh.
- [Claude plugins](https://code.claude.com/docs/en/discover-plugins) and [skills](https://code.claude.com/docs/en/skills): activation and instruction lifetime.
