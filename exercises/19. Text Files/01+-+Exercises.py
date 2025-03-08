# Question 1
# Write some code that generates a file containing the following data:
# 
# i, fibonacci_i, factorial_i, gcd_fibonacci_i_factorial_i
# 
# where:
# - `i`: integer values from 0 to 100
# - `fibonacci_i`: the `i`th Fibonacci number
# - `factorial_i`: the factorial of `i` (i!)
# - `gcd_fib_i_fact_i`: the greatest common denominator of the `i`th Fibonacci number and `i!`
# 
# Hint: look at the `math.factorial` and `math.gcd` functions in the Python docs
# Also make sure to include a header row in your file.

from functools import lru_cache
from math import factorial, gcd

myfile = 'data.csv'
header = ('i', 'fib', 'fact', 'gcd')

# Fibonacci function using LRU cache to optimize the computation
@lru_cache
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Write data to file
def write_data():
    data = [i, fib(i), factorial(i), gcd(fib(i), factorial(i))]
    row = ','.join(map(str, data))
    return row

n = 101  # Generate data from 0 to 100

# Write data to the file
with open(myfile, 'w') as f:
    f.write(','.join(header) + '\n')
    for i in range(n):
        f.write(write_data() + '\n')

# Question 2
# Using the file you just generated, write three functions:
# - `fib`
# - `fact`
# - `gcd_fib_fact`
# that perform the same calculations as our original `fib` function, the `math` module's `factorial`
# and the `gcd` of the corresponding fibonacci and factorial numbers, but uses the data that was saved
# in the file as a cache/lookup mechanism - i.e. just use the numbers in the file if they are available,
# otherwise make the calculation.

# Reading the data from the generated file
data = []

with open(myfile) as f:
    next(f)  # Skip header row
    for row in f:
        data.append(list(map(int, row.strip().split(','))))

# Store Fibonacci, Factorial, and GCD values
fib_stored = [row[1] for row in data]
fac_stored = [row[2] for row in data]
gcd_stored = [row[3] for row in data]

# Fibonacci function with cache lookup
def fib_cached(n):
    if n < len(fib_stored):
        return fib_stored[n]
    else:
        return fib(n)

# Factorial function with cache lookup
def fac_cached(n):
    if n < len(fac_stored):
        return fac_stored[n]
    else:
        return factorial(n)

# GCD function with cache lookup
def gcd_values(n):
    if n < len(gcd_stored):
        return gcd_stored[n]
    else:
        return gcd(fib_cached(n), fac_cached(n))

# Print stored values to verify correctness
print(f'Fibonacci values: {fib_stored}')
print(f'Factorial values: {fac_stored}')
print(f'GCD values: {gcd_stored}')
