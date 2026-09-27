# Release readiness — 2026-09-27

Author: Oluwaseyi Sobande.

This record joins the [engineering maturity](2026-09-27-engineering-maturity.md) and [assurance follow-up](2026-09-27-assurance-followup.md) evidence. Those records keep their original candidates and observations. This release preparation closes the remaining packaging, current-candidate verification and handoff work; it does not establish general field reliability or superiority over CE/PStack.

## Final policy and evidence changes

- A council has at most three participants including the main agent, with at most two independent specialists. The main agent resolves technical disagreement through evidence. There is no additional judge or replacement roster to expand the cap.
- HTML explanation artifacts default to focused content, destination, navigation and delivery checks, plus structural verification for creation or structural changes. Production or consequential artifacts earn relevant deeper checks. Explicit verification waivers are recorded as skipped. The user waived further verification of the separate comparison report.
- The public [O05 initial fixture](../outcomes/fixtures/ledger-replay) preserves the replay defect and missing local contract check. It includes the explicit caller guarantee, but no successful repair. Actor prompts and held-out expectations remain separate. Its baseline has two passing unit tests and a contract test failing because `ValueError` is not raised. The earlier successful delivery is a separate observation, not a rerun of this newly retained case.
- CI runs the same seven gates as local verification and retains receipts and bounded logs for 14 days, including failed runs when evidence exists. This makes the execution evidence available after runner teardown. Mechanical proof remains distinct from review, native activation and behavioral outcomes.
- A release check exposed Python bytecode caches being copied from the source skill into clean exports after ordinary local execution. The staging regression failed before the fix and passed afterward: exports now omit nested Python/pytest caches, loose bytecode and `.DS_Store`, while preserving actual runtime source. Installed-file comparison still rejects unexpected files; this does not silently ignore contaminated installs.

## Release contract

`npm run changeset -- status` reports `qp-skills` for a major bump. The feature PR retains the pending major changesets and version 4.3.0. After merge to `ori`, the existing release workflow opens the version PR; its version command updates package metadata, lockfile, changelog and native declarations. The expected next version is 5.0.0. No version bump, tag, release publication or merge is performed by this preparation.

The current local gate, Linux Actions result, installed-byte check, native-session observations and provider head/base are attached to the release PR and the local report's evidence index. They are deliberately outside this source record to avoid a receipt containing a claim about its own final identity. The runtime inventory below identifies the installed content independently of changing evidence prose.

## Runtime identity

The local Codex manager refreshed and enabled the package, verifying 176 runtime files. A subsequent independent comparison through a fresh clean export matched both the installation and retained source export. The source checkout contained Python bytecode at that point; the fresh export contained none. The SHA-256 of the sorted JSON runtime file-hash map was `75b5d577a4114a55beda36d90365d9bca1f833b7652a0383ae038c1bb96a485a`.

This identifies package content and the corrected export behavior. It is not proof that the existing desktop session reloaded, that a model selected the plugin implicitly, or that every supported host completed a real engineering task. Bounded fresh native-session results must retain those distinctions.

## Limits that require continued use

The evidence includes real subprocess/repository boundary tests and bounded model tasks, including one actual repair and independent review. It does not include a controlled competitor run, a calibrated blind judge, broad production adoption, a live rollout/rollback, or demonstrated reliability across an entire real-world SDLC. These are limits on broader claims, not unresolved defects in the accepted bounded implementation. Future experiments should use representative tasks and retain initial inputs, complete traces, outcomes, costs and applicable controls.
