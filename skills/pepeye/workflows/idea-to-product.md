# Idea to usable product

Use when an idea needs several owned results before it can become a usable product increment. Skip results already settled by the user or current evidence.

## Flow

1. `iwadi` — resolve missing evidence that could change direction.
2. `arojinle` — close consequential choices where credible alternatives materially differ.
3. `architect` / `seda-spec` — settle technical structure or observable behavior that implementation would otherwise invent. Run independently only where their decisions do not constrain each other.
4. `atona` — coordinate material delivery dependencies and sequencing. Plan earlier when it helps organize discovery; refresh it after decisions that change execution.
5. Independent plan review — apply the entrypoint's review gate before dependent execution; use the plan-review prompt.
6. `alaga` — implement the accepted increment with sufficient proof.
7. `atunwo` — review the fixed candidate when required or justified by consequence/uncertainty.
8. `seda-pr` — publish when authorized.

## Recovery and completion

- Direction invalidated → `iwadi` for missing evidence, then `arojinle` for the reopened choice.
- Structure or behavior unresolved → `architect` or `seda-spec`; update affected planning dependencies.
- Plan review finds a gap → the owner of that result; re-review only material changes to the judgment boundary.
- Candidate changes or review finds a defect → `alaga` as needed, then refresh invalidated `atunwo` evidence.
- Publication fails → the causal owner; do not restart product discovery.

Complete when the accepted increment is usable, required proof is current, and the requested delivery state is reached. Distinguish publication, integration, and release; none implies the next.
