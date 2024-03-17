from homework_16.core.locators.base_locators import BaseLocators


class MobilePhonesLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath = {
            'locator_naming_page': '//*[@id="content"]/h1',
            'locator_filter_max_price': '//*[@id="filter_current_max_price"]',
            'locator_filter_min_price': '//*[@id="filter_current_min_price"]',
            'locator_first_product_price': '//*[@id="products_list"]/div[1]//span[@class="price"]',
            'locator_clear_filter': '//*[@id="clear_filter"]',
            'locator_filter_brand_apple':
                '//*[@id="filter_bar"]//div[text()="Бренд"]/following-sibling::div/label[text()=" Apple"]/input',
            'locator_first_product_name': '//*[@id="products_list"]/div[1]/a[@class="name"]'
        }
