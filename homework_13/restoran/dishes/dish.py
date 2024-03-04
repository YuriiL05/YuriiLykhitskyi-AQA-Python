from abc import ABC


class Dish(ABC):
    _name = ''

    def __str__(self):
        return self._name
