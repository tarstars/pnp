# Section 5. P = NP

- **Scope:** `paper/paper.txt` lines 622-1498 (pages 10-18).
- **Statements:** Theorem 5.1; Claims 5.2, 5.3; Corollary 5.4; Lemma 5.5; steps S5-CT, S5-IDEO, S5-COMPLX, S5-DTM.
- **Ledger:** `review/01_claims_ledger.md`, section 5.
- **Reviewed:** 2026-10-15, from the text extraction and the page images of pages 10-17 (formulas that the extraction garbles were read from the images).

Notation used below: C = instance answered "Yes" (satisfiable), C-bar = answered "No"; SFE = serendipity finite element; FF = field function; BF = basis function; DTM = deterministic Turing machine.

## Reading notes

### Preamble (lines 623-632, page 10)

"By S we denote an instance of an NP-complete problem. Using the deterministic Turing machine (DTM), C is a type of S with answer 'Yes' after the checking, otherwise is C-bar." And: "theorem 5.1 is a theoretical model of P = NP; the implementation model of theorem 5.1 on the DTM will be described."

### Theorem 5.1 (line 633)

"Based on the theory of plafales, there exists an algorithm that allows to identify all instances of the Boolean satisfiability problem in polynomial time."

- "Identify" is never defined. The reading that would give P = NP is a DTM that, on input a CNF formula of length n, outputs satisfiable or unsatisfiable in time polynomial in n. The paper states neither input nor output for its algorithm. The only operational description is footnote 17 (page 15): with N instances, after "checking the first M instances", "determine a position number of C in (N - M) instances or to identify that all (N - M) instances are C-bar".
- The proof runs: three stages (template, instance-to-basis-function, field function), Claim 5.2, a restatement of [26], "Ideology of P = NP", Claim 5.3 and Corollary 5.4, the system U, a complexity count, then "so P = NP" (line 1303).

### 1st stage: computational template (lines 636-660; Figure 6 at line 701)

"Labeled geo-plafal ... where SFE is a serendipity finite element (square D = {|x| <= 1, |y| <= 1}) on N vertices (nodes). Vertices |v|_i are evenly spaced on the boundary of SFE" with the rule i = 4l+1 on the bottom side, 4l+2 right, 4l+3 top, 4(l+1) left. Each vertex carries (line 657) the pair <S_i, H_i = zeta_i(t) C_i + theta_i(t) C-bar_i> with zeta_i + theta_i = 1, "t is time".

- Node i holds instance S_i and a time-dependent mixture of its two possible answers. Nothing in the paper says what governs zeta_i(t).
- This is the only use the proof makes of Sections 2-4: the phrase "labeled geo-plafal" for a square with N labelled boundary nodes. A grep of lines 622-1306 finds no citation of any definition, claim or corollary of Sections 2-4; "plafal" otherwise occurs in the theorem statement, in a Section 5.2 comment and in the list of key terms.

### 2nd stage: instance to basis function (lines 711-719, page 11)

"Let us consider the word S_i over a given alphabet. Then to each S_i corresponds a unique 'weight' chi_i = S_i / sum_{i=1}^N S_i; however chi_i = (1/G) integral_D L_i(x,y) dx dy >= 0, here G is the area of D, where N is a quantity of instances of the Boolean satisfiability problem. Hence to each chi_i corresponds a unique collection of the basis functions (UCBF) in the CTSA."

- The word S_i is used as a number (its value in an unstated encoding), and its normalised value is declared equal to the load of the basis function L_i at node i. The weights sum to 1 and so do the loads of a nodal basis with sum L_i = 1, so the two normalisations are compatible.
- "Hence to each chi_i corresponds a unique collection of the basis functions" asserts that for any prescribed loads chi_1..chi_N a nodal basis with those loads exists and is unique. No construction or reference is given. The construction offered in Section 5.2 comment 2 (lines 1333-1340), L_i = xi L^1_i + (1 - xi) L^2_i with one scalar xi, cannot meet N prescribed loads. See ISSUE-005.
- Footnote 13 (page 11): the relationship "acts as a 'lock' ... such that S_i <-> UCBF. This enables us to determine S_i based on lambda_i." lambda_i is the nodal value, which by the 3rd stage encodes the answer; the footnote says the answer determines the instance, which is the reverse of what a decision procedure needs, and gives no mechanism either way.
- The only property of an instance the proof ever extracts is its numeric value. The clause structure of a formula is never used anywhere in Section 5.

