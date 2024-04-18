import pytest
from playwright.sync_api import sync_playwright
from .product_page import ProductPage




url = "https://petslike.ua/"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def product_page(page):
    page.goto('https://petslike.ua/olenina-z-m-iasom-kurki-konservi-dlia-kotiv')
    yield ProductPage(page)