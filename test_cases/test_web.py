import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_cases.conftest import driver
from utilities import common_ops
from work_flows.web_flows import WebFlows

@pytest.mark.usefixtures('init_web_driver')
class Test_Issta_Web_Site:
    def test_search_flight_only(self):
        WebFlows.open_search_flight_only_table_flow()
        WebFlows.insert_data_to_search_flight_only_table_flow()

    def test_select_flight(self):
        WebFlows.search_result_page_flow()
        WebFlows.flight_details_flow()

    def test_passengers_detail_page(self):
        WebFlows.passengers_ordering_details_flow()
        WebFlows.passengers_details_flow()
        WebFlows.passengers_additional_service_flow()
        WebFlows.flight_payment_detail_flow()
        WebFlows.flight_payment_flow()

    def test_search_flight_with_hotel(self):
        WebFlows.insert_data_to_flight_with_hotel_table_flow()





