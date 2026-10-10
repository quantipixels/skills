# Actor task: framework invocation

Repair the supplied operation whose direct method test passes while its normal framework entry point violates the supplied persistence or validation contract. Use the project's actual framework version, configuration, build and verification commands. Identify the existing owner and invocation path before changing it.

Preserve the public operation and unaffected callers. Verify the repair through the real container and database, including the specified failure path and the resulting committed state. A direct object invocation or mocked repository may support diagnosis but does not establish this boundary. Add only the focused proof needed; do not upgrade the framework or install dependencies without a separately authorized need.

Return the scoped diff, commands and discovered/executed test results, observed before/after behavior, and any unexercised framework or storage boundary. Explain the mechanism and why the change belongs at the chosen owner.
