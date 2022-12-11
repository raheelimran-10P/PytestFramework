from decouple import config
from Browser.Pages.AwsLoginPage import AwsLoginPage
from Browser.Pages.DashboardPage import DashboardPage
from Browser.TestData.TestData import TestData
from Browser.Tests.test_base import BaseTest


class TestDashboardPage(BaseTest):

    def test_1(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(config('BASE_URL'))
        self.DashboardPage.get_title(TestData.TITLE)

    def test_2(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(config('BASE_URL'))
        control = self.DashboardPage.is_visible(self.DashboardPage.CONTROL_TEXT)
        assert control == True

    def test_3(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(config('BASE_URL'))
        geophex = self.DashboardPage.is_visible(self.DashboardPage.GEOPHEXMOCK_TEXT)
        assert geophex == True

        idsgpr = self.DashboardPage.is_visible(self.DashboardPage.IDSGPRMOCKk_TEXT)
        assert idsgpr == True

        mlmodel = self.DashboardPage.is_visible(self.DashboardPage.MLMODELDEVICE_TEXT)
        assert mlmodel == True

    def test_4(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(config('BASE_URL'))
        geophex = self.DashboardPage.is_visible(self.DashboardPage.GEOPHEXMOCK_TEXT)
        assert geophex == True

        idsgpr = self.DashboardPage.is_visible(self.DashboardPage.IDSGPRMOCKk_TEXT)
        assert idsgpr == True

        mlmodel = self.DashboardPage.is_visible(self.DashboardPage.MLMODELDEVICE_TEXT)
        assert mlmodel == True

        # Connect the Geophex device
        self.DashboardPage.is_visible(self.DashboardPage.GEOPHEXMOCK_CONNECT)
        self.DashboardPage.do_click(self.DashboardPage.GEOPHEXMOCK_CONNECT)

        # Connect the Idsgpr device
        self.DashboardPage.is_visible(self.DashboardPage.IDSGPRMOCKk_CONNECT)
        self.DashboardPage.do_click(self.DashboardPage.IDSGPRMOCKk_CONNECT)

        # Add values in Collection Name field
        self.DashboardPage.is_visible(self.DashboardPage.COLLECTION_NAME_FIELD)
        self.DashboardPage.do_send_key(self.DashboardPage.COLLECTION_NAME_FIELD, "Name")

        # Add values in Collection Notes field
        self.DashboardPage.is_visible(self.DashboardPage.COLLECTION_NOTES_FIELD)
        self.DashboardPage.do_send_key(self.DashboardPage.COLLECTION_NOTES_FIELD, "Notes")

        # Start the collection
        self.DashboardPage.is_visible(self.DashboardPage.COLLECTION_START)
        self.DashboardPage.do_click(self.DashboardPage.COLLECTION_START)

        # Store the ID of the first tab
        window_1 = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Open new tab and switch to it
        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.openNewTab()
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.get_title("IoT Device Simulator")

        # self.DashboardPage.switchTab(window_1)

    def test_5(self):
        self.AwsLoginPage = AwsLoginPage(self.driver)
        self.AwsLoginPage.goToUrl(config('AWS_IOT_URL'))
        self.AwsLoginPage.set_username(config('AWS_IOT_USERNAME'))
        
