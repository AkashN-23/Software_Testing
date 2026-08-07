import time
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# step 1: setup firefox browser
# GeckoDriverManager automattically downloads and manages the GeckoDriver for your firefox version
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# step 2: Open the website
website_url = "https://www.google.com"
print(f"Opening {website_url} in firefox")
driver.get(website_url)

# step 3: Maximize the window
driver.maximize_window()

# Passing for 3sec to see what is happening
time.sleep(3)

# Closing the browser
print("Closing the browser")
driver.quit()

