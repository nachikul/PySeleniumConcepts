from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open a webpage
    driver.get("https://www.wikipedia.org/")
    print("Opened Wikipedia homepage.")

    # Pause to see the browser
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "js-link-box-en")))
    print("Page loaded, waiting for the English language link...")

    # Click on the English language link
    english_link = driver.find_element(By.ID, "js-link-box-en")
    english_link.click()
    print("Clicked on the English language link.")

    # Pause to see the new page
    WebDriverWait(driver, 10).until(EC.title_contains("Wikipedia"))
    print("Navigated to the English Wikipedia page.")

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