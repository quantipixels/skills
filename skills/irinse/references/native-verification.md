# Native runtime checks

Use when a concrete memory, parser or concurrency risk needs dynamic evidence beyond ordinary tests. Discover the actual language, compiler, target platform, build profile and existing harness first. Alaga owns harness implementation and regression fixes; atunwo owns independent findings. Do not add instrumentation or dependencies merely to consult this reference.

Select a supported sanitizer for memory/undefined-behavior evidence, a race detector for exercised conflicting accesses, or coverage-guided fuzzing for input boundaries. Use current official docs for the chosen compiler/tool. Instrument the actual target and preserve symbols/build identity. Race detection does not prove every schedule or logical effect; fuzz coverage guides input search but supplies no oracle.

A useful fuzz harness reaches the intended public boundary, bounds resources, resets per-input state and reproduces the same failure from the same input. Decode bytes without introducing harness-level alignment, bounds or aliasing faults. Use structured inputs or seeds when raw bytes fail before the target behavior; retain malformed inputs when rejection is the contract. Catch only expected rejection errors so the harness does not swallow defects. Sequence operations when the relevant fault depends on state.

Set a finite runtime and input-size budget. Confirm instrumentation and target reachability, then retain the minimized reproducer, original artifact when needed, build identity and diagnostic. Distinguish a product failure from a harness fault, unsupported instrumentation, timeout or resource exhaustion. After a fix, replay the same reproducer with an unaffected control; a fresh random run alone does not establish correction.
