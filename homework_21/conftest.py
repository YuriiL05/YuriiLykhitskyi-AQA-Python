import pytest
from homework_21.site_parser import SiteParser


@pytest.fixture
def comp_service():
    yield SiteParser('https://compservice.in.ua')

@pytest.fixture
def comp_service_phones(comp_service):
    comp_service.parse_page('/catalogue/59-mobilni-telefoni.html')
    yield comp_service

