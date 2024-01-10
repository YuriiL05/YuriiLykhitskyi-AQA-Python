from random import randrange

# Задача 1.
# В змінній min лежить число від 0 до 59, згенероване випадковим чином.
# Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій).

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
