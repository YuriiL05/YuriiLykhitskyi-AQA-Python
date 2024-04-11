import pytest
from homework_19.api.swapi import StarshipService


@pytest.fixture
def starship_service():
    yield StarshipService()