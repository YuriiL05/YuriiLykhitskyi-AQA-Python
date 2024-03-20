from homework_16.core import CompareLocators
from homework_16.pages.base_page import BasePage


class ComparePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CompareLocators()

    def get_page_title(self):
        return self.find_wait_for_presence_of_element(self.locator.locator_page_title).text
