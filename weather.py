import asyncio
import os
from src.facebook_post import post_images
from src.weather.weather import generate_weather_template
from nepali_datetime import datetime

FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")

async def post_weather():
    images = [await generate_weather_template()]
    nepali_time = datetime.now().strftime("%I:%M")
    devnagari_time = nepali_time.translate(str.maketrans("0123456789", "०१२३४५६७८९"))

    
    data = await post_images(
        FACEBOOK_PAGE_ID,
        f"मौसम अपडेट - {devnagari_time} बजे \n#vianet #weather #nepal",
        images,
    )

    print(data)

asyncio.run(post_weather())
