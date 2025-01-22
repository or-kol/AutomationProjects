import allure
from pages.base_page import BasePage
from pages.locators import Locators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login with Username: {username} and Password: {password}")
    def fill_info(self, username, password):
        self.fill_text(Locators.USER_NAME_FIELD, username)
        self.fill_text(Locators.PASSWORD_FIELD, password)
        self.click(Locators.LOGIN_BTN)

    @allure.step("Get error message")
    def get_error_msg(self):
        return self.get_text(Locators.ERROR_MSG)


