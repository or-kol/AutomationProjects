import allure
from pages.base_page import BasePage
from pages.locators import Locators

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Remove product (product number in DB is : {prod})")
    def remove_item_from_cart(self, prod):
        button_mapping = {
            "1": Locators.SAUCE_LABS_BACKPACK_REMOVE_FROM_CART_BTN,
            "2": Locators.SAUCE_LABS_BIKE_LIGHT_REMOVE_FROM_CART_BTN,
            "3": Locators.SAUCE_LABS_BOLT_TSHIRT_REMOVE_FROM_CART_BTN,
            "4": Locators.SAUCE_LABS_FLEECE_JACKET_REMOVE_FROM_CART_BTN,
            "5": Locators.SAUCE_LABS_ONESIE_REMOVE_FROM_CART_BTN,
            "6": Locators.TEST_ALL_THE_THINGS_REMOVE_FROM_CART_BTN
        }

        button = button_mapping.get(prod)
        if button:
            self.click(button)
        else:
            print(f"{prod} is invalid input")

    @allure.step("Go to products list page")
    def go_back_to_prod_list_page(self):
        self.click(Locators.CONTINUE_SHOPPING_BTN)

    @allure.step("Go to checkout page")
    def go_to_checkout_page(self):
        self.click(Locators.CHECKOUT_BTN)

    @allure.step("Get items list from cart")
    def get_cart_list(self):
        return self.get_elements_list(Locators.CART_LIST)

    @allure.step("Get amount of items in cart")
    def get_amount_of_prod_in_cart(self):
        return self.get_text(Locators.CART_BTN)

    @allure.step("Get cart page title")
    def get_cart_page_title(self):
        return self.get_text(Locators.CART_PAGE_TITLE)