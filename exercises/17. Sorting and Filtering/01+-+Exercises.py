# Question 1
# Given a list of tuples containing two numerical values, write a function that returns 
# a list of the same tuples, sorted by the absolute value of the difference between 
# the two numbers, in descending order.

# Example input
l = [
    (1, 2),
    (-4, -5.5),
    (10, -10),
    (-2, 2)
]

# Function to sort the tuples by the absolute difference between the two numbers
def sort_by_abs_diff(l):
    return sorted(
        l, 
        key=lambda t: abs(t[0] - t[1]),
        reverse=True
    )

# Print the result
print(sort_by_abs_diff(l))

# Question 2
# Given the following data:
suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

# Write a function that returns a list with all 52 cards.
# Optional: You can specify whether the cards should be sorted in ascending or descending order.
def deck(suits, ranks, *, reverse=False):
    ordered_ranks = [
        rank 
        for rank, rank_number in sorted(
            list(zip(ranks, range(1, 14))), 
            key=lambda t: t[1], 
            reverse=reverse
        )
    ]
    return [
        [
            r + s 
            for r in ordered_ranks
        ]
        for s in suits
    ]

# Print the result of the deck function with descending order
print(deck(suits, ranks, reverse=True))

# Question 3
# Suppose we are given some data consisting of symbols (the keys in the dictionary) 
# and values being a tuple containing Open/High/Low/Close values for that symbol.

data = {
    'S1': (100, 200, 80, 180),
    'S2': (10, 20, 8, 18),
    'S3': (50, 150, 50, 150)
}

# Function to find the symbol with either the smallest or largest high/low difference
def find_min_max(d, *, is_min=True):
    if is_min:
        return min(d, key=lambda key: data[key][1] - data[key][2])
    else:
        return max(d, key=lambda key: data[key][1] - data[key][2])

# Print the result of finding the max high/low difference
print(find_min_max(data, is_min=False))

# Question 4
# Given data might look like this:
quotes = [
    ('AACC', 6.05, 6.07, 6.03, 6.05, 65800),
    ('AAME', 1.7, 1.82, 1.7, 1.82, 4300),
    ('AAON', 24.98, 25.07, 24.9, 24.94, 28200),
    # ... (more data entries)
]

# Function to filter rows where the close value is more than a certain percentage away from the high value
def more_than(threshold):
    percent = threshold * 0.01
    def predicate(data):
        return abs(data[4] - data[2]) / data[2] > percent
    return predicate

# Use the filter function to generate a list of rows
print(list(filter(more_than(5), quotes)))

# Example to demonstrate filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list = list(even_numbers)

# Print the even numbers
print(even_numbers_list)
