import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/4/4.html")

    checkboxes = driver.find_elements(By.CLASS_NAME, "check")
    for checkbox in checkboxes:
        checkbox.click()

    button = driver.find_element(By.CLASS_NAME, "btn").click()
    result = driver.find_element(By.ID, "result")

    print(result.text)


