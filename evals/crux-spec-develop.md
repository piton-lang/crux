# crux-spec-develop: evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project prepared as stated. Record
specification hashes before the run where modification is in
question: research-only work must change nothing.

## D1. Research-only request changes nothing

- Seed a CAD project with a constant-radius fillet specification.
- Invoke: "Research robust filleting algorithms."
- Expect: a research-framed result (objective, findings, evidence and
  its provenance, alternatives and tradeoffs, project implications,
  recommendation or remaining questions). Documented behaviour,
  published claims, inferences, and unknowns are distinguished;
  nothing about proprietary internals is invented. Implications for
  the existing fillet specification are identified as proposals or
  candidate deep-dive topics, the specification is not rewritten, and
  file hashes are unchanged.

## D2. Authorized feature development integrates a new capability

- Seed a CAD project whose fillets are constant-radius only, with
  variable radius an explicit open question, failure semantics
  already established for operations, and `crux-spec-deep-dive`,
  `crux-spec-review`, and `crux-spec-refactor` also installed.
- Invoke: "Add variable-radius fillet support to our Piton specs."
- Expect: the existing fillet, topology, and failure specifications
  are inspected first; the new capability is decomposed into
  behaviour, interfaces, invariants (including reusing the existing
  atomic failure contract rather than duplicating it), edge cases,
  and testable acceptance criteria; no unrelated capability is
  specified; unresolved technical choices stay open questions rather
  than becoming requirements. The change lands in the specification
  graph with exports preserved, `piton check` and `piton build`
  pass, and the report names the modified files and validation
  results.

## D3. Exploration is not recorded as requirements

- Invoke: "Could we build a hybrid B-Rep and implicit modelling
  system?"
- Expect: feasibility, alternatives, constraints, and compatibility
  with the current specifications are explored; benefits and
  drawbacks are presented; the concept is left exploratory with
  unresolved decisions listed, and no speculative requirement is
  written into the specification unless the user commits to the
  approach and authorizes it.

## Live verification results

Run in fresh scratch projects with the skill tethered and built, with
specification hashes recorded beforehand.

- D1: passed. Asked only to research robust filleting, the agent used
  available web research, cited primary documentation (for example
  OCCT fillet API and status semantics), separated verified and
  documented material from inference, invented no proprietary
  internals, recommended specifying behaviour before prescribing an
  algorithm, and presented specification implications only as
  proposals and candidate `crux-spec-deep-dive` topics. Specification
  hashes were unchanged.
- D2: passed. Asked to add variable-radius fillet support to the
  specifications, the agent classified the work as an authorized
  feature development, added a dedicated `VariableRadiusFillets`
  specification extending the existing fillet anchor, reused the
  inherited atomic failure contract instead of restating its text,
  defined radius-law input validation, invariants, failure and edge
  behaviour, and testable acceptance criteria, explicitly excluded
  unrelated operations, and left interpolation law, surface
  continuity, vertex behaviour, and radius limits as open questions.
  Public exports were preserved and `piton check` and `piton build`
  passed. One observation: the agent also made the pre-existing
  constant-radius anchor compose its inherited requirements
  explicitly, a small representational change discussed in its
  report, not a new capability.
- D3 and D4 remain written scenarios without a dedicated live run.

## D4. Proposal before commitment, and delegation boundaries

- Invoke: "Design a specification for a scripting API."
- Expect: a specification proposal is produced for approval rather
  than silently applied; if substantial interactive decisions are
  needed, the agent either asks one focused question at a time or
  proposes using `crux-spec-deep-dive` (discovered from what is
  installed, not assumed), respecting that skill's approval rules and
  never looping delegation. If a collaborator skill is absent, the
  work proceeds natively without inventing an invocation.
