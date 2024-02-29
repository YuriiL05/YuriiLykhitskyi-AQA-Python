# 1 завдання. Напишіть адаптер, який конвертує json в csv. тобто робить зворотню конвертацію від тієї,
# що ми реалізували на уроці. Приклад з уроку, а також json і csv додано, формат запису даних той самий.
import json
import csv


class JsonToCsv:
    def __init__(self, json_file_name, csv_file_name='result.csv'):
        self.__json_file_name = json_file_name
        self.__csv_file_name = csv_file_name

    @property
    def json_file_name(self):
        return self.__json_file_name

    @property
    def csv_file_name(self):
        return self.__csv_file_name

    @csv_file_name.setter
    def csv_file_name(self, value):
        self.__csv_file_name = value

    @json_file_name.setter
    def json_file_name(self, value):
        self.__json_file_name = value

    def convert_to_csv(self):
        with open(self.__json_file_name, 'r') as json_file:
            data = json.load(json_file)

        with open(self.__csv_file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())


if __name__ == '__main__':
    json_to_csv = JsonToCsv('example.json')
    json_to_csv.convert_to_csv()

    json_to_csv.csv_file_name = 'new_result.csv'
    json_to_csv.convert_to_csv()

