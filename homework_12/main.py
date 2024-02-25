import train
import passenger

# Create route
route = ['London', 'Mystery Lake', 'Forbidden Forest', 'Diagon', 'Hogwarts']

# Create Passengers
pas1 = passenger.Passenger('Harry Potter', 'Hogwarts', 'London')
pas2 = passenger.Passenger('Hermione G', 'Mistery Lake', 'London')
pas3 = passenger.Passenger('Ronaldo W', 'Forbidden Forest', 'Mystery Lake')
pas4 = passenger.Passenger('Malfoy G', 'Diagon', 'Forbidden Forest')

# Create a train with 2 train cars
hogwarts_express = train.Train(2)

# Book places for passengers into train cars
hogwarts_express.train_cars[1].add_tickets(pas1)
hogwarts_express.train_cars[1].add_tickets(pas2)
hogwarts_express.train_cars[2].add_tickets(pas3)
hogwarts_express.train_cars[2].add_tickets(pas4)

hogwarts_express.set_route(route)
hogwarts_express.start_journey()

hogwarts_express.move_to_next_station()
hogwarts_express.move_to_next_station()
hogwarts_express.move_to_next_station()
hogwarts_express.move_to_next_station()
hogwarts_express.move_to_next_station()
