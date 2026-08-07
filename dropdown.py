import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

try:
    print("--Dropdwon--")
    driver.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(2)

    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    print("Selecting text from the text that is visible in the webpage")
    dropdown.select_by_visible_text("Option 1")
    time.sleep(2)

    print("Selecting by value")
    dropdown.select_by_value("2")
    time.sleep(2)

    print("Select by index")
    dropdown.select_by_index(1)
    time.sleep(2)

finally:
    print("Closing the browser")
    driver.quit()