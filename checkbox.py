import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

try:
    print("--Checkbox--")
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(2)

    checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")

    if not checkbox1.is_selected():
        print("CheckBox1 is no selected, checking it!")
        checkbox1.click()
    
    if checkbox2.is_selected():
        print("CheckBox2 is already selected, Unchecking it!")
        checkbox2.click()

    time.sleep(2)

    """
    # Select Both
    if not checkbox1.is_selected():
        checkbox1.click()
    
    if not checkbox2.is_selected():
        checkbox2.click()

    # Uncheck Both
    if checkbox1.is_selected():
        checkbox1.click()
    
    if checkbox2.is_selected():
        checkbox2.click()
    """
    
finally:
    print("Closing the Browser")
    driver.quit()
