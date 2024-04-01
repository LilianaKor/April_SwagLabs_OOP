import time

USER_NAME = ("css selector", "input[data-test='username']")
PASSWORD = ("css selector", "input[data-test='password']")
LOGIN = ("css selector", "input[data-test='login-button']")
TITLE = ("css selector", "span[data-test='title']")
CARDS = ("css selector", "div[data-test='inventory-item']")



def test_loginLK(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()

    actual_text = driver.find_element(*TITLE).text
    expected_text = "Products"
    assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
    time.sleep(3)

def test_loginLK(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()

    cards = driver.find_elements(*CARDS)
    for i in cards:
        print(i.text)



