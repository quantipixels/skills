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

## PR description

Write for a reviewer with no prior knowledge of the PR or product. Briefly explain the relevant product behavior and terms so they can understand the problem and why it matters. Lead with the problem and its impact, then the resolution and a short summary of the consequential changes. Identify what to review first: critical behavior, risks, and specific files or changed lines, with links when useful. Include meaningful alternatives actually considered and why they were not chosen; do not invent alternatives or reopen investigation to fill the description. End with checks run and material limitations.

Keep detail proportional to the change. Use a few sentences for a simple PR and short sections when they help scanning. Omit empty sections, routine file inventories, and work-session narration. Follow the repository template and describe the final diff.
