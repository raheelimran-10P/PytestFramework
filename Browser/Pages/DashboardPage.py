from selenium.webdriver.common.by import By
from Browser.Pages.BasePage import BasePage


class DashboardPage(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    CONTROL_TEXT = (By.XPATH, "//h1[text()='Controls']")
    GEOPHEXMOCK_TEXT = (By.XPATH, "//label[text()='GeophexMock']")
    IDSGPRMOCKk_TEXT = (By.XPATH, "//label[text()='IDSGPRMock']")
    MLMODELDEVICE_TEXT = (By.XPATH, "//label[text()='MLModelDevice']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_key(self, username)
        self.do_send_key(self, password)
        self.do_click(self.LOGIN_BUTTON)

