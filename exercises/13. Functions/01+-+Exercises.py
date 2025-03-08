from collections import Counter

def arguments_average(*arguments):
    if not arguments:
        raise ValueError('No arguments: minimum of one')
    
    print(f'Arguments: {arguments}')
    average = sum(arguments) / len(arguments)
    print(f'Average: {average}')
    return average

# Example usage
arguments_average(5, 10, 15)


def separator(*, string_arg='-', repetitions=10):
    return string_arg * repetitions

# Example usage
print(separator(string_arg='+', repetitions=50))


unique_count = lambda x: len(set(x.lower())) if x else 0

# Example usage
print(unique_count('The quick brown fox jumps over the lazy dog')) # Expected output: 26


def get_unique_letters_ordered(input_string):
    seen = set()
    unique_letters = []
    
    for char in input_string:
        if char not in seen:
            unique_letters.append(char)
            seen.add(char)
    
    return "".join(unique_letters)

# Example usage
original_string = "programming"
result_ordered = get_unique_letters_ordered(original_string)
print(result_ordered)


def words_frequency(words=''):
    cleaned_words = words.replace(',', ' ').replace('.', ' ').split()
    return dict(Counter(cleaned_words))

# Example usage
sentence = 'This is the first sentence. This is the second sentence. This is not the fourth sentence, it is the third sentence.'
print(words_frequency(sentence))
