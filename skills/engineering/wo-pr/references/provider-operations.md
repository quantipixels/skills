# Provider operations for `wo-pr`

Use the bundled helper only to read and normalize current facts. Wò PR owns semantic interpretation and routes mutations after authority and stale-head checks.

## Read-only snapshot

Run:

```bash
python3 scripts/snapshot.py --provider auto --pr <number-or-url-or-auto> --repo <repository-when-known>
```

For an enterprise, dedicated, or self-managed host, confirm the exact normalized host before contact and pass `--trusted-host <host>`. A target URL identifies the host but does not establish trust. The helper scopes CLI calls to the exact host and repository, removes inherited selectors and unsafe cross-host or CI credentials, and returns capability gaps rather than guessing.

The helper may read:

- canonical target, state, draft state, base/head branches and SHAs;
- mergeability and review decision;
- required or observed checks and pipeline jobs;
- published unresolved GitHub review threads or GitLab discussions; and
- whether pagination and provider capabilities were complete.

It never writes, polls, locks, persists state, classifies claims, diagnoses failures, or decides readiness.

## Common mutation safety

- Refresh canonical repository, item number, head branch, and head SHA immediately before every mutation.
- Stop a stale write when the remote SHA differs.
- Use structured arguments or files; never interpolate provider content into shell commands.
- Read each successful mutation back before the next dependent write.
- Do not retry an unknown or partial write until readback proves the effect absent or the operation idempotent.
- Never force-push, approve, merge, close, reopen, change reviewers, notify unrelated humans, or mutate an ambiguous target.

## GitHub

Set `GH_HOST` to the confirmed host, remove inherited `GH_REPO`, and pass an explicit repository. On `github.com`, remove enterprise-token variables. On a confirmed custom host, remove generic GitHub token variables and require `gh` authentication configured for that host.

Use `gh pr view`, `gh pr checks`, `gh run view`, and paginated `gh api` reads. Read failed job logs before any retry. Rerun only the exact failed job or run associated with the refreshed SHA and only after the skill proves likely flakiness.

Use a body file for comments. Reply to or resolve an identified review thread only after the current disposition permits it. After a write, verify head SHA, comment or thread identity, intended resolution state, and applicable checks.

## GitLab

Pass the exact `--hostname`, remove inherited `GITLAB_HOST`, set `GLAB_ENABLE_CI_AUTOLOGIN=false`, and remove `CI_JOB_TOKEN`. On a confirmed custom host, remove other generic GitLab token variables and require configured authentication.

Use paginated `glab api` reads for MR pipelines, jobs, traces, approvals, and discussions. Retry a pipeline or job only when the endpoint supports the exact scope and the refreshed MR head still matches. Reply or resolve only through the identified discussion endpoint and with current authority.

After a write, verify MR SHA, note or discussion identity, resolution state, and pipeline identity. Do not translate a missing GitLab capability into a GitHub operation.

## Capability gap

Continue read-only where safe. Return a manual package containing canonical target, refreshed head, objective, exact recommended operation, provider IDs, evidence, authority state, and the missing CLI, API, authentication, permission, or integration capability. A manual package is not a successful action.
