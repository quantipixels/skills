# Final source-consolidation migration — 2026-09-25

Both native managers migrated a disposable local marketplace from 19 discoverable QP skills to one Alárinà skill. The installed B package matched all 134 files in the final generated artifact. An independently installed `unrelated-sentinel` plugin remained enabled and byte-identical after the update and after QP was uninstalled.

| Host | Manager | Supported transition used | Final inventory |
| --- | --- | --- | --- |
| Codex | `codex-cli 0.156.1` | `codex plugin add qp-skills --marketplace qp-skills --json` after changing the registered local marketplace | One skill; no native agent |
| Claude Code | `2.1.263` | `claude plugin marketplace update qp-skills`, then `claude plugin update qp-skills@qp-skills --scope user --yes` | One skill; one Alárinà agent |

The A fixture used the 19 skill trees from repository revision `06cbdb2282268a8b0489ad744ac2dc18ed5de918`, a root plugin manifest with version `4.2.0`, and the same marketplace/plugin identities as B. B moved the marketplace source to `plugins/<host>/qp-skills` and used the final generated `4.3.0` candidate. This is a constructed migration fixture, not an assertion that the published 4.2.0 package had these exact bytes. Manager homes were disposable; no personal installation or credentials were changed.

Each manager first installed A and the unrelated fixture. The run saved A, changed the marketplace source to B, invoked the manager update, compared B with the candidate using `verify_upgrade_snapshot`, checked the unrelated plugin, uninstalled QP, and checked that only the unrelated plugin remained registered. Successful fresh installs of the same final artifacts were also verified separately with `verify_native_install.py --host all`.

Exact candidate digests and manager command/output traces are in [the machine-readable observation](2026-09-25-native-results.json). The temporary fixture initially needed two corrections: create Codex's home directory before calling it, and obtain its installation path from `plugin add` rather than `plugin list`. Those were test-fixture errors; the final run completed on both managers.

This establishes local versioned manager transition, installed inventory, exact file fidelity, scoped uninstall registration, and preservation of the unrelated fixture. It does not establish Git-backed marketplace refresh, same-version refresh, interrupted-update recovery, old cache pruning, removal of separately installed skills, model selection, successful method execution, or activation in an existing session. Claude reports that a restart is needed. Native model activation remains a separate test.
