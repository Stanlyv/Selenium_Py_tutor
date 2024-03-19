import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get("https://parsinger.ru/methods/3/index.html")

    result = 0
    cookies = browser.get_cookies()

    for cookie in cookies:
        print(f"cookie name = {cookie['name']}")
        print(f"cookie value = {cookie['value']}")
        result += int(cookie["value"])

    print(result)
