from PIL import Image


def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(output_path)


# 使用示例
resize_image("/path/to/input.jpg", "/path/to/output.jpg", 800, 600)
