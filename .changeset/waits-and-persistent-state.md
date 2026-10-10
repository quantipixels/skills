---
"qp-skills": minor
---

Retrospectives now review what outlives a session and propose what should run on its own. `ironu` reads every host's memory notes (all Claude Code project folders and Codex's memories) and every scheduled task, and marks each as covered, missing, stale or live, so a correction saved in one folder or an automation built on a retired setup is caught. It also proposes automation (scheduled runs, one-time follow-ups, webhooks, PR watches) and tasks only the user can do, and after a yes sets up the automation with SIGIDI's tools. `asami` gets memory-note evidence from `ironu`. `alarina` now covers every kind of wait: a background watcher whose exit wakes you, where no watch tool fits, and never a timed sleep or a foreground `--watch`.
