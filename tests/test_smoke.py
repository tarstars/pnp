from pnp_check import PAPER_TXT, paper_lines


def test_paper_text_present():
    assert PAPER_TXT.exists()


def test_theorem_5_1_is_where_the_ledger_says():
    assert paper_lines(633, 633)[0].startswith("Theorem 5.1.")


def test_proof_ends_with_p_eq_np():
    assert "so P = NP" in paper_lines(1303, 1303)[0]
