import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    print("Opening the Browser")
    website_url = "https://www.google.com"
    driver.get(website_url)
    time.sleep(2)

    driver.maximize_window()

    print("Navigating to WikiPedia")
    driver.get("https://www.wikipedia.com")
    time.sleep(2)

    print("Hitting back to go back to www.google.com")
    driver.back()
    time.sleep(2)

    print("Hitting forward to go back to wikipedia")
    driver.forward()
    time.sleep(2)

    print("Tab Switching")
    original_tab = driver.current_window_handle

    # Create to new tab
    driver.switch_to.new_window("tab")
    driver.get("https://www.python.org")
    time.sleep(2)

    # Switch tabs
    driver.switch_to.window(original_tab)
    time.sleep(3)

finally:
    print("Closing the browser")
    driver.quit()
