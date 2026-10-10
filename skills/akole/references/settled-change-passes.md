# Passes on a working change

Two optional passes, run only after the change works and its proof passes. Neither is an independent review.

## Simplify

Use on a settled recent change when the diff is large enough to hide waste. Skip it for a tiny diff, a document, or code that is only moved.

Look in the changed code for three things:

- **Reuse.** An existing helper, type, constant or pattern that already does this. Extend the owner instead of adding a twin.
- **Quality.** Needless state, indirection, copies, dead branches, names that mislead, comments that only restate code.
- **Efficiency.** Repeated work, extra passes, avoidable round trips or allocations on a path that runs often.

Apply only changes that clearly help. Keep behaviour exactly: results, errors, ordering and side effects. Keep safety checks, validation, guards and accessibility, even when they look wordy. Fewer lines is not a reason. Rerun the affected checks after the edits. For a large diff, split the three looks across subagents; for a small one, do it yourself.

## Polish

Use when a feature works and the user wants it to feel right, and they are looking at it. Their observations drive the work, not your own audit.

- Get the running page or screen up where the user can see it, and ask for what they see: spacing, wording, motion, states, flow.
- Turn each observation into a small fix, apply it, and let the user look again. Keep the loop short.
- Stay in the feature. Note unrelated problems for the end instead of fixing them.
- Check the states a user can reach: empty, loading, error, long text, keyboard, small screen.
- Do not install tools or set up capture services for this unless the user agrees.

Finish with what changed, what is left, and the URL or command to see it. Do not open a PR unless asked. Browser checks use the project's verification skill if it has one, else the host's browser tool.
