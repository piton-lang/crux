# crux-arch-interfaces: evaluation scenarios

Run in a fresh agent session with the built skill installed (alone, without the other architecture skills, to prove independence), against a scratch Piton project prepared as stated. Record specification hashes before the run where modification is in question.

## Scenario

With topology, geometry, and operations anchors seeded, invoke: 'Define the interface between topology and geometry.' Expect components and boundary, explicit ownership (state, validation, persistence, lifecycle, errors), operations with inputs/preconditions/outputs/guarantees, invariants, and failure semantics including atomicity; only relevant dimensions used; conflicts with existing requirements named; output as a proposal with no file changed unless the user then authorizes 'add these contracts to the specs', after which Piton changes validate.

## Independence and collaboration checks

- The skill works when the other four architecture skills are not installed.
- When a subtask genuinely belongs to another installed skill, it is discovered and delegated to with a narrow objective, or recommended, without a recursive loop and without surrendering the primary result.
- Proposals, alternatives, assumptions, and research findings are never presented as confirmed requirements or decisions; nothing is modified without authorization.

## Live verification result

Passed live, installed alone. On 'Define the interface between topology and geometry', the agent produced the boundary, proposed responsibility ownership (Topology solely owning persistent identity, Geometry forbidden from mutating topology), behavioral capabilities, input/output contracts, invariants, failure semantics, unresolved decisions, and Piton changes presented as a proposal only, explicitly not an established decision. No file changed (hash verified).
