import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get("https://parsinger.ru/selenium/5.5/5/1.html")

    span_elements = browser.find_elements(By.TAG_NAME, "span")
    for span in span_elements:
        div = span.find_element(By.XPATH, "./..")
        selector = div.find_element(By.TAG_NAME, "select")
        selector.send_keys(span.text)
        colors = div.find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "button")
        for color in colors:
            if color.get_attribute("data-hex") == span.text:
                color.click()
                break
        checkbox = div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox.click()

        text_field = div.find_element(By.CSS_SELECTOR, "input[type='text']")
        text_field.send_keys(span.text)

        button_check = div.find_element(By.XPATH, "//*[text()='Проверить']")
        button_check.click()

    browser.find_element(By.XPATH, "//*[text()='Проверить все элементы']").click()

    alert = browser.switch_to.alert

    print(alert.text)