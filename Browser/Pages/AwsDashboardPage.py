import time

from selenium.webdriver.common.by import By

from Browser.Pages.BasePage import BasePage
import os


class AwsDashboardPage(BasePage):
    DEVICE_TYPE_LINK = (By.XPATH, "//a[@href='/device-types']")
    EMI_DEVICE_TYPE = (By.XPATH, "//td[text()='EMI']")
    EMI_TOPIC = (By.XPATH, "//td[text()='EMI_DATA']")
    CREATE_DEVICE = (By.XPATH, "//a[@href=\"/device-types/create\"]")
    FILE_UPLOAD_BUTTON = (By.CSS_SELECTOR,
                          "#root > div > div > div.content-card.card > div.content-card-title.card-title.h5 > button:nth-child(3)")
    FILE_UPLOAD = (By.XPATH, "//*[@id='fileUpload']")
    SAVE = (By.XPATH, "//*[@id=\"deviceTypeForm\"]/div[4]/button[1]")
    GPS_DEVICE_TYPE = (By.XPATH, "//td[text()='GPS']")
    GPS_TOPIC = (By.XPATH, "//td[text()='GPS_DATA']")
    GPR_DEVICE_TYPE = (By.XPATH, "//td[text()='GPR']")
    GPR_TOPIC = (By.XPATH, "//td[text()='GPR_DATA']")
    DEVICE_FILTER = (By.XPATH, "//div[text()=' (']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_page_title(self, title):
        return self.get_title(title)

    def goToDeviceType(self):
        self.do_click(self.DEVICE_TYPE_LINK)

    def createDeviceTypes(self, EMI=True, GPS=True, GPR=True):
        os.chdir("../")
        if EMI:
            try:
                self.is_visible(self.EMI_DEVICE_TYPE)
                self.is_visible(self.EMI_TOPIC)
            except:
                self.is_visible(self.CREATE_DEVICE)
                self.do_click(self.CREATE_DEVICE)
                PATH = os.path.abspath(os.curdir) + "/TestData/JsonFiles/EMI_2022_11_25-09:56:37_AM.json"
                time.sleep(3)
                self.is_visible(self.FILE_UPLOAD_BUTTON)
                self.driver.execute_script("document.getElementById(\"fileUpload\").removeAttribute(\"hidden\");")
                self.do_send_key(self.FILE_UPLOAD, PATH)
                self.is_visible(self.SAVE)
                self.do_click(self.SAVE)
                self.is_visible(self.DEVICE_FILTER)
                self.is_visible(self.EMI_DEVICE_TYPE)
                self.is_visible(self.EMI_TOPIC)
        if GPR:
            try:
                self.is_visible(self.GPR_DEVICE_TYPE)
                self.is_visible(self.GPR_TOPIC)
            except:
                self.is_visible(self.CREATE_DEVICE)
                self.do_click(self.CREATE_DEVICE)
                PATH = os.path.abspath(os.curdir) + "/TestData/JsonFiles/GPR_2022_11_25-09:57:26_AM.json"
                time.sleep(3)
                self.is_visible(self.FILE_UPLOAD_BUTTON)
                self.driver.execute_script("document.getElementById(\"fileUpload\").removeAttribute(\"hidden\");")
                self.do_send_key(self.FILE_UPLOAD, PATH)
                self.is_visible(self.SAVE)
                self.do_click(self.SAVE)
                self.is_visible(self.DEVICE_FILTER)
                self.is_visible(self.GPR_DEVICE_TYPE)
                self.is_visible(self.GPR_TOPIC)
        if GPS:
            time.sleep(3)
            try:
                self.is_visible(self.GPS_DEVICE_TYPE)
                self.is_visible(self.GPS_TOPIC)
            except:
                self.is_visible(self.CREATE_DEVICE)
                self.do_click(self.CREATE_DEVICE)
                PATH = os.path.abspath(os.curdir) + "/TestData/JsonFiles/GPS_2022_11_25-09:56:28_AM.json"
                time.sleep(3)
                self.is_visible(self.FILE_UPLOAD_BUTTON)
                self.driver.execute_script("document.getElementById(\"fileUpload\").removeAttribute(\"hidden\");")
                self.do_send_key(self.FILE_UPLOAD, PATH)
                self.is_visible(self.SAVE)
                self.do_click(self.SAVE)
                self.is_visible(self.DEVICE_FILTER)
                self.is_visible(self.GPS_DEVICE_TYPE)
                self.is_visible(self.GPS_TOPIC)
