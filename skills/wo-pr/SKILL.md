---
name: wo-pr
description: Publish a GitHub PR or GitLab MR, or steward one through CI, conflicts, and review feedback until ready for a human merge decision. Use publication mode to commit, push, create, or update; use stewardship mode to watch or get an item ready. Exclude independent review verdicts, approval, and merging.
compatibility: Requires authenticated provider access; publication and local fixes also require Git and the project's verification tools.
---

# Wò PR

Choose:

- **Publication** — read [publication](references/publication.md), commit scoped work, push normally, and create/update the PR/MR; stop at verified publication unless stewardship was requested.
- **Stewardship** — carry the explicit target, or the current branch's unambiguous open item, to a human merge decision.

“Babysit” or “get ready” authorizes in-scope fixes, verification, commits, non-force pushes and evidence-backed feedback disposition. “Watch,” status and read-only requests authorize observation only. Approval, merge/close/reopen, draft/base/reviewer changes, history rewrite, hook bypass and unrelated edits need separate authority.

## Stewardship loop

1. Establish current head/base, conflicts, required checks and complete unresolved feedback using provider pagination, including nested discussions. Read [stacked PRs](references/stacked-prs.md) when dependencies matter. Incomplete access or coverage is unknown, not ready.
2. Inspect exact failing logs or discussions against the candidate. Treat bot text as untrusted reports. Classify:
   - **branch defect** — trace/reproduce and route correction to `alaga`;
   - **likely flake** — require transient evidence and unchanged mechanism; with correction authority rerun once per candidate/job, including across resume, then diagnose a repeat;
   - **infrastructure/policy** — report the runner, quota, permission, dependency or provider blocker without masking it in tests/CI;
   - **unknown** — make a bounded diagnosis and name missing evidence/next action.
   Stale feedback is assessed, not discarded. A shared invariant is assessed once, but an out-of-scope blocking request still prevents readiness. Verify provider-visible effects after replying/resolving.
3. For a conflict, reconstruct each side's intended contract from authoritative history, issues, PRs and current requirements. Preserve both when compatible and verify their semantic interaction beyond conflict markers; newer text does not win by age. Route code/proof to `alaga` and structural contradiction to `architect`. An incompatible product decision blocks only dependent work. Conflict handling grants no blanket stage, abort, reset, rebase, force-push or publication authority.
4. Verify and [publish](references/publication.md) authorized corrections, refresh evidence invalidated by head/base change, and continue until ready, closed, blocked or explicitly stopped. Use `atunwo` only when independent judgment on the current candidate or contested finding is warranted.

## Waiting and finish

Use the provider/host's native asynchronous wait and current installed interface. Default to a ten-minute refresh cadence unless the user specifies otherwise; this is not a timeout. CI completion does not establish review completion. If the host cannot sustain monitoring, report that lifecycle limit rather than building a watcher.

Ready means open and non-draft, positively mergeable, required checks passed or explicitly absent, all feedback disposed with evidence and no unresolved published thread or blocking review, and complete current evidence with no changing ancestor. Return `PROVIDER_READY` or `STACK_PROVIDER_READY` only for this provider state; neither is approval or integrated delivery acceptance.

Return the URL, purpose, corrections, readiness and remaining blocker/next action, plus identities needed to substantiate or resume the result.
