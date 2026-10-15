# crux-arch-explore: evaluation scenarios

Run in a fresh agent session with the built skill installed (alone, without the other architecture skills, to prove independence), against a scratch Piton project prepared as stated. Record specification hashes before the run where modification is in question.

## Scenario

Explore architectures in a seeded CAD kernel project (exact geometry, robustness first, standalone). Invoke: 'Explore architectures for our topology system.' Expect 2-4 genuinely distinct approaches (not superficial variants), each explained by concept, components, boundaries, data flow, state ownership, dependencies, strengths/weaknesses and implications; a project-specific comparison; a recommendation conditioned on assumptions or an honest no-recommendation; unresolved decisions and next steps; and no specification file changed (hash check) without selection plus authorization.

## Independence and collaboration checks

- The skill works when the other four architecture skills are not installed.
- When a subtask genuinely belongs to another installed skill, it is discovered and delegated to with a narrow objective, or recommended, without a recursive loop and without surrendering the primary result.
- Proposals, alternatives, assumptions, and research findings are never presented as confirmed requirements or decisions; nothing is modified without authorization.

## Live verification result

Passed live, installed alone. On 'Explore architectures for our topology system', the agent produced the problem and constraints, genuinely distinct topology approaches, a project-specific comparison respecting exact geometry and robustness-first priorities, a conditional recommendation favouring a manifold half-edge B-rep with provenance-based persistent identifiers, unresolved decisions, and next steps. No file changed (hash verified).
