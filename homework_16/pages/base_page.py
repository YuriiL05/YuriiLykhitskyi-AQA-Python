from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from homework_16.core import BaseLocators


class BasePage:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)
        self.actions = ActionChains(self.driver)
        self.base_locators = BaseLocators()

    def find_wait_for_presence_of_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_empty_value_in_element(self, locator):
        self.wait.until(EC.text_to_be_present_in_element_value(locator, ''))

    def click_element(self, locator):
        self.find_wait_for_clickable_element(locator).click()

    def scroll_a_bit(self):
        self.actions.scroll_by_amount(200, 200).perform()

    def get_float_price(self, locator):
        element = self.find_wait_for_presence_of_element(locator)
        return float(element.text.split()[0])

    # def get_wait_for_value_between(self, locator, lower_value=0, upper_value=0):
    #     try:
    #         self.wait.until(lambda x: (lower_value <= self.get_float_price(locator) <= upper_value))
    #         return self.get_float_price(locator)
    #     except TimeoutException:
    #         return self.get_float_price(locator)

    def is_element_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_element_refreshed(self, locator):
        try:
            element = self.find_wait_for_presence_of_element(locator)
            WebDriverWait(self.driver, 3).until(EC.staleness_of(element))
        except TimeoutException:
            print('Element NO refreshed')
            pass

    def get_basket_count(self):
        self.wait_element_refreshed(self.base_locators.locator_basket_count)
        basket_count = self.find_wait_for_presence_of_element(self.base_locators.locator_basket_count)
        return int(basket_count.text.split()[0])

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_mouse_to_element(self, element):
        self.actions.move_to_element(element).perform()

    def is_success_popup_visible(self):
        return self.is_element_visible(self.base_locators.locator_success_popup)

    def is_error_popup_visible(self):
        return self.is_element_visible(self.base_locators.locator_error_popup)

    def navigate_to_phones_page(self):
        self.click_element(self.base_locators.locator_phones_tablets)
        self.click_element(self.base_locators.locator_phones)
