# piton-skills

A Piton package that provides skills for working with Piton.

| Skill | What it does |
| --- | --- |
| `crux-project-bootstrap` | Guides a user from a vague project idea to an initial, structured Piton specification through a short, adaptive interview, then lets them accept it or keep refining it in further rounds. |
| `crux-spec-deep-dive` | Takes one selected part of an existing specification — a feature, capability, or subsystem — and develops it into a detailed, precise, implementable specification through a focused, adaptive interview, without expanding its scope. |
| `crux-spec-review` | Critically examines a whole project or a selected part of it for contradictions, ambiguities, missing requirements, and weak assumptions, and produces a prioritized, evidence-backed review with the highest-value unanswered questions. It never modifies specifications. |
| `crux-spec-refactor` | Automatically scans existing specifications for duplication, layout and modularity problems, and other refactoring opportunities, presents a numbered proposal list for the user to select from and add to, and applies only approved transformations, verifying against a semantic baseline that effective requirements and public exports are preserved exactly. |
| `crux-spec-develop` | Transforms an idea, feature request, technical question, or high-level requirement into a well-researched, appropriately detailed specification, balancing research, decomposition, and focused clarification, delegating to the other crux skills where they fit, and integrating only authorized changes. |
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

They share one abstract base, `spec/skills/lib/CruxArchBase.pi`, itself
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

This installs the package's `spec/` tree into `tethers/piton-skills/`
and records it in `.piton/tether.lock`. To choose only this package
when the repository offers several, list it under the URL in the
consuming project's `dependencies`:

```piton
dependencies:
    - <git-url-of-this-repository>
        packages: [piton-skills]
```

## Use

Import the skills you want from the package entry and re-export them
from your project's entry file, so your build emits them:

```piton
from piton-skills import MySkill
export MySkill
```

or take everything the package exports:

```piton
from piton-skills export *
```

Then run `piton build` in the consuming project. Each skill is emitted
by the consuming project's adapters into that tool's skill directory.

## Layout

| Path | Purpose |
| --- | --- |
| `piton.config.pi` | Project config: source root, entry, Belay preview build, and the `piton-skills` package declaration. Not installed. |
| `spec/index.pi` | Package entry. Everything a consumer can import is re-exported here. |
| `spec/skills/index.pi` | Skills index. Every skill file is re-exported here. |
| `spec/skills/*.pi` | One skill per file, named after the skill anchor. |
| `spec/skills/lib/PitonSkillBase.pi` | Abstract base every skill extends. It is never compiled or emitted on its own; its shared properties are inherited by each concrete skill and serialized as sections after that skill's own prompt. |
| `evals/` | Conversational evaluation scenarios for the skills, run in a live agent session. Static checks do not substitute for them. |

Only the tree under the package `root` (`spec/`) is installed into
`tethers/piton-skills/`. The adapters in `piton.config.pi` only drive
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
