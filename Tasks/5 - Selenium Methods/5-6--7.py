import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/scroll/4/index.html")

    result = 0
    buttons = browser.find_elements(By.CLASS_NAME, "btn")
    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        result += int(browser.find_element(By.ID, "result").text)

    print(result)


