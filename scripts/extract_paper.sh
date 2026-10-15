#!/usr/bin/env bash
# Regenerate paper/paper.txt from the PDF. Review notes cite paper.txt by line
# number, so keep the extraction flags stable (-layout) or re-check citations.
set -euo pipefail
cd "$(dirname "$0")/.."
pdftotext -layout paper/P_vs_NP_problem_by_Topchyi_sep_2026.pdf paper/paper.txt
echo "wrote paper/paper.txt ($(wc -l < paper/paper.txt) lines)"
