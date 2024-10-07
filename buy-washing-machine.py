from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set path for the ChromeDriver
service = Service("chromedriver-mac-arm64")  # Replace with your ChromeDriver path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# 1. Open Amazon.com (Basic Navigation)
driver.get("https://www.amazon.com")

# Allow time for the page to load
time.sleep(2)

# 2. Locate and click the 'Sign in' button (Locating Elements)
signin_button = driver.find_element(By.ID, 'nav-link-accountList')
signin_button.click()

# Allow time for the login page to load
time.sleep(2)

# 3. Input Amazon credentials (Handling Forms & Input)
email_input = driver.find_element(By.ID, 'ap_email')
email_input.send_keys("your-email@example.com")  # Replace with your email
driver.find_element(By.ID, 'continue').click()

# Allow time for the next page to load
time.sleep(2)

password_input = driver.find_element(By.ID, 'ap_password')
password_input.send_keys("your-password")  # Replace with your password
driver.find_element(By.ID, 'signInSubmit').click()

# Wait for the home page to load after login
time.sleep(5)

# 4. Search for Televisions that are 43 inches or bigger
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys("43 inch TV")
search_box.send_keys(Keys.RETURN)

# Wait until the search results are visible (Explicit Waits)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'search'))
)

# 5. Handle a pop-up alert (if there is any) (Handling Alerts & Pop-ups)
try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.accept()
except:
    print("No alert found.")

# Pause to view search results
time.sleep(3)

# 6. Switch to an iframe if needed (Handling Frames)
# This is just an example of how you might switch to an iframe
# iframes = driver.find_elements(By.TAG_NAME, 'iframe')
# if iframes:
#     driver.switch_to.frame(iframes[0])

# Close the browser after search is complete
driver.quit()