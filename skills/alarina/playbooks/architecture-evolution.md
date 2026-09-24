# Architecture evolution

Use for recurring design/dependency friction, an engineering health assessment, dependency or framework upgrades, or a selected structural improvement. Preserve an audit-only or recommendation-only stopping point. For upgrades, `architect` assesses version compatibility, migration cost and consumer obligations through its architecture-evolution method.

1. Give `architect` the concrete friction and affected consumers. Its survey assesses ownership, interfaces, invariants, technology fit and the rationale for current choices. Use `alaga` for a material external evidence gap; use `atunwo` when the requested result is independent code judgment rather than design.
   When component or policy boundaries drive the friction, use Architect's module-design lenses to establish the concrete dependency/change cost. Sound cohesive or framework-native structure is a valid outcome; principle names do not authorize a redesign.
2. Resolve whether the change earns its migration and maintenance cost. `alaga` can test a consequential uncertain benefit; an already-supported choice needs no experiment. Consider end-user, developer and agent experience without trading away the first two merely to make agent navigation easier.
3. Return the findings and alternatives for an audit-only request. For authorized delivery, `atona` owns any necessary phased plan and combined acceptance; a bounded accepted refactor goes directly to `alaga`.
4. `alaga` preserves the required behavior, migrates real callers and verifies the selected improvement using its existing methods. Retain supported compatibility until its consumers can migrate. Use `atunwo` when independent scrutiny is requested or material, reusing valid evidence.

Finish with the requested recommendation or a verified structural improvement and its remaining costs. Fewer files, lower metrics or a newer dependency alone do not establish improvement. Publish only within existing authority.
