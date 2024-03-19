import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/3/1.html")

    result = 0

    divs = browser.find_elements(By.CLASS_NAME, "parent")

    for div in divs:
        if div.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            result += int(div.find_element(By.TAG_NAME, "textarea").text)

    print(result)


