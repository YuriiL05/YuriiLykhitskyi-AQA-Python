# Створіть класс з описом будь-якої тварини. Додайте 1 static method
class Dog:
    def __init__(self, breed, weight):
        self.breed = breed
        self.weight = weight
        self.sound = 'Wof'

    @staticmethod
    def info():
        print('This class is about Dog')


Dog.info()
