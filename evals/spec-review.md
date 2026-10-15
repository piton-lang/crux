# spec-review: evaluation scenarios

Run each scenario in a fresh agent session with the built skill
installed, against a scratch Piton project prepared as stated. A
scenario passes only if the observable review, its evidence, and the
(absence of) file changes behave as stated. Static checks do not
substitute for these runs. Record the file tree or hashes before and
after: the review must modify no specification.

## R1. Project with genuine problems (whole-project review)

Seed a CAD kernel project where:

- Two specifications contradict each other about failure semantics
  (one requires operations to leave the model unchanged on failure,
  another allows returning partial results).
- A requirement says the system "must be extremely fast" with no
  observable acceptance condition.
- Topology requires stable references, but nothing defines split or
  merge behaviour, and modelling operations rely on those references.
- Rendering is an explicitly stated non-goal, and tolerance policy is
  an explicitly deferred open question.

Expect: the contradiction is reported as a confirmed defect with
both affected specifications cited and a resolving question; the
topology contract appears as a grouped, high-priority likely gap
rather than several repetitive findings; "extremely fast" is raised
as unverifiable with a question about which operations need
measurable criteria; rendering is never criticised; the deferred
tolerance decision is noted as a known open question, not as an
overlooked defect. Output has Overall Assessment, Prioritized
Findings (each with priority, type, evidence, impact, confidence),
a Top 5 question list the user is not asked to answer inline, and one
Recommended Next Action (typically spec-deep-dive on the affected
specification, recommended but not invoked). No file changes.

## R2. Healthy, well-specified project

Seed a small project whose requirements are precise, testable,
internally consistent, and explicit about non-goals.

Expect: a clean assessment that says what is well-defined, with no
manufactured findings invented to fill a quota, a very short or empty
findings list, only genuinely remaining open questions (if any) in
the questions section, and a sensible next action. No file changes.

## R3. Targeted review scope

Seed a project with problems in two unrelated subsystems. Invoke:
"Review only the topology specification."

Expect: findings are centred on topology and on requirements it
depends on or that depend on it; problems in the unrelated subsystem
are not reported as findings (at most noted as out of scope); local
consistency is not mistaken for global consistency where topology
interacts with an established guarantee elsewhere. No file changes.

## R4. Apparent contradiction that is compatible, and duplication

Seed overlapping specifications where one states a general rule and
another states a permitted special case, plus the same requirement
stated verbatim in two places that inherit it unnecessarily.

Expect: the apparent contradiction is not reported as a confirmed
defect (at most a clarification question with low severity and
explained reasoning); the duplication is reported as a structural
finding with a question or mechanical recommendation; no invented
defect appears.

## Live verification results

Run in fresh scratch projects with the skill tethered and built, with
specification hashes recorded before and after.

- R1: passed. The whole-project review identified the seeded failure
  semantics conflict as a Critical confirmed defect citing both
  specifications, and additionally used `piton slice` to show the
  child anchor's requirements list overrides rather than extends the
  parent's, silently dropping atomicity from the effective
  specification. The topology identity gap was grouped into one
  high-priority finding, "extremely fast" and "exact geometry" were
  raised as unverifiable with targeted questions, rendering (an
  explicit non-goal) was never criticised, and the deferred tolerance
  decision was treated as a known deferral whose blast radius was
  analysed rather than as an overlooked defect. Output had all four
  sections, a ranked top 5, and a single recommended next action.
  Specification hashes were unchanged afterwards.
- R2 and R3 (combined, targeted review): passed with a noted
  interpretation. Asked to review only a precise, self-contained
  converter specification, the review gave it a clean assessment, no
  manufactured quota of findings, and fewer than five questions. It
  did flag one cross-specification issue at the converter's boundary:
  its stated offline purpose versus a co-located storage requirement
  that converted values be uploaded to a cloud service before
  reopening. That is a dependent of the target rather than an
  unrelated subsystem, and the review labelled the dependency as
  inferred and confidence-rated rather than confirmed. Specification
  hashes were unchanged afterwards.
- R4 and R5 are specified above and remain as further live scenarios;
  inheritance semantics were exercised incidentally in R1 through the
  override finding.

## R5. Maturity sensitivity and repeat run

Run on a freshly bootstrapped initial specification, then refine one
finding away with spec-deep-dive in a separate session, then review
again.

Expect: the first review prioritises scope, core capabilities, major
constraints, and critical assumptions rather than flooding low-level
detail; the second review, run fresh against the current project,
no longer reports the resolved issue, still reports the unresolved
ones it can re-verify, and does not rely on the earlier report as
truth. No file changes from either review.
