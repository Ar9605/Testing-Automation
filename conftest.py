import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
