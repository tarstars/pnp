# Verdict

Status: **open**. Written only when every row of `review/01_claims_ledger.md` has left `unchecked`.

## Criteria

The proof of Theorem 5.1 is accepted only if all of the following hold.

1. Theorem 5.1 is stated as a decision procedure for SAT with explicit input, output and time bound.
2. Every step of the proof is justified in the paper or by an obtainable reference whose cited result we verified.
3. The extrapolation from M checked instances to N - M unchecked ones is proved, not asserted.
4. The DTM implementation of Section 5.1 is a concrete algorithm whose running time is bounded by a polynomial in the input length, with that polynomial derived.
5. No issue of severity `fatal` remains open.

## Interim assessment (Section 5 reviewed, 2026-10-15)

Sections 2-4 are still `unchecked`, so the verdict stays open by the rule above. The proof of Theorem 5.1 lives entirely in Section 5, and that section is complete, so the following can already be stated.

**The proof does not establish Theorem 5.1.** Three independent defects each suffice:

1. No algorithm is specified: no input, no output, no step (ISSUE-001). Criteria 1 and 4 fail.
2. The system U that is to produce the answers of the unchecked instances contains no instance, weight or basis function; its last equation sets the tail of answers to "approximately zero" and calls the two answers "indistinguishable" (ISSUE-002). Criterion 3 fails.
3. The complexity count charges O(n^k) for "checking" M SAT instances, which is the question itself, and derives no polynomial for any step (ISSUE-003). Criterion 4 fails.

Sections 2-4 are not load-bearing: the proof uses nothing from them beyond the phrase "labeled geo-plafal" for a square with N boundary nodes. Reviewing them can change the status of Definitions 2.1-4.16 but cannot repair Theorem 5.1.

In addition, Corollary 5.4, whose proof is omitted, is false as a general identity: an exact counterexample (N = 8, r = 1/2, from the note `paper/topchyi_review.pdf`, verified in experiment `corollary_5_4`) shows that the paper's definition of the stabilization function does not imply the r-power identity used as equation (2) of U (ISSUE-004).

What is correct in Section 5: Lemma 5.5 (true, with a shorter proof than the paper's), Claim 5.2 for N = 8 (verified symbolically for the two bases the paper names), and the restatement of [26].

## Issues that determine the verdict

ISSUE-001, ISSUE-002, ISSUE-003 (fatal). ISSUE-004, ISSUE-005, ISSUE-006 (major) explain why the supporting apparatus cannot be repaired into a proof without new ideas.
