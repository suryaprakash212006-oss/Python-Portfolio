from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)
driver.refresh()
print("Page refreshed")
