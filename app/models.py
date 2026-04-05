from pydantic import BaseModel, Field


class Category(BaseModel):
    """Menu category shown on the homepage."""

    id: int = Field(..., description="Category identifier")
    name: str = Field(..., description="Category display name")


class Banner(BaseModel):
    """Hero banner item displayed on the homepage."""

    id: int = Field(..., description="Banner identifier")
    image_url: str = Field(..., description="Banner image URL")
    title: str = Field(..., description="Banner title")
    alt_text: str = Field(..., description="Alternative text for the image")


class Product(BaseModel):
    """Product card shown in homepage sections."""

    id: int = Field(..., description="Product identifier")
    name: str = Field(..., description="Product name")
    price: int = Field(..., description="Product price")
    currency: str = Field(..., description="Product currency")
    rating: int = Field(..., ge=0, le=5, description="Product rating")
    image_url: str = Field(..., description="Product image URL")

