from decouple import config
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
