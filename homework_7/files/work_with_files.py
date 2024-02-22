# 2. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).
import csv
import re


def domains_from_file(filename) -> list:
    with open(filename, 'r') as domains_file:
        # Read file to a string, remove the first dot by regexp and split the string
        domains = re.sub(r'(\.(.+(\n|$)))', r'\2', domains_file.read()).splitlines()

    return domains


print(domains_from_file('domains.txt'))

# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
# Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані


def lastnames_from_file(filename) -> list:
    with open(filename, 'r') as names_file:
        names = re.sub(r'(\d+ )([\w-]+) (.*(\n|$))', r'\2\4', names_file.read()).splitlines()

    return names


print(lastnames_from_file('names.txt'))

# 4. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду
# {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


def dates_from_file(filename) -> list:
    dates_list = []
    with open(filename, 'r') as authors_file:
        dates = re.findall(r'\d{1,2}(?:nd|st|th|rd) [a-z,A-Z]+ \d{4}', authors_file.read())

    for date in dates:
        dates_list.append({'date': date})

    return dates_list


print(dates_from_file('authors.txt'))

# 5.Створіть функцію, яка читає файл csv. Вона приймає назву файлу(str), повертає список рядків(list).
# Також створіть функцію, яка записує в файл данні. Вона приймає назву файлу(str), список рядків(list),
# які треба записать в файл. Нічого не повертає.
# Тепер за допомогою створених функцій
# спочатку створіть файл(3 рядків достатньо), потім прочитайте той-же файл, записавши рядки в змінну,
# потім додайте два рядки в змінну, і після цього запишіть ваші зміни в інший файл.


def csv_file_to_list(filename) -> list:
    csv_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_list.append(row)

    return csv_list


def write_file_from_list(filename: str, lines: list) -> None:
    with open(filename, 'w') as new_csv_file:
        csv.writer(new_csv_file, delimiter=',').writerows(lines)


write_file_from_list('test_csv_file.csv', [
    ['existed', 'line', 'test'],
    ['something', 'here', 'as well'],
    ['not', 'at the', 'end']
])

some_file_list = csv_file_to_list('test_csv_file.csv')

some_file_list.extend([['new', 'line', 'test'], ['new', 'line2', 'test2']])

write_file_from_list('new_csv_file.csv', some_file_list)
