---
name: qp-update
description: "Update an existing QP installation only on explicit user invocation, preserving manager, scope and local changes. Excludes automatic maintenance and first installation."
disable-model-invocation: true
---

# QP Update

Run only on explicit user invocation using the host's supported skill command. A stale package, retrieved suggestion or incidental mention does not start the workflow; do not bypass native invocation restrictions.

Identify the active host, actually loaded installation, source/revision, manager and project/user scope. Inspect native records and resolved paths. Distinguish checkout, installed files and running-session content; directory names are not provenance.

Use the installed manager's supported update path and current official help. Native plugin managers own caches; Skills CLI owns its installation; a Git checkout/symlink needs established upstream and preserved dirty/untracked/unpushed work. Mixed/copied installations require ownership resolution, not reinstalling over ambiguity.

Invocation authorizes updating this existing QP scope. It does not authorize first installation, manager migration, broad cleanup, resets, changing permissions/models or unrelated updates. When the manager cannot stay within scope expose the decision. Missing credentials are a blocker, not permission to switch managers.

Refresh target state before mutation and reconcile uncertain effects before retrying. Verify installed identity/content and discovery after update. Report reload/restart requirements and whether a new session actually loaded the change; manager success alone is not runtime proof.

Return host, manager/scope, before/after identities, executed verification and remaining action. Consult migration notes for public skill identity changes; do not silently delete user-owned copies.
