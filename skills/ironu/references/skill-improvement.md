# Improve skills from a session

Use in Reflect mode, when the user asks to reflect on a session, or to turn what went wrong or right into changes to skills, instructions or tooling. The output is a list of proposed changes the user approves one by one. Nothing changes before that approval.

## Gather findings

Read the session itself (on SIGIDI: `t3_thread_read` on the current thread; elsewhere the host transcript). Do not read other projects' or unrelated threads. When the session is long, do not write the digest yourself: a cheap reader (see `asoju`'s reader records) writes a positioned session record (every user turn, corrections, failures, delegations, reversals, open items, coverage note), and reviewers work from it, spot-checking the thread only for gaps the record names.

For a substantial session, run three independent delegated reviewers in parallel, each with a self-contained brief (thread id or the session record, read-only, no subagents, numbered findings back). Give them the same evidence and, where the host allows, split them across providers:

- **Judgment:** the durable principle behind a correction or mistake.
- **Tooling:** commands, flags, paths and host quirks a future agent would otherwise rediscover, and every time the user supplied context the agent could have fetched itself.
- **Blind spots:** what worked for the wrong reason, checks that were self-reported instead of verified, second-order effects, and skills that should have triggered but did not.

Each finding names the principle in one sentence, the moment in the session that shows it, and the skill or file it would change. For a short session, do the three passes yourself.

## Judge each finding

Accept a finding only when all of these hold:

- it will still be true after paths, versions and code shapes change;
- a future agent would act differently because of it, not just read more;
- it points at a skill, tool or instruction this session actually used, or at a skill that should have triggered (then the fix is its description);
- the target does not already say it clearly (if it says it weakly, propose a wording or placement fix instead of a duplicate);
- a test, lint, script or check cannot enforce it more reliably. If one can, propose that mechanism instead of prose.

Findings two reviewers reached independently carry more weight. Reject one-offs, platitudes and pinned details (SHAs, byte counts, today's file paths).

## Propose, then apply

Give each accepted finding one home by who it is about, as in SKILL.md: a check, project docs, the user's defaults or their own stack or organisation skills. A project-docs lesson is written as in capture and needs no approval; the other homes do. A finding about how an agent works anywhere is listed as a suggestion for the skill's maintainers, not applied.

Show the user three lists: **Accepted** (problem, proposed change, target file and section), **Rejected** (finding and the rule it failed), and **Backlog** (mechanisms worth building later). Apply only the rows the user approves, handing skill text and the user's defaults back to the caller to write. Keep each skill within its host limits, and run the package's validator after editing.

A change to how a skill steers agents needs end-to-end proof before it ships: give fresh agents (on the models set for tests) the edited skill and a disposable repository that tempts the old failure, then check what they did in the repository, not what they reported.
