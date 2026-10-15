# crux-arch-dependencies: evaluation scenarios

Run in a fresh agent session with the built skill installed (alone, without the other architecture skills, to prove independence), against a scratch Piton project prepared as stated. Record specification hashes before the run where modification is in question.

## Scenario

Seed anchors where modelling imports topology and geometry, topology references rendering helpers, and two anchors reference each other. Invoke: 'Analyze dependencies across the project.' Expect imports, inheritance, composition, interface, data, runtime and external dependencies distinguished (a Piton import not equated with a runtime dependency), reach/slice evidence used, coupling, the cycle, any bottleneck and inappropriate direction reported with whether the cycle is legitimate, prioritized improvements with benefit/affected components/compatibility cost, and no false-positive violation claimed for legitimate structure. Read-only unless changes are approved.

## Independence and collaboration checks

- The skill works when the other four architecture skills are not installed.
- When a subtask genuinely belongs to another installed skill, it is discovered and delegated to with a narrow objective, or recommended, without a recursive loop and without surrendering the primary result.
- Proposals, alternatives, assumptions, and research findings are never presented as confirmed requirements or decisions; nothing is modified without authorization.

## Live verification result

Passed live, installed alone. On 'Analyze dependencies across the project', using reach and slice evidence, the agent distinguished dependency types, found the only cycle to be a legitimate documentation-reference cycle between Topology and Rendering rather than a runtime cycle (noting slice output alone would overstate propagation), and reported coupling, bottlenecks, risks, prioritized improvements, change-impact, and affected specifications. No file changed (hash verified).
