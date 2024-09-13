from dataclasses import dataclass
from PIL import Image, ImageFont

weather_template = Image.open("src/images/weather.jpg")
temperature_font = ImageFont.truetype("src/fonts/impact.ttf", 300)
text_font = ImageFont.truetype("src/fonts/fira_sans.ttf", 60)

@dataclass
class WeatherData:
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    weather_description: str
    precipitation: float
    wind_speed: float
    wind_direction: int
