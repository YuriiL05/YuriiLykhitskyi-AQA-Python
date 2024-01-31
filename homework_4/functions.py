from random import choice

# 1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках,
# і надрукуйте їх у порядку зростання.

numbers_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 54, 3.1, 12, 5]
numbers_list_2 = [3, 7, 5, 6, 7, 23, 9, 54, 3.1, 34, 3.0]


def intersection_numbers_sorted_list(numbers_1: list, numbers_2: list) -> list:
    # Convert lists to sets to remove duplicates and use intersection '&' and convert back to list
    intersected_numbers = list(set(numbers_1) & set(numbers_2))

    # Sort the list
    intersected_numbers.sort()

    return intersected_numbers


print(intersection_numbers_sorted_list(numbers_list_1, numbers_list_2))

# 2.Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного.
# Програма повинна визначити середній бал і вивести імена студентів, чий бал вище середнього.

students_score = {'John': 80, 'Alex': 60, 'Stew': 65, 'Henry': 90, 'Yurii': 100}


def students_above_average_score(students_and_score: dict) -> list:
    students_above_average = []

    # Find the average score
    average_score = sum(students_and_score.values()) / len(students_and_score)

    # Add student to the list if the score is above average
    for student, score in students_and_score.items():
        if score > average_score:
            students_above_average.append(student)

    return students_above_average


print(students_above_average_score(students_score))

# 3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba'].
# напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат.
# для випадковості значень скористайтесь модулем random. приклад згенерованого словника:
# {'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}

names_list = ['John', 'Alex', 'Stew', 'Yurii']
surnames_list = ['Week', 'Bloob', 'Paterson', 'Long', 'Best']
locations_list = ['San Francisco', 'Kyiv', 'London', 'Boston', 'Sumy', 'British Columbia']


def person_with_random_data(names: list, surnames: list, locations: list) -> dict:
    random_person = {}

    if names:
        random_person['name'] = choice(names)
    if surnames:
        random_person['surname'] = choice(surnames)
    if locations:
        random_person['location'] = choice(locations)

    return random_person


print(person_with_random_data(names_list, surnames_list, locations_list))
print(person_with_random_data(names_list, surnames_list, locations_list))
print(person_with_random_data(names_list, surnames_list, locations_list))
