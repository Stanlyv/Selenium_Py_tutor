from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/1/1.html")

    firstname = driver.find_element(By.NAME, "first_name").send_keys("name")
    lastname = driver.find_element(By.NAME, "last_name").send_keys("lastname")
    patronymic = driver.find_element(By.NAME, "patronymic").send_keys("patronymic")
    age = driver.find_element(By.NAME, "age").send_keys("22")
    city = driver.find_element(By.NAME, "city").send_keys("Vancouver")
    email = driver.find_element(By.NAME, "email").send_keys("email@gmail.com")
    button = driver.find_element(By.ID, "btn").click()
    result = driver.find_element(By.ID, "result")

    print(result.text)


