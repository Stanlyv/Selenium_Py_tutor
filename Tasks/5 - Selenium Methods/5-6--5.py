import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/5/index.html")
    list_of_links = []
    cookie_date = 0
    link_result = ""

    links = browser.find_elements(By.TAG_NAME, "a")
    for link in links:
        list_of_links.append(link.get_attribute("href"))

    for i in list_of_links:
        browser.get(i)
        cookies = browser.get_cookies()
        for cookie in cookies:
            if cookie["expiry"] > cookie_date:
                cookie_date = cookie["expiry"]
                link_result = i

    browser.get(link_result)

    result = browser.find_element(By.ID, "result")

    print(result.text)



