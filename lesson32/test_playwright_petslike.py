import pytest


@pytest.mark.regression_playwright
def test_check_search(product_page):
    product_page.search_something('purina')
    product_page.check_header_on_search_page('Пошук товарів')


@pytest.mark.regression_playwright
def test_check_header(product_page):
    product_page.check_header("Baskerville Оленина з м'ясом курки Консерви для котів")

@pytest.mark.regression_playwright
def test_add_pack(product_page):
    product_page.add_pack_of_products()
    product_page.check_expected_amount_added(6)