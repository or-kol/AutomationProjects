from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def fill_text(self, locator, text):
        self.highlight_element(locator, "yellow")
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator))
        self.highlight_element(locator, "yellow")
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located(locator))
        self.highlight_element(locator, "red")
        return self.driver.find_element(*locator).text

    def select_option(self, locator, option):
        self.highlight_element(locator, "yellow")
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(f"{option}")

    def get_elements_list(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def highlight_element(self, locator, color):
        element = self.driver.find_element(*locator)
        original_style = element.get_attribute("style")
        new_style = "background-color: " + color + ";" + original_style

        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)

        self.driver.execute_script("setTimeout(function() {arguments[0].setAttribute('style', arguments[1]);}, 100);"
                                   ,element, original_style)