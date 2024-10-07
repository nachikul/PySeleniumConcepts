from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open a page with JavaScript alert
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    print("Opened the JavaScript Alerts page.")

    # Allow time for the page to load
    time.sleep(5)

    # Click the button to trigger an alert
    alert_button = driver.find_element("xpath", "//button[text()='Click for JS Alert']")
    alert_button.click()
    print("Clicked the button to trigger the JavaScript alert.")

    # Allow time for the alert to appear
    time.sleep(5)

    # Switch to alert and accept it
    alert = driver.switch_to.alert
    alert.accept()
    print("Accepted the JavaScript alert.")

    # Allow time to observe the action
    time.sleep(5)

except NoSuchElementException:
    print("Error: The specified element was not found on the page.")
except TimeoutException:
    print("Error: The operation timed out. The element was not found in the given time.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    # Close the browser
    driver.quit()
    print("Closed the browser.")