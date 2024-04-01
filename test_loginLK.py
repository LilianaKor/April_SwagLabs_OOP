import time

USER_NAME = ("css selector", "input[data-test='username']")
PASSWORD = ("css selector", "input[data-test='password']")
LOGIN = ("css selector", "input[data-test='login-button']")


def test_loginLK(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    time.sleep(3)

