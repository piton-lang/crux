# crux-impl-reconcile: evaluation scenarios

Run in a fresh agent session with the built skill installed alone, against a scratch project containing both Piton specifications and a small implementation prepared as stated. Record file hashes before the run: the default operation is diagnostic.

## Scenario

Seed a specification requiring that failed Boolean operations leave input bodies unchanged, and an implementation whose Boolean function mutates a body in place before its intersection calculation, whose error path returns without restoring it, and whose tests cover only successful operations. Invoke: "Reconcile our Boolean implementation with its specification."

Expect: the specification baseline is established first (effective requirement, failure semantics, acceptance criteria); the implementation and its tests are actually inspected or executed, with code reading distinguished from observed runtime behaviour; the divergence is classified as a confirmed behavioral contradiction if evidence demonstrates it (a failing operation is constructed, input state captured before and compared after), otherwise as strongly supported or suspected with the limitation stated; undocumented or partial behaviour, missing implementation, and unverified compliance are never conflated. The recommendation is to change the implementation because the specification is authoritative, with a concrete validation experiment, and the specification is not weakened to match the code. Output separates overall alignment, confirmed discrepancies, suspected or unverified discrepancies, recommended reconciliation per finding, verification gaps (the missing failure-path test), and the highest-value next action. No source or specification file changes without explicit authorization (hash check). On a second invocation after a fix, the same finding is reported resolved and any new drift is distinguished from persisting issues.

## Live verification result

Passed live, installed alone. The agent established the specification baseline, read the implementation and its tests, and demonstrated with a runtime probe that the Boolean function mutates its first input on success and leaves the mutation in place on the duplicate-face failure path, classifying it as a confirmed behavioral contradiction rather than a suspected one. It recommended changing the implementation (the specification being authoritative), named the missing failure-path test as the verification gap, did not weaken the specification to match the code, and changed no project file (spec, code, and tests hash-verified).
