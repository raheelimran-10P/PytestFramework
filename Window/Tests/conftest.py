import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
# from selenium import webdriver
from Window.TestData.TestData import TestData
import os
from appium import webdriver


@pytest.fixture()
def setup(request):
    os.startfile(TestData.WIN_APP_DRIVER_EXE_DIR)
    time.sleep(3)
    desired_caps = {
        "app": TestData.SIMULATOR_EXE_DIR
    }
    app_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)
    request.cls.driver = app_driver
    yield
    app_driver.quit()
    terminate(TestData.WIN_APP_DRIVER_EXE)
    terminate(TestData.SIMULATOR_EXE_DIR)


def terminate(process_name):
    os.system('taskkill /IM "' + process_name + '" /F')


# @pytest.fixture(params=["chrome"])
# def setup(request):
#     options = Options()
#     options.add_argument("start-maximized")
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-extensions")
#     # if request.param == "Chrome":
#     try:
#         web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     except:
#         web_driver = webdriver.Chrome(service=Service(), options=options)
#
#     # web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
#     # if request.param == "Firefox":
#     # web_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(10)
#     yield web_driver
#     web_driver.quit()
