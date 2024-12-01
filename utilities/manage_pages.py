
import test_cases.conftest as conf
from page_objects.flight_details_page import FlightDetailsPage
from page_objects.home_flight_only_page import HomeFlightOnlyPage
from page_objects.home_flight_with_hotel_page import HomeFlightWithHotelPage
from page_objects.home_page import HomePage
from page_objects.home_right_side_menu_page import HomeRightSideMenu
from page_objects.passengers_details_page import PassengersDetailsPage
from page_objects.payment_page import PaymentPage
from page_objects.search_results_page import SearchResultsPage

#Web Objects - global
home_page = None
right_side_menu= None
flight_with_hotel = None
flight_only = None
flight_details = None
search_results = None
payment_page = None
passengers_details = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['home_page'] = HomePage(conf.driver)
        globals()['right_side_menu'] = HomeRightSideMenu(conf.driver)
        globals()['flight_with_hotel'] = HomeFlightWithHotelPage(conf.driver)
        globals()['flight_only'] = HomeFlightOnlyPage(conf.driver)
        globals()['flight_details'] = FlightDetailsPage(conf.driver)
        globals()['search_results'] = SearchResultsPage(conf.driver)
        globals()['passengers_details'] = PassengersDetailsPage(conf.driver)
        globals()['payment_page'] = PaymentPage(conf.driver)
