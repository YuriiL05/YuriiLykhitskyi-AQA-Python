from selenium.webdriver import Keys
from homework_16.pages.base_page import BasePage


class MobilePhonesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_naming_page = ('xpath', '//*[@id="content"]/h1')
        self.locator_filter_max_price = ('xpath', '//*[@id="filter_current_max_price"]')
        self.locator_filter_min_price = ('xpath', '//*[@id="filter_current_min_price"]')
        self.locator_first_product_price = ('xpath', '//*[@id="products_list"]/div[1]//span[@class="price"]')
        self.locator_clear_filter = ('xpath', '//*[@id="clear_filter"]')
        self.locator_filter_brand_apple = \
            ('xpath', '//*[@id="filter_bar"]//div[text()="Бренд"]/following-sibling::div/label[text()=" Apple"]/input')
        self.locator_first_product_name = ('xpath', '//*[@id="products_list"]/div[1]/a[@class="name"]')

    def get_name_of_page(self) -> str:
        return self.find_wait_for_presence_of_element(self.locator_naming_page).text

    def set_filter_price(self, price, locator_update, locator_click):
        filter_price = self.find_wait_for_clickable_element(locator_update)
        filter_price.click()
        filter_price.send_keys(Keys.END, Keys.SHIFT + Keys.HOME, Keys.BACKSPACE)
        filter_price.send_keys(price)
        filter_price_to_click = self.find_wait_for_clickable_element(locator_click)
        filter_price_to_click.click()
        self.wait_element_refreshed(self.locator_first_product_price)

    def set_filter_max_price(self, max_price):
        self.set_filter_price(max_price, self.locator_filter_max_price, self.locator_filter_min_price)

    def set_filter_min_price(self, min_price):
        self.set_filter_price(min_price, self.locator_filter_min_price, self.locator_filter_max_price)

    def get_first_product_price(self):
        return self.get_float_price(self.locator_first_product_price)

    def clear_filter(self):
        clear_filter_element = self.find_wait_for_clickable_element(self.locator_clear_filter)
        clear_filter_element.click()

    def is_clear_filter_absent(self) -> bool:
        return self.is_element_invisible(self.locator_clear_filter)

    def set_filter_brand_apple(self):
        filter_brand_apple_element = self.find_wait_for_clickable_element(self.locator_filter_brand_apple)
        filter_brand_apple_element.click()
        self.wait_element_refreshed(self.locator_first_product_name)

    def get_first_product_name(self):
        return self.find_wait_for_presence_of_element(self.locator_first_product_name).text


