# spec-deep-dive: conversational evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project that already has a
high-level specification. A scenario passes only if the observable
conversation and the resulting files behave as stated. Static checks
(`piton check`, `piton build`) do not substitute for these runs.

## T1. Explicit target, default budget

- Existing spec: a CAD kernel stating robust topology and persistent
  entity identification at a high level.
- Invoke with "Deep dive into topology naming."
- Expect: no candidate list is needed (target given), the agent reads
  the existing topology requirements and open questions before asking
  anything, asks the question-count question (default 5, not counted),
  then asks exactly one question per turn with target-labelled
  progress, never re-asking anything the spec already establishes.
- Expect questions in the spirit of stability of references across
  operations, split-face ambiguity, successor candidates,
  determinism, and atomic failure — adapted to the answers, not a
  copied script.
- After 5: no more discovery questions; the topology specification is
  refined in place with confirmed requirements, anything suggested
  but not accepted stays out of the requirements, unknowns remain
  open questions, `piton check` and `piton build` pass, and the turn
  ends with a decision-oriented summary, the updated files, and
  Good enough / Keep going.

## T2. Ambiguous target and target with no specification yet

- Invoke with no target in a project whose spec covers booleans,
  fillets, and topology only as prose inside a larger anchor.
- Expect: a short candidate selection by capability name (not
  filenames), with an escape to something else. Choosing a capability
  that has no dedicated specification leads the agent to locate its
  parent requirements, interview against them, and create an
  appropriately placed dedicated specification only when the round
  completes — without restructuring anything else.

## T3. Custom budget, don't-know, defer, recommendation

- Configure 3 questions. Answer one, say "I don't know" to one, and
  ask "What would you recommend?" on the third.
- Expect: exactly 3 consumed questions; the don't-know is preserved
  as an open question; the recommendation is presented with options
  and tradeoffs and is recorded as a confirmed requirement only if
  explicitly accepted, otherwise as a suggestion or open question.
- Expect a mid-interview unrelated insight to be captured, attributed
  to where it belongs, and not expanded into a second interview.

## T4. Keep going, correction, and scope discipline

- Finish a round, choose Keep going with the default of 5.
- Mid-round, change an earlier decision ("That should work
  differently") and raise an unrelated capability.
- Expect: no answered question is repeated, round 2 goes measurably
  more specific than round 1, the changed decision revises the
  affected requirements with downstream consistency checked and the
  change called out in the summary, unrelated specifications are
  byte-identical afterwards (check with a diff), and the unrelated
  capability is recorded where it belongs without derailing the
  target.

## T5. Interruption and resume

- Interrupt a round halfway, end the session, start a new session in
  the same project, and invoke the skill again.
- Expect: the agent inspects the project and its persisted state
  (target, budget, answered count, decisions, open questions, focus,
  whether refinement was applied, whether it awaits
  Good enough / Keep going) before asking anything, repeats no
  answered question, and finishes the round on the remaining budget.

## Live verification results

Run in fresh scratch projects with the skill tethered and built, each
turn and generated file inspected, and each refined specification
re-validated independently afterwards.

- T1 (topology naming, default 5, Good enough): passed. The fluency
  command exited 0, the explicit target needed no candidate list, the
  existing requirements were analyzed before questioning, exactly one
  question was asked per turn (`Question 1 of 5` through
  `Question 5 of 5`), and a new dedicated `Topology` specification was
  created with five testable requirements (reference stability, split
  ambiguity, successor-candidate exposure, determinism under identical
  histories, atomic failure), matching acceptance criteria, one
  design suggestion kept explicitly out of the confirmed requirements,
  and merges, deleted topology, and history changes preserved as open
  questions. The unrelated `Booleans` anchor was unchanged, and
  `piton check` and `piton build` passed.
- T2, T3, T5 (combined run): passed. With no target given, candidates
  were presented by capability name; fillets existed only as prose in
  the parent anchor, and a dedicated `FilletsAndChamfers`
  specification was created only when the round completed, leaving the
  parent anchor unchanged. A custom budget of 3 was respected, a
  don't-know stayed an open question, and a recommendation the user
  deferred was recorded only as suggested approaches with tradeoffs,
  never as a requirement. An interruption after two answers resumed
  from persisted state without repeating a question, Keep going ran a
  further round of 2, and the same specification gained atomic-failure
  behaviour and an explicit out-of-scope item before being accepted
  with Good enough. Both rounds validated cleanly.
- T4's unrelated-specification preservation and revision behaviour,
  and T6's unresolved-conflict handling, are specified in the skill
  and partially exercised above (unrelated anchors byte-preserved in
  both runs); a dedicated live run for T6 is still outstanding.

## T6. Conflict that cannot be resolved safely

- Give an answer that contradicts an existing confirmed requirement
  outside the deep-dive's authorized scope.
- Expect: the contradiction is surfaced, identified with the affected
  requirements, and preserved as unresolved rather than silently
  resolved; within-scope latest decisions still win and are reported.
