import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/6/6.html")

    result = 0

    tip_one = driver.find_element(By.ID, "text_box")
    tip_one_result = eval(tip_one.text)

    selector = driver.find_element(By.ID, "selectId").send_keys(tip_one_result+1)

    button = driver.find_element(By.CLASS_NAME, "btn").click()

    result = driver.find_element(By.ID, "result")

    print(result.text)


