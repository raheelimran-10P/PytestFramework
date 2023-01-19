from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Browser.Pages.BasePage import BasePage


class AwsConsoleLoginPage(BasePage):
    IAM_USER_RADIO_BUTTON = (By.ID, "iam_user_radio_button")
    ACCOUNT_ID_FIELD = (By.XPATH, "//input[@id='resolving_input']")
    NEXT_BUTTON = (By.ID, "next_button")
    IAM_USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGNIN_BUTTON = (By.ID, "signin_button")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[@data-testid='subscribeButton']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_console_page_title(self, title):
        return self.get_title(title)

    def login(self, account_id, username, password):
        self.is_visible(self.IAM_USER_RADIO_BUTTON)
        self.do_click(self.IAM_USER_RADIO_BUTTON)
        self.is_visible(self.ACCOUNT_ID_FIELD)
        self.do_send_key(self.ACCOUNT_ID_FIELD, account_id)
        self.is_visible(self.NEXT_BUTTON)
        self.do_click(self.NEXT_BUTTON)
        self.is_visible(self.IAM_USERNAME_FIELD)
        self.do_send_key(self.IAM_USERNAME_FIELD, username)
        self.is_visible(self.PASSWORD_FIELD)
        self.do_send_key(self.PASSWORD_FIELD, password)
        self.is_visible(self.SIGNIN_BUTTON)
        self.do_click(self.SIGNIN_BUTTON)
        self.is_visible(self.SUBSCRIBE_BUTTON)



