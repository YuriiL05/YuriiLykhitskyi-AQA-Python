import re

# Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа та нижнє підкреслення.


def if_letter_digits_and_underscore(word: str) -> bool:
    pattern = re.compile(r'(\w*)(\d*)(_*)')
    result = pattern.fullmatch(word)

    if result and word != '':
        return True
    else:
        return False


print(if_letter_digits_and_underscore('Test_123_andOther'))
print(if_letter_digits_and_underscore('123'))
print(if_letter_digits_and_underscore('Word'))
print(if_letter_digits_and_underscore('___'))
print(if_letter_digits_and_underscore('With-some other 23'))
print(if_letter_digits_and_underscore(''))

# Напишіть програму, що видаляє область дужок в стрічці
# 		["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
# 		example
# 		github
# 		stackoverflow

list_of_strings = ["example (.com)", "github (.com)", "stackoverflow (.com)"]


def remove_brackets_info(input_str: str) -> str:
    pattern = re.compile(r'\(.*\)')
    return pattern.sub('', input_str)


for s in list_of_strings:
    print(remove_brackets_info(s))


# Напишіть програму, що. вставляє пробіл перед великою літерою


def add_space_before_capital_letters(input_str: str) -> str:
    return re.sub(r'([A-Z])', r' \1', input_str)


print(add_space_before_capital_letters('SomeTestWords hereSomeNew and Here231test_'))
