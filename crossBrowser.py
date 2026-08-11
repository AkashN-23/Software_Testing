import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def run_login_test(driver, browser_name):
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    finally:
        driver.quit()

firefox_Service = FirefoxService(GeckoDriverManager().install())
firefoxdriver = webdriver.Firefox(service = firefox_Service)

run_login_test(firefoxdriver, "Firefox")

chrome_service = ChromeService(ChromeDriverManager(chrome_type = ChromeType.CHROMIUM).install())
chrome_driver = webdriver.Chrome(service = chrome_service)

run_login_test(chrome_driver, "Chromium")