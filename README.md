# crux

A Piton package that provides skills for working with Piton.

| Skill | What it does |
| --- | --- |
| `crux-spec-deep-dive` | Takes one selected part of an existing specification — a feature, capability, or subsystem — and develops it into a detailed, precise, implementable specification through a focused, adaptive interview, without expanding its scope. |
| `crux-spec-review` | Critically examines a whole project or a selected part of it for contradictions, ambiguities, missing requirements, and weak assumptions, and produces a prioritized, evidence-backed review with the highest-value unanswered questions. It never modifies specifications. |
| `crux-spec-refactor` | Automatically scans existing specifications for duplication, layout and modularity problems, unnecessary complexity, and other refactoring and simplification opportunities, presents a numbered proposal list for the user to select from and add to, and applies only approved transformations, verifying against a semantic baseline that effective requirements and public exports are preserved exactly. |
| `crux-spec-develop` | Transforms a project idea, however vague, a feature request, technical question, or high-level requirement into a well-researched, appropriately detailed specification, including structured feature proposals that remain proposals until accepted, balancing research, decomposition, and focused clarification, delegating to the other crux skills where they fit, and integrating only authorized changes. For a new project it runs a short, budgeted interview to an initial specification, then lets the user accept it or keep refining it in further rounds. |
| `crux-impl-reconcile` | Compares a project's Piton specifications with its actual implementation, classifies divergences (missing, contradictory, partial, undocumented, outdated, ambiguous, unverified, structural), and recommends for each whether to change the implementation, change the specification, or investigate further. Diagnostic by default, and the home of drift detection. |
| `crux-spec-coverage` | Systematically evaluates whether specifications cover their claimed capabilities, behaviors, scenarios, boundaries, failure conditions, and acceptance criteria, and prioritizes the gaps without inventing a completeness score. Read-only by default. |
| `crux-spec-impact` | Analyzes the direct and downstream consequences of a proposed specification change across requirements, interfaces, dependencies, and contracts before it is applied, separating confirmed impact from possible impact. Read-only by default. |
| `crux-ui-develop` | Interviews the user about which part of the UI to work on and how it should work, then runs mockup rounds: it asks how many variations to make, saves them numbered 1, 2, 3 next to the spec file in a `<Spec>.mockups/round-N/` folder with one gallery page to compare and dive into them, and records the picked number and what it settled in the specification, which references the mockup files. |

## Analysis skill boundaries

| Skill | Question it answers |
| --- | --- |
| `crux-spec-review` | What is unclear, contradictory, or problematic in these specifications? |
| `crux-spec-coverage` | What behaviors and scenarios have we failed to specify? |
| `crux-spec-impact` | What happens to our specifications if we change this? |
| `crux-arch-dependencies` | Is the architecture's dependency structure healthy? |

Consolidation between these skills is by optional delegation, never by
mandatory dependency. `crux-spec-review` notes missing behavior at
review level and defers systematic coverage modelling to
`crux-spec-coverage`. `crux-arch-dependencies` keeps dependency-health
analysis and defers the consequences of one specific proposed change
to `crux-spec-impact`. `crux-spec-develop` may use coverage to find
missing behaviors and impact to assess significant proposed changes.
`crux-spec-refactor` may use impact when evaluating a transformation's
consequences, while keeping its own semantic-equivalence verification.
Every skill remains fully usable when none of the others is installed.
| `crux-arch-explore` | Generates, researches, and compares genuinely distinct architectural approaches for a system or subsystem and recommends a direction when evidence supports one. |
| `crux-arch-interfaces` | Defines subsystem boundaries, responsibility ownership, input and output contracts, invariants, and failure semantics. |
| `crux-arch-dependencies` | Analyzes coupling, dependency types, cycles, layering, and bottlenecks, and explains how changes propagate. |
| `crux-arch-tradeoffs` | Compares defined alternatives against explicit hard constraints and project criteria with evidence and sensitivity analysis. |
| `crux-arch-risks` | Challenges architectural assumptions with concrete causal failure scenarios, prioritized mitigations, and validation experiments. |

## Architecture skills overview

