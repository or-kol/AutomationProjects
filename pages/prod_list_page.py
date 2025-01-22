import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import Locators


class ProductsList(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Go to product page (product number in DB is : {prod})")
    def go_to_prod_page(self, prod):
        button_mapping = {
            "1": Locators.SAUCE_LABS_BACKPACK_BTN,
            "2": Locators.SAUCE_LABS_BIKE_LIGHT_BTN,
            "3": Locators.SAUCE_LABS_BOLT_TSHIRT_BTN,
            "4": Locators.SAUCE_LABS_FLEECE_JACKET_BTN,
            "5": Locators.SAUCE_LABS_ONESIE_BTN,
            "6": Locators.TEST_ALL_THE_THINGS_BTN
        }

        button = button_mapping.get(prod)
        if button:
            self.click(button)
        else:
            print(f"{prod} is invalid input")

    @allure.step("Get products list page title")
    def get_prod_list_page_title(self):
        return self.get_text(Locators.PRODUCT_LIST_PAGE_TITLE)

    @allure.step("Add product to cart from products list page (product number in DB is : {prod})")
    def quick_add_item_to_cart(self, prod):
        button_mapping = {
            "1": Locators.SAUCE_LABS_BACKPACK_ADD_TO_CART_BTN,
            "2": Locators.SAUCE_LABS_BIKE_LIGHT_ADD_TO_CART_BTN,
            "3": Locators.SAUCE_LABS_BOLT_TSHIRT_ADD_TO_CART_BTN,
            "4": Locators.SAUCE_LABS_FLEECE_JACKET_ADD_TO_CART_BTN,
            "5": Locators.SAUCE_LABS_ONESIE_ADD_TO_CART_BTN,
            "6": Locators.TEST_ALL_THE_THINGS_ADD_TO_CART_BTN
        }

        button = button_mapping.get(prod)
        if button:
            self.click(button)
        else:
            print(f"{prod} is invalid input")

    @allure.step("Remove product from cart from products list page (product number in DB is : {prod})")
    def quick_remove_item_from_cart(self, prod):
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

    @allure.step("Go to cart")
    def go_to_cart(self):
        self.click(Locators.CART_BTN)

    @allure.step("Get the product in position {n} in the page")
    def get_nth_product_in_page(self, n):
        return self.get_text((By.CSS_SELECTOR, f"#inventory_container>div>div:nth-child({n}).inventory_item"))

    @allure.step("Sort products list")
    def sort_products(self, option):
        self.select_option(Locators.PRODUCT_SORT, option)

    @allure.step("Get amount of products in cart")
    def get_amount_of_prod_in_cart(self):
        return self.get_text(Locators.CART_BTN)

    @allure.step("Get products names list from in products list page")
    def get_products_names_list(self):
        return [element.text for element in self.get_elements_list(Locators.PRODUCTS_NAMES_LIST)]

    @allure.step("Get products prices list from in products list page")
    def get_products_prices_list(self):
        return [element.text for element in self.get_elements_list(Locators.PRODUCTS_PRICES_LIST)]

