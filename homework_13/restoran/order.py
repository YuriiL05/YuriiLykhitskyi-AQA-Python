# Створіть клас Order, який зберігатиме час замовлення і всі замовлені блюда/напої
from datetime import datetime

from homework_13.restoran.order_part import OrderPart


class Order:
    def __init__(self, table_number):
        self.__table_number = table_number
        self.__items = []
        self.__order_date = datetime.now().strftime('%d-%m-%y %H:%M:%S')

    def add_item(self, item):
        self.__items.append(item)

    def __str__(self):
        item_list = ', '.join(map(str, self.__items))
        return f'Table: {self.__table_number}\nOrder time: {self.__order_date}\nOrder Items: {item_list}'


if __name__ == '__main__':
    order1 = Order(1)
    order2 = Order(2)
    order_part = OrderPart()

    order1.add_item(order_part.get_dish('Risotto'))
    order1.add_item(order_part.get_dish('Pizza'))
    order1.add_item(order_part.get_drink('Cocacola'))

    order2.add_item(order_part.get_dish('Pasta'))
    order2.add_item(order_part.get_drink('Jagerbomb'))

    print(order1)
    print(order2)
