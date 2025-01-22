import allure
from pages.login_page import LoginPage
from pages.prod_list_page import ProductsList
from utils.config_reader import ConfigReader

@allure.epic("Security")
@allure.feature("Login")
@allure.severity(allure.severity_level.BLOCKER)
class TestLoginPage:

    @allure.description("Logging in with valid credentials. Then logging out")
    @allure.title("Loging into the system using valid credentials")
    @allure.story("Login using valid credentials")
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        user_name = ConfigReader.read_config("login_info", "valid_user_name")
        password = ConfigReader.read_config("login_info", "valid_password")
        login_page.fill_info(user_name, password)

        prod_list_page = ProductsList(self.driver)
        expected_result = "Products"
        actual_result = prod_list_page.get_prod_list_page_title()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.description("Trying to Login with locked user credentials")
    @allure.title("Fail to loging into the system with locked user credentials")
    @allure.story("Login using blocked user credentials")
    def test_locked_user_login(self):
        login_page = LoginPage(self.driver)
        user_name = ConfigReader.read_config("login_info", "locked_out_user_name")
        password = ConfigReader.read_config("login_info", "valid_password")
        login_page.fill_info(user_name, password)

        expected_result = "Epic sadface: Sorry, this user has been locked out."
        actual_result = login_page.get_error_msg()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.description("Trying to Login with invalid password")
    @allure.title("Fail to loging into the system with invalid password and valid username")
    @allure.story("Login using invalid password")
    def test_invalid_password_login(self):
        login_page = LoginPage(self.driver)
        user_name = ConfigReader.read_config("login_info", "valid_user_name")
        password = ConfigReader.read_config("login_info", "invalid_password")
        login_page.fill_info(user_name, password)

        expected_result = "Epic sadface: Username and password do not match any user in this service"
        actual_result = login_page.get_error_msg()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"


    @allure.description("Trying to Login with invalid username")
    @allure.title("Fail to loging into the system with valid password and invalid username")
    @allure.story("Login using invalid username")
    def test_invalid_username_login(self):
        login_page = LoginPage(self.driver)
        user_name = ConfigReader.read_config("login_info", "unknown_user")
        password = ConfigReader.read_config("login_info", "valid_password")
        login_page.fill_info(user_name, password)

        expected_result = "Epic sadface: Username and password do not match any user in this service"
        actual_result = login_page.get_error_msg()

        assert actual_result == expected_result, f"Actual result = '{actual_result}', expected = '{expected_result}'"