from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    print("Opened Google homepage.")

    # Allow time for the page to load and wait for the search bar to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
    print("Page loaded, waiting for the search bar...")

    # Locate the search bar and input a query
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("Selenium Python")
    print("Entered search query: 'Selenium Python'.")

    # Submit the search form
    search_bar.send_keys(Keys.RETURN)
    print("Submitted the search query.")

    time.sleep(5)
    # Allow time for search results to load
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium Python"))
    print("Search results loaded successfully.")
    time.sleep(5)

except TimeoutException:
    print("Error: The operation timed out. The element was not found in the given time.")
except NoSuchElementException:
    print("Error: The specified element was not found on the page.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    # Close the browser
    driver.quit()
    print("Closed the browser.")