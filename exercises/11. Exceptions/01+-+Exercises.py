# Question 1
# The following code is meant to calculate the smallest absolute value of a given sequence of numbers.
values = []

try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
except IndexError:
    minimum = 0

print(f'Minimum is: {minimum}')

# The problem is that if the sequence is empty, it will raise an exception.
# Write code such that if the `values` sequence is empty, the calculated minimum is printed as `0`.

# Question 2
# Write code that raises the built-in Python exception `ValueError` with a custom message,
# and catches the exception and prints the custom message.

try:
    raise ValueError('ValueError custom message')
except ValueError as ex:
    print(str(ex))
