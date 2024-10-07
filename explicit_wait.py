from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open a slow-loading page
    driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")
    print("Opened the Dynamic Data Loading Demo page.")

    # Allow time for the page to load
    time.sleep(5)

    # Click button to load new data
    load_button = driver.find_element(By.ID, "save")
    load_button.click()
    print("Clicked the button to load new data.")

    # Wait for the element with new data to become visible
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='loading']/br"))
        )
        print("Data loaded successfully!")
    except TimeoutException:
        print("Error: Data did not load within the timeout period.")
    except NoSuchElementException:
        print("Error: The expected element was not found after loading new data.")

    # Allow time to observe the loaded data
    time.sleep(5)

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
    print("Closed the browser.")