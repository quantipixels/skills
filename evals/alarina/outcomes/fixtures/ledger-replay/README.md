# Harbor ledger

`record(entries, event_id, amount)` stores a positive integer amount for an event and returns the total. A replay with the same event ID and amount returns the unchanged total. Reusing an event ID with a different amount must raise `ValueError` and preserve the entries. Different event IDs remain independent. Data is in memory; there are no live effects or services.

The caller guarantees that `amount` is a positive integer. Behavior outside that input domain is unspecified, and input validation is outside this function's responsibility. Readiness for this module depends on the replay contract above, not on introducing a new invalid-input rejection policy.

Run unit coverage with `python3 -m unittest discover -s unit`. Run the public contract with `python3 -m unittest discover -s contracts`. CI exercises both on Linux and Python 3.12. No dependencies beyond Python are required.
