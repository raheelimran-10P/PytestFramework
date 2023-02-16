import pytest
from appium import webdriver


@pytest.fixture()
def setup(request):
    desired_caps = {
        "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    }
    app_driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps, direct_connection=False)
    request.cls.driver = app_driver
    yield
    app_driver.quit()
