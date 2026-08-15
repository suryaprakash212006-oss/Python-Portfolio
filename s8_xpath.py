from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    #FNDING ELEMENT BY XPATH
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
wait = WebDriverWait(driver, 30)
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("iphones")
search_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
search_button.click()
