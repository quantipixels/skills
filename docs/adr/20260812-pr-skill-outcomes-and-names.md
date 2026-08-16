# Separate PR publication, watching, and explanation

The explanation and `tunmo-pr` parts of this decision are superseded by [Separate session continuity from conversational exploration](20260814-separate-session-continuity-from-conversational-exploration.md). The `seda-pr`, `wo-pr`, provider-runtime, and provider-safety decisions below remain current.

QP publishes three independently installable skills for GitHub pull requests and GitLab merge requests:

- `seda-pr` commits and pushes one bounded current-branch change, then creates or reconciles its zero-context public narrative and bounded metadata;
- `wo-pr` keeps one open item attached through CI, conflicts, and review feedback until a human merge decision;
- `tunmo-pr` explained one exact current diff without mutation. This unreleased owner was later replaced by the broader opt-in `salaye` conversational protocol.

Use the ASCII Yorùbá act names `seda` and `wo` as the public PR and MR lifecycle identifiers. Keep the English actions and GitHub PR/GitLab MR terms in descriptions and metadata so selection does not require Yorùbá knowledge. The superseding decision owns the `salaye` name and its wider subject boundary.

A single PR helper was rejected because publication, monitoring, and explanation have different triggers, mutation authority, state lifecycles, adjacent owners, and completion proof. Invoking `seda-pr` grants the bounded commit, non-force branch push, and ready-item provider writes required to complete publication; it does not grant code implementation, unrelated commits, history rewriting, or human notification. A GitHub-first release was rejected because the accepted public boundary includes GitLab from launch; provider normalization must preserve explicit capability differences rather than claim parity.

QP also rejects a public or required executable forge-provider skill for now. Exact-current inspection found different local Git and provider operations and only one full executable provider consumer. A central runtime would add installation, discovery, version, and failure contracts without hiding one repeated implementation across multiple callers. Keep each skill independently installable and self-contained. Centralize only maintainer-facing safety rules for provider identity, host trust, credential filtering, pagination, evidence completeness, stale-head rejection, structured payloads, and readback. Keep raw `gh` or `glab` execution, small helpers, provider-native semantics, authority, retries, state, and result interpretation with each outcome skill. Reconsider an executable shared runtime only when a second independent executable caller needs the same normalized behavior and QP has a supported packaging contract.

`wo-pr` uses a read-only local observer and direct bounded agent actions. A bare stewardship request includes exact-branch conflict and code repair, non-force commit and push, diagnosed failing-CI reruns, feedback replies or resolution, and progress updates. Reviewer changes require an explicit request. Approval, merge, close, base changes, title/body, and force-push remain separate or excluded. `HANDOFF_READY` is a milestone; watching continues until explicit stop or item closure. Its checkpoint stores only target and head identity, handled-event receipts, retry counts, and the last snapshot and readiness identities. A schema-v1 file is archived before a fresh provider snapshot; old action state never transfers authority.

This decision makes later renaming or recombination expensive after users adopt the public identifiers. Runtime rules remain with each skill, direct provider references, local helpers, and the small `wo-pr` observer checkpoint.
