def test_search_apple(home, dashboard):
    home.search_product('Apple')
    assert dashboard.get_name_of_page() == 'РЕЗУЛЬТАТИ ПОШУКУ "APPLE"'


def test_search_apple_result_cases_category(home, search_dashboard, dashboard):
    home.search_product('Apple')
    search_dashboard.select_category_in_search_results('Телефони, планшети', 'Чохли')
    assert dashboard.get_first_product_name().lower().find('чохол') != -1
