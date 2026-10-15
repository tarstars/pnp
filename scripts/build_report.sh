#!/usr/bin/env bash
# Build report/review.pdf from report/review.tex with latexmk (TeX Live with pgfplots).
# Auxiliary files go to report/build/ (ignored by git); the PDF is copied next to the source.
set -euo pipefail
cd "$(dirname "$0")/../report"
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build review.tex > build/latexmk.log 2>&1 \
  || { tail -40 build/latexmk.log; exit 1; }
cp build/review.pdf review.pdf
echo "wrote report/review.pdf ($(pdfinfo review.pdf | awk '/^Pages/ {print $2}') pages)"
