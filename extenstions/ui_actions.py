from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf


# Cover actions of selenium
class UiActions:
    @staticmethod
    def click(elem):
        elem.click()

    @staticmethod
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    def update_text(elem: WebElement, value):
        elem.send_keys(value)

    @staticmethod
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    def right_click(elem: WebElement):
        conf.action.conftext_click(elem).perform()

    @staticmethod
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop(elem1).move_to_element(elem2).click().perform()



