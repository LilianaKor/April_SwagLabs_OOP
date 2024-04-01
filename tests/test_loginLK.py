#import time

# USER_NAME = ("css selector", "input[data-test='username']")  ## go to fixture conftest
# PASSWORD = ("css selector", "input[data-test='password']")
# LOGIN = ("css selector", "input[data-test='login-button']")
# TITLE = ("css selector", "span[data-test='title']")   # because go to class Mainlocators:
# CARDS = ("css selector", "div[data-test='inventory-item']")

class TestLogin():

    def test_loginLK(self, driver):
        page = LoginPage(driver, base_url)

        # driver.get("https://www.saucedemo.com/")     ## go to fixture
        # driver.find_element(*USER_NAME).send_keys("standard_user")
        # driver.find_element(*PASSWORD).send_keys("secret_sauce")
        # driver.find_element(*LOGIN).click()
        actual_text = driver.find_element(*TITLE).text
        expected_text = "Products"
        assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
        time.sleep(3)

    def test_loginLK(self, driver):
        # driver.get("https://www.saucedemo.com/")           # go to fixture
        # driver.find_element(*USER_NAME).send_keys("standard_user")
        # driver.find_element(*PASSWORD).send_keys("secret_sauce")
        # driver.find_element(*LOGIN).click()
        expected_len = 6
        cards = driver.find_elements(*CARDS)
        assert len(cards) == expected_len, f"Expected: {expected_len}, actual: {len(cards)}"




