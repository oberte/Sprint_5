# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    _driver = webdriver.Chrome(options=chrome_options)
    yield _driver
    _driver.quit()


@pytest.fixture(scope="module")
def user_credentials():
    return {"email": "marinaorangkhadivi3111@test.te", "password": "123456"}