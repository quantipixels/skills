# Runtime evidence

Use when a supplied CPU profile, heap snapshot, stack sample or execution trace needs reduction, or when a resource-cost question needs a bounded measurement. Irinse owns selecting and interpreting the capture tool. `alaga` owns the causal diagnosis and any correction; return the reduced evidence there rather than promoting a hotspot or correlation into a verdict.

Pin the candidate, workload, environment, capture interval and artifact identity. Prefer an existing capture. For a live capture, use the narrowest project-native profiler or tracer that can expose the disputed behavior, within existing runtime and side-effect authority. Preserve the original artifact and record whether symbol/source maps are available.

For resource-cost evidence, record useful work alongside cost: requests or rows processed, query/round-trip count, peak memory, connection occupancy, lock waits or active concurrency as applicable. Include data distribution and warm/cache state when they can change the conclusion. Use a bounded representative workload and stop conditions; a wall-clock improvement can conceal more queries, retained memory or dropped work. Infrequent migrations and administrative jobs can still exhaust shared resources. Return the measurements to `adanwo` for comparative judgment or `alaga` for diagnosis.

Identify the format and use its native parser. Make a large artifact queryable with a bounded table or database projection only when that materially improves reduction. Select evidence by symptom:

- for CPU cost, rank inclusive and self time, then retain the relevant caller/callee path rather than a flat hot symbol;
- for retained memory, follow the suspected object through retaining edges to a root and distinguish retained size from allocation volume;
- for a stall, identify the blocked or running thread/task, its stack, wait reason and the resource or owner it awaits;
- for event traces, correlate the relevant interval and identifiers across the events that lead to the symptom.

Attribute the reduced path to file, symbol and line when the artifact supports it. Missing symbols limit source attribution; state that limit instead of guessing. When matched captures exist, compare the same workload and conditions and report the observed path or cost difference. Paired traces strengthen attribution but do not by themselves prove a causal mechanism.

Return the artifact identity and format, capture conditions, reduced hot path/retainer chain/wait chain, source attribution, comparison basis, and limits that affect the next discriminating probe. Do not prescribe a fix from tool output alone.
