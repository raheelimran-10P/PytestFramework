from selenium.webdriver.common.by import By
from Browser.Pages.BasePage import BasePage


class DashboardPage(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    CONTROL_TEXT = (By.XPATH, "//h1[text()='Controls']")
    COLLECTION_TEXT = (By.XPATH, "//h1[text()='Collections']")
    GEOPHEXMOCK_TEXT = (By.XPATH, "//label[text()='GeophexMock']")
    IDSGPRMOCKk_TEXT = (By.XPATH, "//label[text()='IDSGPRMock']")
    MLMODELDEVICE_TEXT = (By.XPATH, "//label[text()='MLModelDevice']")
    GEOPHEXMOCK_CONNECT = (By.XPATH, "//label[text()='GeophexMock']/following-sibling::button[1]")
    IDSGPRMOCKk_CONNECT = (By.XPATH, "//label[text()='IDSGPRMock']/following-sibling::button[1]")
    MLMODELDEVICE_CONNECT = (By.XPATH, "//label[text()='MLModelDevice']/following-sibling::button[1]")
    COLLECTION_NAME_FIELD = (By.XPATH, "//input[@id='filled-basic']")
    COLLECTION_NOTES_FIELD = (By.XPATH, "//input[@id='filled-basic-notes']")
    COLLECTION_START = (By.XPATH, "//div[@class='collection']/button[1]")
    COLLECTION_STOP = (By.XPATH, "//div[@class='collection']/button[2]")
    COLLECTION_SUBMIT = (By.XPATH, "//div[@class='collection']/button[3]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_key(self, username)
        self.do_send_key(self, password)
        self.do_click(self.LOGIN_BUTTON)

