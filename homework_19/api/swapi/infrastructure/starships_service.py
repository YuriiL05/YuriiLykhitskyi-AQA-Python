from requests import get
from lesson24.swapi import config
import json

class StarshipService:
    def __init__(self):
        self.__starship_url = f"{config['host1']}starships/"

    def get_all_starships(self, page=1):
        return get(f'{self.__starship_url}?page={page}')

    def get_single_starship(self, id=41):
        return get(f'{self.__starship_url}{id}/')

    def save_single_starship(self, id):
        response = self.get_single_starship(id)
        with open(f'{response.json()["name"]}_starship.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)