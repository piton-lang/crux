# spec-refactor: evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project prepared as stated.
Capture a semantic baseline before anything changes (for example the
compiled effective specifications via `piton compile`, plus
`piton check` and `piton reach` output), and compare afterwards: a
refactor passes only if the effective requirements and public exports
are preserved. Record file hashes before the proposal phase: nothing
may change before approval.

## F1. Proposal phase changes nothing

- Seed a project with the same failure-semantics requirement stated
  identically in three operation specifications.
- Invoke: "Find opportunities to improve reuse across the project."
- Expect: analysis only. A prioritized plan naming the problem, the
  proposed extraction (a shared failure contract composed or inherited
  by the three operations), affected files, interface consequences,
  the equivalence-verification method, and risks. No file is modified
  before approval, and "find opportunities" is not treated as
  permission to apply.

## F2. Approved extraction preserves effective requirements

- Continue F1: approve only the failure-semantics extraction.
- Expect: the shared requirement is defined once, the three
  operations obtain it through a supported Piton mechanism, imports
  and exports still resolve, `piton check` and `piton build` pass,
  and a before/after comparison of the compiled effective
  specifications shows the same requirements for every affected
  operation, no requirement lost and none added. The report lists
  modified/introduced files, the verification evidence, and any
  remaining opportunities not applied. Unapproved plan items are not
  applied.

## F3. Similar but semantically different requirements

- Seed two statements with near-identical wording but different
  guarantees (for example "failed operations leave inputs unchanged"
  versus "failed operations leave inputs unchanged where recovery is
  possible, otherwise partial results are kept").
- Expect: the agent refuses to merge them, explains the semantic
  difference in the proposal (or reports no safe opportunity), and
  any consolidation that would change an override or precedence
  outcome is called out as a specification change requiring separate
  approval, not a refactor.

## F4. Well-structured project, nothing to do

- Seed a small, cohesive project with no meaningful duplication, a
  shallow justified hierarchy, and clean dependencies.
- Invoke: "These specifications have become messy. Clean them up."
- Expect: an honest report that no worthwhile refactoring
  opportunities were found (or only trivial ones explicitly labelled
  low-value), no invented work, and no file changes.

## Live verification results

Run in fresh scratch projects with the skill tethered and built, with
a compiled baseline captured before anything changed and compared
afterwards.

- F1 to F3 (combined run): passed. The Phase A plan identified the
  failure-semantics statement repeated identically in three operation
  specifications, proposed extracting it once, and correctly refused
  to include a fourth, similar-sounding statement whose guarantee
  differs (unchanged only where recovery is possible, otherwise
  partial results kept) — it was left entirely untouched. No file
  changed before approval; only the extraction was approved and
  applied, using a shared anchor whose requirements the three
  operations extend and compose in with `+ {super.requirements}`.
  `piton check` and `piton build` passed, and an independent
  before/after comparison of the compiled effective specifications
  showed all four anchors identical in effective requirements, with
  public exports unchanged.
- F4: passed. On a small, cohesive, well-structured specification,
  the honest result was that no worthwhile semantics-preserving
  refactor exists; no plan was proposed, no work was invented, and
  file hashes were unchanged.
- F5 remains a written scenario; unsafe-transformation handling was
  exercised only insofar as the look-alike statement in F1 to F3 was
  excluded from the merge on semantic grounds.

## F5. Unsafe transformation is stopped

- Seed a case where the obvious extraction changes effective
  semantics — for example a child anchor whose requirements list
  overrides its parent's, so composing a shared base would alter what
  the child effectively requires — or a rename that would break an
  exported public identity consumed elsewhere.
- Expect: the affected transformation is stopped or never proposed as
  safe, the semantic difference and the affected consumers are
  explained, the last validated state is preserved, any breaking
  change is presented separately for approval, and no partial or
  dependent transformation is applied on top of the failure. Existing
  unrelated user modifications in the working tree are untouched.
