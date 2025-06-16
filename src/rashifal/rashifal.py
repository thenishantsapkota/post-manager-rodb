import io
import random
from src.rashifal.rashifal_variables import (
    template_one,
    template_two,
    template_three,
    template_four,
)
from src.rashifal.rashifal_utils import get_rashifal, draw_text
from PIL import Image


async def generate_template(image: Image) -> bytes | None:
    rashifal = await get_rashifal()
    print("Generating Template!")
    buf = io.BytesIO()
    if rashifal:
        if image == template_one:
            draw_text(image, template_one.size[0] / 1.6, 1400, rashifal.aries)
            draw_text(image, template_one.size[0] / 1.6, 2500, rashifal.taurus)
            draw_text(image, template_one.size[0] / 1.6, 3650, rashifal.gemini)

        elif image == template_two:
            draw_text(image, template_one.size[0] / 1.6, 1400, rashifal.cancer)
            draw_text(image, template_one.size[0] / 1.6, 2500, rashifal.leo)
            draw_text(image, template_one.size[0] / 1.6, 3650, rashifal.virgo)

        elif image == template_three:
            draw_text(image, template_one.size[0] / 1.6, 1400, rashifal.libra)
            draw_text(image, template_one.size[0] / 1.6, 2500, rashifal.scorpio)
            draw_text(image, template_one.size[0] / 1.6, 3650, rashifal.sagittarius)

        elif image == template_four:
            draw_text(image, template_one.size[0] / 1.6, 1400, rashifal.capricorn)
            draw_text(image, template_one.size[0] / 1.6, 2500, rashifal.aquarius)
            draw_text(image, template_one.size[0] / 1.6, 3650, rashifal.pisces)

        image.save(buf, format="PNG")
        return buf.getvalue()
