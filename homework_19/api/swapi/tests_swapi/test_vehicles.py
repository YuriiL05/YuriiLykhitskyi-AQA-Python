import json
import pytest


def test_get_vehicles(vehicle_service):
    vehicle = vehicle_service.get_all()
    assert vehicle.status_code == 200


@pytest.mark.parametrize('_id', [4, 6, 14])
def test_save_vehicle(vehicle_service, _id):
    vehicle = vehicle_service.get_single(_id)
    vehicle_service.save_single(_id)
    with open(f'{vehicle.json()["name"]}_vehicles.json') as vehicle_file:
        assert vehicle.json() == json.load(vehicle_file)


def test_get_single_vehicle(vehicle_service):
    vehicle = vehicle_service.get_single(7)
    assert vehicle.status_code == 200
    assert vehicle.json()["name"] == "X-34 landspeeder"


def test_go_next_page(vehicle_service):
    vehicle_service.get_all(1)
    next_vehicles = vehicle_service.go_and_get_next_page()
    assert next_vehicles.status_code == 200
    assert next_vehicles.json()["next"] == 'https://swapi.dev/api/vehicles/?page=3'


def test_save_all_vehicles(vehicle_service):
    vehicle_service.save_all_topic()
    with open('vehicles.json') as vehicle_file:
        assert json.load(vehicle_file)[-1]['name'] == 'AT-RT'
