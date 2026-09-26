# Project verification capabilities

Read the [shared engineering contract](../references/alaga/engineering-contract.md) before applying this method.

Use when recurring work needs a reliable way to exercise one project's actual product, or an existing verification skill has drifted. Reuse the project's working commands, tests and harness before proposing another capability. A one-off probe does not require a skill.

Own harness implementation and runtime proof. Reuse an existing project verification specialist when one owns these journeys; use [oro-sigidi](oro-sigidi.md) to author agent instructions from verified commands and evidence. The project or host owns material readiness gaps. Creating guidance does not authorize product repairs, installation, deployment or publication.

## Ground the capability

Establish from current project evidence:

- the public surface: API, CLI, library, browser, desktop or mobile;
- the supported build/start command, fixtures, authentication and observable readiness;
- the existing way to drive that surface and observe its effects;
- isolation limits, shared resources and ownership of processes/data; and
- where evidence survives cleanup.

Ask only for consequential choices or unavailable facts. A broken baseline is a named readiness gap, not a reason to invent working commands or silently repair the product.

## Write only the project's useful contract

Preserve its established location and host-native skill packaging. Include exact commands and handles grounded in the project, with only the branches it needs:

Write for an agent arriving without this conversation: identify the working directory, prerequisites, exact invocation and expected observations. Make an existing capability discoverable through a scoped project pointer. If a new project-local skill is justified, use the active host's supported discovery location and metadata; do not hardcode Cursor's layout for every host or install it globally. A named script without its invocation and required inputs is not a usable handoff.

| Concern | What the next user or agent must know |
| --- | --- |
| Start and readiness | How to reach a usable instance of the intended build; how to distinguish it from a stale or unrelated process. |
| Doctor | A cheap read-only readiness check for the target instance, build, owned resources and required access. Recheck after a surprising failure; a healthy process may still need its application state reset. Reuse native checks instead of requiring a wrapper. |
| Drive | Stable public operations or selectors and the setup they require. Short-lived CLIs may need a fresh isolated process per case. |
| Observe | The action and expected result, plus material persisted or external effects. A final screen or HTTP status alone may miss the contract. |
| Recover and clean up | How to reset after a failed drive and remove only owned processes/scratch state. Retain evidence at its named destination. |

Record a small useful set of journeys: entry point, prerequisite, drive command and observable outcome. Reuse existing test or journey identities; add an index only when it makes several maintained recipes easier to find. Do not generate placeholders or an exhaustive feature catalogue.

When acceptance depends on user navigation or later effects, follow the action through its destination and aftermath. For example, a notification must reach the intended recipient and open the correct item, with the expected data and focus where relevant; successful sending alone is insufficient. Record observed friction for the affected user separately from functional failure. Select only affected journeys; this does not require an exhaustive browser matrix or browser testing of static reports. This example is informed by Compound Engineering's [journey taxonomy](https://github.com/EveryInc/compound-engineering-plugin/blob/a763b392c3c05faa1a383c0d228b7e95200ecc90/skills/ce-dogfood/references/test-matrix-taxonomy.md).

For each journey, record material alternate entry points, reset state and known limitations. Label source-derived recipes separately from executed proof, with candidate/environment identity and an evidence locator. Verifying one mapped path does not verify its unexercised alternatives. A feature map guides later selection; seeding it does not claim full-product coverage.

Prefer the real public path over internal setters or verification-only endpoints. An isolated external substitute may be appropriate; state the boundary it leaves unproved. Confirm what a dry-run actually omits before relying on it to prevent effects.

For recurring integration risks, retain the project-specific commands and observations for the applicable framework invocation, supported old/new consumer or data combination, denied access, or interruption/restart journey. Reuse Alaga’s proof methods; this capability supplies the real build, fixtures and driver rather than copying the general method. Record resource-cost recipes only when a concrete workload and bounded measurement are available.

## Prove the instructions

Within existing runtime and effect authority, follow the authored instructions in an appropriate test environment through startup/readiness, one representative journey, effect inspection and cleanup. Check that evidence remains available afterwards and owned resources are released, including after a failed attempt. Correct the instructions or harness from observed failures and rerun the affected path. Missing runtime access or effect authority leaves an unexecuted recipe with a named verification gap; an authoring request does not itself authorize live effects.

Perform this run from the documented starting state using only the recorded setup, without relying on a leftover server, hidden fixture or command remembered from authoring. Fix missing instructions exposed by that run. A separate worker is optional; the requirement is reproducibility from the supplied contract.

Return the usable capability, exact candidate and executed coverage. An unexecuted recipe is unverified; one passing journey establishes only that journey and the exercised harness lifecycle.

## Maintain against intent and observation

When relevant code or the harness changes, or a verification audit is requested, compare the affected recipes with source and runtime. A full-map audit covers the requested map; ordinary delivery checks only affected journeys. Reconcile missing or obsolete entry points using concrete evidence.

Classify discrepancies before correcting them:

- **Instruction drift:** the intended behavior still works, but the recipe is inaccurate.
- **Harness gap:** the product works, but the available driver cannot reach or observe it.
- **Product regression:** observed behavior violates the accepted contract; return it to [alaga-deliver](alaga-deliver.md) instead of rewriting the expectation.
- **Blocked or unassessed:** a prerequisite or observation is missing; name it without claiming success.

Reuse compatible app states and keep one owner for shared driving. After a surprising failure, establish readiness or reset only the invalidated state before continuing. Re-exercise corrected instructions or harness code; preserve evidence through teardown. Report scope and uncovered paths. Maintenance alone does not require a new report, scheduled sweep or PR.

For a requested full-map audit, reconcile the index with its recipes and check source changes for omitted user paths, then exercise every in-scope feature. Source inspection alone cannot produce a clean runtime verdict. Mark unreachable paths with the attempted route and concrete missing prerequisite, retaining successful evidence from other paths. Independent source readers may help; shared live driving keeps one owner.

Informed by PStack's [create-verification-skill](https://github.com/cursor/plugins/blob/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack/skills/create-verification-skill/SKILL.md) and [maintain-verification-skill](https://github.com/cursor/plugins/blob/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack/skills/maintain-verification-skill/SKILL.md). Alárinà preserves project/host conventions, scoped maintenance and existing effect authority.
