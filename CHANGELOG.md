# Changelog

## 0.2.0

### Minor Changes

- [#3](https://github.com/quantipixels/skills/pull/3) [`bb8974c`](https://github.com/quantipixels/skills/commit/bb8974cfab076a302510d55ddf3bacbfbdf04e4a) Thanks [@mosobande](https://github.com/mosobande)! - `asoju`'s briefs now keep children to the change (no extra guards, shims, refactors or tests; decide instead of stopping to ask), make them clean up what they start, and have the lead cut anything the brief did not ask for. These rules moved from agent-setup's instruction templates, which no longer carry them. Runbooks (deploy, backup, restore, observability) now have a default home, `docs/internal/operations/`.

- [#1](https://github.com/quantipixels/skills/pull/1) [`270536f`](https://github.com/quantipixels/skills/commit/270536fb89b654b71354d3e261e9b71f8d512e09) Thanks [@mosobande](https://github.com/mosobande)! - Retrospectives now review what outlives a session and propose what should run on its own. `ironu` reads every host's memory notes (all Claude Code project folders and Codex's memories) and every scheduled task, and marks each as covered, missing, stale or live, so a correction saved in one folder or an automation built on a retired setup is caught. It also proposes automation (scheduled runs, one-time follow-ups, webhooks, PR watches) and tasks only the user can do, and after a yes sets up the automation with SIGIDI's tools. `asami` gets memory-note evidence from `ironu`. `alarina` now covers every kind of wait: a background watcher whose exit wakes you, where no watch tool fits, and never a timed sleep or a foreground `--watch`.

## 0.1.0

First release of qp-skills from a clean history. Earlier versions are retired.
