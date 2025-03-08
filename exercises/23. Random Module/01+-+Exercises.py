import random
from collections import Counter

# #### Question 1
# Generate the sample space of rolling two 6-sided dice, numbered '9', '10', 'J', 'Q', 'K', 'A'.
# (The sample space is the set of all possible outcomes).
# Your result should be a list containing tuples for the outcome of each die, e.g.
# [('9', '9'), ('9', '10'), ('9', 'J'), ('9', 'Q'), ('9', 'K'), ('9', 'A'),
#  ('10', '9'), ('10', '10'), ('10', 'J'), ('10', 'Q'), ('10', 'K'), ('10', 'A'), etc.]

def make_sample_space():
    sample_space = []
    face_values = ['9', '10', 'J', 'Q', 'K', 'A']
    for v1 in face_values:
        for v2 in face_values:
            sample_space.append((v1, v2))
    
    return sample_space

print(make_sample_space())

# #### Question 2
# Using the sample space you just created above, simulate throwing the two dice `n` times by making random choices from the sample space.
# Again, make this into a function that returns the random choices as a list of tuples, with `n` as a parameter of this function.
# Call the function `simulate_throws_from_sample_space`.

def simulate_throws_from_sample_space(n):
    return random.choices(make_sample_space(), k=n)

print(simulate_throws_from_sample_space(5))

# #### Question 3
# Your goal here is to implement a function `simulate_throws`, similar to the one you wrote in Question 2, but without generating a sample space at all - just using the `face_values`.
# Write a function that implements this, and name it `simulate_throws`.

face_values = ['9', '10', 'J', 'Q', 'K', 'A']

def simulate_throws(n):
    return [tuple(random.choices(face_values, k=2)) for _ in range(n)]

print(simulate_throws(7))

# #### Question 4
# Using both methods of generating throws, build a dictionary that contains the face values as keys, and the number of times they were selected in the simulated throws.
# For example, assuming you made `100` throws using one of these methods, your dictionary might look like this:
# {'9': 39, '10': 27, 'J': 28, 'Q': 34, 'K': 36, 'A': 36}
# Note that your values in the dictionary should add up to `200` if you made one `100` throws.
# Write a function that is given the function to use to generate the throws, the number of throws to simulate, and returns this dictionary.

def frequency_analysis():
    sample = simulate_throws(70)  # Adjust the number of throws as needed
    frequencies = {}
    for row in sample:
        for value in row:
            frequencies[value] = frequencies.get(value, 0) + 1
    
    return frequencies

print(frequency_analysis())

# #### Question 5
# Write a function that given two arguments `a` and `b` returns a random float between `a` (inclusive) and `b` (exclusive).

def random_float(a=0, b=1):
    return a + random.random() * (b - a)

print(random_float(2, 4))
