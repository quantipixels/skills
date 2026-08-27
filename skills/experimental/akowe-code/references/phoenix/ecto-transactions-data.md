# Phoenix Ecto transactions and data access

Use when the candidate changes Repo/Ecto queries, changesets, transactions, preloads, concurrency, or remote side effects.

<a id="phx-ecto-transaction"></a>
## `phx-ecto-transaction` — Keep local DB atomicity around one owned use case

Use `Repo.transaction`/`Ecto.Multi` when several DB changes form one local invariant. Do not stretch a transaction across unrelated user/network work.

<a id="phx-ecto-remote"></a>
## `phx-ecto-remote` — Keep irreversible remote effects outside local transactions

A database rollback cannot undo email/HTTP/broker/provider effects. Persist durable intent/outbox state or design explicit compensation/idempotency when coordination is required.

<a id="phx-ecto-query-shape"></a>
## `phx-ecto-query-shape` — Own query cardinality and fetch shape

Bound result size and select/preload only what the use case needs. Detect hidden N+1 access instead of relying on incidental association loading.

<a id="phx-ecto-changeset"></a>
## `phx-ecto-changeset` — Separate external validation from domain/data invariants

Changesets are useful validation/change contracts, but do not expose raw internal changeset shape as a public API automatically. Keep invariants at the owner that can enforce them.

<a id="phx-ecto-concurrency"></a>
## `phx-ecto-concurrency` — Make optimistic/pessimistic/idempotency semantics explicit

When multiple requests/jobs can update the same business state, choose the actual DB/application coordination mechanism and prove conflict/retry behavior.

## Sources

- Ecto: <https://hexdocs.pm/ecto/>
- Ecto.Repo: <https://hexdocs.pm/ecto/Ecto.Repo.html>
- Ecto.Multi: <https://hexdocs.pm/ecto/Ecto.Multi.html>
