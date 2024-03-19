import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/1/index.html")

    while True:
        result = browser.find_elements(By.ID, "result")
        if "1" in result[0].text:
            break
        browser.refresh()

    print(result[0].text)


