# Оберіть будь-який інтернет ресурс. напишіть 5 будь-яких простих тестів на натискання на елементи і ввід тексту.
# Додайте перевірки за допомогою assert.
# Пройдіться по пагінації. Відфільтруйте вивід(наприклад, введіть в фільтрі на сайті мінімальну чи максимальну ціну)

from selenium.common import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_wait_for_presence_of_element(driver, locator, time_in_seconds=7):
    web_driver_wait = WebDriverWait(driver, time_in_seconds)
    element = web_driver_wait.until(EC.presence_of_element_located(locator))
    return element


def find_wait_for_clickable_element(driver, locator, time_in_seconds=7):
    web_driver_wait = WebDriverWait(driver, time_in_seconds)
    element = web_driver_wait.until(EC.element_to_be_clickable(locator))
    return element


def get_wait_for_value_between(driver, locator, lower_value, upper_value, time_in_seconds=4):
    try:
        web_driver_wait = WebDriverWait(driver, time_in_seconds)
        web_driver_wait.until(
            lambda result: lower_value <= int(driver.find_element(*locator).text.split('\n')[0]) <= upper_value)
        return int(driver.find_element(*locator).text.split('\n')[0])
    except TimeoutException:
        return int(driver.find_element(*locator).text.split('\n')[0])


def open_site_chrome_driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.copart.com')
    return driver


def search_by_mark(mark, driver):
    search_box_selector = '//*[@id="input-search"]'
    search_button_selector = '//*[@id="search-form"]//button[@aria-label="Search Inventory"]'
    search_button = find_wait_for_presence_of_element(driver, ('xpath', search_button_selector))
    search_box = find_wait_for_presence_of_element(driver, ('xpath', search_box_selector))
    search_box.send_keys(mark)
    search_button.click()


def test_search_by_mark():
    mark = 'Honda'
    driver = open_site_chrome_driver()
    search_by_mark(mark, driver)
    search_results_name_selector = '//*[@id="main-container"]//search-results-header//span[2]'
    search_results_name = find_wait_for_presence_of_element(driver, ('xpath', search_results_name_selector))
    assert search_results_name.text == f'Search Results For: {mark}'


def test_pagination_next():
    mark = 'Honda'
    driver = open_site_chrome_driver()
    search_by_mark(mark, driver)
    next_page_selector = '//*[@id="pr_id_1"]/p-paginator/div/button[contains(@class, "p-paginator-next")]'
    next_page = find_wait_for_clickable_element(driver, ('xpath', next_page_selector))
    next_page.click()
    # Check if the second page button is highlighted
    second_page_selector = '//*[@id="pr_id_1"]/p-paginator//button[text()=" 2 "]'
    second_page = find_wait_for_presence_of_element(driver, ('xpath', second_page_selector))
    assert second_page.get_attribute('class').find('p-highlight') >= 0


def test_pagination_third():
    mark = 'Honda'
    driver = open_site_chrome_driver()
    search_by_mark(mark, driver)

    third_page_selector = '//*[@id="pr_id_1"]/p-paginator//button[text()=" 3 "]'
    third_page = find_wait_for_clickable_element(driver, ('xpath', third_page_selector))
    third_page.click()
    # Check if the third page button is highlighted
    assert third_page.get_attribute('class').find('p-highlight') >= 0


def test_filter_by_odometer():
    mark = 'Honda'
    driver = open_site_chrome_driver()
    search_by_mark(mark, driver)
    filter_odometer_selector = '//*[@id="p-panel-1-titlebar"]'
    filter_odometer_min_selector = '//*[@id="p-panel-1-content"]//span[text()="Min"]/following-sibling::input'
    filter_odometer_max_selector = '//*[@id="p-panel-1-content"]//span[text()="Max"]/following-sibling::input'
    filter_odometer_apply_selector = '//*[@id="p-panel-1-content"]//button[text()="Apply"]'

    filter_odometer = find_wait_for_clickable_element(driver, ('xpath', filter_odometer_selector))
    filter_odometer.click()

    filter_odometer_min = find_wait_for_clickable_element(driver, ('xpath', filter_odometer_min_selector))
    filter_odometer_max = find_wait_for_clickable_element(driver, ('xpath', filter_odometer_max_selector))
    min_odometer = 10000
    max_odometer = 100000

    filter_odometer_min.clear()
    filter_odometer_min.send_keys(min_odometer)
    filter_odometer_max.clear()
    filter_odometer_max.send_keys(max_odometer)

    filter_odometer_apply = find_wait_for_clickable_element(driver, ('xpath', filter_odometer_apply_selector))
    filter_odometer_apply.click()

    result_odometer_selector = '//*[@id="pr_id_1-table"]/tbody/tr[1]//label[text()="Odometer"]/following-sibling::div'
    result_odometer = get_wait_for_value_between(driver,
                                                 ('xpath', result_odometer_selector), min_odometer, max_odometer)
    assert result_odometer >= min_odometer
    assert result_odometer <= max_odometer


def test_open_first_car():
    mark = 'Honda'
    driver = open_site_chrome_driver()
    search_by_mark(mark, driver)

    car_selector = '//*[@id="pr_id_1-table"]/tbody/tr[1]/td[1]//a'
    car = find_wait_for_presence_of_element(driver, ('xpath', car_selector))
    car.click()

    car_title_selector = '//*[@id="lot-details"]//div[@class="title-and-highlights"]/h1'
    car_title = find_wait_for_presence_of_element(driver, ('xpath', car_title_selector))

    assert car_title.text.lower().find(mark.lower()) >= 0
