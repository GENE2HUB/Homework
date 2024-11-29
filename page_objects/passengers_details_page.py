from selenium.webdriver.common.by import By

# content menu elements
Ordering_details_table = (By.XPATH, "//*[@id='payment_modal']")
Ordering_details_first_name = (By.XPATH, "//*[@id='checkout-first-name']")
Ordering_details_last_name = (By.XPATH, "//*[@id='checkout-last-name']")
Ordering_details_email = (By.XPATH, "//*[@id='checkout-email']")
Ordering_details_phone = (By.XPATH, "//*[@id='checkout-phone']")
Ordering_details_button = (By.XPATH, "//*[@id='customer_info_form']/div[2]/button")


passenger_first_name = (By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[1]/div[1]")
passenger_last_name = (By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[1]/div[2]")
passenger_email = (By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[1]/div[3]")
passenger_phone = (By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[1]/div[4]")

passenger_with_Handy_suitcase = (
By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]")
passenger_without_Handy_suitcase = (
By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[6]/div[2]/div[1]")

passenger_with_suitcase = (
By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[4]/div[2]/div[2]")
passenger_without_suitcase = (
By.XPATH, "//*[@id='presonalDetailsForm']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[4]/div[2]/div[1]")

passenger_sumit_button = (
By.XPATH, "//*[@id='presonalDetailsForm']/div[2]/button")


#Payment table
payment_first_name = (By.XPATH, "//*[@id='payment_step_details']/div[3]/div[2]/div/div[1]")
payment_last_name = (By.XPATH, "//*[@id='payment_step_details']/div[3]/div[2]/div/div[2]")
payment_checkout_email = (By.XPATH, "//*[@id='payment_step_details']/div[3]/div[2]/div/div[3]")
payment_checkout_phone = (By.XPATH, "//*[@id='payment_step_details']/div[3]/div[2]/div/div[4]")

# additional Services
vip_service = (By.XPATH, "//*[@id='3bde5b31-1585-4b9e-b18a-b2c481e9b8b7']/div[3]")
cancel_service = (By.XPATH, "//*[@id='2d0e362d-1b17-49a5-ad85-3a62d9bcc582']/div[3]")
new_service = (By.XPATH, "//*[@id='3bcc57e9-e118-466c-8308-171052ea568f']/div[3]")
addition_submit_button = (By.XPATH, "additional Services //*[@id='generalServicesForm']/div[2]/button")

# payment info
agreement = (By.XPATH, "//*[@id='payment_step_details']/div[6]/div/div/div[1]/label/p")
payment = (By.XPATH, "//*[@id='payment_step_details']/div[6]/div/div/div[2]/div[2]/div/div")
payment_submit_button = (By.XPATH, "//*[@id='payment_step_details']/div[6]/div/div/div[2]/div[2]/div/div")


class PassengersDetailsPage:
    # initiation Constructor - get driver from
    def __init__(self, driver):
        # initiation the driver
        self.driver = driver

    def get_Ordering_details_table(self):
        return self.driver.find_element(Ordering_details_table[0], Ordering_details_table[1])

    def get_Ordering_details_first_name(self):
        return self.driver.find_element(Ordering_details_first_name[0], Ordering_details_first_name[1])

    def get_Ordering_details_last_name(self):
        return self.driver.find_element(Ordering_details_last_name[0], Ordering_details_last_name[1])

    def get_Ordering_details_email(self):
        return self.driver.find_element(Ordering_details_email[0], Ordering_details_email[1])

    def get_Ordering_details_phone(self):
        return self.driver.find_element(Ordering_details_phone[0], Ordering_details_phone[1])

    def get_Ordering_details_button(self):
        return self.driver.find_element(Ordering_details_button[0], Ordering_details_button[1])

# Passengers Info
    def get_passenger_first_name(self):
        return self.driver.find_element(passenger_first_name[0], passenger_first_name[1])

    def get_passenger_last_name(self):
        return self.driver.find_element(passenger_last_name[0], passenger_last_name[1])

    def get_passenger_email(self):
        return self.driver.find_element(passenger_email[0], passenger_email[1])

    def get_passenger_phone(self):
        return self.driver.find_element(passenger_phone[0], passenger_phone[1])

    def get_passenger_with_Handy_suitcase(self):
        return self.driver.find_element(passenger_first_name[0], passenger_first_name[1])

    def get_passenger_without_Handy_suitcase(self):
        return self.driver.find_element(passenger_last_name[0], passenger_last_name[1])

    def get_passenger_with_suitcase(self):
        return self.driver.find_element(passenger_with_suitcase[0], passenger_with_suitcase[1])

    def get_passenger_without_suitcase(self):
        return self.driver.find_element(passenger_without_suitcase[0], passenger_without_suitcase[1])

    def get_passenger_sumit_button(self):
        return self.driver.find_element(passenger_sumit_button[0], passenger_sumit_button[1])


    def get_vip_service(self):
        return self.driver.find_element(vip_service[0], vip_service[1])

    def get_cancel_service(self):
        return self.driver.find_element(cancel_service[0], cancel_service[1])

    def get_new_service(self):
        return self.driver.find_element(new_service[0], new_service[1])

    # Payment table
    def get_payment_first_name(self):
        return self.driver.find_element(payment_first_name[0], payment_first_name[1])

    def get_payment_last_name(self):
        return self.driver.find_element(payment_last_name[0], payment_last_name[1])

    def get_payment_checkout_email(self):
        return self.driver.find_element(payment_checkout_email[0], payment_checkout_email[1])

    def get_payment_checkout_phone(self):
        return self.driver.find_element(payment_checkout_phone[0], payment_checkout_phone[1])

    def get_agreement(self):
        return self.driver.find_element(payment[0], payment[1])

    def get_payment(self):
        return self.driver.find_element(payment[0], payment[1])
