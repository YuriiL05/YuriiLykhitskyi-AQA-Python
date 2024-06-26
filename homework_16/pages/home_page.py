from homework_16.core import HomeLocators
from homework_16.pages.base_page import BasePage
from homework_16.pages.product_page import ProductPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomeLocators()

    def click_bestsellers_tab(self):
        self.click_element(self.locators.locator_bestsellers_tab)

    def click_new_products_tab(self):
        self.click_element(self.locators.locator_new_product_tab)

    def click_promotions_tab(self):
        self.click_element(self.locators.locator_promotions_tab)

    def find_bestsellers_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_bestsellers_active_tab)

    def find_new_product_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_new_product_active_tab)

    def find_promotions_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_promotions_active_tab)

    def find_marker_promotion_firs_product(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_marker_promotion_first_product)

    def open_first_product_bestseller(self):
        first_product = self.find_wait_for_presence_of_element(self.locators.locator_bestseller_first_product)
        first_product.click()
        return ProductPage(self.driver)

    def get_bestseller_first_product_name(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_bestseller_first_product).text

    def is_cookie_present_by_name(self, cookie_name):
        self.cookies_service.read_and_store_all_cookies()
        return self.cookies_service.get_stored_cookie_by_name(cookie_name) is not None



