import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AmazonTVSearchTestFail(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_search_sony_55_inch_tv(self):
        driver = self.driver
        driver.get("https://www.amazon.in")

        # Wait for page to load
        time.sleep(2)

        # Login steps
        driver.find_element(By.ID, 'nav-link-accountList').click()
        time.sleep(2)
        driver.find_element(By.ID, 'ap_email').send_keys("test@gmail.com")
        driver.find_element(By.ID, 'continue').click()
        time.sleep(2)
        driver.find_element(By.ID, 'ap_password').send_keys("test")
        driver.find_element(By.ID, 'signInSubmit').click()
        time.sleep(5)

        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
        )
        # Search for 43 inch TV
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys("Sony 55 inch TV")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'search'))
        )
        # Check if "Sony 55 inch TV" appears in the results
        page_source = driver.page_source
        self.assertIn("Sony 55 inch TV", page_source, "Sony 55 inch TV not found in search results")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()