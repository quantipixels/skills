# Bundled-script boundary

Read this reference only when a skill candidate adds, keeps, expands, moves, or replaces a bundled script. The skill owns judgment and workflow. A script earns a place only at a narrow deterministic seam that native capabilities or one focused existing library do not express adequately.

## Require one mechanical contract

State the script's complete contract in one sentence:

> Given X, deterministically produce Y.

Reject the script when that sentence requires semantic judgment, routing, authorization, lifecycle control, or a broad workflow. Repetition alone does not justify code.

A script may:

- parse or normalize structured input;
- search or rank a bounded local dataset;
- validate explicit mechanical invariants;
- transform or compile one representation into another;
- fingerprint an exact candidate;
- aggregate counts or metadata; or
- expose a compact read-only snapshot of source or provider truth.

A script must not own:

- recommendations, architecture, design direction, or prioritization;
- user-intent interpretation or skill selection;
- mutation authority or permission inference;
- readiness, acceptance, severity, or semantic classifications;
- another skill's status, lifecycle, recovery, or orchestration; or
- a second source of truth that duplicates readable source material.

Explicit deterministic classifications are allowed only when the categories and rules are mechanical, stable, and owned exclusively by the script. Unclassified input stays unclassified; do not split one rule system between script and model.

## Apply the gates

For each script, record:

1. **Owner** — the skill genuinely owns the operation.
2. **Need** — host-native tools, provider CLIs, project tooling, or one focused library are insufficient.
3. **Mechanical boundary** — the result is a fact, validation, transformation, fingerprint, or bounded retrieval result rather than a semantic conclusion.
4. **Narrowness** — the complete operation fits the `X → Y` sentence without hidden orchestration.
5. **State discipline** — the script is stateless by default. Persistent state requires an observed cross-process need that current source/provider truth cannot reconstruct.
6. **Truth boundary** — source, repository, or provider state remains authoritative. Script output is a derived observation.
7. **Output** — return compact structured data or the exact transformed artifact. The skill interprets it.
8. **Proof** — tests cover the deterministic seam and credible boundary failures, not an unnecessary workflow engine.

Prefer a focused mature library when it materially removes custom parsing, search, protocol, or transformation code. Do not introduce a framework for a small helper, preserve custom code merely because it exists, or maintain an allowlist of permitted libraries.

## Choose one disposition

Return one disposition for every reviewed script:

- `KEEP` — narrow, necessary, correctly owned, and proportionately proved;
- `SHRINK` — the operation is valid but the implementation absorbs avoidable behavior;
- `REPLACE_WITH_NATIVE` — host, provider, project, or standard tool capability already owns it;
- `REPLACE_WITH_LIBRARY` — a focused existing dependency removes substantial custom mechanics;
- `MOVE_TO_OWNER` — the deterministic operation belongs to another skill;
- `REMOVE` — it adds no justified deterministic capability;
- `NEEDS_EVIDENCE` — necessity or ownership is not yet proved.

Do not retain a script because deleting it would delete its tests. Remove obsolete tests with the obsolete behavior. Do not use line count as an acceptance rule; use it only as a signal that the one-sentence contract may have expanded.
