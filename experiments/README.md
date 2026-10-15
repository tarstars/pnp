# Experiments

Computational checks of constructions the paper makes concrete enough to compute. Each experiment is a module under `src/pnp_check/` with a test under `tests/`, and a row in the table below naming the ledger row it bears on and what it showed.

Candidates, in the order the proof uses them:

1. **Node configuration of the computational template** (ledger S5-CT, page 10, line 636). Reproduce the N boundary nodes of the square and the residue-mod-4 numbering; confirm the construction is well defined for every N.
2. **Field functions and the stabilization function** (Claim 5.2, S5-IDEO). Implement lambda_i(t) as the paper defines them and test the limit claims numerically.
3. **The extrapolation step against real SAT instances** (S5-IDEO, S5-COMPLX). Take small random 3-SAT instances, apply the paper's rule for inferring unchecked instances from checked ones, and compare with a brute-force solver.

| Experiment | Ledger row | Result |
|---|---|---|
| (none yet) | | |

Run everything with `uv run pytest`. Outputs that are not source go to `experiments/out/`, which git ignores.
