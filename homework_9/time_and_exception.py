# Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів.
# Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int),
# і знак(True або False, які репрезентують + і -). Повертає datetime. В цій задачі скористайтесь datetime.timedelta
from datetime import datetime, timedelta


def date_shifted_by_days(input_date: datetime, shift_days: int, sign: bool) -> datetime:
    return input_date + (timedelta(days=shift_days) * (1 if sign else -1))


print(date_shifted_by_days(datetime.now(), 10, False))

# Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні),
# вираховуючі різницю між наданим значенням і значенням datetime.now(). Приймає дату та час(datetime),
# повертає три значення: datetime.timedelta, datetime.timestamp прожитого життя і строкове значення часу народження
# в форматі (рік(останні два числа, день, місяць, години, хвилини,секунди, am/pm в 12 годинному форматі).
# Виведіть результат в консоль


def get_age(birthday: datetime):
    current_age_delta = datetime.now() - birthday
    current_age_timestamp = current_age_delta.total_seconds()
    birthday_srt = birthday.strftime('%y-%d-%m %I:%M:%S %p')

    return current_age_delta, current_age_timestamp, birthday_srt


print(get_age(datetime(1993, 12, 1, 15, 5, 10)))

# Створіть обробку одного будь-якого exception, який не використався як приклад на занятті,
# додайте обробку решти ексепшенів за допомогою Exception. Виведіть результат в консоль


def func_with_exceptions(file_name: str):
    try:
        with open(file_name, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('File Not found', e)
    except Exception as e:
        print('Unexpected error:', e)
    else:
        print('=== Success ===')


func_with_exceptions('not_existed.txt')
func_with_exceptions('existed.txt')
