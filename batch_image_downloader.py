import requests


def download_images(url, save_directory):
    """
    从指定的URL下载图片并保存到指定目录。

    Args:
        url (str): 包含图片URL的JSON数组的API URL。
        save_directory (str): 保存下载图片的目录路径。

    Returns:
        None

    Raises:
        无

    """
    response = requests.get(url)
    if response.status_code == 200:
        # 假设API返回一个图片URL的JSON数组
        images = response.json()
        for index, image_url in enumerate(images):
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(f"{save_directory}/image_{index}.jpg", "wb") as f:
                    f.write(image_response.content)
            else:
                print("Failed to retrieve image.")


# 使用示例
download_images("https://api.example.com/images", "/path/to/save")
