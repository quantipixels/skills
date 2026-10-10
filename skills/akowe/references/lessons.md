# Keeping lessons true

Lessons are docs. This is the audit of the project's lesson store (and, on request, the user's own local skills) against current code, tests, docs and skills. A lesson a skill update now covers is obsolete. A lesson stored outside its project that names a client, host or other identifying detail is flagged. Freshness is evidence, not age.

## Check

For each lesson (or the scoped subset), compare its claims with the current code, tests and docs. Classify as:

- current: leave it;
- drifted: the facts changed but the lesson still matters; fix it in place;
- duplicate or overlapping: merge into one, keep the better-evidenced file;
- contradicted: two lessons, or a lesson and the code, disagree. Flag these first, with both sides, before any other edit;
- obsolete: the code, tests or docs now make it obvious, or the thing it described is gone.

## Act

Fix drift and merge duplicates directly, and say what changed. Flag contradictions for the user. Report an obsolete lesson that is still accurate; delete it only when the user asks for a cleanup. Delete a lesson that is wrong or about code that no longer exists, and say so.

When the store is large, search by the task's terms and symptoms rather than reading everything. Report counts per class and the files touched.
