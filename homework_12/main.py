import train
import train_car
import passenger

# Create Passengers
pas1 = passenger.Passenger('Harry Potter', 'Hogwarts')
pas2 = passenger.Passenger('Hermione G', 'Mistery Lake')
pas3 = passenger.Passenger('Ronaldo W', 'Restricted Forest')

# Create a train with 2 train cars
hogwarts_express = train.Train(2)

# Locate passengers into train cars and places
hogwarts_express.train_cars[1].add_passenger(pas1)
hogwarts_express.train_cars[1].add_passenger_to_place(pas2, 4)
hogwarts_express.train_cars[2].add_passenger(pas3)

print(hogwarts_express)

# Drop passengers on the Mistery Lake station
hogwarts_express.train_cars[1].remove_passenger_by_station('Mistery Lake')

# Create a new train car
new_train_car = train_car.TrainCar()
# Add passenger to the train car
new_train_car.add_passenger_to_place(pas2, 5)

print('\n!!! New Train Car !!!')
# Add train car to the train
hogwarts_express + new_train_car
print(hogwarts_express)

print('\n!!! Train Cars number !!!')
print(len(hogwarts_express))
print('\n!!! Passengers number in hogwarts express !!!')
for car in hogwarts_express.train_cars.values():
    print(f'Train car: {car.train_car_number} has {len(car)} passenger/s')



