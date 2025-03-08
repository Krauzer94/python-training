# Question 1
# Many functions in Python deal with numbers in half-closed intervals.
# For example, `range(n)` returns integers in the interval [0, n).
# When we deal with integers, it is very easy to include `n` - we simply add `1` to it.
# For example, to generate integers in the range [a, b], we use range(a, b+1).
# However, when it comes to real numbers there is no (mathematically speaking) "next" real number.
# But for floats, remember that these are actually **not** real numbers, but approximations with some fixed precision -
# in those cases it is indeed possible to always calculate the "next" number after any given float.

import math

# Using the math module to find the "next" number after 1
e = math.nextafter(1, math.inf)
print(e)

# Question 2
# Given a sequence of points, each one with possibly different number of dimensions,
# generate a list that contains the magnitude (norm) of the point.
# For an n-dimensional point (therefore containing n components):
# x = (x_1, x_2, ..., x_n)
# this value can be computed as:
# sqrt(x_1 ** 2 + x_2 ** 2 + ... + x_n **2)

# Example data:
data = [
    (0, 1),
    (1, 2, 3),
    (1, 3, 5, 7),
    (1, 1, 2, 3, 5, 8, 13)
]

# Function to calculate the norm of each point
def compute_norms(points):
    norms = []
    for point in points:
        norm = math.sqrt(sum(x ** 2 for x in point))
        norms.append(norm)
    return norms

# Call the function and print the results
norms = compute_norms(data)
print(norms)

# Question 3
# Given an arbitrary sequence of numerical values, write a function that "analyzes" the sequence
# by generating print outputs of:
# - number of elements
# - number of unique elements
# - the min
# - the max
# - the mean
# - the standard deviation
# - all the modes (if there are more than one)
# - the 25th, 50th, and 75th percentiles

# Example data:
data = [
    61, 35, 99, 100, 75, 94, 88, 14, 21, 39, 53, 25, 87, 84, 
    81, 55, 86, 18, 69, 44, 16, 33, 66, 52, 70, 52, 95, 45, 
    94, 35, 68, 70, 52, 53, 30, 87, 79, 51, 92, 72, 55, 40, 
    15, 74, 86, 87, 91, 70, 45, 37
]

import statistics

# Function to analyze the sequence
def analyze_sequence(seq):
    count = len(seq)
    unique_count = len(set(seq))
    min_val = min(seq)
    max_val = max(seq)
    mean = round(statistics.mean(seq), 3)
    std_dev = round(statistics.stdev(seq), 3)
    modes = statistics.multimode(seq)
    percentile_25 = round(statistics.quantiles(seq, n=4)[0], 3)
    median = round(statistics.median(seq), 3)
    percentile_75 = round(statistics.quantiles(seq, n=4)[2], 3)
    
    # Print the analysis results
    print(f"count: {count}")
    print(f"unique count: {unique_count}")
    print(f"min: {min_val}")
    print(f"max: {max_val}")
    print(f"mean: {mean}")
    print(f"std dev: {std_dev}")
    print(f"modes: {modes}")
    print(f"25th percentile: {percentile_25}")
    print(f"median: {median}")
    print(f"75th percentile: {percentile_75}")

# Call the function and print the results
analyze_sequence(data)
