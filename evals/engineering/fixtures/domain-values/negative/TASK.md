# Add an internal layout choice

Add `COMPACT` to the internal layout preference with exact token `compact`.
Keep `comfortable` unchanged. Uppercase, aliases, whitespace and unknown inputs remain invalid
and must throw `IllegalArgumentException`; the wire contract of account state is unchanged.

Inspect nearby enum conversion before choosing the implementation. Change only `LayoutChoice.java`;
you may add focused tests. Keep `WireValues.java` unchanged. Use the available JDK; no dependencies.
Return the implementation, executed checks and why the chosen boundary fits this contract.
