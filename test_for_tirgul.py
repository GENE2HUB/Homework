import selenium

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = None
web_driver = 'Chrome'


# Fixture for setting up and tearing down the browser
@pytest.fixture(scope='class')
def init_web_driver(request):
    # Setup: Create a new instance of the browser
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait for elements to load
    driver.get("https://www.issta.co.il/")
    request.cls.driver = driver

    yield driver  # Provide the browser to the test
    # Teardown: Quit the browser after the test
    driver.quit()


# Test case
def test_issta_title(self):
    # Open the Issta homepage
    #driver.get("https://www.issta.co.il/")

    # Assert the page title contains "איסתא"
    assert "איסתא" in driver.title, "איסתא - אתר התיירות הגדול בישראל"


def test_search_flight(self):
    # Verify the search results page title
    driver.find_element(By.XPATH, "//div[@class='ng-tns-c19-0 ng-star-inserted']").click()
    driver.find_element(By.XPATH, "//*[@class='ng-spinner-remove']").click()
    driver.find_element(By.XPATH, "//*[@class='ng-btn ng-btn-primary']").click()
    driver.find_element(By.XPATH, "//*[@class='ng-btn ng-btn-primary ng-btn-form valid']").click()


def get_web_driver():
    #web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
        """
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong Input, Unrecognize Browser")
    """
    return driver


def get_chrome():
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)  # for Selenium 4.x
    #chrome_driver = selenium.webdriver.chrome(ChromeDriverManager().install()) # for Selenium 3.x
    return chrome_driver
