import time

import pytest
from appium import webdriver
from Window.TestData.TestData import TestData
import os


@pytest.fixture()
def setup(request):
    # os.startfile(TestData.WIN_APP_DRIVER_EXE_DIR)
    # time.sleep(3)
    # desired_caps = {
    #     "app": TestData.COLLECTOR_EXE_DIR
    # }
    # app_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps,
    #                               direct_connection=False)
    # request.cls.driver = app_driver
    # yield
    # app_driver.quit()
    # terminate(TestData.WIN_APP_DRIVER_EXE)
    pass


def terminate(process_name):
    os.system('taskkill /IM "' + process_name + '" /F')
