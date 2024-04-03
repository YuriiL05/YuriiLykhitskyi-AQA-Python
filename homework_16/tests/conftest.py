import pytest
from selenium.webdriver import Chrome

from homework_16.pages.dashboard_page import DashboardPage
from homework_16.pages.home_page import HomePage
from homework_16.pages.product_page import ProductPage
from homework_16.pages.search_page import SearchPage


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
    yield DashboardPage(driver)


@pytest.fixture
def iphone_14_256_midnight(driver):
    driver.get('https://compservice.in.ua/product/5224991.html')
    yield ProductPage(driver)


@pytest.fixture
def dashboard(driver):
    yield DashboardPage(driver)


@pytest.fixture
def product(driver):
    yield ProductPage(driver)


@pytest.fixture
def search_dashboard(driver):
    yield SearchPage(driver)