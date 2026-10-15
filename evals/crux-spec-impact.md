# crux-spec-impact: evaluation scenarios

Run in a fresh agent session with the built skill installed alone (no other crux skill required), against a scratch Piton project prepared as stated. Record specification hashes before the run.

## Scenario

Seed the same CAD kernel project (topology identity guarantees; modelling operations, parametric references, constraint evaluation, feature history, serialization, and an application interface depending on them in the specification graph). Invoke: 'What would happen if topology entities became immutable?' Expect the proposed change restated, direct effects (entity mutation contracts, topology ownership, lifecycle), downstream effects classified Confirmed / Likely / Possible / Unlikely with reachability never treated as proof, required versus potential versus review-only updates distinguished, conflicts with established guarantees named without being resolved, a recommended change sequence, unresolved decisions, and no file changed in the working project (hash check; any hypothetical modelling done on a temporary copy and reported as such).

## Cross-skill checks

- On the same seeded project, this skill's output is meaningfully different from its neighbours: coverage asks what has been failed to be specified, impact asks what a change would affect, review asks what is unclear or problematic, and arch-dependencies asks whether the dependency structure is healthy.
- Delegation or recommendation of another installed skill is optional, scoped, non-recursive, and never a precondition for the core analysis.

## Live verification result

Passed live, installed alone, on the same seeded CAD kernel. Asked what would happen if topology entities became immutable, the agent identified the direct contradiction with the established create-and-delete requirement, traced downstream effects on parametric reference resolution, modelling, serialization, and the application interface with Confirmed, Likely, and Possible classes (explicitly stating reachability alone proved nothing), separated required, potential, and review-only updates, named conflicts and compatibility consequences, modelled the hypothetical only on an isolated copy outside the working specifications, recommended a change sequence with unresolved decisions first, and changed no working file (hash verified).
