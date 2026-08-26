# Narrow bundled scripts to deterministic seams

Status: Accepted

Supersedes the script-retention boundary in [20260824-keep-scripts-with-outcome-owners.md](20260824-keep-scripts-with-outcome-owners.md). That decision remains authoritative for outcome ownership and use of native platform capabilities.

QP will retain a bundled script only when its complete operation can be stated as “given X, deterministically produce Y,” the owning skill genuinely owns that mechanical result, and native tools or one focused existing library do not express it adequately.

Scripts may parse, normalize, retrieve, validate mechanical invariants, transform, fingerprint, aggregate, or expose read-only source/provider facts. Skills retain semantic judgment, user-intent interpretation, routing, authorization, readiness, acceptance, architecture, design direction, and lifecycle orchestration. Source, repository, and provider state remain authoritative.

Stateless operation is the default. Persistent state, locking, retry ledgers, schema migrations, and process ownership require an observed cross-process need that current truth cannot reconstruct. Provider skills may use narrow read-only snapshot helpers, but they will not maintain a parallel semantic model of provider state merely to orchestrate the workflow.

Focused mature libraries are allowed when they materially remove custom parsing, search, protocol, or transformation code. QP will not maintain a library allowlist or use licensing as a selection gate. A framework is not justified for a small helper.

Kọ Skill owns enforcement through its bundled-script boundary. Portfolio audits classify each script as `KEEP`, `SHRINK`, `REPLACE_WITH_NATIVE`, `REPLACE_WITH_LIBRARY`, `MOVE_TO_OWNER`, `REMOVE`, or `NEEDS_EVIDENCE`. Tests prove the retained deterministic seam; obsolete tests leave with obsolete runtime behavior.

This decision permits removal of the Ṣẹ̀dá PR command-policing wrapper, replacement of Wò PR's watcher state machine with a facts-only snapshot helper, reduction of Alága's candidate snapshot to exact candidate identity, and consolidation or removal of duplicated design-search and token-validation helpers.
