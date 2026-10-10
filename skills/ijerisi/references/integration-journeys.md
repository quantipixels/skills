# Journeys for recurring integration risks

Read when a project's verification skill should cover a risk that comes back often. The general proof method (integration obligations, stateful proof) is the builder's; this skill supplies the project's real build, fixtures and driver, and records the project-specific commands and observations. Do not copy the general method here.

Record a journey only for a risk the project actually has:

- the framework invoked the way the framework does it (container, lifecycle, commit time), not a hand-built call;
- a supported old and new consumer, writer or data combination running together;
- denied access, checked through each real entry point that reaches the same data;
- interruption and restart between a durable effect and the step that records it.

For each, keep the command, the prerequisite state and what to observe. Add a resource-cost recipe only when a concrete workload and a bounded measurement exist, using the measurement method.

Keep the set small. Reuse existing test or journey identities, and add an index only when it makes several maintained recipes easier to find. Do not write placeholders or an exhaustive feature catalogue.
