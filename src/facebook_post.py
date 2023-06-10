import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

FACEBOOK_AUTH_TOKEN = os.environ.get("FACEBOOK_AUTH_TOKEN")


async def post_image(group_id, image):
    print("Posting one image!")
    async with aiohttp.ClientSession(conn_timeout=None) as session:
        url = f"https://graph.facebook.com/{group_id}/photos?access_token={FACEBOOK_AUTH_TOKEN}"

        form = aiohttp.FormData()
        form.add_field("file", image)
        form.add_field("published", "false")
        async with session.post(url, data=form) as resp:
            r = await resp.json()

    return r


async def post_images(group_id, content, images: list):
    print("Final Step: Posting images with a caption!")
    img_ids = []
    for image in images:
        post_id = await post_image(group_id, image)
        img_ids.append(post_id["id"])

    args = dict()
    args["message"] = content
    for img_id in img_ids:
        key = "attached_media[" + str(img_ids.index(img_id)) + "]"
        args[key] = "{'media_fbid': '" + img_id + "'}"
    url = (
        f"https://graph.facebook.com/{group_id}/feed?access_token="
        + FACEBOOK_AUTH_TOKEN
    )
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=args) as response:
            data = await response.json()

    return data
