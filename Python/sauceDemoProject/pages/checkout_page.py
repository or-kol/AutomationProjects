import allure
from pages.base_page import BasePage
from pages.locators import Locators

class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checkout information: first name: {first_name}, last name: {last_name}, zip: {zip_code}")
    def fill_info(self, first_name, last_name, zip_code):
        self.fill_text(Locators.FIRST_NAME_FIELD, first_name)
        self.fill_text(Locators.LAST_NAME_FIELD, last_name)
        self.fill_text(Locators.ZIP_CODE_FIELD, zip_code)
        self.click(Locators.CONTINUE_BTN)

    @allure.step("Go to cart")
    def go_back_to_cart(self):
        self.click(Locators.CANCEL_BTN)

    @allure.step("Get checkout page title")
    def get_checkout_page_title(self):
        return self.get_text(Locators.CHECKOUT_PAGE_TITLE)

    @allure.step("Get checkout page error message")
    def get_checkout_error_msg(self):
        return self.get_text(Locators.ERROR_MSG)