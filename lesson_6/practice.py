# Task 2
def if_in_range(start=0, stop=10, numb=0):
    return start <= numb <= stop


entered_number = int(input('numb > '))
print(if_in_range(2, 4, entered_number))


# Task 2
def remove_chars_from_string(*chars):
    input_string = input('Enter a string: ')

    for char in chars:
        input_string = input_string.replace(char, '')

    return input_string


print(remove_chars_from_string('a', 'l'))
