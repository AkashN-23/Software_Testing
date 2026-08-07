import request
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

