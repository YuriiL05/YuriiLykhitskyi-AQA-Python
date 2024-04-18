from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_locator = 'xpath=//h1[@class="product__title"]'
        self.search_input_locator = 'xpath=//input[@type="text"]'
        self.buy_pack_button = 'xpath=//div[@class="product__weight"][contains(text(), "6 шт x 400 г")]/../div[3]'
        self.cart_quantity_locator = 'xpath=//div[@class="header__counter js-cart-count"]'


    def check_header(self, text_in_header):
        self.check_element_contains_text(self.header_locator, text_in_header)


    def search_something(self, text_to_search):
        self.send_text_to_element(self.search_input_locator, text_to_search)
        self.send_enter()

    def add_pack_of_products(self):
        self.click_on_element(self.buy_pack_button)

    def check_expected_amount_added(self, amount):
        self.check_element_contains_text(self.cart_quantity_locator, str(amount))


    def check_header_on_search_page(self, text_in_header):
        self.check_element_contains_text(self.general_header_locator, text_in_header)
