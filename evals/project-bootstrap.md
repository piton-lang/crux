# project-bootstrap: conversational evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, in a scratch Piton project. A scenario passes only if the
observable conversation and the generated files behave as stated.
Static checks (`piton check`, `piton build`) do not substitute for
these runs.

## S1. Cold start, default budget

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

## S2. Pre-described project, custom budget

- Describe the project fully in the invocation, then ask for 3
  questions.
- Expect: the agent does not re-ask the project's identity, spends all
  3 questions on gaps in the given description, and stops at 3 even
  though uncertainty remains, recording it as open questions.

## S3. Clarifications, skips, and unknowns

- Mid-round, ask "Can you give me an example?" and later "I don't
  know", then skip a question.
- Expect: the example is given without advancing the counter, the
  unknown is carried as an unresolved/open question (never turned into
  a stated requirement), the skip counts as answered, and the round
  still ends on budget.

## S4. Keep going and revision

- Finish a round, choose Keep going, accept the default of 5 more.
- Change an earlier decision ("actually support artistic modeling
  too").
- Expect: no previously answered question is repeated, the same
  specification file is updated in place, statements contradicting the
  new decision are removed or revised, unrelated requirements survive,
  and the round again ends with Good enough / Keep going.

## S5. Early stop and resume

- Stop the interview after 2 of 5 answers and ask to keep the work.
  End the session. Start a new session in the same project and invoke
  the skill again.
- Expect: the best specification possible from the 2 answers is
  offered or generated, and on resume the agent inspects the project
  and its recorded state, resumes the round without repeating the 2
  answered questions, and distinguishes this from a completed round
  awaiting the Good enough / Keep going decision.

## Live verification results

Run in fresh scratch projects with the skill tethered and built, each
turn and generated file inspected, and each generated specification
re-validated independently afterwards.

- S1 (CAD kernel, default budget, Good enough): passed. Fluency
  command exited 0; the question-count ask preceded Question 1 of 5,
  the given project idea was never re-asked, exactly one question was
  asked per turn across 5 questions, and no sixth question followed.
  The generated minimal Piton project passed `piton check` and
  `piton build`, contained only what the answers established, and
  recorded the remaining unknowns as open questions. The session
  closed with the summary, unknowns, file location, and the
  Good enough / Keep going choice; Good enough was chosen.
- S2 to S5 (recipe manager, combined run): passed. A custom budget of
  3 was respected, a "don't know" and an explicit skip stayed as open
  questions without consuming extra budget, Keep going started a
  second round at the default of 5, an unprompted revision to also
  support professional chefs replaced the earlier home-cooks-only
  wording without losing unrelated requirements, and an interruption
  after 2 of 5 round-two questions resumed from structured state
  recorded in the specification itself, repeating no answered
  question. The same specification file was updated, re-validated, and
  accepted with Good enough.
- S6 is covered by the S1 inspection above: vague, unspecified areas
  appeared only as open questions, with no implementation code and no
  speculative modules.

## S6. No invented requirements

- Answer questions vaguely, leaving representations, platforms, and
  integrations unspecified.
- Expect: the generated specification contains only what was said or
  plainly implied, lists the unspecified areas under open questions,
  contains no implementation code, and stays minimal (no speculative
  modules or files).
