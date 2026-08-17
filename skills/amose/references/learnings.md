# Maintain `.learnings`

Use one optional root `.learnings` file for durable, non-obvious knowledge that can change future implementation, review, debugging, operation, or design work. It may contain rules, patterns, conventions, constraints, architectural nuances, operational knowledge, and gotchas. Keep canonical domain terms, definitions, semantic relationships, and context boundaries in the project's existing domain-language record or the applicable `CONTEXT.md`; do not duplicate them here.

Preserve an existing human-readable format. Create the file lazily only when useful knowledge exists and creation is authorized. With no existing format, use lightweight Markdown and include only sections with content.

Require evidence from a confirmed decision, current code, test, configuration, runtime result, ADR, or established repository practice. `.learnings` cannot serve as its own sole proof. When no independent current evidence supports an entry, mark it unverified or remove it instead of perpetuating it.

Keep hypotheses, temporary task state, session history, speculative preferences, obvious code facts, secrets, credentials, and personal data out. Require user or confirmed-decision authority before promoting observed behavior into a business rule, project boundary, or architecture decision.

Keep the file current rather than append-only. Re-read it immediately before writing, make the smallest semantic edit, merge duplicates, replace stale entries, and retain a short supersession or `avoid` note only when it prevents likely recurrence. Remove obsolete detail and use ADRs for consequential rationale. On concurrent or conflicting edits, stop for semantic reconciliation; never overwrite or blindly append.

Compact relevant sections when repetition or stale material impairs use. Do not impose an arbitrary size limit. Consumers may read only relevant sections; passive reading does not require invoking Amọ̀ṣẹ́.
