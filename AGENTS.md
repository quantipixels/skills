# Repository guidance

This repository packages qp-skills: independently installable skills at `skills/<name>/SKILL.md`, where the folder and the frontmatter name agree. Hosts discover skills natively; do not add a second catalogue or generated `default_prompt` metadata. Preserve invocation permissions when moving a skill.

## Packaging

A skill is installed as one folder and must work on its own:

- Whatever it needs at runtime (scripts, references, assets) lives inside it, and its links stay inside it.
- Bundled scripts run through `"$SKILL_DIR/scripts/..."`.
- It calls another skill by name, never through that skill's files, and keeps essential guidance locally even when a caller also states it.
- Every `SKILL.md` stays under 8000 bytes so Codex loads it whole; put on-demand detail in references.

Repository tooling stays outside skills: package validators in `scripts/skills/`, model comparisons in `evals/`. `check_package.py` enforces the paths, the size limit and the routing rules below.

## Architecture

- **One router.** `alarina` holds the rules every task shares (outcome, asking, building, proof, do-no-harm, SIGIDI tool use, reporting) and is the only place routing lives: its skills table and `skills/alarina/references/workflow.md`.
- **Single-job workers, one owner per kind of output.** A worker's description says what it produces and when it applies, and names no other skill. Its body states its output, what it needs (returning at once, saying what is missing, when that is absent or the request is not its job), its done check, and what it returns to the caller. It never names a next step. It may name a skill it calls, never one it excludes, and it names record kinds, not paths.
- **Overlaps move, they are not patched.** When two skills claim the same output, move the job to one owner; do not add exclusions. Specialists keep only their own method and never repeat or contradict `alarina`.
- **SIGIDI first.** Where SIGIDI (T3 Code) provides a capability (delegation, worktrees, PR watching, inline HTML, previews, scheduling, secrets), point to it and say what to use when it is absent.
- **When to split.** A capability gets its own skill when people ask for it on its own, its method is used without the rest of its host, two or more skills use it, or keeping it would give the host two jobs or crowd its file. Keep it inside a skill when it is one step of that skill's method and nothing else uses it.

## Writing skills

`ilana` owns skill and prompt text; `oro` owns prose for people. Write in plain words, using the reader's domain and project terms. Simplify repeated or obsolete guidance while keeping behavior, authority boundaries and useful expertise. Keep a script only when it gives a bounded result that prose cannot reliably give.

When a review finds a gap in a rule, fix the condition, not the case. On the second round against the same rule, restate the rule instead of adding another case.

## Verification

- `npm run check` runs the package checks, smoke tests and unit tests; run it before every commit.
- Test behavior changes end to end: give a fresh Claude and a fresh Codex agent the skill on disk and a disposable repository, and judge what they did, not what they said. Run tests and evals on Sol (`gpt-6.1-sol`) at medium.
- Keep checks that catch realistic failures of shipped mechanics; remove redundant or incidental ones, and do not recreate a check the user deliberately removed. When removing a script or workflow, remove references to its commands and claims of its results.
- Report what was actually verified.

## Releases

Every user-visible change carries a changeset (`npm run changeset`, or a file in `.changeset/`). Merging to `ori` opens a "chore: version skills" release PR; merging that bumps the version, writes `CHANGELOG.md` and tags the release. Do not hand-edit versions. A major bump (renamed or removed skills) needs the user's go-ahead.
