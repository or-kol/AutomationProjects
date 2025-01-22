import allure
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_purchase_page import CompletePurchasePage
from pages.overview_page import OverviewPage
from pages.prod_list_page import ProductsList
from utils.config_reader import ConfigReader

@allure.epic("Purchase")
@allure.feature("Overview")
class TestOverviewPage:

    TAX_RATE = 0.08
    TWO_DECIMAL_PLACES = 2

    product_list = ConfigReader.get_keys("products_list")

    def get_to_overview_page(self, prod_list_page):
        first_name = ConfigReader.read_config("valid_checkout_data", "first_name5")
        last_name = ConfigReader.read_config("valid_checkout_data", "last_name5")
        zip = ConfigReader.read_config("valid_checkout_data", "zip5")

        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_to_checkout_page()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_info(first_name, last_name, zip)

        return OverviewPage(self.driver)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "verify payment information. Then logging out")
    @allure.title("Verify payment information")
    @allure.story("Adding a product to cart, going to cart and from there to overview. Filling information and verify "
                  "the payment information")
    def test_verify_payment_info(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Onesie_position"))

        payment_info = ConfigReader.read_config("overview_page_data", "payment_info")
        overview_page = self.get_to_overview_page(prod_list_page)

        expected_result = payment_info
        actual_result = overview_page.get_payment_info()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "verify shipping information. Then logging out")
    @allure.title("Verify shipping information")
    @allure.story("Adding a product to cart, going to cart and from there to overview. Filling information and verify "
                  "the shipping information")
    def test_verify_shipping_info(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Onesie_position"))

        shipping_info = ConfigReader.read_config("overview_page_data", "shipping_info")
        overview_page = self.get_to_overview_page(prod_list_page)

        expected_result = shipping_info
        actual_result = overview_page.get_shipping_info()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "verify net price information. Then logging out")
    @allure.title("Verify net price information")
    @allure.story("Adding a product to cart, going to cart and from there to overview. Filling information and verify "
                  "the product price information")
    @pytest.mark.parametrize("product", product_list)
    def test_verify_net_price_info(self, product, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", product))

        item_net_price = ConfigReader.read_config("overview_page_data", product.replace("_position", "_price"))
        overview_page = self.get_to_overview_page(prod_list_page)

        expected_result = f"Item total: ${item_net_price}"
        actual_result = overview_page.get_net_price()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "verify tax information. Then logging out")
    @allure.title("Verify tax information")
    @allure.story("Adding a product to cart, going to cart and from there to overview. Filling information and verify "
                  "the tax information")
    @pytest.mark.parametrize("product", product_list)
    def test_verify_tax_info(self, product, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", product))

        item_net_price = float(ConfigReader.read_config("overview_page_data", product.replace("_position", "_price")))
        item_tax = round(item_net_price * self.TAX_RATE, self.TWO_DECIMAL_PLACES)
        overview_page = self.get_to_overview_page(prod_list_page)

        expected_result = f"Tax: ${item_tax:.2f}"
        actual_result = overview_page.get_tax()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "verify total price information. Then logging out")
    @allure.title("Verify total price information")
    @allure.story("Adding a product to cart, going to cart and from there to overview. Filling information and verify "
                  "the total price information")
    @pytest.mark.parametrize("product", product_list)
    def test_verify_total_price_info(self, product, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", product))

        item_net_price = float(ConfigReader.read_config("overview_page_data", product.replace("_position", "_price")))
        total_item_price = round(item_net_price * 1.08, 2)
        overview_page = self.get_to_overview_page(prod_list_page)

        expected_result = f"Total: ${total_item_price:.2f}"
        actual_result = overview_page.get_total_price()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "clicking cancel button. Then logging out")
    @allure.title("Click cancel button in overview page")
    @allure.story("Going to overview, clicking cancel button, take to main page")
    def test_cancel_btn(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Onesie_position"))

        overview_page = self.get_to_overview_page(prod_list_page)
        overview_page.go_back_to_prod_list_page()

        prod_list_page = ProductsList(self.driver)

        expected_result = "Products"
        actual_result = prod_list_page.get_prod_list_page_title()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Logging in, adding a product to cart, going to cart, going to checkout, going to overview page, "
                        "going to complete purchase page. Then logging out")
    @allure.title("Going to complete purchase page")
    @allure.story("Going to overview, clicking finish button, take to complete purchase page")
    def test_finish_btn(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Onesie_position"))

        overview_page = self.get_to_overview_page(prod_list_page)
        overview_page.complete_purchase()

        complete_purchase_page = CompletePurchasePage(self.driver)

        expected_result = "Thank you for your order!"
        actual_result = complete_purchase_page.get_complete_purchase_msg()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"