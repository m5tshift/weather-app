from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

from config import DEFAULT_CITY
from utils import get_weather

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/temperature")
async def temperature(city: str = DEFAULT_CITY):
    try:
        return await get_weather(city)
    except Exception:
        return JSONResponse(
            content={"error": "Failed to fetch weather data"},
            status_code=502,
        )

app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static",
)
