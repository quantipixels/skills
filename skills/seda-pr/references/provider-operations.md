# Provider operations for `seda-pr`

Read this reference after `SKILL.md` resolves the provider, repository, and new or existing publication target, and before any provider read or write. Prefer authenticated provider CLIs. Use structured arguments or JSON input; never interpolate provider text into a shell command.

## Common preflight

1. Resolve the canonical provider host and repository from explicit input, then one unambiguous Git remote.
2. Verify authentication without reading or printing credentials.
3. Resolve the repository default branch, current remote head SHA, candidate base SHA, and open same-head/same-base items.
4. Fetch the complete target-to-head diff and detect provider truncation or missing pages.
5. Refresh head identity immediately before each dependent write.

Never create a duplicate or draft, force-push, infer a write target from ambiguous remotes, or use an older generated body after the head changes. Before provider contact, reject every creation command or payload that uses a draft flag, `draft=true`, a `Draft:` or `WIP:` title convention, a draft template, or a provider default that is not confirmed ready for review.

A target URL does not establish host trust. Resolve the absolute path to `scripts/provider_cli.py` from the installed `seda-pr` skill directory that owns this reference. Never resolve the helper from the current working directory, `PATH`, or the target checkout. Run every `gh` or `glab` command in this reference through `python3 <absolute-helper-path> --provider <github|gitlab> --host <host> -- <command>`. Select the declared host in each command through `--hostname`, a host-qualified repository selector, or a GitHub `--repo owner/repository` value combined with the helper's pinned `GH_HOST`; do not rely on a positional URL or content field for host selection. The helper rejects commands whose host cannot be verified. It removes host-selection overrides and generic provider tokens before it contacts an untrusted host. For an administrator-confirmed enterprise or self-managed host that depends on generic token environment variables, add `--trusted-host <host>` before `--`. Do not bypass the helper for authentication checks, reads, writes, pagination, REST, or GraphQL.

## GitHub

Through the host-trust helper, use `gh auth status --hostname <host>`. Use `gh repo view`, `gh pr list`, `gh pr view`, `gh label list`, and paginated `gh api` reads for identity, default branch, current narrative, files, labels, reviews, and linked issue context.

Create a ready PR with `gh pr create` and a body file. Never pass `--draft` or a draft API field. Reconcile title/body and existing labels with `gh pr edit`. Use the REST or GraphQL API only when the normal command does not preserve the required semantics. Reviewer requests and assignments are separate notification capabilities. Read review-thread state through GraphQL when resolution identity matters.

After a write, read the PR by canonical number and verify URL, state, base, head branch, head SHA, title, body, labels, and any requested people. GitHub closing keywords can close linked issues when the PR merges; require the separate authority defined by `SKILL.md`.

## GitLab

Through the host-trust helper, use `glab auth status --hostname <host>`. Prefer `glab api` for exact project and MR semantics. URL-encode the project path when addressing `/projects/{project}`. Read the project default branch, merge requests filtered by source and target branch, MR details, changes or diffs, labels, discussions, approvals, and linked issues through paginated endpoints.

Create through `POST /projects/{project}/merge_requests` with source branch, target branch, title, description, and explicit `draft=false`. Do not use a `Draft:` or `WIP:` title prefix. Reconcile through `PUT /projects/{project}/merge_requests/{iid}`. Apply only existing labels. Reviewer and assignee fields notify or attribute people and require their own authority.

After a write, read the MR by IID and verify web URL, state, source and target branches, head SHA, title, description, labels, draft state, and intended people. Preserve GitLab-specific merge rules and closing semantics instead of translating them into GitHub terms.

## Partial capability or failure

Continue read-only when safe. Return a manual package containing canonical target, refreshed SHA, exact intended field changes, preserved human content, labels, people, issue effects, and the missing authentication, permission, CLI, API, or integration capability. A manual package is not proof that a write occurred.
