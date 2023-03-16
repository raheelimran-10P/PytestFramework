from appium.webdriver.common.appiumby import AppiumBy
from Window.Pages.BasePage import BasePage


class Simulator(BasePage):

    # OneButton = (AppiumBy.NAME, "One")

    def __init__(self, driver):
        super().__init__(driver)

    def select_port(self):
        self.do_click(AppiumBy.NAME, 'Open')
        self.do_click(AppiumBy.NAME, 'COM1')

    def start(self):
        self.do_click(AppiumBy.NAME, 'Start')

    def stop(self):
        self.do_click(AppiumBy.NAME, 'Stop')
