import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

try:
    print("Opening Broken Image")
    driver.get("https://the-internet.herokuapp.com/broken_images")
    images = driver.find_elements(By.TAG_NAME, "img")
    
    print({f"Total images in the webpage is {len(images)}"})

    for image in images :
        image_url = image.get_attribute("src")
        if image_url :
            response = requests.get(image_url)

            if response.status_code == 200 :
                print(f"Good image {image_url}")
            else :
                print(f"Broken Image {image_url}")

finally:
    print("Closing the Browser")
    driver.quit()