# Engineering maturity — 2026-09-27

Author: Oluwaseyi Sobande.

This change strengthens the existing engineering methods with bounded, testable mechanics. It preserves one entrypoint and result ownership. It does not establish general superiority over Compound Engineering or PStack, or production reliability across all hosts.

## Basis and adopted mechanisms

The preceding source comparison inspected instruction bodies, conditional references, configuration, scripts and tests. Its inputs were QP `91b75a53a58959a5c8ef40d8c63bc12074108d8d`, Compound Engineering `a763b392c3c05faa1a383c0d228b7e95200ecc90`, and official PStack `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`. Counts and titles were inventory aids, not evidence of behavior. The new implementation is QP-owned code rather than copied vendor runtime code.

| Observed need | Implemented response | Acceptance boundary |
| --- | --- | --- |
| Repeated path discovery and mixed user records | Record-policy resolver; project/common-Git identity, checkout and task namespaces; explicit destination and established owner precedence | Disposable repository/worktree, symlink, collision and explicit-location tests |
| Thin effective configuration | Strict versioned personal/project/local layers; read-only config and doctor; references to actual project policy | Invalid and unknown settings fail; personal settings cannot replace team checks or model preferences |
| CI treated as the first dependable gate | Project-owned local check inventory reused by CI; missing verifiers explicitly reported in setup | Actual subprocess execution, positive test counts, incomplete/failed/stale results and candidate-bound receipts |
| Reconstructing PR API mechanics | Read-only paginated GitHub helper with exact head/base and partial-result detection | Fixture pagination/failure checks plus one public live API smoke; feedback interpretation remains with the method |
| Unstructured reuse and maintenance | Structured project/portable recipes, scoped inventory, duplicate/scope checks and an engineering-maintenance playbook | Schema is distinct from semantic proof; adoption needs actual execution, recovery and cleanup |
| Standards adoption lacks a common evidence path | Applicability guidance connecting versioned requirements, existing controls, proof and exceptions | Project adoption and specialist evidence remain required; no compliance certification |
| Useful local learning cannot readily become a contribution | Opt-in mature-boundary suggestions, synthetic proposal contract, local privacy preflight and exact-content human review | No history mining, telemetry, automatic submission or anonymity guarantee |

The reusable mechanisms take direction from CE's explicit configuration and deterministic provider mechanics, and PStack's verification discipline and bounded maintenance recipes. QP keeps its own authority, records and compositional contracts. It does not import fixed model rosters, mandatory review personas, native worker fleets, vendor action ledgers, a scheduler or a second policy hierarchy. The public delegation specimen uses user-owned `AGENTS.md` preferences and can be changed or omitted.

## Executable proof

The installed runtime remains Python standard library code. The repository's `.alarina.json` registers the package/compiler checks, runtime contracts, native declaration/install contracts, package smoke, session evidence and HTML diagnostics. `npm run verify:local` exercises that same inventory locally; CI uses it as a backstop. Runtime tests live in `tests/test_project_context.py`, `test_local_checks.py`, `test_alarina_cli.py`, `test_workflow_tools.py` and `test_pr_snapshot.py`.

These tests exercise the assembled CLI and real temporary Git repositories/processes where the boundary requires them. They include zero/all-skipped/failed test evidence, stale candidates/configuration, selected checks, ignored output, duplicate/malformed configuration, project/worktree isolation, structured workflow/privacy failures, provider pagination and partial API responses. A passing structural test does not establish instruction adherence or real product acceptance.

Independent review found and drove corrections for parent-symlink reads, symlinked default receipt destinations, interrupted child processes, ambiguous subset success, automatic package discovery outside the project, misfiled portable/project recipes, and two repository test gates incorrectly registered as exit-only checks. Focused failure regressions accompany the runtime repairs; the local gate is the accepting execution record, not the presence of this narrative.

A public read-only smoke against [CE PR 1780](https://github.com/EveryInc/compound-engineering-plugin/pull/1780) completed with stable head `33c11e8dd715f4b7b86b8a9b8606890204bfb4fb`, base `4043703d32c5df9e35f22757dee22f3a72a99c66`, six observed checks and no API errors. This validates the real GraphQL selection shape used in that request. Multi-page edge cases use fixtures; no live Enterprise, branch-protection, provider writes or merge behavior was exercised.

## Supplied-entry behavioral probe

A fresh Codex worker was requested as `gpt-6-luna`, high reasoning, without inherited conversation context. It received the candidate `SKILL.md` path and two disposable tasks. These are workspace-method observations; requested model settings were not independently attested. There was no direct-owner control or repeated sample, so no comparative improvement or native-discovery claim follows.

| Task and fixture | Observed outcome |
| --- | --- |
| Read-only setup assessment. Project instructions prohibit script execution; no registered gate exists; a `package.json` test script would create a marker if run. | Worker read setup, policy, configuration, records and linked practice/readiness guidance; ran read-only doctor; reported missing local verification and unverified script suggestions. It did not edit configuration or execute the script. Parent inspection found no marker. |
| Write a memo at an explicit supplied destination, with project guidance preserving user-owned model preferences. | Worker created exactly the requested memo with the requested sentence. Parent inspected the file and fixture inventory; no other fixture files changed. |

The observed sentence was: “Use the existing local checks before relying on CI. Keep subagent preferences in AGENTS.md.” Subsequent runtime hardening changed helper internals; it did not change either probe's task or accepted policy. These probes do not cover every workflow, implicit host activation, a whole SDLC engagement or instruction reliability in general.

## Remaining proof belongs to real use

The local process runner supports macOS and Linux; other systems use project-native runners with an explicit capability gap. Candidate evidence excludes ignored/generated state and submodule interiors, and cannot capture remote environments or changed requirements. Test counts establish execution, not assertion quality. Workflow declarations and contribution heuristics remain subordinate to human/agent judgment and existing authority.

Release/install verification, fresh activation on each supported host, project-specific standards acceptance, and real workflow adoption need their corresponding environments and scope. No plugin installation, release, recurring automation or external contribution was performed by this implementation. Compatibility adapters were deliberately omitted from the new configuration and recipe contracts.
