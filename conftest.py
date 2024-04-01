import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")   #max window
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()