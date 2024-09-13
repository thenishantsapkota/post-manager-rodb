import io

from src.weather.weather_utils import fetch_weather, draw_text
from src.weather.weather_variables import weather_template, temperature_font, text_font
from nepali_datetime import datetime


async def generate_weather_template():
    weather = await fetch_weather()
    buf = io.BytesIO()

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        850,
        f"{weather.temperature}",
        temperature_font,
    )

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        1050,
        weather.weather_description,
        text_font,
    )

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        1250,
        f"Feels Like: {weather.feels_like} °C",
        text_font,
    )

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        1350,
        f"Humidity: {weather.humidity}%",
        text_font,
    )

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        1450,
        f"Wind Speed: {weather.wind_speed} km/h",
        text_font,
    )

    draw_text(
        weather_template,
        weather_template.size[0] / 4 + 80,
        1900,
        datetime.now().strftime("%Y %B %d"),
        text_font,
        (255, 255, 255),
    )
    weather_template.save(buf, format="PNG")
    return buf.getvalue()
