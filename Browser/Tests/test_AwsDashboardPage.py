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

    @pytest.mark.skip(reason="Just for testing | create device type and simulator")
    def create_device_type_and_simulator(self):
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

    @pytest.mark.skip(reason="Just for testing | create device type, simulator, and run simulator")
    def create_device_type_simulator_and_run_simulator(self):
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

    @pytest.mark.skip(reason="Just for testing | subscribe and publish msg")
    def subscribe_and_publish_msg(self):
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, True, True)

    # @pytest.mark.skip(reason="Just for testing")
    @pytest.mark.parametrize(
        "before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req, after_sensor_inuse_flag", [
            (True, True, False, False),  # Test case 13
            (True, True, False, True),   # Test case 14
            (True, True, True, False)    # Test case 15
        ])
    def test_for_exported_data(self, before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req,
                               after_sensor_inuse_flag):
        object_01 = script_01_check_exported_data()
        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
        try:
            os.remove(TestData.APPSTATE_FILE_PATH)
        except:
            pass
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, before_data_storage_req,
                                                        before_sensor_inuse_flag)
        self.AwsConsoleDashboardPage.wait(10)
        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
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
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, after_data_storage_req,
                                                        after_sensor_inuse_flag)
        self.AwsConsoleDashboardPage.wait(10)

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

        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
        os.remove(TestData.APPSTATE_FILE_PATH)

        self.AwsConsoleDashboardPage.log_out()
        self.AwsConsoleDashboardPage.driver.close()
        self.AwsDashboardPage.switchTab(aws_DashboardPage)
        self.AwsDashboardPage.log_out()
        self.AwsDashboardPage.driver.close()

    # @pytest.mark.skip(reason="Just for testing")
    @pytest.mark.parametrize(
        "before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req, after_sensor_inuse_flag", [
            (False, False, False, False),  # Test case 01
            (False, False, False, True),   # Test case 02
            (False, False, True, False),   # Test case 03
            (False, False, True, True),    # Test case 04
            (False, True, False, False),   # Test case 05
            (False, True, False, True),    # Test case 06
            (False, True, True, False),    # Test case 07
            (False, True, True, True),     # Test case 08
            (True, False, False, False),   # Test case 09
            (True, False, False, True),    # Test case 10
            (True, False, True, False),    # Test case 11
            (True, False, True, True),     # Test case 12
            (True, True, True, True)       # Test case 16

        ])
    def test_for_non_exported_data(self, before_data_storage_req, before_sensor_inuse_flag, after_data_storage_req,
                                   after_sensor_inuse_flag):
        object_01 = script_01_check_exported_data()
        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
        try:
            os.remove(TestData.APPSTATE_FILE_PATH)
        except:
            pass
        self.AwsConsoleLoginPage = AwsConsoleLoginPage(self.driver)
        self.AwsConsoleLoginPage.goToUrl(config('AWS_Console_URL'))
        self.AwsConsoleLoginPage.login(config('AWS_Console_ACCOUNT_ID'), config('AWS_Console_USERNAME'),
                                       config('AWS_Console_PASSWORD'))
        self.AwsConsoleDashboardPage = AwsConsoleDashboardPage(self.driver)
        self.AwsConsoleDashboardPage.is_visible(self.AwsConsoleDashboardPage.SUBSCRIBE_BUTTON)
        self.AwsConsoleDashboardPage.subscribe_to_a_topic(TestData.TOPIC_FILTER)
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, before_data_storage_req,
                                                        before_sensor_inuse_flag)
        self.AwsConsoleDashboardPage.wait(10)
        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
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
        self.AwsConsoleDashboardPage.publish_to_a_topic(TestData.TOPIC_NAME, after_data_storage_req,
                                                        after_sensor_inuse_flag)
        self.AwsConsoleDashboardPage.wait(10)

        dir = os.listdir(TestData.APPDATA_PATH)

        # Checking if the AppData folder is empty or not
        if len(dir) == 0:
            print("Exported data is not generated!")
        else:
            raise Exception("Exported data is generated!")

        object_01.delete_all__exported_date(TestData.APPDATA_PATH)
        os.remove(TestData.APPSTATE_FILE_PATH)

        self.AwsConsoleDashboardPage.log_out()
        self.AwsConsoleDashboardPage.driver.close()
        self.AwsDashboardPage.switchTab(aws_DashboardPage)
        self.AwsDashboardPage.log_out()
        self.AwsDashboardPage.driver.close()
