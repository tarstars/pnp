# Issue log

One entry per problem found. Severity: `fatal` (breaks Theorem 5.1), `major` (breaks a supporting statement or leaves a step unjustified), `minor` (fixable, does not affect the conclusion), `unclear` (we cannot tell what is being claimed). Every entry names the ledger row it affects. Line numbers refer to `paper/paper.txt`; the reasoning behind each entry is in `review/sections/s5_p_eq_np.md`.

## Index

| ID | Severity | Ledger row | Page / line | Summary | Status |
|---|---|---|---|---|---|
| ISSUE-001 | fatal | Theorem 5.1, S5-DTM | 10 / 633; 17 / 1307 | No algorithm is specified: no input, no output, no steps | confirmed |
| ISSUE-002 | fatal | S5-IDEO | 15 / 1176 | The system U that is to determine the unknown answers does not contain the instances | confirmed |
| ISSUE-003 | fatal | S5-COMPLX | 16 / 1286 | Complexity count assumes the conclusion and derives no polynomial | confirmed |
| ISSUE-004 | major | Claim 5.3, Corollary 5.4 | 15 / 1152, 1164 | Claim 5.3 vacuous with unspecified constants; Corollary 5.4 false as a general identity (exact counterexample) | confirmed |
| ISSUE-005 | major | S5-CT (2nd stage) | 11 / 711 | Instance enters only as a number; basis with prescribed loads asserted; weight order carries no information | confirmed |
| ISSUE-006 | major | S5-IDEO | 15-16 / 1194, 1275 | BBGKY hierarchy attached by one sentence, nothing derived from it | confirmed |
| ISSUE-007 | minor | Claim 5.3 | 14 / 1119 | "s* = P(n), a polynomial" asserted without derivation | confirmed |
| ISSUE-008 | unclear | Claim 5.2 | 11-13 / 789-1049 | General-N proof not followable; holds for N = 8 | open |
| ISSUE-009 | minor | Theorem 5.1 | 17 / 1330 | Author denies the standard consequence of P = NP (TSP) | confirmed |

## ISSUE-001: No algorithm is specified

- **Severity:** fatal
- **Where:** Theorem 5.1 (page 10, line 633); Section 5.1 (page 17, lines 1307-1322)
- **What the paper says:** "there exists an algorithm that allows to identify all instances of the Boolean satisfiability problem in polynomial time." The implementation model: "we can numerate them on tape in polynomial time. We will operate with polynomially bounded collection of computable values g_1, ..., g_{s*+upsilon+1} ... such that the relevant collection of computable 'weights' ... is given."
- **What is wrong or missing:** "Identify" is undefined. No input is named, no output is named, and no step is described that takes a formula and produces its answer. Section 5.1 describes a collection of real numbers kept on tape, and its second paragraph uses Theorem 5.1 to describe the implementation of Theorem 5.1.
- **Why it matters for Theorem 5.1:** P = NP requires a decision procedure for SAT with a polynomial time bound. Without input, output and steps there is nothing whose running time could be bounded.
- **Evidence:** lines 633, 1307-1322; the only operational phrasing is footnote 17 (page 15), which speaks of "a position number of C" among instances sorted by weight.
- **Status:** confirmed

## ISSUE-002: The system U does not contain the instances

- **Severity:** fatal
- **Where:** S5-IDEO (page 15, lines 1174-1217)
- **What the paper says:** "we have the following system U for determination of lambda_i(t), here i > s*", followed by equations (1)-(6).
- **What is wrong or missing:** The unknown answers lambda_i (i > M) are to be found from U. Equations (1)-(3) relate sums of the lambda_i and of their r-th powers through the unspecified kappa, upsilon and w; (4) is the BBGKY hierarchy for hard spheres; (5) fixes a block to the undecided value 0.5/0.5; (6) sets the tail to "|g_i - g_{i+1}| approx 0". Neither the instances S_i, nor their weights chi_i, nor the basis functions L_i appear in U. A system that never reads a formula cannot output that formula's satisfiability. Equation (6) also concedes that for the tail the two answers "are indistinguishable" (line 1281).
- **Why it matters for Theorem 5.1:** this is the step that is supposed to produce the N - M answers without checking. It produces nothing that depends on the instances.
- **Evidence:** page 15 image, equations (1)-(6); lines 1176-1217 and 1281.
- **Status:** confirmed

## ISSUE-003: The complexity count assumes the conclusion and derives no polynomial

