from selenium.webdriver.common.by import By

flight_detail_table = (By.XPATH,"//*[@id='wrapper']/div/main/div/div/issta-branded-fares")
flight_direction_abroad = (By.XPATH,"//*[@id='wrapper']/div/main/div/div/ul/li[1]/div")
flight_direction_home = (By.XPATH,"//*[@id='wrapper']/div/main/div/div/ul/li[2]/div")
flight_price = (By.XPATH, "//*[@id='wrapper']/div/main/div/div/issta-branded-fares/issta-branded-fares-header/div/div[2]/section/div/div[1]")
flight_price_value = (By.XPATH, "//*[@id='wrapper']/div/main/div/div/issta-branded-fares/issta-branded-fares-footer/div/div[2]/section/div/div[1]")
continue_field = (By.XPATH,"//*[@id='wrapper']/div/main/div[2]/div/issta-branded-fares/issta-branded-fares-footer/div/div[2]/div")

class FlightDetailsPage:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    def get_flight_detail_table(self):
        return self.driver.find_element(flight_detail_table[0],flight_detail_table[1])

    def get_flight_direction_abroad(self):
        return self.driver.find_element(flight_direction_abroad[0],flight_direction_abroad[1])

    def get_flight_direction_home(self):
        return self.driver.find_elements(flight_direction_home[0],flight_direction_home[1])

    def get_flight_price(self):
        return self.driver.find_element(continue_field[0],continue_field[1])

    def get_flight_price_value(self):
        price = self.driver.find_element(flight_price).text
        return float(price.replace("$", ""))

    def get_continue_field(self):
        return self.driver.find_element(continue_field[0],continue_field[1])
