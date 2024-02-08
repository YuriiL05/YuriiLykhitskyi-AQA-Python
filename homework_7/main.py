from mylib import mathfunc, is_empty_string, is_a_number

print(is_a_number('3.2'))
print(is_a_number('3.2.2'))

print(is_empty_string(''))
print(is_empty_string('no'))

print(mathfunc.do_sum(1, 34))
print(mathfunc.do_subtraction(45, 23))
