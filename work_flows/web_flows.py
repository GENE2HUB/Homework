import time
import utilities.manage_pages as page
from extenstions.ui_actions import UiActions
from extenstions.verifications import Verifications
from selenium.webdriver import Keys
from test_cases.conftest import action
from utilities.common_ops import wait, get_data

class WebFlows:
    @staticmethod
    # @allure.step('go to users flow')
    # def search_flight_with_hotel__table_flow(self):

    @staticmethod
    # @allure.step('go to users flow')
    def open_search_flight_only_table_flow(self):
        elem1 = page.HomeRightSideMenu.get_right_side_menu(self)
        elem1 = page.HomeRightSideMenu.get_flight(self)
        UiActions.mouse_hover(elem1, elem1)

    @staticmethod
    def insert_data_to_search_flight_only_table_flow():
        UiActions.clear(page.HomeFlightOnlyPage.get_flight_from())
        UiActions.update_text(page.HomeFlightOnlyPage.get_flight_from(), "TLV")
        UiActions.update_text(page.HomeFlightOnlyPage.get_flight_to(), "ATH")
        UiActions.click(page.HomeFlightOnlyPage.get_open_calendar())
        # UiActions.click(page.HomeFlightOnlyPage.get_search_table())
        UiActions.click(page.HomeFlightOnlyPage.get_next_month())
        start_date = page.HomeFlightOnlyPage.get_next_month()
        end_date = page.HomeFlightOnlyPage.get_next_month()
        UiActions.mouse_hover(start_date, end_date)
        UiActions.click(page.HomeFlightOnlyPage.get_find_cheap_flight())

    @staticmethod
    def insert_data_to_flight_with_hotel_table_flow():
        UiActions.update_text(page.HomeFlightWithHotelPage.get_destination(), "ATH")
        UiActions.click(page.HomeFlightWithHotelPage.get_open_calender())
        UiActions.click(page.HomeFlightWithHotelPage.get_next_month())
        start_date = page.HomeFlightWithHotelPage.get_start_date()
        end_date = page.HomeFlightWithHotelPage.get_end_date()
        UiActions.mouse_hover(start_date, end_date)
        UiActions.click(page.HomeFlightWithHotelPage.get_find_deal_abroad_button())

    @staticmethod
    def search_result_page_flow():
        UiActions.click(page.SearchResultsPage.get_flight_detail())
        UiActions.click(page.SearchResultsPage.get_first_flight())
        UiActions.click(page.FlightDetailsPage.get_continue_field())

    @staticmethod
    def flight_details_flow():
        price = page.FlightDetailsPage.get_flight_price_value()
        UiActions.click(page.FlightDetailsPage.get_continue_field())

    @staticmethod
    def passengers_ordering_details_flow():
        UiActions.click(page.PassengersDetailsPage.get_ordering_details_table())
        UiActions.update_text(page.PassengersDetailsPage.get_ordering_details_first_name(), get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_ordering_details_last_name(), get_data('LastName'))
        UiActions.update_text(page.PassengersDetailsPage.get_ordering_details_email(), get_data('Email'))
        UiActions.update_text(page.PassengersDetailsPage.get_ordering_details_phone(), get_data('Phone'))
        UiActions.click(page.PassengersDetailsPage.get_ordering_details_button())

    @staticmethod
    def passengers_details_flow():
        UiActions.click(page.PassengersDetailsPage.get_passenger_first_name())
        UiActions.update_text(page.PassengersDetailsPage.get_passenger_first_name(), get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_passenger_last_name(),get_data('LastName'))
        UiActions.update_text(page.PassengersDetailsPage.get_passenger_email(), get_data('Email'))
        UiActions.update_text(page.PassengersDetailsPage.get_passenger_phone(), get_data('Phone'))
        UiActions.click(page.PassengersDetailsPage.get_passenger_without_handy_suitcase())
        UiActions.click(page.PassengersDetailsPage.get_passenger_without_suitcase())
        UiActions.click(page.PassengersDetailsPage.get_passenger_phone())
        UiActions.click(page.PassengersDetailsPage.get_passenger_sumit_button())

    @staticmethod
    def passengers_additional_service_flow():
        UiActions.click(page.PassengersDetailsPage.get_vip_service())
        UiActions.click(page.PassengersDetailsPage.get_cancel_service())
        UiActions.click(page.PassengersDetailsPage.get_new_service())

    @staticmethod
    def flight_payment_detail_flow():
        UiActions.click(page.PassengersDetailsPage.get_agreement())
        UiActions.click(page.PassengersDetailsPage.get_payment())

    @staticmethod
    def flight_payment_flow():
        UiActions.click(page.PaymentPage.get_payment_window())
        UiActions.update_text(page.PaymentPage.get_payment_credit_card(), get_data('CardNumber'))
        UiActions.update_text(page.PaymentPage.get_payment_id(), get_data('ID'))
        UiActions.update_text(page.PaymentPage.get_payment_month(), get_data('FirstName'))
        UiActions.update_text(page.PaymentPage.get_payment_card_cvv(), get_data('CardNumber'))
        UiActions.click(page.PaymentPage.get_submit_button())
