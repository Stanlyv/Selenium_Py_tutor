import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/3/index.html")

    result = 0

    cookies = browser.get_cookies()
    for cookie in cookies:
        name = cookie["name"].split("_")
        if int(name[2]) % 2 == 0:
            result += int(cookie["value"])

    print(result)


