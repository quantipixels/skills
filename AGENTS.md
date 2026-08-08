When *creating or updating* a skill, use `ko-skill`.

[`alarina`](./skills/alarina/SKILL.md) is the router that maps every user-reachable skill and how they relate. The canonical public catalog is [`../web/public/skills.html`](../web/public/skills.html); do not create a second public copy in this repository. Whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read alarina's SKILL.md and update both the router and the public catalog so neither one becomes stale.
