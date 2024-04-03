def test_page_naming(phones):
    assert phones.get_name_of_page() == 'МОБІЛЬНІ ТЕЛЕФОНИ'


def test_filter_max_price(phones):
    max_price = 500
    phones.set_filter_max_price(max_price)
    assert phones.get_first_product_price() <= max_price


def test_checkbox_brand_apple(phones):
    phones.set_filter_brand('Apple')
    assert phones.get_first_product_name().lower().find('apple') != -1


def test_filter_brand_apple_min_price(phones):
    phones.set_filter_brand('Apple')
    phones.set_filter_min_price(40000)
    assert phones.get_first_product_price() >= 40000
    assert phones.get_first_product_name().lower().find('apple') != -1


def test_clear_filter(phones):
    phones.set_filter_max_price(500)
    phones.clear_filter()
    assert phones.is_clear_filter_absent()


def test_navigate_from_home_and_switch_to_list(home, dashboard):
    home.navigate_to('phones')
    dashboard.switch_view_to_list()
    assert dashboard.is_list_view_active()


def test_filter_expand_state_by_local_storage(phones):
    phones.set_filter_brand('Apple')
    assert phones.get_local_storage_value_by_key('filter_expand_state')
