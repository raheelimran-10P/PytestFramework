from telenium import connect

from Window.TestData.TestData import TestData


class EarthOpticsDataCollector:
    app_driver = None
    connect_tab_xpath = '//MDNavigationRailItem[@text="Connect"]'
    connect_all_xpath = '//MDFillRoundFlatIconButton[@text="Connect All"]'
    disconnect_all_xpath = '//MDFillRoundFlatIconButton[@text="Disconnect All"]'

    def connect(self):
        self.app_driver = connect()

    def go_to_connect_tab(self):
        self.app_driver.wait_click(self.connect_tab_xpath, TestData.TIMEOUT)

    def click_on_connect_all_button(self):
        self.app_driver.wait_click(self.connect_all_xpath, TestData.TIMEOUT)

    def click_on_disconnect_all_button(self):
        self.app_driver.wait_click(self.disconnect_all_xpath, TestData.TIMEOUT)

