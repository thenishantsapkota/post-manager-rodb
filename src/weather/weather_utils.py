import aiohttp
import os


from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
from src.weather.weather_variables import WeatherData

load_dotenv()


async def fetch_weather(city="Damak", country="NP") -> WeatherData | None:
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    full_url = f"{base_url}?q={city},{country}&appid={api_key}&units=metric"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(full_url) as response:
                if response.status == 200:
                    weather_data = await response.json()
                    main = weather_data["main"]
                    weather = weather_data["weather"][0]
                    wind = weather_data["wind"]
                    rain = weather_data.get("rain", {}).get("1h", 0.0)

                    weather_info = WeatherData(
                        city=city,
                        country=country,
                        temperature=round(main["temp"]),
                        feels_like=round(main["feels_like"]),
                        humidity=main["humidity"],
                        weather_description=weather["description"].capitalize(),
                        precipitation=rain,
                        wind_speed=wind["speed"],
                        wind_direction=wind.get("deg", 0),
                    )
                    return weather_info
                else:
                    print(f"Error fetching data. HTTP Status code: {response.status}")
                    return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def draw_text(image: Image, x: int, y: int, content: str, font: ImageFont, color=(51, 187, 0)):
    draw = ImageDraw.Draw(image)
    draw.text((x, y), content, color, font, anchor="mm", align="center")