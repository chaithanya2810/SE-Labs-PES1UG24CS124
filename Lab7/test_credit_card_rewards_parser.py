from hypothesis import given, strategies as st

from credit_card_rewards_parser import (
    mask_card_number,
    parse_transaction,
    parse_statement_total
)


@given(st.text() | st.none())
def test_mask_card_number_no_crash(s):
    try:
        mask_card_number(s)
    except Exception as e:
        assert False, f"mask_card_number crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_parse_transaction_no_crash(s):
    try:
        parse_transaction(s)
    except Exception as e:
        assert False, f"parse_transaction crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_parse_statement_total_no_crash(s):
    try:
        parse_statement_total(s)
    except Exception as e:
        assert False, f"parse_statement_total crashed with input {s!r}: {e}"

# Additional tests to verify correct outputs and invalid input handling

def test_mask_card_number_expected_results():
    assert mask_card_number("4111 1111 1111 1234") == "************1234"
    assert mask_card_number("1234") == "1234"
    assert mask_card_number("123") is None
    assert mask_card_number(None) is None


def test_parse_transaction_expected_results():
    assert parse_transaction("2026-11-11,dining,1550") == ("dining", 1550)
    assert parse_transaction(None) is None
    assert parse_transaction("") is None
    assert parse_transaction("2026-11-11,dining,abc") is None
    assert parse_transaction("2026-11-11,,1550") is None


def test_parse_statement_total_expected_results():
    assert parse_statement_total("Total: 12,500") == 12500
    assert parse_statement_total("Total: 12500") == 12500
    assert parse_statement_total(None) is None
    assert parse_statement_total("") is None
    assert parse_statement_total("Total: 12,50") is None
    assert parse_statement_total("Total: twelve") is None