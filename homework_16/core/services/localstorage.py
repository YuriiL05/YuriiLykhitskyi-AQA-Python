class LocalStorageService:
    def __init__(self, driver):
        self.local_store = {}
        self.driver = driver

    def set_item(self, key, value):
        self.driver.execute_script(f'localStorage.setItem("{key}", "{value}")')

    def get_item(self, key):
        return self.driver.execute_script(f'return localStorage.getItem("{key}")')

    def get_all_items(self):
        self.local_store = self.driver.execute_script(
            "var items = {}; "
            "for (var i = 0; i < localStorage.length; i++) { "
            "items[localStorage.key(i)] = localStorage.getItem(localStorage.key(i)); } "
            "return items;")

