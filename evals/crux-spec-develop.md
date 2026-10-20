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

## D5. Question-budget kickoff defaults to 5

- Seed any project with an underdefined existing capability.
- Invoke: "Add sheet metal support."
- Expect: before any clarification question of its own, the agent
  asks how many questions the user would like to use to develop the
  specification, recommends 5 as the default, and treats accepting
  the default (Enter or a natural reply) as choosing 5. That choice
  is not counted as a question. Questions then arrive exactly one
  per turn with progress such as `Question 2 of 5`; clarifications
  and examples do not consume budget; a substantive answer or an
  explicit skip does. The agent may spend fewer than 5 when the
  project already settles what matters, but never asks a sixth, and
  never spends one on information already established. When the
  budget ends, it proceeds to research, decomposition, and the
  proposal or authorized integration, recording leftovers as open
  questions. Choosing a different number (including no questions) is
  respected exactly.

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
- D5: passed live. On "Add sheet metal support", the first
  substantive response asked how many questions to use to develop
  the specification with a default of 5, before any clarification
  question; the default was accepted and not counted. Questions
  followed one per turn with `Question N of 5` markers, four were
  spent, and the fifth was deliberately not spent because atomic
  failure was already established by the existing Operations
  specification rather than re-asked. The run ended with a sheet
  metal specification proposal for approval and no file modified,
  confirmed by hashes.
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

## D6. Structured feature proposal stays a proposal

- Seed an established CAD kernel (solids, topology, Booleans; CAM an explicit non-goal).
- Invoke: "Propose adding sheet metal support."
- Expect: a structured, decision-oriented proposal (what it adds, why it belongs, what it requires, which existing specifications would change, uncertainties, tradeoffs, proposed initial scope, recommended next action) with the choices accept, revise, defer, or reject. No specification file changes (hash check). Revising updates the one proposal; rejecting leaves normative specifications unchanged; accepting integrates it under the skill's usual authorization, reuse, and validation rules.

- D6: passed live. On 'Propose adding sheet metal support', the agent produced a structured decision-oriented proposal with accept, revise, defer, and reject choices, performed the impact reasoning inline because crux-spec-impact was not installed (without requiring it), and changed no specification file (hash verified).

## New-project scenarios

These cover starting a project from an idea, formerly the separate
crux-project-bootstrap skill. Run them in an empty scratch Piton
project. The live results below predate the merge and were recorded
against crux-project-bootstrap; rerun them against crux-spec-develop.

### P1. Cold start, default budget

- Say only: "I want to build a CAD kernel."
- Expect: the agent first asks how many questions to use, recommends
  5, and does not ask a project question in the same turn. Accepting
  with Enter or "sure" starts Question 1 of 5 without re-asking what
  the project is, since the idea was already given.
- Expect exactly one question per turn and a `Question N of 5`
  progression, with each new question visibly building on prior
  answers (for example, domain before capabilities before tradeoffs).
- After answer 5: no further discovery questions. A minimal Piton
  specification is written, `piton check` and `piton build` pass on
  it, and the turn ends with a summary, remaining unknowns, the file
  location, and the Good enough / Keep going choice.

### P2. Pre-described project, custom budget

- Describe the project fully in the invocation, then ask for 3
  questions.
- Expect: the agent does not re-ask the project's identity, spends all
  3 questions on gaps in the given description, and stops at 3 even
  though uncertainty remains, recording it as open questions.

### P3. Clarifications, skips, and unknowns

- Mid-round, ask "Can you give me an example?" and later "I don't
  know", then skip a question.
- Expect: the example is given without advancing the counter, the
  unknown is carried as an unresolved/open question (never turned into
  a stated requirement), the skip counts as answered, and the round
  still ends on budget.

### P4. Keep going and revision

- Finish a round, choose Keep going, accept the default of 5 more.
- Change an earlier decision ("actually support artistic modeling
  too").
- Expect: no previously answered question is repeated, the same
  specification file is updated in place, statements contradicting the
  new decision are removed or revised, unrelated requirements survive,
  and the round again ends with Good enough / Keep going.

### P5. Early stop and resume

- Stop the interview after 2 of 5 answers and ask to keep the work.
  End the session. Start a new session in the same project and invoke
  the skill again.
- Expect: the best specification possible from the 2 answers is
  offered or generated, and on resume the agent inspects the project
  and its recorded state, resumes the round without repeating the 2
  answered questions, and distinguishes this from a completed round
  awaiting the Good enough / Keep going decision.

### New-project live verification results

Run in fresh scratch projects with the skill tethered and built, each
turn and generated file inspected, and each generated specification
re-validated independently afterwards.

- P1 (CAD kernel, default budget, Good enough): passed. Fluency
  command exited 0; the question-count ask preceded Question 1 of 5,
  the given project idea was never re-asked, exactly one question was
  asked per turn across 5 questions, and no sixth question followed.
  The generated minimal Piton project passed `piton check` and
  `piton build`, contained only what the answers established, and
  recorded the remaining unknowns as open questions. The session
  closed with the summary, unknowns, file location, and the
  Good enough / Keep going choice; Good enough was chosen.
- P2 to P5 (recipe manager, combined run): passed. A custom budget of
  3 was respected, a "don't know" and an explicit skip stayed as open
  questions without consuming extra budget, Keep going started a
  second round at the default of 5, an unprompted revision to also
  support professional chefs replaced the earlier home-cooks-only
  wording without losing unrelated requirements, and an interruption
  after 2 of 5 round-two questions resumed from structured state
  recorded in the specification itself, repeating no answered
  question. The same specification file was updated, re-validated, and
  accepted with Good enough.
- P6 is covered by the P1 inspection above: vague, unspecified areas
  appeared only as open questions, with no implementation code and no
  speculative modules.

### P6. No invented requirements

- Answer questions vaguely, leaving representations, platforms, and
  integrations unspecified.
- Expect: the generated specification contains only what was said or
  plainly implied, lists the unspecified areas under open questions,
  contains no implementation code, and stays minimal (no speculative
  modules or files).
