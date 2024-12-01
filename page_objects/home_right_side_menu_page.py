from selenium.webdriver.common.by import By

# Issta Home Page Title - elemente of left side menu
right_side_menu = (By.XPATH,"//*[@id='nav-tabs']")
flight_and_hotel = (By.XPATH,"//ul[@id='nav-tabs']/li[3]")
package_tour = (By.XPATH,"//ul[@id='nav-tabs']/li[2]")
flight = (By.XPATH,"//*[@id='nav-tabs']/li[3]")
vacation_in_israel = (By.XPATH,"//ul[@id='nav-tabs']/li[4]")
hotels_abroad = (By.XPATH,"//ul[@id='nav-tabs']/li[4]")
organized_tour = (By.XPATH,"//ul[@id='nav-tabs']/li[4]")


class HomeRightSideMenu:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    # Right Side Menu Element methods
    def get_right_side_menu(self):
        return self.driver.find_element(right_side_menu[0],right_side_menu[1])

    def get_flight_and_hotel(self):
        return self.driver.find_element(flight_and_hotel[0],flight_and_hotel[1])

    def get_flight(self):
        return self.driver.find_element(flight[0],flight[1])

    def get_vacation_in_israel(self):
        return self.driver.find_element(vacation_in_israel[0],vacation_in_israel[1])

    def get_package_tour(self):
        return self.driver.find_element(package_tour[0],package_tour[1])

    def get_hotels_abroad(self):
        return self.driver.find_element(hotels_abroad[0],hotels_abroad[1])

    def get_organized_tour(self):
        return self.driver.find_element(organized_tour[0],organized_tour[1])
