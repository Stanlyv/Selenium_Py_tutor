from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/3/3.html")

    result = 0

    p_elements = driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    for p in p_elements:
        result += int(p.text)

    print(result)


