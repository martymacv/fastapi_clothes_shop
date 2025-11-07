# Точка входа приложения


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import subscribes


app = FastAPI(
    title="Clothes Shop FastAPI",
    version="0.1.0",
)

origins = [
    "*",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subscribes.router)


@app.get("/")
async def root():
    """
    Init root endpoint
    """
    return {
        "message": "Hello everyone!"
    }
