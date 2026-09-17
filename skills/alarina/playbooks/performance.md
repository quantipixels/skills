# Performance improvement

Use for an authorized runtime, build or CI improvement, or a measured keep/revert decision. A request only to explain a slowdown uses Investigation; a settled optimization needing implementation goes directly to `alaga`.

1. Establish the affected workload, useful performance outcome and correctness constraints. If the mechanism is unresolved, `alaga` diagnoses it; use the project's measurement capability for needed capture/tool expertise. Reuse adequate existing measurements.
2. `adanwo` in measured-experiment mode compares bounded candidates against a compatible baseline. For builds, it preserves required outputs/checks and distinguishes clean, incremental and cache-dependent work. For sustained optimization, use its finite trial budget, confirmation and stopping rules. Let measured cost suggest the hypothesis class; do not add batching, caching, concurrency or custom infrastructure merely because they are available.
3. Route a consequential design choice to `architect`. Use `atona` when a larger improvement needs dependent delivery slices, preserving the same metric, constraints and stopping point. One experiment needs no extra initiative.
4. A selected implementation and its regression proof belong to `alaga`; the experiment's keep/revert judgment stays with `adanwo`. Reuse candidate code and valid proof rather than commissioning the same implementation or measurement twice.

Finish with a supported improvement, a justified rejection or an inconclusive result and its limiting evidence. Iterate only within the requested target and budget. Retained performance wins still need required API, persistence and user-journey proof; publication remains conditional on authority.
