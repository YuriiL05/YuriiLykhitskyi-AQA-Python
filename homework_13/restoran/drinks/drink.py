from abc import ABC


class Drink(ABC):
    _name = ''

    def __str__(self):
        return self._name
