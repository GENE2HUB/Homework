import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pytest
from test_cases.conftest import driver
from utilities import common_ops

from work_flows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class Test_Issta:
    def test_search_flight_only(self):
        WebFlows.open_search_flight_only_table_flow(self)
        time.sleep(5)
        WebFlows.insert_data_to_search_flight_only_table_flow(self)
        time.sleep(5)

    def test_search_flight_with_hotel(self):
        WebFlows.insert_data_to_flight_with_hotel_table_flow(self)

    def test_passengers_detail_page(self):
        WebFlows.passengers_details_flow(self)
