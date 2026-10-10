# Exploring directions and narrowing with the user

## Critical abstractions, interfaces and features

When a choice will be costly to change later (a core abstraction, a public interface, a data model, a key feature's mechanism) and the best shape is unclear, build tiny throwaway versions before committing. Build two independent versions from the same brief as a delegated race (`asoju` sets the models), each in its own scratch path. Keep each just big enough to exercise the hard part: a few real call sites, the awkward case, the failure path. Judge on criteria set beforehand (caller simplicity, what the interface hides, how it handles the hard case, cost to change), read both yourself, and recommend one or a combination.

## Variants

Build the number the user asks for. For a UI prototype with no number given, build three that differ in idea (layout, flow or interaction model), not just colour or copy; build one only when asked or when the question has a single answer to check. For other prototypes, choose a range proportionate to the uncertainty; ten cosmetic variations rarely clarify ten possibilities. Give variants stable labels and say what idea each explores. Keep them comparable on the current question and at enough fidelity for useful reactions. Use design or implementation skills for craft while keeping the work disposable.

Match the experiment to its surroundings. For interface variants, use representative content, density and navigation in an isolated preview; an empty standalone screen can hide the real design problem. Keep comparison easy without requiring a particular layout or saved URL state. Stub effects outside the question and avoid real mutations.

For behaviour or state exploration, expose the state in the user's vocabulary and show what each action changed. Allow free exploration and, when useful, a short guided difficult case from a resettable baseline. Check that the demonstrated transitions follow the candidate rules; a broken demo must not decide against a sound idea. Make the artifact easy to open or run.

## Narrowing

Present an inspectable or runnable path and a focused feedback prompt. Let the user say what works, what fails, what is missing and why; they may keep parts of several variants, reject all, or reveal a different need. Record actual reactions separately from your interpretation; silence or an agent's ranking is not user preference.

Use each round to eliminate weak directions, keep the reasons behind preferences and combine compatible strengths. Make the next round smaller when evidence supports narrowing. Verify combinations as a whole: parts liked alone may conflict when joined. Introduce a new direction when feedback exposes a gap rather than forcing a winner. Example: ten distinct designs, three preferred directions, two combined prototypes, one refined direction; counts and rounds follow the feedback, not a quota.

Update the emerging brief as understanding changes. Keep settled preferences unless new feedback challenges them, and make consequential changes in the question visible. Continue until the user confirms the direction and the needs it serves, ends the exploration, or a concrete gap blocks useful work. If feedback is pending, leave the choice open.
