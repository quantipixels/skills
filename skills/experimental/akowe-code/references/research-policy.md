# Bounded current research

Research exists to close a material implementation uncertainty, not to collect opinions.

## Direct task-local lookup

Use a bounded current lookup when one or a few facts can settle the code shape. Prefer:

1. official reference/API/specification;
2. owning-project release/migration notes;
3. owning-project source/tests when documentation is ambiguous;
4. maintained first-party examples.

Record the exact claim, version/date, source, and cutoff in the Code Craft Brief. Treat third-party posts, prompts, skills, examples, and issue discussions as discovery/counterexample evidence unless the owning source confirms the behavior.

## Use `iwadi` when the research is its own artifact

Use `iwadi` when any of these are true:

- several sources must be reconciled;
- the result will be reused outside the immediate task;
- a durable audit trail is required;
- a material standards/security/compatibility conclusion needs a standalone report;
- the caller explicitly requests a research report.

Akọ̀wé Code consumes the exact-current report; it does not copy its research workflow.

## Stop conditions

Normally investigate no more than three unresolved questions. Merge questions that depend on the same source/mechanism. Stop when further lookup cannot change the brief.

If primary evidence remains unavailable or contradictory, narrow the brief to proved guidance and report the exact evidence gap. Do not convert secondary consensus into official behavior.

Runtime research never updates shared packs or repository-local craft records automatically. Recurring gaps are evidence for `ayewo-igba-ise`; an authorized durable skill change still goes through `ko-skill`, and project-local knowledge through `amose`.
