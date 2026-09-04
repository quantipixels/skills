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
| Claude Code plugin structure | `.claude-plugin/plugin.json`, marketplace metadata, the QP agent entry, and current skill/frontmatter surfaces pass QP structural checks and the pinned Claude Code CLI validator | QP package/plugin validators plus `@anthropic-ai/claude-code@2.1.260 plugin validate .` in `Compatibility smoke` | CI_PROVED |
| Claude Code plugin runtime install/load | The README documents the native marketplace/plugin path, but CI does not complete a clean authenticated/runtime install and model-visible load | No exact runtime-load smoke yet | NOT_RUN |
| Claude Code through Skills CLI | The upstream Skills CLI supports a Claude Code target, but QP does not currently make a release claim for that project/global path | No QP smoke; upstream behavior can change independently | NOT_CLAIMED |
| Other Skills CLI agents | QP follows the portable Agent Skills package shape, but host destination/loading behavior belongs to the current CLI/host | No QP per-host smoke | NOT_CLAIMED |
| `system-cleanup` runtime | macOS-specific behavior as declared by the skill | Skill contract; no cross-platform claim | STRUCTURAL |

## External capability records

### Skills CLI

The compatibility smoke uses the external [`skills`](https://www.npmjs.com/package/skills) CLI from [`vercel-labs/skills`](https://github.com/vercel-labs/skills), pinned in QP CI to **1.5.23**. Current CLI behavior and supported-agent destinations remain upstream-owned; QP adopts only the exact discovery/install path exercised by its smoke.

- **Adoption:** local-repository discovery and Codex project copy installation for all current QP skills.
- **Not adopted as QP truth:** the CLI's full supported-agent matrix, future install locations, or Claude/Codex runtime loading semantics beyond the path QP exercises.
- **Copied material:** none; QP invokes the external CLI and records its behavior.
- **Refresh trigger:** change the pin, change QP package layout, change a claimed destination/host path, or investigate a smoke failure caused by upstream behavior.

### Claude Code CLI

The Claude compatibility smoke uses Anthropic's [`@anthropic-ai/claude-code`](https://www.npmjs.com/package/@anthropic-ai/claude-code), pinned in QP CI to **2.1.260** and recorded on **2026-09-04**. Anthropic's community plugin validation workflow uses the package's `claude plugin validate` command as its canonical CLI validation surface.

- **Adoption:** candidate-local `claude plugin validate .` as an additional Claude-owned syntax/frontmatter/plugin validation check.
- **Not adopted as QP truth:** successful runtime installation, model-visible skill loading, or equivalence between the CLI validator and every Claude runtime/plugin surface.
- **Known boundary:** upstream Claude Code issues [#60725](https://github.com/anthropics/claude-code/issues/60725) and [#62400](https://github.com/anthropics/claude-code/issues/62400) document cases where CLI validation and runtime plugin acceptance diverged. QP therefore keeps runtime install/load at `NOT_RUN` until that exact path is exercised.
- **Copied material:** none; QP invokes the external CLI and records its behavior.
- **Refresh trigger:** change the pin, change Claude plugin/package layout, change the claimed runtime boundary, or investigate a validator/runtime mismatch.

## Release rule

Do not upgrade a compatibility state from `STRUCTURAL`/`NOT_RUN` to `CI_PROVED` because a manifest looks plausible or an upstream tool lists a host as supported. Exercise the QP package through that exact path on the candidate.

When a pinned compatibility tool version changes, rerun the relevant smoke and update this matrix in the same logical change. The version pin exists to make a QP release claim reproducible; it is not a recommendation that users stay on that version forever.

A host-specific capability may still work outside this matrix. `NOT_CLAIMED` means QP does not use it as release evidence.
