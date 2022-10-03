from Config.Config import TestData
from Browser.Pages.LoginPage import LoginPage
from Browser.Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_1(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.goToUrl(TestData.BASE_URL)
        flag = self.LoginPage.is_signup_link_exist()
        assert flag, "something "

    def test_2(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.goToUrl(TestData.BASE_URL)
        self.LoginPage.get_title(TestData.TITLE)
