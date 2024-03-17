class BaseLocators:
    def __getattr__(self, name: str) -> tuple[str, str]:
        if name in self._xpath:
            return 'xpath', self._xpath[name]
        elif name in self._css_selectors:
            return 'css selector', self._css_selectors[name]
        else:
            raise AttributeError(f'Locator: {name} is not defined')
