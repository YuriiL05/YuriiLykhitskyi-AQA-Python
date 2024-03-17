# Покрийте тестами свій власний код, який ви написали для ДЗ magic methods
# додайте фікстуру на створення інстансу класу, параметризовані тести,
# розділіть на групи ваші тести за допомогою @pytest.mark, зареєструйте ваші фікстури
# (наприклад @pytest.mark.smoke, @pytest.mark.regression або ваш варіант)

import pytest

from homework_12.passenger import Passenger
from homework_12.train import Train


@pytest.fixture
def passenger_instances():
    pas1 = Passenger('Harry Potter', 'Hogwarts', 'London')
    pas2 = Passenger('Hermione G', 'Mystery Lake', 'London')
    pas3 = Passenger('Ronaldo W', 'Forbidden Forest', 'Mystery Lake')
    pas4 = Passenger('Malfoy G', 'Diagon', 'Forbidden Forest')
    return [pas1, pas2, pas3, pas4]


@pytest.fixture
def train_instance(passenger_instances):
    route = ['London', 'Mystery Lake', 'Forbidden Forest', 'Diagon', 'Hogwarts']
    train = Train(2)
    train.set_route(route)
    train.train_cars[1].add_tickets(passenger_instances[0])
    train.train_cars[1].add_tickets(passenger_instances[1])
    train.train_cars[2].add_tickets(passenger_instances[2])
    train.train_cars[2].add_tickets(passenger_instances[3])
    return train


@pytest.mark.smoke
def test_train_initialization(train_instance):
    assert len(train_instance) == 2


@pytest.mark.smoke
def test_set_route(train_instance):
    train_instance.set_route(['Kyiv', 'Lviv'])
    train_instance.train_cars[1].add_tickets(Passenger('Yurii L', 'Lviv', 'Kyiv'))
    train_instance.start_journey()
    assert len(train_instance.train_cars[1]) == 1


@pytest.mark.smoke
def test_add_passenger(train_instance, passenger_instances):
    train_instance.train_cars[1].add_passenger(passenger_instances[0])
    assert len(train_instance.train_cars[1]) == 1


@pytest.mark.smoke
def test_remove_passenger_by_station(train_instance, passenger_instances):
    train_instance.train_cars[1].add_passenger(passenger_instances[0])
    train_instance.train_cars[1].remove_passenger_by_station('Hogwarts')
    assert len(train_instance.train_cars[1]) == 0


@pytest.mark.regression
@pytest.mark.parametrize('station, train_car, expected_result', [('London', 1, 2), ('Forbidden Forest', 2, 1)])
def test_add_passenger_by_station(train_instance, station, train_car, expected_result):
    train_instance.train_cars[train_car].add_passenger_by_station(station)
    assert len(train_instance.train_cars[train_car]) == expected_result


@pytest.mark.regression
@pytest.mark.parametrize('station, train_car, expected_result', [('Hogwarts', 1, 1), ('Mystery Lake', 1, 1)])
def test_handle_passengers_at_station(train_instance, station, train_car, expected_result):
    train_instance.train_cars[train_car].handle_passengers_at_station('London')
    train_instance.train_cars[train_car].handle_passengers_at_station(station)
    assert len(train_instance.train_cars[train_car]) == expected_result


@pytest.mark.regression
@pytest.mark.parametrize('full_name, place, instance', [('Harry Potter', 1, 0), ('Hermione G', 3, 1)])
def test_add_passenger_to_place(train_instance, passenger_instances, full_name, place, instance):
    train_instance.train_cars[1].add_passenger_to_place(passenger_instances[instance], place)
    assert train_instance.train_cars[1]._TrainCar__places[place].full_name == full_name


@pytest.mark.regression
@pytest.mark.parametrize('station', ['Hogwarts', 'Mystery Lake'])
def test_remove_passengers_by_station(train_instance, passenger_instances, station):
    train_instance.train_cars[1].add_passenger(passenger_instances[0])
    train_instance.train_cars[1].add_passenger(passenger_instances[1])
    train_instance.train_cars[1].add_passenger(passenger_instances[2])
    train_instance.train_cars[1].add_passenger(passenger_instances[3])
    train_instance.train_cars[1].remove_passenger_by_station(station)
    assert len(train_instance.train_cars[1]) == 3


@pytest.mark.regression
def test_move_to_next_station(train_instance, passenger_instances):
    train_instance.start_journey()
    train_instance.move_to_next_station()
    assert len(train_instance.train_cars[2]) == 1
