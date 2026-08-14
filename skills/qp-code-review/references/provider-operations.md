# Provider operations

Read this reference only after `SKILL.md` selects provider mode for an identified active PR or MR. Use this mapping for exact-head review, authorized publication, and discussion reconciliation. Prefer the installed provider CLI when it supplies the required semantics. Use a purpose-built connector or raw API when it is more accurate.

Derive the canonical host from the canonical PR or MR URL or an explicit repository identity. Include that host on every CLI, connector, or API operation. Never rely on the current directory, a default host, or the first authenticated account.

## Capability gate

Verify each required read capability before review. Verify each explicitly authorized write capability before publication.

| Capability | GitHub | GitLab |
| --- | --- | --- |
| Read canonical head/base | PR REST API | MR REST API |
| Read changed files/diffs | PR files/diff | MR diffs endpoint |
| Read resolved/outdated discussions | GraphQL review threads | Discussions API |
| Batch formal verdict with inline comments | Pull-request reviews API | No equivalent bundled event |
| Reply to discussion | Review-comment reply API | Discussion notes API |
| Resolve or reopen | GraphQL review-thread mutation | Discussions API `resolved` update |
| Approve exact head | Review with `commit_id` | Approvals API with `sha` |

If a required capability is unavailable because of host version, permissions, authentication, or integration coverage, record the exact gap. Continue only review work that does not depend on that capability.

## GitHub

Use `--hostname <host>` for `gh auth` and `gh api` operations. Pass the same canonical host to any connector. This supports GitHub.com and GitHub Enterprise.

1. Verify authentication with `gh auth status --hostname <host>`.
2. Read PR identity from `GET /repos/{owner}/{repo}/pulls/{number}` and pin `head.sha` plus `base.sha`.
3. Read the diff and changed files from the PR comparison, then inspect surrounding repository code locally.
4. Read submitted reviews and comments through REST. Read `reviewThreads` through GraphQL when thread ID, `isResolved`, or `isOutdated` matters.
5. Submit a review through `POST /repos/{owner}/{repo}/pulls/{number}/reviews` with exact `commit_id`, `event`, summary `body`, and current-line `comments` using `path`, `line`, and `side`.
6. Reply through `POST /repos/{owner}/{repo}/pulls/{number}/comments/{comment_id}/replies`.
7. Resolve or reopen with GraphQL `resolveReviewThread` or `unresolveReviewThread` using the review-thread node ID.
8. Read the PR again and verify head, review decision, submitted review URL, and thread states.

GitHub review events are `APPROVE`, `REQUEST_CHANGES`, and `COMMENT`. A body is required for `REQUEST_CHANGES` and `COMMENT`. Write Markdown-rich payloads to JSON and pass them with `gh api --input`.

Primary documentation:

- <https://docs.github.com/en/rest/pulls/reviews>
- <https://docs.github.com/en/rest/pulls/comments>
- <https://docs.github.com/en/graphql/reference/mutations#resolvereviewthread>
- <https://docs.github.com/en/graphql/reference/mutations#unresolvereviewthread>

## GitLab

Use `--hostname <host>` for `glab auth` and `glab api` operations. Pass the same canonical host to any connector. This supports GitLab.com and self-managed GitLab.

1. Verify authentication with `glab auth status --hostname <host>`.
2. Read MR identity from `GET /projects/{url-encoded-project}/merge_requests/{iid}` and pin `sha`, `diff_refs.base_sha`, `diff_refs.start_sha`, and `diff_refs.head_sha`.
3. Read every page from the merge-request diffs endpoint, which replaces the deprecated single-MR changes endpoint. Check response limits and each diff's `collapsed` and `too_large` fields. If any changed content remains unavailable, treat the candidate as incomplete and return `INSUFFICIENT_EVIDENCE`.
4. Read every discussion from `GET /projects/{project}/merge_requests/{iid}/discussions`; preserve discussion IDs, note IDs, positions, `resolvable`, and `resolved`.
5. Create a current-line discussion through `POST /projects/{project}/merge_requests/{iid}/discussions` with `body` and a `position` containing `position_type=text`, the three diff SHAs, paths, and the applicable old or new line.
6. Reply through `POST /projects/{project}/merge_requests/{iid}/discussions/{discussion_id}/notes`.
7. Resolve or reopen through `PUT /projects/{project}/merge_requests/{iid}/discussions/{discussion_id}` with `resolved=true` or `resolved=false`.
8. Post one top-level summary through the MR notes endpoint after inline discussions succeed.
9. Approve only with explicit authority through `POST /projects/{project}/merge_requests/{iid}/approve` and supply exact `sha`.
10. Read the MR, discussions, and approval state again to verify publication.

GitLab represents requested changes through review discussions and project merge rules. Keep blocking findings in resolvable discussions and state the verdict in the summary note.

Primary documentation:

- <https://docs.gitlab.com/api/merge_requests/>
- <https://docs.gitlab.com/api/discussions/>
- <https://docs.gitlab.com/api/notes/>
- <https://docs.gitlab.com/api/merge_request_approvals/>

## Report or publish

Without write authority, report the reviewed head, verdict, review scope, separate defect and maintainability finding counts, publication state `READ_ONLY`, discussion dispositions, capability gaps, and next action.

For each explicitly authorized write, verify that its capability and authority are current. Prepare the exact head SHA, verdict, summary, inline findings, replies, and discussion changes. Refresh the head before the first write. If it changed, do not publish stale content; return to evidence collection.

Reply to an existing discussion when possible. Use a current changed line for a new inline finding. Replace or reopen a stale discussion only when explicitly authorized. On GitHub, submit the authorized review event, comments, replies, and thread changes. On GitLab, publish discussions, replies, a summary note, and any separately authorized approval.

If an operation fails, stop dependent writes. Record each successful URL and the failed operation. Do not retry a partial mutation without a safe, verified retry path.

Fetch provider state again. Verify the current head, published verdict or approval, URLs, and intended discussion states. Report publication state as `PUBLISHED`, `PARTIAL`, or `FAILED`.

## Fallback package

When provider mode is selected and the provider or required capability falls outside this mapping, produce a manual package before requesting direction:

- pinned local and remote identities, or unavailable identity fields;
- reviewed diff boundary;
- verdict and review summary;
- each inline finding with file, side, line, body, and evidence;
- each intended reply or discussion-state change with provider ID and URL;
- unsupported operation, attempted integration, returned error, and safe alternatives.

Preserve unfamiliar provider concepts as named capabilities instead of translating them into GitHub or GitLab terms. Continue read-only where possible. Report the separate permission, authentication, integration, or manual-posting action required for unavailable operations.
