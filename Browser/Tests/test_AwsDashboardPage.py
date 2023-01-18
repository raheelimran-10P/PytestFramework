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
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, TestData.MESSAGE_PAYLOAD)

