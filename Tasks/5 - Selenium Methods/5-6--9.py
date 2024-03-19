import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get("https://parsinger.ru/selenium/5.5/4/1.html")

    divs = browser.find_elements(By.CLASS_NAME, "parent")

    for div in divs:
        gray = div.find_element(By.CSS_SELECTOR, "textarea[color = 'gray']")
        blue = div.find_element(By.CSS_SELECTOR, "textarea[color = 'blue']")
        blue.send_keys(gray.text)
        gray.clear()
        div.find_element(By.TAG_NAME, "button").click()

    browser.find_element(By.ID, "checkAll").click()
    result = browser.find_element(By.ID, "congrats")

    print(result.text)

