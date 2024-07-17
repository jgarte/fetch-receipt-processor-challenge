import pytest

from .receipt_rules import (
    calculate_points,
    generate_receipt_id,
    is_round_dollar_amount,
    is_multiple_of_quarter,
    trimmed_length_is_multiple_of_three,
    purchase_date_is_odd,
    is_between_two_and_four,
    points_for_alphanumeric_in_name,
    points_for_round_dollar_with_no_cents,
    points_for_every_two_items_on_receipt,
    six_points_if_the_day_in_the_purchase_date_is_odd,
    ten_points_if_the_time_of_purchase_is_between_two_and_four,
    points_for_trimmed_length_of_item,
    points_if_total_is_a_multiple_of_quarter,
)

from .models import Item, Receipt


def test_generate_receipt_id() -> None:
    assert isinstance(generate_receipt_id(), str)
    assert len(generate_receipt_id()) == 36


def test_is_round_dollar_amount() -> None:
    assert is_round_dollar_amount("2.00") is True
    assert is_round_dollar_amount("1.35") is False


def test_is_multiple_of_quarter() -> None:
    assert is_multiple_of_quarter("2.75") is True
    assert is_multiple_of_quarter("1.35") is False


def test_trimmed_length_is_multiple_of_three() -> None:
    assert trimmed_length_is_multiple_of_three("Pepsi - 12-oz") is False
    assert trimmed_length_is_multiple_of_three("Dasani") is True


def test_purchase_date_is_odd() -> None:
    assert purchase_date_is_odd("2024-01-28") is False
    assert purchase_date_is_odd("2024-01-29") is True


def test_is_between_two_and_four() -> None:
    assert is_between_two_and_four("1:50") is False
    assert is_between_two_and_four("15:30") is True


def test_points_for_alphanumeric_in_name() -> None:
    assert points_for_alphanumeric_in_name("Target") is 6


def test_points_for_every_two_items_on_receipt(target_items: list[Item]) -> None:
    assert points_for_every_two_items_on_receipt(target_items) == 10


def test_points_for_round_dollar_with_no_cents() -> None:
    assert points_for_round_dollar_with_no_cents("35.30") == 0
    assert points_for_round_dollar_with_no_cents("9.00") == 50


def test_points_if_total_is_a_multiple_of_quarter() -> None:
    assert points_if_total_is_a_multiple_of_quarter("35.30") == 0
    assert points_if_total_is_a_multiple_of_quarter("9.00") == 25


def test_six_points_if_the_day_in_the_purchase_date_is_odd() -> None:
    assert six_points_if_the_day_in_the_purchase_date_is_odd("2022-01-01") == 6
    assert six_points_if_the_day_in_the_purchase_date_is_odd("2022-01-02") == 0


def test_ten_points_if_the_time_of_purchase_is_between_two_and_four() -> None:
    assert ten_points_if_the_time_of_purchase_is_between_two_and_four("13:01") == 0
    assert ten_points_if_the_time_of_purchase_is_between_two_and_four("14:30") == 10


def test_points_for_trimmed_length_of_item(target_items: list[Item]) -> None:
    item = target_items[1]
    assert points_for_trimmed_length_of_item(item) == 3


def test_calculate_points(target_receipt: Receipt) -> None:
    assert calculate_points(target_receipt) == 28

def test_calculate_points(corner_market_receipt: Receipt) -> None:
    assert calculate_points(corner_market_receipt) == 109