### 3rd stage: field function (lines 720-745, page 11; Figure 7 at line 784)

Nodes are ordered by weight: "chi_1 < chi_2 < ... < chi_l < ..." (line 722). The "non-standard Dirichlet boundary value problem [4]": f(x,y,t) = sum_i lambda_i(t) L_i(x,y) with g_1 > g_2 > ... > 0, lim g_i = 0, lambda_i(t) = zeta_i(t) (g_i - g_{i+1}) + g_{i+1} in (g_{i+1}, g_i) for t < T, and for t >= T: lambda_i = g_i or g_{i+1}. Line 745: "For C we get lambda_i(t) = g_i, otherwise is lambda_i(t) = g_{i+1}."

- The answer of instance i is encoded as the nodal value lambda_i in {g_i, g_{i+1}}; before time T the value lies in between (undecided). The sequence g is fixed and decreasing, so g_i - g_{i+1} -> 0: for large i the two possible answers become numerically indistinguishable. The paper says so itself: equation (6) of U (line 1217) sets "lambda_{s*+v+1 <= i <= N} = |g_i - g_{i+1}| approx 0" and line 1281 says "g_{j+1}, g_j are indistinguishable".
- Nothing states what drives zeta_i(t) for t < T. The field function is a function of the answers; to write it down one needs them.

### Claim 5.2 (lines 789-805, page 11; proof lines 826-1049, pages 12-13)

Statement: for SFE on N vertices "the condition of invariant of the field function (stability of the FF w.r.t. the BF)" is, for N = 4k, (sum_{i=1}^4 lambda_i)/4 = (sum_{i=5}^N lambda_i)/(N - 4), with analogous split sums for N = 4k+1, 4k+2, 4k+3.

- Meaning, from the proof text (page 13): "Our goal is that the choice of the basis functions is insignificant. So, the expected value of difference of two field functions with different collections of the basis functions is equal to zero." So the claim is: the interpolant sum lambda_i L_i is the same for two different nodal bases exactly when the stated linear condition on the lambda_i holds.
- **N = 8 verified** (experiment `sfe8`). With the paper's basis K_1..K_8 (lines 892-905) and the standard Zienkiewicz basis, K_i - N_i = +B/4 at the four corners and -B/4 at the four mid-sides, where B = (1 - x^2)(1 - y^2). Hence f_K - f_Z = (B/4)(sum of corner values - sum of side values), which vanishes exactly when corner mean = side mean. The paper's K basis is nodal and sums to 1, with loads 1/9 (corners) and 8/9 (sides), all positive; the standard basis has corner loads -1/3, which is the "Zienkiewicz's paradox" of Section 5.2 comment 2.
- **General N: unclear.** The proof introduces functions Q_i and gamma_j and node counts q_1..q_4 given by cubic expressions in b = N mod 4 (e.g. q_1 = (N + 2b^3/3 - 4b^2 + 19b/3 - 4)/4, line 950) without defining Q_i or deriving the counts, and asserts the "expected value" statement. It does not say with respect to which family of bases invariance is claimed for N > 8. See ISSUE-008.
- **Not load-bearing.** At line 1147-1149 the paper writes "We can assume without loss of generality that (sum_{i=1}^4 lambda_i / 4) * w(N,t) = sum_{i=5}^N lambda_i / (N - 4), where w(N,t) is a stabilization function", that is, it replaces the condition by an identity that defines the factor w.

### Stepanets' extremal problem, restated from [26] (lines 1052-1121, page 14)

For nonincreasing positive alpha with limit 0 and sequences m >= 0 with sum m_k <= 1, E_n(alpha, r) is the supremum over m of (sum alpha_k m_k^r - sup over n-subsets of the partial sum); (i) gives a closed form for r >= 1 and (ii) for 0 < r < 1, both in terms of an index s* > n determined by a supremum.

