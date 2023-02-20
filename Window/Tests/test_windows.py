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

    def test_01(self):
        # go to kivy app | cd app
        # python -m telenium.execute main.py
        cli = connect()
        cli.wait('//MDNavigationRailItem[@text="Connect"]', 5)
        cli.wait_click('//MDRaisedButton[@text="Connect"]', 5)
        cli.sleep(10)
