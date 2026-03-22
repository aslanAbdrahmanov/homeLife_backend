# Файл: app/homepage/router.py
from fastapi import APIRouter
from data.home_data import HOME_DATA  # Импортируем нашу "базу данных"

router = APIRouter(prefix="/home", tags=["Homepage"])

@router.get("/")
async def get_homepage():
    # Просто возвращаем весь словарь с данными
    return HOME_DATA