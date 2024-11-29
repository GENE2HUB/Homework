import time

from test_cases.conftest import action
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager

import pytest
import selenium
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = None


class TestIsstaSite:
    """
    Test class for handling the Issta website.
    """

    def setup_class(self):
        globals()['driver'] = driver
        srv = Service(ChromeDriverManager().install())
        driver = selenium.webdriver.Chrome(service=srv)  # for Selenium 4.x
        # chrome_driver = selenium.webdriver.chrome(ChromeDriverManager().install()) # for Selenium 3.x
        driver.maximize_window()

        #srv = Service(EdgeChromiumDriverManager().install())
        #edge_driver = selenium.webdriver.Edge(service=srv)  # for Selenium 4.x
        # edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) # for Selenium 3.x


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
            print("\nJavaScript alert handled")
        except Exception:
            print("\nNo JavaScript alert found")

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
            print("\nJavaScript alert handled")
        except Exception:
            print("\nNo JavaScript alert found")

    def test_search_table(self):
        elem1 = (By.XPATH,
                           "//*[@id='wrapper']/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div[1]/div/se-tabs/nav")
        action.move_to_element(elem1).click().perform()
        #elem2 =
        #action.move_to_element(elem1).move_to_element(elem2).click().perform()

        #driver.find_element(By.XPATH, "//*[@id='flights_form_00f4aebd-8416-4770-9ebd-6c7b57ba3bbb']/div[1]/div[1]/div[1]/div/div[2]/se-flights-autocomplete/input").click()
        """
        driver.find_element(By.XPATH, "//*[@id='start_date']")
        time.sleep(2)

        #driver.find_element(By.XPATH, "//*[@id='datepicker_widget,]/div/div[2]/table[2]/thead/tr[1]/th[2]").click()
        #driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]").click()
        print(driver.find_element(By.XPATH, "//*[@id='datepicker_widget,]/div/div[2]/table[2]/thead/tr[1]/th[2]").text)
        driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]/thead/tr[1]").click()
        #date_widget = driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]/tbody")
        date_widget = driver.find_element(By.XPATH, "//table[@class='month2']")
        days = date_widget.find_elements(By.TAG_NAME, "td")
        # selecting to date
        for day in days:
            if day.text == "1":
                day.click()
                break
        time.sleep(2)
        # Open date picker
        time.sleep(3)
"""
    def test_click_element(self):
        """
        Test to locate and click the specified element on the Issta website.
        """
        #driver.implicitly_wait(5)  # Wait for the page to load

        """ 
        driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()
        date_widget = driver.find_element(By.XPATH, "//table[@class='month1']")
        days = date_widget.find_elements(By.TAG_NAME, "td")
        # selecting from date
        for day in days:
            if day.text == "28":
                days.click()
                break
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='start_date']").click()
        date_widget = driver.find_element(By.XPATH, "//table[@class='month2']")
        cells = date_widget.find_elements(By.TAG_NAME, "td")
        # selecting to date
        for day in days:
            if day.text == "28":
                days.click()
                break
        time.sleep(2)
        # Open date picker
        time.sleep(3)
        #driver.find_element(By.XPATH, "//*[@id='start_date']").clear()
        print(driver.find_element(By.XPATH, "//*[@id='start_date']").text)
        driver.find_element(By.XPATH, "//*[@id='start_date']").click()
        #guestes
        driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()
        print(driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").text)
 
    # Select "From" date
    self.select_date(driver, "1")

    # Wait for any DOM updates and select "To" date
    WebDriverWait(driver, 2).until(
        EC.staleness_of(driver.find_element(By.XPATH, "//table[@class='month2']")))
    self.select_date(driver, "28")

    
    driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()
    date_widget = driver.find_element(By.XPATH, "//table[@class='month1']")
    days = date_widget.find_elements(By.TAG_NAME, "td")
    # selecting from date
    for day in days:
        if days.text == "28":
            days.click()
            break
    time.sleep(2)
    
    date_widget = driver.find_element(By.XPATH, "//table[@class='month2']")
    cells = date_widget.find_elements(By.TAG_NAME, "td")
    #selecting to date
    for day in days:
        if days.text == "28":
            days.click()
            break
    time.sleep(2)
    
    
        #driver.find_element(By.XPATH, "//*[@id='start_date']").clear()

        driver.find_element(By.XPATH, "//*[@id='start_date']")
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]").click()
        print(driver.find_element(By.XPATH, "//*[@id='datepicker_widget,]/div/div[2]/table[2]/thead/tr[1]/th[2]").text)
        driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]/thead/tr[1]").click()
        date_widget = driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]/tbody")
        try:
            select_date_range(driver, "1", "28")
        except Exception as e:
            print(f"An error occurred: {e}")
"""

        driver.find_element(By.XPATH, "//div[@class='ng-tns-c19-0 ng-star-inserted']").click()
        driver.find_element(By.XPATH, "//*[@class='ng-spinner-remove']").click()
        driver.find_element(By.XPATH, "//*[@class='ng-btn ng-btn-primary']").click()
        driver.find_element(By.XPATH, "//*[@class='ng-btn ng-btn-primary ng-btn-form valid']").click()

        """
        # Step 1: Interact with the specified element
        try:
            # Locate and click the element by XPath

            elem = driver.find_element(By.XPATH,
                                       "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[1]/div/div/div[2]/se-abroad-dynamic-packages-autocomplete/input")
            elem.send_keys("LCA" + Keys.RETURN)
            alert = driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()  # Accept the alert

            #driver.find_element(By.XPATH,"//span[@class='next']").click()
            #driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()

            # elem.click()
            time.sleep(3)
            print("\nClicked on the element successfully")
        except Exception as e:
            pytest.fail(f"Failed to click on the element: {e}")


    
    def select_date(driver, date_value):

        # Function to select a date cell in the date widget.

        # Wait for the date widget to be visible
        date_widget = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='month2']"))
        )
        cells = date_widget.find_elements(By.TAG_NAME, "td")
        # Select the desired date
        for cell in cells:
            if cell.text == date_value:
                cell.click()
                break

        # Open date picker

    driver.find_element(By.XPATH, "//div[@class='ng-form-datepicker-head ng-star-inserted']").click()

    # Select "From" date
    select_date(driver, "1")

    # Wait for any DOM updates and select "To" date
    WebDriverWait(driver, 2).until(
        EC.staleness_of(driver.find_element(By.XPATH, "//table[@class='month2']")))
    select_date(driver, "28")


 """
