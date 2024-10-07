from selenium import webdriver
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.wikipedia.org/")

# Pause to see the browser
time.sleep(2)

# Click on the English language link
english_link = driver.find_element("id", "js-link-box-en")
english_link.click()

# Pause to see the new page
time.sleep(2)

# Close the browser
driver.quit()