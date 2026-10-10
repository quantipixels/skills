# Capture a lesson

Runs automatically at the end of solved, verified work. Usually nothing is kept, and that is the right result.

## Counterfactual bar

Keep a lesson only when: if the note vanished, a future engineer reading the final code, tests, types, comments and existing docs would still likely repeat the mistake or redo substantial investigation. Finishing, effort and diff size do not count. If a test, lint or type could enforce it, build that instead and keep no note. If the project already documents it, keep nothing.

## Write it

- Search the project's existing lessons first. Update the matching lesson rather than adding a near-duplicate.
- Otherwise write one lesson, one per file, in the lessons home. Reuse the categories already there; if none exist, choose a short one (for example `build`, `integrations`, `data`, `workflow`).
- Use the template in [lesson template](lesson-template.md). Keep it short: what happened, why the obvious reading is wrong, what to do. Cite the code or test that proves it; do not paste transcripts.
- Ship it in the same PR as the work.
- Ask nothing. Edit no skills or personal instructions; note in the report that a skill-level lesson exists and suggest a reflection.

Say in the report whether a lesson was kept or not (one line why).
