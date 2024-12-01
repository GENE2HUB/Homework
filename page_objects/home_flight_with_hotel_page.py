from selenium.webdriver.common.by import By

# Issta Home Page Title > flight with hotel - search table  elements
destination = (By.XPATH,"//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[1]/div/div/div[2]")
#destination = (By.XPATH,"//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[2]")
#//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[1]/div/div/div[2]
open_calendar = (By.XPATH,"//*[@id='start_date']")
current_month = (By.ID, "//table[@class='month1 current']/tbody/tr/td/div[@class='day toMonth  valid']/span[@class='day-number'")
next_month = (By.ID, "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[1]/desktop-se-datepicker/div/div[3]/div[1]/div/div[2]")
start_date = (By.ID, "//*[@id='datepicker_widget']/div/div[2]/table[2]/tbody/tr[1]/td[1]/div")
end_date = (By.ID, "//*[@id='datepicker_widget']/div/div[2]/table[2]/tbody/tr[4]/td[7]/div")
passengers = (By.ID, "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[2]/se-base-hotels-passengers-picker")
find_deal_button = (By.ID, "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[3]")
direct_flight_only_button = (By.ID, "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[3]/div")
find_deal_abroad_button = (By.XPATH, "//*[@id='search_dynamic_packages']/se-abroad-dynamic-packages-form/form/div[1]/div[2]/div[3]/div/form-button/button")

class HomeFlightWithHotelPage:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    #main page> flight with hotel - search methods:
    def get_destination(self):
        return self.driver.find_element(destination[0],destination[1])

    def get_open_calender(self):
        return self.driver.find_element(flight[0],flight[1])

    def get_current_month(self):
        return self.driver.find_element(current_month[0],current_month[1])

    def get_next_month(self):
        return self.driver.find_element(next_month[0],next_month[1])

    def get_start_date(self):
        return self.driver.find_element(start_date[0],start_date[1])

    def get_end_date(self):
        return self.driver.find_element(end_date[0],end_date[1])

    def get_passengers(self):
        return self.driver.find_element(passengers[0],passengers[1])

    def get_direct_flight_only_button(self):
        return self.driver.find_element(direct_flight_only_button[0],direct_flight_only_button[1])

    def get_find_deal_abroad_button(self):
        return self.driver.find_element(find_deal_abroad_button[0],find_deal_abroad_button[1])