- Line 1119, "Note. 1. s* = P(n), here P(n) is a polynomial", is the paper's addition, not part of [26]. s* depends on alpha and n through a supremum; no bound is derived. See ISSUE-007.
- Application (lines 1132-1137): "lambda_i(t) > 0, lambda_i(t) decreasing, lim lambda_i(t) -> 0, L_i(x,y) = m_i^r". The functions L_i(x,y) are identified with the numbers m_i^r of the extremal problem. At a fixed point the values L_i(x,y) sum to 1, but serendipity basis functions take negative values inside the square (the paper's own K_2 = -(1/4)(1 + x)(1 - y) x y is negative for x, y > 0), while m_k^r with 0 < r < 1 needs m_k >= 0. Lemma 5.5 relaxes to |m_k| <= 1 but only for r = 1. The lambda sequence is finite (N values) while [26] is about infinite sequences; line 1137 "N -> infinity (word length)" treats the number of instances and the length of a word as the same quantity.

### Ideology of P = NP (lines 1139-1141, page 15)

"Due to checking the first M instances (see 1st stage: configuration of nodes) with total computational complexity of O(n^k), we can identify (N - M) instances without checking them, here M is polynomially bounded." Footnote 17: "We are able to level the specified surplus of instances, N (see 2nd stage). We are interested in the case when M instances is a collection of C-bar. Our goal is to determine a position number of C in (N - M) instances or to identify that all (N - M) instances are C-bar."

- This is the content of the theorem: the answers of the first M instances in weight order determine the answers of all the others. The mechanism offered is the system U below.
- "The first M" are the M instances of smallest weight, that is of smallest numeric encoding.
- **Experiment `weight_order`.** Every CNF formula with 3 variables and 3 clauses of width 1 to 3, listed in the numeric order of its word (17,576 instances): the answer changes between neighbours 862 times, and the part after the first M instances has at most one change only from M = 17,034 (96.9 % of all instances). With 4 clauses (456,976 instances): 48,948 changes, M = 99.9 %. With 4 variables and 3 clauses (262,144 instances): 2,554 changes, M = 98.6 %. Satisfiable and unsatisfiable instances interleave along the whole order; there is no "position number of C" to find. See ISSUE-005.

### Agreement, the factor w, Claim 5.3, Corollary 5.4 (lines 1142-1172, page 15)

- Line 1142: "Without loss of generality it can be assumed that a functional type of lambda_i(t) = f_i(t) is not principled; all required g_1, ..., g_{M+1} are defined at time t = T*."
- w(N,t), the "stabilization function", is introduced (line 1149) as whatever makes the equality of Claim 5.2 hold.
- Claim 5.3 (line 1152): the FF at the barycentre, sum_{i=1}^N lambda_i(t) / N, "equals kappa * w(N,t) * E_n(lambda(t), 1), here kappa = const, see (i)". Proof (lines 1157-1163): "It is easily shown that sum_{i=1}^{s*} lambda_i(T*) / s* = kappa * w(s*, T*) * E_n(lambda(T*), 1), where s* = M. Taking into account [the w identity] ... by induction, we obtain the statement."
  - kappa is unspecified, w is fixed only by one identity, E_n(lambda, 1) is a number computed from lambda. The claim reads "a number equals an unspecified constant times an unspecified function times a number"; any positive left-hand side satisfies it. "Easily shown" and "by induction" are the entire proof. (i) of [26], which needs an infinite sequence, is applied to the finite sequence lambda_1..lambda_N.
- Corollary 5.4 (line 1164): a formula for w(N, T*) and the r-power analogue with a further constant upsilon; "The proof is omitted."
- See ISSUE-004.

### The system U (lines 1176-1217, page 15; comments lines 1218-1284, pages 15-16)

Line 1174-1176: "Using claim 5.3, corollary 5.4 and the results of the Bogolyubov principle of the decay of correlations for an infinite three-dimensional systems [27], [28] for the FF (see figure 7), we have the following system U for determination of lambda_i(t), here i > s*."

1. sum_{i=1}^N lambda_i / N = kappa * w(N,t) * E_n(lambda(t), 1)
2. (sum_{i=1}^4 lambda_i^r / 4) * w^r = sum_{i=5}^N lambda_i^r / (N - 4)
3. sum_{i=1}^N lambda_i^r / N = upsilon * w^r * E_n(lambda(t), 0 < r < 1)
4. dF/dt = -L F + a L^int F, F(0) given: the BBGKY hierarchy for hard spheres in R^3, equations (5.1)-(5.4) copied from [27]
5. lambda_i for s*+1 <= i <= s*+upsilon, T* <= t <= T**, "such that H_i = 0.5 C_i + 0.5 C-bar_i (in the case of t = T*)"
6. lambda_i for s*+upsilon+1 <= i <= N, t >= T*: "= |g_i - g_{i+1}| approx 0".

- U is to determine the unknown answers lambda_i, i > s* = M. Its content: (1)-(3) are relations among sums of the lambda_i and of their r-th powers, with unspecified kappa, upsilon, w; (4) is a kinetic equation for a gas of hard spheres; (5) fixes a block of upsilon instances to the undecided value at T*; (6) sets the whole remaining tail to approximately zero, with the comment "g_{j+1}, g_j are indistinguishable" (line 1281).
- **The instances S_i, their weights chi_i and the basis functions L_i do not occur in U.** Whatever U determines, it determines without reading the formulas. See ISSUE-002.
- Equation (4) is tied to the field function by one sentence (line 1275): "f(x,y,t) is a phase space: each z-axis at the node is a particle of unit mass and diameter rho > 0 such that |q_i - q_j| >= rho." No map from nodal values or instances to particle positions and momenta is defined; nothing computed from (5.1)-(5.4) is used afterwards except the sentence "the number of r is polynomially bounded" (line 1280). See ISSUE-006.
- The conclusion drawn (line 1283): "This implies that lim_{t -> T** - 0} lambda_{s*+1 <= i <= s*+upsilon}(t) -> {g_i, g_{i+1}}", that is, the undecided values settle to one of the two answers. Which one is not determined by anything stated.

### Complexity accounting (lines 1286-1303, page 16)

"1. Checking the first M instances with total computational complexity of O(n^k) (see ideology of P = NP). 2. The analysis of U: 2a. checking lambda^{0<r<1}_{1<=i<=s*}(t) with total computational complexity of O(n^{k'}). 2b. determination of lambda_{s*+1<=i<=s*+upsilon} with total computational complexity of O(n^{k''}). ... 2c. Consider the segment s*+upsilon+1 <= i <= N as the union over 1 <= j <= theta of z_j, plus P, here each of z_j contains l values such that l >> upsilon; where theta, P are polynomials. Determination of each lambda_{z_j} is realized due to permutation with previously defined lambda_{s*+1<=i<=s*+upsilon} (we take upsilon ... evenly spaced representatives from each z_j including endpoints) with total computational complexity of O(n^{k'''}). Thus we have leveled the surplus of (N - M) instances of the Boolean satisfiability problem, so P = NP."

- Item 1 asserts that checking M SAT instances costs O(n^k). The cost of checking one instance of length n on a DTM is the quantity the theorem is about, and the paper gives no method for it. Read as the DTM check of the preamble, item 1 assumes the conclusion for the first M instances. Read as "the M smallest encodings are trivial", their answers carry no information about the rest (experiment above).
- Items 2a-2c assign exponents k', k'', k''' to steps that are never described as computations. theta and P "are polynomials" by declaration. In 2c the tail of N - M - upsilon instances is cut into theta blocks of l >> upsilon values each and every block is "determined ... due to permutation" of upsilon representatives; no sentence explains why the answer of a non-representative instance equals that of any representative. The number N of instances of length n is exponential in n while theta and upsilon are polynomial, so almost every instance is a non-representative.
- No polynomial is derived anywhere. See ISSUE-003.

### 5.1 Implementation model on the DTM (lines 1307-1322, page 17)

"Using the DTM with polynomial memory, we cannot print on tape all instances of the Boolean satisfiability problem in polynomial time, but we can numerate them on tape in polynomial time. We will operate with polynomially bounded collection of computable values g_1, ..., g_M, ..., g_{s*+upsilon+1} (including (theta * upsilon + P) representatives from each z_j (see 2c)) such that the relevant collection of computable 'weights' chi_1 = ... < ... < chi_P = ... is given (see 2nd stage)." Then (line 1319): "Using theorem 5.1, we cannot make a permutation between two numerated instances, which are not the representatives from each z_j, because a priori we take into account their unique 'weights' (see 2nd stage)."

- No input, no output, no step. Nothing says what the machine does when handed a formula. The second paragraph invokes Theorem 5.1 inside the description of its own implementation. See ISSUE-001.

### 5.2 General comments (lines 1323-1358, page 17)

- Comment 1 (line 1330): "theorem 5.1 is not a universal algorithm (specifically, for the TSP)." A polynomial-time decision procedure for SAT gives one for every NP problem, the decision version of TSP included (Cook-Levin 1971, Karp 1972). The author therefore does not claim what P = NP means in the standard sense. See ISSUE-009.
- Comment 2 (lines 1333-1348): the one-parameter mixing of two bases (see 2nd stage) and an "alternative apparatus" of substitute functions that are not nodal.
- Comment 4 (line 1353): "The article was 16 years in the making. AI was not used." Perspective (line 1355): NP within BQP via a quantum Turing machine.

### 5.3 Appendix, Lemma 5.5 (lines 1359-1498, pages 18-19)

Setting: real sequences m with |m_k| <= 1 and sum m_k <= 1; alpha nonincreasing and nonnegative with alpha_k = 0 for k > N (line 1368 says "k > s", a typo). E_n(alpha) is the supremum over m of sum_{k<=N} alpha_k m_k minus the largest n-term partial sum.

- Lemma: E_n(alpha) = sum_{k=n+1}^N alpha_k, attained by m* = (1 repeated N times, -1 repeated N-1 times, 0, ...).
- **True**, with a two-line proof. For any admissible m, choosing the n-subset {1, ..., n} inside the inner supremum gives E_n(m) <= sum_{k=n+1}^N alpha_k m_k <= sum_{k=n+1}^N alpha_k, since alpha_k >= 0 and m_k <= 1. The sequence m* is admissible (its sum is N - (N - 1) = 1) and gives equality because the first n terms alpha_k are the largest.
- The paper's page-long rearrangement argument (steps 1 to N, lines 1400-1480) is unnecessary; it does not check that the rearranged sequence keeps |m_k| <= 1 when entries are negative, but the lemma does not depend on it.
- Not used in the proof of Theorem 5.1: Claim 5.3 invokes (i) of [26] with r = 1, not Lemma 5.5. Status: ok.

## Questions

1. What are the input and the output of the algorithm of Theorem 5.1? (ISSUE-001)
2. Which quantity in the system U depends on the clause structure of an instance? (ISSUE-002)
3. By what method are the first M instances "checked" within O(n^k)? (ISSUE-003)
4. For N > 8, invariance with respect to which family of bases does Claim 5.2 assert, and what are the functions Q_i? (ISSUE-008)
5. How is a nodal basis with N prescribed loads constructed, and why is it unique? (ISSUE-005)

## Checks performed

- Experiment `sfe8` (`src/pnp_check/sfe8.py`, `tests/test_sfe8.py`): Claim 5.2 at N = 8, nodal property, partition of unity, loads. Result: the claim holds for the pair (paper's K, Zienkiewicz).
- Experiment `weight_order` (`src/pnp_check/weight_order.py`, `tests/test_weight_order.py`): satisfiability along the weight order for three exhaustive families. Result: no prefix shorter than 96.9-99.9 % of all instances makes the rest readable.
- Grep of lines 622-1306 for citations of Sections 2-4: none beyond the phrase "labeled geo-plafal".
- Page images 10-17 consulted for every formula quoted above.
