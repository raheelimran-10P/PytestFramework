
import pytest

from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_1(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.goToUrl(TestData.BASE_URL)
        flag = self.LoginPage.is_signup_link_exist()
        assert flag

    def test_2(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.get_title(TestData.TITLE)


