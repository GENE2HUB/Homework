from selenium.webdriver.common.by import By

# Home Page - flight only - search table  elements and metods:
search_table = (By.XPATH, "//*[@id='flights_form_d2e69178-63f5-4b16-8ce6-f9cf9bcd7834']/div[1]/div[1]")
flight_from = (By.XPATH, "//*[@id='flights_form_501a2521-d997-4df8-aa3e-bdab94ffbe33']/div[1]/div[1]/div[1]")
flight_to = (By.XPATH, "//*[@id='flights_form_501a2521-d997-4df8-aa3e-bdab94ffbe33']/div[1]/div[1]/div[2]")
#open_calendar = (By.XPATH, "//*[@id='start_date']")
current_month = (By.XPATH, "//table[@class='month1 current']/tbody/tr/td/div[@class='day toMonth  valid']/span[@class='day-number']")
open_calendar = (By.XPATH,"//*[@id='flights_form_501a2521-d997-4df8-aa3e-bdab94ffbe33']/div[1]/div[2]/div[1]")
calendar_icon = (By.XPATH,
                 "#//*[@id='flights_form_ab1d5fef-4077-4d48-ac63-46ee058819a9']/div[1]/div[2]/div[1]/div[1]/desktop-se-datepicker/div/div[1]")
next_month = (By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]")
start_date = (By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]")
end_date = (By.XPATH, "//*[@id='datepicker_widget']/div/div[2]/table[2]")

open_passengers_list = (By.ID, "//*[@id='flights_form_501a2521-d997-4df8-aa3e-bdab94ffbe33']/div[1]/div[2]/div[2]")
direct_flights_button_only = (By.XPATH, "//*[@id='flights_form_00f4aebd-8416-4770-9ebd-6c7b57ba3bbb']/div[3]/ul/li[1]/div/label/i")
flexible_dates_button = (By.XPATH, "//*[@id='flights_form_6e92792a-e5dc-40bf-84f9-37e8a06a408f']/div[3]/ul/li[2]/div/label")
find_cheap_flight = (By.XPATH, "//*[@id='flights_form_501a2521-d997-4df8-aa3e-bdab94ffbe33']/div[1]/div[2]/div[3]")

class HomeFlightOnlyPage:
    # initiation Constructor - get driver from
    def __init__(self, driver):
        # initiation the driver
        self.driver = driver

    # flight only Search Element methods
    def get_search_table(self):
        return self.driver.find_element(search_table[0], search_table[1])

    def get_flight_from(self):
        return self.driver.find_element(flight_from[0], flight_from[1])

    def get_flight_to(self):
        return self.driver.find_element(flight_to[0], flight_to[1])

    def get_open_calendar(self):
        return self.driver.find_element(open_calendar[0], open_calendar[1])

    def get_current_month(self):
        return self.driver.find_element(current_month[0], current_month[1])

    def get_next_month(self):
        return self.driver.find_element(next_month[0], next_month[1])

    def get_start_date(self):
        return self.driver.find_element(start_date[0], start_date[1])

    def get_end_date(self):
        return self.driver.find_element(end_date[0], end_date[1])

    def get_open_passengers_list(self):
        return self.driver.find_element(open_passengers_list[0], open_passengers_list[1])

    def get_direct_flights_button_only(self):
        return self.driver.find_element(direct_flights_button_only[0], direct_flights_button_only[1])

    def get_flexible_dates_button(self):
        return self.driver.find_element(flexible_dates_button[0], flexible_dates_button[1])

    def get_find_cheap_flight(self):
        return self.driver.find_element(find_cheap_flight[0], find_cheap_flight[1])