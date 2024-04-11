import pytest
from ..infrastructure import StarshipService


@pytest.fixture
def starship_service():
    yield StarshipService()