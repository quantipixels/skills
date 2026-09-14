# Units, scale and numeric meaning

Use for numeric correctness in diagnosis, implementation or review; retain the caller's authority. Trace only the relevant calculation and its input/output boundaries. No annotation pipeline or repository-wide inventory is required.

For each material quantity establish its dimension, unit, stored scale, semantic basis, numeric representation and valid range. Names are clues; schemas, contracts and producers settle meaning. Equal physical dimensions do not imply equal semantics: currency, valuation date, gross/net basis and coordinate frame can differ.

Addition and comparison need compatible units, scale and basis. Multiplication/division compose dimensions; track powers of ten separately from physical units. Make conversions explicit at the owning boundary and check both directions with known values. A conversion round-trip alone can hide two inverse mistakes.

Trace integer truncation, intermediate overflow, signedness, decimal rounding location/mode, zero denominators and floating-point special values where the domain admits them. A widened result type does not repair overflow in an earlier narrow operation. Rearranging multiplication/division may change precision or overflow even when algebra is equivalent. Derive tolerances from the contract's representation and error budget rather than choosing an epsilon that makes a failure pass.

Use bounds, conservation, monotonicity or scale relations when the contract supports them; read [property-based testing](property-based-testing.md) for generators and counterexamples. State uncertainty where units or basis cannot be established. Keep application-specific tax, payment or device rules in project verification/domain records.
