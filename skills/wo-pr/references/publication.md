
# Publication

Create or update the PR/MR for the requested work. A request to create a PR authorizes the scoped commit, push, and publication. Use the existing repository context to finish the job.

Default to `gh` for GitHub and `glab` for GitLab; fall back to the provider API when needed. Use CLI help or current docs for syntax. Verify the target and any uncertain write before retrying.

1. Reuse the scope and branch's existing PR/MR. Create a feature branch if needed; use the established integration branch or specified stack parent as the base. Ask only when the target is ambiguous.
2. Preserve unrelated work, commit coherent changes, and push normally. Resolve in-scope conflicts; history rewrites, force-pushes and hook bypass need separate authority.
3. Create or update the PR/MR, ready by default unless draft was requested. Preserve human content, templates, base, and state unless their change is authorized. Do not publish an empty diff.
4. Verify the published head, base and state. Return the URL and any material gap.

Use `oro` for a concise reviewer-facing description: problem, effect of the change, important review focus, checks run and material limitations. Follow the repository template; omit routine inventories and session narration.
