When *creating or updating* a skill, use `ko-skill`.

[`alarina`](./skills/alarina/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a docs page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read alarina's SKILL.md and update it so the map stays accurate — a new skill it never mentions, or a stale one it still routes to, is a router that lies.
