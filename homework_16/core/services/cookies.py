class CookieService:
    def __init__(self, driver):
        self.cookies = []
        self.driver = driver

    def add_to_stored_cookie(self, cookie_list: list) -> None:
        self.cookies.append(cookie_list)

    def get_stored_cookie_by_name(self, name):
        for cookie in self.cookies:
            if cookie['name'] == name:
                return cookie
        return None

    def get_all_stored_cookies(self):
        return self.cookies

    def read_and_store_all_cookies(self):
        self.cookies = self.driver.get_cookies()

    def set_cookie_from_store_by_name(self, name):
        cookie = self.get_stored_cookie_by_name(name)
        if cookie is not None:
            self.driver.add_cookie(cookie)
        else:
            print("Cookie is no stored")

    def set_all_cookies_from_store(self):
        self.driver.set_cookies(self.cookies)

