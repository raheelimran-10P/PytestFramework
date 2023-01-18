import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Browser.Pages.BasePage import BasePage
import os

from Browser.TestData.TestData import TestData


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
    SIMULATION_LINK = (By.XPATH, "(//a[@href='/simulations'])[2]")
    CREATE_SIMULATION = (By.XPATH, "//a[@href=\"/simulations/create\"]")
    SIMULATION_NAME = (By.ID, "name")
    SIMULATION_TYPE = (By.ID, "type")
    DEVICE_TYPE = (By.ID, "typeId")
    NUMBER_OF_DEVICE = (By.ID, "amount")
    DATA_TRANSMISSION_INTERVAL = (By.ID, "interval")
    DATA_TRANSMISSION_DURATION = (By.ID, "duration")
    SIMULATION_SAVE = (By.XPATH, "//button[@type=\"submit\"]")
    SIMULATION_EMI = (By.XPATH, "//td[text()=\"EMI\"]")
    SIMULATION_GPS = (By.XPATH, "//td[text()=\"GPS\"]")
    SIMULATION_GPR = (By.XPATH, "//td[text()=\"GPR\"]")
    SIMULATION_CHECK_ALL = (By.ID, "all")
    SIMULATION_CHECK_GPS = (By.XPATH, "//td[text()='GPS']/../td/div/input")
    SIMULATION_CHECK_EMI = (By.XPATH, "//td[text()='EMI']/../td/div/input")
    SIMULATION_CHECK_GPR = (By.XPATH, "//td[text()='GPR']/../td/div/input")
    SIMULATION_START = (By.CSS_SELECTOR,
                        "#root > div > div > div:nth-child(2) > div > div > div.content-card-title.card-title.h5 > button:nth-child(4)")
    SIMULATION_REFRESH = (By.CSS_SELECTOR,
                          "#root > div > div > div:nth-child(2) > div > div > div.content-card-title.card-title.h5 > button:nth-child(1)")
    SIMULATION_SLEEPING_GPS = (By.XPATH, "//td[text()='GPS']/../td[text()='sleeping']")
    SIMULATION_SLEEPING_EMI = (By.XPATH, "//td[text()='EMI']/../td[text()='sleeping']")
    SIMULATION_SLEEPING_GPR = (By.XPATH, "//td[text()='GPR']/../td[text()='sleeping']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_page_title(self, title):
        return self.get_title(title)

    def go_to_device_type(self):
        self.do_click(self.DEVICE_TYPE_LINK)

    def create_device_types(self, emi=True, gps=True, gpr=True):
        os.chdir("../")
        if emi:
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
        if gpr:
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
        if gps:
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

    def go_to_simulation(self):
        self.do_click(self.SIMULATION_LINK)

    def create_simulation(self, emi=True, gps=True, gpr=True):
        if emi:
            try:
                self.is_visible(self.SIMULATION_EMI)
            except:
                self.is_visible(self.CREATE_SIMULATION)
                self.do_click(self.CREATE_SIMULATION)
                self.is_visible(self.SIMULATION_NAME)
                self.do_send_key(self.SIMULATION_NAME, "EMI")
                self.is_visible(self.SIMULATION_TYPE)
                self.select_by_visible_text(self.SIMULATION_TYPE, "User created")
                self.is_visible(self.DEVICE_TYPE)
                self.select_by_visible_text(self.DEVICE_TYPE, "EMI")
                self.is_visible(self.NUMBER_OF_DEVICE)
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.CONTROL + 'a')
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.DELETE)
                self.do_send_key(self.NUMBER_OF_DEVICE, TestData.NUMBER_OF_DEVICE)
                self.is_visible(self.DATA_TRANSMISSION_INTERVAL)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, TestData.DATA_TRANSMISSION_INTERVAL_SECONDS)
                self.is_visible(self.DATA_TRANSMISSION_DURATION)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, TestData.DATA_TRANSMISSION_DURATION_SECONDS)
                self.is_visible(self.SIMULATION_SAVE)
                self.do_click(self.SIMULATION_SAVE)
                self.is_visible(self.SIMULATION_EMI)
        if gps:
            try:
                self.is_visible(self.SIMULATION_GPS)
            except:
                self.is_visible(self.CREATE_SIMULATION)
                self.do_click(self.CREATE_SIMULATION)
                self.is_visible(self.SIMULATION_NAME)
                self.do_send_key(self.SIMULATION_NAME, "GPS")
                self.is_visible(self.SIMULATION_TYPE)
                self.select_by_visible_text(self.SIMULATION_TYPE, "User created")
                self.is_visible(self.DEVICE_TYPE)
                self.select_by_visible_text(self.DEVICE_TYPE, "GPS")
                self.is_visible(self.NUMBER_OF_DEVICE)
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.CONTROL + 'a')
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.DELETE)
                self.do_send_key(self.NUMBER_OF_DEVICE, TestData.NUMBER_OF_DEVICE)
                self.is_visible(self.DATA_TRANSMISSION_INTERVAL)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, TestData.DATA_TRANSMISSION_INTERVAL_SECONDS)
                self.is_visible(self.DATA_TRANSMISSION_DURATION)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, TestData.DATA_TRANSMISSION_DURATION_SECONDS)
                self.is_visible(self.SIMULATION_SAVE)
                self.do_click(self.SIMULATION_SAVE)
                self.is_visible(self.SIMULATION_GPS)
        if gpr:
            try:
                self.is_visible(self.SIMULATION_GPR)
            except:
                self.is_visible(self.CREATE_SIMULATION)
                self.do_click(self.CREATE_SIMULATION)
                self.is_visible(self.SIMULATION_NAME)
                self.do_send_key(self.SIMULATION_NAME, "GPR")
                self.is_visible(self.SIMULATION_TYPE)
                self.select_by_visible_text(self.SIMULATION_TYPE, "User created")
                self.is_visible(self.DEVICE_TYPE)
                self.select_by_visible_text(self.DEVICE_TYPE, "GPR")
                self.is_visible(self.NUMBER_OF_DEVICE)
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.CONTROL + 'a')
                self.do_send_key(self.NUMBER_OF_DEVICE, Keys.DELETE)
                self.do_send_key(self.NUMBER_OF_DEVICE, 1)
                self.is_visible(self.DATA_TRANSMISSION_INTERVAL)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_INTERVAL, 2)
                self.is_visible(self.DATA_TRANSMISSION_DURATION)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.CONTROL + 'a')
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, Keys.DELETE)
                self.do_send_key(self.DATA_TRANSMISSION_DURATION, 80)
                self.is_visible(self.SIMULATION_SAVE)
                self.do_click(self.SIMULATION_SAVE)
                self.is_visible(self.SIMULATION_GPR)

    def run_simulations(self):
        self.is_visible(self.SIMULATION_REFRESH)
        self.do_click(self.SIMULATION_REFRESH)
        # self.is_visible(self.SIMULATION_CHECK_ALL)
        # self.checked_box(self.SIMULATION_CHECK_ALL)
        self.do_click(self.SIMULATION_CHECK_EMI)
        self.do_click(self.SIMULATION_CHECK_GPS)
        self.do_click(self.SIMULATION_CHECK_GPR)
        self.is_visible(self.SIMULATION_START)
        self.do_click(self.SIMULATION_START)
        self.wait()
        self.is_visible(self.SIMULATION_REFRESH)
        self.do_click(self.SIMULATION_REFRESH)
        try:
            self.is_visible(self.SIMULATION_SLEEPING_EMI, TestData.DATA_TRANSMISSION_DURATION_SECONDS)
            self.is_visible(self.SIMULATION_SLEEPING_GPS, TestData.DATA_TRANSMISSION_DURATION_SECONDS)
            self.is_visible(self.SIMULATION_SLEEPING_GPR, TestData.DATA_TRANSMISSION_DURATION_SECONDS)
        except:
            self.is_visible(self.SIMULATION_REFRESH)
            self.do_click(self.SIMULATION_REFRESH)
            self.wait()
            self.is_visible(self.SIMULATION_SLEEPING_EMI)
            self.is_visible(self.SIMULATION_SLEEPING_GPS)
            self.is_visible(self.SIMULATION_SLEEPING_GPR)
