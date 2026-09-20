# Native installation and upgrade evidence

`verify_native_install.py` checks fresh installation through the native Codex or Claude manager in disposable manager state. It does not invoke an AI model or prove activation in an existing session.

```bash
python3 scripts/plugins/verify_native_install.py --host codex
python3 scripts/plugins/verify_native_install.py --host claude
python3 scripts/plugins/test_verify_native_install.py
```

The unit tests exercise real temporary files and subprocess failure handling. They do not simulate a successful native update or establish model behavior.

## Check a real A → B update

Keep manager execution, installed content and session activation as separate evidence. Use disposable user/project state, the installed manager's supported source/update commands, and no personal installation or credentials. Record the manager version, source/ref, registration, scope, host targets, enabled state and commands. A local-path result does not prove Git-backed marketplace refresh behavior.

1. Prepare two complete QP package revisions: A has a skill retired in B; B has an addition and a changed updater body/reference. Equal before/after skill counts make the fixture detect count-only verification. Preserve the existing package identity.
2. Install A through the real manager. Resolve its installed plugin root from the manager's records. Save a separate **byte copy** of that root as the before snapshot, dereferencing links so the copy cannot change when the source updates.
3. Advance the same permitted source to B and run the supported update through the same registration. Do not uninstall A and install B as a substitute for an upgrade. Check that scope, tracking policy, host placement and enabled state are unchanged.
4. From the expected B checkout, run the read-only comparison below. Its `--before-root` and `--installed-root` arguments must both be supplied with one host. It never installs or updates anything in this mode.
5. In the actual consumer session, observe the host's supported discovery/reload behavior. Verify exact identities and resolved paths, read the updated procedure/reference, and record any activation still pending. Never reinvoke `qp-update` merely to check whether it is discoverable.

```bash
# Set these to the saved A byte-copy and manager-resolved installed B root.
python3 scripts/plugins/verify_native_install.py --host codex \
  --before-root "$before_snapshot" --installed-root "$installed_plugin_root"
```

Use `--host claude` for a Claude plugin. The comparison is for **whole native plugin roots**, not selective Skills CLI directories. It compares exact skill/agent membership, every updater resource, and the declared package inputs (`PACKAGE_INPUTS`) against the current checkout. It reports before/after digests and added/retired skills. Missing, foreign or aliased baselines, stale resources and mismatched package content fail with a nonzero exit.

The output deliberately says `manager_transition: not_observed` and `session_activation: not_observed`, even when the files agree. Pair it with the recorded real-manager transition and active-session observations. A manually constructed fixture, a fresh B install, or a second process is not upgrade or original-session activation proof. Freeze source and snapshots during comparison; the helper does not provide a transaction or protect against concurrent mutation.

## Targeted lifecycle checks

Use these only when exercising the changed updater boundary, not as a standing certification questionnaire. Keep proposed actions, source checks and actual execution results distinct.

| Controlled installation | Observable result |
| --- | --- |
| Native bundle A → B | One authorized package update includes its ordinary additions/retirements without another approval. Preserve disabled state and unrelated packages. |
| Selective Skills CLI, with another host and an unrelated source | Only the authorized QP selection/placement changes. Available additions are reported, not silently installed. |
| Retired CLI skill, non-TTY or `--yes` | Observe whether removal was skipped. A subsequent scoped removal needs applicable authorization; a modified or foreign copy remains protected. |
| Authorized replacement, replacement install fails | The old separate copy remains. Report the partial result; do not claim migration complete. |
| Modified updater or unavailable/truncated source | No overwrite, retirement inference or stale-procedure fallback. Preserve local state and report the exact gap. |
| Updated files, stale active discovery | Report files verified and activation pending with the supported next action; do not trust a count or a second process. |
| Source procedure B differs from installed procedure A | Read B and its references once, retain request authority, and avoid recursive bootstrap. A changed tracking branch does not silently change pins or authorize new permissions. |
| Discussion mentions `qp-update` without invocation | No maintenance action. Preserve both native explicit-invocation guards. |

Older updaters need one supported upgrade to receive the bootstrap. Exercise that first rollout separately from subsequent self-refresh. Record missing native CLIs, credentials or session access as **not run**, not as passing fixture evidence.
