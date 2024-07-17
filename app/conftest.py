import pytest

from .models import Item, Receipt


@pytest.fixture
def target_items() -> list[Item]:
    return [
        Item(shortDescription="Mountain Dew 12PK", price="6.49"),
        Item(shortDescription="Emils Cheese Pizza", price="12.25"),
        Item(shortDescription="Knorr Creamy Chicken", price="1.26"),
        Item(shortDescription="Doritos Nacho Cheese", price="3.35"),
        Item(shortDescription="   Klarbrunn 12-PK 12 FL OZ  ", price="12.00"),
    ]


@pytest.fixture
def target_receipt(target_items: list[Item]) -> Receipt:
    return Receipt(
        retailer="Target",
        purchaseDate="2022-01-01",
        purchaseTime="13:01",
        items=target_items,
        total="35.35",
    )


@pytest.fixture
def corner_market_items() -> list[Item]:
    return [
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
    ]


@pytest.fixture
def corner_market_receipt(corner_market_items: list[Item]) -> Receipt:
    return Receipt(
        retailer="M&M Corner Market",
        purchaseDate="2022-03-20",
        purchaseTime="14:33",
        items=corner_market_items,
        total="9.00",
    )
