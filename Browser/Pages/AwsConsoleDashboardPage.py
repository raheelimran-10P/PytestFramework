from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Browser.Pages.BasePage import BasePage
from Browser.TestData.TestData import TestData


class AwsConsoleDashboardPage(BasePage):
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[@data-testid='subscribeButton']")
    TOPIC_FILTER_FIELD = (By.XPATH, "//input[@name='topicFilter']")
    ADDITIONAL_CONFIGURATION = (By.XPATH, "//div[text()='Additional configuration']")
    QUALITY_OF_SERVICE_1_RADIO_BUTTON = (By.XPATH,
                                         "//*[text()='Quality of Service 1 - Message will be delivered at least once']/parent::span/parent::label/span[1]")
    PUBLISH_TO_A_TOPIC_TAB = (By.XPATH, "//h2[text()='Publish to a topic']")
    TOPIC_NAME_FIELD = (By.XPATH, "//input[@name='topic']")
    PUBLISH_BUTTON = (By.XPATH, "//button[@data-testid='publishButton']")
    MESSAGE_PAYLOAD_FIELD = (By.XPATH, "//textarea[@name='message']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_console_dashboard_page_title(self, title):
        return self.get_title(title)

    def subscribe_to_a_topic(self, topic_filter):
        self.is_visible(self.TOPIC_FILTER_FIELD)
        self.do_send_key(self.TOPIC_FILTER_FIELD, topic_filter)
        self.is_visible(self.ADDITIONAL_CONFIGURATION)
        self.do_click(self.ADDITIONAL_CONFIGURATION)
        self.is_visible(self.QUALITY_OF_SERVICE_1_RADIO_BUTTON)
        self.do_click(self.QUALITY_OF_SERVICE_1_RADIO_BUTTON)
        self.is_visible(self.ADDITIONAL_CONFIGURATION)
        self.do_click(self.ADDITIONAL_CONFIGURATION)
        self.is_visible(self.SUBSCRIBE_BUTTON)
        self.do_click(self.SUBSCRIBE_BUTTON)

    def publish_to_a_topic(self, topic_name, data_storage_req=False, sensor_inuse_flag=False):
        self.is_visible(self.PUBLISH_TO_A_TOPIC_TAB)
        self.do_click(self.PUBLISH_TO_A_TOPIC_TAB)
        self.is_visible(self.TOPIC_NAME_FIELD)
        self.do_send_key(self.TOPIC_NAME_FIELD, Keys.CONTROL + 'a')
        self.do_send_key(self.TOPIC_NAME_FIELD, Keys.DELETE)
        self.do_send_key(self.TOPIC_NAME_FIELD, topic_name)
        self.is_visible(self.MESSAGE_PAYLOAD_FIELD)
        self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, Keys.CONTROL + 'a')
        self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, Keys.DELETE)
        if data_storage_req == True and sensor_inuse_flag == True:
            self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, TestData.MESSAGE_PAYLOAD_04)
        elif data_storage_req == False and sensor_inuse_flag == True:
            self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, TestData.MESSAGE_PAYLOAD_02)
        elif data_storage_req == True and sensor_inuse_flag == False:
            self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, TestData.MESSAGE_PAYLOAD_03)
        else:
            self.do_send_key(self.MESSAGE_PAYLOAD_FIELD, TestData.MESSAGE_PAYLOAD_01)
        self.is_visible(self.ADDITIONAL_CONFIGURATION)
        self.do_click(self.ADDITIONAL_CONFIGURATION)
        self.is_visible(self.QUALITY_OF_SERVICE_1_RADIO_BUTTON)
        self.do_click(self.QUALITY_OF_SERVICE_1_RADIO_BUTTON)
        self.is_visible(self.ADDITIONAL_CONFIGURATION)
        self.do_click(self.ADDITIONAL_CONFIGURATION)
        self.is_visible(self.PUBLISH_BUTTON)
        self.do_click(self.PUBLISH_BUTTON)
