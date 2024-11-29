# tests/test_flight_booking.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = None

class TestFlightBooking:

    """
    Test class for handling the Issta website.
    """
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()


    def teardown_class(self):
        time.sleep(3)
        driver.quit()

    def test_handle_alert(self):
        """
        Test to handle JavaScript alert on the Issta website (if it appears).
        """
        # Navigate to the site
        driver.get("https://www.issta.co.il/")
        driver.implicitly_wait(10)  # Wait for the page to load

        # Step 1: Handle JavaScript Alert (if present)
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait up to 5 seconds for the alert
            alert = driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()  # Accept the alert
            print("JavaScript alert handled")
        except Exception:
            print("No JavaScript alert found")
            elem = driver.find_element(By.XPATH,
                                       "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[1]/div/div/div[2]/se-abroad-dynamic-packages-autocomplete/input")
            elem.click()
            time.sleep(3)



