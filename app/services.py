from typing import List

from app.mock_db import MOCK_DB
from app.models import Banner, Category, Product


def fetch_categories() -> List[Category]:
    """Return categories from the mock database."""

    return [Category(**item) for item in MOCK_DB["categories"]]


def fetch_banners() -> List[Banner]:
    """Return banners from the mock database."""

    return [Banner(**item) for item in MOCK_DB["banners"]]


def fetch_deal_of_the_day() -> Product:
    """Return the deal of the day from the mock database."""

    return Product(**MOCK_DB["deal_of_the_day"])


def fetch_new_products() -> List[Product]:
    """Return new products from the mock database."""

    return [Product(**item) for item in MOCK_DB["new_products"]]

