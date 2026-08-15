from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://www.amazon.in')                   #SELECTING LINKS
driver.maximize_window()
time.sleep(5)

select = driver.find_element(By.LINK_TEXT,'Electronics')
select.click()

time.sleep(5)
select1=driver.find_element(By.LINK_TEXT,'Audio')
select1.click()
