import allure
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from utils.config_reader import ConfigReader

@allure.epic("Purchase")
@allure.feature("Checkout")
class TestCheckoutPage:

    def get_to_checkout_page(self, prod_list_page):
        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_to_checkout_page()

        return CheckoutPage(self.driver)


    valid_checkout_info = [("first_name1", "last_name1", "zip1"),
                     ("first_name2", "last_name2", "zip2"),
                     ("first_name3", "last_name3", "zip3"),
                     ("first_name4", "last_name4", "zip4"),
                     ("first_name5", "last_name5", "zip5")]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding product to cart, going to cart, go to checkout, adding valid information"
                        "continue to overview page. Then logging out")
    @allure.title("Valid input in checkout")
    @allure.story("Filling valid information in checkout")
    @pytest.mark.parametrize("first_name, last_name, zip", valid_checkout_info)
    def test_fill_checkout_info_valid_info(self, first_name, last_name, zip, login_fixture):
        first_name = ConfigReader.read_config("valid_checkout_data", first_name)
        last_name = ConfigReader.read_config("valid_checkout_data", last_name)
        zip = ConfigReader.read_config("valid_checkout_data", zip)

        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Bolt_T-Shirt_position"))

        checkout_page = self.get_to_checkout_page(prod_list_page)
        checkout_page.fill_info(first_name, last_name, zip)

        overview_page = OverviewPage(self.driver)

        expected_result = "Checkout: Overview"
        actual_result = overview_page.get_overview_page_title()
        assert expected_result == actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    invalid_checkout_info = [("first_name1", "last_name1", "zip1"),
                             ("first_name2", "last_name2", "zip2"),
                             ("first_name3", "last_name3", "zip3"),
                             ("first_name4", "last_name4", "zip4"),
                             ("first_name5", "last_name5", "zip5"),
                             ("first_name6", "last_name6", "zip6")]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding product to cart, going to cart, go to checkout, adding invalid information"
                        "continue to overview page. Then logging out")
    @allure.title("Invalid input in checkout")
    @allure.story("Filling invalid information in checkout")
    @pytest.mark.parametrize("first_name, last_name, zip", invalid_checkout_info)
    def test_fill_checkout_info_missing_info(self, first_name, last_name, zip, login_fixture):
        first_name = ConfigReader.read_config("invalid_checkout_data", first_name)
        last_name = ConfigReader.read_config("invalid_checkout_data", last_name)
        zip = ConfigReader.read_config("invalid_checkout_data", zip)

        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Bolt_T-Shirt_position"))

        checkout_page = self.get_to_checkout_page(prod_list_page)
        checkout_page.fill_info(first_name, last_name, zip)

        expected_result = ""
        if first_name == "" or first_name.isnumeric():
                expected_result = "Error: First Name is required"
        elif last_name == "" or last_name.isnumeric():
                expected_result = "Error: Last Name is required"
        elif zip == "" or zip.isalpha():
                expected_result = "Error: Postal Code is required"

        try:
            actual_result = checkout_page.get_checkout_error_msg()
        except Exception as e:
            print(e)
            actual_result = "No error"

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding product to cart, going to cart, go to checkout, clicking cancel button. "
                        "Then logging out")
    @allure.title("Clicking cancel button in checkout")
    @allure.story("Clicking cancel button on checkout take back to cart")
    def test_cancel_button(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Bolt_T-Shirt_position"))

        checkout_page = self.get_to_checkout_page(prod_list_page)
        checkout_page.go_back_to_cart()

        cart_page = CartPage(self.driver)

        expected_result = "Your Cart"
        actual_result = cart_page.get_cart_page_title()
        assert expected_result == actual_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"

