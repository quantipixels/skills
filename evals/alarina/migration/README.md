# One-entry plugin migration evidence

Exercise migration only in disposable Codex or Claude manager state. Use the real supported manager transition; uninstalling the old plugin and freshly installing the candidate is not upgrade evidence.

The before package is the current production all-skills plugin. The candidate is the provider-specific one-entry artifact. Record the manager and host version, package versions, registration source, enabled state, exact commands, before/after resolved plugin roots and restart/reload state.

The accepting post-update inventory contains:

- one discoverable `alarina` skill;
- the expected hidden owners beneath that root;
- the provider's one intended Alárinà agent profile when supported;
- no stale plugin-owned standalone QP skills or agents;
- unchanged unrelated user-managed skills and plugins.

Also verify same-version refresh behavior, uninstall ownership, interrupted/failed transition recovery, package digests and activation separately from installed files. The verifier must never use the active user home for these cases.

[Published-tag checks](2026-09-25-tagged-upgrade.md) exercise the actual `v4.2.0` source in disposable Codex, Claude and Skills CLI installations. The [constructed local fixture](2026-09-25-local-native.md) covers additional package-fidelity and unrelated-plugin checks. Read the limits in each record before treating an installed cache as active-session proof.
