# Файл: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.homepage.router import router as homepage_router

app = FastAPI(title="HomeLife API")

# Настройка CORS (разрешаем фронтенду получать наши данные)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # В реальном проекте тут будет адрес фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутер главной страницы
app.include_router(homepage_router)

@app.get("/")
async def root():
    return {"message": "Бэкенд HomeLife запущен и работает! Перейди на /docs для просмотра API."}