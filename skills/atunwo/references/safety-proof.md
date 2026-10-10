# Prove a change is safe

Use when the question is whether a change is safe to merge, or a finding or the author claims it is. Skip it for changes whose risk is plain from the diff.

## Find the deciding facts

Name the one or two facts that would make the change safe or unsafe. Typical ones: what a library version really does for this input, whether a stored or wire value is read elsewhere, whether a framework calls this by name or reflection. Do not list every worry; do not force the question into one fact when two are needed.

## Look past the diff

- Read the behaviour of the library or framework at the version the project pins, not the latest docs.
- Look for hidden consumers: serialised or stored data, wire formats, other services, scripts, config, generated code, reflection, anything that reads the thing by name.
- Check removed or changed defaults, error types and ordering that callers may rely on.

## Climb the evidence ladder only as far as needed

1. A claim (the author or a comment says so).
2. A cited source (the library code or doc at the pinned version).
3. A traced exclusion (you followed callers and found none that break).
4. Executed real code (a small run that shows the behaviour).
5. The running app (the real surface shows it).

Run the cheapest check that settles the deciding fact. Stop climbing when the fact is settled. Say which rung each conclusion stands on. Stay inside the review's execution limits; if the decisive check needs more, name it as the cheapest pre-merge check instead.

## Return

The behaviour change, the safety claim and whether it is proved or unproved, risks that are confirmed, concerns that are cleared and why, and the cheapest check left. Give no invented odds for risks you have not shown.
