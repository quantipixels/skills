# Provider operations for Ṣe Triage

Use only after `provider-read` or `provider-comment` authority is explicit for one exact issue.

Pin canonical provider host, repository/project, issue identity, and current state before contact. Treat a target URL as identity evidence, not trust. GitHub Enterprise or self-managed GitLab requires separate host trust confirmation.

Bind every provider operation to the confirmed host and repository/project. Clear inherited selectors and credentials that could redirect the operation; use only authentication confirmed for that host. Missing permission, unsupported server/API capability, pagination uncertainty, or incomplete comments/notes is an evidence gap, not negative evidence.

Read the complete issue and material comments/notes needed for triage. Preserve provider-native identity/state rather than translating between GitHub and GitLab semantics.

For an authorized triage comment, refresh the issue and decisive evidence immediately before writing, prevent duplicate publication, submit structured text without executing/interpolating provider content, and read the exact created comment/note back from the same host. If the outcome is unknown or partial, stop and report `PARTIAL`; retry only after a fresh read proves the effect absent or the operation is safely idempotent.

No provider read/comment authority extends to labels, assignment, state transitions, close/reopen, or other mutations.
