# crux

A Piton package that provides skills for working with Piton.

| Skill | What it does |
| --- | --- |
| `crux-spec-describe` | Takes descriptions and statements about what to build, one at a time, and writes each one into the specification. After each statement it places the requirement, resolves conflicts with the user, refactors to keep the specification simple, validates the build, and asks for the next statement. |
| `crux-spec-develop` | Transforms a project idea, however vague, a feature request, technical question, or high-level requirement into a well-researched, appropriately detailed specification, including structured feature proposals that remain proposals until accepted, balancing research, decomposition, and focused clarification, and integrating only authorized changes. For a new project it runs a short, budgeted interview to an initial specification, then lets the user accept it or keep refining it in further rounds. |

The package is installed with the Piton package manager and compiled by the consuming
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
from crux import CruxSpecDevelop
export CruxSpecDevelop
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
| `spec/skills/spec/` | Specification skills (`crux-spec-*`), one per file, named after the skill anchor, with `index.pi` re-exporting them. |
| `spec/skills/lib/BaseSpecSkill.pi` | Abstract base every skill extends. It is never compiled or emitted on its own; its shared properties are inherited by each concrete skill and serialized as sections after that skill's own prompt. |
| `spec/skills/lib/PitonFluency.pi` | Abstract base holding the instruction for reading Piton fluency, inherited through `BaseSpecSkill`. |
| `spec/skills/lib/SpecWriting.pi` | Abstract base holding the guidance for reading and changing Piton specifications, inherited through `BaseSpecSkill`. |
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
