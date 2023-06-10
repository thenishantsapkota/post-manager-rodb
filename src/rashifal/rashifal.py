import io
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
            draw_text(image, template_one.size[0] / 2.5, 800, rashifal.aries)
            draw_text(image, template_one.size[0] / 2.5, 1500, rashifal.taurus)
            draw_text(image, template_one.size[0] / 2.5, 2250, rashifal.gemini)

        elif image == template_two:
            draw_text(image, template_one.size[0] / 2.5, 800, rashifal.cancer)
            draw_text(image, template_one.size[0] / 2.5, 1500, rashifal.leo)
            draw_text(image, template_one.size[0] / 2.5, 2250, rashifal.virgo)

        elif image == template_three:
            draw_text(image, template_one.size[0] / 2.5, 800, rashifal.libra)
            draw_text(image, template_one.size[0] / 2.5, 1500, rashifal.scorpio)
            draw_text(image, template_one.size[0] / 2.5, 2250, rashifal.sagittarius)

        elif image == template_four:
            draw_text(image, template_one.size[0] / 2.5, 800, rashifal.capricorn)
            draw_text(image, template_one.size[0] / 2.5, 1500, rashifal.aquarius)
            draw_text(image, template_one.size[0] / 2.5, 2250, rashifal.pisces)

        image.save(buf, format="PNG")
        return buf.getvalue()
