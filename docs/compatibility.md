# QP compatibility claims

Compatibility is a release property, not a blanket promise that every host-specific feature works everywhere.

Use these evidence states:

- **CI_PROVED** — the exact path is exercised on every validated candidate;
- **STRUCTURAL** — repository metadata/package shape is deterministically validated, but the target host runtime is not exercised;
- **NOT_RUN** — a plausible path exists but QP has no current proof for it;
- **NOT_CLAIMED** — QP deliberately makes no release claim for that path.

## Current matrix

| Surface | Claim | Evidence | State |
| --- | --- | --- | --- |
| Core Agent Skills package | Every public QP skill has valid `SKILL.md` structure and local resource integrity | `ko-skill/scripts/validate-package.py` in `Validate` | CI_PROVED |
| Skills CLI discovery | Pinned `skills@1.5.23` can discover QP from a local checkout | `Compatibility smoke` job runs `skills add <checkout> --list` | CI_PROVED |
| Codex project install through Skills CLI | Pinned `skills@1.5.23` can copy every current QP skill into the Codex project skill surface on Ubuntu | `Compatibility smoke` installs `--skill '*' --agent codex --copy -y` and compares installed/current skill counts | CI_PROVED |
| Claude Code plugin manifest | `.claude-plugin/plugin.json`, the QP agent entry, and its preloaded QP skill references are structurally valid | `validate-plugin-agents.py` plus package validation | STRUCTURAL |
| Claude Code plugin runtime install/load | The README documents the native marketplace/plugin path, but CI does not launch Claude Code and load the plugin | No exact runtime smoke yet | NOT_RUN |
| Claude Code through Skills CLI | The upstream CLI supports a Claude Code target, but QP does not currently make a release claim for that project/global path | No QP smoke; upstream behavior can change independently | NOT_CLAIMED |
| Other Skills CLI agents | QP follows the portable Agent Skills package shape, but host destination/loading behavior belongs to the current CLI/host | No QP per-host smoke | NOT_CLAIMED |
| `system-cleanup` runtime | macOS-specific behavior as declared by the skill | Skill contract; no cross-platform claim | STRUCTURAL |

## Release rule

Do not upgrade a compatibility state from `STRUCTURAL`/`NOT_RUN` to `CI_PROVED` because a manifest looks plausible or an upstream tool lists a host as supported. Exercise the QP package through that exact path on the candidate.

When a pinned compatibility tool version changes, rerun the relevant smoke and update this matrix in the same logical change. The version pin exists to make a QP release claim reproducible; it is not a recommendation that users stay on that version forever.

A host-specific capability may still work outside this matrix. `NOT_CLAIMED` means QP does not use it as release evidence.
