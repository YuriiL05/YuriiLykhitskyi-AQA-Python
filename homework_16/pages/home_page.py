from homework_16.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_bestsellers_tab = ('xpath', '//*[@id="mainpage"]/div/ul/li[1]/a')
        self.locator_new_product_tab = ('xpath', '//*[@id="mainpage"]/div/ul/li[2]/a')
        self.locator_promotions_tab = ('xpath', '//*[@id="mainpage"]/div/ul/li[3]/a')
        self.locator_bestsellers_active_tab = \
            ('xpath', '//*[@id="mainpage"]/div/ul/li[1][@class="r-tabs-tab r-tabs-state-active"]')
        self.locator_new_product_active_tab = \
            ('xpath', '//*[@id="mainpage"]/div/ul/li[2][@class="r-tabs-tab r-tabs-state-active"]')
        self.locator_promotions_active_tab = \
            ('xpath', '//*[@id="mainpage"]/div/ul/li[3][@class="r-tabs-tab r-tabs-state-active"]')
        self.locator_marker_promotion_first_product = \
            ('xpath', '//*[@id="tab-promotions"]//div[1]/span[@class="marker marker_promotion"]')
        self.locator_bestseller_first_product = ('xpath', '//*[@id="tab-bestsellers"]//div[1]/a[@class="name"]')
        self.locator_opened_product_name = ('xpath', '//*[@id="content"]/div/h1')

    def click_bestsellers_tab(self):
        self.click_element(self.locator_bestsellers_tab)

    def click_new_products_tab(self):
        self.click_element(self.locator_new_product_tab)

    def click_promotions_tab(self):
        self.click_element(self.locator_promotions_tab)

    def find_bestsellers_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locator_bestsellers_active_tab)

    def find_new_product_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locator_new_product_active_tab)

    def find_promotions_active_tab(self):
        return self.find_wait_for_presence_of_element(self.locator_promotions_active_tab)

    def find_marker_promotion_firs_product(self):
        return self.find_wait_for_presence_of_element(self.locator_marker_promotion_first_product)

    def open_first_product_bestseller(self):
        first_product = self.find_wait_for_presence_of_element(self.locator_bestseller_first_product)
        first_product.click()

    def get_bestseller_first_product_name(self):
        return self.find_wait_for_presence_of_element(self.locator_bestseller_first_product).text

    def get_opened_product_name(self):
        return self.find_wait_for_presence_of_element(self.locator_opened_product_name).text


