from selenium.common import ElementClickInterceptedException
from homework_16.core import ProductLocators, BaseLocators
from homework_16.pages.base_page import BasePage
from homework_16.pages.compare_page import ComparePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()
        self.base_locators = BaseLocators()

    def get_product_name(self):
        return self.find_wait_for_presence_of_element(self.locators.locator_product_name).text

    def add_to_basket(self):
        self.click_element(self.locators.locator_product_to_basket)

    def get_product_characteristic(self, characteristic_name):
        return self.find_wait_for_presence_of_element(self.locators.get_characteristic_locator(characteristic_name))

    def open_comments_tab(self):
        self.click_element(self.locators.locator_comments_tab)

    def pass_robot_protection(self):
        robot_protection = self.find_wait_for_presence_of_element(self.locators.locator_robot_protection)
        self.scroll_to_element(robot_protection)
        self.move_mouse_to_element(robot_protection)
        robot_protection.click()
        self.wait_element_refreshed(self.locators.locator_robot_protection)

    def is_robot_protection_passed(self):
        try:
            self.click_element(self.locators.locator_button_add_comment)
            self.is_error_popup_visible()
            return self.is_element_invisible(self.locators.locator_error_robot_popup)
        except ElementClickInterceptedException:
            return False

    def add_comment_to_textarea(self, comment_text):
        textarea = self.find_wait_for_presence_of_element(self.locators.locator_comments_textarea)
        textarea.send_keys(comment_text)

    def set_rating(self, rating=4):
        rating_div = self.find_wait_for_presence_of_element(self.locators.locator_vote_block)

        div_size = rating_div.size
        div_width = div_size['width']
        div_height = div_size['height']
        # Calculate the width and height of each section
        section_width = div_width / 5
        section_height = div_height

        # Calculate the coordinates of the click point within the selected section
        click_x = (rating - 3) * section_width
        click_y = 0.5 * section_height

        # Use JavaScript to simulate a click event at the calculated coordinates
        self.actions.move_to_element_with_offset(rating_div, click_x, click_y).click().perform()

        # Return element with information about set rating
        return self.find_wait_for_presence_of_element(self.locators.locator_vote_success)

    def send_a_comment(self, comment_text, rating: int):
        self.open_comments_tab()
        self.add_comment_to_textarea(comment_text)
        self.set_rating(rating)
        self.pass_robot_protection()
        self.click_element(self.locators.locator_button_add_comment)

    def add_product_to_compare(self):
        self.click_element(self.locators.locator_add_to_compare)

    def open_compare_products_page(self):
        self.click_element(self.locators.locator_open_compare)
        return ComparePage(self.driver)

    def add_telephone_number_buy_in_click(self):
        number_element = self.find_wait_for_presence_of_element(self.locators.locator_tel_number_buy_in_click)
        number_element.send_keys('+380000000000')

    def send_telephone_number_buy_in_click(self):
        self.click_element(self.locators.locator_button_buy_in_click)

