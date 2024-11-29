import time

import pytest
import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EC, EdgeChromiumDriverManager

from utilities.common_ops import get_data
from utilities.manage_pages import ManagePages

driver = None
action = None

@pytest.fixture(scope='class') #will be recognize in the scope of the class
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    driver.get(get_data('Url')) # Navigate to the site
    driver.implicitly_wait(int(get_data('WaitTime')))  # Wait for the page to load

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

    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()

    yield
    driver.quit()


def get_web_driver():
    web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong Input, Unrecognize Browser")
    return driver


def get_chrome():
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)  # for Selenium 4.x
    #chrome_driver = selenium.webdriver.chrome(ChromeDriverManager().install()) # for Selenium 3.x
    return chrome_driver


def get_firefox():
    srv = Service(executable_path=GeckoDriverManager().install())
    firefox_driver = selenium.webdriver.Firefox(service=srv)  # for Selenium 4.x
    # firefox_driver = selenium.webdriver.GeckoDriverManager().install()) # for Selenium 3.x
    return firefox_driver


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=srv)  # for Selenium 4.x
    # edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) # for Selenium 3.x
    return edge_driver

