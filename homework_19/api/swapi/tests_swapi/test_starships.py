import json

import pytest


def test_get_starships_without_parameters(starship_service):
    starships = starship_service.get_all_starships()
    assert starships.json()["next"] == "https://swapi.dev/api/starships/?page=2"

@pytest.mark.parametrize('current,previous,next', [(1,None,"https://swapi.dev/api/starships/?page=2"),
                                                   (2,'https://swapi.dev/api/starships/?page=1',"https://swapi.dev/api/starships/?page=3"),
                                                   (3,'https://swapi.dev/api/starships/?page=2',"https://swapi.dev/api/starships/?page=4"),
                                                   (4,'https://swapi.dev/api/starships/?page=3',None)])
def test_get_starships_with_parameters(starship_service,current,previous,next):
    starships = starship_service.get_all_starships(current)
    assert starships.json()["previous"] == previous
    assert starships.json()["next"] == next

def test_get_single_starship(starship_service):
    single_starship = starship_service.get_single_starship()
    assert single_starship.status_code == 200
    assert single_starship.json()["name"] == "Scimitar"

def test_get_single_starship_validate_data_consistency(starship_service):
    single_starship = starship_service.get_single_starship(41)
    assert single_starship.status_code == 200
    with open('Scimitar_starship.json') as data:
        data_converted = json.load(data)
        assert data_converted == single_starship.json()



