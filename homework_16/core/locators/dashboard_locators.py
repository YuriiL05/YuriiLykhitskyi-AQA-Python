from homework_16.core.locators.base_locators import BaseLocators


class DashboardLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath = {
            'locator_naming_page': '//*[@id="content"]/h1',
            'locator_filter_max_price': '//*[@id="filter_current_max_price"]',
            'locator_filter_min_price': '//*[@id="filter_current_min_price"]',
            'locator_first_product_price': '//*[@id="products_list"]/div[1]//span[@class="price"]',
            'locator_clear_filter': '//*[@id="clear_filter"]',
            'locator_filter_brand':
                '//*[@id="filter_bar"]//div[text()="Бренд"]/following-sibling::div/label[text()=" ',
            'locator_first_product_name': '//*[@id="products_list"]/div[1]/a[@class="name"]',
            'locator_list_view': '//*[@id="sortbar"]//a[text()="Список"]',
            'locator_title_view': '//*[@id="sortbar"]//a[text()="Плитка"]'
        }

    def get_filter_by_brand_locator(self, brand: str) -> tuple:
        return 'xpath', self._xpath['locator_filter_brand'] + f'{brand}"]/input'
