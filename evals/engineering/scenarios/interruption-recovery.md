# Actor task: interruption and recovery

Repair the supplied retryable operation so the accepted external effect and its local durable record remain coherent after the specified interruption. Use the existing operation identity, persistence owner and provider contract where they satisfy the requirement. Preserve completed records and reject conflicting reuse of an operation identity.

Exercise a real worker process, the durable provider fixture and persistent local state. Demonstrate recovery after the process is terminated after the provider commits but before local completion, then after normal completion. Use deterministic synchronization rather than a lucky sleep. Distinguish the guarantee supported by the provider from guarantees the application cannot establish alone.

Return the scoped diff, the interruption/restart commands and final durable observations. State whether concurrent callers, cancellation and earlier historical uncertain operations were covered; do not infer those guarantees from sequential recovery.
