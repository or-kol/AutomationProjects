import pytest
import allure
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import ConfigReader


@allure.epic("Purchase")
@allure.feature("Cart")
class TestCartPage:

    ONE_PROD_IN_CART = "1"
    ZERO_PROD_IN_CART = "0"

    product_list = ConfigReader.get_keys("products_list")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding product to cart, going to cart to make sure correct product was added. "
                        "Then logging out")
    @allure.title("Correct item added to cart")
    @allure.story("Adding a product to cart, going to cart and validate that the product added to cart is correct")
    @pytest.mark.parametrize("product", product_list)
    def test_correct_item_added_to_cart(self, product, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", product))
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_items_list = cart_page.get_cart_list()

        expected_result = product.replace("_position", "").replace("_", " ")
        actual_result = cart_items_list[0].text.lower()
        assert expected_result in actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding product to cart, going to cart to make sure product was added to cart,"
                        "remove item from cart. Then logging out")
    @allure.title("remove from cart from cart page")
    @allure.story("Adding a product to cart, going to cart and removing the product from cart page")
    @pytest.mark.parametrize("product", product_list)
    def test_remove_item_from_cart(self, product, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", product))
        product_num = ConfigReader.read_config("products_list", product)
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)

        if cart_page.get_amount_of_prod_in_cart() == self.ONE_PROD_IN_CART:
            cart_page.remove_item_from_cart(product_num)
            expected_result = self.ZERO_PROD_IN_CART
            actual_result = self.ZERO_PROD_IN_CART if cart_page.get_amount_of_prod_in_cart() == '' \
                else cart_page.get_amount_of_prod_in_cart()
            assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"
        else:
            f"there are {cart_page.get_amount_of_prod_in_cart()} in cart, expected {self.ONE_PROD_IN_CART}"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, going to cart, go to checkout. Then logging out")
    @allure.title("Go to checkout page")
    @allure.story("Going to cart page and continue to checkout page")
    def test_go_to_checkout_page(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_to_checkout_page()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.get_checkout_page_title()

        expected_result = "Checkout: Your Information"
        actual_result = checkout_page.get_checkout_page_title()
        assert expected_result in actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding product to cart, click continue shopping button. "
                        "Then logging out")
    @allure.title("Go to products list page")
    @allure.story("Going to cart page and going back to product list page")
    def test_go_to_prod_list_page(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_back_to_prod_list_page()

        prod_list_page.get_prod_list_page_title()

        expected_result = "Products"
        actual_result = prod_list_page.get_prod_list_page_title()
        assert expected_result in actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"