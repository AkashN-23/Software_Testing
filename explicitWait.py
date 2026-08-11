from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

try:
    print("Opening a website with slow loading")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_button.click()

    wait = WebDriverWait(driver, 10)

    print("Waiting smartly for loading hidden text")
    hidden_text_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print(f"The hidden text says: {hidden_text_element.text}")

finally :
    driver.quit()