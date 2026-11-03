import pytest

from credit_card_rewards import card_status, late_payment_fee, reward_points


def test_classic_grocery_points():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_gold_tier_multiplier():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_platinum_tier_multiplier():
    assert reward_points("platinum", 1000, "grocery", False) == 40


def test_dining_category_double_points():
    assert reward_points("gold", 1000, "dining", False) == 40


def test_travel_category_double_points():
    assert reward_points("classic", 1000, "travel", False) == 20


def test_fuel_category_awards_zero_points():
    assert reward_points("platinum", 5000, "fuel", True) == 0


def test_weekend_bonus_for_gold_card():
    assert reward_points("gold", 1000, "grocery", True) == 70


def test_weekend_bonus_not_given_to_classic_card():
    assert reward_points("classic", 1000, "grocery", True) == 10


def test_unknown_card_tier_raises_value_error():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("silver", 1000, "grocery", False)


def test_zero_amount_raises_value_error():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", 0, "grocery", False)


def test_negative_amount_raises_value_error():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("classic", -100, "grocery", False)


def test_on_time_payment_has_no_late_fee():
    assert late_payment_fee(5000, 0) == 0


def test_nonpositive_outstanding_has_no_late_fee():
    assert late_payment_fee(0, 5) == 0


def test_small_outstanding_fee_tier():
    assert late_payment_fee(1000, 5) == 100


def test_medium_outstanding_fee_tier():
    assert late_payment_fee(5000, 5) == 500


def test_large_outstanding_fee_tier():
    assert late_payment_fee(15000, 5) == 1000


def test_fee_surcharge_after_30_days():
    assert late_payment_fee(5000, 31) == 1250


def test_no_surcharge_at_exactly_30_days():
    assert late_payment_fee(5000, 30) == 500


def test_frozen_card_status_has_highest_priority():
    assert card_status(95, 4, True) == "frozen"


def test_three_missed_payments_block_card():
    assert card_status(20, 3, False) == "blocked"


def test_utilisation_above_90_is_over_limit_risk():
    assert card_status(91, 0, False) == "over limit risk"


def test_utilisation_above_30_is_watch():
    assert card_status(50, 0, False) == "watch"


def test_missed_payment_causes_watch_status():
    assert card_status(20, 1, False) == "watch"


def test_low_utilisation_and_no_missed_payments_is_good():
    assert card_status(30, 0, False) == "good"
