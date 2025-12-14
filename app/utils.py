import httpx
from config import WEATHER_API_KEY


class WeatherError(Exception):
    pass


async def get_weather(city: str) -> dict:
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=5.0)
            resp.raise_for_status()
            data = resp.json()

    except httpx.RequestError as e:
        raise WeatherError(f"HTTP request failed: {e}")
    except ValueError:
        raise WeatherError("Invalid JSON in response")

    if "error" in data:
        raise WeatherError(f"API returned error: {data['error']}")

    location = data.get("location", {})
    current = data.get("current", {})

    result = {
        "city": location.get("name"),
        "region": location.get("region"),
        "country": location.get("country"),
        "temperature_c": current.get("temp_c"),
        "feelslike_c": current.get("feelslike_c"),
    }
    return result
