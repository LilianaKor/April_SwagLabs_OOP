import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

USER_NAME = ("css selector", "input[data-test='username']")
PASSWORD = ("css selector", "input[data-test='password']")
LOGIN = ("css selector", "input[data-test='login-button']")


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")  # max window
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # driver.get("https://www.saucedemo.com/")       # because moved to locators page (OOP)
    # driver.find_element(*USER_NAME).send_keys("standard_user")
    # driver.find_element(*PASSWORD).send_keys("secret_sauce")
    # driver.find_element(*LOGIN).click()
    yield driver
    driver.quit()
