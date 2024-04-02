import time

from pages.order_page import OrderPage
from src.urls import Urls


class TestOrder:
    url = Urls()
    def  test_order_with_wrong_credential(self, driver):
        page = OrderPage(driver,self.url.base_url)
        page.open()
        page.login()
        page.order_with_wrong_credential()
        time.sleep(3)