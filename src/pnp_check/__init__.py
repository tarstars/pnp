"""Computational checks for the review of Topchyi's P = NP paper (September 2026)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER_TXT = ROOT / "paper" / "paper.txt"


def paper_lines(start: int, end: int) -> list[str]:
    """Return lines start..end (1-based, inclusive) of paper/paper.txt.

    The review cites the paper by these line numbers; experiments quote the
    text they test against through this helper so a re-extraction that shifts
    lines fails loudly.
    """
    lines = PAPER_TXT.read_text().split("\n")
    return lines[start - 1 : end]
