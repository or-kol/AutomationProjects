import allure
from pages.base_page import BasePage
from pages.locators import Locators

class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Add product to cart from product page")
    def add_item_to_cart(self):
        self.click(Locators.ADD_TO_CART_BTN)

    @allure.step("Remove product from cart from product page")
    def remove_item_from_cart(self):
        self.click(Locators.REMOVE_FROM_CART_BTN)

    @allure.step("Go to products list page")
    def back_to_prod_list_page(self):
        self.click(Locators.BACK_TO_PRODUCTS_LIST_PAGE_BTN)

    @allure.step("Get the name of the product in the page")
    def get_product_name(self):
        return self.get_text(Locators.PRODUCTS_NAME)

    @allure.step("Get amount of products in cart")
    def get_amount_of_prod_in_cart(self):
        return self.get_text(Locators.CART_BTN)