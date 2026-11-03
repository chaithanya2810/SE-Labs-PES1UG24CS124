import pytest

from credit_card_rewards import card_status, late_payment_fee, reward_points


def test_unknown_card_tier_branch():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("silver", 1000, "grocery", False)


def test_valid_card_tier_branch():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_invalid_amount_branch():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("gold", 0, "grocery", False)


def test_positive_amount_branch():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_fuel_category_branch():
    assert reward_points("platinum", 1000, "fuel", False) == 0


def test_non_fuel_category_branch():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_dining_category_true_branch():
    assert reward_points("classic", 1000, "dining", False) == 20


def test_travel_category_true_branch():
    assert reward_points("classic", 1000, "travel", False) == 20


def test_other_category_false_branch():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_weekend_bonus_true_branch():
    assert reward_points("gold", 1000, "grocery", True) == 70


def test_weekend_false_branch():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_classic_weekend_bonus_false_branch():
    assert reward_points("classic", 1000, "grocery", True) == 10


def test_days_late_nonpositive_branch():
    assert late_payment_fee(5000, 0) == 0


def test_outstanding_nonpositive_branch():
    assert late_payment_fee(0, 5) == 0


def test_positive_days_and_outstanding_branch():
    assert late_payment_fee(500, 5) == 100


def test_outstanding_at_or_below_1000_branch():
    assert late_payment_fee(1000, 5) == 100


def test_outstanding_between_1001_and_10000_branch():
    assert late_payment_fee(5000, 5) == 500


def test_outstanding_above_10000_branch():
    assert late_payment_fee(15000, 5) == 1000


def test_more_than_30_days_branch():
    assert late_payment_fee(5000, 31) == 1250


def test_30_days_or_less_branch():
    assert late_payment_fee(5000, 30) == 500


def test_frozen_card_branch():
    assert card_status(95, 4, True) == "frozen"


def test_not_frozen_branch_then_blocked():
    assert card_status(20, 3, False) == "blocked"


def test_missed_payments_below_three_branch():
    assert card_status(91, 0, False) == "over limit risk"


def test_utilisation_above_90_branch():
    assert card_status(91, 0, False) == "over limit risk"


def test_utilisation_at_or_below_90_branch():
    assert card_status(30, 0, False) == "good"


def test_watch_due_to_utilisation_branch():
    assert card_status(50, 0, False) == "watch"


def test_watch_due_to_missed_payment_branch():
    assert card_status(20, 1, False) == "watch"


def test_good_status_else_branch():
    assert card_status(30, 0, False) == "good"
