from homework_16.core import SearchLocators
from homework_16.pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SearchLocators()

    def select_category_in_search_results(self, category_name, subcategory_name):
        self.click_element(self.locators.get_category_results_locator(category_name, subcategory_name))
