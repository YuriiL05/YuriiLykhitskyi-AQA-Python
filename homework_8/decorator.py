# Створіть декоратор, який виводить в консоль ім'я функції, яку було викликано.
# Наприклад, створіть пару функцій для арифметичних операцій додавання і множення.
# При виклику цих функцій має повертатись результат операції і виводиться в консоль ім'я функції, яку було викликано.

def function_name_log(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@function_name_log
def sum_numbers(x, y):
    return x + y


@function_name_log
def multiply_numbers(x, y):
    return x * y


print(sum_numbers(1, 3))
print(multiply_numbers(2, 5))
