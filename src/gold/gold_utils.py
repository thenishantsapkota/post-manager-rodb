import aiohttp
from datetime import date, timedelta
from src.gold.gold_variables import GoldPrice, font
from PIL import Image, ImageDraw

# Get yesterday's date
yesterday = date.today() - timedelta(days=30)

BASE_URL = f"https://api.nepalipatro.com.np/v3/bullions?from-date={yesterday.strftime('%Y-%m-%d')}"


async def get_gold_prices(url: str = BASE_URL) -> GoldPrice:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.json()
            data = response.get("data", {})

        today_str = str(date.today())
        prices = data.get(today_str, {})

        if not (prices.get('t_ha') and prices.get('t_te') and prices.get('t_s')):
            index = 0
            dates = list(data.keys())
            
            while index < len(dates):
                previous_date = dates[index]
                prices = data.get(previous_date, {})

                if all(prices.get(key) != 0 for key in ['t_ha', 't_te', 't_s']):
                    break
                index += 1

                if index >= len(dates):
                    # Handle case where no valid data is found
                    raise ValueError("No valid gold prices found in the available data.")

        s = GoldPrice(**prices)
        print(s.t_ha, s.t_te, s.t_s)
        return s

def draw_text(image: Image, x, y, content: str):
    draw = ImageDraw.Draw(image)
    draw.text((x, y), content, (0, 0, 0), font)
