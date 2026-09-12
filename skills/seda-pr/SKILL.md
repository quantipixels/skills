---
name: seda-pr
description: Commit the requested work, push its branch, and create or update a GitHub PR or GitLab MR.
compatibility: Requires Git and trusted authenticated provider access through a connected interface or gh/glab.
---

# Ṣẹ̀dá PR

Create or update the PR/MR for the requested work. A request to create a PR authorizes the scoped commit, push, and publication. Use the existing repository context to finish the job.

1. Check the scoped diff, branch, remote, base, and any existing PR together. Preserve unrelated work. Use the established integration branch unless a different base or stack parent is specified; ask only when the target is ambiguous.
2. Commit the requested changes and push normally. Create a branch if needed. Resolve conflicts within the authorized scope. Do not bypass hooks, rewrite history, or force-push without separate authorization.
3. Reuse the branch's open PR or create one, ready by default unless draft was requested. Write a concise title and description of the final change and checks actually run. Preserve human content, templates, labels, and an existing PR's base and state unless a change is authorized. Do not publish an empty diff.
4. Verify the published head matches the commit and the PR has the intended base and state. Return its URL and any material gap.


