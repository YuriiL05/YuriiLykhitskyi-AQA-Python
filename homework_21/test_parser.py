def test_parse_page_and_header(comp_service):
    comp_service.parse_page('/catalogue/59-mobilni-telefoni.html')
    assert comp_service.get_header() == 'Мобільні телефони'


def test_product_name_and_links(comp_service_phones):
    links = comp_service_phones.get_product_name_and_links()
    assert links['Термінал Xiaomi Redmi 13C 8/256 Navy Blue'] == 'https://compservice.in.ua/product/5438106.html'


def test_product_code_and_price(comp_service_phones):
    code_price = comp_service_phones.get_product_code_and_prices()
    assert code_price['5432128'] == '4950.00'


def test_several_pages(comp_service_phones):
    next_page_link_1 = comp_service_phones.get_next_page_link()
    comp_service_phones.parse_page(next_page_link_1)
    next_page_link_2 = comp_service_phones.get_next_page_link()
    comp_service_phones.parse_page(next_page_link_2)
    code_price = comp_service_phones.get_product_code_and_prices()
    assert code_price['5233176']

