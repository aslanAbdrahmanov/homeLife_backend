from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["Homepage"])

@router.get("/")
async def get_homepage():
    return {
        "banners": [{"id": 1, "title": "Акция"}],
        "products": [{"id": 10, "name": "Товар"}]
    }