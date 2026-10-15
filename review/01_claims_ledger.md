# Claims ledger

Every numbered statement of the paper, in order. One row per statement; detailed reasoning lives in `review/sections/`, problems get an entry in `review/02_issues.md` and are linked from the *Notes* column.

Status values: `unchecked` · `ok` (statement and proof accepted) · `unclear` (cannot be evaluated as written) · `gap` (proof step missing or unjustified) · `error` (statement or proof is wrong). Page and line refer to the PDF and to `paper/paper.txt` respectively.

Total: 41 statements Definition 27, Claim 10, Theorem 1, Lemma 1, Corollary 2.


## Section 2. Concept of the plafal

| ID | Page | Line | Statement (opening) | Status | Notes |
|---|---|---|---|---|---|
| Definition 2.1 | 2 | 66 | A plafal is a tuple hG, P F, Pi and is denoted by P F or P Fji , where G = G(V, E) is a simple graph2, i =... | unchecked | |
| Claim 2.2 | 2 | 93 | V, E are categories. Proof. Let us show for V. idv ◦idv = idv , idVe ◦idVe = idVe , v◦idv = v, idVe ◦v = v.... | unchecked | |
| Definition 2.3 | 2 | 96 | A plafal is a tuple hASC, Disc, Fi, where ASC is a 1-dimensional abstract simplicial complex (considering a... | unchecked | |
| Definition 2.4 | 2 | 101 | Labeled plafal is a type of the plafal, where all or some of vertices π1 and/or edges are enumerated. We ha... | unchecked | |

## Section 3. The category of plafales and operations

| ID | Page | Line | Statement (opening) | Status | Notes |
|---|---|---|---|---|---|
| Definition 3.1 | 4 | 183 | A plafal morphism P F −−−−−→ P F 0 is a tuple of maps’s collec- tions such that f | unchecked | |
| Claim 3.2 | 4 | 193 | Plafales and plafal morphisms form the category Plafales, together with the componentwise compositions hf,... | unchecked | |
| Definition 3.3 | 4 | 224 | hb 0G(P Fji ) = h∅, ∅i, P F = h∅, ∅ii is called an empty plafal and is denoted by P F emp | unchecked | |
| Claim 3.4 | 4 | 230 | In Plafales, there’re no initial and terminal objects. Proof. Initial. Omitted. Terminal. In SimpGph, there... | unchecked | |
| Definition 3.5 | 4 | 232 | Q A product of two plafales P F prod = P F × P F 0 is defined by the 0 graph product = G(P F ) × G(P F ) an... | unchecked | |
| Definition 3.6 | 4 | 243 | A coproduct of two plafales P F coprod = P F + P F 0 is defined by = G(P F ) + G(P F 0 ) and the following... | unchecked | |
| Claim 3.7 | 5 | 254 | In Plafales, the (co)-product of any two plafales does not always exist. Proof. It is sufficient to conside... | unchecked | |
| Corollary 3.8 | 5 | 258 | Plafales is not a (quasi)-topos. The proof is streightforward. 3.1. Basic operations. | unchecked | |
| Definition 3.9 | 5 | 287 | A union of plafales P F un is defined by H un and the following condition holds: ecommon = S | unchecked | |
| Definition 3.10 | 5 | 295 | A docking of plafales P F doc is defined by H un and the following condition holds: (i) V | unchecked | |
| Definition 3.11 | 5 | 302 | A docking• of plafales P F doc• is defined by H un and the following condition holds: (i) Condition (i) of... | unchecked | |
| Definition 3.12 | 5 | 307 | An intersection of plafales P F in is defined by H in and the fol- lowing condition holds: ecommon = T | unchecked | |
| Definition 3.13 | 6 | 320 | A merger of plafales P F m is defined by H in and the following condition holds: (i) V | unchecked | |
| Definition 3.14 | 6 | 326 | A merger• of plafales P F m• is defined by H in and the following condition holds: (i) Condition (i) of def... | unchecked | |
| Definition 3.15 | 6 | 404 | A Q product• of two plafales P F prod• = P F × P F 0 is defined by 0 the graph product = G(P F ) × G(P F )... | unchecked | |
| Definition 3.16 | 6 | 414 | A decomposition of plafales is a collection of maps such that Hd S(P) S(G(P F )) −−→ S(G(P F )) −−−→ S(P F... | unchecked | |

## Section 4. Geo-space

| ID | Page | Line | Statement (opening) | Status | Notes |
|---|---|---|---|---|---|
| Definition 4.1 | 7 | 431 | A geo-space is a tuple hR3 , U i and is denoted by \|P F \|U , where U is a universe of U-standard such that... | unchecked | |
| Definition 4.2 | 7 | 439 | h\|G\|, P F i is a geo-plafal and is denoted by \|P F \|, \|G\| is the geo- P0 P metric realization of G in R3 s... | unchecked | |
| Definition 4.3 | 7 | 445 | h\|K\|, \|K\|, T i is a geo-plafal and is denoted by \|P F \| or \|P F \|ij , where \|K\| is a 1-dimensional simplic... | unchecked | |
| Definition 4.4 | 7 | 476 | A geo-plafal morphism \|P F \| −−−−−−→ \|P F \|0 is a tuple of maps’s collections such that ϑ | unchecked | |
| Claim 4.5 | 7 | 486 | Geo-plafales and geo-plafal morphisms form the category Geo-Plafales, together with the componentwise compo... | unchecked | |
| Definition 4.6 | 8 | 494 | A product of Qtwo geo-plafales \|P F \|prod = \|P F \| × \|P F \|0 is defined 0 by the product of polyhedra = \|K\|... | unchecked | |
| Definition 4.7 | 8 | 505 | A coproduct of two geo-plafales \|P F \|coprod = \|P F \| + \|P F \|0 is defined by the disjoint union of polyhed... | unchecked | |
| Claim 4.8 | 8 | 512 | In Geo-plafales, there’re no initial and terminal objects. The (co)- product of any two geo-plafales does n... | unchecked | |
| Definition 4.9 | 8 | 522 | hpl, pl = U-standard, X i is a limit point and is denoted by \|P F \|pl , X where pl is a limit point in R3... | unchecked | |
| Definition 4.10 | 8 | 531 | A morphism \|P F \|pl pl i −−−−−−→ \|P F \|j is a tuple of maps’s collec- tions such that | unchecked | |
| Claim 4.11 | 8 | 540 | S(\|P F \|pl ) and morphisms tpl form the category PFpl. Proof. id\|P F \|pl = hidpl , idpl i. We get the foll... | unchecked | |
| Definition 4.12 | 9 | 571 | hM, M = U-standard, Ii is a manifold and is denoted by \|P F \|M , where M is a topological manifold in R3 ,... | unchecked | |
| Definition 4.13 | 9 | 583 | A morphism \|P F \|M M i −−−−−−→ \|P F \|j is a tuple of maps’s col- lections such that | unchecked | |
| Claim 4.14 | 9 | 591 | S(\|P F \|M ) and morphisms tM form the category PFM. Omitted. Definitions 4.6 and 4.7 (in terms of the produ... | unchecked | |
| Definition 4.15 | 9 | 596 | hhS, Gi, hU, Ωii is a dynamical system and is denoted by d \|P F \|U , where S = hR3 , τ i is a locally compa... | unchecked | |
| Definition 4.16 | 9 | 601 | A homomorphism d \|P F \|U U i −−−−−−−→ \|P F \|j is a tuple of maps’s collections such that | unchecked | |

## Section 5. P = NP

| ID | Page | Line | Statement (opening) | Status | Notes |
|---|---|---|---|---|---|
| Theorem 5.1 | 10 | 633 | Based on the theory of plafales, there exists an algorithm that allows to identify all instances of the Boo... | error | Proof does not establish the statement; no input/output/steps (ISSUE-001), U reads no instance (ISSUE-002), no polynomial derived (ISSUE-003). Statement itself undecided. |
| Claim 5.2 | 11 | 789 | In general, for SFE on N vertices the condition of invariant of the field function (stability of the FF w.r... | unclear | Holds for N = 8 (experiment sfe8). General-N proof not followable (ISSUE-008). Not load-bearing: replaced by the factor w at line 1147. |
| Claim 5.3 | 15 | 1152 | The value of the field function at the barycentre18 N equals κ · $(N, t) · En (λ(t), 1), here κ = const, se... | gap | kappa and w unspecified; proof is 'easily shown ... by induction' (ISSUE-004, ISSUE-007). |
| Corollary 5.4 | 15 | 1164 | We get $(N, T ∗ ) = 4·N ·κ·E (λ(T ∗ ),1)−(N i=1 i −4)· 4 | gap | 'The proof is omitted' (ISSUE-004). |
| Lemma 5.5 | 18 | 1382 | Let α ∈ AN , N ∈ N. Then for any n = 0, 1, . . . , n < N N X | ok | True; two-line direct proof in section notes. Typo 'k > s' for 'k > N'. Not used in the proof of Theorem 5.1. |

## Unnumbered load-bearing steps (Section 5)

Steps that carry the argument but have no statement number. Treated like statements.

| ID | Page | Line | Step | Status | Notes |
|---|---|---|---|---|---|
| S5-CT | 10 | 636 | Computational template: labeled geo-plafal on a serendipity finite element with N boundary nodes | unclear | Square with N boundary nodes; H_i mixture never governed; instance enters only as a number; basis with prescribed loads asserted (ISSUE-005). |
| S5-IDEO | 15 | 1139 | Ideology of P = NP: checking the first M instances identifies the remaining N - M without checking | error | U contains no instance (ISSUE-002); BBGKY block inert (ISSUE-006); weight order carries no information, experiment weight_order (ISSUE-005). |
| S5-COMPLX | 16 | 1286 | Total complexity accounting (items 1, 2a, 2b, 2c) ending in "so P = NP" | error | Item 1 assumes the conclusion; exponents and polynomials declared, none derived (ISSUE-003). |
| S5-DTM | 17 | 1307 | Implementation model of Theorem 5.1 on a deterministic Turing machine | error | No input, output or step; invokes Theorem 5.1 inside its own implementation (ISSUE-001). |
