from passenger import Passenger


class TrainCar:
    def __init__(self, places_number=5, train_car_number=0):
        self.__train_car_number = train_car_number
        self.__places_number = places_number
        self.__places = {number: None for number in range(1, places_number + 1)}
        self.__tickets = []

    def __len__(self):
        return len([k for k, v in self.__places.items() if v is not None])

    def __str__(self):
        return (f'=========================\nTrain car: {self.__train_car_number}\n' +
                '\n'.join([f'Place {number}\n{passenger}' for number, passenger in self.__places.items() if passenger]))

    @property
    def train_car_number(self):
        return self.__train_car_number

    @train_car_number.setter
    def train_car_number(self, value):
        self.__train_car_number = value

    def get_empty_places(self):
        return [place for place, passenger in self.__places.items() if passenger is None]

    def add_passenger(self, new_passenger: Passenger):
        for place, passenger in self.__places.items():
            if passenger is None:
                self.__places[place] = new_passenger
                break

    def add_passenger_by_station(self, station: str):
        for passenger in self.__tickets:
            if passenger.boarding_station == station:
                self.add_passenger(passenger)
                print(f'Passenger: {passenger.full_name} boarded the train at the station: {station}')

    def add_passenger_to_place(self, new_passenger: Passenger, place: int):
        if place in self.__places and self.__places[place] is None:
            self.__places[place] = new_passenger

    def remove_passenger_by_station(self, station: str):
        for place, passenger in self.__places.items():
            if passenger is not None and passenger.destination == station:
                self.__places[place] = None
                print(f'Passenger: {passenger.full_name} left the train at the station: {station}')

    def remove_all_passengers(self):
        self.__places = {number: None for number in range(1, self.__places_number)}

    def add_tickets(self, passenger: Passenger):
        self.__tickets.append(passenger)

    def handle_passengers_at_station(self, station):
        self.add_passenger_by_station(station)
        self.remove_passenger_by_station(station)
