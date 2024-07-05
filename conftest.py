import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import URL


@pytest.fixture(params=["chrome", "firefox"])
def web_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.set_window_size(1280, 720)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        driver.set_window_size(1280, 720)
    else:
        raise TypeError("Driver is not found")

    driver.get(URL)
    yield driver
    driver.quit()