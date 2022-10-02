from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(
            text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))
        return self.driver.title
