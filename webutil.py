from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\vaibh\Downloads\selpython")
driver.get("https://www.google.com")
elem =driver.find_element(By.CLASS_NAME,"gLFyf")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
