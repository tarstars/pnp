# Checking the P = NP proof of Topchyi (September 2026)

Review repository for the paper **"The theory of plafales: P vs NP problem solution"** by Dmytro Topchyi, dated 11 September 2026 (20 pages). Its central claim is Theorem 5.1: an algorithm identifies all instances of the Boolean satisfiability problem in polynomial time, hence P = NP.

Goal: establish whether the proof holds, and document exactly where it does or does not.

## Verdict

Open until Sections 2-4 are reviewed, but Section 5 (the whole proof of Theorem 5.1) is done: the proof does not establish the theorem. Three independent defects, each sufficient: no algorithm is specified (ISSUE-001); the system that is to produce the unchecked answers never reads an instance (ISSUE-002); the complexity count assumes the conclusion and derives no polynomial (ISSUE-003). See `review/03_verdict.md` and `review/02_issues.md`, or the article `report/review.pdf`.

## Layout

| Path | What it holds |
|---|---|
| `paper/` | The PDF and its text extraction `paper.txt` (regenerate with `scripts/extract_paper.sh`). Notes cite `paper.txt` by line number. |
| `review/00_summary.md` | What the paper claims and how the proof is organised. Start here. |
| `review/01_claims_ledger.md` | Every numbered statement (41) plus the unnumbered load-bearing steps of Section 5, each with a status. |
| `review/02_issues.md` | Numbered log of problems found, with severity and location. |
| `review/03_verdict.md` | The final assessment and the criteria it is judged against. |
| `review/sections/` | Section-by-section working notes. |
| `report/` | The review as an article: `review.tex` and the compiled `review.pdf` (rebuild with `scripts/build_report.sh`). |
| `refs/bibliography.md` | The 28 references, their role in the argument, and whether we obtained them. |
| `experiments/` | Computational checks of concrete constructions from the paper. |
| `src/pnp_check/`, `tests/` | Python package and tests backing the experiments. |
| `docs/superpowers/specs/` | Design notes for this repository. |

## Workflow

1. Read `review/00_summary.md`.
2. Pick a statement from the ledger and work through it in the matching `review/sections/` file, citing `paper/paper.txt` lines.
3. Set its status in the ledger. Anything other than `ok` gets an entry in `review/02_issues.md`.
4. When a claim is concrete enough to compute, add an experiment (see `experiments/README.md`) and link it from the issue.
5. The verdict is written only when every ledger row has left `unchecked`.

## Tooling

```
uv sync
uv run pytest
```

Regenerating the paper text needs `pdftotext` from poppler-utils. Building the article needs TeX Live with `latexmk` and `pgfplots`.
