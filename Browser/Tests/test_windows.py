import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def init_driver2(request):
    request.cls.driver = __get_driver('calc')
    yield
    request.cls.driver.quit()

def __get_driver(app_name):
    desired_caps = {}
    if app_name == 'calc':
        desired_caps['app'] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)
    return driver


@pytest.mark.usefixtures("init_driver2")
@pytest.mark.skip(reason="Just for testing")
def skip_test_01(self):
    pass
