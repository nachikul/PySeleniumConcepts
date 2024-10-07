from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open a page with JavaScript alert
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the button to trigger an alert
alert_button = driver.find_element("xpath", "//button[text()='Click for JS Alert']")
alert_button.click()

# Switch to alert and accept it
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()

time.sleep(2)
driver.quit()