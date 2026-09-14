# Native runtime checks

Use when a concrete memory, parser or concurrency risk needs dynamic evidence beyond ordinary tests. Discover the actual language, compiler, target platform, build profile and existing harness first. Alaga owns harness implementation and regression fixes; atunwo owns independent findings. Do not add instrumentation or dependencies merely to consult this reference.

Select by the observable failure:

- **AddressSanitizer** for supported memory-access and lifetime failures in instrumented native code; **UndefinedBehaviorSanitizer** for its supported undefined-behavior checks. Verify compiler/platform support and instrument the relevant code, not just a wrapper. Preserve symbols and exact build flags for reproduction.
- **Go race detector** for exercised conflicting accesses. `go test -race` is a starting point within a scoped package selection, not evidence that every schedule was explored. It does not detect all logical races or duplicate business effects.
- **Coverage-guided fuzzing** for parsers and input-driven native boundaries: use the repository's libFuzzer/AFL++/cargo-fuzz or native Go infrastructure when suitable. Coverage growth guides input search; it is not a correctness oracle.

A useful fuzz harness reaches the intended public boundary, bounds resources, resets per-input state and reproduces the same failure from the same input. Decode bytes without introducing harness-level alignment, bounds or aliasing faults. Use structured inputs or seeds when raw bytes fail before the target behavior; retain malformed inputs when rejection is the contract. Catch only expected rejection errors so the harness does not swallow defects. Sequence operations when the relevant fault depends on state.

Set a finite runtime and input-size budget. Confirm instrumentation and target reachability, then retain the minimized reproducer, original artifact when needed, build identity and diagnostic. Distinguish a product failure from a harness fault, unsupported instrumentation, timeout or resource exhaustion. After a fix, replay the same reproducer with an unaffected control; a fresh random run alone does not establish correction.

Sources: [Clang ASan](https://clang.llvm.org/docs/AddressSanitizer.html), [Clang UBSan](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html), [Go race detector](https://go.dev/doc/articles/race_detector), [Go fuzzing](https://go.dev/doc/security/fuzz/).
