from requests import get
from bs4 import BeautifulSoup


class SiteParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.page = None

    def parse_page(self, url=''):
        response = get(self.base_url + url).content
        self.page = BeautifulSoup(response, 'html.parser')
        return self.page

    def get_product_name_and_links(self):
        links = {}
        links_a = self.page.find_all('a', class_='name')
        for link in links_a:
            links[link.text] = self.base_url + (link.attrs['href'])
        return links

    def get_next_page_link(self):
        return self.page.find('a', id='more_products').attrs['href']

    def get_product_code_and_prices(self) -> dict:
        code_and_prices = {}
        codes = self.page.find_all('div', class_="code")
        prices = self.page.find_all('span', class_="price")
        for code, price in list(zip(codes, prices)):
            code_and_prices[code.text.split()[1]] = price.text.split()[0]
        return code_and_prices

    def get_header(self):
        return self.page.find('h1').text


if __name__ == '__main__':
    site_parser = SiteParser('https://compservice.in.ua/catalogue/59-mobilni-telefoni.html')
    first_page = site_parser.parse_page()
    print(site_parser.get_product_code_and_prices())
