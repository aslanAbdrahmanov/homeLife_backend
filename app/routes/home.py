from typing import List

from fastapi import APIRouter

from app.models import Banner, Category, Product
from app.services import (
    fetch_banners,
    fetch_categories,
    fetch_deal_of_the_day,
    fetch_new_products,
)

router = APIRouter()


@router.get("/")
def healthcheck() -> dict[str, str]:
    """Return a simple response to confirm the backend is running."""

    return {"message": "Tech Store backend is running"}


@router.get("/api/categories", response_model=List[Category])
def get_categories() -> List[Category]:
    """Return the homepage menu categories."""

    return fetch_categories()


@router.get("/api/banners", response_model=List[Banner])
def get_banners() -> List[Banner]:
    """Return hero banner data."""

    return fetch_banners()


@router.get("/api/products/deal-of-the-day", response_model=Product)
def get_deal_of_the_day() -> Product:
    """Return the deal of the day product."""

    return fetch_deal_of_the_day()


@router.get("/api/products/new", response_model=List[Product])
def get_new_products() -> List[Product]:
    """Return a list of new products."""

    return fetch_new_products()
