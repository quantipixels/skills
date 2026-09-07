# Compatibility

A claim applies only to the stated path. `CI_PROVED` means that path is exercised by candidate CI; `STRUCTURAL` means configuration/package checks only; `NOT_RUN` is an unproved runtime path; `NOT_CLAIMED` is outside the release claim.

| Path | Evidence | State |
| --- | --- | --- |
| Flat Agent Skills package and local resources | Strict package/agent validators and rejection tests | CI_PROVED |
| Skills CLI discovery and Codex project copy | Pinned `skills@1.5.23` against the exact checkout | CI_PROVED |
| Claude plugin validation and clean local-marketplace installation | Pinned `@anthropic-ai/claude-code@2.1.260` | CI_PROVED |
| Direct QP snapshot install/update/remove | Exact-checkout round-trip on Ubuntu; filesystem/interruption tests on Linux and macOS | CI_PROVED |
| Remote installer bootstrap | Exact same-repository head fetch on pushes and same-repository PRs; skipped for forks/merge groups | CI_PROVED |
| Native Codex manifest and shared skill target | Package validator and rejection tests; no bundled hooks, servers, or startup settings | STRUCTURAL |
| Native Codex plugin installation, update/removal and authenticated invocation | Host round-trip and behavioral checks not supplied | NOT_RUN |
| Knowledge retrieval, premortem readiness, boundary review, agent-facing design and measured optimization | Source guidance and [targeted native-host cases](verification.md), not observed model comparisons | NOT_RUN |
| Pepeye native adapter structure | One lazy-loading main agent; equivalent Codex instruction body; no model/permission overrides | STRUCTURAL |
| Authenticated skill selection, decision-tree composition, supervision and worker reuse | [Native-host checks](verification.md); package success is not model behavior | NOT_RUN |
| Akọsílẹ̀ and local session parsers | Existing deterministic tests on Linux, macOS and Windows | CI_PROVED |
| Direct installer on Windows | Uses POSIX symlinks and `flock`; use the native Skills CLI instead | NOT_CLAIMED |
| Other hosts, model-runtime parity and macOS storage cleanup | Per-host proof not supplied by this package | NOT_CLAIMED |

The direct installer owns only its generation store and recorded host links. It neither adopts native plugin/Skills CLI installations nor edits their locks, hooks, credentials, startup defaults, or policies. It refuses foreign collisions and modified installed content. Interrupted visible-link changes recover from the journal; an incomplete unowned staging copy is preserved rather than guessed away.

The external Skills CLI remains an independent alternative, not the direct installer's backend. Its pin makes discovery/copy tests reproducible, not a recommendation to retain that version forever. The Claude CLI pin proves validation and installation, not authenticated load or every future host version. Update a pin together with its relevant tests and claim.

Claude's [main-agent selection](https://code.claude.com/docs/en/sub-agents) replaces the built-in system prompt. Codex's [profile](https://developers.openai.com/codex/config-advanced) adds primary-session configuration, and an instruction string replaces rather than appends to an existing string. The adapters intentionally expose this distinction. Read the installed host's documentation when behavior differs; do not loosen permissions to obtain a preferred topology.

No general orchestration server, custom skill runtime, or authenticated behavior guarantee is implied by these checks.
