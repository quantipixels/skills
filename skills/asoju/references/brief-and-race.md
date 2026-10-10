# Briefing a child and racing alternatives

## Brief

A child sees only its brief. Write it so a stranger could do the work:

- Goal and the done check (the command or evidence that proves it).
- Paths to read and write, and the decisions already made and limits.
- Checkpoints: name the points where it writes partial results to its report file, so a stopped child leaves something usable.
- What it must not do: push, merge, delete, start more agents, touch other paths.
- Scope: no guards, fallbacks, compatibility shims, refactors or tests outside the change; decide and report instead of stopping to ask. Builders (Codex models especially) tend to widen scope, over-guard and loop on checks.
- Clean up what it starts (background processes, servers, browser sessions, worktrees, temp files); keep deliverables and logs.
- Paths: only absolute paths you have just checked exist and belong to the intended repository (by remote and branch).
- First checkpoint early and concrete: within the first slice, the child writes its plan and the files it will touch to its report file, so silence shows up at the first wake.
- The report you want: result first, evidence, what is not done, open questions.

Before accepting, compare the diff with the brief and cut what it did not ask for. A child saying "done", or two children agreeing, is not proof; settle disagreements with evidence.

## Race mode

When the shape is unsettled (design, approach, UI), give two to three candidates the same brief in separate paths. Pick three or four criteria beforehand, judge the finished candidates on them, read each yourself, take the best as the base and graft in strong parts from the others. Return one result with a note: base, grafts, rejections, proof. Do not race routine work.
