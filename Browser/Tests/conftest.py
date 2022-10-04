import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    options = Options()
    options.add_argument("start-maximized")
    #if request.param == "Chrome":
    #web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #if request.param == "Firefox":
    #    web_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    #web_driver.implicitly_wait(10)
    yield
    web_driver.quit()


