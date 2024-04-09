import pytest
from lesson24.swapi import StarshipService


@pytest.fixture
def starship_service():
    yield StarshipService()