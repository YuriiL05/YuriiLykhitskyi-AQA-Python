from homework_16.core.locators.base_locators import BaseLocators


class ProductLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self._xpath: dict = {
            'locator_product_name': '//*[@id="content"]/div/h1',
            'locator_product_to_basket': '//*[@id="content"]//a[text()="до кошика"]',
            'characteristic': ['//*[@id="tab-characteristics"]/table/tbody//td[text()="', '"]/following-sibling::td'],
            'locator_robot_protection': '//*[@id="tab-comments"]/form/div[2]/p[3]/span/div',
            'locator_robot_protection_status': '//*[@id="recaptcha-accessible-status"]',
            'locator_robot_protection_checkmark': '//*[@id="recaptcha-anchor"]/div[@class="recaptcha-checkbox-checkmark"]',
            'locator_comments_tab': '//*[@id="content"]//ul[@class="r-tabs-nav"]//a[@href="#tab-comments"]',
            'locator_comments_textarea': '//*[@id="tab-comments"]/form//textarea[@name="add[comments]"]',
            'locator_vote_block': '//*[@id="tab-comments"]/form//div[@class="vote-stars"]',
            'locator_vote_success': '//*[@id="tab-comments"]/form//div[@class="vote-success"]',
            'locator_button_add_comment': '//*[@id="tab-comments"]/form/p/input',
            'locator_error_robot_popup': '//*[@id="err"]//li[text()="Будь ласка, підтвердіть те, що Ви не робот."]',
            'locator_add_to_compare': '//*[@id="content"]//a[text()="порівняти"]',
            'locator_open_compare': '//*[@id="sidebar_compare"]//a[@class="compare"]',
            'locator_tel_number_buy_in_click': '//*[@id="content"]/div/div[3]/form/input[1]',
            'locator_button_buy_in_click': '//*[@id="content"]//form/input[@value="Купити"]',
            'locator_product_code': '//*[@id="content"]/div/div[@class="code"]/span',
            'locator_in_stock': '//*[@id="content"]//div[@class="in_stock"]/div'
        }

    def get_characteristic_locator(self, character: str) -> tuple[str, str]:
        return 'xpath', self._xpath['characteristic'][0] + character + self._xpath['characteristic'][1]

