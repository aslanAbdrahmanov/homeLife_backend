from fastapi import FastAPI
from app.homepage.router import router as home_router

app = FastAPI()

# Подключаем роутер из твоей папки
app.include_router(home_router)

@app.get("/")
async def root():
    return {"message": "Бэкенд HomeLife запущен и работает!"}