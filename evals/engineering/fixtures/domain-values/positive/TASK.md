# Add a delivery state at the external boundary

Add the `PAUSED` delivery state with canonical wire value `paused` and legacy alias `hold`.
Preserve all current delivery/account round trips, case handling and unknown-value behavior.
Existing configured aliases must remain effective for new values as well as old ones.

Inspect the analogous external-value path before editing. Change only `DeliveryBoundary.java`;
you may add focused tests. Keep `WireValues.java` unchanged. Use the available JDK; no dependencies.
Return the implementation, executed checks and the analogous boundary you followed.
