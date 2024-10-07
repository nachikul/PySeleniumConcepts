from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")

# Locate the search bar using ID
search_bar = driver.find_element("id", "twotabsearchtextbox")
search_bar.send_keys("Selenium Books")

# Locate and click the search button using Xpath
search_button = driver.find_element("xpath", "//input[@value='Go']")
search_button.click()

time.sleep(2)

driver.quit()