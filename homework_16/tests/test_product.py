import pytest


def test_add_product_to_basket(iphone_14_256_midnight):
    iphone_14_256_midnight.add_to_basket()
    assert iphone_14_256_midnight.get_basket_count() == 1


@pytest.mark.parametrize('characteristic, expected_value',
                         [("Бренд", "Apple"),
                          ("Лінійка", "iPhone 14"),
                          ("Тип", "Смартфон"),
                          ("Попередньо встановлена ОС", "iOS 16"),
                          ("Вбудована пам'ять, ГБ", "256")])
def test_product_characteristic(iphone_14_256_midnight, characteristic, expected_value):
    characteristic_value_element = iphone_14_256_midnight.get_product_characteristic(characteristic)
    assert characteristic_value_element.text == expected_value


def test_set_rating(iphone_14_256_midnight):
    iphone_14_256_midnight.open_comments_tab()
    assert iphone_14_256_midnight.set_rating(4).text == 'Ваша оценка: 4'


def test_robot_protection_passed(iphone_14_256_midnight):
    iphone_14_256_midnight.open_comments_tab()
    iphone_14_256_midnight.pass_robot_protection()
    assert iphone_14_256_midnight.is_robot_protection_passed()


def test_send_a_comment(iphone_14_256_midnight):
    iphone_14_256_midnight.send_a_comment(
        'Даний телефон є досить привабливим за свою ціну. Користуюся ним досить давно. Все супер!', 4)
    assert iphone_14_256_midnight.is_success_popup_visible()


def test_add_to_compare(iphone_14_256_midnight):
    iphone_14_256_midnight.add_product_to_compare()
    assert iphone_14_256_midnight.is_success_popup_visible()


def test_open_compare_page(phones):
    first_phone = phones.open_first_product()
    first_phone.add_product_to_compare()
    first_phone.navigate_to('phones')
    phones.set_filter_brand_apple()
    phones.set_filter_max_price(20000)
    another_phone = phones.open_first_product()
    another_phone.add_product_to_compare()
    compare_page = another_phone.open_compare_products_page()
    assert compare_page.get_page_title() == 'ПОРІВНЯННЯ ТОВАРІВ'


def test_buy_iphone_in_one_click_error(phones):
    phones.set_filter_brand_apple()
    iphone = phones.open_first_product()
    iphone.add_telephone_number_buy_in_click()
    iphone.send_telephone_number_buy_in_click()
    assert iphone.is_error_popup_visible()


@pytest.mark.parametrize('products', ['phones', 'tablets', 'laptops'])
def test_first_product_on_dashboard_is_available(home, dashboard, product, products):
    home.navigate_to(products)
    dashboard.open_first_product()
    assert product.is_product_in_stock()
