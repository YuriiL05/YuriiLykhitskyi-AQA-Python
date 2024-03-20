from homework_16.core.locators.base_locators import BaseLocators


class HomeLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath: dict[str, str] = {
            'locator_bestsellers_tab': '//*[@id="mainpage"]/div/ul/li[1]/a',
            'locator_bestsellers_active_tab': '//*[@id="mainpage"]/div/ul/li[1][@class="r-tabs-tab r-tabs-state-active"]',
            'locator_new_product_tab': '//*[@id="mainpage"]/div/ul/li[2]/a',
            'locator_promotions_tab': '//*[@id="mainpage"]/div/ul/li[3]/a',
            'locator_new_product_active_tab': '//*[@id="mainpage"]/div/ul/li[2][@class="r-tabs-tab r-tabs-state-active"]',
            'locator_promotions_active_tab': '//*[@id="mainpage"]/div/ul/li[3][@class="r-tabs-tab r-tabs-state-active"]',
            'locator_marker_promotion_first_product': '//*[@id="tab-promotions"]//div[1]/span[@class="marker marker_promotion"]',
            'locator_bestseller_first_product': '//*[@id="tab-bestsellers"]//div[1]/a[@class="name"]',
            'locator_opened_product_name': '//*[@id="content"]/div/h1'
        }
        self._css_selectors: dict[str, str] = {
            'css_locator_test': '#content > div > h1'
        }
