from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    #BACK AND FORWARD NAVIGATIONS
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h1")))
driver.get("https://www.selenium.dev/downloads/")  # navigate to Downloads page
time.sleep(3)
driver.back()    # go back to main page
time.sleep(3)
driver.forward() # go forward and downloads again
driver.quit()
