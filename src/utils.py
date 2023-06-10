import io
from PIL import Image


def convert_to_bytes(image_path: str) -> bytes:
    buf = io.BytesIO()
    image = Image.open(image_path)
    image.save(buf, format="PNG")
    return buf.getvalue()
