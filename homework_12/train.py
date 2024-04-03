from homework_12.train_car import TrainCar


class Train:
    def __init__(self, train_cars_number: int):
        self.__train_cars = {number: TrainCar(train_car_number=number) for number in range(1, train_cars_number + 1)}
        self.__route = []
        self.__current_station = ''

    def __add__(self, other: TrainCar):
        self.__train_cars[max(self.__train_cars.keys()) + 1] = other
        self.__train_cars[max(self.__train_cars.keys())].train_car_number = max(self.__train_cars.keys())

    def __len__(self):
        return len(self.__train_cars)

    def __str__(self):
        return '\n'.join([f'{train_car}' for number, train_car in self.__train_cars.items()])

    @property
    def train_cars(self):
        return self.__train_cars

    def set_route(self, route: list):
        self.__route = route

    def handle_passengers_at_station(self):
        for train_car in self.__train_cars.values():
            train_car.handle_passengers_at_station(self.__current_station)

    def start_journey(self):
        self.__current_station = self.__route[0]
        print(f'Train departed from statin {self.__current_station}')
        self.handle_passengers_at_station()

    def move_to_next_station(self):
        if self.__current_station != self.__route[-1]:
            self.__current_station = self.__route[self.__route.index(self.__current_station) + 1]
            print(f'Train arrived to the station {self.__current_station}')
            self.handle_passengers_at_station()
        else:
            print(f'Train arrived to the last station {self.__current_station}')


