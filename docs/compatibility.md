# QP compatibility claims

Compatibility is a release property, not a blanket promise that every host-specific feature works everywhere.

Use these evidence states:

- **CI_PROVED** — the exact path is exercised in CI within the stated host and event scope;
- **STRUCTURAL** — repository metadata/package shape is deterministically validated, but the target host runtime is not exercised;
- **NOT_RUN** — a plausible path exists but QP has no current proof for it;
- **NOT_CLAIMED** — QP deliberately makes no release claim for that path.

## Current matrix

| Surface | Claim | Evidence | State |
| --- | --- | --- | --- |
| Core Agent Skills package | Every public QP skill has valid `SKILL.md` structure and local resource integrity | `ko-skill/scripts/validate-package.py` in `Validate` | CI_PROVED |
| Skills CLI discovery | Pinned `skills@1.5.23` can discover QP from a local checkout | `Compatibility smoke` job runs `skills add <checkout> --list` | CI_PROVED |
| Codex project install through Skills CLI | Pinned `skills@1.5.23` can copy every current QP skill into the Codex project skill surface on Ubuntu | `Compatibility smoke` installs `--skill '*' --agent codex --copy -y` and compares installed/current skill counts | CI_PROVED |
| Claude Code plugin structure | `.claude-plugin/plugin.json`, marketplace metadata, the sole Pepeye main-agent entry, and current skill/frontmatter surfaces pass QP structural checks and the pinned Claude Code CLI validator | QP package/plugin validators plus `@anthropic-ai/claude-code@2.1.260 plugin validate .` | CI_PROVED |
| Claude Code clean marketplace install | A clean isolated Claude config can add the candidate checkout as a local marketplace, install `qp-skills@qp-skills`, and list both marketplace/plugin records | pinned Claude CLI marketplace-add/install/list smoke in `Compatibility smoke` | CI_PROVED |
| Claude Code model-visible load/invocation | Clean install is proved, but CI does not start an authenticated model session and demonstrate QP skill/agent selection inside that runtime | Fresh-host behavioral/runtime proof still required | NOT_RUN |
| Pepeye host-adapter wiring | One Claude main-agent entry with no mandatory skill preloads; the Codex profile carries the same role without native-prompt/model/permission overrides | Focused adapter tests in `.github/tests/test_package_integrity.py`; model-visible loading is not proved | STRUCTURAL |
| Pepeye supervision on Claude Code/Codex | Session/default selection, worker-role isolation, delegation, guidance, reuse, settings readback, and cancellation need authenticated runtime proof | [Main-agent setup](../README.md#main-agent-pepeye) and the runtime check below; syntax/install checks do not prove orchestration | NOT_RUN |
| Codex/Claude global skill-only install and cleanup | Install/reinstall through `scripts/install.sh`, verify candidate bytes and Claude links, then uninstall/repeat removal in an isolated home on Ubuntu | `Round-trip public global installer` in `Compatibility smoke`, on pushes and same-repository PRs only; skipped for forks and merge groups | CI_PROVED |
| Global cleanup safety boundaries | Refuse unmanaged same-name Codex/Claude paths, leave other host directories untargeted, and detect lock-only cleanup or native shared-install retention | `scripts/test_install.py` and `scripts/test_uninstall.py` on Linux/macOS, using filesystem state and controlled native commands | CI_PROVED |
| Claude Code project installation through Skills CLI | The upstream CLI supports this target, but QP has no project-install smoke | Global skill-only installation above is a different path | NOT_CLAIMED |
| Other Skills CLI agents | QP follows the portable Agent Skills package shape, but host destination/loading behavior belongs to the current CLI/host | No QP per-host smoke | NOT_CLAIMED |
| `system-cleanup` runtime | macOS-specific behavior as declared by the skill | Skill contract; no cross-platform claim | STRUCTURAL |

## Pepeye runtime check

In a fresh selected session, ask a simple question, request an exact specialist result, then request two independent read-only checks with a related follow-up to one worker. Confirm direct handling without an unnecessary router/coordination pass, specialist selection, early guidance, actual handle reuse, honest settings/status reporting, and worker-role isolation. Cancel a worker and verify it is not restarted. Prohibit edits/publication. Refresh live state after resume or compaction; a saved handle is not proof of continuity. Record unsupported controls and observed evidence separately from package/install success.

## External capability records

### Skills CLI

The compatibility smoke uses the external [`skills`](https://www.npmjs.com/package/skills) CLI from [`vercel-labs/skills`](https://github.com/vercel-labs/skills), pinned in QP CI to **1.5.23**. Current CLI behavior and supported-agent destinations remain upstream-owned; QP adopts only the exact discovery/install path exercised by its smoke.

- **Adoption:** local-repository discovery, Codex project copy installation, and the event-scoped global Codex/Claude install–reinstall–uninstall path above. Cleanup uses the native CLI only after checking the QP lock and its permitted paths; retained shared installations are not force-removed.
- **Not adopted as QP truth:** the CLI's full supported-agent matrix, future install locations, or Claude/Codex runtime loading semantics beyond the path QP exercises.
- **Copied material:** none; QP invokes the external CLI and records its behavior.
- **Refresh trigger:** change the pin, change QP package layout, change a claimed destination/host path, or investigate a smoke failure caused by upstream behavior.

### Claude Code CLI

The Claude compatibility smoke uses Anthropic's [`@anthropic-ai/claude-code`](https://www.npmjs.com/package/@anthropic-ai/claude-code), pinned in QP CI to **2.1.260** and recorded on **2026-09-04**. Current Anthropic documentation exposes non-interactive `claude plugin validate`, `plugin marketplace add`, `plugin install`, `plugin marketplace list --json`, and `plugin list --json` surfaces for local marketplace testing and automation.

- **Adoption:** candidate-local plugin validation plus a clean isolated-config local-marketplace add/install/list path for `qp-skills@qp-skills`.
- **What this proves:** the candidate marketplace can be registered, the plugin can be installed through Claude's own CLI, and Claude's installed-plugin inventory reports QP.
- **Not adopted as QP truth:** authenticated model-visible skill/agent loading, invocation correctness, or equivalence between CLI acceptance and every Claude runtime session surface.
- **Known boundary:** upstream Claude Code issues [#60725](https://github.com/anthropics/claude-code/issues/60725) and [#62400](https://github.com/anthropics/claude-code/issues/62400) document cases where CLI validation and runtime plugin acceptance diverged. Clean install narrows that gap but does not replace a model-visible fresh-host run.
- **Copied material:** none; QP invokes the external CLI and records its behavior.
- **Refresh trigger:** change the pin, change Claude plugin/package/marketplace layout, change the claimed runtime boundary, or investigate a validator/install/runtime mismatch.

## Release rule

Do not upgrade a compatibility state from `STRUCTURAL`/`NOT_RUN` to `CI_PROVED` because a manifest looks plausible or an upstream tool lists a host as supported. Exercise the QP package through that exact path on the candidate.

When a pinned compatibility tool version changes, rerun the relevant smoke and update this matrix in the same logical change. The version pin exists to make a QP release claim reproducible; it is not a recommendation that users stay on that version forever.

A host-specific capability may still work outside this matrix. `NOT_CLAIMED` means QP does not use it as release evidence.
