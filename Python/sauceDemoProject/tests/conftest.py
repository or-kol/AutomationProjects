import os
import platform
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from pages.login_page import LoginPage
from pages.prod_list_page import ProductsList
from utils.config_reader import ConfigReader

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    # Create a local driver instance for each test
    driver = webdriver.Chrome()
    request.cls.driver = driver  # Attach driver to the test class
    driver.maximize_window()
    url = ConfigReader.read_config("url_info", "url")
    driver.get(url)

    # Yield control back to the test and cleanup after
    yield driver
    driver.quit()


@pytest.fixture
def handle_alerts(request, setup):
    alert = Alert(setup)  # Use the driver instance from the setup fixture
    request.cls.alert = alert


def pytest_exception_interact(node, call, report):
    if report.failed and hasattr(node, 'cls') and hasattr(node.cls, 'driver'):
        # Attach screenshot if a driver instance exists
        driver = node.cls.driver
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )


def pytest_sessionfinish(session, exitstatus):
    # Check if driver is available before using it
    driver = getattr(session, 'driver', None)
    if driver:
        environment_properties = {
            'browser': driver.name,
            'driver_version': driver.capabilities['browserVersion'],
            'os': platform.system(),
            'os_version': platform.version(),
            'python_version': platform.python_version(),
            'selenium_version': webdriver.__version__,
        }

        allure_env_path = os.path.join("allure-results", 'environment.properties')
        os.makedirs(os.path.dirname(allure_env_path), exist_ok=True)

        with open(allure_env_path, 'w') as f:
            data = '\n'.join([f'{key}={value}' for key, value in environment_properties.items()])
            f.write(data)

@pytest.fixture
def login_fixture(request, setup):
    login_page = LoginPage(setup)  # Use the driver from the setup fixture
    user_name = ConfigReader.read_config("login_info", "valid_user_name")
    password = ConfigReader.read_config("login_info", "valid_password")
    login_page.fill_info(user_name, password)
    return ProductsList(setup)
