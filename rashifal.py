import asyncio
import os
from src.facebook_post import post_images
from src.rashifal.rashifal import generate_template
from src.rashifal.rashifal_utils import get_rashifal
from src.rashifal.rashifal_variables import (
    template_one,
    template_two,
    template_three,
    template_four,
)

FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")

async def post_rashifal():
    images = [
        await generate_template(image)
        for image in [template_one, template_two, template_three, template_four]
    ]
    rashifal = await get_rashifal()

    data = await post_images(FACEBOOK_PAGE_ID, f"{rashifal.date} को ताजा राशिफल ।", images)
    print(data)

asyncio.run(post_rashifal())