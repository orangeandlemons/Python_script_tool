import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # 从网站提取相关数据的代码在此处
    return soup


# 使用示例
url = "https://example.com"
soup = scrape_data(url)
print(soup.title.string)
