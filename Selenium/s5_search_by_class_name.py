from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC     #SEARCH BY CLASS NAME

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"navbar-brand")))
driver.find_element(By.CLASS_NAME,"nav-item").click()
print("Navigated to:", driver.title)
driver.quit()
