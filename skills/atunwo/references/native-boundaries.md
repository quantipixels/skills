# Native and foreign-function boundaries

Read only when native memory, unsafe code or FFI is material to the requested review. Keep atunwo's scope and evidence standard; a suspicious cast or an unsafe block is not itself a defect.

Trace the affected safe/public entrypoint to the unsafe operation. State the operation's actual preconditions and find their enforcement: allocation lifetime, bounds, alignment, initialization, aliasing and valid representations as applicable. Account for type and ownership guarantees before requesting runtime checks. A comment or debug-only assertion cannot enforce a precondition missing from a safe interface in release behavior. An unsafe interface may legitimately transfer documented obligations to its callers; verify the relevant caller satisfies them.

At an FFI seam, compare both declarations and the actual target ABI. Follow buffer length and ownership together: who allocates, retains, mutates and frees it, with which allocator, and for how long? Inspect callback lifetimes, reentrancy and permitted unwind behavior. Do not assume a foreign integer is a valid language enum or that an internal layout is a portable wire representation. Verify language-specific rules rather than treating every pointer cast or metadata conversion as unsound.

Trace exceptional cleanup as carefully as success: partial initialization, early return, cancellation, double release and use after ownership transfer. Separate memory-safety guarantees from deadlock, leaked resources and business-level duplicate effects. A race-free execution can still violate the operation's contract.

For a supported risk, name a distinguishing input or schedule and the proof tool that can observe it. Use the project's existing fuzzing, sanitizer or race-detector capability when authorized. A clean sampled run does not prove all unsafe preconditions. Optimizer-sensitive cryptographic timing or secret erasure needs specialist, target-specific evidence; do not certify it from source appearance.

Language rules: [Rustonomicon FFI](https://doc.rust-lang.org/nomicon/ffi.html).
