# Створіть за допомогою list comprehension список, в якому буде 100 елементів,
# і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random).
# Порахуйте кількість кожного елемента і виведіть в консоль
from random import randint

list_comp = [randint(1, 10) for number in range(100)]


def count_numbers(list_numb):
    count = {}
    for number in list_numb:
        if number not in count:
            count[number] = 1
        else:
            count[number] = count[number] + 1

    for key, value in count.items():
        print(f'The number {key} is {value} times')


count_numbers(list_comp)
