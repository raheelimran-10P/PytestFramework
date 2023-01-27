import os
import time
import pytest
from decouple import config

from Browser.Pages.AwsConsoleDashboardPage import AwsConsoleDashboardPage
from Browser.Pages.AwsConsoleLoginPage import AwsConsoleLoginPage
from Browser.Pages.AwsDashboardPage import AwsDashboardPage
from Browser.Pages.AwsLoginPage import AwsLoginPage
from Browser.Pages.DashboardPage import DashboardPage
from Browser.TestData.TestData import TestData
from Browser.Tests.test_base import BaseTest
from Utilities.script_01 import script_01


class TestAwsDashboardPage(BaseTest):

    def test_6(self):
        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.login(config('AWS_IOT_USERNAME'), config('AWS_IOT_PASSWORD'))

        self.AwsDashboardPage = AwsDashboardPage(self.driver)
        self.AwsDashboardPage.get_title('IoT Device Simulator')
        self.AwsDashboardPage.go_to_device_type()
        self.AwsDashboardPage.create_device_types()
        self.AwsDashboardPage.go_to_simulation()
        self.AwsDashboardPage.create_simulation()
        self.AwsDashboardPage.run_simulations()

    def test_7(self):
        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.login(config('AWS_IOT_USERNAME'), config('AWS_IOT_PASSWORD'))

        self.AwsDashboardPage = AwsDashboardPage(self.driver)
        self.AwsDashboardPage.get_title('IoT Device Simulator')
        # self.AwsDashboardPage.go_to_device_type()
        # self.AwsDashboardPage.create_device_types()
        self.AwsDashboardPage.go_to_simulation()
        # self.AwsDashboardPage.create_simulation()
        self.AwsDashboardPage.run_simulations()

    def test_8(self):
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'), config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, True, True)

    def test_9(self):
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, True, True)
        aws_ConsoleDashboardPage = self.driver.current_window_handle
        self.AwsConsoleDashboardPage.openNewTab()

        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.login(config('AWS_IOT_USERNAME'), config('AWS_IOT_PASSWORD'))

        self.AwsDashboardPage = AwsDashboardPage(self.driver)
        self.AwsDashboardPage.get_title('IoT Device Simulator')
        # self.AwsDashboardPage.go_to_device_type()
        # self.AwsDashboardPage.create_device_types()
        self.AwsDashboardPage.go_to_simulation()
        # self.AwsDashboardPage.create_simulation()
        self.AwsDashboardPage.run_simulations()
        aws_DashboardPage = self.driver.current_window_handle
        self.AwsDashboardPage.switchTab(aws_ConsoleDashboardPage)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, False, False)
        self.AwsConsoleDashboardPage.wait(10)

        object_01 = script_01()
        path = "/media/raheel/22687D06687CD9CD/projects/groundowl-app/appData/"
        text_01 = "mock_geophex_v2_raw_emi"
        text_02 = "mock_geophex_v2_raw_gps"
        text_03 = "mock_ml_model_v1_till_depth"
        text_04 = "IDSGPRMock"

        print(text_01, object_01.is_data_exported(path, text_01))
        print(text_02, object_01.is_data_exported(path, text_02))
        print(text_03, object_01.is_data_exported(path, text_03))
        print(text_04, object_01.is_data_exported(path, text_04))

        if (object_01.is_data_exported(path, text_01)) and (object_01.is_data_exported(path, text_02)) and (
                object_01.is_data_exported(path, text_03)) and (object_01.is_data_exported(path, text_04)):
            print("all passed")

        else:
            raise Exception
            print("not all passed")




