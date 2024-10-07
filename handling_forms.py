from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Locate the search bar and input a query
search_bar = driver.find_element("name", "q")
search_bar.send_keys("Selenium Python")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()