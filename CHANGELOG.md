# Changelog

## 0.3.0

### Minor Changes

- [#4](https://github.com/quantipixels/skills/pull/4) [`0dce92d`](https://github.com/quantipixels/skills/commit/0dce92dcb6ff1f7d7ce5064aba551e28f92a4e4a) Thanks [@mosobande](https://github.com/mosobande)! - Retrospectives and clean-ups get five fixes from a recent reflection. Session readers now count every message that rejects, undoes, redirects, renames or repeats an earlier instruction as a correction, however politely put, and mark a session's coverage complete once every user message was read. `alarina` notes that a build or test piped through `grep`, `head` or `tail` reports the filter's status, not the command's. Clean-up now removes without asking only what is clearly safe (regenerable or already preserved elsewhere), lists everything else with its reason until you say yes, and prefers Trash or a backup to deleting. `ironu` proposes the strongest fitting remedy for each recurring pain point (a check or hook, a tool to install or custom tooling built for you, a skill, a line in your defaults or instructions, automation, a task for you, or a combination) with the evidence and why it beats weaker options.

## 0.2.0

### Minor Changes

- [#3](https://github.com/quantipixels/skills/pull/3) [`bb8974c`](https://github.com/quantipixels/skills/commit/bb8974cfab076a302510d55ddf3bacbfbdf04e4a) Thanks [@mosobande](https://github.com/mosobande)! - `asoju`'s briefs now keep children to the change (no extra guards, shims, refactors or tests; decide instead of stopping to ask), make them clean up what they start, and have the lead cut anything the brief did not ask for. These rules moved from agent-setup's instruction templates, which no longer carry them. Runbooks (deploy, backup, restore, observability) now have a default home, `docs/internal/operations/`.

- [#1](https://github.com/quantipixels/skills/pull/1) [`270536f`](https://github.com/quantipixels/skills/commit/270536fb89b654b71354d3e261e9b71f8d512e09) Thanks [@mosobande](https://github.com/mosobande)! - Retrospectives now review what outlives a session and propose what should run on its own. `ironu` reads every host's memory notes (all Claude Code project folders and Codex's memories) and every scheduled task, and marks each as covered, missing, stale or live, so a correction saved in one folder or an automation built on a retired setup is caught. It also proposes automation (scheduled runs, one-time follow-ups, webhooks, PR watches) and tasks only the user can do, and after a yes sets up the automation with SIGIDI's tools. `asami` gets memory-note evidence from `ironu`. `alarina` now covers every kind of wait: a background watcher whose exit wakes you, where no watch tool fits, and never a timed sleep or a foreground `--watch`.

## 0.1.0

First release of qp-skills from a clean history. Earlier versions are retired.
