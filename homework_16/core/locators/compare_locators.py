from homework_16.core.locators.base_locators import BaseLocators


class CompareLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath: dict = {
            'locator_page_title': '//*[@id="content"]/h1'
        }