import time
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By # We are importing By to locate elements on the webpage

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # step 1: Opening a website
    print("Opening Swag Labs")
    website_url = "https://www.saucedemo.com/"
    driver.get(website_url)
    driver.maximize_window()
    time.sleep(3)

    # step 2: Find the username and type the username
    print("Entering username")
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    # step 3: Find the Password field and type the password
    print("Entering password")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    time.sleep(3)

    # step 4: Finding the login button and Clicking it
    print("Clicking Login Button")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(3)

finally:
    print("Closing the browser")
    driver.quit()