The five `crux-arch-*` skills each own one question: what architectures
could solve this problem (`crux-arch-explore`), how should components
communicate and divide responsibility (`crux-arch-interfaces`), how are
components coupled and what changes propagate
(`crux-arch-dependencies`), which alternative best satisfies our
priorities (`crux-arch-tradeoffs`), and what could make this design
fail (`crux-arch-risks`). Each is a separate skill that works on its
own; none requires another.

They share one abstract base, `spec/skills/arch/lib/CruxArchBase.pi`, itself
built on `PitonSkillBase`. The architecture base carries the common
conventions once (distinguishing requirements, decisions, proposals,
alternatives, assumptions, findings, risks, and open questions;
project awareness under Piton semantics; one-question-at-a-time
clarification with no default interview budget; evidence-labelled
research; purposeful delegation to any installed skill, including the
other architecture skills and the `crux-spec-*` skills, with loop
prevention; and the analysis, proposal, and authorized-change
modification policy). Each concrete skill adds only its own workflow
and output. Collaboration is illustrative rather than mandatory: a
topology redesign might explore approaches, delegate detailed
comparison to `crux-arch-tradeoffs`, define contracts with
`crux-arch-interfaces`, audit the result with
`crux-arch-dependencies`, and challenge it with `crux-arch-risks`,
using the smallest set that serves the request.

It is
installed with the Piton package manager and compiled by the consuming
project's own Belay configuration, so it works with whichever adapters
(Claude Code, Codex, OpenCode) that project enables.

## Install

From the consuming project (where its `piton.config.pi` lives):

```bash
piton tether <git-url-of-this-repository>
```

This installs the package's `spec/` tree into `tethers/crux/`
and records it in `.piton/tether.lock`. To choose only this package
when the repository offers several, list it under the URL in the
consuming project's `dependencies`:

```piton
dependencies:
    - <git-url-of-this-repository>
        packages: [crux]
```

## Use

Import the skills you want from the package entry and re-export them
from your project's entry file, so your build emits them:

```piton
from crux import MySkill
export MySkill
```

or take everything the package exports:

```piton
from crux export *
```

Then run `piton build` in the consuming project. Each skill is emitted
by the consuming project's adapters into that tool's skill directory.

## Layout

| Path | Purpose |
| --- | --- |
| `piton.config.pi` | Project config: source root, entry, Belay preview build, and the `crux` package declaration. Not installed. |
| `spec/index.pi` | Package entry. Everything a consumer can import is re-exported here. |
| `spec/skills/index.pi` | Skills index. Re-exports each skill family's index. |
| `spec/skills/spec/` | Specification skills (`crux-spec-*`), one per file, named after the skill anchor, with `index.pi` re-exporting them. `lib/ReadOnlyAnalysis.pi` is the read-only base shared by coverage and impact. |
| `spec/skills/arch/` | Architecture skills (`crux-arch-*`), laid out the same way, with their shared base in `lib/CruxArchBase.pi`. Not exported yet. |
| `spec/skills/impl/` | Implementation skills (`crux-impl-*`). Not exported yet. |
| `spec/skills/lib/PitonSkillBase.pi` | Abstract base every skill extends. It is never compiled or emitted on its own; its shared properties are inherited by each concrete skill and serialized as sections after that skill's own prompt. |
| `spec/skills/lib/Fluency.pi` | Abstract base holding the instruction for reading Piton fluency, inherited through `PitonSkillBase`. |
| `spec/skills/lib/CruxSkills.pi` | The map of which skill owns which question. Emitted as one reference document that every skill links to. |
| `evals/` | Conversational evaluation scenarios for the skills, run in a live agent session. Static checks do not substitute for them. |

Only the tree under the package `root` (`spec/`) is installed into
`tethers/crux/`. The adapters in `piton.config.pi` only drive
this repository's own preview build; they are not part of the package.

## Develop

```bash
piton check
piton format --check
piton build
piton reach
```

Generated output (`.claude/`, `.codex/`, `.agents/`, `.opencode/`,
`dist/`) is derived from the `.pi` source. Never hand-edit it; change
the `.pi` files and rebuild.
