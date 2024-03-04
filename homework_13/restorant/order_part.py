# 3. опишіть частину функціоналу замовлення в ресторані. OrderPart класс має метод, що повертає певне блюдо.
# Можуть бути різні блюда, наприклад Risotto, Pasta, Pizza,
# які наслідуються від одного батьківського абстрактного класу Dish(Factory).
# *необов'язкова задача. Доповніть 2 задачу, додавши розділи, окрім блюда, наприклад напої,
# або розділивши блюда на холодні та гарячі. На Ваш розсуд, розширте існуючий клас OrderPart,
# або створіть додатковий для обробки нового розділу. Створіть клас Order, який зберігатиме час замовлення
# і всі замовлені блюда/напої
from homework_13.restorant.dishes.pasta import Pasta
from homework_13.restorant.dishes.pizza import Pizza
from homework_13.restorant.dishes.risotto import Risotto
from homework_13.restorant.drinks.cocacola import Cocacola
from homework_13.restorant.drinks.jagerbomb import Jagerbomb
from homework_13.restorant.drinks.slowscrew import Slowscrew


class OrderPart:

    def get_dish(self, dish_name):
        if dish_name == 'Risotto':
            return Risotto()
        elif dish_name == 'Pasta':
            return Pasta()
        elif dish_name == 'Pizza':
            return Pizza()
        else:
            raise Exception('Invalid dish name')

    def get_drink(self, drink_name):
        if drink_name == 'Cocacola':
            return Cocacola()
        elif drink_name == 'Jagerbomb':
            return Jagerbomb()
        elif drink_name == 'Slowscrew':
            return Slowscrew()
        else:
            raise Exception('Invalid drink name')

