# Summary of the paper

- **Title.** The theory of plafales: P vs NP problem solution
- **Author.** Dmytro Topchyi
- **Date.** 11 September 2026 (`paper/paper.txt` line 48). 20 pages, 5 sections, 28 references.
- **MSC 2020.** Primary 00-02, 00A05, 68Q15.

## Claim

Theorem 5.1 (page 10, line 633): "Based on the theory of plafales, there exists an algorithm that allows to identify all instances of the Boolean satisfiability problem in polynomial time." The proof ends with "so P = NP" (page 16, line 1303).

The abstract describes the architecture: the geo-plafal is the "kernel (computational template)" of the proof; the constructive theory of serendipity approximations (Khomchenko's school), Stepanets' school and the Bogolyubov principle of the decay of correlations are its "shell".

## How the paper is organised

| Section | Pages | Content |
|---|---|---|
| 1. Introduction | 1 | History of the theory of plafales (books of 2011 and 2013) and prior applications: finite elements, software, two block ciphers. |
| 2. Concept of the plafal | 2-3 | A plafal is a simple graph whose vertices and edges carry arbitrary "U-standard" mathematical objects (Def. 2.1), restated categorically (Def. 2.3); labeled plafales (Def. 2.4). |
| 3. The category of plafales and operations | 4-7 | Morphisms and the category Plafales (Claim 3.2); no initial or terminal objects (Claim 3.4); (co)products need not exist (Claim 3.7); not a (quasi)-topos (Cor. 3.8); basic operations (3.1); Definitions 3.9-3.16. |
| 4. Geo-space | 7-10 | Geo-plafal (4.1), point (4.2), manifold (4.3), dynamical system (4.4). Definitions 4.1-4.16, Claims 4.5, 4.8, 4.11, 4.14. |
| 5. P = NP | 10-18 | Theorem 5.1 and its proof; Claims 5.2 and 5.3, Cor. 5.4; 5.1 implementation model on a DTM; 5.2 general comments; 5.3 appendix with Lemma 5.5. |

## Architecture of the proof of Theorem 5.1, as the paper presents it

1. **Computational template** (page 10, line 636). A labeled geo-plafal built on a serendipity finite element: the square D = {|x| <= 1, |y| <= 1} with N nodes evenly spaced on its boundary, where the residue of the node index mod 4 selects the side of the square.
2. **Field functions** lambda_i(t) attached to the nodes, analysed with the constructive theory of serendipity approximations (CTSA, refs [4], [15-24]) and the extremal problem for positive series of Stepanets' and Shydlich [26] (Lemma 5.5 in the appendix).
3. **"Ideology of P = NP"** (page 15, line 1139). Checking the first M instances, M polynomially bounded, with total cost O(n^k) lets the procedure "identify (N - M) instances without checking them".
4. **Complexity accounting** (page 16, line 1286). Items 1, 2a, 2b and 2c are each claimed O(n^k) for some exponent; the remaining index range is split into blocks z_j handled by permutation with already-determined values; conclusion "so P = NP".
5. **Implementation model on a DTM** (page 17, line 1307). Instances are "numerated on tape in polynomial time"; the machine operates on a polynomially bounded collection of computable values g_1, ..., g_{s*+v+1} and weights chi.

## Terms used by the paper

- **Plafal / plafale** (plural plafales): the author's object, a graph with arbitrary mathematical entities attached to its vertices and edges.
- **U-standard**: a size condition on mathematical entities taken from Levy's "Standard by default" [11].
- **Geo-plafal, geo-space**: plafales whose attached entities are geometric (Section 4).
- **Serendipity finite element (SFE)**: a finite element of the serendipity family; here the square with boundary nodes only.
- **CTSA**: constructive theory of serendipity approximations, the author's name for the Khomchenko school's work on serendipity elements.
- **Instance S**: an instance of an NP-complete problem; C marks instances answered "Yes" by a deterministic Turing machine (DTM).

## Where the proof must be examined first

Listed as questions, not findings. Each has a ledger row.

1. **What does "identify all instances" mean?** The theorem must be read as a decision procedure: input a formula of length n, output satisfiable or not, in time polynomial in n. The text speaks of N instances and of the word length N -> infinity; the correspondence between instances, nodes and inputs has to be pinned down. Ledger: Theorem 5.1.
2. **The extrapolation step.** The "ideology" step infers answers for N - M instances from M checked ones. The justification offered is a limit statement on the field functions (lines 1136-1150 and 1283-1303) via [26] and [27]. Whether any property of SAT instances follows from a property of the node functions is the central question. Ledger: S5-IDEO, S5-COMPLX, Claim 5.2.
3. **Is there an algorithm?** Section 5.1 should specify input encoding, steps and output. Ledger: S5-DTM.
4. **Are Sections 2-4 load-bearing?** If the proof of Theorem 5.1 uses only the square with N boundary nodes, the category-theoretic apparatus can be checked separately from the complexity claim. Ledger: Definitions 2.1-4.16.
5. **External dependencies.** The argument cites [4] and [15-24] (theses and regional journals, Kherson and Mykolaiv) and "about 1000 papers" of CTSA. Which results are used, and whether they can be obtained, is tracked in `refs/bibliography.md`.
