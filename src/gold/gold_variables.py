from PIL import ImageFont, Image

gold_price = Image.open("src/images/gold.png")
font = ImageFont.truetype("src/fonts/hind_semibold.ttf", 63)


class GoldPrice:
    def __init__(
        self,
        bs: str,
        t_ha: int,
        t_te: int,
        t_s: int,
        *args,
        **kwargs,
    ) -> None:
        self.bs = bs
        self.t_ha = t_ha
        self.t_te = t_te
        self.t_s = t_s
