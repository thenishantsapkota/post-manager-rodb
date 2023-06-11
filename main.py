import os
import aiocron
import asyncio
from src.rashifal.rashifal_utils import get_rashifal
from src.rashifal.rashifal_variables import (
    template_one,
    template_two,
    template_three,
    template_four,
)
from src.rashifal.rashifal import generate_template
from src.gold.gold import generate_gold_prices
from src.facebook_post import post_images
from dotenv import load_dotenv
from src.utils import convert_to_bytes
from fastapi import FastAPI


load_dotenv()

FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "world"}


@aiocron.crontab("15 2 * * *")
async def post_rashifal():
    images = [
        await generate_template(image)
        for image in [template_one, template_two, template_three, template_four]
    ]
    rashifal = await get_rashifal()

    data = await post_images(
        FACEBOOK_PAGE_ID, f"{rashifal.date} को ताजा राशिफल ।", images
    )
    print(data)


@aiocron.crontab("15 0 * * *")
async def post_pathibhara():
    images = [convert_to_bytes("src/images/pathibhara.png")]
    data = await post_images(FACEBOOK_PAGE_ID, "श्री पाथिभरा माताकी जय । <3", images)

    print(data)


@aiocron.crontab("15 6 * * *")
async def post_gold_prices():
    images = [await generate_gold_prices()]
    data = await post_images(
        FACEBOOK_PAGE_ID,
        "आजको सुन, चाँदीको दर\n#vianet #goldprices #expensive #rodb",
        images,
    )
    print(data)


async def start_jobs():
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(post_rashifal()),
        loop.create_task(post_pathibhara()),
        loop.create_task(post_gold_prices()),
    ]
    await asyncio.gather(*tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(start_jobs())
    loop.run_forever()


if __name__ == "__main__":
    main()
