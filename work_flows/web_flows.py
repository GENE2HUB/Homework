import time
import utilities.manage_pages as page
from extenstions.ui_actions import UiActions
from extenstions.verifications import Verifications
from selenium.webdriver import Keys
from utilities.common_ops import wait, get_data


class WebFlows:
    @staticmethod
    # @allure.step('go to users flow')
    #def search_flight_with_hotel__table_flow(self):

    @staticmethod
    # @allure.step('go to users flow')
    def open_search_flight_only_table_flow(self):
        elem1 = page.HomeRightSideMenu.get_right_side_menu(self)
        elem2 = page.HomeRightSideMenu.get_flight(self)
        UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    def insert_data_to_search_flight_only_table_flow(self):
        UiActions.update_text(page.HomeFlightOnlyPage.get_flight_from(self),"TLV" + Keys.RETURN)
        UiActions.update_text(page.HomeFlightOnlyPage.get_flight_to(self),"ATH"+ Keys.RETURN)
        UiActions.click(page.HomeFlightOnlyPage.get_open_calendar())
        UiActions.click(page.HomeFlightOnlyPage.get_open_calendar())
        UiActions.click(page.HomeFlightOnlyPage.get_next_month())

        start_date = page.HomeFlightOnlyPage.get_next_month()
        end_date = page.HomeFlightOnlyPage.get_next_month()
        UiActions.mouse_hover(start_date, end_date)

        UiActions.click(page.HomeFlightOnlyPage.get_find_cheap_flight())

    @staticmethod
    def insert_data_to_flight_with_hotel_table_flow(self):
        UiActions.update_text(page.HomeFlightWithHotelPage.get_destination(self),"ATH")
        UiActions.click(page.HomeFlightWithHotelPage.get_open_calender())
        UiActions.click(page.HomeFlightWithHotelPage.get_next_month())

        start_date = page.HomeFlightWithHotelPage.get_start_date()
        end_date = page.HomeFlightWithHotelPage.get_end_date()
        UiActions.mouse_hover(start_date, end_date)

        UiActions.click(page.HomeFlightWithHotelPage.get_find_deal_abroad_button())

    @staticmethod
    def flight_details_flow(self):
        price = page.FlightDetailsPage.get_flight_price_value()
        UiActions.click(page.FlightDetailsPage.get_all_results())


    @staticmethod
    def passengers_details_flow(self):
        UiActions.click(page.PassengersDetailsPage.get_Ordering_details_table())
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_first_name(),get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_passenger_last_name(),get_data('LaststName'))
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_email(),get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_phone(),get_data('FirstName'))
        UiActions.click(page.PassengersDetailsPage.get_Ordering_details_button())
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_first_name(),get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_first_name(),get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_first_name(),get_data('FirstName'))
        UiActions.update_text(page.PassengersDetailsPage.get_Ordering_details_first_name(),get_data('FirstName'))


    """
    # Verify Right Side Menu Buttons
    @staticmethod
    # @allure.step('verify Issta title flow')
    def verify_right_side_menu_buttons_flow_smart_assertions(expected: str):
        elems = [page.HomeRightSideMenu.get_right_side_menu(),
                 page.HomeRightSideMenu.get_flight_and_hotel(),
                 page.HomeRightSideMenu.get_flight(),
                 page.HomeRightSideMenu.get_vacation_in_israel(),
                 page.HomeRightSideMenu.get_hotels_abroad(),
                 page.HomeRightSideMenu.get_organized_tour()]
        Verifications.soft_assert(elems)
"""
