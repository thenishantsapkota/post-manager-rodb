import aiohttp
from datetime import date, timedelta
from src.gold.gold_variables import GoldPrice, font
from PIL import Image, ImageDraw

BASE_URL = "https://api.nepalipatro.com.np/v3/bullions?from-date=2023-6-08"


async def get_gold_prices(url: str = BASE_URL) -> GoldPrice:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            response: dict = await resp.json()
            data: dict = response.get("data")

        prices = data.get(str(date.today()))
        if not prices:
            prices = data[list(data)[-1]]

        return GoldPrice(**prices)


def draw_text(image: Image, x, y, content: str):
    draw = ImageDraw.Draw(image)
    draw.text((x, y), content, (0, 0, 0), font)
