from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import  pytest

@pytest.fixture(scope="class")
def setup(request,browser,enviroment):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))
    else:
        print("Tarayıcı ismini doğru giriniz")




    driver.get("https://www.trendyol.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")
