from Browser.Pages.DashboardPage import DashboardPage
from Browser.TestData.TestData import TestData
from Browser.Tests.test_base import BaseTest


class TestDashboardPage(BaseTest):

    def test_1(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(TestData.BASE_URL)
        flag = self.DashboardPage.is_control_text_exist()
        assert flag, "something "

    def test_2(self):
        self.DashboardPage = DashboardPage(self.driver)
        self.DashboardPage.goToUrl(TestData.BASE_URL)
        self.DashboardPage.get_title(TestData.TITLE)
