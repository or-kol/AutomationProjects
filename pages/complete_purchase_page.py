import allure
from pages.base_page import BasePage
from pages.locators import Locators

class CompletePurchasePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get complete purchase message")
    def get_complete_purchase_msg(self):
        return self.get_text(Locators.COMPLETE_MSG)

    @allure.step("Go 'back home' (products list page)")
    def go_to_prod_list_page(self):
        self.click(Locators.BACK_HOME_BTN)