from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Open a slow-loading page
driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

# Click button to load new data
load_button = driver.find_element(By.ID, "save")
load_button.click()

# Wait for the element with new data to become visible
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='loading']/br"))
    )
    print("Data loaded successfully!")
finally:
    time.sleep(2)
    driver.quit()