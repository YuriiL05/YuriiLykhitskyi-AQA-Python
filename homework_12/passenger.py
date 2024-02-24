class Passenger:
    def __init__(self, full_name, destination):
        self.__full_name = full_name
        self.__destination = destination

    def __str__(self):
        return f'Passenger: {self.__full_name}\nDestination: {self.__destination}'

    @property
    def destination(self):
        return self.__destination

    @property
    def full_name(self):
        return self.__full_name
