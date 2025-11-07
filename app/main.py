# Точка входа приложения


from fastapi import FastAPI
from app.routers import subscribes

app = FastAPI(
    title="Clothes Shop FastAPI",
    version="0.1.0",
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
