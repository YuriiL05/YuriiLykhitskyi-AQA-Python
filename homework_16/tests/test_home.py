def test_open_new_product_tab(home):
    home.click_new_products_tab()
    assert home.find_new_product_active_tab()


def test_open_promotions_tab(home):
    home.click_promotions_tab()
    assert home.find_promotions_active_tab()


def test_open_bestsellers_tab(home):
    home.click_bestsellers_tab()
    assert home.find_bestsellers_active_tab()


def test_marker_promotion(home):
    home.click_promotions_tab()
    assert home.find_marker_promotion_firs_product()


def test_open_bestseller_fist_product(home):
    first_product_name = home.get_bestseller_first_product_name()
    opened_product = home.open_first_product_bestseller()
    assert first_product_name == opened_product.get_product_name()


def test_initial_cookie(home):
    home.cookies_service.read_and_store_all_cookies()
    assert home.cookies_service.get_stored_cookie_by_name('COMPSESSID')


def test_recently_viewed_product_by_cookie(home, phones):
    viewed_product_codes = []
    first_phone = phones.open_first_product()
    viewed_product_codes.append(first_phone.get_product_code())
    first_phone.navigate_to('phones')
    phones.set_filter_brand_apple()
    another_phone = phones.open_first_product()
    viewed_product_codes.append(another_phone.get_product_code())
    assert home.get_recently_viewed_cookie_list() == viewed_product_codes[::-1]


def test_recently_viewed_product_by_cookie_no_duplicates(home, phones):
    viewed_product_codes = []
    first_phone = phones.open_first_product()
    viewed_product_codes.append(first_phone.get_product_code())
    first_phone.navigate_to('phones')
    phones.set_filter_brand_apple()
    second_phone = phones.open_first_product()
    viewed_product_codes.append(second_phone.get_product_code())
    # Open the first phone again
    second_phone.navigate_to('phones')
    phones.open_first_product()
    assert home.get_recently_viewed_cookie_list() == viewed_product_codes
