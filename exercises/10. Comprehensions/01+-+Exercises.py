# Question 1
# Given the following data:
data = [
    {'open': 100, 'high': 120, 'low': 90, 'close': 110},
    {'open': 110, 'high': 130, 'low': 80, 'close': 120},
    {'open': 120, 'high': 140, 'low': 70, 'close': 130},
    {'open': 130, 'high': 150, 'low': 60, 'close': 140},
]

# Re-writing the following code using a comprehension:
# Original version:
# ranges = []
# for d in data:
#     ranges.append(d['high'] - d['low'])
# 
# ranges

# Using list comprehension:
ranges2 = [d['high'] - d['low'] for d in data]
print(ranges2)

# Question 2
# Find all the numbers from 1 to 100 (inclusive) that are divisible by any single digit except 1.

numbers = range(1, 101)
divisors = range(2, 10)

# Finding numbers divisible by any single digit from 2-9 using set comprehension
divisible = {
    number
    for number in numbers
    for num in divisors
    if number % num == 0
}

print(f'Divisible: {divisible}')

# Finding numbers not in the divisible list
non_div = set(range(1, 101)) - divisible
print(f'Not divisible: {non_div}')

# Question 3
# Given a dataset of companies with their ranking and risk factor:
data = [
    {'symbol': 'ABCD', 'name': 'ABCD Company', 'ranking': 2, 'risk': 0.2},
    {'symbol': 'BCDE', 'name': 'BCDE Company', 'ranking': 5, 'risk': 0.2},
    {'symbol': 'CDEF', 'name': 'CDEF Company', 'ranking': 8, 'risk': 0.5},
    {'symbol': 'DEFG', 'name': 'DEFG Company', 'ranking': 7, 'risk': 0.8},
    {'symbol': 'EFGH', 'name': 'EFGH Company', 'ranking': 9, 'risk': 0.6},
    {'symbol': 'FGHI', 'name': 'FGHI Company', 'ranking': 10, 'risk': 0.1},
    {'symbol': 'GHIJ', 'name': 'GHIJ Company', 'ranking': 3, 'risk': 0.6},
    {'symbol': 'HIJK', 'name': 'HIJK Company', 'ranking': 5, 'risk': 0.5},
    {'symbol': 'IJKL', 'name': 'IJKL Company', 'ranking': 5, 'risk': 0.7},
    {'symbol': 'JKLM', 'name': 'JKLM Company', 'ranking': 6, 'risk': 0.9},
    {'symbol': 'KLMN', 'name': 'KLMN Company', 'ranking': 6, 'risk': 0.4},
    {'symbol': 'LMNO', 'name': 'LMNO Company', 'ranking': 8, 'risk': 0.4},
    {'symbol': 'MNOP', 'name': 'MNOP Company', 'ranking': 8, 'risk': 0.2},
    {'symbol': 'NOPQ', 'name': 'NOPQ Company', 'ranking': 1, 'risk': 0.5},
    {'symbol': 'OPQR', 'name': 'OPQR Company', 'ranking': 9, 'risk': 0.2},
    {'symbol': 'PQRS', 'name': 'PQRS Company', 'ranking': 10, 'risk': 0.9},
    {'symbol': 'QRST', 'name': 'QRST Company', 'ranking': 3, 'risk': 0.4},
    {'symbol': 'RSTU', 'name': 'RSTU Company', 'ranking': 7, 'risk': 0.3},
    {'symbol': 'STUV', 'name': 'STUV Company', 'ranking': 8, 'risk': 0.1},
    {'symbol': 'TUVW', 'name': 'TUVW Company', 'ranking': 7, 'risk': 0.9}
]

# Create a new list of dictionaries where the ranking is at least 5 and the risk is less than 0.6
# The new dictionaries should contain the 'symbol' and a calculated key 'weighted', which is ranking / risk
ranking = [
    {
        'symbol': item['symbol'],
        'weighted': round(item['ranking'] / item['risk'], 2)
    }
    for item in data
    if item['ranking'] >= 5 and item['risk'] < 0.6
]

print(ranking)
