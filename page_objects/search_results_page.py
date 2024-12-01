from selenium.webdriver.common.by import By

# elements used in tests
search_results_title = (By.XPATH,"//*[@id='all-flights-tab']/section/div[1]/div")
sort_cheap_price = (By.XPATH,"//*[@id='sort_tabs']/ul/li[1]")
flight_detail = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[1]/div[1]/div[1]/section[2]/div/div[4]/a")
flight_list_items = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]")
first_flight = (By.XPATH, "//*[@id='all-flights-tab']/section/div[3]/div[1]")
flight_price = (By.XPATH, "//*[@id='all-flights-tab']/section/div[3]/div[1]/div/section[2]/div/div[2]")
flight_title = (By.XPATH,"//*[@id='wrapper']/div/div[1]/div/div[1]/div/div[1]/div[1]/h1")

""" additional elements - that will be add acording to there necessary to the flow
#upper menu elements

date_search_field = (By.XPATH,"//*[@id='wrapper']/div/div[1]/div/div[1]/div/div[1]/div[2]")
persons_search_field = (By.XPATH,"//*[@id='wrapper']/div/div[1]/div/div[1]/div/div[1]/div[3]")
search_update_button = (By.XPATH,"//*[@id='wrapper']/div/div[1]/div/div[1]/div/div[1]/div[4]")

#all results tab elements
all_results_tab = (By.XPATH,"//*[@id='all-flights']")

#search result
search_result = (By.XPATH,"//*[@id='all-flights-tab']/section/div[1]/div")
single_flight_detail = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[3]")
sort_fast_flight = (By.XPATH,"//*[@id='sort_tabs']/ul/li[2]")
alert_info_flight = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[1]/p/span")
flight_list = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]")

#search_results_table - 
flight_list_items = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]") 
first_flight = (By.XPATH, "//*[@id='all-flights-tab']/section/div[3]/div[1]")
single_flight_detail = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[3]")
flight_price = (By.XPATH, "//*[@id='all-flights-tab']/section/div[3]/div[1]/div/section[2]/div/div[2]")

#list item result single item
flight_direction_abroad = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[3]/div/section[1]/ul/li[1]/div")
flight_direction_back = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[3]/div/section[1]/ul/li[2]/div")
flight_detail_button = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[3]/div/section[2]/div/div[4]")
more_flights_button = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[12]")

#right side menu elements
price = (By.XPATH,"'filter_form']/div[1]/div[1]")
price1 = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[1]/div/section[2]/div/div[2]")

single_flight = (By.XPATH,"//*[@id='all-flights-tab']/section/div[3]/div[1] ")
num_of_stops = (By.XPATH,"//*[@id='filter_form']/div[1]/div[2]")
company_name = (By.XPATH,"//*[@id='filter_form']/div[1]/div[3]")
departure_time = (By.XPATH,"//*[@id='filter_form']/div[1]/div[4]")
connection_duration = (By.XPATH,"//*[@id='filter_form']/div[1]/div[5]")
filter_reset = (By.XPATH,"//*[@id='filter_form']/div[2]")

#flexible tab elements
flexible_result_tab = (By.XPATH,"//*[@id='flexible-dates']")
flexible_dates = (By.XPATH,"//*[@id='flexible-dates-tab']/div[1]")
legend_line = (By.XPATH,"//*[@id='flexible-dates-tab']/div[1]/div")
remark_line = (By.XPATH,"//*[@id='flexible-dates-tab']/div[2]")
calendar_table = (By.XPATH,"//*[@id='days3-table']")

#month view tab elements
month_view_tab = (By.XPATH,"//*[@id='flights-by-price']")
flights_per_price = (By.XPATH,"//*[@id='calendar']/div[1]/div[2]")
months_list = (By.XPATH,"//*[@id='calendar']/div[1]/div[1]/div")
week_days = (By.XPATH,"//*[@id='calendar']/div[2]/div/table/thead")
calendar_table = (By.XPATH,"//*[@id='calendar']/div[2]/div/table/tbody/tr/td/div/div")
"""

class SearchResultsPage:
    # initiation Constructor - get driver from
    def __init__(self,driver):
        # initiation the driver
        self.driver = driver

    # upper menu elements methods

    def get_flight_list_items(self):
        num_of_results = len(self.driver.find_elements(flight_list_items[0], flight_list_items[1]))
        if not num_of_results:
            print("No search results. Returning to the previous page to update parameters.")
            self.driver.back()
            return False
        else:
            return self.driver.find_elements(flight_list_items[0], flight_list_items[1])

    def get_first_flight(self):
        return self.driver.find_element(first_flight[0], first_flight[1])

    def get_flight_detail(self):
        return self.driver.find_element(flight_detail[0], flight_detail[1])

    def get_search_results_title(self):

        return self.driver.find_element(search_results_title[0],search_results_title[1])

    def get_flight_title(self):
        return self.driver.find_element(flight_title[0],flight_title[1])

    def get_sort_cheap_price(self):
        return self.driver.find_element(sort_cheap_price[0],sort_cheap_price[1])

    def get_flight_price (self):
        return self.driver.find_element(flight_price[0], flight_price[1])

    def get_flight_price_and_element(self, locator):
        """
        Retrieves the WebElement and its price value.
        Args:
            locator (tuple): A tuple containing the locator strategy and value (e.g., (By.XPATH, xpath)).
        Returns:
            tuple: WebElement, price (float).
        """
        #element = self.driver.find_element(*locator)
        price_text = flight_price.text
        price = float(price_text.replace("$", "").replace(",", ""))
        return self.driver.find_element(flight_price[0], flight_price[1]), price

"""
    def get_search_update_button(self):
        return self.driver.find_element(search_update_button[0],search_update_button[1])

    #all results tab elements  methods
    def get_all_results_tab(self):
        return self.driver.find_element(all_results_tab[0], all_results_tab[1])

    def get_single_flight(self):
        return self.driver.find_element(single_flight[0], single_flight[1])

    def get_price(self):
        return self.driver.find_element(price[0], price[1])

    def get_num_of_stops(self):
        return self.driver.find_element(num_of_stops[0], num_of_stops[1])

    def get_company_name(self):
        return self.driver.find_element(company_name[0], company_name[1])

    def get_departure_time(self):
        return self.driver.find_element(departure_time[0], departure_time[1])

    def get_connection_duration(self):
        return self.driver.find_element(connection_duration[0], connection_duration[1])

    def get_filter_reset(self):
        return self.driver.find_element(filter_reset[0], filter_reset[1])

    #flexible tab elements  methods
    def get_flexible_result_tab(self):
            return self.driver.find_element(flexible_result_tab[0], flexible_result_tab[1])

    #month view tab elements  methods
    def get_month_view_tab(self):
        return self.driver.find_element(month_view_tab[0], month_view_tab[1])

    def get_flights_per_price(self):
        return self.driver.find_element(flights_per_price[0], flights_per_price[1])

    def get_result_month_view_tab(self):
        return self.driver.find_element(months_list[0], months_list[1])

    def get_week_days(self):
        return self.driver.find_element(week_days[0], week_days[1])

    def get_calendar_table(self):
        return self.driver.find_element(calendar_table[0], calendar_table[1])
        
"""

