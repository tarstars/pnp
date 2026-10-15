# Design: repository for checking Topchyi's P = NP proof

Date: 2026-10-15. Status: implemented as the initial layout.

## Intent

Check the proof of P = NP in "The theory of plafales: P vs NP problem solution" (D. Topchyi, 11 September 2026, 20 pages) and reach a defensible verdict, with every finding traceable to a line of the paper.

## Assumptions

- The deliverable is a review repository (ledger, issue log, verdict) plus computational checks where the paper's constructions are concrete. Formal verification in a proof assistant is out of scope until a step is found that would benefit from it.
- Python with uv, matching the owner's other projects.
- The text extraction of the PDF is committed so that notes cite stable line numbers; `scripts/extract_paper.sh` regenerates it with fixed flags.

## Structure

- `paper/`: source PDF and `paper.txt`.
- `review/`: `00_summary.md` (claim and proof architecture), `01_claims_ledger.md` (41 numbered statements and 4 unnumbered load-bearing steps, one status each), `02_issues.md` (numbered issues with severity), `03_verdict.md` (criteria and final assessment), `sections/` (working notes per section).
- `refs/bibliography.md`: 28 references with role and access status.
- `experiments/`, `src/pnp_check/`, `tests/`: computational checks; `pnp_check.paper_lines` ties tests to cited text.

## Conventions

- Ledger statuses: `unchecked`, `ok`, `unclear`, `gap`, `error`.
- Issue severities: `fatal`, `major`, `minor`, `unclear`. IDs `ISSUE-NNN`.
- Every claim about the paper quotes it with a page and a `paper.txt` line.
- Open questions are recorded as questions; a verdict is written only once the ledger is complete.

## Out of scope for the initial layout

Any actual evaluation of the statements. The ledger is fully `unchecked` on purpose.
