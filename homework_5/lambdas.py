# Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.

list_1 = [1, 2, 3, 4, 5, 6, 7, '8', 9, 10]
list_2 = [2, 3, 4, 5, 6, 12, 13, 14, 15, 16, '8']

intersected_list = lambda a, b: list(set(a) & set(b))

print(intersected_list(list_1, list_2))

# Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда

initial_string = '2.2.2'
numeric_string = '-2.4'

is_number = lambda s: s.lstrip('-').replace('.', '', 1).isdigit() and s.count('-') <= 1

print(is_number(initial_string))
print(is_number(numeric_string))

# Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.

list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 32, 54, 3], [8, 9], [10, 10, 34, 12], [11, 42, 53]]

max_and_min = lambda l: (max(l, key=lambda x: len(x)), min(l, key=lambda x: len(x)))

print(max_and_min(list_of_lists))
