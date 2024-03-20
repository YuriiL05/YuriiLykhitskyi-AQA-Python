class BaseLocators:

    def __init__(self):
        self._xpath = {
            'locator_basket_count': '//*[@id="small_basket"]/div[@class="count"]',
            'locator_success_popup': '//*[@id="inf"]',
            'locator_error_popup': '//*[@id="err"]',
            'locator_phones_tablets': '//*[@id="c1101"]/a',
            'locator_phones': '//*[@id="c59"]/a'
        }

    def __getattr__(self, name: str) -> tuple[str, str]:
        if name in self._xpath:
            return 'xpath', self._xpath[name]
        else:
            raise AttributeError(f'Locator: {name} is not defined')

    def get_locator(self, name: str) -> tuple[str, str]:
        if name in self._xpath:
            return 'xpath', self._xpath[name]
        elif name in self._css_selectors:
            return 'css selector', self._css_selectors[name]
        else:
            raise AttributeError(f'Locator: {name} is not defined')

