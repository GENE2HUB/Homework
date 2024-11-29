from selenium.webdriver.common.by import By

payment_window = (By.XPATH,"//*[@id='payment_modal']")
payment_credit_card = (By.XPATH,"//*[@id='payment_modal']")
payment_id = (By.XPATH,"//*[@id='payment_modal']")
payment_year = (By.XPATH,"//*[@id='payment_modal']")
payment_month = (By.XPATH,"//*[@id='payment_modal']")
payment_card_cvv = (By.XPATH,"//*[@id='payment_modal']")

class PaymentPage:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    def get_payment_window(self):
        return self.driver.find_element(payment_window[0],payment_window[1])

    def get_payment_credit_card(self):
        return self.driver.find_element(payment_credit_card[0],payment_credit_card[1])

    def get_payment_id(self):
        return self.driver.find_element(payment_id[0],payment_id[1])

    def get_payment_month(self):
        return self.driver.find_element(payment_month[0],payment_month[1])

    def get_payment_card_cvv(self):
        return self.driver.find_element(payment_card_cvv[0],payment_card_cvv[1])
