# crux-spec-coverage: evaluation scenarios

Run in a fresh agent session with the built skill installed alone (no other crux skill required), against a scratch Piton project prepared as stated. Record specification hashes before the run.

## Scenario

Seed one CAD kernel project (geometry, topology with creation/deletion/reference preservation but no merge, split-successor, deleted-reference, recovery, or history behaviour; Booleans with normal behaviour only and no coincident/tangential/degenerate scenarios or acceptance criteria; rendering explicitly excluded and detailed fillet tolerances intentionally deferred). Invoke: 'Evaluate coverage of our topology and Boolean specifications.' Expect a coverage summary, a matrix with Covered / Partially covered / Missing / Not applicable / Unknown statuses (rendering marked excluded or not applicable, never a gap), prioritized gaps with capability, missing scenario, why it matters, spec references, priority and confidence, likely omissions distinguished from optional extensions, no arbitrary percentage, recommendations pointing at crux-spec-develop or crux-spec-deep-dive without invoking them, and no file changed (hash check).

## Cross-skill checks

- On the same seeded project, this skill's output is meaningfully different from its neighbours: coverage asks what has been failed to be specified, impact asks what a change would affect, review asks what is unclear or problematic, and arch-dependencies asks whether the dependency structure is healthy.
- Delegation or recommendation of another installed skill is optional, scoped, non-recursive, and never a precondition for the core analysis.

## Live verification result

Passed live, installed alone, on the shared seeded CAD kernel. The review produced a coverage summary and matrix, distinguished missing merge and split-successor behaviour, deleted-reference and identifier-reuse semantics, degenerate and coincident Boolean configurations, invalid inputs, failure and atomicity behaviour, and observable acceptance criteria as prioritized gaps with priorities and confidence, treated rendering as excluded rather than a gap, issued no arbitrary completeness percentage, recommended crux-spec-develop or crux-spec-deep-dive without invoking them, and changed no file (hash verified).
