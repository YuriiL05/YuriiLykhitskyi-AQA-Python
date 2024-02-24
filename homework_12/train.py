from train_car import TrainCar


class Train:
    def __init__(self, train_cars_number: int):
        self.__train_cars = {number: TrainCar(train_car_number=number) for number in range(1, train_cars_number + 1)}

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


