import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def chrome():
    with  webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        driver.set_window_size(1920, 1080)
        yield driver
