import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/2/1.html")

    fields = browser.find_elements(By.CLASS_NAME, "text-field")
    for field in fields:
        if field.is_enabled():
            field.clear()

    button = browser.find_element(By.ID, "checkButton").click()

    alert = browser.switch_to.alert

    print(alert.text)


