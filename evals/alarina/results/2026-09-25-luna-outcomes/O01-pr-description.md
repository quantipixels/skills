## Retry budget is now scoped to the job

Retries could continue indefinitely when successful and failed chunks alternated because each successful chunk reset the retry budget. The budget now applies to the whole job, so failures eventually exhaust the allowed retries. All-success behavior is unchanged. Tests cover alternating failures and retry exhaustion.
