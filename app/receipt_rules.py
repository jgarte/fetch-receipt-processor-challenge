from datetime import datetime, time
import math
from typing import Optional
import uuid

from .models import Receipt, Item


def generate_receipt_id() -> str:
    unique_id = uuid.uuid4()
    return str(unique_id)


def is_round_dollar_amount(total: str) -> bool:
    """
    Returns:
        True if the total is a rounded dollar amount.
    """
    return total.endswith(".00")


def is_multiple_of_quarter(total: str) -> bool:
    """
    Returns:
        True if the total is a multiple of 0.25.
    """
    parsed_total = float(total)
    print(parsed_total)
    return parsed_total % 0.25 == 0


def trimmed_length_is_multiple_of_three(item_description: str) -> bool:
    """
    Rule:
        If the trimmed length of the item description is a multiple of 3,
        multiply the price by 0.2 and round up to the nearest integer.
    """
    trimmed_length = len(item_description.strip())
    return trimmed_length % 3 == 0


def purchase_date_is_odd(date: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Note:
        The date must be of the format 2024-01-29 or year-month-date.

    Returns:
        True if the purchase date is odd.
    """
    try:
        date_obj = datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError(f"Date string does not match format {date_format}")

    day_of_month = date_obj.day

    return day_of_month % 2 != 0


def is_between_two_and_four(purchase_time: str, time_format: str = "%H:%M") -> bool:
    """
    Returns:
        True if the time of purchase is after 2:00pm and before 4:00pm.
    """
    dt = datetime.strptime(purchase_time, time_format)
    start_time = time(14, 0)
    end_time = time(16, 0)
    current_time = dt.time()
    print(start_time, current_time, end_time)
    return start_time <= current_time <= end_time


def points_for_alphanumeric_in_name(retailer: str) -> int:
    alphanumeric_chars = "".join([char for char in retailer if char.isalnum()])
    return len(alphanumeric_chars)


def points_for_round_dollar_with_no_cents(total: str) -> int:
    if is_round_dollar_amount(total):
        return 50
    else:
        return 0


def points_if_total_is_a_multiple_of_quarter(total: str) -> int:
    if is_multiple_of_quarter(total):
        return 25
    else:
        return 0


def points_for_every_two_items_on_receipt(items: list[Item]) -> int:
    """
    Returns:
        5 points for every two items on a receipt.
    """
    return int(round(len(items) / 2) * 5)


def six_points_if_the_day_in_the_purchase_date_is_odd(purchase_date: str) -> int:
    """
    Returns:
        6 points if the day in the purchase date is odd.
    """
    if purchase_date_is_odd(purchase_date):
        return 6
    else:
        return 0


def ten_points_if_the_time_of_purchase_is_between_two_and_four(
    purchase_time: str,
) -> int:
    """
    Returns:
        10 points if the time of purchase is after 2:00pm and before 4:00pm.
    """
    if is_between_two_and_four(purchase_time):
        return 10
    else:
        return 0


def points_for_trimmed_length_of_item(item: Item) -> int:
    """
    Returns:
        If the trimmed length of the item description is a multiple of 3,
        multiply the price by 0.2 and round up to the nearest integer. The
        result is the number of points earned.
    """
    if trimmed_length_is_multiple_of_three(item.short_description):
        price_float = float(item.price)
        return int(math.ceil(price_float * 0.2))
    return 0


def calculate_points(receipt: Receipt) -> int:
    points = 0
    points += points_for_alphanumeric_in_name(receipt.retailer)
    points += points_for_round_dollar_with_no_cents(receipt.total)
    points += points_if_total_is_a_multiple_of_quarter(receipt.total)
    points += points_for_every_two_items_on_receipt(receipt.items)
    for item in receipt.items:
        points += points_for_trimmed_length_of_item(item)
    points += six_points_if_the_day_in_the_purchase_date_is_odd(receipt.purchase_date)
    points += ten_points_if_the_time_of_purchase_is_between_two_and_four(
        receipt.purchase_time
    )
    return points
