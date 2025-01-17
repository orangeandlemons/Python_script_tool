import pytesseract
from PIL import Image


def recognize_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(
        image,
    )
    # 使用简体中文
    return text


# 使用示例
text = recognize_text("/path/to/image.jpg")
print(text)
