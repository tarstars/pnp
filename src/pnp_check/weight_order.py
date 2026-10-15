"""Satisfiability along the paper's weight ordering of instances.

Second stage of the proof (page 11, paper.txt lines 757-763): each instance is a
word S_i over an alphabet, its weight is chi_i = S_i / sum(S_j), and the nodes
are configured so that chi_1 < chi_2 < ... (third stage, line 766). Footnote 17
(page 15) states the goal: after checking the first M instances, "determine a
position number of C in (N - M) instances or to identify that all (N - M)
instances are C-bar" (C = satisfiable, C-bar = unsatisfiable).

This module enumerates every CNF formula with n variables and m clauses of
width 1 to 3 as a
fixed-length word over the alphabet of clauses, in numeric (= lexicographic)
order, decides each by brute force, and measures how satisfiability behaves
along that order.
"""

from __future__ import annotations

from itertools import combinations, product


def clauses(n: int, widths: tuple[int, ...] = (1, 2, 3)) -> list[tuple[tuple[int, ...], int]]:
    """All clauses of the given widths over n variables, distinct variables per clause.

    The list is the alphabet; its index order (width, then variables, then signs)
    fixes the numeric order of words. Returns (literals, mask): literals as signed
    1-based ints, mask as a bitmask over the 2**n assignments satisfying the clause.
    Widths 1..3 are used so that unsatisfiable formulas exist at small sizes
    (3-literal clauses alone need at least 8 clauses to be unsatisfiable).
    """
    out = []
    for w in widths:
        for vars_ in combinations(range(n), w):
            for signs in product((1, -1), repeat=w):
                lits = tuple(s * (v + 1) for v, s in zip(vars_, signs))
                mask = 0
                for a in range(1 << n):
                    if any(((a >> v) & 1) == (1 if s > 0 else 0) for v, s in zip(vars_, signs)):
                        mask |= 1 << a
                out.append((lits, mask))
    return out


def sat_sequence(n: int, m: int) -> list[bool]:
    """Satisfiability of every m-clause formula, in the numeric order of its word."""
    masks = [mask for _, mask in clauses(n)]
    seq = []
    for word in product(range(len(masks)), repeat=m):
        acc = (1 << (1 << n)) - 1
        for c in word:
            acc &= masks[c]
        seq.append(acc != 0)
    return seq


def switches(seq: list[bool]) -> int:
    """Number of positions where the answer changes between neighbours in the order."""
    return sum(1 for a, b in zip(seq, seq[1:]) if a != b)


def min_prefix_for_readable_suffix(seq: list[bool]) -> int:
    """Smallest M such that the answers after position M change at most once.

    That is the weakest form of the paper's goal: with the first M checked, the
    rest is either constant or has a single 'position number' where it flips.
    """
    n = len(seq)
    # count switches in suffixes from the right
    suffix_switches = [0] * (n + 1)
    for i in range(n - 2, -1, -1):
        suffix_switches[i] = suffix_switches[i + 1] + (seq[i] != seq[i + 1])
    for m in range(n + 1):
        if suffix_switches[m] <= 1:
            return m
    return n


def summary(n: int, m: int) -> dict[str, int | float]:
    seq = sat_sequence(n, m)
    total = len(seq)
    sw = switches(seq)
    prefix = min_prefix_for_readable_suffix(seq)
    return {
        "variables": n,
        "clauses": m,
        "instances": total,
        "satisfiable": sum(seq),
        "switches": sw,
        "switches_per_instance": sw / total,
        "min_prefix_for_readable_suffix": prefix,
        "prefix_fraction": prefix / total,
    }