- **Severity:** fatal
- **Where:** S5-COMPLX (page 16, lines 1286-1303)
- **What the paper says:** "1. Checking the first M instances with total computational complexity of O(n^k) ... 2a ... O(n^{k'}) ... 2b ... O(n^{k''}) ... 2c ... theta, P are polynomials ... O(n^{k'''}). Thus we have leveled the surplus of (N - M) instances ..., so P = NP."
- **What is wrong or missing:** Item 1 charges O(n^k) for checking M SAT instances on a DTM, which is the quantity the theorem is about; no method is given. Items 2a-2c attach exponents to steps that are never described as computations, and theta, P are declared polynomial. In 2c, blocks of l >> upsilon instances are "determined due to permutation" with upsilon representatives, with no reason why a non-representative's answer equals a representative's. No polynomial is derived at any point.
- **Why it matters for Theorem 5.1:** the time bound is the theorem.
- **Evidence:** lines 1286-1303; page 16 image.
- **Status:** confirmed

## ISSUE-004: Claim 5.3 is vacuous and Corollary 5.4 is false as a general identity

- **Severity:** major
- **Where:** Claim 5.3 (page 15, line 1152), Corollary 5.4 (line 1164), the "stabilization function" (line 1149), equation (2) of U (line 1182)
- **What the paper says:** "We can assume without loss of generality that (sum_{i=1}^4 lambda_i / 4) * w(N,t) = sum_{i=5}^N lambda_i / (N - 4), where w(N,t) is a stabilization function." Claim 5.3: the barycentre value "equals kappa * w(N,t) * E_n(lambda(t), 1), here kappa = const". Proof: "It is easily shown that ... by induction, we obtain the statement." Corollary 5.4: with the same w, (sum_{i=1}^4 lambda_i^r / 4) * w^r = sum_{i=5}^N lambda_i^r / (N - 4) for 0 < r < 1; "The proof is omitted."
- **What is wrong or missing:** (a) w is defined by the very identity it is then used in and kappa is a free constant, so Claim 5.3 reads "a number equals kappa times w times a number", which any positive left-hand side satisfies; no proof is given. (b) Corollary 5.4 is false in general. Write A_r = (1/4) sum_{i=1}^4 lambda_i^r and B_r = (1/(N-4)) sum_{i=5}^N lambda_i^r, so w = B_1/A_1 and the corollary asserts A_r w^r = B_r. Counterexample (from the note `paper/topchyi_review.pdf`, Section 3; verified exactly in experiment `corollary_5_4`): N = 8, r = 1/2, lambda = (64, 49, 36, 25, 16, 9, 4, 1). Then A_1 = 87/2, B_1 = 15/2, w = 5/29, A_{1/2} = 13/2, B_{1/2} = 5/2 and A_{1/2}^2 w - B_{1/2}^2 = 169/4 * 5/29 - 25/4 = 30/29, not 0. The sequence is positive and strictly decreasing, and appending 2^{-k} gives a tail to 0 with sum lambda_i^{1/(1-r)} finite, so every condition the paper states at lines 1134-1136 is met. Since w = B_1/A_1, the corollary holds exactly when A_r / A_1^r = B_r / B_1^r, an extra condition the paper never imposes. (c) Two hypotheses of [26] are not met: (i) concerns infinite sequences and is applied to the finite sequence lambda_1..lambda_N; and at line 1134 the functions L_i(x,y) are identified with the numbers m_i^r of [26], which requires m_i >= 0 while serendipity basis functions take negative values inside the square.
- **Why it matters for Theorem 5.1:** Claim 5.3 and Corollary 5.4 are the stated source of equations (1)-(3) of U; equation (2) is therefore false as written.
- **Evidence:** lines 1134-1137, 1147-1172, 1182; page 15 image; `src/pnp_check/corollary_5_4.py`, `tests/test_corollary_5_4.py`; `paper/topchyi_review.pdf` (3-page note prepared with ChatGPT, 15 October 2026).
- **Status:** confirmed

## ISSUE-005: The instance enters the proof only as a number, and the weight order carries no information

