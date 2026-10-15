# Experiments

Computational checks of constructions the paper makes concrete enough to compute. Each experiment is a module under `src/pnp_check/` with a test under `tests/`, and a row in the table below naming the ledger row it bears on and what it showed.

Candidates, in the order the proof uses them:

1. **Claim 5.2 at N = 8** (done: `sfe8`).
2. **Satisfiability along the weight order** (done: `weight_order`).
2a. **Corollary 5.4 counterexample** (done: `corollary_5_4`).
3. **Claim 5.2 for N = 12, 16** (open, ISSUE-008): needs the family of bases the claim refers to; the paper's Remark 7 points to [19].
4. **The extrapolation step itself** cannot be implemented: the system U (page 15) has unspecified kappa, upsilon, w and no computable form (ISSUE-002).

| Experiment | Ledger row | Result |
|---|---|---|
| `sfe8` (`src/pnp_check/sfe8.py`, `tests/test_sfe8.py`) | Claim 5.2 | Holds for N = 8 with the pair (paper's K basis, Zienkiewicz basis): f_K - f_Z = (B/4)(sum of corner values - sum of side values), B = (1-x^2)(1-y^2). Both bases nodal, sum to 1; loads 1/9 and 8/9 (paper) versus -1/3 and 4/3 (standard). |
| `corollary_5_4` (`src/pnp_check/corollary_5_4.py`, `tests/test_corollary_5_4.py`) | Corollary 5.4 | The r-power identity A_r w^r = B_r with w = B_1/A_1 fails exactly for lambda = (64, 49, 36, 25, 16, 9, 4, 1), r = 1/2: A_{1/2}^2 w - B_{1/2}^2 = 30/29. Counterexample from `paper/topchyi_review.pdf`, Section 3. |
| `weight_order` (`src/pnp_check/weight_order.py`, `tests/test_weight_order.py`) | S5-IDEO, S5-CT | Along the numeric order of formula words, answers interleave throughout. 3 vars / 3 clauses: 17,576 instances, 862 flips, tail readable only from M = 96.9 %. 3 vars / 4 clauses: 456,976 instances, 48,948 flips, M = 99.9 %. 4 vars / 3 clauses: 262,144 instances, 2,554 flips, M = 98.6 %. |

"Flips" counts positions where the answer changes between neighbours in the order. "Tail readable from M" is the smallest M such that the answers after the first M instances change at most once, the weakest form of the paper's "determine a position number of C in (N - M) instances". Reproduce with `uv run python -c "from pnp_check.weight_order import summary; print(summary(3, 4))"`.

Run everything with `uv run pytest`. Outputs that are not source go to `experiments/out/`, which git ignores.
