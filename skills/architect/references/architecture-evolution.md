# Architecture evolution

Use when changed needs, recurring friction, support constraints or a concrete capability put an established choice in question. Preserve Architect's survey/design/review boundary; age and novelty alone justify no migration.

Recover the responsibility, directly stated original rationale, supported inference, current constraints and what changed. Missing rationale is uncertainty. Follow only history/decisions/incidents needed to resolve a live constraint.

Trace a representative development change and, for observable behavior, one user journey. Compare consequences for users, maintainers and coding agents; agent convenience cannot degrade the product or developer maintainability.

Include retaining the current choice. Compare extending its owner, simplifying it and replacing it against the same requirement. Before adding dependency/service/state, verify whether the current language, runtime, framework or provider already owns the responsibility.

For dependencies/upgrades, inspect the effective resolved version/graph, generated artifacts, runtime/toolchain requirements, public interfaces, transitive cost and official compatibility/migration guidance. Distinguish source, wire and semantic compatibility. Compare total ownership cost: removed work, integration, licensing/support, operations, debugging, upgrades and exit/migration.

For API changes, inspect realistic caller sequencing, identity, errors and pagination. For repository layout, prefer locality and explicit dependency direction over a universal folder convention. For build/test changes, compare equivalent useful work and distinguish clean, incremental and no-change paths plus executed versus cached proof.

When alternatives remain credible, compare caller burden, failure ownership, compatibility, migration/reversibility and required proof. Use `adanwo` for a disputed empirical claim and `atunwo` for independent simplification judgment. State when keeping the current design wins.

Return the selected change or retention decision, evidence, user/developer/agent consequences, strongest alternative, migration cost and the smallest experiment that could overturn it. A bounded result may be keep, change, investigate or defer with a re-entry condition.

A stable consequential invariant may earn an executable fitness check; verify it rejects a representative violation. One-off preferences do not.
