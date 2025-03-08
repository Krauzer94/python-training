import math
from timeit import timeit
from time import perf_counter

# #### Question 1
# We want to write a function that can find an approximate maximum or minimum of some given function over some given range.

# For example, given some function:
# f(x) = x**2 - 1
# our function should return an approximate minimum (or maximum) of f over some given range, say [-5, 5].

# We'll do this by essentially splitting our intervals into n points (what I'll call the resolution),
# evaluating the function at each of these points, and returning either the min or the max.

# We want this function to be generic, so it should have the following parameters:
# - a function of one variable
# - a range of values defined by start/end values
# - a value indicating the "resolution"
# - a value indicating whether we want the min or the max

# Dummy functions for later test
func_1 = lambda x: x ** 2 - 1
func_2 = lambda x: abs(x - 2)
func_3 = lambda x: math.sin(x)

# Find out min/max out of range
def find_extreme(func, start=-10, end=10, res=1_000, is_min=True):
    delta = (end - start) / (res - 1)
    data = [start + i * delta for i in range(res)]
    f_values = map(func, data)
    min_max = min if is_min else max
    result = min_max(f_values)
    return result

# Output for each function
print(f'\nMinimum for Function 1: {find_extreme(func_1):.4f}')
print(f'Minimum for Function 2: {find_extreme(func_2):.4f}')
print(f'Minimum for Function 3: {find_extreme(func_3):.4f}\n')

# #### Question 2
# You are given a function of two variables, and a list of tuples containing the values for the two variables.
# Create a list that is the result of calling the function on each value in the list, using three different techniques:
# - a `for` loop
# - a list comprehension
# - the `map` function
# Use the `timeit` function to time each approach.

# Hint: write a function that implements each approach, and then time calling those functions using the `timeit` function 
# (from timeit import timeit - we've used it before). Also, you will want to specify `number=10` or something like that 
# when you run `timeit` - unless you want to sit there watching your screen for quite a while :-)

# Define the function that calculates the Euclidean distance
def func(point):
    # expect point to be a sequence of two values
    x, y = point
    return math.hypot(x, y)  # hypot is a function that calculates sqrt(x**2 + y**2)

# Comprehension approach
def comprehension_approach(variable):
    return [math.hypot(x, y) for x, y in variable]

# Map approach
def map_approach(variable):
    return list(map(lambda p: math.hypot(p[0], p[1]), variable))

# For approach
def for_op(func, points):
    results = []
    for point in points:
        results.append(func(point))
    return results

# Points for testing
points = [
    (0, 0),
    (1, 1),
    (10, 20),
    (math.pi, math.e)
]

# Output validation
print(f'For approach: {for_op(func, points)}')
print(f'Comprehension approach: {comprehension_approach(points)}')
print(f'Map approach: {map_approach(points)}\n')

# Performance validation
for_time = timeit('for_op(func, points)', globals=globals(), number=10)
comp_time = timeit('comprehension_approach(points)', globals=globals(), number=10)
map_time = timeit('map_approach(points)', globals=globals(), number=10)

# Performance output
print(f'For time: {for_time}')
print(f'Comprehension time: {comp_time}')
print(f'Map time: {map_time}\n')

# #### Question 3
# Write a function that returns a function with all arguments, except the first one, prefilled with certain values provided to the outer function.
# (This is sometimes called a partial function).

# For example, we may have some functions such as:
# power(x, n) = x ** n
# dist(pt1, pt2) = sqrt(sum((coord_1 - coord_2) for coord_1, coord_2 in zip(pt1, pt2)))

# And we want to generate new functions where the first argument is supplied when the function is called, 
# but all the other arguments are prefilled.

# Define the partial function
def outter_func(f, *args, **kwargs):
    def inner_func(first_arg):
        return f(first_arg, *args, **kwargs)
    return inner_func

# Example functions
squares = outter_func(lambda x, n: x ** n, 2)
dist_origin = outter_func(lambda pt1, pt2: math.sqrt(sum((coord_1 - coord_2) for coord_1, coord_2 in zip(pt1, pt2))), (0, 0))
gcd_13 = outter_func(math.gcd, 13)
log_2 = outter_func(math.log, 2)
log_10 = outter_func(math.log, 10)
log_16 = outter_func(math.log, 16)

# Testing the new functions
print(f'         squares(4): {squares(4)}')
print(f'dist_origin((1, 1)): {dist_origin((1, 1))}')
print(f'        gcd_13(169): {gcd_13(169)}')
print(f'          log_2(10): {log_2(10)}')
print(f'         log_10(10): {log_10(10)}')
print(f'         log_16(10): {log_16(10)}')

# #### Question 4
# Write a function that can be used to not only execute another function with specified arguments, 
# but print a "log" (basically just print to the console), of how long it took to execute the function.

# Example functions
def norm(x, y):
    return math.sqrt(x**2 + y**2)

def find_index_min(seq):
    min_ = min(seq)
    return seq.index(min_)

# Logged function decorator
def logged(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = f(*args, **kwargs)
        elapsed_time = perf_counter() - start_time
        print(f"Elapsed: {elapsed_time} secs")
        print(f" Result: {result}")
        return result
    return wrapper

# Create logged functions
norm_logged = logged(norm)
find_index_min_logged = logged(find_index_min)

# Testing logged functions
norm_logged(1, 1)
find_index_min_logged([3, 1, 4, 1, 5, 9])
