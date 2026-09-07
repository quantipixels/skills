# Compatibility

Claims are scoped to the path shown. `CI_PROVED` means the current candidate CI exercises that mechanical path; `STRUCTURAL` means package/configuration checks only; `NOT_RUN` means authenticated runtime behavior is unproved; `NOT_CLAIMED` is outside the package claim.

| Surface | Evidence | State |
| --- | --- | --- |
| Flat skill package and local resources | package/agent validation in CI | `CI_PROVED` |
| Skills CLI discovery/copy | compatibility smoke in CI | `CI_PROVED` |
| Claude plugin validation and clean installation | compatibility smoke in CI | `CI_PROVED` |
| Direct snapshot install/update/remove on macOS/Linux | round-trip and interruption/filesystem checks | `CI_PROVED` |
| Native Codex manifest and shared `skills/` target | package validation only | `STRUCTURAL` |
| Native Codex plugin install/update/remove and authenticated invocation | no host round-trip supplied | `NOT_RUN` |
| Skill selection, premortem quality, review quality, agent-facing design, measured optimization, and Pepeye coordination | model evaluation not run for this release | `NOT_RUN` |
| Direct snapshot installer on Windows | POSIX symlink/locking path is not supported | `NOT_CLAIMED` |

Exact tool pins and platform jobs live in [the validation workflow](../.github/workflows/validate.yml); this file records claims rather than duplicating CI configuration.

Package success does not establish model behavior. Model datasets, rubrics, harnesses, and comparison runs belong in the separate internal eval repository; unavailable evaluations remain `NOT_RUN`.
