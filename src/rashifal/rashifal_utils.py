import aiohttp
from bs4 import BeautifulSoup
from src.rashifal.rashifal_variables import rashifal_map, Rashifal, font
from PIL import Image, ImageDraw
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=3600)


def add_newline(string: str, number_of_words: int = 5) -> str:
    new_string = ""
    words = string.split(" ")
    word_count = 0
    for word in words:
        new_string += f"{word} "
        word_count += 1
        if word_count == number_of_words:
            new_string += "\n"
            word_count = 0
    return new_string


def draw_text(image: Image, x, y, content: str):
    draw = ImageDraw.Draw(image)
    draw.text(
        (x, y),
        add_newline(content, 7),
        (0, 0, 0),
        font,
        anchor="mm",
        align="center",
    )


async def get_rashifal(
    url: str = "https://www.hamropatro.com/rashifal",
) -> Rashifal | None:
    print("Getting rashifal!")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.text()
                soup = BeautifulSoup(data, "html.parser")
                items = soup.find_all("div", {"class": "item"})
                rashifal = []
                for item in items:
                    if item == items[-1]:
                        rashifal.append(
                            "।".join(
                                "".join(item.text.split(")")[1:])
                                .strip()
                                .split("।")[0:3]
                            )
                        )
                    else:
                        rashifal.append("".join(item.text.split(")")[1:]).strip())
                rashi_dict = {}
                for i, rashi in enumerate(rashifal_map.values()):
                    rashi_dict[rashi.lower()] = rashifal[i]

                items = soup.find_all("div", {"class": "column7"})
                date = " ".join(
                    " ".join(items[0].text.split("-"))[4:].strip().split(" ")[0:4][::-1]
                )
                rashi_dict["date"] = date

                rashifal_obj = Rashifal(**rashi_dict)
                cache[url] = rashifal_obj
                return rashifal_obj

    return None