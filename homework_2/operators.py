from random import randrange

# Task 1

min_in_hour = 60
quarter_of_hour = min_in_hour // 4
_min = randrange(min_in_hour)

if _min < quarter_of_hour:
    print(f'{_min} minutes is a first quarter')
elif _min < quarter_of_hour * 2:
    print(f'{_min} minutes is a second quarter')
elif _min < quarter_of_hour * 3:
    print(f'{_min} minutes is a third quarter')
else:
    print(f'{_min} minutes is a fourth quarter')


# Task 2

birth_month = input('What is your birth month number (1-12)? ')

if not birth_month.isdecimal():
    print('Please enter numbers only')
elif int(birth_month) < 1 or int(birth_month) > 12:
    print('Please enter a number between 1 and 12')
else:
    birth_month = int(birth_month)
    if 1 <= birth_month <= 2 or birth_month == 12:
        print('Зима - За вікном падав сніг.')
    elif 3 <= birth_month <= 5:
        print('Весна - Все довкола розцвітало.')
    elif 6 <= birth_month <= 8:
        print('Літо - Діти насолоджувались літніми канікулами.')
    else:
        print('Осінь - Все довкола загоралось яскравими фарбами.')


# Task 3

some_number = randrange(99999999)
string_number = str(some_number)

sum_digits = sum(int(digit) for digit in str(string_number))

if int(string_number[-1]) % 2 == 0 and sum_digits % 3 == 0:
    print(f'Число {some_number} ділиться на 6')
    print(f'Тому що сума цифр {sum_digits} ділиться на 3 та остання цифра {string_number[-1]} парна')
else:
    print(f'Число {some_number} не ділиться на 6')
    print(f'Тому що сума цифр {sum_digits} не ділиться на 3 та/або остання цифра {string_number[-1]} не парна')


# Task 4

x = input('Enter X coordinate: ')
y = input('Enter Y coordinate: ')

if x.count('.') > 1 or y.count('.') > 1:
    print('Invalid coordinates')
elif ((x.startswith('-') and x[1:].replace('.', '').isdecimal())
      or x.replace('.', '').isdecimal()) \
        and ((y.startswith('-') and y[1:].replace('.', '').isdecimal())
             or y.replace('.', '').isdecimal()):

    x = float(x)
    y = float(y)

    if x > 0 and y > 0:
        print(f'Dot with coordinates {x} and {y} in quarter 1')
    elif x < 0 < y:
        print(f'Dot with coordinates {x} and {y} in quarter 2')
    elif x < 0 and y < 0:
        print(f'Dot with coordinates {x} and {y} in quarter 3')
    elif x > 0 > y:
        print(f'Dot with coordinates {x} and {y} in quarter 4')
    elif x == 0 and y == 0:
        print(f'Dot with coordinates {x} and {y} at the beginning')
    elif x == 0 and y != 0:
        print(f'Dot with coordinates {x} and {y} on X line')
    else:
        print(f'Dot with coordinates {x} and {y} on Y line')
else:
    print('Invalid coordinates')
