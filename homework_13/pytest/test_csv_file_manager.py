#2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок. Напишіть функцію,
# яка видаляє з csv один рядок. напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився.
# в якості перевірного csv можете скористатись доданим до завдання файлом або будь-яким іншим.
import csv


def add_row_to_csv_file(file_name, new_row):
    with open(file_name, 'r') as file:
        rows = list(csv.reader(file))

    if rows:
        rows.append(new_row)

    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def remove_last_row_from_csv_file(file_name):
    with open(file_name, 'r') as file:
        rows = list(csv.reader(file))

    if rows:
        rows.pop()

    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def test_add_row_to_csv_file():
    with open('example.csv', 'r') as file:
        before_rows = list(csv.reader(file))

    add_row_to_csv_file('example.csv', ['Ben', 'Still', 41, 'Male', 10000])

    with open('example.csv', 'r') as file:
        after_rows = list(csv.reader(file))
        assert len(after_rows) == len(before_rows) + 1 and after_rows[-1] == ['Ben', 'Still', '41', 'Male', '10000']


def test_remove_last_row_from_csv_file():
    with open('example.csv', 'r') as file:
        before_rows_remove = list(csv.reader(file))

    remove_last_row_from_csv_file('example.csv')

    with open('example.csv', 'r') as file:
        after_rows_remove = list(csv.reader(file))
        assert len(after_rows_remove) == len(before_rows_remove) - 1