def select_date_range(driver, start_date, end_date):
    """
    Function to select a range of dates in the date widget.

    :param driver: Selenium WebDriver instance
    :param start_date: The starting date as string (e.g., "1")
    :param end_date: The ending date as string (e.g., "28")
    """
    # Open date picker
    date_widget = driver.find_element(By.XPATH, "//table[@class='month2']")
    cells = date_widget.find_elements(By.TAG_NAME, "td")
    date_picker_xpath = "//div[@class='ng-form-datepicker-head ng-star-inserted']"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, date_picker_xpath))
    ).click()

    # Wait for the date widget to be visible
    date_widget_xpath = "//table[@class='month2']"

    def select_date_range(driver, start_date, end_date):
        # Open date picker
        #date_widget = driver.find_element(By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]")
        date_picker_xpath = "//table[@class='month2'"
            #"//div[@class='ng-form-datepicker-head ng-star-inserted']"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_picker_xpath))
        ).click()

        # Wait for the date widget to be visible
        date_widget_xpath = "//table[@class='month2']"
        date_widget = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, date_widget_xpath))
        )

        # Find all cells within the date widget
        cells = date_widget.find_elements(By.TAG_NAME, "td")

        # Create ActionChains object
        actions = ActionChains(driver)

        start_cell = None
        end_cell = None

        # Find start and end date cells
        for cell in cells:
            if cell.text == start_date:
                start_cell = cell
            if cell.text == end_date:
                end_cell = cell
            if start_cell and end_cell:
                break

        if start_cell and end_cell:
            # Hover over start date and click
            actions.move_to_element(start_cell).click().perform()

            # Hover over end date and click
            actions.move_to_element(end_cell).click().perform()
        else:
            print("Start or end date not found in the calendar")

    # Example usage
    try:
        select_date_range(driver, "1", "28")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    """
