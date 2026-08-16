# Decision System Reference

Use this reference when an idea is difficult to classify or when preparing a detailed journal.

## Contents

1. Dynamic boundary
2. Idea Gate
3. State transitions
4. Phase policy
5. Decision quality
6. AI correction
7. Skill extraction

## 1. Dynamic boundary

A boundary is a membrane, not a wall. It has two simultaneous jobs:

- protect completion from unrelated expansion;
- allow new evidence to change a mistaken direction.

Treat the current scope as a versioned hypothesis:

```text
Scope v1 = best decision given information at start
New signal = idea, evidence, constraint, failure, correction
Gate decision = keep / test / revise / defer / reject
Scope v2 = explicit change with reason and consequence
```

Changing direction is valid only when the reason is recorded. Quietly drifting into a larger task is not a direction change; it is scope creep.

## 2. Idea Gate

### DIRECTION-CHANGING

Signals:

- the user's true need differs from the stated deliverable;
- the current path solves the wrong problem;
- evidence invalidates a core assumption;
- continuing would create an outcome that is unusable even if technically complete;
- a safety, ethical, or fundamental feasibility issue emerges.

Action:

1. Suspend the affected work only.
2. State old and new assumptions.
3. Compare continuing, changing, and testing.
4. Decide explicitly.
5. Revise the definition of done and boundary version.

### ARCHITECTURE-IMPACTING

Signals:

- choice affects platform compatibility, interfaces, data model, or future replacement;
- work is expensive to reverse;
- delay likely creates substantial rework;
- uncertainty can be reduced through a small prototype, sample, or check.

Action:

1. Define the decision the test must resolve.
2. Set the smallest test and a stop condition.
3. Test only that uncertainty.
4. Record the result and return to the main line.

Do not let a validation prototype become a second project.

### ENHANCEMENT

Signals:

- makes the result prettier, broader, faster, or more automated;
- introduces a new integration or future feature;
- does not invalidate the current outcome;
- remains cheap and reversible later.

Action: preserve context, classify as `PARK` or `NEXT`, and continue.

## 3. State transitions

```text
CAPTURED
  ├─ necessary for current output ─> NOW ─> DONE
  ├─ prevents valid progress ─────> BLOCK ─> NOW or PARK
  ├─ needs bounded evidence ──────> TEST ─> NOW / PARK / REJECT
  ├─ useful after completion ─────> NEXT
  ├─ valuable but unscheduled ────> PARK
  └─ intentionally declined ──────> REJECT
```

Transition rules:

- Every `BLOCK` must name what it blocks.
- Every `TEST` must have a question, budget, and stopping point.
- Every `PARK` must retain `Why now` and retrieval cue.
- Every `REJECT` must retain a reason.
- `NEXT` is not an obligation. Reassess it after delivery.
- Only one main line may be `NOW`; supporting subtasks may exist beneath it.

## 4. Phase policy

| Phase | Purpose | Idea policy | Exit |
|---|---|---|---|
| EXPLORE | Discover the right problem and route | Invite alternatives; compare assumptions | Goal and critical choices are sufficiently clear |
| CONVERGE | Build the selected outcome | Gate new ideas; test only high-impact uncertainty | Definition of done is met |
| DELIVER | Verify and hand off | Accept only blockers, correctness, and safety fixes | Artifact, journal, and handoff are complete |

Reopen a converged decision only when:

- new evidence invalidates it;
- an assumption proves false;
- the user changes the desired outcome;
- the cost of not reopening exceeds the disruption.

## 5. Decision quality

A useful decision entry answers:

- What did we believe before?
- What new signal appeared?
- What real alternatives existed?
- Why did the chosen path fit this context?
- What did we knowingly give up?
- What would cause us to revisit it?

Avoid hindsight rewriting. Uncertainty and emotional context are valid data when they affected the decision, but distinguish them from evidence.

## 6. AI correction

Classify corrections:

- `CONTENT`: fact, omission, or interpretation.
- `PROCESS`: AI stopped, asked unnecessarily, or acted outside scope.
- `BOUNDARY`: AI expanded or over-constrained scope.
- `VOICE`: wording, tone, or structure.
- `EPISTEMIC`: AI sounded more certain than evidence allowed.

Promote a correction to a reusable rule when it can be stated as an observable trigger and action:

```text
When [condition], do [behavior], because [reason].
Do not [anti-pattern].
```

## 7. Skill extraction

Score a candidate from 0–2 on each:

- recurrence: likely to happen again;
- leverage: meaningfully improves future work;
- clarity: can be followed without hidden context;
- evidence: supported by actual work;
- scope: has a clear application boundary.

Interpretation:

- 8–10: promote to a rule/workflow;
- 5–7: retain as a candidate;
- 0–4: keep only in the journal.

Do not turn every preference or single accident into permanent procedure.
