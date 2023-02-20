from selenium.webdriver.common.by import By
from Browser.Pages.BasePage import BasePage


class Calculator(BasePage):

    OneButton = (By.NAME, "One")

    def __init__(self, driver):
        super().__init__(driver)

    def click_one_button(self):
        self.do_click(self.OneButton)
