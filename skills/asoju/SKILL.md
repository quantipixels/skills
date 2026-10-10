---
name: asoju
description: Hand work to subagents - split it into slices, brief them, run them in parallel or as a race, pick each one's model and effort, then check and merge what comes back. Use when work is large or independent enough that parallel or fresh-context children pay for their briefing, or when a model must be chosen for delegated work.
---

# Aṣojú

Output: delegated work that is checked and merged into one result. You stay responsible for it.

Needs: a goal and a done check. If either is missing, or the task is not delegation (a question, one small edit), return it and say what is missing.

## Method

- Delegate when slices are independent, a fresh context helps, or an independent view is needed. If the briefing costs more than the work, do it yourself.
- Split into vertical slices as `seda-ticket` defines them (wide refactors are its exception); order slices into phases when one needs another's output. A wide refactor gets one writer, or phases with a lead who owns the merge.
- Before running two slices at once, check they do not share files, types or schemas, migrations, generated files, lockfiles, or a single resource (database, server, browser, device). Different file names do not prove safety. If they overlap, run in order or give one owner.
- Give each child its own worktree or output path. The lead owns integration and the final checks.
- Brief so a stranger could do the work, with checkpoints; see [brief and race](references/brief-and-race.md). When the shape is unsettled, race two or three candidates from one brief (same file); never race routine work.
- Pick each child's model and effort from [models](references/models.md). When a row is your own model, do the job yourself unless it needs independence from you, would flood your context, or must run alongside other work.
- Before a long task, or any child that must read a lot (a long thread, a large repo, many docs or logs, past sessions, PR history), have a cheap reader write a positioned record first and give that record to the expensive models; see [reader records](references/reader-records.md). For other splits between cheap and expensive models (explore and explain, investigate and synthesize, race with a cross-judge, panel review, lens fan-out, gauntlet or swarm, hillclimb, scripted runs), see [model workflows](references/model-workflows.md).
- Run what can run at once: 3 children by default, one level deep (children do not delegate). Keep a roster: who does what, what each owns, and what goes next so a free slot never sits idle. When a child finishes and a next task fits its context (same area, same files), give it that task instead of starting fresh.
- At each launch, set a host wake-up (SIGIDI task wake or scheduler, Claude Code wake-up) for 45 minutes or less, and write the launch time and next check time in the roster. Memory is not a timer. At each wake, read the child's report file: empty or unchanged since the last check is a stall, so redirect or stop it. On Claude Code, mind the prompt-cache limit.
- A launch is not a result. Collect the return, then check the diff and the evidence yourself. A missing slice is a gap, not a pass. Retry a bad result once with a sharper brief, then do it or ask.
- Review is yours. When your own model wrote the work, send review to the `independent` row as a fresh task each round, carrying the original brief, earlier findings and your answers.

## Done

Every child's result is collected and checked against its done check, overlaps are merged, and the final checks pass on the merged work.

## Return

The merged result, with per-child outcome, requested and served model, what is not done, and open questions.
