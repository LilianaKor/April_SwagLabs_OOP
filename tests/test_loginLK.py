#import webdriver_manager
import time
#from locators.login_locators import LoginLocators
from locators.main_locators import Mainlocators
#from locators.main_locators import Mainlocators
from pages.login_page import LoginPage
from src.urls import Urls

from pages.login_page import LoginPage
from src.urls import Urls

# USER_NAME = ("css selector", "input[data-test='username']")  ## improve:go to fixture conftest
# PASSWORD = ("css selector", "input[data-test='password']")
# LOGIN = ("css selector", "input[data-test='login-button']")
# TITLE = ("css selector", "span[data-test='title']")   # because go to class Mainlocators
# CARDS = ("css selector", "div[data-test='inventory-item']")

# class LoginPage:
#     pass
class TestLogin():
    url = Urls()
    main_locators = Mainlocators()
    def test_loginLK(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        # time.sleep(4)

        # driver.get("https://www.saucedemo.com/")     ##  Improve: go to fixture
        # driver.find_element(*USER_NAME).send_keys("standard_user")
        # driver.find_element(*PASSWORD).send_keys("secret_sauce")
        # driver.find_element(*LOGIN).click()
 #        actual_text = driver.find_element(*TITLE).text
        expected_text = "Products"
        assert actual_text == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
        #time.sleep(3)

    def test_login1LK(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        # driver.get("https://www.saucedemo.com/")           #  update ; go to fixture
        # driver.find_element(*USER_NAME).send_keys("standard_user")
        # driver.find_element(*PASSWORD).send_keys("secret_sauce")
        # driver.find_element(*LOGIN).click()
        expected_len = 6
        cards = page.get_length(self.main_locators.CARDS)
        # cards = driver.find_elements(*CARDS)
        assert cards == expected_len, f"Expected: {expected_len}, actual: {cards}"




