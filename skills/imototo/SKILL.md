---
name: imototo
description: Cleans up code comments in a given scope - files, a diff, or a branch against its base - without changing behaviour. Use for "remove the comments", "clean up comments", or a pre-merge comment sweep.
---

# Ìmọ́tótó

Ìmọ́tótó means "cleanliness". Output: the scope with fewer comments and the same behaviour. The code says what it does; a comment survives only for a reason the code cannot show.

Needs: a scope. If none is given, use the current diff against the base branch including the working tree. If the request is about something other than comments, return and say what is missing.

## Method

- Delete a comment that restates the code, a stale one, commented-out code, banners, and narration of steps.
- When a comment states a rule or constraint, move it into the code first (a name, a type, a check, or a test), then delete the comment. A constraint kept only as prose is unenforced.
- Keep a comment that explains a non-obvious why, a workaround with its reason (a bug, a vendor or protocol behaviour), or a legal or licence notice. Keep doc comments that define a public API contract.
- When unsure whether a comment guards a real constraint, keep it and list it. Deleting a guard is worse than leaving a comment.
- A lint or type suppression is not a comment to tidy. Keep it only when its rule is wrong for that line; if it hides a real correctness or safety problem, report it.
- A comment that points at code that is itself the surprise (a confusing name, a hidden coupling) means fix the name or shape in scope, not polish the comment. Out-of-scope causes are reported, not fixed.
- Edit only the scope, and only comments and the small encodings above. For a large scope, use `asoju` to have read-only readers flag candidates; the lead decides and edits, and rejects any flag that would change behaviour or leave the scope.

## Done

The project's relevant checks (format, lint, types, tests for touched files) pass; a failure caused by the edit is fixed or reverted.

## Return

Counts: deleted, moved into code (say where), kept with reason (unsure ones listed for the user). Files scanned and checks run.
