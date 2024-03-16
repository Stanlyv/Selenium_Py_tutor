import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/7/7.html")

    result = 0

    options = driver.find_elements(By.TAG_NAME, "option")
    for option in options:

        result += int(option.text)

    text_box = driver.find_element(By.ID, "input_result").send_keys(result)

    button = driver.find_element(By.CLASS_NAME, "btn").click()

    result = driver.find_element(By.ID, "result")

    print(result.text)


