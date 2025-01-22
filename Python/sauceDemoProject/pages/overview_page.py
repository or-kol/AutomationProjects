import allure
from pages.base_page import BasePage
from pages.locators import Locators

class OverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get overview page title")
    def get_overview_page_title(self):
        return self.get_text(Locators.OVERVIEW_PAGE_TITLE)

    @allure.step("Complete purchase")
    def complete_purchase(self):
        self.click(Locators.FINISH_BTN)

    @allure.step("Go to products list page")
    def go_back_to_prod_list_page(self):
        self.click(Locators.CANCEL_BTN)

    @allure.step("Get payment information")
    def get_payment_info(self):
        return self.get_text(Locators.PAYMENT_INFO)

    @allure.step("Get shipping information")
    def get_shipping_info(self):
        return self.get_text(Locators.SHIPPING_INFO)

    @allure.step("Get net price")
    def get_net_price(self):
        return self.get_text(Locators.ITEM_PRICE_INFO)

    @allure.step("Get tax amount")
    def get_tax(self):
        return self.get_text(Locators.TAX_INFO)

    @allure.step("Get total price")
    def get_total_price(self):
        return self.get_text(Locators.TOTAL_PRICE_INFO)