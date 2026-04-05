from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.home import router as home_router


app = FastAPI(
    title="Tech Store Homepage API",
    description="Mock API for the homepage of a home appliances online store.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home_router)
