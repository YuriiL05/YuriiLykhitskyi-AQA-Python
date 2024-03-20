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
