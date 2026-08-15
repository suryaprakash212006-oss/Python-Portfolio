from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/s?k=iphone")
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
time.sleep(3)
selectors = [
    "//span[@class='a-size-medium a-color-base a-text-normal']",
    "//span[@class='a-size-base-plus a-color-base a-text-normal']",
    "//h2/a/span",
    "//span[contains(text(),'iPhone')]"
]
found_any = False
for sel in selectors:
    titles = driver.find_elements(By.XPATH, sel)
    print(f"\n Selector: {sel}")
    print(f"   Found {len(titles)} items")
    if titles:
        found_any = True
        for i, t in enumerate(titles[:10], 1):
            print(f"   {i}. {t.text.strip()}")
        break
if not found_any:
    print("\n Still no titles found — Amazon page layout changed or blocked automation.")
time.sleep(3)
driver.quit()
