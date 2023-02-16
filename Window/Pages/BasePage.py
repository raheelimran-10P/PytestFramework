import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def wait(self, number_of_seconds=3):
        time.sleep(number_of_seconds)

    def do_send_key(self, by_locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(
            text)

    def get_element_text(self, by_locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.title_is(title))
        return self.driver.title

    def openNewTab(self):
        self.driver.switch_to.new_window('tab')

    def switchTab(self, handler):
        self.driver.switch_to.window(handler)

    def select_by_index(self, locator, index, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_index(index)

    def select_by_visible_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(text)
        # assert element.text == text

    def select_by_value(self, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def checked_box(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        if not element.is_selected():
            element.click()
