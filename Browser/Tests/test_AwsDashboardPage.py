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
from Utilities.script_01_check_exported_data import script_01_check_exported_data


class TestAwsDashboardPage(BaseTest):

    @pytest.mark.skip(reason="project setup locally (not hosted on any server)")
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
        # self.AwsDashboardPage.run_simulations()

    @pytest.mark.skip(reason="project setup locally (not hosted on any server)")
    def test_7(self):
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

    @pytest.mark.skip(reason="project setup locally (not hosted on any server)")
    def test_8(self):
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, True, True)

    @pytest.mark.parametrize("before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req, after_sensor_inuse_flag", [
        (True, True, False, False)
    ])
    def test_9(self, before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req, after_sensor_inuse_flag):
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, before_data_storage_req, before_sensor_inuse_flag)
        aws_ConsoleDashboardPage = self.driver.current_window_handle
        self.AwsConsoleDashboardPage.openNewTab()
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
        aws_DashboardPage = self.driver.current_window_handle
        self.AwsDashboardPage.switchTab(aws_ConsoleDashboardPage)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, after_data_storage_req, after_sensor_inuse_flag)
        self.AwsConsoleDashboardPage.wait(10)

        object_01 = script_01_check_exported_data()

        print(TestData.EMI_KEYWORD_IN_EXPORT_DATA,
              object_01.is_data_exported(TestData.APPDATA_PATH, TestData.EMI_KEYWORD_IN_EXPORT_DATA))
        print(TestData.GPS_KEYWORD_IN_EXPORT_DATA,
              object_01.is_data_exported(TestData.APPDATA_PATH, TestData.GPS_KEYWORD_IN_EXPORT_DATA))
        print(TestData.MLMODEL_KEYWORD_IN_EXPORT_DATA,
              object_01.is_data_exported(TestData.APPDATA_PATH, TestData.MLMODEL_KEYWORD_IN_EXPORT_DATA))
        print(TestData.IDSGPR_KEYWORD_IN_EXPORT_DATA,
              object_01.is_data_exported(TestData.APPDATA_PATH, TestData.IDSGPR_KEYWORD_IN_EXPORT_DATA))

        if (object_01.is_data_exported(TestData.APPDATA_PATH, TestData.EMI_KEYWORD_IN_EXPORT_DATA)) and \
                (object_01.is_data_exported(TestData.APPDATA_PATH, TestData.GPS_KEYWORD_IN_EXPORT_DATA)) and \
                (object_01.is_data_exported(TestData.APPDATA_PATH, TestData.MLMODEL_KEYWORD_IN_EXPORT_DATA)) and \
                (object_01.is_data_exported(TestData.APPDATA_PATH, TestData.IDSGPR_KEYWORD_IN_EXPORT_DATA)):
            print("Exported data is verified!")
            object_01.delete_all__exported_date(TestData.APPDATA_PATH)
            print("Deleted all export data!")

        else:
            raise Exception("Exported data is not verified!")
            object_01.delete_all__exported_date(path)
            print("Deleted all export data!")

        os.remove(TestData.APPSTATE_FILE_PATH)
