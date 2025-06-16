from dataclasses import dataclass
from PIL import Image, ImageFont

template_one = Image.open("src/images/rashifal_1.png")
template_two = Image.open("src/images/rashifal_2.png")
template_three = Image.open("src/images/rashifal_3.png")
template_four = Image.open("src/images/rashifal_4.png")

font = ImageFont.truetype("src/fonts/noto_sans.ttf", 110)


@dataclass
class Rashifal:
    aries: str
    taurus: str
    gemini: str
    cancer: str
    leo: str
    virgo: str
    libra: str
    scorpio: str
    sagittarius: str
    capricorn: str
    aquarius: str
    pisces: str
    date: str


rashifal_map = {
    "मेष": "Aries",
    "वृष": "Taurus",
    "मिथुन": "Gemini",
    "कर्कट": "Cancer",
    "सिंह": "Leo",
    "कन्या": "Virgo",
    "तुला": "Libra",
    "वृश्चिक": "Scorpio",
    "धनु": "Sagittarius",
    "मकर": "Capricorn",
    "कुम्भ": "Aquarius",
    "मीन": "Pisces",
}
