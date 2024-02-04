import asyncio
import os
from src.facebook_post import post_images
from src.gold.gold import generate_gold_prices

FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")


async def post_gold_prices():
    images = [await generate_gold_prices()]
    data = await post_images(
        FACEBOOK_PAGE_ID,
        "आजको सुन, चाँदीको दर\n#vianet #goldprices #expensive #rodb",
        images,
    )
    print(data)


asyncio.run(post_gold_prices())
