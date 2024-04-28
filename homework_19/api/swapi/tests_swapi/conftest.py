import pytest
from homework_19.api.swapi import StarshipsService
from homework_19.api.swapi import VehiclesService


@pytest.fixture
def starship_service():
    yield StarshipsService()


@pytest.fixture
def vehicle_service():
    yield VehiclesService()
