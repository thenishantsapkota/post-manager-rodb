import asyncio
import os
from src.facebook_post import post_images
from src.utils import convert_to_bytes

FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")

async def post_pathibhara():
    images = [convert_to_bytes("src/images/pathibhara.png")]
    data = await post_images(FACEBOOK_PAGE_ID, "श्री पाथिभरा माताकी जय । <3", images)

    print(data)


asyncio.run(post_pathibhara())