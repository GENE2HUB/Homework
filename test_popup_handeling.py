import time

import pytest

import selenium

from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = None
web_driver = 'Chrome'

@pytest.fixture(scope='class') #will be recognize in the scope of the class
class Test_Popup:

    # Set up the WebDriver (ensure ChromeDriver is in your PATH)
    #driver = webdriver.Chrome()

    def setup_class(self):
        global driver
        srv = Service(ChromeDriverManager().install())
        driver = selenium.webdriver.Chrome(service=srv)  # for Selenium 4.x
        # chrome_driver = selenium.webdriver.chrome(ChromeDriverManager().install()) # for Selenium 3.x
        driver.maximize_window()



    def teardown_class(self):
        time.sleep(3)
        driver.quit()


    def test_close_window(self):

        try:
            # Launch the website
            driver.get("https://www.issta.co.il/")
            driver.implicitly_wait(10)  # Wait for elements to load

            # Get the main window handle
            main_window = driver.current_window_handle

            # Handle any popups or alerts
            try:
                # If the popup is a JavaScript alert
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # Accept or dismiss as needed
                print("JavaScript alert handled")
            except Exception:
                print("No JavaScript alert found")

            # Handle additional windows or tabs if they open
            all_windows = driver.window_handles
            for handle in all_windows:
                if handle != main_window:
                    driver.switch_to.window(handle)
                    print(f"Switched to window: {handle}")
                    # Perform actions in the popup window, if needed
                    driver.close()
                    print("Popup window closed")
                    driver.switch_to.window(main_window)
                    print("Switched back to the main window")

            # Handle HTML modal popups
            try:
                # Locate the modal popup by ID, class, or other attributes
                popup = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ui-dialog"))  # Example class
                )
                print("Modal popup found")
                # Close the modal
                close_button = popup.find_element(By.CLASS_NAME, "ui-dialog-titlebar-close")
                close_button.click()
                print("Modal popup closed")
            except Exception:
                print("No HTML modal popup found")

        finally:
            #
            #time.sleep(3)
            # Close the browser
            #driver.find_element(By.XPATH, "//*[@id='nav-tabs']/li[3]").click()
            driver.quit()


   # def test_launching_to_search_table(self):
        #driver.find_element(By.XPATH, "//*[@id='nav-tabs']/li[3]").click()


        #time.sleep(3)