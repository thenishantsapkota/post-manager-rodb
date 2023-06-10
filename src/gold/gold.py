import io
from src.gold.gold_utils import draw_text, get_gold_prices
from src.gold.gold_variables import gold_price


async def generate_gold_prices():
    prices = await get_gold_prices()
    buf = io.BytesIO()

    draw_text(gold_price, 250, 1120, f"रू {prices.t_ha}")
    draw_text(gold_price, 1550, 1120, f"रू {prices.t_te}")
    draw_text(gold_price, gold_price.size[0] / 2 - 60, 1850, f"रू {prices.t_s}")

    gold_price.save(buf, format="PNG")
    return buf.getvalue()
