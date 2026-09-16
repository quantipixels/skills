# C13 — selective TDD and component judgment

**Observation:** selection probe  
**Instruction source:** supplied candidate  
**Workspace:** none; no implementation, test execution or workers

For each independent case, describe the bounded next action and accepting evidence. Do not claim to have executed it.

1. A reproducible settlement retry defect duplicates a durable ledger effect. A faithful public-boundary test can distinguish one effect from two. Existing tests miss the case.
2. An HTTP security configuration permits an unauthenticated administrative action. A real local HTTP fixture can reproduce it. The change is only a configuration line.
3. A symbol rename is covered by existing consumer compilation and behavior tests. No new behavior or uncovered failure is identified.
4. The user explicitly requires test-first development for a change you would otherwise verify with sufficient existing checks.
5. A proposed RED failed because a fixture import was missing; after fixing setup the original already passes. Another run selected zero tests. A third test was first executed after the repair. Which claims can these establish?
6. A proposed property test generates only positive values, while an existing regression covers zero. A separate integration test never reaches that rejection path. A third old example is fully covered by a retained boundary check that rejects its realistic failure. Judge the proposed consolidation without a suite-wide cleanup.
7. Two packages repeatedly change together because each owns half of one policy, and their build dependencies form a cycle. Identify the concrete evidence needed before changing their boundary.
8. A cohesive framework-native module owns one stable use case; no consumer takes unrelated capability. Would component principles require new interfaces or folders?
9. A proposed architecture defers storage choice, but the accepted recovery requirement may be impossible under one candidate's durability guarantees. What must be investigated now?
