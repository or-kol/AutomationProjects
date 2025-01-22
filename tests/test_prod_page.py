from random import random
import allure
from pages.prod_page import ProductPage
from utils.config_reader import ConfigReader
import random

@allure.epic("Website browsing")
@allure.feature("Product page")
class TestProductPage:

    ONE_PROD_IN_CART = "1"
    ZERO_PROD_IN_CART = "0"

    product_list = ConfigReader.get_values("products_list")

    @allure.description("Logging in, going to product page, adding product to cart. Then logging out")
    @allure.title("Add to cart from product page")
    @allure.story("Going to product page and adding the product to cart from the product page")
    def test_add_to_cart(self, login_fixture):
        prod_list_page = login_fixture
        product_num = random.choice(self.product_list)
        prod_list_page.go_to_prod_page(product_num)

        prod_page = ProductPage(self.driver)
        prod_page.add_item_to_cart()

        expected_result = self.ONE_PROD_IN_CART
        actual_result = prod_page.get_amount_of_prod_in_cart()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.description("Logging in, going to product page, adding product to cart, checking a product qas added to cart,"
                        "remove product from cart. Then logging out")
    @allure.title("remove from cart from product page")
    @allure.story("Going to product page, adding the product to cart and removing the product from cart from the product page")
    def test_remove_from_cart(self, login_fixture):
        prod_list_page = login_fixture
        product_num = random.choice(self.product_list)
        prod_list_page.go_to_prod_page(product_num)

        prod_page = ProductPage(self.driver)
        prod_page.add_item_to_cart()

        if prod_page.get_amount_of_prod_in_cart() == self.ONE_PROD_IN_CART:
            prod_page.remove_item_from_cart()
        else:
            print(f"Item was not added to cart")

        expected_result = self.ZERO_PROD_IN_CART
        actual_result = self.ZERO_PROD_IN_CART if prod_page.get_amount_of_prod_in_cart() == '' \
            else prod_page.get_amount_of_prod_in_cart()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.description("Logging in, going to product page, clicking back to products. Then logging out")
    @allure.title("Clicking back to products button")
    @allure.story("Going to product page, clicking back to product button, taking to main page")
    def test_back_to_products_btn(self, login_fixture):
        prod_list_page = login_fixture
        product_num = random.choice(self.product_list)
        prod_list_page.go_to_prod_page(product_num)

        prod_page = ProductPage(self.driver)
        prod_page.back_to_prod_list_page()

        expected_result = "Products"
        actual_result = prod_list_page.get_prod_list_page_title()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"