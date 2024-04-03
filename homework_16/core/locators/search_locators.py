from homework_16.core.locators.base_locators import BaseLocators


class SearchLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath = {
            'category_results': ['//*[@id="search_categories"]//div[@class="root_item" and text()="',
                                 '"]/following::div[@class="root_item"][1]/preceding-sibling::div[@class="item"]'
                                 '/a[text()="', '"]']
        }

    def get_category_results_locator(self, category: str, subcategory: str) -> tuple:
        locator = self._xpath['category_results']
        return 'xpath', locator[0] + category + locator[1] + subcategory + locator[2]
