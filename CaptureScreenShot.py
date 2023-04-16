from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
driver.save_screenshot("C:\\Users\hsaji\PycharmProjects\pythonProject\Selenium\download\homepage.png")
#driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()