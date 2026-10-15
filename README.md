# piton-skills

A Piton package that provides skills for working with Piton.

| Skill | What it does |
| --- | --- |
| `project-bootstrap` | Guides a user from a vague project idea to an initial, structured Piton specification through a short, adaptive interview, then lets them accept it or keep refining it in further rounds. |

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
