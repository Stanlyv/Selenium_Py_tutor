from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/2/2.html")

    search_text = "16243162441624"

    link = driver.find_element(By.LINK_TEXT, search_text).click()

    result = driver.find_element(By.ID, "result")

    print(result.text)


