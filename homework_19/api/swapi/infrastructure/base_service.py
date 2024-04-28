from requests import get
from homework_19.api.swapi import config
import json


class BaseService:
    def __init__(self, topic):
        self.__base_url = f'{config["host1"]}{topic}/'
        self.topic = topic
        self.current_page = 1

    def get_all(self, page=1):
        return get(f'{self.__base_url}?page={page}')

    def get_single(self, _id=41):
        return get(f'{self.__base_url}{_id}/')

    def save_single(self, _id):
        response = self.get_single(_id)
        with open(f'{response.json()["name"]}_{self.topic}.json', 'w') as data:
            json.dump(response.json(), data, indent=4)

    def save_all_current_page(self):
        response = self.get_all_currant_page()
        with open(f'{self.topic}_page#{self.current_page}.json', 'w') as data:
            json.dump(response.json(), data, indent=4)

    def save_all_topic(self):
        response = self.get_all_currant_page()
        all_response = response.json()['results']
        while True:
            next_response = self.go_and_get_next_page()
            if next_response:
                all_response += next_response.json()['results']
            else:
                break

        with open(f'{self.topic}.json', 'w') as data:
            json.dump(all_response, data, indent=4)

    def get_all_currant_page(self):
        return self.get_all(self.current_page)

    def get_next_and_previous_page(self):
        response = self.get_all(self.current_page)
        next_page = response.json()['next']
        previous_page = response.json()['previous']
        return next_page, previous_page

    def go_and_get_next_page(self):
        next_page, previous_page = self.get_next_and_previous_page()
        if next_page:
            self.current_page = next_page.split('page=')[1]
            return self.get_all_currant_page()
        else:
            return None

    def go_and_get_previous_page(self):
        next_page, previous_page = self.get_next_and_previous_page()
        if previous_page:
            self.current_page = previous_page.split('page=')[1]
            return self.get_all_currant_page()
        else:
            return None
