import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('../Chrome_Extensions/Mouse_coordinate/mouse_coordinates_0_2__0.crx')
# options_chrome.add_argument('--headless=chrome')
options_chrome.add_argument('--no-sandbox')
options_chrome.add_argument('user-data-dir=/Users/stanlyvm1/Library/Application Support/Google/Chrome')

with webdriver.Chrome(options=options_chrome) as browser:
    url = "https://google.com"
    browser.get(url)
    time.sleep(25)
