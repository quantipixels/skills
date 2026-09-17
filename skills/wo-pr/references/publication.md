# Publication

Create or update the PR/MR for the requested work. A request to create a PR authorizes the scoped commit, push, and publication. Use the existing repository context to finish the job.

Verify the target and any uncertain provider write before retrying.

1. Reuse the scope and branch's existing PR/MR. Create a feature branch if needed; use the established integration branch or specified stack parent as the base. Ask only when the target is ambiguous.
2. Preserve unrelated work, commit coherent changes, and push normally. Resolve in-scope conflicts; history rewrites, force-pushes and hook bypass need separate authority.
3. Read [reviewer brief](reviewer-brief.md) and compose or refresh the body against the candidate being published. Reuse valid proof; make missing or stale evidence visible rather than manufacturing it.
4. Create or update the PR/MR, ready by default unless draft was requested. Preserve human content, templates, base, and state unless their change is authorized. Do not publish an empty diff.
5. Read back the published head, base, state and body. Check that the brief describes that candidate, preserves human content, and exposes its material evidence gaps and risk. Verify evidence-link accessibility when possible; report unresolved access rather than treating a local path as an attachment.

Return the URL and any material gap. Publication, provider readiness, independent review, approval and merge remain distinct.
