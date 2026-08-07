import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    print("Opening the Browser")
    driver.get("https://www.google.com")
    time.sleep(2)

    print("Navigating to WikiPedia")
    driver.get("https://www.wikipedia.com")
    time.sleep(2)

    print("Refreshing the Page")
    driver.refresh()
    time.sleep(2)

finally:
    print("Closing the Browser")
    driver.quit()
