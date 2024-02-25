class Passenger:
    def __init__(self, full_name, destination, boarding_station):
        self.__full_name = full_name
        self.__destination = destination
        self.__boarding_station = boarding_station

    def __str__(self):
        return f'Passenger: {self.__full_name}\nDestination: {self.__destination}'

    @property
    def destination(self):
        return self.__destination

    @property
    def full_name(self):
        return self.__full_name

    @property
    def boarding_station(self):
        return self.__boarding_station
