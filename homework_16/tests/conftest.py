import pytest
from selenium.webdriver import Chrome

from homework_16.pages.home_page import HomePage
from homework_16.pages.mobile_phones_page import MobilePhonesPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    driver.get('https://compservice.in.ua')
    yield HomePage(driver)


@pytest.fixture
def phones(driver):
    driver.get('https://compservice.in.ua/catalogue/59-mobilni-telefoni.html')
    yield MobilePhonesPage(driver)

