import selenium

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def setup_browser():
    """
    Pytest fixture to set up and tear down the Selenium WebDriver.
    """
    global driver

    srv = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=srv)  # for Selenium 4.x
    # chrome_driver = selenium.webdriver.chrome(ChromeDriverManager().install()) # for Selenium 3.x
    driver.maximize_window()
    driver.get("https://www.issta.co.il/")
    yield driver  # Test function runs here
    driver.quit()

def select_date_range(driver, start_date, end_date):
    """
    Function to select a range of dates in the date widget.
    """
    # Wait for the date widget to be visible
    date_widget = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@class='month2']"))
    )
    days = date_widget.find_elements(By.TAG_NAME, "td")
    # Select dates within the range
    for date in range(start_date, end_date + 1):  # Inclusive range
        for day in days:
            if day.text == str(date):
                day.click()
                break
        # Wait for potential DOM updates after clicking
        WebDriverWait(driver, 1).until(
            EC.staleness_of(days[0])  # Wait for table to refresh (if necessary)
        )
        # Refresh days after DOM updates
        date_widget = driver.find_element(By.XPATH, "//table[@class='month2']")
        days = date_widget.find_elements(By.TAG_NAME, "td")

def test_select_date_range():
    """
    Test case to select a range of dates using a date picker.
    """
    #driver = setup_browser
    #driver.get("https://www.issta.co.il/")  # Replace with the URL of your application

    # Open date picker
    driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()

    # Select a range of dates, e.g., 1 to 28
    select_date_range(driver, 1, 28)

    # Add assertions here based on expected behavior
    # For example, verify that the range has been selected successfully.
    # Example (adjust based on app's behavior):
    selected_dates = driver.find_element(By.XPATH, "//span[@id='selected-dates']").text
    assert "1 - 28" in selected_dates, "Date range was not selected correctly!"
