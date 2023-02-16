import time

from selenium.webdriver.support.wait import WebDriverWait

from Window.Tests.test_base import BaseTest
from appium.webdriver.common.appiumby import AppiumBy


class TestWindow(BaseTest):

    def get_web_element_from_dict_if_it_is(self, element_to_check_for_dict):
        if type(element_to_check_for_dict) is dict:
            first_element_value = list(element_to_check_for_dict.values())[0]
            element_to_check_for_dict = self.driver.create_web_element(element_id=first_element_value)
        return element_to_check_for_dict

    def test_01(self):
        el = self.driver.find_element(AppiumBy.NAME, 'One')
        el = self.get_web_element_from_dict_if_it_is(el)
        el.click()

        el2 = self.driver.find_element(AppiumBy.NAME, 'Two')
        el2 = self.get_web_element_from_dict_if_it_is(el2)
        el2.click()

        el3 = self.driver.find_element(AppiumBy.NAME, 'Seven')
        el3 = self.get_web_element_from_dict_if_it_is(el3)
        el3.click()

    def test_02(self):
        pass
