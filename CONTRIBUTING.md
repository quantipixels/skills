# Contributing

Thanks for helping. Agents and people follow the same rules; [AGENTS.md](AGENTS.md) holds them in full.

## Before you change a skill

- Read the skill and `alarina`'s skills table. Each kind of output has one owner; if your change overlaps another skill, move the job rather than adding an exclusion ([why](docs/internal/decisions/20261010-one-router-single-job-workers.md)).
- Keep everything the skill needs inside its folder, and keep `SKILL.md` under 8000 bytes ([why](docs/internal/solutions/skill-design/runtime-files-ship-inside-the-skill.md)).

## Check your change

```bash
npm run check                  # package checks, smoke tests, unit tests
sh scripts/install-hooks.sh    # optional: run the checks before each commit
```

For a change in what a skill makes an agent do, run it end to end: give a fresh Claude Code and a fresh Codex agent the skill from disk and a throwaway repository, and judge what they did.

## Open a pull request

1. Add a changeset: `npm run changeset` (patch for fixes, minor for new behaviour; ask before a major).
2. Fill in the pull request template, including the security and agent disclosures.
3. After merge, a "chore: version skills" pull request collects changesets into the next release.
