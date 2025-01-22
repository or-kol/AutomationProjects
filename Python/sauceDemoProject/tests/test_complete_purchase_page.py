import allure
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_purchase_page import CompletePurchasePage
from pages.overview_page import OverviewPage
from pages.prod_list_page import ProductsList
from utils.config_reader import ConfigReader

@allure.epic("Purchase")
@allure.feature("Complete purchase")
class TestCompletePurchasePage:

    def get_to_copmlete_purchase_page(self, prod_list_page):
        first_name = ConfigReader.read_config("valid_checkout_data", "first_name5")
        last_name = ConfigReader.read_config("valid_checkout_data", "last_name5")
        zip = ConfigReader.read_config("valid_checkout_data", "zip5")

        prod_list_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.go_to_checkout_page()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_info(first_name, last_name, zip)

        overview_page = OverviewPage(self.driver)
        overview_page.complete_purchase()

        return CompletePurchasePage(self.driver)


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Logging in, adding product to cart, going to cart, go to checkout, continue to overview page, "
                        "finish transaction. Then logging out")
    @allure.title("Clicking back home button in complete transaction page")
    @allure.story("Clicking back home take to main page")
    def test_back_home_btn(self, login_fixture):
        prod_list_page = login_fixture
        prod_list_page.quick_add_item_to_cart(ConfigReader.read_config("products_list", "Sauce_Labs_Onesie_position"))

        overview_page = self.get_to_copmlete_purchase_page(prod_list_page)
        overview_page.go_to_prod_list_page()

        prod_list_page = ProductsList(self.driver)
        expected_result = "Products"
        actual_result = prod_list_page.get_prod_list_page_title()
        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"