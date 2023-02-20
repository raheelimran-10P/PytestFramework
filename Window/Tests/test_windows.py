import time

from selenium.webdriver.support.wait import WebDriverWait
from telenium.client import TeleniumHttpClient

from Window.Tests.test_base import BaseTest
from appium.webdriver.common.appiumby import AppiumBy
from telenium import connect


class TestWindow(BaseTest):

    def get_web_element_from_dict_if_it_is(self, element_to_check_for_dict):
        if type(element_to_check_for_dict) is dict:
            first_element_value = list(element_to_check_for_dict.values())[0]
            element_to_check_for_dict = self.driver.create_web_element(element_id=first_element_value)
        return element_to_check_for_dict

    def connect_telenium(self, host="127.0.0.1", port=4723, timeout=5):
        """Connect to a remote telenium kivy module
        """
        return TeleniumHttpClient(f"http://{host}:{port}/jsonrpc", timeout=timeout)

    def test_01(self):
        # el = self.driver.find_element(AppiumBy.CUSTOM, '//MDRaisedButton[@text="Connect"]')
        # el = self.get_web_element_from_dict_if_it_is(el)

        # el2 = self.driver.find_element(AppiumBy.NAME, 'Export Data')
        # el2 = self.get_web_element_from_dict_if_it_is(el2)
        # el2.click()

        # el3 = self.driver.find_element(AppiumBy.NAME, 'Seven')
        # el3 = self.get_web_element_from_dict_if_it_is(el3)
        # el3.click()
        #
        # el4 = self.driver.find_element(AppiumBy.NAME, 'Clear entry')
        # el4 = self.get_web_element_from_dict_if_it_is(el4)
        # el4.click()
        pass

    def test_02(self):
        cli = self.connect_telenium()
        cli.wait('//MDRaisedButton[@text="Connect"]')
        cli.wait_click('//MDRaisedButton[@text="Connect"]')
        cli.sleep(10)
