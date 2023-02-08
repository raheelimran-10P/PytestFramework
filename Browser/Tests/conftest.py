import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


@pytest.fixture(params=["chrome"])
def init_driver(request):
    options = Options()
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    # if request.param == "Chrome":
    try:
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    except:
        web_driver = webdriver.Chrome(service=Service(), options=options)

    # web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    # if request.param == "Firefox":
    # web_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    request.cls.driver = webdriver.Chrome(options=chrome_options)

    yield request.cls.driver
    request.cls.driver.close()
