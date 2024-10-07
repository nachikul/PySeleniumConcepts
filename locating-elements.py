from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Open Barnes & Noble website
    driver.get("https://www.barnesandnoble.com")
    print("Opened Barnes & Noble homepage.")

    # Allow time for page to load and wait for search bar to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "rbt-input-main")))
    print("Page loaded, waiting for the search bar...")

    # Locate the search bar using class name and input the query
    search_bar = driver.find_element(By.CLASS_NAME, "rbt-input-main")
    search_bar.send_keys("Dan Brown - Deception Point")
    print("Entered search query: 'Dan Brown - Deception Point'.")

    # Allow time for the input to register
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-outline-secondary rhf-search-btn']")))

    # Locate and click the search button using the provided XPath
    search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-outline-secondary rhf-search-btn']")
    search_button.click()
    print("Clicked on the search button.")

    # Allow time for search results to load
    WebDriverWait(driver, 10).until(EC.title_contains("Dan Brown - Deception Point"))
    print("Search results loaded successfully.")

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