from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.general_header_locator = 'xpath=//h1[@class="catalog__title h2"]'

    def click_on_element(self, recieved_locator):
        self.page.locator(recieved_locator).click()


    def check_url(self, url):
        assert url == self.page.url

    def check_element_contains_text(self, recieved_locator, expected_text):
        expect(self.page.locator(recieved_locator)).to_contain_text(expected_text)

    def check_titl_contains_text(self, expected_text):
        expect(self.page).to_contain_title(expected_text)


    def send_text_to_element(self, recieved_locator, text_to_send):
        self.page.locator(recieved_locator).fill(text_to_send)

    def send_enter(self):
        self.page.keyboard.press('Enter')


