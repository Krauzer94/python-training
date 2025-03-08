# Question 1
# Given these two lists:
widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]

# Function to generate a dictionary using zip
# The keys are from `widgets` and values from `skus`
def format_zip(widgets, skus):
    return dict(zip(widgets, skus))

# Printing the resulting dictionary
if __name__ == "__main__":
    from pprint import pprint
    pprint(format_zip(widgets, skus))

# Question 2
# Given the following data:
suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

# Function to generate all 52 playing cards as tuples (rank, suit)
def deck(suits, ranks):
    return [[(rank, suit) for rank in ranks] for suit in suits]

# Printing the deck
if __name__ == "__main__":
    pprint(deck(suits, ranks))

# Question 3
# Function to sort a list of numbers and return the sorted list,
# along with the minimum and maximum values
def ordering_numbers(numbers_list, *, reverse=False):
    sorted_numbers = sorted(numbers_list, reverse=reverse)
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    return sorted_numbers, min_value, max_value

# Example usage
if __name__ == "__main__":
    list_numbers = [1, 2, 3]
    sorted_nums, min_val, max_val = ordering_numbers(list_numbers, reverse=True)
    print(f"Sorted numbers: {sorted_nums}\nMinimum: {min_val}\nMaximum: {max_val}")

# Additional example: Finding the minimum value of an array
if __name__ == "__main__":
    original_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    minimum_value = min(original_array)
    print(minimum_value)
