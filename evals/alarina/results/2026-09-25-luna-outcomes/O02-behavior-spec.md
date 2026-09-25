# CSV account import behavior

**Result:** `SPEC_READY`

## Contract

Import CSV rows by account ID. The input is handled as one unit: if any row is invalid or any ID is duplicated within the input, reject the entire import and make no partial writes. An ID already present in the system updates that account; an ID not present creates an account. A successful import applies every valid row. Empty input succeeds as a no-op.

When the import is rejected, the error output identifies the input row number or numbers responsible. Row numbering uses the CSV input's row positions, including the header row if present; the header convention is not specified, so implementations must use the input's established CSV row-number convention consistently. The import still identifies the offending input rows.

## Acceptance examples

- Given rows with IDs `A-17` and `B-42`, neither previously present, importing both succeeds and creates both accounts.
- Given one row with ID `A-17` and an existing account `A-17`, importing the row succeeds and updates that account.
- Given two rows in the same input with ID `A-17`, the import rejects the whole input, reports the duplicate row numbers, and writes nothing.
- Given a valid row followed by an invalid row, the import rejects the whole input, identifies the invalid row number, and writes nothing, including no write for the valid row.
- Given empty input, the import succeeds and changes no accounts.

## Acceptance and proof

- Every nonempty accepted input has unique IDs and valid rows; all its rows are applied, updating existing IDs and creating absent IDs.
- Any invalid row or within-input duplicate rejects the whole input; no account is partially changed or created.
- Rejection output identifies the input row numbers responsible.
- Empty input succeeds without writes.

Verify at the import boundary with examples that inspect both the result and account state after success and rejection. The exact storage technology and authorization rules are outside this contract.

## Source and limits

Source: supplied accepted decisions in the O02 request. No implementation, header convention, invalid-row taxonomy, or authorization policy was supplied. The examples are acceptance examples derived directly from those decisions. The row-number display convention is left to the established CSV input contract; the requirement to identify input rows is settled.
