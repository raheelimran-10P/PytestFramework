from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Browser.Pages.BasePage import BasePage


class AwsLoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    DEVICE_TYPE_LINK = (By.XPATH, "//a[@href='/device-types']")
    DEVICE_FILTER = (By.XPATH, "//div[text()=' (']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_page_title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        shadow_host1 = self.driver.find_element(By.TAG_NAME, "amplify-authenticator")
        shadow_root1 = shadow_host1.shadow_root
        shadow_content1 = shadow_root1.find_element(By.CLASS_NAME, "auth-container")

        shadow_host2 = shadow_content1.find_element(By.TAG_NAME, "amplify-sign-in")
        shadow_root2 = shadow_host2.shadow_root

        shadow_content_input = shadow_root2.find_elements(By.CLASS_NAME, "input")
        shadow_content_input[0].send_keys(username)
        shadow_content_input[1].send_keys(password)

        shadow_content_button = shadow_root2.find_elements(By.CLASS_NAME, "button")
        shadow_content_button[1].click()
        self.is_visible(self.DEVICE_TYPE_LINK)
        self.is_visible(self.DEVICE_FILTER)


