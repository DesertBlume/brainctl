import os
from pyowm import OWM

def handle(location: str) -> str:
    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        return "❌ Weather API Key not found."

    try:
        owm = OWM(api_key)
        mgr = owm.weather_manager()
        obs = mgr.weather_at_place(location)
        weather = obs.weather
        status = weather.detailed_status
        temp = weather.temperature('celsius')['temp']
        return f"🌤️ {location.title()}: {status}, {temp:.1f}°C"
    except Exception as e:
        return f"❌ Could not fetch weather info: {e}"

