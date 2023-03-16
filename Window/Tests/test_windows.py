from datetime import datetime
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from Browser.Pages.AwsDashboardPage import AwsDashboardPage
from Browser.Pages.AwsLoginPage import AwsLoginPage
from Window.Pages.EarthOticsDataCollector import EarthOpticsDataCollector
from Window.Pages.Simulator import Simulator
from Window.TestData.TestData import TestData
from telenium import connect
from decouple import config
from Window.Tests.test_base import BaseTest


class TestWindow(BaseTest):

    def get_web_element_from_dict_if_it_is(self, element_to_check_for_dict):
        if type(element_to_check_for_dict) is dict:
            first_element_value = list(element_to_check_for_dict.values())[0]
            element_to_check_for_dict = self.driver.create_web_element(element_id=first_element_value)
        return element_to_check_for_dict

    # @pytest.mark.skip(reason="Just for testing | reason")
    # def test_3(self):
    #     # Interact with app using accessibility IDs
    #     self.driver.find_element_by_accessibility_id("warmup_button")

    # @pytest.mark.skip(reason="Just for testing | reason")
    def test_01(self):
        # go to kivy app | cd app
        # python -m telenium.execute main.py
        app_driver = connect()
        app_driver.assertExists('//MDNavigationRailItem[@text="Connect"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDRaisedButton[@text="Connect"]', TestData.TIMEOUT)
        app_driver.assertExists('//MDLabel[@text="Connected"]', TestData.TIMEOUT)
        app_driver.assertExists('//MDNavigationRailItem[@text="Collect Data"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDNavigationRailItem[@text="Collect Data"]', TestData.TIMEOUT)

        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.login(config('AWS_IOT_USERNAME'), config('AWS_IOT_PASSWORD'))
        self.AwsDashboardPage = AwsDashboardPage(self.driver)
        self.AwsDashboardPage.get_title('IoT Device Simulator')
        self.AwsDashboardPage.go_to_device_type()
        self.AwsDashboardPage.create_device_types()
        self.AwsDashboardPage.go_to_simulation()
        self.AwsDashboardPage.create_simulation()
        self.AwsDashboardPage.run_simulations_without_wait()

        app_driver.assertExists('//MDRaisedButton[@text="Warmup"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDRaisedButton[@text="Warmup"]', TestData.TIMEOUT)
        app_driver.sleep(5)
        app_driver.assertExists('//MDRaisedButton[@text="Stop Warmup"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDRaisedButton[@text="Stop Warmup"]', TestData.TIMEOUT)
        app_driver.sleep(3)
        text = f"{datetime.now().strftime('%m/%d/%y %H:%M:%S')}-Automation"
        app_driver.setattr("//MDTextField", "text", "")
        app_driver.setattr("//MDTextField", "text", text)
        app_driver.wait_click('//MDRaisedButton[@text="Start"]', TestData.TIMEOUT)
        app_driver.sleep(5)
        app_driver.wait_click('//MDRaisedButton[@text="Stop"]', TestData.TIMEOUT)
        app_driver.assertExists('//MDNavigationRailItem[@text="Export Data"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDNavigationRailItem[@text="Export Data"]', TestData.TIMEOUT)
        app_driver.sleep(5)
        app_driver.assertExists('//MDLabel[@text="Selected 0"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDLabel[@text="Selected 0"]', TestData.TIMEOUT)

        app_driver.wait_click('//MDNavigationRailItem[@text="Connect"]', TestData.TIMEOUT)
        app_driver.wait_click('//MDRaisedButton[@text="Disconnect"]', TestData.TIMEOUT)

    def test_2(self):
        app_driver = connect()
        # app_driver.wait_click('//MDNavigationRailItem[@text="Export Data"]', TestData.TIMEOUT)
        # print(app_driver.select('//MDNavigationRailItem[@text="Export Data"]'))
        # print(app_driver.version())
        # print(app_driver.select('//MDGridLayout/MDBoxLayout[1]'))
        # app_driver.wait_click('//MDGridLayout/MDBoxLayout[1]', TestData.TIMEOUT)

        app_driver.wait("//MDGridLayout/MDBoxLayout[1]")
        a = app_driver.execute("app.root.children[0].status_label")
        b = app_driver.execute("app.root.children[1].children[1].id")

        # app_driver.evaluate_and_store("root", "app.set_screen('export')")
        # a = app_driver.execute("root.Exporter")

        # b = app_driver.execute("app.root.children[1].manager")


        print(a)
        print(b)

    def test_4(self):
        self.Simulator = Simulator(self.driver)
        self.Simulator.select_port()
        self.Simulator.start()
        self.EarthOpticsDataCollector = EarthOpticsDataCollector()
        self.EarthOpticsDataCollector.connect()
        self.EarthOpticsDataCollector.go_to_connect_tab()
        self.EarthOpticsDataCollector.click_on_connect_all_button()
        self.Simulator.wait(5)
        self.EarthOpticsDataCollector.click_on_disconnect_all_button()
        self.Simulator.stop()




