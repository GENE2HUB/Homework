from selenium.webdriver.common.by import By

# Issta Home Page Title
home_page_title = (By.XPATH,"//*[@id='wrapper']/div/div[4]/section/div/div/h1")

"""
# search table header elements:elements:
search_table_title = (By.XPATH,"'search_dynamic_packages']/div/h1")
flight_direction = (By.XPATH,"//*[@id='search_flights']/div[1]/div/nav[1]/div/div[1]")
flight_direction_arrow = (By.XPATH,"//*[@id='search_flights']/div[1]/div/nav[1]/div/div[1]/span")
flight_direction_list = (By.XPATH,"//*[@id='search_flights']/div[1]/div/nav[1]/div/div[2]/ul")
flight_type = (By.XPATH,"//*[@id='search_flights']/div[1]/div/div[2]/div/div[1]")
flight_type_arrow = (By.XPATH,"//*[@id='search_flights']/div[1]/div/nav[1]/div/div[1]/span")
flight_type_list = (By.XPATH,"//*[@id='search_flights']/div[1]/div/div[2]/div/div[2]/flight-class-select/div/ul")
flight_from_popular_destinations_list = (By.XPATH,"//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[1]/div[1]/div/div[2]/se-flights-autocomplete/div")
flight_to__popular_destinations_list = (By.XPATH,"//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[1]/div[2]/div/div[2]/se-flights-autocomplete/div")
next_month_arrow = (By.XPATH,"//*[@id='datepicker_widget']/div/div[2]/table[2]/thead/tr[1]/th[3]/span")
previous_month_arrow = (By.XPATH,"//*[@id='datepicker_widget']/div/div[2]/table[1]/thead/tr[1]/th[1]/span")
"""

#common field - elements- passengers
passengers = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]")
number_of_passengers = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]/se-flight-passengers-picker/div/div[2]/ul/li[1]/spinner-input/div/input")
passengers_list = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]/se-flight-passengers-picker/div/div[2]")
passengers_minus_button = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]/se-flight-passengers-picker/div/div[2]/ul/li[1]/spinner-input/div/button[1]")
passengers_add_button = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]/se-flight-passengers-picker/div/div[2]/ul/li[1]/spinner-input/div/button[2]")
passengers_choose_button = (By.XPATH, "//*[@id='flights_form_867f8871-b6f2-4119-875c-28bc8e93925a']/div[1]/div[2]/div[2]/se-flight-passengers-picker/div/div[2]/div/div/button")


class HomePage:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    # main page common element methods - passengers methods

    def get_passengers(self):
        return self.driver.find_element(passengers[0], passengers[1])

    def get_number_of_passengers(self):

        return self.driver.find_element(number_of_passengers[0], number_of_passengers[1])

    def get_passengers_list(self):
        return self.driver.find_element(passengers_list[0], passengers_list[1])

    def get_passengers_minus_button(self):
        return self.driver.find_element(passengers_minus_button[0], passengers_minus_button[1])
