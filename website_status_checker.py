import requests


def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up and running.")
        else:
            print(f"Website {url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing website {url}: {e}")


# 使用示例
check_website_status("https://example.com")
