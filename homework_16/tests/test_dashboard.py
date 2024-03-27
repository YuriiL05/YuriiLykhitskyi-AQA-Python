import pytest


@pytest.mark.parametrize('products, page_name', [
    ('phones', 'МОБІЛЬНІ ТЕЛЕФОНИ'),
    ('tablets', 'ПЛАНШЕТИ'),
    ('laptops', 'НОУТБУКИ, НЕТБУКИ')])
def test_main_categories_dashboard(home, dashboard, products, page_name):
    home.navigate_to(products)
    assert dashboard.get_name_of_page() == page_name


@pytest.mark.parametrize('brand', ['Acer', 'Apple', 'Asus'])
def test_laptops_filers(home, dashboard, brand):
    home.navigate_to('laptops')
    dashboard.set_filter_brand(brand)
    assert dashboard.get_first_product_name().lower().find(brand.lower()) != -1