- **Severity:** major
- **Where:** S5-CT, 2nd and 3rd stages (page 11, lines 711-722); footnote 17 (page 15); Section 5.2 comment 2 (page 17, lines 1333-1340)
- **What the paper says:** "to each S_i corresponds a unique 'weight' chi_i = S_i / sum S_i; however chi_i = (1/G) integral_D L_i dx dy ... Hence to each chi_i corresponds a unique collection of the basis functions (UCBF)." Nodes are then ordered chi_1 < chi_2 < .... Footnote 17: "Our goal is to determine a position number of C in (N - M) instances or to identify that all (N - M) instances are C-bar."
- **What is wrong or missing:** (a) The only property of a formula used anywhere is its numeric value in an unstated encoding; its clauses are never read. (b) The existence and uniqueness of a nodal basis with N prescribed loads is asserted; the one-parameter mixing offered in Section 5.2 comment 2 cannot satisfy N constraints. (c) Experiment `weight_order`: along the numeric order of words, satisfiable and unsatisfiable formulas interleave throughout (3 variables, 4 clauses of width 1-3: 48,948 answer changes among 456,976 instances; the tail after the first M instances has at most one change only from M = 99.9 % of all instances). There is no "position number of C".
- **Why it matters for Theorem 5.1:** the "ideology" rests on the first M instances in this order determining the rest.
- **Evidence:** `src/pnp_check/weight_order.py`, `tests/test_weight_order.py`; measurements recorded in `experiments/README.md`.
- **Status:** confirmed

## ISSUE-006: The BBGKY hierarchy is attached by one sentence and nothing is derived from it

- **Severity:** major
- **Where:** equation (4) of U (page 15, line 1194) and its comments (page 16, lines 1218-1284)
- **What the paper says:** equations (5.1)-(5.4), the Liouville operator, the collision operator and the chaos condition from [27], then: "f(x,y,t) is a phase space: each z-axis at the node is a particle of unit mass and diameter rho > 0 such that |q_i - q_j| >= rho."
- **What is wrong or missing:** No map from nodal values or instances to particle positions and momenta is defined, no initial datum F(0) is specified, no solution is computed, and the only sentence that follows from the block is "the number of r is polynomially bounded" (line 1280), which is not derived.
- **Why it matters for Theorem 5.1:** (4) is one of the six equations said to determine the unknown answers.
- **Evidence:** lines 1218-1284; page 16 image.
- **Status:** confirmed

## ISSUE-007: "s* = P(n), a polynomial" is asserted

- **Severity:** minor
- **Where:** Note after (ii) (page 14, line 1119)
- **What the paper says:** "Note. 1. s* = P(n), here P(n) is a polynomial."
- **What is wrong or missing:** In [26] s* is the index realising a supremum that depends on the sequence alpha and on n; no bound is derived, and the note is not part of the cited result. The index s* is a position in a sequence, not a running time, so even a polynomial bound on it would say nothing about computation.
- **Why it matters for Theorem 5.1:** s* = M is the number of instances that are "checked"; its polynomial size is taken from this note.
- **Evidence:** line 1119; the statement of (i) and (ii) at lines 1075-1118.
- **Status:** confirmed

## ISSUE-008: Claim 5.2 for general N cannot be followed

- **Severity:** unclear
- **Where:** Claim 5.2 (page 11, line 789) and its proof (pages 12-13, lines 826-1049)
- **What the paper says:** a system of four conditions on the lambda_i indexed by N mod 4; proof via functions Q_i, gamma_j and node counts q_1..q_4 given by cubic expressions in b = N mod 4.
- **What is wrong or missing:** The functions Q_i are never defined, the counts q_j are not derived, the pair or family of bases with respect to which invariance is claimed for N > 8 is not named, and the key step is the sentence "the expected value of difference of two field functions with different collections of the basis functions is equal to zero". For N = 8 the claim is correct for the pair (paper's K, Zienkiewicz): experiment `sfe8` shows f_K - f_Z = (B/4)(sum of corners - sum of sides).
- **Why it matters for Theorem 5.1:** it does not: at line 1147 the paper replaces the condition by an identity defining w(N,t).
- **Evidence:** `src/pnp_check/sfe8.py`, `tests/test_sfe8.py`; page 12-13 images.
- **Status:** open

## ISSUE-009: The author denies the standard consequence of P = NP

- **Severity:** minor
- **Where:** Section 5.2 comment 1 (page 17, line 1330)
- **What the paper says:** "theorem 5.1 is not a universal algorithm (specifically, for the TSP)."
- **What is wrong or missing:** A polynomial-time decision procedure for SAT yields one for every problem in NP, the decision version of the travelling salesman problem included, by the Cook-Levin theorem and Karp's reductions. The comment indicates that the claimed result is not P = NP in the standard sense.
- **Why it matters for Theorem 5.1:** it bears on what the theorem is meant to assert, not on the proof.
- **Evidence:** line 1330.
- **Status:** confirmed
