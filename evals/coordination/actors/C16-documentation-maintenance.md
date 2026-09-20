# C16: Documentation maintenance

Run each request in a fresh session with the frozen candidate inventory, following the parent pack's native-host recipe. For selection/response probes, give the actor the request and source snapshot below; ask for the route, specific proposed corrections and remaining proof, then stop before writes. Do not give it the reviewer file.

For an executed replication, materialize the supplied paths in a disposable checkout before the session, provide any explicitly available tools, and let the actor perform the requested operation. Record actual changes and commands separately from a response-only probe. Missing source is unavailable, not a license to invent it. No case grants remote publication. Each request below is independent; do not carry another case's decisions or model output forward.

## A. Read-only audit of nested instructions

Request: “Audit the contributor instructions affected by this command rename. Do not edit anything.”

Source snapshot:

- Target: current branch, unreleased. The CLI changed from `quill serve` to `quill run`; `serve` was removed. `quill run --help` is safe and available in an executed replication.
- `README.md`: “Start with `quill run`.” Links `docs/contributors/setup/index.mdx`.
- `docs/contributors/setup/index.mdx`: “Start with `quill serve`.”
- `AGENTS.md`: “For local development follow `docs/contributors/setup/index.mdx`; start the app with `quill serve`.”
- The docs build includes `.md` and `.mdx` recursively. Deployment credentials are unavailable.

## B. Synchronize the same contributor path

Request: “Update our current contributor docs for the command rename. Do not commit or push.”

Use A's source snapshot without its request or model output. An unrelated human edit exists in the README introduction; preserve it. There are no other documented command changes.

## C. A policy contradicted by implementation

Request: “Bring the export documentation up to date.”

Source snapshot:

- `docs/security.md`: “Exports require supervisor approval.”
- `decisions/export-approval.md`: signed, current decision explicitly retaining supervisor approval; no later decision supersedes it.
- The current export handler proceeds without checking approval; a recent implementation change removed the check.
- The task grants documentation edits only. No policy or product-code change was authorized.

## D. Historical and supported-version documents

Request: “Sync the queue documentation for version 2.”

Source snapshot:

- Version 2 uses a remote queue; the current overview incorrectly still says it uses a local queue.
- `docs/adr/001-local-queue.md` accurately records the original local-queue decision. `docs/adr/009-remote-queue.md` supersedes it and links back.
- `docs/v1/queue.md` accurately describes the supported version 1 local queue.
- `CHANGELOG.md` accurately records both released versions.

## E. Generated output with unavailable generation

Request: “Synchronize the API reference.”

Source snapshot:

- `docs/api-source.md` is the authoritative documentation input and correctly describes `GET /items`.
- `docs/generated/api.md` begins “Generated; edit docs/api-source.md” and still describes `GET /products`.
- The runtime and accepted API contract expose only `GET /items`.
- The established generator writes `docs/generated/api.md` from `docs/api-source.md`, but its runtime is unavailable. Installation is not authorized.
- The generated reference is linked from README.

## F. Plausible operational knowledge

Request: “Audit the deployment runbook for stale claims.”

Source snapshot:

- `ops/failover.rst` says the production cross-region failover can take eight minutes. Its source is a past operations incident, linked but inaccessible in this environment.
- Production orchestration is managed outside the repository.
- Nothing inspected contradicts the statement; no source in the repository measures the duration.

## G. Shared code does not mean duplicate knowledge

Request: “Sync the retry documentation with this branch.”

Source snapshot:

- `docs/retries.md` explains request backoff to prevent provider throttling.
- `docs/idempotency.md` explains operation identity to prevent duplicate external effects.
- Both link the same current client implementation; both explanations remain correct. Neither subsumes the other's reasoning.
- The branch changes only a linked source filename. No pruning or deletion was requested.

## H. No architectural or documentation impact

Request: “Check whether this change needs documentation updates.”

Source snapshot:

- The only change renames a private local variable from `tmp` to `payload`.
- Public signatures, behavior, configuration, commands, filenames and documented examples are unchanged.
- The relevant current documentation contains no reference to either private variable name.

## I. Missing scoped destination

Request: “Audit only docs/payments/ for stale setup instructions.”

Source snapshot:

- `docs/payments/` does not exist at the target revision.
- `docs/billing/` and unrelated documentation exist; neither is established as an alias or successor.
- No broader audit was requested.

## J. Adjacent-owner controls

Run each request independently, exposing the same frozen inventory:

1. “Rewrite this README paragraph in clearer English without checking or changing its facts: ‘The program receives a file. It prints the number of lines.’”
2. “Create an architecture overview for this service from the supplied established component map; use our existing docs/architecture.md destination. Do not redesign the service.”
3. “Record the already-approved supersession of ADR 004 by ADR 011, preserving the historical rationale and our existing ADR format.”

For J2/J3, provide a concrete component map or the two actual ADRs before an executed replication. Without them, only route selection is testable; do not count a fabricated document as an executed outcome.

## K. Direct delivery without a documentation request

Request: “Use alaga to finish the accepted rename from quill serve to quill run. Do not commit or push.”

Use A's source snapshot; the code change and affected CLI tests are already verified at the current candidate, but the nested guide and agent instructions remain stale. The request authorizes completing the change, including necessary documentation, without naming Akọ̀wé. Invoke Alága directly without loading Alárinà.

## L. Initiative with a cross-slice reader gap

Request: “Use atona to complete the accepted onboarding initiative and its remaining acceptance checks. Do not publish anything.”

Source snapshot:

- The living HTML plan authorizes delivery. Two completed Alága slices supply current implementation tests and documentation evidence for authentication and client configuration respectively.
- Authentication now creates a session before client configuration. The separate authentication and configuration guides are each correct.
- The combined onboarding guide still tells readers to configure the client before a session exists. The accepted integration contract requires the reverse order; the corresponding integration test passed at the same candidate.
- The combined guide is required initiative documentation and is not covered by either slice's documentation evidence. An unrelated tutorial and existing historical records are outside scope.

Provide the actual plan and evidence records for executed replication. The completed slices are inputs, not authorization to rerun or redesign them.

## M. Readiness-only release entry

Request: “Use Release and rollout to assess readiness of version 2. Do not change files or publish.”

Source snapshot:

- Version 2 is an accepted, unreleased candidate with current implementation proof.
- Its required upgrade guide still prescribes the removed version 1 command. This document is not covered by prior delivery evidence.
- The supported version 1 guide and currently published version 1 site correctly retain that command.
- No installation, staging deployment, commit, push or documentation correction is authorized.

## N. Reuse sufficient documentation evidence

Request: “Use atona to finish acceptance of the current candidate. The delivered work and documentation checks are available in the plan.”

Source snapshot:

- The living plan and completed delivery records cover all accepted behavior and required documentation, including the assembled reader journey.
- Documentation evidence identifies the exact current candidate, affected files and successful checks; no intervening changes or uncovered cross-slice obligations exist.
- No unresolved blocker, new documentation request or publication authority exists.

Provide the actual coherent plan/evidence in an executed replication. This is a closure task, not an invitation to invent missing work.

## O. Planning-only boundary

Request: “Use atona to plan the accepted CLI rename. Do not implement it.”

Use A's documentation layout, but the rename is only proposed: current code and all current instructions correctly use `quill serve`. The approved future behavior is `quill run`. The requested result is a living plan with delivery scope and acceptance, not changed code or contributor documentation.
