from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData

class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    # def login(self):  # go to base page
    #     self.driver.find_element(*self.locators.USER_NAME).send_keys(self.user.standard_user)
    #     self.driver.find_element(*self.locators.PASSWORD).send_keys(self.user.password)
    #     self.driver.find_element(*self.locators.LOGIN).click()

# pass
