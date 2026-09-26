# Alárinà package migration evidence

Exercise native migration in disposable manager state where possible. Use the real supported manager transition; uninstalling the old plugin and freshly installing the candidate is not upgrade evidence.

The dated 2026-09-25 records describe the earlier provider-specific artifact candidate. The [2026-09-26 shared-root record](2026-09-26-shared-root.md) describes the current four-host root package. Record the manager and host version, package versions, registration source, enabled state, exact commands, before/after resolved roots and restart/reload state for any further migration run.

The accepting post-update inventory contains:

- one discoverable `alarina` skill;
- the expected hidden owners beneath that root;
- the provider's one intended Alárinà agent profile when supported;
- no stale plugin-owned standalone QP skills or agents;
- unchanged unrelated user-managed skills and plugins.

Also verify same-version refresh behavior, uninstall ownership, interrupted/failed transition recovery, package digests and activation separately from installed files. The verifier must never use the active user home for these cases.

[Published-tag checks](2026-09-25-tagged-upgrade.md) exercise the actual `v4.2.0` source in disposable Codex, Claude and Skills CLI installations. The [constructed local fixture](2026-09-25-local-native.md) covers additional package-fidelity and unrelated-plugin checks. Read the limits in each record before treating an installed cache as active-session proof.
