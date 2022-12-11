from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Browser.Pages.BasePage import BasePage


class AwsLoginPage(BasePage):

    USERNAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_page_title(self, title):
        return self.get_title(title)

    def set_username(self, username):

        shadow_host1 = self.driver.find_element(By.TAG_NAME, "amplify-authenticator")
        shadow_root1 = shadow_host1.shadow_root
        shadow_content1 = shadow_root1.find_element(By.CLASS_NAME, "auth-container")

        shadow_host2 = shadow_content1.find_element(By.TAG_NAME, "amplify-sign-in")
        shadow_root2 = shadow_host2.shadow_root

        shadow_content2 = shadow_root2.find_element(By.CLASS_NAME, "input")
        shadow_content2.send_keys(username)

        #self.do_send_key(self, username)
        #self.do_send_key(self, password)
        #self.do_click(self.LOGIN_BUTTON)

