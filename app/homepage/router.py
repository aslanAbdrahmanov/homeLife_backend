# Файл: app/homepage/router.py

from fastapi import APIRouter
from data.home_data import HOME_MOCK_DATA  # Достаем наши моки

# Создаем роутер
router = APIRouter(prefix="/api/home", tags=["Главная страница"])

@router.get("/")
async def get_homepage_data():
    # Когда кто-то делает GET запрос, возвращаем весь словарь
    return HOME_MOCK_DATA