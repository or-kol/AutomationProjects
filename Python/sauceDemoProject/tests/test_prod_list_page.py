import allure
import pytest
from pages.cart_page import CartPage
from pages.prod_page import ProductPage
from utils.config_reader import ConfigReader

@allure.epic("Website browsing")
@allure.feature("Main page (product list page)")
class TestProductsList:

    ONE_PROD_IN_CART = "1"
    ZERO_PROD_IN_CART = "0"

    product_list = ConfigReader.get_keys("products_list")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, going to product page, verify it's the correct product. Then logging out")
    @allure.title("Go to product page")
    @allure.story("Going to product page")
    @pytest.mark.parametrize("product", product_list)
    def test_go_to_product_page(self, product, login_fixture):
        prod_list_page = login_fixture
        product_num = ConfigReader.read_config("products_list", product)
        prod_list_page.go_to_prod_page(product_num)

        prod_page = ProductPage(self.driver)
        expected_result = product.replace("_position", "").replace("_", " ")
        actual_result = prod_page.get_product_name().lower()
        assert expected_result in actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, going to cart. Then logging out")
    @allure.title("Go to cart")
    @allure.story("Going to cart")
    def test_go_to_cart_page(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)

        expected_result = "Your Cart"
        actual_result = cart_page.get_cart_page_title()
        assert expected_result in actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, quick adding to cart, checking an item was added to cart. Then logging out")
    @allure.title("Add to cart from products list page")
    @allure.story("Adding product to cart from main page")
    @pytest.mark.parametrize("product", product_list)
    def test_quick_add_to_cart(self, product, login_fixture):
        prod_list_page = login_fixture
        product_num = ConfigReader.read_config("products_list", product)

        prod_list_page.quick_add_item_to_cart(product_num)

        expected_result = self.ONE_PROD_IN_CART
        actual_result = prod_list_page.get_amount_of_prod_in_cart()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, quick adding to cart, checking an item was added to cart, quick remove from cart"
                        "checking that the cart is empty. Then logging out")
    @allure.title("remove from cart from products list page")
    @allure.story("Removing product from cart from main page")
    @pytest.mark.parametrize("product", product_list)
    def test_quick_remove_from_cart(self, product, login_fixture):
        prod_list_page = login_fixture
        product_num = ConfigReader.read_config("products_list", product)
        prod_list_page.quick_add_item_to_cart(product_num)

        if prod_list_page.get_amount_of_prod_in_cart() == self.ONE_PROD_IN_CART:
            prod_list_page.quick_remove_item_from_cart(product_num)

            expected_result = self.ZERO_PROD_IN_CART
            actual_result = self.ZERO_PROD_IN_CART if prod_list_page.get_amount_of_prod_in_cart() == '' \
                else prod_list_page.get_amount_of_prod_in_cart()
            assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"
        else:
            f"there are {prod_list_page.get_amount_of_prod_in_cart()} in cart, expected {self.ONE_PROD_IN_CART}"


    sort_options = ConfigReader.get_values("product_sort_options")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, set items list sort, checking items order. Then logging out")
    @allure.title("Products list sort")
    @allure.story("Sorting products list")
    @pytest.mark.parametrize("sort", sort_options)
    def test_product_sort(self, sort, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.sort_products(sort)

        expected_result = sort
        actual_result = "Sorting Error"

        match sort:
            case "az":
                products_names_list = prod_list_page.get_products_names_list()
                actual_result = sort if products_names_list == sorted(products_names_list) else "Sorting Error"
            case "za":
                products_names_list = prod_list_page.get_products_names_list()
                actual_result = sort if products_names_list == sorted(products_names_list, reverse=True) else "Sorting Error"
            case "lohi":
                products_prices_list = prod_list_page.get_products_prices_list()
                actual_result = sort if products_prices_list == sorted(products_prices_list, key=lambda x: float(x[1:])) else "Sorting Error"
            case "hilo":
                products_prices_list = prod_list_page.get_products_prices_list()
                actual_result = sort if products_prices_list == sorted(products_prices_list, key=lambda x: float(x[1:]), reverse=True) else "Sorting Error"
            case _:
                print(f"{sort} is invalid sorting option")

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"
