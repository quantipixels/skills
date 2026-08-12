# Provider operations for `seda-pr`

Read this reference only after `SKILL.md` selects an identified GitHub PR or GitLab MR. Prefer authenticated provider CLIs. Use structured arguments or JSON input; never interpolate provider text into a shell command.

## Common preflight

1. Resolve the canonical provider host and repository from explicit input, then one unambiguous Git remote.
2. Verify authentication without reading or printing credentials.
3. Resolve the repository default branch, current remote head SHA, candidate base SHA, and open same-head/same-base items.
4. Fetch the complete target-to-head diff and detect provider truncation or missing pages.
5. Refresh head identity immediately before each dependent write.

Never create a duplicate, force-push, infer a write target from ambiguous remotes, or use an older generated body after the head changes.

A target URL does not establish host trust. Resolve the absolute path to `scripts/provider_cli.py` from the installed `seda-pr` skill directory that owns this reference. Never resolve the helper from the current working directory, `PATH`, or the target checkout. Run every `gh` or `glab` command in this reference through `python3 <absolute-helper-path> --provider <github|gitlab> --host <host> -- <command>`. The helper removes generic provider tokens before it contacts a host other than `github.com` or `gitlab.com`. For an administrator-confirmed enterprise or self-managed host that depends on generic token environment variables, add `--trusted-host <host>` before `--`. Do not bypass the helper for authentication checks, reads, writes, pagination, REST, or GraphQL.

## GitHub

Through the host-trust helper, use `gh auth status --hostname <host>`. Use `gh repo view`, `gh pr list`, `gh pr view`, `gh label list`, and paginated `gh api` reads for identity, default branch, current narrative, files, labels, reviews, and linked issue context.

Create a ready PR with `gh pr create` and a body file. Reconcile title/body and existing labels with `gh pr edit`. Use the REST or GraphQL API only when the normal command does not preserve the required semantics. Reviewer requests and assignments are separate notification capabilities. Read review-thread state through GraphQL when resolution identity matters.

After a write, read the PR by canonical number and verify URL, state, base, head branch, head SHA, title, body, labels, and any requested people. GitHub closing keywords can close linked issues when the PR merges; require the separate authority defined by `SKILL.md`.

## GitLab

Through the host-trust helper, use `glab auth status --hostname <host>`. Prefer `glab api` for exact project and MR semantics. URL-encode the project path when addressing `/projects/{project}`. Read the project default branch, merge requests filtered by source and target branch, MR details, changes or diffs, labels, discussions, approvals, and linked issues through paginated endpoints.

Create through `POST /projects/{project}/merge_requests` with source branch, target branch, title, description, and `draft=false`. Reconcile through `PUT /projects/{project}/merge_requests/{iid}`. Apply only existing labels. Reviewer and assignee fields notify or attribute people and require their own authority.

After a write, read the MR by IID and verify web URL, state, source and target branches, head SHA, title, description, labels, draft state, and intended people. Preserve GitLab-specific merge rules and closing semantics instead of translating them into GitHub terms.

## Partial capability or failure

Continue read-only when safe. Return a manual package containing canonical target, refreshed SHA, exact intended field changes, preserved human content, labels, people, issue effects, and the missing authentication, permission, CLI, API, or integration capability. A manual package is not proof that a write occurred.
