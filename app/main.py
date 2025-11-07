# Точка входа приложения


from fastapi import FastAPI


app = FastAPI(
    title="Burger Joint FastAPI",
    version="0.1.0",
)


@app.get("/")
async def root():
    """
    Init root endpoint
    """
    return {
        "message": "Hello everyone!"
    }
