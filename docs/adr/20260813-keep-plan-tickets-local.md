# Keep plan tickets local — superseded

This decision is no longer current. It coupled `seda-ticket` to Atona plans, HTML persistence, durable graph identity, and a durable graph-node lifecycle.

The confirmed replacement keeps `seda-ticket` focused on decomposition: it turns supplied work into consumable vertical tickets with acceptance, blocking edges, and a small portable state vocabulary. Callers own grouping, durable identity, persistence, publication, and transition authority. The replacement does not restore the prior graph or persistence architecture.
