from selenium import webdriver

try:
    # This automatically downloads/finds ChromeDriver
    driver = webdriver.Chrome()

    # Open a website
    driver.get("https://www.google.com")

    # Print page title
    print("Page title is:", driver.title)

    # Close browser
    driver.quit()
    print("Selenium and Chrome are working correctly!")

except Exception as e:
    print("Error:", e)
    print("Check your Selenium installation or Chrome browser version.")
