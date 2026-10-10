# Actor task: measured resource cost

Improve the supplied operation against its stated workload and resource constraint while preserving observable behavior. Use the existing project and measurement tools. Establish the baseline before deciding whether the issue is repeated queries, retained data, contention, concurrency or another mechanism.

Compare the same operation, data and environment before and after the scoped change. Record output correctness and the supplied cost measures, including relevant database round trips, processed rows, peak memory or concurrency. Separate cold/warm conditions and measurement noise where they affect the conclusion. Do not add a cache, batching mechanism or parallel execution solely because it sounds faster.

Return the scoped diff, reproducible commands, workload description, baseline/candidate results and remaining limitations. If usable measurement is unavailable, report the blockage and the smallest useful probe; do not replace measurements with a complexity claim or a guessed percentage improvement.
